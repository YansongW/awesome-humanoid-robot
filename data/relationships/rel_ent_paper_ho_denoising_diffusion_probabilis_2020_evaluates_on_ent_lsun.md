---
$id: rel_ent_paper_ho_denoising_diffusion_probabilis_2020_evaluates_on_ent_lsun
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: evaluates_on
source:
  id: ent_paper_ho_denoising_diffusion_probabilis_2020
  name:
    en: Denoising Diffusion Probabilistic Models
    zh: 去噪扩散概率模型
    ko: 노이즈 제거 확산 확률 모델
target:
  id: ent_lsun
  name:
    en: LSUN
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 09_data_datasets
description:
  en: The model was evaluated on 256x256 LSUN bedroom, church, and cat datasets.
  zh: 该模型在256x256 LSUN卧室、教堂和猫数据集上进行了评估。
  ko: 해당 모델은 256x256 LSUN bedroom, church, cat 데이터셋에서 평가되었다.
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: Abstract: ''On 256x256 LSUN,
    we obtain sample quality similar to ProgressiveGAN.'''
sources:
- id: src_001
  type: paper
  title: Denoising Diffusion Probabilistic Models
  url: https://arxiv.org/abs/2006.11239
  date: '2020'
  accessed_at: '2026-06-25'
---
