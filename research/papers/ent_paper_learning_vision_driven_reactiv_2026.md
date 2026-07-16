---
$id: ent_paper_learning_vision_driven_reactiv_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Vision-Driven Reactive Soccer Skills for Humanoid Robots
  zh: 足球任务里，视觉和动作是同一件事
  ko: Learning Vision-Driven Reactive Soccer Skills for Humanoid Robots
summary:
  en: Learning Vision-Driven Reactive Soccer Skills for Humanoid Robots is a knowledge node related to paper in the humanoid
    robot value chain.
  zh: Humanoid soccer poses a representative challenge for embodied intelligence, requiring robots to operate within a tightly
    coupled perception-action loop. However, existing systems typically rely on decoupled modules, resulting in delayed responses
    and incoherent behaviors in dynamic environments, while real-world perceptual limitations further exacerbate these issues.
    In this work, we present a unified reinforcement learning-based controller that enables humanoid robots to acquire reactive
    soccer skills through the direct integration of visual perception and motion control. Our approach extends Adversarial
    Motion Priors to perceptual settings in real-world dynamic environments, bridging motion imitation and visually grounded
    dynamic control. We introduce an encoder-decoder architecture comb
  ko: Learning Vision-Driven Reactive Soccer Skills for Humanoid Robots is a knowledge node related to paper in the humanoid
    robot value chain.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- mobile_manipulation
- task_interface
- visual_closed_loop
- vla
- whole_body_control
- world_model
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.03996v1.
sources:
- id: src_001
  type: paper
  title: Learning Vision-Driven Reactive Soccer Skills for Humanoid Robots (arXiv)
  url: https://arxiv.org/abs/2511.03996
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 足球任务里，视觉和动作是同一件事 project page
  url: https://humanoid-kick.github.io
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
Humanoid soccer poses a representative challenge for embodied intelligence, requiring robots to operate within a tightly coupled perception-action loop. However, existing systems typically rely on decoupled modules, resulting in delayed responses and incoherent behaviors in dynamic environments, while real-world perceptual limitations further exacerbate these issues. In this work, we present a unified reinforcement learning-based controller that enables humanoid robots to acquire reactive soccer skills through the direct integration of visual perception and motion control. Our approach extends Adversarial Motion Priors to perceptual settings in real-world dynamic environments, bridging motion imitation and visually grounded dynamic control. We introduce an encoder-decoder architecture combined with a virtual perception system that models real-world visual characteristics, allowing the policy to recover privileged states from imperfect observations and establish active coordination between perception and action. The resulting controller demonstrates strong reactivity, consistently executing coherent and robust soccer behaviors across various scenarios, including real RoboCup matches.

## 核心内容
Humanoid soccer poses a representative challenge for embodied intelligence, requiring robots to operate within a tightly coupled perception-action loop. However, existing systems typically rely on decoupled modules, resulting in delayed responses and incoherent behaviors in dynamic environments, while real-world perceptual limitations further exacerbate these issues. In this work, we present a unified reinforcement learning-based controller that enables humanoid robots to acquire reactive soccer skills through the direct integration of visual perception and motion control. Our approach extends Adversarial Motion Priors to perceptual settings in real-world dynamic environments, bridging motion imitation and visually grounded dynamic control. We introduce an encoder-decoder architecture combined with a virtual perception system that models real-world visual characteristics, allowing the policy to recover privileged states from imperfect observations and establish active coordination between perception and action. The resulting controller demonstrates strong reactivity, consistently executing coherent and robust soccer behaviors across various scenarios, including real RoboCup matches.

## 参考
- http://arxiv.org/abs/2511.03996v1

## Overview
Humanoid soccer poses a representative challenge for embodied intelligence, requiring robots to operate within a tightly coupled perception-action loop. However, existing systems typically rely on decoupled modules, resulting in delayed responses and incoherent behaviors in dynamic environments, while real-world perceptual limitations further exacerbate these issues. In this work, we present a unified reinforcement learning-based controller that enables humanoid robots to acquire reactive soccer skills through the direct integration of visual perception and motion control. Our approach extends Adversarial Motion Priors to perceptual settings in real-world dynamic environments, bridging motion imitation and visually grounded dynamic control. We introduce an encoder-decoder architecture combined with a virtual perception system that models real-world visual characteristics, allowing the policy to recover privileged states from imperfect observations and establish active coordination between perception and action. The resulting controller demonstrates strong reactivity, consistently executing coherent and robust soccer behaviors across various scenarios, including real RoboCup matches.

