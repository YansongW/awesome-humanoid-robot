---
$id: ent_paper_chen_see_once_then_act_vision_langu_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'See Once, Then Act: Vision-Language-Action Model with Task Learning from One-Shot Video Demonstrations'
  zh: ViVLA
  ko: 'See Once, Then Act: Vision-Language-Action Model with Task Learning from One-Shot Video Demonstrations'
summary:
  en: 'See Once, Then Act: Vision-Language-Action Model with Task Learning from One-Shot Video Demonstrations (ViVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Beijing Institute of Technology, LimX
    Dynamics.'
  zh: 'See Once, Then Act: Vision-Language-Action Model with Task Learning from One-Shot Video Demonstrations (ViVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Beijing Institute of Technology, LimX
    Dynamics.'
  ko: 'See Once, Then Act: Vision-Language-Action Model with Task Learning from One-Shot Video Demonstrations (ViVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Beijing Institute of Technology, LimX
    Dynamics.'
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
- robotic_manipulation
- vision_language_action
- vivla
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.07582v1.
sources:
- id: src_001
  type: paper
  title: 'See Once, Then Act: Vision-Language-Action Model with Task Learning from One-Shot Video Demonstrations (arXiv)'
  url: https://arxiv.org/abs/2512.07582
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ViVLA source
  url: https://doi.org/10.48550/arXiv.2512.07582
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Developing robust and general-purpose manipulation policies represents a fundamental objective in robotics research. While Vision-Language-Action (VLA) models have demonstrated promising capabilities for end-to-end robot control, existing approaches still exhibit limited generalization to tasks beyond their training distributions. In contrast, humans possess remarkable proficiency in acquiring novel skills by simply observing others performing them once. Inspired by this capability, we propose ViVLA, a generalist robotic manipulation policy that achieves efficient task learning from a single expert demonstration video at test time. Our approach jointly processes an expert demonstration video alongside the robot's visual observations to predict both the demonstrated action sequences and subsequent robot actions, effectively distilling fine-grained manipulation knowledge from expert behavior and transferring it seamlessly to the agent. To enhance the performance of ViVLA, we develop a scalable expert-agent pair data generation pipeline capable of synthesizing paired trajectories from easily accessible human videos, further augmented by curated pairs from publicly available datasets. This pipeline produces a total of 892,911 expert-agent samples for training ViVLA. Experimental results demonstrate that our ViVLA is able to acquire novel manipulation skills from only a single expert demonstration video at test time. Our approach achieves over 30% improvement on unseen LIBERO tasks and maintains above 35% gains with cross-embodiment videos. Real-world experiments demonstrate effective learning from human videos, yielding more than 38% improvement on unseen tasks.

## 核心内容
Developing robust and general-purpose manipulation policies represents a fundamental objective in robotics research. While Vision-Language-Action (VLA) models have demonstrated promising capabilities for end-to-end robot control, existing approaches still exhibit limited generalization to tasks beyond their training distributions. In contrast, humans possess remarkable proficiency in acquiring novel skills by simply observing others performing them once. Inspired by this capability, we propose ViVLA, a generalist robotic manipulation policy that achieves efficient task learning from a single expert demonstration video at test time. Our approach jointly processes an expert demonstration video alongside the robot's visual observations to predict both the demonstrated action sequences and subsequent robot actions, effectively distilling fine-grained manipulation knowledge from expert behavior and transferring it seamlessly to the agent. To enhance the performance of ViVLA, we develop a scalable expert-agent pair data generation pipeline capable of synthesizing paired trajectories from easily accessible human videos, further augmented by curated pairs from publicly available datasets. This pipeline produces a total of 892,911 expert-agent samples for training ViVLA. Experimental results demonstrate that our ViVLA is able to acquire novel manipulation skills from only a single expert demonstration video at test time. Our approach achieves over 30% improvement on unseen LIBERO tasks and maintains above 35% gains with cross-embodiment videos. Real-world experiments demonstrate effective learning from human videos, yielding more than 38% improvement on unseen tasks.

## 参考
- http://arxiv.org/abs/2512.07582v1

## Overview
Developing robust and general-purpose manipulation policies represents a fundamental objective in robotics research. While Vision-Language-Action (VLA) models have demonstrated promising capabilities for end-to-end robot control, existing approaches still exhibit limited generalization to tasks beyond their training distributions. In contrast, humans possess remarkable proficiency in acquiring novel skills by simply observing others performing them once. Inspired by this capability, we propose ViVLA, a generalist robotic manipulation policy that achieves efficient task learning from a single expert demonstration video at test time. Our approach jointly processes an expert demonstration video alongside the robot's visual observations to predict both the demonstrated action sequences and subsequent robot actions, effectively distilling fine-grained manipulation knowledge from expert behavior and transferring it seamlessly to the agent. To enhance the performance of ViVLA, we develop a scalable expert-agent pair data generation pipeline capable of synthesizing paired trajectories from easily accessible human videos, further augmented by curated pairs from publicly available datasets. This pipeline produces a total of 892,911 expert-agent samples for training ViVLA. Experimental results demonstrate that our ViVLA is able to acquire novel manipulation skills from only a single expert demonstration video at test time. Our approach achieves over 30% improvement on unseen LIBERO tasks and maintains above 35% gains with cross-embodiment videos. Real-world experiments demonstrate effective learning from human videos, yielding more than 38% improvement on unseen tasks.

