---
$id: ent_paper_park_acg_action_coherence_guidance_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ACG: Action Coherence Guidance for Flow-based VLA models'
  zh: ACG
  ko: 'ACG: Action Coherence Guidance for Flow-based VLA models'
summary:
  en: 'ACG: Action Coherence Guidance for Flow-based VLA models (ACG), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by KAIST AI.'
  zh: 'ACG: Action Coherence Guidance for Flow-based VLA models (ACG), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by KAIST AI.'
  ko: 'ACG: Action Coherence Guidance for Flow-based VLA models (ACG), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by KAIST AI.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- acg
- large_vla_model
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.22201v2.
sources:
- id: src_001
  type: paper
  title: 'ACG: Action Coherence Guidance for Flow-based VLA models (arXiv)'
  url: https://arxiv.org/abs/2510.22201
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ACG source
  url: https://doi.org/10.48550/arXiv.2510.22201
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Diffusion and flow matching models have emerged as powerful robot policies, enabling Vision-Language-Action (VLA) models to generalize across diverse scenes and instructions. Yet, when trained via imitation learning, their high generative capacity makes them sensitive to noise in human demonstrations: jerks, pauses, and jitter which reduce action coherence. Reduced action coherence causes instability and trajectory drift during deployment, failures that are catastrophic in fine-grained manipulation where precision is crucial. In this paper, we present Action Coherence Guidance (ACG) for VLA models, a training-free test-time guidance algorithm that improves action coherence and thereby yields performance gains. Evaluated on RoboCasa, DexMimicGen, and real-world SO-101 tasks, ACG consistently improves action coherence and boosts success rates across diverse manipulation tasks. Code and project page are available at https://github.com/DAVIAN-Robotics/ACG and https://DAVIAN-Robotics.github.io/ACG , respectively.

## 核心内容
Diffusion and flow matching models have emerged as powerful robot policies, enabling Vision-Language-Action (VLA) models to generalize across diverse scenes and instructions. Yet, when trained via imitation learning, their high generative capacity makes them sensitive to noise in human demonstrations: jerks, pauses, and jitter which reduce action coherence. Reduced action coherence causes instability and trajectory drift during deployment, failures that are catastrophic in fine-grained manipulation where precision is crucial. In this paper, we present Action Coherence Guidance (ACG) for VLA models, a training-free test-time guidance algorithm that improves action coherence and thereby yields performance gains. Evaluated on RoboCasa, DexMimicGen, and real-world SO-101 tasks, ACG consistently improves action coherence and boosts success rates across diverse manipulation tasks. Code and project page are available at https://github.com/DAVIAN-Robotics/ACG and https://DAVIAN-Robotics.github.io/ACG , respectively.

## 参考
- http://arxiv.org/abs/2510.22201v2

## Overview
Diffusion and flow matching models have emerged as powerful robot policies, enabling Vision-Language-Action (VLA) models to generalize across diverse scenes and instructions. Yet, when trained via imitation learning, their high generative capacity makes them sensitive to noise in human demonstrations: jerks, pauses, and jitter which reduce action coherence. Reduced action coherence causes instability and trajectory drift during deployment, failures that are catastrophic in fine-grained manipulation where precision is crucial. In this paper, we present Action Coherence Guidance (ACG) for VLA models, a training-free test-time guidance algorithm that improves action coherence and thereby yields performance gains. Evaluated on RoboCasa, DexMimicGen, and real-world SO-101 tasks, ACG consistently improves action coherence and boosts success rates across diverse manipulation tasks. Code and project page are available at https://github.com/DAVIAN-Robotics/ACG and https://DAVIAN-Robotics.github.io/ACG , respectively.

## Content
Diffusion and flow matching models have emerged as powerful robot policies, enabling Vision-Language-Action (VLA) models to generalize across diverse scenes and instructions. Yet, when trained via imitation learning, their high generative capacity makes them sensitive to noise in human demonstrations: jerks, pauses, and jitter which reduce action coherence. Reduced action coherence causes instability and trajectory drift during deployment, failures that are catastrophic in fine-grained manipulation where precision is crucial. In this paper, we present Action Coherence Guidance (ACG) for VLA models, a training-free test-time guidance algorithm that improves action coherence and thereby yields performance gains. Evaluated on RoboCasa, DexMimicGen, and real-world SO-101 tasks, ACG consistently improves action coherence and boosts success rates across diverse manipulation tasks. Code and project page are available at https://github.com/DAVIAN-Robotics/ACG and https://DAVIAN-Robotics.github.io/ACG , respectively.

## 개요
확산 및 흐름 매칭 모델은 강력한 로봇 정책으로 부상하여, Vision-Language-Action (VLA) 모델이 다양한 장면과 명령에 걸쳐 일반화할 수 있게 했습니다. 그러나 모방 학습을 통해 훈련될 때, 이들의 높은 생성 능력은 인간 시연의 노이즈(급격한 움직임, 일시 정지, 떨림)에 민감하게 만들어 행동 일관성을 저하시킵니다. 행동 일관성 저하는 배포 중 불안정성과 궤적 드리프트를 유발하며, 정밀성이 중요한 세밀한 조작 작업에서 치명적인 실패로 이어집니다. 본 논문에서는 VLA 모델을 위한 Action Coherence Guidance (ACG)를 제시합니다. 이는 훈련 없이 테스트 시점에 적용되는 가이던스 알고리즘으로, 행동 일관성을 개선하여 성능 향상을 가져옵니다. RoboCasa, DexMimicGen 및 실제 세계 SO-101 작업에서 평가된 ACG는 다양한 조작 작업에서 행동 일관성을 지속적으로 개선하고 성공률을 높입니다. 코드와 프로젝트 페이지는 각각 https://github.com/DAVIAN-Robotics/ACG 및 https://DAVIAN-Robotics.github.io/ACG 에서 확인할 수 있습니다.

## 핵심 내용
확산 및 흐름 매칭 모델은 강력한 로봇 정책으로 부상하여, Vision-Language-Action (VLA) 모델이 다양한 장면과 명령에 걸쳐 일반화할 수 있게 했습니다. 그러나 모방 학습을 통해 훈련될 때, 이들의 높은 생성 능력은 인간 시연의 노이즈(급격한 움직임, 일시 정지, 떨림)에 민감하게 만들어 행동 일관성을 저하시킵니다. 행동 일관성 저하는 배포 중 불안정성과 궤적 드리프트를 유발하며, 정밀성이 중요한 세밀한 조작 작업에서 치명적인 실패로 이어집니다. 본 논문에서는 VLA 모델을 위한 Action Coherence Guidance (ACG)를 제시합니다. 이는 훈련 없이 테스트 시점에 적용되는 가이던스 알고리즘으로, 행동 일관성을 개선하여 성능 향상을 가져옵니다. RoboCasa, DexMimicGen 및 실제 세계 SO-101 작업에서 평가된 ACG는 다양한 조작 작업에서 행동 일관성을 지속적으로 개선하고 성공률을 높입니다. 코드와 프로젝트 페이지는 각각 https://github.com/DAVIAN-Robotics/ACG 및 https://DAVIAN-Robotics.github.io/ACG 에서 확인할 수 있습니다.
