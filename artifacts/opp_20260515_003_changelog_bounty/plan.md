# Plan — Changelog Generator Bounty

## Scope
Prepare a small, dependency-free bounty submission package for the open GitHub/Opire bounty: generate a structured `CHANGELOG.md` from git history.

## Buyer / channel
- Buyer/payer: `claude-builders-bounty` bounty owner via Opire.
- Channel: GitHub issue claim (`/opire try`) and PR.

## Deliverable
- `changelog.sh`: Bash script.
- `SKILL.md`: Claude Code skill-style documentation.
- `README.md`: 3-step setup instructions.
- `sample-output.md`: output from a real temporary git repo test.

## Differentiator
- Works on macOS default Bash 3.2, not only modern Bash.
- No dependencies.
- Handles no-tag repos by falling back to full history.

## ROI assumptions
- Conservative: 0 KRW if another PR wins or maintainer rejects.
- Base: $50 headline bounty × 50% acceptance probability ≈ 35,000 KRW expected value before any payout friction.
- Optimistic: $50 paid and reusable changelog utility/skill asset for future bounties.

## External approval path
Do not comment, claim, fork, push, or open PR without explicit user approval. Next action after approval: claim issue, create branch/PR with prepared files, include sample output.
