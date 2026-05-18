# Cash bounty/direct-payout scout

검토 기준: actual bounty/open state, duplicate/competition PR, PR route, payout rail, participant constraints, user burden, approval/payment odds. 콘텐츠 fallback 없음.

1. https://github.com/zio/zio/issues/9844
   - 후보: ZIO #9844 — Queue shutdownCause, $1K label
   - 지급: GitHub issue has $1K label; payout/claim mechanics not visible in issue body.
   - preflight: Issue open, assignee 없음, repo accepts PRs. Open PR #10935 directly implements Queue shutdownCause propagation; recent comments include multiple /attempts. Scala/ZIO core semantics and test suite burden high.
   - 결정: NO-GO / DUPLICATE — large core-code bounty is already directly contested by PR #10935; approval odds low for another implementation.

2. https://github.com/claude-builders-bounty/claude-builders-bounty/issues/3
   - 후보: Claude Builders #3 — destructive bash hook, $100 Opire
   - 지급: Opire-powered bounty; body says /opire try, PR, automatic payment on merge.
   - preflight: Issue open, assignee 없음, PR route exists. Comment count 500+ and open PR #1641 already adds destructive bash guard hook; security-hook scope touches command blocking behavior.
   - 결정: NO-GO / DUPLICATE — cash/platform route clear but direct open PR and extreme competition make new PR spammy/low odds.

3. https://github.com/archestra-ai/archestra/issues/3511
   - 후보: Archestra #3511 — invalid Mermaid diagram error display
   - 지급: No visible bounty amount or Algora/Opire claim route on this issue.
   - preflight: Issue open, assignee 없음, repo accepts PRs. Comments include a detailed /attempt plan and another user asking whether a bounty could be added, implying payout is not currently attached.
   - 결정: NO-GO / PAYMENT_UNCLEAR — small bug shape is good, but not a verified paid bounty/direct-payout item.

4. https://github.com/calcom/cal.diy/issues/10805
   - 후보: Cal.com #10805 — encryption key strength docs/code note
   - 지급: No bounty/claim route visible; Maige comments explicitly update instructions to avoid bounties.
   - preflight: Issue open but assigned to zomars. Security/authentication area; external bounty submission could be unwelcome. Repo accepts PRs but no direct payout evidence.
   - 결정: NO-GO / PAYMENT_UNCLEAR — not a bounty and assignee/security context makes automatic PR inappropriate.

5. https://github.com/UnsafeLabs/Bounty-Hunters/issues/763
   - 후보: UnsafeLabs #763 — FastAPI dynamic CORS middleware, $300 Algora-style
   - 지급: Issue labels show $300 and bounty; comments include /attempt and /claim style.
   - preflight: Issue open, assignee 없음, repo accepts PRs. Labels include AI only allowed - no humans, which is reputational/platform-risky. Existing PR #1073 is referenced and multiple attempts/claim comments exist.
   - 결정: NO-GO / HIGH_RISK — AI-only repo policy plus existing PR/attempts and framework-level API design risk block safe auto submission.

6. https://github.com/BAWES-Universe/studenthub-staff/issues/29
   - 후보: BAWES #29 — Ionic 6→8 migration, Opire try comments
   - 지급: /opire try comments present, but issue body does not show bounty amount; broad upgrade task.
   - preflight: Issue open, assignee 없음, repo accepts PRs. Prerequisite issue #28 must merge first; several users already trying, PR #72 submitted per comments; current open PRs show related upgrade work.
   - 결정: NO-GO / OPPORTUNITY_COST — blocked by prerequisite and broad migration/visual QA; not a micro-bounty fit.

7. https://github.com/AstroxNetwork/agent_dart/issues/13
   - 후보: agent_dart #13 — API docs, 20 ICP reward
   - 지급: Reward is 20 ICP plus optional bonus; token/wallet payout, not preferred cash/platform rail.
   - preflight: Issue open, assignee 없음, repo accepts PRs. Existing doc PRs #148-#152 already cover individual files; prior comments ask if still active. Scope is broad all API docs.
   - 결정: NO-GO / PAYMENT_UNCLEAR — token-only payout and many existing doc PRs make it unsuitable for automatic cash bounty lane.

8. https://github.com/y4aniv/sandbox/issues/1
   - 후보: y4aniv/sandbox #1 — Roadsource $100 demonstration issue
   - 지급: Roadsource bot comments say $100 bounty and transfer after merged PR.
   - preflight: Issue open, assignee 없음, repo accepts PRs. Issue body is empty/demo-only; no acceptance criteria. Existing PR #4 updates LICENSE and unrelated issue context suggests test/demo bounty environment.
   - 결정: NO-GO / NO_EVIDENCE — payout bot exists but deliverable is undefined; likely demo/test issue, so no safe implementation target.

결론: 8건 모두 자동 구현/PR 기준 미달. 가장 명확한 cash/platform 후보인 Claude Builders #3은 직접 open PR과 500+ 댓글로 승인 가능성이 낮고, Archestra #3511은 작은 버그지만 bounty가 붙지 않았다.
