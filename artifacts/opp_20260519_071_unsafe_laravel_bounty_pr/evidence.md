# Cash bounty/direct-payout scout + PR submission

검토 기준: actual bounty/open state, duplicate/competition PR, PR route, payout rail, participant constraints, user burden, approval/payment odds. 콘텐츠 fallback 없음.

1. https://github.com/archestra-ai/archestra/issues/4758
   - 후보: Archestra #4758 — usage limits visibility UX/DX, $150 Algora
   - 지급: Algora $150 cash/platform bounty.
   - preflight: Open, but assigned to piercypixel; required core-team assignment in bot instructions. Existing /attempt by assignee.
   - 결정: NO-GO / HIGH_USER_INPUT — participant eligibility blocked by existing assignee/core-team assignment requirement.

2. https://github.com/archestra-ai/archestra/issues/4030
   - 후보: Archestra #4030 — Approval flow broken in Web UI Chat, $100 Algora
   - 지급: Algora $100 cash/platform bounty.
   - preflight: Open, assigned to mbachaud, Reserved for SE interview. Prior PR branch history and assignee /attempt present.
   - 결정: NO-GO / HIGH_USER_INPUT — reserved/assigned interview task; automatic PR would violate eligibility/approval odds.

3. https://github.com/tscircuit/jlcsearch/issues/92
   - 후보: tscircuit jlcsearch #92 — is_extended_promotional column, $75
   - 지급: Algora-style /bounty $75 cash/platform label.
   - preflight: Open but direct comments include PR #310 and multiple current attempts. gh PR search found 30 open related PRs.
   - 결정: NO-GO / DUPLICATE — crowded with direct competing PRs; approval odds low.

4. https://github.com/UnsafeLabs/Bounty-Hunters/issues/803
   - 후보: UnsafeLabs #803 — FastAPI concurrent runner, $50
   - 지급: Algora/Stacylia $50 cash/platform label.
   - preflight: Open, no assignee, but maintainer comment says PR #1478 already completed implementation.
   - 결정: NO-GO / DUPLICATE — already implemented according to maintainer; do not duplicate.

5. https://github.com/UnsafeLabs/Bounty-Hunters/issues/745
   - 후보: UnsafeLabs #745 — Laravel password cast bcrypt rounds, $50
   - 지급: Algora/Stacylia $50 cash/platform label; PR body /claim route visible.
   - preflight: Open, no assignee, repo accepts fork PRs. No open PR found by issue search. Scope is 2 small Laravel files plus test; no L4.
   - 결정: GO / None — small, safe, cash/platform micro-bounty with clear acceptance and low active competition; implemented and submitted PR #1710.

6. https://github.com/arakoodev/EdgeChains/issues/290
   - 후보: EdgeChains #290 — AWS Comprehend redaction utility, $50
   - 지급: Algora-style $50 label.
   - preflight: Open but 22 open PRs directly mention the issue; requires AWS Comprehend integration, example, and Loom video.
   - 결정: NO-GO / DUPLICATE — crowded and requires external AWS/video validation burden.

7. https://github.com/tscircuit/circuitjson.com/issues/79
   - 후보: circuitjson.com #79 — dependency update, $50
   - 지급: $50 bounty but label shows rewarded.
   - preflight: Open issue, rewarded label, PR #227/#230 comments and 30 open related PRs.
   - 결정: NO-GO / DUPLICATE — rewarded/crowded; not a fresh payout candidate.

8. https://github.com/Bu1ldTh3Futur3/bounty-hunter-test/issues/1
   - 후보: bounty-hunter-test #1 — currency utility bugs, $50
   - 지급: /bounty $50 cash/platform label.
   - preflight: Open but comments and gh PR search show dozens of direct submitted PRs.
   - 결정: NO-GO / DUPLICATE — trivial task already saturated; approval odds poor.

9. https://github.com/aqualinkorg/aqualink-app/issues/1162
   - 후보: Aqualink #1162 — historical map/data view, $50
   - 지급: $50 bounty label.
   - preflight: Open but at least 10 direct open PRs and broad frontend/backend/date data flow scope.
   - 결정: NO-GO / DUPLICATE — crowded and too broad for quick cash scout.

10. https://github.com/rohitdash08/FinMind/issues/124
   - 후보: FinMind #124 — login anomaly detection, $50
   - 지급: Bounty/$50 labels; Opire comments visible.
   - preflight: Open, assigned to Pranjal6955, many direct PRs and broad production-ready auth/security scope.
   - 결정: NO-GO / HIGH_USER_INPUT — assigned and high-risk auth/security surface; not suitable for automatic PR.

결론: UnsafeLabs #745만 GO. /attempt 댓글 후 fork branch push 및 PR 제출 완료: https://github.com/UnsafeLabs/Bounty-Hunters/pull/1710
