import asyncio, json, pathlib, re, time, urllib.request
import requests, websockets
PORT = 9334
ROOT = pathlib.Path('/Users/beemo/.hermes/money_ops/money_flow')
OID = 'opp_20260516_017_clinic_vacation_notice_blog'
OPP_DIR = ROOT / 'opportunities' / OID
ASSETS = OPP_DIR / 'assets'
MD = ASSETS / 'draft_clinic_vacation_notice_20260516_revised.md'
HTML = ASSETS / 'clinic_vacation_notice_tistory_body.html'
TITLE = MD.read_text(encoding='utf-8').splitlines()[0].replace('# ', '').strip()
TAGS = '병원운영,휴진안내,여름휴가공지,치과운영,예약변경문구,병원문자,소상공인'
PNG_FILES = [
    ASSETS / '01-thumbnail-clinic-vacation.png',
    ASSETS / '02-sms-clinic-vacation.png',
    ASSETS / '03-checklist-clinic-vacation.png',
]
async def cdp_call(ws, method, params=None, timeout=12):
    cdp_call.i += 1
    await ws.send(json.dumps({'id': cdp_call.i, 'method': method, 'params': params or {}}))
    while True:
        msg = json.loads(await asyncio.wait_for(ws.recv(), timeout=timeout))
        if msg.get('id') == cdp_call.i:
            return msg
cdp_call.i = 0
async def get_cookies():
    for _ in range(10):
        try:
            tabs = json.load(urllib.request.urlopen(f'http://127.0.0.1:{PORT}/json', timeout=3)); break
        except Exception: time.sleep(1)
    else:
        raise RuntimeError('CDP port not ready')
    tab = next((t for t in tabs if t.get('type')=='page' and 'tistory.com' in t.get('url','')), None) or next(t for t in tabs if t.get('type')=='page')
    async with websockets.connect(tab['webSocketDebuggerUrl'], max_size=None) as ws:
        await cdp_call(ws,'Network.enable')
        ck = await cdp_call(ws,'Network.getAllCookies')
    return ck['result']['cookies']
def session_from_cookies(cookies):
    s=requests.Session()
    s.headers.update({'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 15_7_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148 Safari/537.36','Accept':'application/json, text/plain, */*','Referer':'https://beemo.tistory.com/manage/newpost','Origin':'https://beemo.tistory.com'})
    for c in cookies:
        s.cookies.set(c['name'], c['value'], domain=c.get('domain'), path=c.get('path','/'))
    return s
def md_slug(title):
    s=re.sub(r'[^0-9A-Za-z가-힣\s-]+','',title).strip(); s=re.sub(r'\s+','-',s); return s[:180] or 'post'
def main():
    s=session_from_cookies(asyncio.run(get_cookies()))
    r=s.get('https://beemo.tistory.com/manage/newpost', timeout=20)
    r.raise_for_status()
    if ('post-editor' not in r.text and 'needCaptcha' not in r.text) or 'login' in r.url.lower():
        raise RuntimeError('newpost HTML sanity failed; not marking AUTH_BLOCKED without Profile 2 review')
    posts=s.get('https://beemo.tistory.com/manage/posts', timeout=20); posts.raise_for_status()
    if TITLE in posts.text:
        m=re.search(r'https://beemo\.tistory\.com/(\d+)', posts.text) or re.search(r'href="/(\d+)"', posts.text)
        url=(m.group(0) if m and m.group(0).startswith('http') else ('https://beemo.tistory.com/'+m.group(1) if m else ''))
        print(json.dumps({'status':'DUPLICATE_POSSIBLE','title':TITLE,'url':url}, ensure_ascii=False)); return
    uploads=[]
    for p in PNG_FILES:
        with p.open('rb') as f:
            u=s.post('https://beemo.tistory.com/manage/post/attach.json', files={'file':(p.name,f,'image/png')}, timeout=40)
        print('UPLOAD_STATUS', p.name, u.status_code, u.text[:160].replace('\n',' '))
        u.raise_for_status(); uploads.append(u.json())
    body=HTML.read_text(encoding='utf-8')
    urls=re.findall(r'https://bmoh95\.github\.io/money-flow-dashboard-public/artifacts/'+OID+r'/[^"\s<>]+?\.png(?:\?v=\d+)?', body)
    print('PUBLIC_URL_COUNT', len(urls))
    for old, up in zip(urls, uploads):
        body=body.replace(old, up['url'])
    thumb=f"kage@{uploads[0]['key']}/{uploads[0]['filename']}"
    payload={'id':'0','title':TITLE,'content':body,'slogan':md_slug(TITLE),'visibility':'20','category':'','tag':TAGS,'acceptComment':'1','published':'1','password':'','uselessMarginForEntry':'1','daumLike':'','cclCommercial':'0','cclDerive':'0','thumbnail':thumb,'type':'post','attachments':[],'recaptchaValue':'','draftSequence':'','totalWritingTimeMs':'200000'}
    pr=s.post('https://beemo.tistory.com/manage/post.json', json=payload, timeout=40)
    print('POST_STATUS', pr.status_code, pr.text[:500].replace('\n',' ')); pr.raise_for_status()
    pdata=pr.json(); url=pdata.get('entryUrl') or pdata.get('url') or ''
    if url and url.startswith('/'): url='https://beemo.tistory.com'+url
    if not url:
        latest=s.get('https://beemo.tistory.com/manage/posts', timeout=20).text
        if TITLE not in latest: raise RuntimeError('published but not found in manage list')
        m=re.search(r'https://beemo\.tistory\.com/(\d+)', latest) or re.search(r'href="/(\d+)"', latest)
        url=(m.group(0) if m and m.group(0).startswith('http') else ('https://beemo.tistory.com/'+m.group(1) if m else ''))
    if not url: raise RuntimeError('published but public URL not found')
    vr=s.get(url, timeout=30)
    og=re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)', vr.text)
    ok=vr.status_code==200 and TITLE in vr.text and uploads[0]['filename'] in vr.text and bool(og)
    print(json.dumps({'status':'PUBLISHED_VERIFIED' if ok else 'PUBLISHED_VERIFY_WEAK','url':url,'http':vr.status_code,'title_found':TITLE in vr.text,'first_image_filename_found':uploads[0]['filename'] in vr.text,'upload_count':len(uploads),'thumbnail':thumb,'og_image':og.group(1) if og else ''}, ensure_ascii=False))
    if not ok: raise RuntimeError('public verification failed')
if __name__=='__main__': main()