## Content
Developing robust and general-purpose manipulation policies represents a fundamental objective in robotics research. While Vision-Language-Action (VLA) models have demonstrated promising capabilities for end-to-end robot control, existing approaches still exhibit limited generalization to tasks beyond their training distributions. In contrast, humans possess remarkable proficiency in acquiring novel skills by simply observing others performing them once. Inspired by this capability, we propose ViVLA, a generalist robotic manipulation policy that achieves efficient task learning from a single expert demonstration video at test time. Our approach jointly processes an expert demonstration video alongside the robot's visual observations to predict both the demonstrated action sequences and subsequent robot actions, effectively distilling fine-grained manipulation knowledge from expert behavior and transferring it seamlessly to the agent. To enhance the performance of ViVLA, we develop a scalable expert-agent pair data generation pipeline capable of synthesizing paired trajectories from easily accessible human videos, further augmented by curated pairs from publicly available datasets. This pipeline produces a total of 892,911 expert-agent samples for training ViVLA. Experimental results demonstrate that our ViVLA is able to acquire novel manipulation skills from only a single expert demonstration video at test time. Our approach achieves over 30% improvement on unseen LIBERO tasks and maintains above 35% gains with cross-embodiment videos. Real-world experiments demonstrate effective learning from human videos, yielding more than 38% improvement on unseen tasks.

## 개요
강건하고 범용적인 조작 정책을 개발하는 것은 로봇 공학 연구의 근본적인 목표입니다. Vision-Language-Action(VLA) 모델은 엔드투엔드 로봇 제어에서 유망한 능력을 보여주었지만, 기존 접근 방식은 훈련 분포를 벗어난 작업에 대한 일반화가 여전히 제한적입니다. 반면, 인간은 다른 사람이 한 번 수행하는 것을 관찰하는 것만으로 새로운 기술을 습득하는 놀라운 능력을 가지고 있습니다. 이러한 능력에 영감을 받아, 우리는 테스트 시점에 단일 전문가 시연 비디오만으로 효율적인 작업 학습을 달성하는 범용 로봇 조작 정책인 ViVLA를 제안합니다. 우리의 접근 방식은 전문가 시연 비디오와 로봇의 시각적 관찰을 함께 처리하여 시연된 행동 시퀀스와 후속 로봇 행동을 모두 예측함으로써, 전문가 행동에서 세분화된 조작 지식을 효과적으로 추출하고 이를 에이전트에 원활하게 전이합니다. ViVLA의 성능을 향상시키기 위해, 우리는 쉽게 접근 가능한 인간 비디오에서 쌍을 이룬 궤적을 합성할 수 있는 확장 가능한 전문가-에이전트 쌍 데이터 생성 파이프라인을 개발하고, 공개 데이터셋에서 선별된 쌍으로 추가 보강했습니다. 이 파이프라인은 ViVLA 훈련을 위해 총 892,911개의 전문가-에이전트 샘플을 생성합니다. 실험 결과는 ViVLA가 테스트 시점에 단일 전문가 시연 비디오만으로 새로운 조작 기술을 습득할 수 있음을 보여줍니다. 우리의 접근 방식은 보지 못한 LIBERO 작업에서 30% 이상의 개선을 달성하고, 교차 체현 비디오에서도 35% 이상의 이득을 유지합니다. 실제 환경 실험은 인간 비디오로부터의 효과적인 학습을 입증하며, 보지 못한 작업에서 38% 이상의 개선을 보여줍니다.

## 핵심 내용
강건하고 범용적인 조작 정책을 개발하는 것은 로봇 공학 연구의 근본적인 목표입니다. Vision-Language-Action(VLA) 모델은 엔드투엔드 로봇 제어에서 유망한 능력을 보여주었지만, 기존 접근 방식은 훈련 분포를 벗어난 작업에 대한 일반화가 여전히 제한적입니다. 반면, 인간은 다른 사람이 한 번 수행하는 것을 관찰하는 것만으로 새로운 기술을 습득하는 놀라운 능력을 가지고 있습니다. 이러한 능력에 영감을 받아, 우리는 테스트 시점에 단일 전문가 시연 비디오만으로 효율적인 작업 학습을 달성하는 범용 로봇 조작 정책인 ViVLA를 제안합니다. 우리의 접근 방식은 전문가 시연 비디오와 로봇의 시각적 관찰을 함께 처리하여 시연된 행동 시퀀스와 후속 로봇 행동을 모두 예측함으로써, 전문가 행동에서 세분화된 조작 지식을 효과적으로 추출하고 이를 에이전트에 원활하게 전이합니다. ViVLA의 성능을 향상시키기 위해, 우리는 쉽게 접근 가능한 인간 비디오에서 쌍을 이룬 궤적을 합성할 수 있는 확장 가능한 전문가-에이전트 쌍 데이터 생성 파이프라인을 개발하고, 공개 데이터셋에서 선별된 쌍으로 추가 보강했습니다. 이 파이프라인은 ViVLA 훈련을 위해 총 892,911개의 전문가-에이전트 샘플을 생성합니다. 실험 결과는 ViVLA가 테스트 시점에 단일 전문가 시연 비디오만으로 새로운 조작 기술을 습득할 수 있음을 보여줍니다. 우리의 접근 방식은 보지 못한 LIBERO 작업에서 30% 이상의 개선을 달성하고, 교차 체현 비디오에서도 35% 이상의 이득을 유지합니다. 실제 환경 실험은 인간 비디오로부터의 효과적인 학습을 입증하며, 보지 못한 작업에서 38% 이상의 개선을 보여줍니다.
