---
$id: ent_paper_gervet_act3d_3d_feature_field_transfo_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Act3D: 3D Feature Field Transformers for Multi-Task Robotic Manipulation'
  zh: Act3D
  ko: 'Act3D: 3D Feature Field Transformers for Multi-Task Robotic Manipulation'
summary:
  en: 'Act3D: 3D Feature Field Transformers for Multi-Task Robotic Manipulation (Act3D), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Carnegie Mellon University, and published at CoRL 2023.'
  zh: 'Act3D: 3D Feature Field Transformers for Multi-Task Robotic Manipulation (Act3D), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Carnegie Mellon University, and published at CoRL 2023.'
  ko: 'Act3D: 3D Feature Field Transformers for Multi-Task Robotic Manipulation (Act3D), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Carnegie Mellon University, and published at CoRL 2023.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- act3d
- generalist_policy
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2306.17817v2.
sources:
- id: src_001
  type: paper
  title: Act3D source
  url: https://proceedings.mlr.press/v229/gervet23a.html
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
3D perceptual representations are well suited for robot manipulation as they easily encode occlusions and simplify spatial reasoning. Many manipulation tasks require high spatial precision in end-effector pose prediction, which typically demands high-resolution 3D feature grids that are computationally expensive to process. As a result, most manipulation policies operate directly in 2D, foregoing 3D inductive biases. In this paper, we introduce Act3D, a manipulation policy transformer that represents the robot's workspace using a 3D feature field with adaptive resolutions dependent on the task at hand. The model lifts 2D pre-trained features to 3D using sensed depth, and attends to them to compute features for sampled 3D points. It samples 3D point grids in a coarse to fine manner, featurizes them using relative-position attention, and selects where to focus the next round of point sampling. In this way, it efficiently computes 3D action maps of high spatial resolution. Act3D sets a new state-of-the-art in RL-Bench, an established manipulation benchmark, where it achieves 10% absolute improvement over the previous SOTA 2D multi-view policy on 74 RLBench tasks and 22% absolute improvement with 3x less compute over the previous SOTA 3D policy. We quantify the importance of relative spatial attention, large-scale vision-language pre-trained 2D backbones, and weight tying across coarse-to-fine attentions in ablative experiments. Code and videos are available on our project website: https://act3d.github.io/.

## 核心内容
3D perceptual representations are well suited for robot manipulation as they easily encode occlusions and simplify spatial reasoning. Many manipulation tasks require high spatial precision in end-effector pose prediction, which typically demands high-resolution 3D feature grids that are computationally expensive to process. As a result, most manipulation policies operate directly in 2D, foregoing 3D inductive biases. In this paper, we introduce Act3D, a manipulation policy transformer that represents the robot's workspace using a 3D feature field with adaptive resolutions dependent on the task at hand. The model lifts 2D pre-trained features to 3D using sensed depth, and attends to them to compute features for sampled 3D points. It samples 3D point grids in a coarse to fine manner, featurizes them using relative-position attention, and selects where to focus the next round of point sampling. In this way, it efficiently computes 3D action maps of high spatial resolution. Act3D sets a new state-of-the-art in RL-Bench, an established manipulation benchmark, where it achieves 10% absolute improvement over the previous SOTA 2D multi-view policy on 74 RLBench tasks and 22% absolute improvement with 3x less compute over the previous SOTA 3D policy. We quantify the importance of relative spatial attention, large-scale vision-language pre-trained 2D backbones, and weight tying across coarse-to-fine attentions in ablative experiments. Code and videos are available on our project website: https://act3d.github.io/.

## 参考
- http://arxiv.org/abs/2306.17817v2

## Overview
3D perceptual representations are well suited for robot manipulation as they easily encode occlusions and simplify spatial reasoning. Many manipulation tasks require high spatial precision in end-effector pose prediction, which typically demands high-resolution 3D feature grids that are computationally expensive to process. As a result, most manipulation policies operate directly in 2D, foregoing 3D inductive biases. In this paper, we introduce Act3D, a manipulation policy transformer that represents the robot's workspace using a 3D feature field with adaptive resolutions dependent on the task at hand. The model lifts 2D pre-trained features to 3D using sensed depth, and attends to them to compute features for sampled 3D points. It samples 3D point grids in a coarse to fine manner, featurizes them using relative-position attention, and selects where to focus the next round of point sampling. In this way, it efficiently computes 3D action maps of high spatial resolution. Act3D sets a new state-of-the-art in RL-Bench, an established manipulation benchmark, where it achieves 10% absolute improvement over the previous SOTA 2D multi-view policy on 74 RLBench tasks and 22% absolute improvement with 3x less compute over the previous SOTA 3D policy. We quantify the importance of relative spatial attention, large-scale vision-language pre-trained 2D backbones, and weight tying across coarse-to-fine attentions in ablative experiments. Code and videos are available on our project website: https://act3d.github.io/.

