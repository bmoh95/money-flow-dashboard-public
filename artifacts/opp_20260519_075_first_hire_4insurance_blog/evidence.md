# Research — 신규 후보 scout (2026-05-19_0953_money-flow)

## 중복 확인
기존 Money Flow에는 고용보험료 지원 글, 최저임금·주휴수당 글, 사업용계좌/카드/현금영수증/전자세금계산서 글이 있다. `첫 직원 채용 후 4대보험 사업장 성립신고·자격취득신고 순서`를 다룬 항목은 없다. 세금 글 반복 위험은 있으나 이번 주제는 직원 채용 직후 행정 실수 prevention이라 reader use case가 다르다.

## 후보 4개 검토

### 후보 A — 첫 직원 채용 후 4대보험 사업장 성립신고 체크 무료 글
- 유형: Korean free validation blog / 소상공인 첫 채용 운영 체크.
- 독자: 아르바이트·정직원을 처음 뽑는 개인사업자, 작은 매장 사장님.
- 채널: Tistory 무료 글, 판매 CTA 없음.
- A 근거: 4대사회보험 정보연계센터 공식 사이트와 찾기쉬운 생활법령 `4대 사회보험 및 취업규칙 신고` 페이지 확인.
- B 근거: 네이버/Tistory/세무·노무 블로그에서 첫 직원 채용, 사업장 성립신고, 자격취득신고 comparable 다수.
- 실패 가능성: 업종·근로시간·보험별 신고기한 예외를 단정하면 노무/세무 위험. `처음 뽑은 날 무엇을 확인할지`로 축소 필요.
- 판단: GO.

### 후보 B — GitHub/Algora cash bounty 재스카우트
- 근거: GitHub search에서 highlight/highlight #8635, UnsafeLabs #760 등 open Algora 후보가 보임.
- 문제: 최근 현금성 bounty scout가 반복됐고 과밀·중복·assignment/payout profile 리스크가 높다. 이 새작업 scout에서는 broad PR 후보 생성 금지.
- 판단: NO-GO / OPPORTUNITY_COST + PAYMENT_UNCLEAR.

### 후보 C — Smashing Magazine paid article pitch
- 근거: 공식 `Writing A Smashing Article` 페이지 존재.
- 문제: pitch 승인까지 오래 걸리고 영어 장문/편집 커뮤니케이션 필요. 사용자의 현금 거리 1~2 선호와 맞지 않음.
- 판단: HOLD / HIGH_USER_INPUT.

### 후보 D — Devpost cash-prize hackathon
- 근거: Devpost에 open cash-prize hackathon 결과 존재.
- 문제: 상금 확률형, 데모/계정/제출 부담 큼. 재사용 자산은 남지만 이 cron의 저부담 신규 검증 기준 미달.
- 판단: NO-GO / OPPORTUNITY_COST.

## comparable sample brief
- 1. 직원을 처음 채용했는데 4대보험 가입은 어떻게 하나요 (Naver 노무사 블로그) — 질문형 제목, 신고 순서와 기한을 짧게 설명
- 2. 개인사업자 직원등록 2025년 첫 등록부터 4대보험 처리까지 (Tistory/세무 정보) — 긴 절차형, 첫 직원 pain이 명확
- 3. 직원이 있는 개인사업자의 4대 보험과 첫 직원채용 후 해야하는 일 (개인 블로그) — 실제 경험담 + 체크리스트 리듬
- 4. 첫 직원이 생겼어요! 개인사업자 대표자의 4대보험 가입 (세무/노무 가이드) — 대표자와 직원 구분을 강조
- 5. 첫 직원 채용 후 7일 안에 할 4대보험·원천세 실무 (세무법인 블로그) — 기한·원천세까지 확장, CTA 강함
- 6. 4대보험 가입대상 사업장 신고 내용 및 신고 방법 안내 (노무 서비스 페이지) — 사업장 성립신고 중심, 서비스 CTA
- 7. 4대보험 사업장 성립신고 대상자, 기한, 신고 방법 총정리 (세무 서비스 글) — 대상/기한/방법 표 중심
- 8. 사업장 성립신고 개인사업자 직원 채용 시 쉬운 신고 방법 (Naver 블로그) — 따라하기 스크린샷형
- 9. 직원 4대보험 신고하는 방법 총정리 (Tistory 정보글) — 항목 나열형, 초보에게는 길다
- 10. 직원 채용했는데 4대보험은 어떻게 시작하나요 (Tistory 세무 글) — 첫 채용 상황을 앞세움

## Research Lead gate
- Buyer/reader clarity: 명확. 첫 직원/알바를 뽑는 개인사업자.
- Channel: Tistory 무료 검증 글. `돈관리·구매체크 > 세금·장부` 또는 직원 운영 글로 fit.
- Evidence: A 공식 + B comparable 다수.
- Payout: 직접 현금 없음. 장기 SEO/검증 자산. 유료 CTA 금지.
- Margin: 외부 비용 0원, 공식 문구 확인 부담 중간.
- Decision: GO, 단 보험별 기한·가입대상은 공식 안내 확인형으로만 표현.
