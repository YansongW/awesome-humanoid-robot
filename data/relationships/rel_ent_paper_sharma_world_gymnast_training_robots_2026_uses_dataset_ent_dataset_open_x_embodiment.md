---
$id: rel_ent_paper_sharma_world_gymnast_training_robots_2026_uses_dataset_ent_dataset_open_x_embodiment
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses_dataset
source:
  id: ent_paper_sharma_world_gymnast_training_robots_2026
  name:
    en: 'World-Gymnast: Training Robots with Reinforcement Learning in a World Model'
    zh: World-Gymnast：在世界模型中利用强化学习训练机器人
    ko: 'World-Gymnast: 월드 모델에서 강화학습으로 로봇 훈련하기'
target:
  id: ent_dataset_open_x_embodiment
  name:
    en: Open X-Embodiment dataset
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 09_data_datasets
description:
  en: Both OpenVLA and the WorldGym variant are pretrained on the Open X-Embodiment
    dataset.
  zh: OpenVLA 和 WorldGym 变体均在 Open X-Embodiment 数据集上预训练。
  ko: OpenVLA와 WorldGym 변형 모델은 Open X-Embodiment 데이터셋으로 사전학습되었다.
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: OpenVLA ... was originally trained
    on Open X-Embodiment dataset (Vuong et al., 2023). For WorldGym, we used a 600M
    parameter variant pretrained on Open X-Embodiment dataset.'
sources:
- id: src_001
  type: paper
  title: 'World-Gymnast: Training Robots with Reinforcement Learning in a World Model'
  url: https://arxiv.org/abs/2602.02454
  date: '2026'
  accessed_at: '2026-06-27'
---