## Content
Humanoid soccer poses a representative challenge for embodied intelligence, requiring robots to operate within a tightly coupled perception-action loop. However, existing systems typically rely on decoupled modules, resulting in delayed responses and incoherent behaviors in dynamic environments, while real-world perceptual limitations further exacerbate these issues. In this work, we present a unified reinforcement learning-based controller that enables humanoid robots to acquire reactive soccer skills through the direct integration of visual perception and motion control. Our approach extends Adversarial Motion Priors to perceptual settings in real-world dynamic environments, bridging motion imitation and visually grounded dynamic control. We introduce an encoder-decoder architecture combined with a virtual perception system that models real-world visual characteristics, allowing the policy to recover privileged states from imperfect observations and establish active coordination between perception and action. The resulting controller demonstrates strong reactivity, consistently executing coherent and robust soccer behaviors across various scenarios, including real RoboCup matches.

## 개요
휴머노이드 축구는 체화된 지능의 대표적인 도전 과제로, 로봇이 긴밀하게 결합된 인식-행동 루프 내에서 작동해야 합니다. 그러나 기존 시스템은 일반적으로 분리된 모듈에 의존하여 동적 환경에서 지연된 반응과 일관성 없는 행동을 초래하며, 실제 세계의 인식 한계가 이러한 문제를 더욱 악화시킵니다. 본 연구에서는 시각 인식과 운동 제어를 직접 통합하여 휴머노이드 로봇이 반응형 축구 기술을 습득할 수 있도록 하는 통합 강화 학습 기반 제어기를 제시합니다. 우리의 접근 방식은 적대적 운동 사전(Adversarial Motion Priors)을 실제 동적 환경의 인식 설정으로 확장하여, 운동 모방과 시각 기반 동적 제어를 연결합니다. 실제 세계의 시각적 특성을 모델링하는 가상 인식 시스템과 결합된 인코더-디코더 아키텍처를 도입하여, 정책이 불완전한 관측으로부터 특권 상태를 복구하고 인식과 행동 간의 능동적 조정을 확립할 수 있도록 합니다. 결과적으로 얻어진 제어기는 강력한 반응성을 보여주며, 실제 RoboCup 경기를 포함한 다양한 시나리오에서 일관되고 견고한 축구 행동을 지속적으로 실행합니다.

## 핵심 내용
휴머노이드 축구는 체화된 지능의 대표적인 도전 과제로, 로봇이 긴밀하게 결합된 인식-행동 루프 내에서 작동해야 합니다. 그러나 기존 시스템은 일반적으로 분리된 모듈에 의존하여 동적 환경에서 지연된 반응과 일관성 없는 행동을 초래하며, 실제 세계의 인식 한계가 이러한 문제를 더욱 악화시킵니다. 본 연구에서는 시각 인식과 운동 제어를 직접 통합하여 휴머노이드 로봇이 반응형 축구 기술을 습득할 수 있도록 하는 통합 강화 학습 기반 제어기를 제시합니다. 우리의 접근 방식은 적대적 운동 사전(Adversarial Motion Priors)을 실제 동적 환경의 인식 설정으로 확장하여, 운동 모방과 시각 기반 동적 제어를 연결합니다. 실제 세계의 시각적 특성을 모델링하는 가상 인식 시스템과 결합된 인코더-디코더 아키텍처를 도입하여, 정책이 불완전한 관측으로부터 특권 상태를 복구하고 인식과 행동 간의 능동적 조정을 확립할 수 있도록 합니다. 결과적으로 얻어진 제어기는 강력한 반응성을 보여주며, 실제 RoboCup 경기를 포함한 다양한 시나리오에서 일관되고 견고한 축구 행동을 지속적으로 실행합니다.
