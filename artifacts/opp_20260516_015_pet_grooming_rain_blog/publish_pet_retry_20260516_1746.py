import asyncio, json, urllib.request, pathlib, re, sys, time
import websockets
PORT=9334
ROOT=pathlib.Path('/Users/beemo/.hermes/money_ops/money_flow')
OID='opp_20260516_015_pet_grooming_rain_blog'
MD=ROOT/'opportunities'/OID/'assets'/'draft_pet_grooming_rainy_booking_20260516_revised.md'
HTML=ROOT/'opportunities'/OID/'assets'/'pet_grooming_rain_tistory_body.html'
TITLE=MD.read_text(encoding='utf-8').splitlines()[0].replace('# ','').strip()
BODY=HTML.read_text(encoding='utf-8')
TAGS='애견미용,펫살롱,장마철예약,예약변경문구,반려동물미용,카톡문구,소상공인'
async def cdp(tab):
    ws=await websockets.connect(tab['webSocketDebuggerUrl'], max_size=80_000_000, open_timeout=5)
    seq=0
    async def call(method, params=None, timeout=25):
        nonlocal seq
        seq+=1
        await ws.send(json.dumps({'id':seq,'method':method,'params':params or {}}))
        while True:
            msg=json.loads(await asyncio.wait_for(ws.recv(),timeout=timeout))
            if msg.get('id')==seq: return msg
    return ws, call
async def evaljs(call, expr, timeout=25, awaitPromise=False):
    msg=await call('Runtime.evaluate', {'expression':expr,'returnByValue':True,'awaitPromise':awaitPromise}, timeout=timeout)
    if 'exceptionDetails' in msg.get('result',{}):
        return {'__exception__': msg['result']['exceptionDetails']}
    return msg.get('result',{}).get('result',{}).get('value')