## Content
3D perceptual representations are well suited for robot manipulation as they easily encode occlusions and simplify spatial reasoning. Many manipulation tasks require high spatial precision in end-effector pose prediction, which typically demands high-resolution 3D feature grids that are computationally expensive to process. As a result, most manipulation policies operate directly in 2D, foregoing 3D inductive biases. In this paper, we introduce Act3D, a manipulation policy transformer that represents the robot's workspace using a 3D feature field with adaptive resolutions dependent on the task at hand. The model lifts 2D pre-trained features to 3D using sensed depth, and attends to them to compute features for sampled 3D points. It samples 3D point grids in a coarse to fine manner, featurizes them using relative-position attention, and selects where to focus the next round of point sampling. In this way, it efficiently computes 3D action maps of high spatial resolution. Act3D sets a new state-of-the-art in RL-Bench, an established manipulation benchmark, where it achieves 10% absolute improvement over the previous SOTA 2D multi-view policy on 74 RLBench tasks and 22% absolute improvement with 3x less compute over the previous SOTA 3D policy. We quantify the importance of relative spatial attention, large-scale vision-language pre-trained 2D backbones, and weight tying across coarse-to-fine attentions in ablative experiments. Code and videos are available on our project website: https://act3d.github.io/.

## 개요
3D 지각 표현은 로봇 조작에 매우 적합한데, 이는 폐색을 쉽게 인코딩하고 공간 추론을 단순화하기 때문입니다. 많은 조작 작업은 엔드 이펙터의 자세 예측에 높은 공간 정밀도를 요구하며, 이는 일반적으로 계산 비용이 많이 드는 고해상도 3D 특징 그리드를 필요로 합니다. 그 결과, 대부분의 조작 정책은 3D 귀납적 편향을 포기하고 2D에서 직접 작동합니다. 본 논문에서는 작업에 따라 적응형 해상도를 가진 3D 특징 필드를 사용하여 로봇의 작업 공간을 표현하는 조작 정책 트랜스포머인 Act3D를 소개합니다. 이 모델은 감지된 깊이를 사용하여 2D 사전 학습 특징을 3D로 변환하고, 이를 주목하여 샘플링된 3D 포인트의 특징을 계산합니다. 또한, 거칠기에서 세밀함까지 3D 포인트 그리드를 샘플링하고, 상대 위치 주의를 사용하여 특징화하며, 다음 포인트 샘플링 라운드에서 집중할 위치를 선택합니다. 이러한 방식으로 높은 공간 해상도의 3D 액션 맵을 효율적으로 계산합니다. Act3D는 확립된 조작 벤치마크인 RL-Bench에서 새로운 최첨단 성능을 달성하며, 74개의 RLBench 작업에서 이전 SOTA 2D 다중 뷰 정책보다 10% 절대적 향상, 이전 SOTA 3D 정책보다 3배 적은 계산량으로 22% 절대적 향상을 보여줍니다. 우리는 절제 실험을 통해 상대 공간 주의, 대규모 비전-언어 사전 학습 2D 백본, 그리고 거칠기에서 세밀함까지의 주의에서 가중치 공유의 중요성을 정량화합니다. 코드와 비디오는 프로젝트 웹사이트에서 확인할 수 있습니다: https://act3d.github.io/.

## 핵심 내용
3D 지각 표현은 로봇 조작에 매우 적합한데, 이는 폐색을 쉽게 인코딩하고 공간 추론을 단순화하기 때문입니다. 많은 조작 작업은 엔드 이펙터의 자세 예측에 높은 공간 정밀도를 요구하며, 이는 일반적으로 계산 비용이 많이 드는 고해상도 3D 특징 그리드를 필요로 합니다. 그 결과, 대부분의 조작 정책은 3D 귀납적 편향을 포기하고 2D에서 직접 작동합니다. 본 논문에서는 작업에 따라 적응형 해상도를 가진 3D 특징 필드를 사용하여 로봇의 작업 공간을 표현하는 조작 정책 트랜스포머인 Act3D를 소개합니다. 이 모델은 감지된 깊이를 사용하여 2D 사전 학습 특징을 3D로 변환하고, 이를 주목하여 샘플링된 3D 포인트의 특징을 계산합니다. 또한, 거칠기에서 세밀함까지 3D 포인트 그리드를 샘플링하고, 상대 위치 주의를 사용하여 특징화하며, 다음 포인트 샘플링 라운드에서 집중할 위치를 선택합니다. 이러한 방식으로 높은 공간 해상도의 3D 액션 맵을 효율적으로 계산합니다. Act3D는 확립된 조작 벤치마크인 RL-Bench에서 새로운 최첨단 성능을 달성하며, 74개의 RLBench 작업에서 이전 SOTA 2D 다중 뷰 정책보다 10% 절대적 향상, 이전 SOTA 3D 정책보다 3배 적은 계산량으로 22% 절대적 향상을 보여줍니다. 우리는 절제 실험을 통해 상대 공간 주의, 대규모 비전-언어 사전 학습 2D 백본, 그리고 거칠기에서 세밀함까지의 주의에서 가중치 공유의 중요성을 정량화합니다. 코드와 비디오는 프로젝트 웹사이트에서 확인할 수 있습니다: https://act3d.github.io/.
