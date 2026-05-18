import asyncio,json,pathlib,re,urllib.request,requests,websockets
PORT=9334
POST_ID='16'
ROOT=pathlib.Path('/Users/beemo/.hermes/money_ops/money_flow')
OID='opp_20260516_016_cafe_summer_menu_blog'
ASSETS=ROOT/'opportunities'/OID/'assets'
TITLE=(ASSETS/'draft_cafe_summer_menu_notice_20260516_revised.md').read_text(encoding='utf-8').splitlines()[0].replace('# ','').strip()
BODY=(ASSETS/'cafe_summer_menu_tistory_body.html').read_text(encoding='utf-8')
TAGS='카페운영,시즌메뉴,품절안내,알레르기안내,카톡문구,소상공인,여름메뉴'
PNGS=[ASSETS/'01-thumbnail-cafe-summer-menu.png',ASSETS/'02-menu-notice-cafe-summer.png',ASSETS/'03-checklist-cafe-summer.png']
async def call(ws,m,p=None,timeout=10):
    call.i+=1; await ws.send(json.dumps({'id':call.i,'method':m,'params':p or {}}))
    while True:
        msg=json.loads(await asyncio.wait_for(ws.recv(),timeout))
        if msg.get('id')==call.i: return msg
call.i=0
async def cookies():
    tabs=json.load(urllib.request.urlopen(f'http://127.0.0.1:{PORT}/json'))
    tab=next((t for t in tabs if t.get('type')=='page' and 'tistory.com' in t.get('url','')),None) or next(t for t in tabs if t.get('type')=='page')
    async with websockets.connect(tab['webSocketDebuggerUrl'],max_size=None) as ws:
        await call(ws,'Network.enable'); ck=await call(ws,'Network.getAllCookies')
    return ck['result']['cookies']
def sess():
    s=requests.Session(); s.headers.update({'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 15_7_4) AppleWebKit/537.36','Accept':'application/json, text/plain, */*','Referer':f'https://beemo.tistory.com/manage/post/{POST_ID}','Origin':'https://beemo.tistory.com'})
    for c in asyncio.run(cookies()): s.cookies.set(c['name'],c['value'],domain=c.get('domain'),path=c.get('path','/'))
    return s
def slug(t):
    s=re.sub(r'[^0-9A-Za-z가-힣\s-]+','',t).strip(); return re.sub(r'\s+','-',s)[:180]
s=sess()
ups=[]
for p in PNGS:
    with p.open('rb') as f:
        r=s.post('https://beemo.tistory.com/manage/post/attach.json',files={'file':(p.name,f,'image/png')},timeout=40)
    print('UPLOAD',p.name,r.status_code,r.text[:120].replace('\n',' '))
    r.raise_for_status(); ups.append(r.json())
urls=re.findall(r'https://bmoh95\.github\.io/money-flow-dashboard-public/artifacts/'+OID+r'/[^"\s<>]+?\.(?:svg|png)(?:\?v=\d+)?', BODY)
print('REPLACE_URLS',len(urls))
for old,up in zip(urls,ups): BODY=BODY.replace(old,up['url'])
thumb=f"kage@{ups[0]['key']}/{ups[0]['filename']}"
p={'id':POST_ID,'title':TITLE,'content':BODY,'slogan':slug(TITLE),'visibility':'20','category':'','tag':TAGS,'acceptComment':'1','published':'1','password':'','uselessMarginForEntry':'1','daumLike':'','cclCommercial':'0','cclDerive':'0','thumbnail':thumb,'type':'post','attachments':[],'recaptchaValue':'','draftSequence':'','totalWritingTimeMs':'200000'}
r=s.put(f'https://beemo.tistory.com/manage/post/{POST_ID}.json',json=p,timeout=40)
print('PUT',r.status_code,r.text[:500].replace('\n',' ')); r.raise_for_status()
url='https://beemo.tistory.com/16'
vr=s.get(url,timeout=30)
imgs=re.findall(r'<img[^>]+src=["\']([^"\']+)',vr.text)
og=re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)',vr.text)
ok=vr.status_code==200 and TITLE in vr.text and len(imgs)>=3 and all(u['filename'] in vr.text for u in ups[:3]) and bool(og)
print(json.dumps({'status':'UPDATED_VERIFIED' if ok else 'VERIFY_WEAK','url':url,'http':vr.status_code,'title_found':TITLE in vr.text,'uploaded_image_filenames_found':[u['filename'] in vr.text for u in ups],'img_count':len(imgs),'og_image':og.group(1) if og else '', 'thumbnail':thumb},ensure_ascii=False))
if not ok: raise RuntimeError('update verification weak')
