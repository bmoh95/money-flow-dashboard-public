import asyncio, json, pathlib, re, time, urllib.request
from datetime import datetime, timezone, timedelta
import requests, websockets

PORT = 9334
ROOT = pathlib.Path('/Users/beemo/.hermes/money_ops/money_flow')
OID = 'opp_20260516_015_pet_grooming_rain_blog'
OPP_DIR = ROOT / 'opportunities' / OID
ASSETS = OPP_DIR / 'assets'
MD = ASSETS / 'draft_pet_grooming_rainy_booking_20260516_revised.md'
HTML = ASSETS / 'pet_grooming_rain_tistory_body.html'
TITLE = MD.read_text(encoding='utf-8').splitlines()[0].replace('# ', '').strip()
TAGS = '애견미용,펫살롱,장마철예약,예약변경문구,반려동물미용,카톡문구,소상공인'
PNG_FILES = [
    ASSETS / '01-thumbnail-pet-rain.png',
    ASSETS / '02-kakao-pet-rain.png',
    ASSETS / '03-checklist-pet-rain.png',
]

async def cdp_call(ws, method, params=None, timeout=12):
    cdp_call.i += 1
    await ws.send(json.dumps({'id': cdp_call.i, 'method': method, 'params': params or {}}))
    while True:
        msg = json.loads(await asyncio.wait_for(ws.recv(), timeout=timeout))
        if msg.get('id') == cdp_call.i:
            return msg
cdp_call.i = 0

async def get_cdp_cookies():
    for _ in range(12):
        try:
            tabs = json.load(urllib.request.urlopen(f'http://127.0.0.1:{PORT}/json', timeout=3))
            break
        except Exception:
            time.sleep(1)
    else:
        raise RuntimeError('CDP port not ready')
    tab = next(t for t in tabs if t.get('type') == 'page')
    async with websockets.connect(tab['webSocketDebuggerUrl'], max_size=None) as ws:
        await cdp_call(ws, 'Network.enable')
        await cdp_call(ws, 'Runtime.enable')
        login = await cdp_call(ws, 'Runtime.evaluate', {
            'expression': 'document.body.innerText.includes("알림") && !document.body.innerText.includes("시작하기")',
            'returnByValue': True,
        })
        ok = login.get('result', {}).get('result', {}).get('value')
        if not ok:
            raise RuntimeError('Tistory login not confirmed in Profile 2 CDP home')
        ck = await cdp_call(ws, 'Network.getAllCookies')
    return ck['result']['cookies']

def session_from_cookies(cookies):
    s = requests.Session()
    s.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 15_7_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://beemo.tistory.com/manage/newpost',
        'Origin': 'https://beemo.tistory.com',
    })
    for c in cookies:
        s.cookies.set(c['name'], c['value'], domain=c.get('domain'), path=c.get('path', '/'))
    return s

def md_slug(title):
    s = re.sub(r'[^0-9A-Za-z가-힣\s-]+', '', title).strip()
    s = re.sub(r'\s+', '-', s)
    return s[:180] or 'post'

def main():
    cookies = asyncio.run(get_cdp_cookies())
    s = session_from_cookies(cookies)

    # Login/newpost sanity via plain HTTP. Do not print cookies.
    r = s.get('https://beemo.tistory.com/manage/newpost', timeout=20)
    r.raise_for_status()
    if 'needCaptcha: false' not in r.text or 'post-editor' not in r.text:
        raise RuntimeError('newpost HTML sanity failed')

    # Duplicate check on manage list page.
    posts = s.get('https://beemo.tistory.com/manage/posts', timeout=20)
    posts.raise_for_status()
    if TITLE in posts.text:
        print(json.dumps({'status': 'DUPLICATE_POSSIBLE', 'title': TITLE}, ensure_ascii=False))
        return

    uploads = []
    for p in PNG_FILES:
        with p.open('rb') as f:
            files = {'file': (p.name, f, 'image/png')}
            u = s.post('https://beemo.tistory.com/manage/post/attach.json', files=files, timeout=40)
        print('UPLOAD_STATUS', p.name, u.status_code, u.text[:160].replace('\n', ' '))
        u.raise_for_status()
        data = u.json()
        uploads.append(data)

    body = HTML.read_text(encoding='utf-8')
    public_urls = re.findall(r'https://bmoh95\.github\.io/money-flow-dashboard-public/artifacts/opp_20260516_015_pet_grooming_rain_blog/[^"\s<>]+?\.png\?v=202605161745', body)
    for old, up in zip(public_urls, uploads):
        body = body.replace(old, up['url'])

    thumb = f"kage@{uploads[0]['key']}/{uploads[0]['filename']}"
    payload = {
        'id': '0',
        'title': TITLE,
        'content': body,
        'slogan': md_slug(TITLE),
        'visibility': 20,  # public
        'category': 0,
        'tag': TAGS,
        'acceptComment': True,
        'published': 1,
        'password': '',
        'uselessMarginForEntry': True,
        'daumLike': '',
        'cclCommercial': False,
        'cclDerive': False,
        'thumbnail': thumb,
        'type': 'post',
        'attachments': [],
        'recaptchaValue': '',
        'draftSequence': None,
        'totalWritingTimeMs': 180000,
    }
    pr = s.post('https://beemo.tistory.com/manage/post.json', json=payload, timeout=40)
    print('POST_STATUS', pr.status_code, pr.text[:500].replace('\n', ' '))
    pr.raise_for_status()
    pdata = pr.json()
    url = pdata.get('entryUrl') or pdata.get('url') or ''
    if not url:
        # Manage API may redirect URL indirectly; inspect latest posts HTML.
        latest = s.get('https://beemo.tistory.com/manage/posts', timeout=20).text
        m = re.search(r'https://beemo\.tistory\.com/(\d+)', latest)
        url = m.group(0) if m else ''
    if url and url.startswith('/'):
        url = 'https://beemo.tistory.com' + url
    if not url:
        raise RuntimeError('published but public URL not found in response')

    vr = s.get(url, timeout=30)
    ok = vr.status_code == 200 and TITLE in vr.text and uploads[0]['filename'] in vr.text
    print(json.dumps({
        'status': 'PUBLISHED_VERIFIED' if ok else 'PUBLISHED_VERIFY_WEAK',
        'url': url,
        'http': vr.status_code,
        'title_found': TITLE in vr.text,
        'first_image_filename_found': uploads[0]['filename'] in vr.text,
        'upload_count': len(uploads),
        'thumbnail': thumb,
    }, ensure_ascii=False))
    if not ok:
        raise RuntimeError('public verification failed')

if __name__ == '__main__':
    main()
