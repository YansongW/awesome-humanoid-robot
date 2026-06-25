---
$id: rel_ent_paper_ho_denoising_diffusion_probabilis_2020_uses_ent_inception_score
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_ho_denoising_diffusion_probabilis_2020
  name:
    en: Denoising Diffusion Probabilistic Models
    zh: 去噪扩散概率模型
    ko: 노이즈 제거 확산 확률 모델
target:
  id: ent_inception_score
  name:
    en: Inception Score
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 10_evaluation_benchmarks
description:
  en: The authors report Inception scores to evaluate sample quality.
  zh: 作者使用Inception分数来评估样本质量。
  ko: 저자들은 샘플 품질을 평가하기 위해 Inception 점수를 보고한다.
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: Abstract: ''...we obtain an
    Inception score of 9.46...'''
sources:
- id: src_001
  type: paper
  title: Denoising Diffusion Probabilistic Models
  url: https://arxiv.org/abs/2006.11239
  date: '2020'
  accessed_at: '2026-06-25'
---
