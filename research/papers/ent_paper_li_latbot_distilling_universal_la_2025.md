---
$id: ent_paper_li_latbot_distilling_universal_la_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LatBot: Distilling Universal Latent Actions for Vision-Language-Action Models'
  zh: LatBot
  ko: 'LatBot: Distilling Universal Latent Actions for Vision-Language-Action Models'
summary:
  en: 'LatBot: Distilling Universal Latent Actions for Vision-Language-Action Models (LatBot), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Institute of Microelectronics, Chinese Academy of Sciences, University of
    Chinese Academy of Sciences, Microsoft Research.'
  zh: 'LatBot: Distilling Universal Latent Actions for Vision-Language-Action Models (LatBot), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Institute of Microelectronics, Chinese Academy of Sciences, University of
    Chinese Academy of Sciences, Microsoft Research.'
  ko: 'LatBot: Distilling Universal Latent Actions for Vision-Language-Action Models (LatBot), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Institute of Microelectronics, Chinese Academy of Sciences, University of
    Chinese Academy of Sciences, Microsoft Research.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- latbot
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.23034v1.
sources:
- id: src_001
  type: paper
  title: 'LatBot: Distilling Universal Latent Actions for Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2511.23034
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: LatBot source
  url: https://doi.org/10.48550/arXiv.2511.23034
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Learning transferable latent actions from large-scale object manipulation videos can significantly enhance generalization in downstream robotics tasks, as such representations are agnostic to different robot embodiments. Existing approaches primarily rely on visual reconstruction objectives while neglecting physical priors, leading to sub-optimal performance in learning universal representations. To address these challenges, we propose a Universal Latent Action Learning framework that takes task instructions and multiple frames as inputs, and optimizes both future frame reconstruction and action sequence prediction. Unlike prior works, incorporating action predictions (e.g., gripper or hand trajectories and orientations) allows the model to capture richer physical priors such as real-world distances and orientations, thereby enabling seamless transferability to downstream tasks. We further decompose the latent actions into learnable motion and scene tokens to distinguish the robot's active movements from environmental changes, thus filtering out irrelevant dynamics. By distilling the learned latent actions into the latest VLA models, we achieve strong performance across both simulated (SIMPLER and LIBERO) and real-world robot settings. Notably, with only 10 real-world trajectories per task collected on a Franka robot, our approach successfully completes all five challenging tasks, demonstrating strong few-shot transferability in robotic manipulation.

## 核心内容
Learning transferable latent actions from large-scale object manipulation videos can significantly enhance generalization in downstream robotics tasks, as such representations are agnostic to different robot embodiments. Existing approaches primarily rely on visual reconstruction objectives while neglecting physical priors, leading to sub-optimal performance in learning universal representations. To address these challenges, we propose a Universal Latent Action Learning framework that takes task instructions and multiple frames as inputs, and optimizes both future frame reconstruction and action sequence prediction. Unlike prior works, incorporating action predictions (e.g., gripper or hand trajectories and orientations) allows the model to capture richer physical priors such as real-world distances and orientations, thereby enabling seamless transferability to downstream tasks. We further decompose the latent actions into learnable motion and scene tokens to distinguish the robot's active movements from environmental changes, thus filtering out irrelevant dynamics. By distilling the learned latent actions into the latest VLA models, we achieve strong performance across both simulated (SIMPLER and LIBERO) and real-world robot settings. Notably, with only 10 real-world trajectories per task collected on a Franka robot, our approach successfully completes all five challenging tasks, demonstrating strong few-shot transferability in robotic manipulation.

## 参考
- http://arxiv.org/abs/2511.23034v1

## Overview
Learning transferable latent actions from large-scale object manipulation videos can significantly enhance generalization in downstream robotics tasks, as such representations are agnostic to different robot embodiments. Existing approaches primarily rely on visual reconstruction objectives while neglecting physical priors, leading to sub-optimal performance in learning universal representations. To address these challenges, we propose a Universal Latent Action Learning framework that takes task instructions and multiple frames as inputs, and optimizes both future frame reconstruction and action sequence prediction. Unlike prior works, incorporating action predictions (e.g., gripper or hand trajectories and orientations) allows the model to capture richer physical priors such as real-world distances and orientations, thereby enabling seamless transferability to downstream tasks. We further decompose the latent actions into learnable motion and scene tokens to distinguish the robot's active movements from environmental changes, thus filtering out irrelevant dynamics. By distilling the learned latent actions into the latest VLA models, we achieve strong performance across both simulated (SIMPLER and LIBERO) and real-world robot settings. Notably, with only 10 real-world trajectories per task collected on a Franka robot, our approach successfully completes all five challenging tasks, demonstrating strong few-shot transferability in robotic manipulation.

