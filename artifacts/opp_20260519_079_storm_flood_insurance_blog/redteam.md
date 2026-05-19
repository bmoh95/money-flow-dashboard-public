# Red Team

Failure modes:
1. 보험·지원율은 지역/보험사/연도별로 달라질 수 있어 과도한 단정은 HIGH_RISK.
2. 재난보험 글은 광고성/보험판매성으로 보일 수 있음. 특정 보험사 추천 금지.
3. 카테고리 체계에 보험 전용 child가 없어 발행 전 카테고리 적합성 확인 필요.

Decision: HOLD / HIGH_RISK until official wording, images, public visual QA, category verification pass.
