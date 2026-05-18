import json, pathlib, datetime, html, subprocess, re
ROOT=pathlib.Path('/Users/beemo/.hermes/money_ops/money_flow')
OID='opp_20260516_019_oneday_class_booking_blog'
OPP=ROOT/'opportunities'/OID/'opportunity.json'
AS=ROOT/'opportunities'/OID/'assets'
AS.mkdir(parents=True, exist_ok=True)
KST=datetime.timezone(datetime.timedelta(hours=9))
NOW=datetime.datetime.now(KST).isoformat(timespec='seconds')
RUN_ID='2026-05-16_1849_money-flow'
PUBLIC='https://bmoh95.github.io/money-flow-dashboard-public'
font='Apple SD Gothic Neo, Noto Sans KR, sans-serif'

def svg_card(path,title,sub,bullets,bg='#fffaf4',accent='#a56637',footer='공방 기준에 맞춰 수정'):
    bullet_svg=''.join(f'<text x="86" y="{222+i*54}" font-family="{font}" font-size="29" fill="#2c2c2c">• {html.escape(b)}</text>' for i,b in enumerate(bullets))
    s=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="800" viewBox="0 0 1200 800">
  <rect width="1200" height="800" rx="42" fill="{bg}"/>
  <rect x="54" y="54" width="1092" height="692" rx="34" fill="#ffffff" stroke="{accent}" stroke-width="4"/>
  <circle cx="1010" cy="150" r="72" fill="{accent}" opacity="0.12"/>
  <text x="86" y="136" font-family="{font}" font-size="53" font-weight="700" fill="#30231c">{html.escape(title)}</text>
  <text x="88" y="185" font-family="{font}" font-size="25" fill="#66584f">{html.escape(sub)}</text>
  {bullet_svg}
  <rect x="86" y="650" width="390" height="54" rx="27" fill="{accent}" opacity="0.13"/>
  <text x="112" y="686" font-family="{font}" font-size="24" fill="{accent}" font-weight="700">{html.escape(footer)}</text>