## Content
Learning transferable latent actions from large-scale object manipulation videos can significantly enhance generalization in downstream robotics tasks, as such representations are agnostic to different robot embodiments. Existing approaches primarily rely on visual reconstruction objectives while neglecting physical priors, leading to sub-optimal performance in learning universal representations. To address these challenges, we propose a Universal Latent Action Learning framework that takes task instructions and multiple frames as inputs, and optimizes both future frame reconstruction and action sequence prediction. Unlike prior works, incorporating action predictions (e.g., gripper or hand trajectories and orientations) allows the model to capture richer physical priors such as real-world distances and orientations, thereby enabling seamless transferability to downstream tasks. We further decompose the latent actions into learnable motion and scene tokens to distinguish the robot's active movements from environmental changes, thus filtering out irrelevant dynamics. By distilling the learned latent actions into the latest VLA models, we achieve strong performance across both simulated (SIMPLER and LIBERO) and real-world robot settings. Notably, with only 10 real-world trajectories per task collected on a Franka robot, our approach successfully completes all five challenging tasks, demonstrating strong few-shot transferability in robotic manipulation.

## 개요
대규모 객체 조작 비디오에서 전이 가능한 잠재 행동을 학습하면 다운스트림 로봇 작업의 일반화 능력을 크게 향상시킬 수 있습니다. 이러한 표현은 다양한 로봇 구현 방식에 구애받지 않기 때문입니다. 기존 접근법은 주로 시각적 재구성 목표에 의존하면서 물리적 사전 지식을 무시하여, 보편적 표현 학습에서 최적 이하의 성능을 초래합니다. 이러한 문제를 해결하기 위해, 우리는 작업 명령과 여러 프레임을 입력으로 받아 미래 프레임 재구성과 행동 시퀀스 예측을 동시에 최적화하는 보편적 잠재 행동 학습 프레임워크를 제안합니다. 기존 연구와 달리, 행동 예측(예: 그리퍼 또는 손의 궤적 및 방향)을 통합함으로써 모델이 실제 세계의 거리 및 방향과 같은 더 풍부한 물리적 사전 지식을 포착할 수 있어, 다운스트림 작업으로의 원활한 전이를 가능하게 합니다. 또한, 잠재 행동을 학습 가능한 모션 토큰과 장면 토큰으로 분해하여 로봇의 능동적 움직임과 환경 변화를 구별함으로써, 무관한 역학을 걸러냅니다. 학습된 잠재 행동을 최신 VLA 모델에 증류함으로써, 시뮬레이션(SIMPLER 및 LIBERO)과 실제 로봇 환경 모두에서 강력한 성능을 달성했습니다. 특히, Franka 로봇에서 작업당 10개의 실제 궤적만 수집하여도, 우리의 접근법은 다섯 가지 도전적인 작업을 모두 성공적으로 완료하여, 로봇 조작에서 강력한 소수 샷 전이 능력을 입증했습니다.

## 핵심 내용
대규모 객체 조작 비디오에서 전이 가능한 잠재 행동을 학습하면 다운스트림 로봇 작업의 일반화 능력을 크게 향상시킬 수 있습니다. 이러한 표현은 다양한 로봇 구현 방식에 구애받지 않기 때문입니다. 기존 접근법은 주로 시각적 재구성 목표에 의존하면서 물리적 사전 지식을 무시하여, 보편적 표현 학습에서 최적 이하의 성능을 초래합니다. 이러한 문제를 해결하기 위해, 우리는 작업 명령과 여러 프레임을 입력으로 받아 미래 프레임 재구성과 행동 시퀀스 예측을 동시에 최적화하는 보편적 잠재 행동 학습 프레임워크를 제안합니다. 기존 연구와 달리, 행동 예측(예: 그리퍼 또는 손의 궤적 및 방향)을 통합함으로써 모델이 실제 세계의 거리 및 방향과 같은 더 풍부한 물리적 사전 지식을 포착할 수 있어, 다운스트림 작업으로의 원활한 전이를 가능하게 합니다. 또한, 잠재 행동을 학습 가능한 모션 토큰과 장면 토큰으로 분해하여 로봇의 능동적 움직임과 환경 변화를 구별함으로써, 무관한 역학을 걸러냅니다. 학습된 잠재 행동을 최신 VLA 모델에 증류함으로써, 시뮬레이션(SIMPLER 및 LIBERO)과 실제 로봇 환경 모두에서 강력한 성능을 달성했습니다. 특히, Franka 로봇에서 작업당 10개의 실제 궤적만 수집하여도, 우리의 접근법은 다섯 가지 도전적인 작업을 모두 성공적으로 완료하여, 로봇 조작에서 강력한 소수 샷 전이 능력을 입증했습니다.
