# Cash bounty/direct-payout scout

검토 기준: actual bounty, open state, duplicate/competition PR, PR route, payout rail, participant constraints, user burden, approval/payment odds. 콘텐츠 fallback 없음.

1. https://github.com/tscircuit/circuit-json-to-readable-netlist/issues/4
   - 후보: tscircuit #4 — readable netlists pin labels, /bounty $5
   - 지급: Algora-style /bounty $5 shown in issue body; cash/platform likely, but issue has many claim/attempt comments.
   - preflight: Issue open, assignee 없음, PR route exists. Comments include prior bounty-claim bot entry and multiple /attempts. Open PRs #454/#453/#452/#451/#450 and more directly target pin-label/readable-netlist behavior.
   - 결정: NO-GO / DUPLICATE — micro-bounty amount is acceptable, but direct competing PR density is too high for approval odds.

2. https://github.com/claude-builders-bounty/claude-builders-bounty/issues/1
   - 후보: claude-builders-bounty #1 — $50 changelog generator
   - 지급: Opire-powered $50; issue says /opire try + PR, payment on merge.
   - preflight: Issue open, assignee 없음. Comments already contain /opire try and /attempt. Open PR #1632 explicitly closes #1, with many adjacent submissions in same repo.
   - 결정: NO-GO / DUPLICATE — clear payout, but already directly contested; late PR would be duplicate and subjective.

3. https://github.com/claude-builders-bounty/claude-builders-bounty/issues/2
   - 후보: claude-builders-bounty #2 — $75 Next.js + SQLite CLAUDE.md template
   - 지급: Opire-powered $75; issue says /opire try + PR, payment on merge.
   - preflight: Issue open, assignee 없음. Comments already contain /opire try and /attempt. Open PR #1633 explicitly closes #2; template acceptance is subjective and crowded.
   - 결정: NO-GO / DUPLICATE — cash/platform clear, but competition already submitted a direct solution.

4. https://github.com/Reqrefusion/FreeCAD-Documentation-Project/issues/30
   - 후보: FreeCAD Documentation #30 — add missing Release_notes_1.2 info
   - 지급: Labels show Bounty/Reward/$$$/€€€, but no exact payout amount, claim route, or settlement rule in issue body.
   - preflight: Issue open, assignee 없음. Comments mention existing bounty attempt PR #75 and an approval-seeking comment. Open PR #78 also targets missing BIM/Draft release notes; many docs PRs open.
   - 결정: NO-GO / PAYMENT_UNCLEAR — possible reward, but claim/payment route unclear and duplicate PRs exist.

5. https://github.com/UnsafeLabs/Bounty-Hunters/issues/829
   - 후보: UnsafeLabs #829 — Effect ACP token refresh, $500
   - 지급: Algora bot posts $500 bounty and /attempt + /claim flow.
   - preflight: Issue open, assignee 없음. Comments include existing /attempt and /opire try. Open PR #1610 directly implements the same issue. Scope touches auth/session retry logic in Effect client, higher review/security risk.
   - 결정: NO-GO / DUPLICATE — payout clear, but already directly claimed/submitted and scope is not quick micro-bounty safe.

6. https://github.com/SecureBananaLabs/bug-bounty/issues/30
   - 후보: SecureBananaLabs #30 — API benchmark suite, $750
   - 지급: Algora bot posts $750 bounty and /attempt + /claim flow.
   - preflight: Issue open, assignee 없음. Existing /attempt comment and open PRs #204/#201 directly target benchmark suite. Requires full endpoint inventory, auth benchmark token, realistic payloads, and potentially staging/local env.
   - 결정: NO-GO / DUPLICATE — payout clear but crowded and broad; likely high operating burden and duplicate.

결론: $1~$10 micro-bounty도 금액만으로 배제하지 않았으나, 이번 6건은 중복 PR 과밀·지급조건 불명확·범위 과대/보안성 때문에 자동 구현/claim/PR 제출 기준 미달.