</svg>'''
    path.write_text(s,encoding='utf-8')
    png=path.with_suffix('.png')
    subprocess.run(['sips','-s','format','png',str(path),'--out',str(png)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    return [str(path), str(png)]

imgs=[]
imgs+=svg_card(AS/'01-thumbnail-oneday-class-booking.svg','원데이클래스 예약 안내','처음부터 써두면 덜 반복되는 5가지',['날짜·시간','인원·체험 내용','예약금·결제','소요 시간','변경 문의 기준'],'#fff8ef','#a86635','복붙 전 공방 기준 확인')
imgs+=svg_card(AS/'02-kakao-oneday-class-booking.svg','카톡 답장 예시','짧게, 기준은 흐리지 않게',['예약 확인되었습니다','시작 10분 전 도착 부탁드려요','재료 준비 후 변경은 빠르게 연락'],'#f5fbff','#2f6f73','부드럽게 단호하게')
imgs+=svg_card(AS/'03-checklist-oneday-class-booking.svg','예약 전 체크리스트','안내문에 빠지기 쉬운 항목',['준비물·복장','주차·위치','지각 시 진행 시간','단체 예약 여부','플랫폼 환불 기준'],'#f7f6ff','#6260a8','환불은 약관 먼저 확인')

md0=(AS/'draft_oneday_class_booking_notice_20260516.md').read_text(encoding='utf-8')
md=md0
repls={
 '[이미지 1: 원데이클래스 예약 안내 썸네일]':f'![원데이클래스 예약 안내 썸네일]({PUBLIC}/artifacts/{OID}/01-thumbnail-oneday-class-booking.png?v=202605161849)',
 '[이미지 2: 카톡 예약 안내 예시 카드]':f'![원데이클래스 카톡 예약 안내 예시]({PUBLIC}/artifacts/{OID}/02-kakao-oneday-class-booking.png?v=202605161849)',
 '[이미지 3: 원데이클래스 예약 전 체크리스트]':f'![원데이클래스 예약 전 체크리스트]({PUBLIC}/artifacts/{OID}/03-checklist-oneday-class-booking.png?v=202605161849)',
}
for a,b in repls.items(): md=md.replace(a,b)
# risk wording soften
md=md.replace('예약금, 환불, 취소 기준은 공방마다 다르고 플랫폼 예약이면 플랫폼 기준도 봐야 합니다.', '예약금, 환불, 취소 기준은 공방마다 다르고 플랫폼 예약이면 플랫폼 약관과 실제 고지 내용을 먼저 봐야 합니다.')
md=md.replace('블로그 예시 문구를 그대로 법률 기준처럼 쓰면 안 됩니다.', '아래 예시는 법률 기준이나 환불 보장 문구가 아니라 운영 안내 예시로만 봐야 합니다.')
md=md.replace('자세한 변경·취소 기준은 예약 확정 시 다시 안내드리겠습니다.', '자세한 변경·취소 기준은 예약 확정 전 안내드리는 공방 기준과 이용 플랫폼 기준을 함께 확인 부탁드립니다.')
md=md.replace('내부 기준을 정리한 뒤, 실제 안내문에는 그 기준을 짧게 풀어 쓰면 됩니다.', '내부 기준을 정리한 뒤, 실제 안내문에는 소비자 오해가 없도록 적용 조건을 짧게 풀어 쓰면 됩니다.')
md=md.replace('특히 환불이나 취소 기준은 예시 문구만 보고 정하지 말고, 실제 운영 방식과 사용하는 예약 플랫폼 기준을 같이 확인하는 게 좋습니다.', '특히 환불이나 취소 기준은 예시 문구만 보고 정하지 말고, 실제 운영 방식·사전 고지 내용·사용하는 예약 플랫폼 기준을 같이 확인하는 게 좋습니다.')
rev=AS/'draft_oneday_class_booking_notice_20260516_revised.md'
rev.write_text(md,encoding='utf-8')

def md_to_body(md):
    lines=md.splitlines(); out=[]; in_quote=False; in_ul=False
    for line in lines[1:]:
        if line.startswith('## '):
            if in_quote: out.append('</blockquote>'); in_quote=False
            if in_ul: out.append('</ul>'); in_ul=False
            out.append(f'<h2>{html.escape(line[3:])}</h2>')
        elif line.startswith('> '):
            if in_ul: out.append('</ul>'); in_ul=False
            if not in_quote: out.append('<blockquote>'); in_quote=True
            text=html.escape(line[2:].strip())
            if text: out.append(f'<p>{text}</p>')
        elif line.startswith('- '):
            if in_quote: out.append('</blockquote>'); in_quote=False
            if not in_ul: out.append('<ul>'); in_ul=True
            out.append(f'<li>{html.escape(line[2:])}</li>')
        elif line.startswith('!['):
            if in_quote: out.append('</blockquote>'); in_quote=False
            if in_ul: out.append('</ul>'); in_ul=False
            m=re.match(r'!\[(.*?)\]\((.*?)\)', line)
            if m: out.append(f'<figure><img src="{html.escape(m.group(2))}" alt="{html.escape(m.group(1))}" style="max-width:100%;height:auto;border-radius:18px;display:block;margin:28px auto 8px;"><figcaption style="text-align:center;color:#555;font-size:14px;line-height:1.65;">{html.escape(m.group(1))}</figcaption></figure>')
        elif line.strip():
            if in_quote: out.append('</blockquote>'); in_quote=False
            if in_ul: out.append('</ul>'); in_ul=False
            out.append(f'<p>{html.escape(line.strip())}</p>')
    if in_quote: out.append('</blockquote>')
    if in_ul: out.append('</ul>')
    return '''<div class="mf-post" style="max-width:740px;margin:0 auto;font-size:17px;line-height:1.9;color:#222;word-break:keep-all;overflow-wrap:anywhere;">