async def main():
    tabs=json.load(urllib.request.urlopen(f'http://127.0.0.1:{PORT}/json',timeout=5))
    # choose a clean /manage/newpost tab, not edit post tab
    pages=[t for t in tabs if t.get('type')=='page']
    tab=next((t for t in pages if t.get('url','').rstrip('/')=='https://beemo.tistory.com/manage/newpost'), None)
    if not tab:
        tab=next((t for t in pages if 'tistory.com' in t.get('url','')), pages[0])
    ws, call = await cdp(tab)
    try:
        await call('Page.enable'); await call('Runtime.enable')
        # login check
        await call('Page.navigate', {'url':'https://www.tistory.com/'}, timeout=10)
        await asyncio.sleep(2.5)
        home=await evaljs(call, '({url:location.href,title:document.title,text:document.body.innerText.slice(0,2200), beemo:document.body.innerText.includes("beemo"), write:document.body.innerText.includes("글쓰기")||document.body.innerText.includes("쓰기"), manage:document.body.innerText.includes("관리")})')
        print('HOME', json.dumps(home,ensure_ascii=False))
        if '로그인' in (home.get('text') or '') and not (home.get('beemo') or home.get('write') or home.get('manage')):
            print(json.dumps({'status':'AUTH_BLOCKED','stage':'home'},ensure_ascii=False)); return
        # duplicate check
        await call('Page.navigate', {'url':'https://beemo.tistory.com/manage/posts'}, timeout=10)
        await asyncio.sleep(3)
        posts=await evaljs(call, f'({{url:location.href,title:document.title,text:document.body.innerText.slice(0,6000), duplicate:document.body.innerText.includes({json.dumps(TITLE,ensure_ascii=False)})}})')
        print('POSTS', json.dumps({'url':posts.get('url'), 'duplicate':posts.get('duplicate')},ensure_ascii=False))
        if posts.get('duplicate'):
            print(json.dumps({'status':'DUPLICATE_POSSIBLE','stage':'manage_posts'},ensure_ascii=False)); return
        await call('Page.navigate', {'url':'https://beemo.tistory.com/manage/newpost'}, timeout=10)
        await asyncio.sleep(6)
        state=await evaljs(call, '({url:location.href,title:document.title,ready:document.readyState,text:document.body.innerText.slice(0,1600),hasTitle:!!document.querySelector("#post-title-inp"),hasTiny:!!window.tinymce,hasPub:!!document.querySelector("#publish-layer-btn")})')
        print('STATE', json.dumps(state,ensure_ascii=False))
        if not state.get('hasTitle') or not state.get('hasTiny'):
            print(json.dumps({'status':'EDITOR_AUTOMATION_BLOCKED','stage':'state','state':state},ensure_ascii=False)); return
        js=f"""
        (()=>{{
          window.onbeforeunload=null;
          const title={json.dumps(TITLE,ensure_ascii=False)};
          const html={json.dumps(BODY,ensure_ascii=False)};
          const tags={json.dumps(TAGS,ensure_ascii=False)};
          const t=document.querySelector('#post-title-inp');
          const setter=Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype,'value').set;
          setter.call(t,title); t.dispatchEvent(new Event('input',{{bubbles:true}})); t.dispatchEvent(new Event('change',{{bubbles:true}}));
          if(window.tinymce&&tinymce.activeEditor){{tinymce.activeEditor.setContent(html); tinymce.activeEditor.fire('change'); tinymce.activeEditor.save();}}
          const ed=document.querySelector('#editor-tistory'); if(ed){{ed.value=html; ed.dispatchEvent(new Event('input',{{bubbles:true}})); ed.dispatchEvent(new Event('change',{{bubbles:true}}));}}
          const tag=document.querySelector('#tagText'); if(tag){{tag.focus(); tag.value=tags; tag.dispatchEvent(new Event('input',{{bubbles:true}})); tag.dispatchEvent(new Event('change',{{bubbles:true}}));}}
          const content=(window.tinymce&&tinymce.activeEditor)?tinymce.activeEditor.getContent():'';
          return {{title:t.value, len:content.length, imgCount:(content.match(/<img/g)||[]).length, png:content.includes('.png?v=202605161745'), risk:content.includes('의료·법률 판단이 아니라')&&content.includes('예약 시 고지한 본인 샵 기준')}};
        }})()
        """
        fill=await evaljs(call, js, timeout=30)
        print('FILL', json.dumps(fill,ensure_ascii=False))
        if fill.get('imgCount')!=3 or not fill.get('png') or not fill.get('risk') or fill.get('title')!=TITLE:
            print(json.dumps({'status':'EDITOR_AUTOMATION_BLOCKED','stage':'editor_qa','fill':fill},ensure_ascii=False)); return
        # publish
        pubjs="""
        (async()=>{
          window.onbeforeunload=null;
          document.querySelector('#publish-layer-btn')?.click();
          await new Promise(r=>setTimeout(r,1800));
          const open=document.querySelector('#open20'); if(open) open.click();
          await new Promise(r=>setTimeout(r,800));
          const btn=document.querySelector('#publish-btn'); const txt=btn?btn.innerText:''; if(btn) btn.click();
          return {clicked:!!btn, btnText:txt, url:location.href};
        })()
        """
        try:
            pub=await evaljs(call, pubjs, timeout=35, awaitPromise=True)
            print('PUB', json.dumps(pub,ensure_ascii=False))
        except Exception as e:
            print('PUB_EXCEPTION', repr(e))
        await asyncio.sleep(12)
    finally:
        try: await ws.close()
        except Exception: pass
    # reconnect to any tistory tab and inspect manage posts for title/url
    tabs=json.load(urllib.request.urlopen(f'http://127.0.0.1:{PORT}/json',timeout=5))
    tab=next((t for t in tabs if t.get('type')=='page' and 'tistory.com' in t.get('url','')), None)
    if not tab:
        print(json.dumps({'status':'VERIFY_BLOCKED','stage':'no_tab'},ensure_ascii=False)); return
    ws, call = await cdp(tab)
    try:
        await call('Page.enable'); await call('Runtime.enable')
        await call('Page.navigate', {'url':'https://beemo.tistory.com/manage/posts'}, timeout=10)
        await asyncio.sleep(4)
        expr=f'''(()=>{{
          const title={json.dumps(TITLE,ensure_ascii=False)};
          const text=document.body.innerText.slice(0,8000);
          const links=[...document.querySelectorAll('a')].map(a=>({{text:a.innerText,href:a.href}}));
          const hit=links.find(a=>a.text.includes(title)||a.text.includes(title.slice(0,15)))||null;
          return {{url:location.href, hasTitle:text.includes(title), hit}};
        }})()'''
        found=await evaljs(call, expr, timeout=25)
        print('VERIFY_POSTS', json.dumps(found,ensure_ascii=False))
    finally:
        try: await ws.close()
        except Exception: pass
asyncio.run(main())
