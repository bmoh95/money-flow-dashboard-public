# Bounty/direct-payout scout

검토 기준: 실제 bounty 여부, open 상태, 중복/경쟁 PR, PR 가능 여부, payout rail, 사용자 관여도, 예상 난이도, 승인/지급 가능성. 콘텐츠 fallback 없음.

1. https://github.com/tscircuit/pcb-viewer/issues/163
   - 근거(A): Algora-style /bounty $3, issue open and PR endpoint works. Reject: reward too small, 22 comments, ~30 open PRs, direct submitted PR #868 already linked; approval odds and EV below threshold.
   - 결정: NO-GO / OPPORTUNITY_COST

2. https://github.com/tscircuit/graphics-debug/issues/42
   - 근거(A): /bounty $8 but label already includes Rewarded. 20 comments and ~30 open PRs with multiple direct attempts. Reject as already crowded/rewarded.
   - 결정: NO-GO / DUPLICATE

3. https://github.com/UnsafeLabs/Bounty-Hunters/issues/818
   - 근거(A): $120 code bounty with clear acceptance criteria, but maintainer comment says PR #1479 already completes it. 24 open PRs. Reject: duplicate and approval risk.
   - 결정: NO-GO / DUPLICATE

4. https://github.com/qtop/qtop/issues/355
   - 근거(A): Opire challenge mentions payment account and delayed payment, but 17 comments and 30 open PRs; recent comments link PR #382 and #383 with /opire try. Reject as crowded/claimed.
   - 결정: NO-GO / OPPORTUNITY_COST

5. https://github.com/ubiquity/business-development/issues/89
   - 근거(A): Price: 400 USD label. Reject: bot requires core/collaborator/admin to start, comments show failed /start by outsiders, wallet command appears required, and deliverable is outreach/business-dev not PR-friendly.
   - 결정: NO-GO / HIGH_USER_INPUT

6. https://github.com/ubiquity/business-development/issues/90
   - 근거(A): Price: 200 USD label for GitHub-based marketing. Reject: core/collaborator start restriction, wallet comments, already multiple completed drafts/bids, and outreach risk/spam adjacency.
   - 결정: NO-GO / HIGH_RISK

7. https://github.com/tari-project/universe/issues/3210
   - 근거(A): Bounty-S 15,000 XTM, issue open. Reject: token payout rail (XTM) not cash/platform, 20 open PRs, direct PR #3233 claims full fix with tests. User preference excludes wallet/token-first bounties.
   - 결정: NO-GO / PAYMENT_UNCLEAR

8. https://github.com/Reqrefusion/FreeCAD-Documentation-Project/issues/29
   - 근거(B): Documentation bounty/reward labels, but no amount/payout route, broad outdated tutorial scope, and 20 open PRs in repo. Reject until specific paid subtask and payout route are visible.
   - 결정: NO-GO / PAYMENT_UNCLEAR

9. https://github.com/congruentlabs/sata.technology/issues/1
   - 근거(B): Bounty listed as 10,000 SATA. Reject: token payout, Rinkeby/IdP support setup requirement, and existing PR #2 already submitted.
   - 결정: NO-GO / PAYMENT_UNCLEAR

결론: GO 후보 없음. 실제 현금성 지급 가능성·경쟁도·승인 확률 기준 미달이라 코딩/claim/PR 제출하지 않음.
