# Bounty/direct-payout scout

검토 기준: 실제 bounty 여부, open 상태, 중복/경쟁 PR, PR 가능 여부, payout rail, 사용자 관여도, 예상 난이도, 승인/지급 가능성. 콘텐츠 fallback 없음.

1. https://github.com/claude-builders-bounty/claude-builders-bounty/issues/3
   - 근거(A): Opire $100 destructive-command pre-tool hook. Issue open, PR endpoint works, but comments already include claims/attempts and repo has many active PRs for same issue (#1606-#1613 etc). Security hook scope is crowded; approval odds poor.
   - 결정: NO-GO / DUPLICATE

2. https://github.com/claude-builders-bounty/claude-builders-bounty/issues/1
   - 근거(A): Opire $50 changelog skill. Issue open and cash/platform route visible, but comments and open PR list show many competing implementations (#1610, #1611, #1614, #1615). No low-competition path.
   - 결정: NO-GO / DUPLICATE

3. https://github.com/sorosave-protocol/frontend/issues/16
   - 근거(A): bounty label; i18n acceptance criteria visible. Payout details asked by commenter but not answered in inspected thread; existing PR #159 and related comments already target the issue. Broad app change.
   - 결정: NO-GO / PAYMENT_UNCLEAR

4. https://github.com/SCIBASE-AI/SCIBASE.AI/issues/18
   - 근거(A): Algora $1,000 bounty visible. Scope is a full scientific bounty marketplace module; repo has many open AI-agent PRs and large feature surface. Not a quick safe micro-bounty.
   - 결정: NO-GO / OPPORTUNITY_COST

5. https://github.com/speakers-in-tech/conference-data/issues/4
   - 근거(A): Algora $10 cash/platform bounty to add ScalaDays data. Issue open, but assigned to another user; comments show prior PR claim and open PRs #303/#305 already add Scala Days. Participant preflight fails before coding.
   - 결정: NO-GO / HIGH_USER_INPUT

6. https://github.com/spaceandtimefdn/sxt-proof-of-sql/issues/560
   - 근거(A): Algora/Space and Time coverage bounty, per-line payout. Multiple parallel PRs open (#1740-#1743) and high-quality Rust coverage review expected. Could be valid later, but current quick scout has no small unclaimed slice verified.
   - 결정: HOLD / OPPORTUNITY_COST

7. https://github.com/LibVNC/libvncserver/issues/686
   - 근거(B): Issue mentions IssueHunt as possible incentive but no visible funded bounty amount in issue; maintainer warns not to spam comments. Payout unclear and C protocol change is non-trivial.
   - 결정: NO-GO / PAYMENT_UNCLEAR

8. https://github.com/UnsafeLabs/Bounty-Hunters/issues/798
   - 근거(A): Algora $400 bounty visible, but comments show prior attempts and PR #982 claiming; repo has many active submissions. SSE feature scope is broad and likely duplicate.
   - 결정: NO-GO / DUPLICATE

결론: 자동 claim/구현/PR 가능한 GO 후보 없음. $1~$10도 허용 기준으로 봤지만, 낮은 금액이 아니라 경쟁/자격/지급/범위 리스크가 blocker.
