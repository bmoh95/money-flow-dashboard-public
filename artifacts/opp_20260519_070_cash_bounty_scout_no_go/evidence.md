# Cash bounty/direct-payout scout

검토 기준: actual bounty/open state, duplicate/competition PR, PR route, payout rail, participant constraints, user burden, approval/payment odds. 콘텐츠 fallback 없음.

1. https://github.com/ubiquity/uusd.ubq.fi/issues/47
   - 후보: Ubiquity #47 — CoWSwap Integration Improvements, $75
   - 지급: Ubiquity labels show Price: 75 USD, Time <2 Hours.
   - preflight: Issue open, assignee 없음, repo accepts PRs. Recent UbiquityOS comments repeatedly say “You must be a core team member, or an administrator to start this task”. Open PR #48 and multiple closed attempts #51/#52/#55/#56.
   - 결정: NO-GO / HIGH_USER_INPUT — cash label exists but contributor eligibility is blocked by core/admin start requirement; automatic PR would likely be closed.

2. https://github.com/ubiquity/pay.ubq.fi/issues/433
   - 후보: Ubiquity pay #433 — Supabase database types, $37.5
   - 지급: Ubiquity labels show Price: 37.5 USD, Time <1 Hour.
   - preflight: Issue open, assignee 없음. UbiquityOS bot repeatedly blocks external /start with core/admin requirement. Many closed duplicate PRs #461/#463/#464/#466/#467/#468/#469. Requires production Supabase schema parity.
   - 결정: NO-GO / DUPLICATE — eligibility blocker plus crowded failed PR history and schema-source uncertainty make approval odds poor.

3. https://github.com/ubiquity/ubiquibot/issues/701
   - 후보: Ubiquity ubiquibot #701 — price PRs without linked issue, $50
   - 지급: Ubiquity labels show Price: 50 USD, Time <2 Hours.
   - preflight: Issue open, no assignee. Requirements are vague and bot/app QA requires Ubiquibot QA app/local workflow context. Comments show maintainers discussing app-install/test setup, not a simple micro-fix.
   - 결정: NO-GO / NO_EVIDENCE — paid label exists but acceptance criteria are under-specified and test environment is non-trivial.

4. https://github.com/ubiquity/business-development/issues/90
   - 후보: Ubiquity business #90 — GitHub Based Marketing, $200
   - 지급: Ubiquity labels show Price: 200 USD.
   - preflight: Issue open, no assignee. Bot comments block external start: must be core/admin. PR search shows many closed attempts #200/#204/#210/#214/#216; work is marketing/research rather than code.
   - 결정: NO-GO / HIGH_USER_INPUT — external eligibility blocked; not suitable for automatic bounty PR.

5. https://github.com/ubiquity/research/issues/83
   - 후보: Ubiquity research #83 — review Polarsource UX
   - 지급: No visible price label; only Priority label.
   - preflight: Issue open, no comments, no visible USD/claim route despite search match. Research/review deliverable requires subjective maintainer acceptance.
   - 결정: NO-GO / PAYMENT_UNCLEAR — not a verified paid bounty/direct-payout item.

6. https://github.com/polarsource/examples/issues/86
   - 후보: Polar examples #86 — Java Spring Boot example
   - 지급: Maintainer explicitly says there is no bounty.
   - preflight: Issue open but assigned to abhinav-m22; open PR #90 already submitted. Comments confirm contributor proceeds without bounty.
   - 결정: NO-GO / PAYMENT_UNCLEAR — no bounty and assigned/competing PR exists.

7. https://github.com/polarsource/examples/issues/87
   - 후보: Polar examples #87 — Rust Axum example
   - 지급: Maintainer explicitly says there is no bounty.
   - preflight: Issue open but assigned to abhinav-m22; open PR #91 already submitted. Comments confirm no bounty.
   - 결정: NO-GO / PAYMENT_UNCLEAR — no payout and already assigned/implemented.

8. https://github.com/Kleo-Network/kleo-connect/issues/56
   - 후보: Kleo Connect #56 — Add Documentation, $25
   - 지급: Issue body says Reward: 25 USD; payout route not platform-mediated and commenters mention PayPal/Stripe privately.
   - preflight: Issue open, no assignee. PR search shows many open duplicate README PRs #79/#84/#85/#89/#95; latest comments include multiple submissions.
   - 결정: NO-GO / DUPLICATE — simple doc bounty is heavily crowded and payout route is private/manual.

9. https://github.com/aukilabs/hagall/issues/62
   - 후보: Auki Hagall #62 — ROS2 topic relay, $50
   - 지급: Issue title says Bounty |50 USD; payout appears manual/private.
   - preflight: Issue open, no assignee. Open PRs #63/#65/#66 and prior closed #64 directly target the issue; comments include several claims. Scope is Go/WebSocket/ROS2 integration with tests.
   - 결정: NO-GO / DUPLICATE — direct competing PRs and integration complexity; not quick or low-competition.

10. https://github.com/UnsafeLabs/Bounty-Hunters/issues/852
   - 후보: UnsafeLabs #852 — ChatView accessibility, $50
   - 지급: Labels include $50 and bounty; comments include wallet/PayPal claim attempts.
   - preflight: Issue open, no assignee. Labels include AI only allowed - no humans. Multiple closed PRs #962/#1148/#1237/#1404/#1670 and active attempts/comments.
   - 결정: NO-GO / HIGH_RISK — AI-only repo policy, repeated failed attempts, and competition make auto PR unsafe/low odds.

11. https://github.com/codingo/dooked/issues/2
   - 후보: dooked #2 — Regular Expression Checks, bounty on merge
   - 지급: Label says bounty on merge; comments mention $200/PayPal, but issue asks to contact maintainer on Twitter before taking it.
   - preflight: Issue open, no assignee. Open PRs #8/#10/#12/#13 already implement same feature; comment asks maintainer whether new submissions are still accepted. External Twitter contact would be customer/contact outreach.
   - 결정: NO-GO / HIGH_USER_INPUT — requires external maintainer contact before starting and already has multiple direct PRs.

12. https://github.com/evilew/GS13-Outdated/issues/188
   - 후보: GS13-Outdated #188 — Weapon jamming bug, $50 PayPal
   - 지급: Issue body says 50 USD via PayPal after tested/documented/explained fix.
   - preflight: Issue open, no assignee, no competing PR found. However it is a BYOND/SS13 gameplay bug with random reproduction over seconds-minutes, requires domain-specific testing and explanation. PayPal details needed after acceptance.
   - 결정: NO-GO / OPPORTUNITY_COST — best low-competition candidate, but debugging/reproduction burden is too high for this quick cash scout cycle.

결론: 12건 모두 자동 구현/PR 기준 미달. Ubiquity 계열은 USD 라벨이 있으나 core/admin start requirement가 반복 확인됐고, Kleo/Auki/codingo는 경쟁 PR이 과밀하며, GS13은 무경쟁이나 재현·테스트 부담이 크다.
