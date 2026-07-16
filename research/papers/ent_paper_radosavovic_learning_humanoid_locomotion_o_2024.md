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

## Overview
Humanoid robots can, in principle, use their legs to go almost anywhere. Developing controllers capable of traversing diverse terrains, however, remains a considerable challenge. Classical controllers are hard to generalize broadly while the learning-based methods have primarily focused on gentle terrains. Here, we present a learning-based approach for blind humanoid locomotion capable of traversing challenging natural and man-made terrain. Our method uses a transformer model to predict the next action based on the history of proprioceptive observations and actions. The model is first pre-trained on a dataset of flat-ground trajectories with sequence modeling, and then fine-tuned on uneven terrain using reinforcement learning. We evaluate our model on a real humanoid robot across a variety of terrains, including rough, deformable, and sloped surfaces. The model demonstrates robust performance, in-context adaptation, and emergent terrain representations. In real-world case studies, our humanoid robot successfully traversed over 4 miles of hiking trails in Berkeley and climbed some of the steepest streets in San Francisco.

## Content
Humanoid robots can, in principle, use their legs to go almost anywhere. Developing controllers capable of traversing diverse terrains, however, remains a considerable challenge. Classical controllers are hard to generalize broadly while the learning-based methods have primarily focused on gentle terrains. Here, we present a learning-based approach for blind humanoid locomotion capable of traversing challenging natural and man-made terrain. Our method uses a transformer model to predict the next action based on the history of proprioceptive observations and actions. The model is first pre-trained on a dataset of flat-ground trajectories with sequence modeling, and then fine-tuned on uneven terrain using reinforcement learning. We evaluate our model on a real humanoid robot across a variety of terrains, including rough, deformable, and sloped surfaces. The model demonstrates robust performance, in-context adaptation, and emergent terrain representations. In real-world case studies, our humanoid robot successfully traversed over 4 miles of hiking trails in Berkeley and climbed some of the steepest streets in San Francisco.

## 개요
휴머노이드 로봇은 원칙적으로 다리를 사용하여 거의 모든 곳으로 이동할 수 있습니다. 그러나 다양한 지형을 횡단할 수 있는 제어기를 개발하는 것은 여전히 상당한 도전 과제로 남아 있습니다. 고전적인 제어기는 광범위하게 일반화하기 어려운 반면, 학습 기반 방법은 주로 완만한 지형에 초점을 맞추어 왔습니다. 본 연구에서는 까다로운 자연 및 인공 지형을 횡단할 수 있는 블라인드 휴머노이드 보행을 위한 학습 기반 접근법을 제시합니다. 우리의 방법은 고유수용성 관측과 행동의 이력을 기반으로 다음 행동을 예측하기 위해 트랜스포머 모델을 사용합니다. 이 모델은 먼저 시퀀스 모델링을 통해 평지 궤적 데이터셋에서 사전 학습된 후, 강화 학습을 사용하여 울퉁불퉁한 지형에서 미세 조정됩니다. 우리는 거친 지형, 변형 가능한 지형, 경사면을 포함한 다양한 지형에서 실제 휴머노이드 로봇으로 모델을 평가합니다. 이 모델은 강력한 성능, 맥락 내 적응, 그리고 창발적인 지형 표현을 보여줍니다. 실제 사례 연구에서, 우리의 휴머노이드 로봇은 버클리에서 4마일 이상의 하이킹 트레일을 성공적으로 횡단하고 샌프란시스코에서 가장 가파른 거리 중 일부를 올랐습니다.

## 핵심 내용
휴머노이드 로봇은 원칙적으로 다리를 사용하여 거의 모든 곳으로 이동할 수 있습니다. 그러나 다양한 지형을 횡단할 수 있는 제어기를 개발하는 것은 여전히 상당한 도전 과제로 남아 있습니다. 고전적인 제어기는 광범위하게 일반화하기 어려운 반면, 학습 기반 방법은 주로 완만한 지형에 초점을 맞추어 왔습니다. 본 연구에서는 까다로운 자연 및 인공 지형을 횡단할 수 있는 블라인드 휴머노이드 보행을 위한 학습 기반 접근법을 제시합니다. 우리의 방법은 고유수용성 관측과 행동의 이력을 기반으로 다음 행동을 예측하기 위해 트랜스포머 모델을 사용합니다. 이 모델은 먼저 시퀀스 모델링을 통해 평지 궤적 데이터셋에서 사전 학습된 후, 강화 학습을 사용하여 울퉁불퉁한 지형에서 미세 조정됩니다. 우리는 거친 지형, 변형 가능한 지형, 경사면을 포함한 다양한 지형에서 실제 휴머노이드 로봇으로 모델을 평가합니다. 이 모델은 강력한 성능, 맥락 내 적응, 그리고 창발적인 지형 표현을 보여줍니다. 실제 사례 연구에서, 우리의 휴머노이드 로봇은 버클리에서 4마일 이상의 하이킹 트레일을 성공적으로 횡단하고 샌프란시스코에서 가장 가파른 거리 중 일부를 올랐습니다.