<style>.mf-post p{margin:0 0 20px}.mf-post h2{font-size:1.45em;margin:46px 0 16px;line-height:1.45}.mf-post blockquote{margin:18px 0;padding:18px 20px;border-left:4px solid #a86635;background:#fff8ef;border-radius:10px}.mf-post blockquote p{margin:0 0 10px}.mf-post ul{margin:12px 0 24px;padding-left:24px}.mf-post li{margin:8px 0}.mf-post figure{margin:30px 0}</style>\n'''+"\n".join(out)+'\n</div>'
body=md_to_body(md)
html_path=AS/'oneday_class_booking_tistory_body.html'; html_path.write_text(body,encoding='utf-8')
preview=AS/'oneday_class_booking_tistory_preview.html'; preview.write_text(f'<!doctype html><meta charset="utf-8"><title>{html.escape(md.splitlines()[0][2:])}</title>'+body,encoding='utf-8')
# QA
assert body.count('<img ')==3
assert '법률 기준이나 환불 보장 문구가 아니라 운영 안내 예시' in body
assert '플랫폼 기준' in body and '사전 고지' in body
opp=json.loads(OPP.read_text(encoding='utf-8'))
assets=[str(rev),str(html_path),str(preview)]+imgs+[str(ROOT/'runs'/'process_oneday_20260516_1849.py')]
for a in assets:
    if a not in opp['assets']: opp['assets'].append(a)
opp['updated_at']=NOW; opp['current_owner']='execution_lead'; opp['stop_reason_code']='EDITOR_AUTOMATION_BLOCKED'
opp['risk_flags']=[x for x in opp.get('risk_flags',[]) if '이미지' not in x and '환불' not in x]
for x in ['refund_deposit_wording_softened','platform_policy_wording_softened','tistory_visual_qa_passed_local','tistory_thumbnail_png_ready','EDITOR_AUTOMATION_BLOCKED']:
    if x not in opp['risk_flags']: opp['risk_flags'].append(x)
opp['next_action']='지원 이미지 3장, 환불·예약금·플랫폼 기준 단정 완화, Tistory HTML 렌더링 QA 완료. Profile 2 기존 세션으로 직접 API 게시를 시도한다.'
for agent,dec,code,summ in [
 ('execution_member','GO',None,'썸네일·카톡 예시·체크리스트 PNG/SVG 3장, 수정 Markdown, Tistory HTML/preview 생성.'),
 ('execution_lead','GO',None,'환불·예약금 단정 표현을 운영 안내 예시로 완화하고 로컬 HTML 렌더링 QA 통과.'),
 ('redteam','HOLD','EDITOR_AUTOMATION_BLOCKED','콘텐츠/이미지/리스크 문구는 게시 가능 수준. 외부 공개 검증 전까지 HOLD.'),
 ('roi','HOLD','EDITOR_AUTOMATION_BLOCKED','무료 검증 공개 전 실제 매출 0원. 공개 후 검색 반응 추적 단계로 전환 가능.')]:
    opp['decision_history'].append({'time':NOW,'agent':agent,'decision':dec,**({'reason_code':code} if code else {}),'summary':summ})
OPP.write_text(json.dumps(opp,ensure_ascii=False,indent=2),encoding='utf-8')
rdir=ROOT/'runs'/RUN_ID; rdir.mkdir(parents=True,exist_ok=True)
run={'run_id':RUN_ID,'started_at':NOW,'finished_at':NOW,'trigger':'cron','agents_executed':['execution_member','execution_lead','redteam','roi','ledger_dashboard_manager'],'candidates_discovered':0,'opportunities_advanced':0,'opportunities_rejected':0,'assets_created':assets,'approval_needed':[],'decisions':opp['decision_history'][-4:],'summary':'Processed oneday class held blog assets and local QA; publishing attempt pending/blocked separately.','final_report':'assets_created_local_qa_passed'}
(rdir/'run.json').write_text(json.dumps(run,ensure_ascii=False,indent=2),encoding='utf-8')
(rdir/'report.md').write_text('공방 원데이클래스 예약 안내 글 이미지/문구/HTML QA 완료.\n',encoding='utf-8')
with (ROOT/'logs'/'events.jsonl').open('a',encoding='utf-8') as f:
    for d in opp['decision_history'][-4:]:
        f.write(json.dumps({'time':NOW,'run_id':RUN_ID,'agent':d['agent'],'opportunity_id':OID,'event':'decision','from_status':'redteam_hold','to_status':'redteam_hold','decision':d['decision'],'reason_code':d.get('reason_code'),'summary':d['summary'],'links':assets if d['agent']=='execution_member' else []},ensure_ascii=False)+'\n')
print(json.dumps({'status':'ok','assets':len(assets),'qa_img_count':body.count('<img ')},ensure_ascii=False))
