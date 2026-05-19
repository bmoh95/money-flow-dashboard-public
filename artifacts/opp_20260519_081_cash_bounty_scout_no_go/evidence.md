# Cash bounty/direct-payout scout

검토 기준: actual bounty/open state/duplicate PR/PR route/payout rail/participant eligibility/user burden/approval-payment odds. 콘텐츠 fallback 없음.

1. https://github.com/UnsafeLabs/Bounty-Hunters/issues/304
   - 후보: [Docs] Fix wrong HTTP method for Create Bounty — $1 Algora
   - 지급: Algora bot comment shows $1 cash/platform bounty with /attempt and /claim route.
   - preflight: Issue open, assignee 없음, PR route exists. Body requires PR description to start with a code block containing the system prompt and contributor_meta.json. Comments show multiple /attempt entries and submitted PR #398 already addressing the exact one-line doc fix.
   - 결정: NO-GO / HIGH_RISK — System-prompt disclosure requirement is explicitly blocked by user rules; exact competing PR also exists.

2. https://github.com/UnsafeLabs/Bounty-Hunters/issues/306
   - 후보: [Docs] Fix wrong package name in setup-guide.md — $1 Algora
   - 지급: Labels show 💎 Bounty and $1; likely Algora cash/platform route.
   - preflight: Issue open, assignee 없음. Same UnsafeLabs AI-only template requires system prompt disclosure in PR body; comments/attempts already present from search result context.
   - 결정: NO-GO / HIGH_RISK — Even $1 micro-bounty is acceptable in principle, but system-prompt disclosure is not allowed; skip before implementation.

3. https://github.com/BAWES-Universe/studenthub-staff/issues/27
   - 후보: [UPGRADE] Angular 17 → 18 incremental migration — Opire-style
   - 지급: Comments include /opire try, but issue body does not show price in GitHub view.
   - preflight: Issue open, assignee 없음. Prerequisite #26 must be merged first; comments show TiagoAlmeidaS, weilixiong, zp6 PR #70, yi-hialong, cycy701 already attempting. Scope requires full Angular upgrade/build/runtime validation.
   - 결정: NO-GO / DUPLICATE — Competing attempts/PR already exist and migration scope is too broad for quick safe scout.

4. https://github.com/BAWES-Universe/studenthub-staff/issues/28
   - 후보: [UPGRADE] Angular 18 → 19 + standalone/control-flow migration — Opire-style
   - 지급: Comments include /opire try, but price is not visible in GitHub issue body.
   - preflight: Issue open, assignee 없음. Depends on #27 first; comments show multiple attempts and PR #71. Scope includes multi-pass Angular standalone migration, control-flow migration, builder changes, and full build validation.
   - 결정: NO-GO / OPPORTUNITY_COST — Large architectural migration, prerequisite dependency, and existing competition make approval odds poor.

5. https://github.com/BAWES-Universe/studenthub-staff/issues/29
   - 후보: [UPGRADE] Ionic 6 → 8 migration — Opire-style
   - 지급: Comments include /opire try, but visible GitHub issue body has no amount.
   - preflight: Issue open, assignee 없음. Depends on #28; comments show multiple attempts and PR #72. Scope includes Ionic major upgrade, CSS migration, component API audits, visual QA.
   - 결정: NO-GO / OPPORTUNITY_COST — Prerequisite blocked and broad manual validation burden; not a safe automated bounty PR.

6. https://github.com/DefGuard/client/issues/833
   - 후보: 💎 Desktop client 2.0 tray window
   - 지급: Issue title has 💎 but reward amount and claim/payout route are not visible. Commenters asked for confirmation.
   - preflight: Issue open, assignee 없음. Maintainer comment says “It is already being implemented.” Figma UI scope is sizeable desktop tray MVP.
   - 결정: NO-GO / PAYMENT_UNCLEAR — Payout route unclear and maintainer says work is already in progress.

7. https://github.com/Kreyren/git-workspace/issues/1
   - 후보: Stub issue for IssueHunt $4 funded bug bounty
   - 지급: IssueHunt badge shows $4 funded and submit-PR-to-claim link.
   - preflight: Issue open, assignee 없음, but IssueHunt summary lists submitted PR #2. Comment confirms PR #2 already implements prefixed workspace config files with tests/docs.
   - 결정: NO-GO / DUPLICATE — Funded micro-bounty fits amount preference, but exact claim PR already exists.

8. https://github.com/sindresorhus/fkill-cli/issues/6
   - 후보: Smart mode — IssueHunt $40 funded
   - 지급: IssueHunt bot/comment shows $40 open bounty historically.
   - preflight: Issue open, assignee 없음. Very old issue; part of Chrome helper filtering already done in 3.5.0. Remaining request is ambiguous smart-mode/product behavior with maintainer design choices; IssueHunt current payout certainty not verified from GitHub alone.
   - 결정: HOLD / PAYMENT_UNCLEAR — Potential cash bounty but stale/ambiguous acceptance and payout certainty require external IssueHunt validation before coding.

9. https://github.com/OWASP-BLT/BLT-Sammich/issues/64
   - 후보: Implement Good First Issue Label Workflow
   - 지급: Issue points to OWASP BLT-Pool, but this GitHub issue has no price/payment terms.
   - preflight: Issue open, assignee 없음. Bot states issue is not ready for assignment and needs maintainer help-wanted label before /assign works.
   - 결정: NO-GO / HIGH_USER_INPUT — Participant eligibility blocked by maintainer approval/label requirement; no visible bounty amount.

결론: 9건 모두 자동 구현/PR 기준 미달. 낮은 금액 때문이 아니라 system-prompt 공개 요구, 중복 PR/attempt, 지급 불명확, 참여자격 제한, 범위 과대 때문에 중단.
