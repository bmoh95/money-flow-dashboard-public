# Cash bounty/direct-payout scout

검토 기준: actual bounty/open state/duplicate PR/PR route/payout rail/participant eligibility/user burden/approval-payment odds. 콘텐츠 fallback 없음.

1. https://github.com/Bu1ldTh3Futur3/bounty-hunter-test/issues/1
   - 후보: Fix formatCurrency and parseCurrency bugs — $50 bounty
   - 지급: GitHub issue has /bounty $50 and $50 label; direct platform/bounty route appears visible but claim mechanics not fully documented in body.
   - preflight: Issue open, assignee 없음, PR route exists. Comments already contain many /attempt and PR references (#50/#51/#52 etc.); open PR list has 20 PRs with several exact currency-formatting fixes.
   - 결정: NO-GO / DUPLICATE — Acceptance is small, but competition is saturated and exact fixes already submitted; approval/payment odds weak.

2. https://github.com/claude-builders-bounty/claude-builders-bounty/issues/1
   - 후보: [BOUNTY $50] Generate structured CHANGELOG from git history
   - 지급: Issue body says $50 powered by Opire, /opire try, payment released automatically on merge.
   - preflight: Issue open, assignee 없음, forks/PR route exists. Open PR list shows competing “Add verified changelog generator” and multiple bounty PRs; acceptance requires tested sample output on a real repo and README.
   - 결정: NO-GO / DUPLICATE — Good cash/platform route, but exact competing PR already exists; new PR would be duplicative unless clearly superior after deeper review.

3. https://github.com/claude-builders-bounty/claude-builders-bounty/issues/2
   - 후보: [BOUNTY $75] CLAUDE.md for Next.js + SQLite SaaS
   - 지급: Issue body says $75 powered by Opire, /opire try, payment released automatically on merge.
   - preflight: Issue open, assignee 없음. Existing open PR titled “[BOUNTY 5] TEMPLATE: CLAUDE.md for a Next.js + SQL…” targets the same acceptance area. Output is subjective/template quality, not deterministic micro-fix.
   - 결정: NO-GO / DUPLICATE — Cash route clear, but contested subjective content/template bounty; not suitable for this cash-bounty scout under “no content drift”.

4. https://github.com/tscircuit/jlcsearch/issues/92
   - 후보: Add is_extended_promotional column to components — $75 Algora-style bounty
   - 지급: Issue has /bounty $75 and $75 label; likely platform bounty.
   - preflight: Issue open, assignee 없음. Open PRs include “Add extended promotional component filter”, “feat: add extended promotional component column”, and “Add is_extended_promotional column to components” already addressing the same request.
   - 결정: NO-GO / DUPLICATE — Direct competing PRs already cover the requested field/filter; approval odds poor.

5. https://github.com/UnsafeLabs/Bounty-Hunters/issues/834
   - 후보: [T3 Code] ProviderModelPicker persistence — $40
   - 지급: Labels include $40, 💎 Bounty, AI Agent friendly; comments include /opire try. Cash/platform possible.
   - preflight: Issue open, assignee 없음. Comments already include /opire try and multiple claims. Acceptance includes localStorage persistence, storage-event cross-tab sync, reset option, fallback validation, exact PR title. Repo has parallel active PRs and prior submitted PR in same org was closed as incomplete.
   - 결정: HOLD / OPPORTUNITY_COST — Not impossible, but front-end behavior/test surface is wider than a safe quick micro-bounty, and competition exists.

6. https://github.com/UnsafeLabs/Bounty-Hunters/issues/853
   - 후보: [T3 Code] environment variable validation at server startup — $35
   - 지급: Labels include $35, 💎 Bounty, AI Agent friendly; comments include /opire try and payment route mentions.
   - preflight: Issue open, assignee 없음. Multiple attempts/claims. Acceptance requires Effect Schema validation, startup exit table, --validate-config CLI flag, docs/output behavior; easy to under-implement.
   - 결정: NO-GO / OPPORTUNITY_COST — Small payout but broad acceptance; prior UnsafeLabs rejection suggests avoiding incomplete broad submissions.

7. https://github.com/ubiquity/ubiquity-dollar/issues/972
   - 후보: CI: fix check_storage_layout for new contracts — 300 USD
   - 지급: Labels show Price: 300 USD and Ubiquity task metadata.
   - preflight: Issue open, assignee 없음, but bot comments warn “You must be a core team member, or an administrator to start this task.” Existing PR #1008/#1009 comments and open PR “fix: Skip storage layout check…” already target it.
   - 결정: NO-GO / HIGH_USER_INPUT — Participant eligibility blocked by core/admin requirement plus existing PRs.

결론: 7건 모두 자동 구현/PR 기준 미달. 낮은 금액 때문이 아니라 중복 PR 과밀, 참여자격 제한, 범위 과대, 주관적 content/template 성격 때문에 중단.
