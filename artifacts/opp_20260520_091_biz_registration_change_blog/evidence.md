# Evidence

- Run: `2026-05-20_1600_money-flow`
- Checked: 2026-05-20T16:09:57+09:00

## Candidate comparison
- **GO / OK** — 사업자등록 정정신고 주소·상호 변경 5분 체크 무료 검증 글 (blog_validation): 정부24/국세청 A급 근거가 있고, 가게 이전·상호 변경 직후 소상공인이 먼저 확인해야 하는 pain이 명확함. 최근 음식점/보험/뉴스 글과 주제가 다르고 세금·장부 카테고리의 실무형 유입 자산.
  - https://www.gov.kr/mw/AA020InfoCappView.do?CappBizCD=12100000073
  - https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2446&cntntsId=7779
  - https://www.gov.kr/mw/AA020InfoCappView.do?HighCtgCD=A09006&CappBizCD=11300000007&tp_seq=01
- **NO-GO / DUPLICATE** — 통신판매업 변경신고만 따로 파는/문구화하는 체크팩 (digital_product): 온라인 판매 신고/통신판매업 registration lane은 기존 `online_sales_registration_blog`와 겹치고, 사용자는 콘텐츠 판매를 중지한 상태. 본 글 안의 해당자 참고 항목으로만 처리.
  - https://www.gov.kr/mw/AA020InfoCappView.do?HighCtgCD=A09006&CappBizCD=11300000007&tp_seq=01
- **HOLD / HIGH_RISK** — 간판 설치 전 옥외광고물 허가·신고 체크 글 (blog_validation): 정부24/법령 근거는 있으나 지자체 조례·광고물 종류·심의 여부 차이가 커서 오늘 신규 persistent 후보로 만들기에는 법령/지역 리스크와 backlog 부담이 더 큼.
  - https://www.gov.kr/mw/AA020InfoCappView.do?HighCtgCD=A09006&CappBizCD=13100000152
- **NO-GO / NO_CHANNEL** — 소상공인 수도요금 감면 신청 정리 글 (blog_validation): 지자체별 대상·기간·신청처 차이가 커 전국형 Tistory 글의 정확도가 낮음. 지역을 특정하지 않으면 채널/독자 fit이 약함.
  - https://i121.seoul.go.kr/cs/cyber/front/cgcalc/NR_chargeReduceInfo.do?_m=m1_6

