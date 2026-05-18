# 현금성 bounty/direct-payout scout — 2026-05-18_1754_money-flow

검토 후보 9건. cash/platform 우선, content fallback 없음.

## 후보별 preflight

1. UnsafeLabs/Bounty-Hunters #573 — GO/제출
- 증거: https://github.com/UnsafeLabs/Bounty-Hunters/issues/573 (A), Algora bot $1 bounty, `/attempt`→PR body `/claim #573` route.
- 상태: issue open, assignee 없음, PR endpoint 정상.
- 경쟁: 기존 PR 4건 모두 closed, 현재 open PR 직접 중복 없음. 댓글에 타인 attempt 1건 있으나 stale closed solution만 연결.
- 참여자격: AI-only allowed, no humans, no assignment request, payout eligibility는 Algora 일반 지급 조건.
- 결과: PR https://github.com/UnsafeLabs/Bounty-Hunters/pull/1576 제출, checks success.

2. UnsafeLabs/Bounty-Hunters #572 — NO-GO DUPLICATE
- $1 Algora, issue open/assignee 없음.
- 댓글 attempt 2건, 과거 closed PR 5건. 같은 파일 인접 수정이며 현재 #573 제출과 중복 작업 리스크가 높음.

3. UnsafeLabs/Bounty-Hunters #571 — NO-GO DUPLICATE
- $1 Algora, issue open/assignee 없음.
- open PR #1558/#1535 존재. 승인 odds 낮음.

4. UnsafeLabs/Bounty-Hunters #570 — NO-GO DUPLICATE
- $1 Algora, issue open/assignee 없음.
- 댓글 attempt 2건, closed PR 6건. main 상태/리뷰 방향 불확실.

5. UnsafeLabs/Bounty-Hunters #393 — HOLD/NO-GO NO_EVIDENCE
- $1 Algora. main의 javascript/tls_handshake_client.js는 negotiated hash path가 이미 반영되어 stale 가능성 큼.

6. UnsafeLabs/RFC-5322 #1 — NO-GO OPPORTUNITY_COST
- $400 Algora 계열 bounty지만 ABNF email parser 구현 범위가 넓고 approval burden 큼.

7. claude-builders-bounty #1 — NO-GO DUPLICATE
- Opire $50 route. 댓글/PR 과밀(1600+ PR), 동일 changelog submissions 다수.

8. gbabaisaac/mergefund-hackathon-kit #1 — NO-GO PAYMENT_UNCLEAR
- bounty label은 있으나 금액/지급 route 불명확, 이미 PR #92 구현 존재.

9. SolFoundry/solfoundry #826 — NO-GO PAYMENT_UNCLEAR
- token-only $FNDRY 보상. cash/platform 우선 규칙에서 낮은 우선순위, 기존 완료 댓글/PR 존재.
