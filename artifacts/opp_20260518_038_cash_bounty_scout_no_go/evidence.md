# Bounty/direct-payout scout

검토 기준: 실제 bounty 여부, open 상태, 중복/경쟁 PR, PR 가능 여부, payout rail, 사용자 관여도, 예상 난이도, 승인/지급 가능성. 콘텐츠 fallback 없음.

1. https://github.com/claude-builders-bounty/claude-builders-bounty/issues/1
   - 근거(A): Opire $50 changelog generator issue open; bounty text says payment on merge. Reject: 871 comments and 100 open PRs in repo, many open/closed PRs explicitly solving #1, approval odds too low.
   - 결정: NO-GO / OPPORTUNITY_COST

2. https://github.com/claude-builders-bounty/claude-builders-bounty/issues/2
   - 근거(A): Opire $75 Next.js+SQLite CLAUDE.md template open. Reject: 348 comments, active competing PRs #1601/#1595/#1592 and many closed attempts; generic template competition creates low differentiation.
   - 결정: NO-GO / DUPLICATE

3. https://github.com/claude-builders-bounty/claude-builders-bounty/issues/3
   - 근거(A): Opire $100 destructive-command hook open. Reject: 496 comments and many open attempts (#1604/#1602/#1600/#1597/#1593); race/selection risk outweighs small payout.
   - 결정: NO-GO / OPPORTUNITY_COST

4. https://github.com/claude-builders-bounty/claude-builders-bounty/issues/4
   - 근거(A): Opire $150 PR review agent open. Reject: 375 comments and active competing PRs (#1603/#1594 plus numerous closed attempts); coding effort moderate but approval odds poor.
   - 결정: NO-GO / OPPORTUNITY_COST

5. https://github.com/claude-builders-bounty/claude-builders-bounty/issues/5
   - 근거(A): Opire $200 n8n weekly dev summary workflow open. Reject: 295 comments, open competing PR #1605, and requires real n8n instance/screenshot plus Claude API setup; high setup burden.
   - 결정: NO-GO / HIGH_USER_INPUT

6. https://github.com/tscircuit/schematic-trace-solver/issues/29
   - 근거(A): Algora-style $100 same-net trace phase open. Reject: 91 comments and multiple active competing PRs (#365/#364/#363/#362/#361); domain-specific geometry risk and crowded queue.
   - 결정: NO-GO / OPPORTUNITY_COST

7. https://github.com/arakoodev/EdgeChains/issues/290
   - 근거(A): $50 AWS Comprehend redaction bounty open. Reject: 40 comments, 100 open PRs in repo and many PRs already targeting #290 (#521/#516/#513/#509/#508); also asks Loom demo with AWS service.
   - 결정: NO-GO / HIGH_USER_INPUT

8. https://github.com/javelin-anticheat/py-workedtask/issues/4
   - 근거(A): $100 integrity verification bounty open. Reject: acceptance checklist in issue body is already checked and open PRs #29/#28/#25/#24/#23 compete; duplicate/likely solved.
   - 결정: NO-GO / DUPLICATE

9. https://github.com/Merit-Systems/x402scan/issues/97
   - 근거(A): Merit $100 OpenAPI upload issue open. Reject: 91 open PRs and direct attempts #877/#853/#795/#765/#758; broader UX/parser scope for small payout.
   - 결정: NO-GO / OPPORTUNITY_COST

10. https://github.com/aqualinkorg/aqualink-app/issues/1162
   - 근거(A): $50 historical map/data feature open. Reject: 31 comments and several active PRs (#1283/#1281/#1280/#1278/#1272); map/site-data scope too broad for $50.
   - 결정: NO-GO / OPPORTUNITY_COST

11. https://github.com/ivrit-ai/ivrit-py/issues/15
   - 근거(B): 100 NIS bounty rules linked, open, no matching open PR found. Reject/HOLD-level risk: requires real GPU/CPU faster-whisper benchmark and 10% performance proof; local environment/payout certainty insufficient for this cron.
   - 결정: NO-GO / HIGH_USER_INPUT

12. https://github.com/Bu1ldTh3Futur3/bounty-hunter-test/issues/1
   - 근거(A): $50 currency parsing/formatting bounty open. Reject: 45 comments and massive competition with open PRs #108-#104 etc.; likely test bounty/contest crowded.
   - 결정: NO-GO / DUPLICATE

결론: GO 후보 없음. 코딩/claim/PR 제출하지 않음.
