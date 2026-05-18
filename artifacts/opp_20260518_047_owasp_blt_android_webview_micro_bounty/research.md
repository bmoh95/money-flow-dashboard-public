# Cash bounty/direct-payout scout — 2026-05-18_1207_money-flow

Reviewed bounty/direct-payout candidates, prioritizing cash/platform payout, low competition, small scope, and PR acceptance odds.

| Candidate | Payout | Decision | Stop code | Notes |
|---|---:|---|---|---|
| `claude-builders-bounty/claude-builders-bounty#1` | $50 Opire changelog skill | NO-GO | DUPLICATE | Open but ~100 open PRs; several existing changelog PRs already compete. |
| `claude-builders-bounty/claude-builders-bounty#2` | $75 Opire Next.js+SQLite CLAUDE.md | NO-GO | DUPLICATE | Open but multiple overlapping CLAUDE.md PRs already submitted. |
| `claude-builders-bounty/claude-builders-bounty#3` | $100 Opire destructive-command hook | NO-GO | DUPLICATE | Open but many overlapping hook PRs already submitted; security scope broad. |
| `UnsafeLabs/Bounty-Hunters#804` | $200 FastAPITestClient | NO-GO | DUPLICATE | Open cash/platform-looking bounty but two overlapping PRs already open; changes target upstream FastAPI-shaped API. |
| `spaceandtimefdn/sxt-proof-of-sql#560` | $200 coverage tests | NO-GO | OPPORTUNITY_COST | Real bounty but broad coverage work with 100 open PRs and high review burden. |
| `tscircuit/tscircuit#328` | $100 Arduino Nano circuit | NO-GO | DUPLICATE | Real bounty but two open Arduino Nano PRs and hardware/Discord review burden. |
| `OWASP-BLT/BLT#6185` | $1 GitHub Sponsors deletion | GO->SUBMITTED | HIGH_USER_INPUT | Fast one-file deletion candidate; PR submitted, but repo automation now says only new contributors accepted and friend mention required. |

## Selected implementation
- Issue: https://github.com/OWASP-BLT/BLT/issues/6185
- Parent bounty: https://github.com/OWASP-BLT/BLT/issues/6119
- PR: https://github.com/OWASP-BLT/BLT/pull/6447
- Verification: `git diff --check`; repository-wide reference scan for `android-webview-beta` and `android-webview-beta.png` returned zero matches.

## Red-team finding
After PR submission, repository automation commented that PRs are currently accepted only from new contributors, and another check requires a friend mention. GitHub Sponsors profile/payment setup also may require user-side L4 setup. No further automatic fix is safe.
