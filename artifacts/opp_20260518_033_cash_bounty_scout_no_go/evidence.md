# Bounty/direct-payout scout

검토 기준: 실제 bounty 여부, open 상태, 중복/경쟁 PR, PR 가능 여부, payout rail, 사용자 관여도, 예상 난이도, 승인/지급 가능성. 콘텐츠 fallback 없음.

1. https://github.com/pschanely/CrossHair/issues/115
   - 근거(A): IssueHunt $100 funded, issue open, PR route works. Reject: active competing PRs #412/#411/#409 already target the trace-performance work; C/Cython tracer benchmark scope is non-trivial for $100 and approval odds are low now.
   - 결정: NO-GO / DUPLICATE

2. https://github.com/sindresorhus/awesome-lint/issues/37
   - 근거(A): IssueHunt $60 funded, issue open, PR route works. Reject: submitted IssueHunt PR #225 already addresses header-image SVG/HiDPI rule and repo has current PRs; duplicate micro-bounty path.
   - 결정: NO-GO / DUPLICATE

3. https://github.com/egoist/majo/issues/9
   - 근거(A): IssueHunt $100 funded, issue open. Reject: submitted PRs #15/#47/#51 plus current PR #53 already implement multiple .source() calls; stale/crowded payout risk.
   - 결정: NO-GO / DUPLICATE

4. https://github.com/sindresorhus/electron-reloader/issues/2
   - 근거(A): IssueHunt $40 funded text is present. Reject: GitHub pulls endpoint returned 404/PR route not usable during preflight; issue is very old with minimal acceptance detail and payment path likely stale.
   - 결정: NO-GO / NO_CHANNEL

5. https://github.com/UnsafeLabs/RFC-5322/issues/1
   - 근거(A): Algora-style $400 issue open and PR route works. Reject: open PR #2 already implements the RFC 5322 parser; full ABNF parser scope is large and previous repo/payment-risk signals remain unacceptable.
   - 결정: NO-GO / DUPLICATE

6. https://github.com/yeheskieltame/claudelance/issues/139
   - 근거(A): Opire/on-chain bounty for 1 CELO, issue open. Reject: token/wallet/stake path (0.1 CELO stake) conflicts with cash/platform preference; open PR #242 appears to implement the PWA manifest/install banner already.
   - 결정: NO-GO / PAYMENT_UNCLEAR

7. https://github.com/ClankerNation/OpenAgents/issues/96
   - 근거(A): $2.4k bounty issue open. Reject: demands full startup/platform initialization text in source file, which is unsafe; repo has ~100 open PRs and PR #345 targets the same task endpoint issue.
   - 결정: NO-GO / HIGH_RISK

8. https://github.com/SecureBananaLabs/bug-bounty/issues/80
   - 근거(A): $780 bounty issue open for pixel-art file. Reject: not code/maintainership work, subjective creative acceptance, many open PRs, and PR #92 already closes #80; approval/payment odds poor.
   - 결정: NO-GO / DUPLICATE

9. https://github.com/organicmaps/organicmaps/issues/7350
   - 근거(A): Official bounty-program issue open with fair remuneration text. Reject for this scout: no fixed payout amount, very large Android screenshot generator scope, 200+ open PRs, likely long review cycle and high setup burden.
   - 결정: NO-GO / LOW_MARGIN

결론: GO 후보 없음. 현금성·플랫폼 지급 명확성·낮은 경쟁도·승인 가능성을 동시에 충족하지 못해 코딩/claim/PR 제출하지 않음.
