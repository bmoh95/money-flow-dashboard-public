# Red Team

Failure modes:
1. 업종별 교육기관·대상·비용이 달라 단정하면 HIGH_RISK.
2. 과태료 금액/기한은 연도·지자체·업종별 차이가 있을 수 있어 공식 근거 재확인 필요.
3. 기존 원산지 표시 블로그와 독자가 겹치므로 문장/이미지 구조가 반복되면 WEAK_DIFFERENTIATION.

Decision: HOLD / HIGH_RISK until official wording, images, category, rendered Tistory QA pass.
## 2026-05-20T16:37:22+09:00 — Red Team release check

- 기존 HIGH_RISK: 공식 문구 재확인 및 범위 완화로 해소.
- 실패 모드 1: 업종별 교육기관 단정 → 영업신고증 업종명/기관/지자체 확인 문구로 완화.
- 실패 모드 2: 과태료 금액 단정 → 공식 페이지 재확인으로 완화.
- 실패 모드 3: 개인정보/계정 공유 오해 → 수료증 파일 위치 공유로 완화.
- 결정: GO / tracking.