## A/B sources for GO candidate
- **A** [https://www.gov.kr/mw/AA020InfoCappView.do?CappBizCD=12100000073](https://www.gov.kr/mw/AA020InfoCappView.do?CappBizCD=12100000073) — 정부24 “사업자등록 정정신고, 법인이 아닌 단체의 고유번호 정정신고”. 신청방법 인터넷/방문, 수수료 없음, 상호·사이버몰명/도메인 변경은 즉시(근무시간 내 3시간), 사업장 이전 등은 총 2일, 제출서류는 사업자등록증·임대차계약서 사본(임차 시)·정정사항 서류로 안내.
- **A** [https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2446&cntntsId=7779](https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2446&cntntsId=7779) — 국세청 사업자등록 정정 공식 안내 페이지. 사업자등록 안내 내 정정 항목으로 정부24/홈택스 글의 공식 보강 근거.
- **A** [https://www.gov.kr/mw/AA020InfoCappView.do?HighCtgCD=A09006&CappBizCD=11300000007&tp_seq=01](https://www.gov.kr/mw/AA020InfoCappView.do?HighCtgCD=A09006&CappBizCD=11300000007&tp_seq=01) — 정부24 통신판매업 변경신고. 상호·주소·전화번호·전자우편·도메인 등 신고사항 변경 시 수수료 없음, 국내 주된 사무소 총 3일, 변경사항 증명서류/신고증 원본 등 안내. 해당자만 참고로 제한.
- **B** [https://duckduckgo.com/html/?q=%EC%82%AC%EC%97%85%EC%9E%90%EB%93%B1%EB%A1%9D+%EC%A0%95%EC%A0%95%EC%8B%A0%EA%B3%A0+%EC%A3%BC%EC%86%8C+%EB%B3%80%EA%B2%BD+%EB%B8%94%EB%A1%9C%EA%B7%B8](https://duckduckgo.com/html/?q=%EC%82%AC%EC%97%85%EC%9E%90%EB%93%B1%EB%A1%9D+%EC%A0%95%EC%A0%95%EC%8B%A0%EA%B3%A0+%EC%A3%BC%EC%86%8C+%EB%B3%80%EA%B2%BD+%EB%B8%94%EB%A1%9C%EA%B7%B8) — 사업자등록 주소변경/정정신고 comparable 글 다수. 기존 글은 홈택스 화면 따라하기 또는 세무서비스 CTA가 많아, “이사 직후 먼저 볼 3가지” 구조로 차별화 가능.
- **B** [https://beemo.tistory.com/rss](https://beemo.tistory.com/rss) — 최근 공개글 5개와 비교. 음식점 위생교육/풍수해보험/뉴스 중심이라, 이번 글은 세금·장부 admin lane이지만 “이사/상호 변경 첫 순서”라는 새 상황 예시로 반복을 줄임.

## Sample and anti-repetition notes
# Comparable Sample Brief

## 최근 검증노트 5개 anti-repetition

1. 음식점 위생교육, 올해 들었는지 헷갈릴 때 보는 순서
2. 장마 오기 전에, 소상공인 풍수해보험 먼저 볼 것들
3. 스타벅스 5·18 ‘탱크데이’ 논란 정리: 확인된 사실과 남은 쟁점
4. 옛 전남도청 정식 개관 정리: 5·18 상징 공간에서 확인할 사실
5. GTX 삼성역 철근 누락 정리: 2열 설계가 1열 시공, 남은 쟁점은 검증과 보고입니다

## Anti-repetition answers
- 같은 heading skeleton인가? 아니요. `한눈에/헷갈리는 N가지` 대신 `이사 직후 → 먼저 볼 3가지 → 준비서류 → 해당자만 추가신고` 구조.
- 첫 4문단이 비슷한가? 아니요. 음식점/보험/뉴스 설명이 아니라 매장 이전 후 주소 수정이 꼬이는 장면으로 시작.
- 이미지 레이아웃/색 반복인가? 아니요. 서류 폴더, 분기 흐름, 서류 체크카드로 역할을 나눔.
- 새 유스케이스가 있는가? 예. 사업장 이전·상호 변경 후 사업자등록 정정이라는 세금·장부 실무 상황.

## Comparable patterns
1. **사업자등록증 주소 변경 방법, 홈택스로 5분 만에 끝내기 (2026 ...)** — 홈택스 절차 중심. 빠른 해결 후킹은 좋지만 공식 처리기간/서류 근거가 약함. (https://blog.naver.com/content_office/224184432419)
2. **개인사업자 사업자등록 정정신고 완벽 가이드｜주소 변경 시 ...** — 세무 블로그형. 범위가 넓어 독자가 첫 행동을 고르기 어렵다. (https://thegamtax.tistory.com/2989)
3. **사업자등록증 주소변경 방법｜홈택스, 세무서 절차 완벽 정리** — 검색형 정리. 절차 나열은 많지만 이사 직후 체크 순서가 약함. (https://docuguide.co.kr/사업자등록증-주소변경-방법/)
4. **사업자등록증 주소변경 방법 및 서류 총정리 (+ 홈택스 5분 완정 ...)** — 긴 가이드형. 제목은 강하지만 독자별 예외를 한꺼번에 넣어 무거움. (https://www.aspiring-ceo.com/business-registration-address-change-guide/)
5. **사업자등록 정정신고 방법 — 상호, 업종, 사업장 이전 등 변경 ...** — 세무서비스 콘텐츠. 상호/업종/주소를 모두 다뤄 유용하지만 CTA 느낌이 있음. (https://www.watax.kr/startup/business-registration-correction-guide)
6. **사업자등록 정정 방법 - 상호·업종·주소 변경 신고 가이드 ...** — 위키형 요약. 표는 좋지만 매장 사장님 말투와 실제 순서감이 약함. (https://bizwiki.co.kr/guide/business-registration-change)
7. **법인 사업자등록에 관한 모든 것 (2) 변경편 - 헬프미 블로그 ...** — 법인 중심. 개인사업자/소상공인 독자에게는 불필요한 법인 절차가 많음. (https://www.help-me.kr/blog/article/사업자등록에-관한-모든-것2-사업자등록-변경/)
8. **홈택스로 사업자 등록증 정정 신고, 따라 하면 끝! » 코리아큐 ...** — 따라하기 톤. 차별화하려면 공식 처리기간과 서류를 더 앞에 둬야 함. (https://koreaq.com/hometax-business-registration-correction-guide/)
9. **국세청>국세정책/제도>사업자등록 안내>사업자등록 정정** — A급 공식 근거. 블로그 말투는 아니므로 독자 행동 순서로 풀어야 함. (https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2446&cntntsId=7779)
10. **사업자등록증 주소 변경(정정 신고) 및 자택 주소 등록 시 주의사항** — 실무 주의사항형. 자택 주소/임대차 이슈를 다루지만 공식 링크 보강 필요. (https://klick.kr/사업자등록증-주소-변경정정-신고-및-자택-주소-등록/)
11. **홈택스 사업장 주소 변경 방법을 알려드려요 - 비즈넵 환급 ...** — 도움말형. 화면 순서에는 강하지만 세무/민원 문맥은 제한적. (https://help.bznav.com/hc/ko/articles/900007649223)
12. **사업장 주소 변경, 사업자등록증 주소지 이전하는 방법** — 개인 블로그형 절차. 독자 친화적이나 출처/예외가 약함. (https://extrememanual.net/49976)

