# Cash bounty/direct-payout scout

검토 기준: actual bounty, open state, duplicate/competition PR, PR route, payout rail, participant constraints, user burden, approval/payment odds. 콘텐츠 fallback 없음.

1. https://github.com/algora-io/algora/issues/238
   - 후보: algora-io/algora #238 — Unauthorized Edit/Delete buttons on bounties page
   - 지급: Algora-related repo issue; title/body does not show a visible bounty amount or reward bot on the issue itself.
   - preflight: Issue open, assignee 없음. PR route exists. Open PRs #267 and #266 already directly address #238, plus active bounties-page PRs #268/#269.
   - 결정: NO-GO / DUPLICATE — likely real bug, but bounty/payment source is not visible and direct competing PRs already exist.

2. https://github.com/claude-builders-bounty/claude-builders-bounty/issues/1
   - 후보: claude-builders-bounty #1 — $50 changelog generator
   - 지급: Opire-powered $50; /opire try + PR; payment on merge per issue body.
   - preflight: Issue open, assignee 없음. Open PR list has #1628/#1627/#1625 and many earlier submissions for same changelog generator.
   - 결정: NO-GO / DUPLICATE — cash/platform clear, but competition/duplicate density makes a late PR low-approval.

3. https://github.com/claude-builders-bounty/claude-builders-bounty/issues/2
   - 후보: claude-builders-bounty #2 — $75 CLAUDE.md template for Next.js + SQLite
   - 지급: Opire-powered $75; /opire try + PR; payment on merge per issue body.
   - preflight: Issue open, assignee 없음. Open PR #1626 already targets #2; repo has very high submission velocity and comments/PR crowding.
   - 결정: NO-GO / DUPLICATE — clear payout but already directly contested; template quality would be subjective and late.

4. https://github.com/RatLoopz/sahidawa-india/issues/196
   - 후보: RatLoopz/sahidawa-india #196 — Copy to Clipboard button
   - 지급: No cash/platform bounty visible; appears GSSOC contribution issue.
   - preflight: Issue open but assigned to shreyamahesh07-git. Labels gssoc-2026. No bounty bot/payment rail; PR route exists but assignment blocks autonomous bounty PR.
   - 결정: NO-GO / NO_EVIDENCE — not a direct-payout bounty and assigned to another contributor.

5. https://github.com/vllm-project/vllm-omni/issues/2645
   - 후보: vllm-omni #2645 — vendor-organized community recipes
   - 지급: No cash bounty visible; help wanted/good first issue only.
   - preflight: Issue open but many assignees and claimers/PRs in body table. Requires hardware/model recipe validation and likely significant manual GPU context.
   - 결정: NO-GO / HIGH_USER_INPUT — not direct cash; crowded and requires external hardware/model validation burden.

6. https://github.com/Scottcjn/rustchain-bounties/issues/443
   - 후보: RustChain #443 — write one-paragraph review for 5 RTC
   - 지급: 5 RTC token reward plus optional social bonus; not cash/platform USD payout.
   - preflight: Issue open. Requires Discord membership and potentially wallet/token ecosystem; not safe autonomous cash bounty. Existing repo has heavy bounty PR/comment automation volume.
   - 결정: NO-GO / PAYMENT_UNCLEAR — token/Discord/user-account path conflicts with cash/platform-first rule and user wallet constraints.

결론: 자동 구현·claim·PR 제출까지 갈 GO 후보 없음. 낮은 금액 때문이 아니라 중복 선점, 지급 불명확, 타인 배정, 토큰/계정 요구, 외부 검증 부담 때문에 중단.
