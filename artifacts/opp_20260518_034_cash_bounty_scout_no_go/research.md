# Bounty/direct-payout scout

검토 기준: 실제 bounty, open 상태, 경쟁 PR, PR 가능 여부, payout rail, 사용자 관여도, 난이도, 승인/지급 가능성. 콘텐츠 fallback 없음.

1. https://github.com/highlight/highlight/issues/8635
   - 근거(A): Algora bounty label, issue open and PR endpoint works. Reject: broad antd removal split across pages, 10 comments, open related PRs #10442/#10440 and prior claimed PR #9716; acceptance/payment odds diluted.
   - 결정: NO-GO / OPPORTUNITY_COST

2. https://github.com/tscircuit/circuit-json-to-readable-netlist/issues/4
   - 근거(A): /bounty $5, issue open and PR endpoint works. Reject: at least five current related PRs #449-#453 plus many /attempt comments; reward too small for competition.
   - 결정: NO-GO / OPPORTUNITY_COST

3. https://github.com/claude-builders-bounty/claude-builders-bounty/issues/4
   - 근거(A): Opire $150 PR review agent. Reject: active /opire try comments and related PR #1603 already open; likely duplicate.
   - 결정: NO-GO / DUPLICATE

4. https://github.com/claude-builders-bounty/claude-builders-bounty/issues/2
   - 근거(A): Opire $75 CLAUDE.md template. Reject: multiple comments/submissions and related PR #1601 already open; generic template bounty has high duplicate/AI-filler risk.
   - 결정: NO-GO / DUPLICATE

5. https://github.com/claude-builders-bounty/claude-builders-bounty/issues/5
   - 근거(A): Opire $200 n8n weekly dev summary workflow. Reject: active /opire try, multiple bidders, related PR #1605 already open; not worth starting without assignment.
   - 결정: NO-GO / DUPLICATE

6. https://github.com/ubiquity/business-development/issues/90
   - 근거(A): Price: 200 USD label. Reject: marketing/outreach deliverable has spam/reputation risk, many claim/comment attempts, wallet-style payout path appears in comments.
   - 결정: NO-GO / HIGH_RISK

7. https://github.com/Spectral-Finance/lux/issues/68
   - 근거(A): Opire-style $3,000 YouTube integration. Reject: large OAuth/live-streaming scope, related PR #616 already submitted claiming full fix, high review burden.
   - 결정: NO-GO / OPPORTUNITY_COST

8. https://github.com/ubiquity/ubiquibot/issues/913
   - 근거(A): Price: 200 USD remove axios dependency. Reject: assigned to developerfred, related PR #936 already open, wallet beneficiary shown by bot.
   - 결정: NO-GO / DUPLICATE

9. https://github.com/ubiquity/ubiquibot/issues/912
   - 근거(A): Price: 200 USD label sync bug. Reject: assigned to wannacfuture; Ubiquity task flow often needs /start and wallet/beneficiary, so outsider approval odds unclear.
   - 결정: NO-GO / HIGH_USER_INPUT

10. https://github.com/spaceandtimefdn/sxt-proof-of-sql/issues/228
   - 근거(A): Algora bounty/good-first refactor. Reject: many competing comments and related PRs #1354/#1397/#1702/#1732 touching same Scalar conversion path; merge-conflict risk high.
   - 결정: NO-GO / OPPORTUNITY_COST

11. https://github.com/spaceandtimefdn/sxt-proof-of-sql/issues/560
   - 근거(A): Algora $200 test coverage issue. Reject: intentionally parallel but extremely crowded with dozens of open test PRs; narrow unclaimed slice not identified in this scout window.
   - 결정: NO-GO / OPPORTUNITY_COST

12. https://github.com/arakoodev/EdgeChains/issues/290
   - 근거(A): Algora $50 AWS Comprehend JS SDK integration. Reject: many competing PRs #502/#507/#508/#509/#513/#516/#521 and comments; low payout vs competition.
   - 결정: NO-GO / DUPLICATE

결론: GO 후보 없음. 코딩/claim/PR 제출하지 않음.
