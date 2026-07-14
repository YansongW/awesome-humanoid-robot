---
$id: ent_paper_radosavovic_learning_humanoid_locomotion_o_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Humanoid Locomotion over Challenging Terrain
  zh: 挑战性地形上的人形机器人运动学习
  ko: 어려운 지형에서의 휴머노이드 보행 학습
summary:
  en: Presents a transformer-based blind locomotion controller for the Digit humanoid robot, pre-trained with sequence modeling
    on flat-ground trajectories and fine-tuned with reinforcement learning on uneven terrain, enabling zero-shot sim-to-real
    traversal of natural and urban environments.
  zh: 提出一种基于Transformer的Digit人形机器人盲态运动控制器，先通过序列建模在平地轨迹上预训练，再通过强化学习在不平坦地形上微调，实现从仿真到现实的零样本迁移，跨越自然与城市环境。
  ko: Digit 휴머노이드 로봇을 위한 Transformer 기반의 시각 정보 없는 보행 컨트롤러를 제안한다. 평지 궤적에 대한 시퀀스 모델링으로 사전 학습하고 불규칙한 지형에 대해 강화 학습으로 미세 조정하여,
    시뮬레이션에서 현실로의 제로샷 전이를 통해 자연 및 도시 환경을 주행할 수 있게 한다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
- 02_components
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- humanoid_locomotion
- blind_locomotion
- transformer
- sequence_modeling
- reinforcement_learning
- sim_to_real
- digit_robot
- agility_robotics
- terrain_traversal
- domain_randomization
- outdoor_navigation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.03654v1.
sources:
- id: src_001
  type: paper
  title: Learning Humanoid Locomotion over Challenging Terrain
  url: https://arxiv.org/abs/2410.03654
  date: '2024'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
Humanoid robots can, in principle, use their legs to go almost anywhere. Developing controllers capable of traversing diverse terrains, however, remains a considerable challenge. Classical controllers are hard to generalize broadly while the learning-based methods have primarily focused on gentle terrains. Here, we present a learning-based approach for blind humanoid locomotion capable of traversing challenging natural and man-made terrain. Our method uses a transformer model to predict the next action based on the history of proprioceptive observations and actions. The model is first pre-trained on a dataset of flat-ground trajectories with sequence modeling, and then fine-tuned on uneven terrain using reinforcement learning. We evaluate our model on a real humanoid robot across a variety of terrains, including rough, deformable, and sloped surfaces. The model demonstrates robust performance, in-context adaptation, and emergent terrain representations. In real-world case studies, our humanoid robot successfully traversed over 4 miles of hiking trails in Berkeley and climbed some of the steepest streets in San Francisco.

## 核心内容
Humanoid robots can, in principle, use their legs to go almost anywhere. Developing controllers capable of traversing diverse terrains, however, remains a considerable challenge. Classical controllers are hard to generalize broadly while the learning-based methods have primarily focused on gentle terrains. Here, we present a learning-based approach for blind humanoid locomotion capable of traversing challenging natural and man-made terrain. Our method uses a transformer model to predict the next action based on the history of proprioceptive observations and actions. The model is first pre-trained on a dataset of flat-ground trajectories with sequence modeling, and then fine-tuned on uneven terrain using reinforcement learning. We evaluate our model on a real humanoid robot across a variety of terrains, including rough, deformable, and sloped surfaces. The model demonstrates robust performance, in-context adaptation, and emergent terrain representations. In real-world case studies, our humanoid robot successfully traversed over 4 miles of hiking trails in Berkeley and climbed some of the steepest streets in San Francisco.

## 参考
- http://arxiv.org/abs/2410.03654v1

