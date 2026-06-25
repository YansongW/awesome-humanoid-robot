---
$id: rel_ent_paper_ho_denoising_diffusion_probabilis_2020_evaluates_on_ent_cifar10
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
  id: ent_cifar10
  name:
    en: CIFAR-10
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 09_data_datasets
description:
  en: The DDPM model was evaluated on the unconditional CIFAR-10 dataset.
  zh: DDPM模型在无条件CIFAR-10数据集上进行了评估。
  ko: DDPM 모델은 무조건 CIFAR-10 데이터셋에서 평가되었다.
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: Abstract: ''On the unconditional
    CIFAR10 dataset, we obtain an Inception score of 9.46 and a state-of-the-art FID
    score of 3.17.'''
sources:
- id: src_001
  type: paper
  title: Denoising Diffusion Probabilistic Models
  url: https://arxiv.org/abs/2006.11239
  date: '2020'
  accessed_at: '2026-06-25'
---
