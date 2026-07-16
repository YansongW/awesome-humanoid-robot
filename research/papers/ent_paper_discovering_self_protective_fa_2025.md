---
$id: ent_paper_discovering_self_protective_fa_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Discovering Self-Protective Falling Policy for Humanoid Robot via Deep Reinforcement Learning
  zh: Discovering Self-Protective Falling Policy for Humanoid Robot via Deep Reinforcement Learning
  ko: Discovering Self-Protective Falling Policy for Humanoid Robot via Deep Reinforcement Learning
summary:
  en: Discovering Self-Protective Falling Policy for Humanoid Robot via Deep Reinforcement Learning is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.
  zh: Discovering Self-Protective Falling Policy for Humanoid Robot via Deep Reinforcement Learning is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.
  ko: Discovering Self-Protective Falling Policy for Humanoid Robot via Deep Reinforcement Learning is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- discovering_self_protective_fa
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.01336v1.
sources:
- id: src_001
  type: paper
  title: Discovering Self-Protective Falling Policy for Humanoid Robot via Deep Reinforcement Learning (arXiv)
  url: https://arxiv.org/abs/2512.01336
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots have received significant research interests and advancements in recent years. Despite many successes, due to their morphology, dynamics and limitation of control policy, humanoid robots are prone to fall as compared to other embodiments like quadruped or wheeled robots. And its large weight, tall Center of Mass, high Degree-of-Freedom would cause serious hardware damages when falling uncontrolled, to both itself and surrounding objects. Existing researches in this field mostly focus on using control based methods that struggle to cater diverse falling scenarios and may introduce unsuitable human prior. On the other hand, large-scale Deep Reinforcement Learning and Curriculum Learning could be employed to incentivize humanoid agent discovering falling protection policy that fits its own nature and property. In this work, with carefully designed reward functions and domain diversification curriculum, we successfully train humanoid agent to explore falling protection behaviors and discover that by forming a `triangle' structure, the falling damages could be significantly reduced with its rigid-material body. With comprehensive metrics and experiments, we quantify its performance with comparison to other methods, visualize its falling behaviors and successfully transfer it to real world platform.

## 核心内容
Humanoid robots have received significant research interests and advancements in recent years. Despite many successes, due to their morphology, dynamics and limitation of control policy, humanoid robots are prone to fall as compared to other embodiments like quadruped or wheeled robots. And its large weight, tall Center of Mass, high Degree-of-Freedom would cause serious hardware damages when falling uncontrolled, to both itself and surrounding objects. Existing researches in this field mostly focus on using control based methods that struggle to cater diverse falling scenarios and may introduce unsuitable human prior. On the other hand, large-scale Deep Reinforcement Learning and Curriculum Learning could be employed to incentivize humanoid agent discovering falling protection policy that fits its own nature and property. In this work, with carefully designed reward functions and domain diversification curriculum, we successfully train humanoid agent to explore falling protection behaviors and discover that by forming a `triangle' structure, the falling damages could be significantly reduced with its rigid-material body. With comprehensive metrics and experiments, we quantify its performance with comparison to other methods, visualize its falling behaviors and successfully transfer it to real world platform.

## 参考
- http://arxiv.org/abs/2512.01336v1

## Overview
Humanoid robots have received significant research interests and advancements in recent years. Despite many successes, due to their morphology, dynamics and limitation of control policy, humanoid robots are prone to fall as compared to other embodiments like quadruped or wheeled robots. And its large weight, tall Center of Mass, high Degree-of-Freedom would cause serious hardware damages when falling uncontrolled, to both itself and surrounding objects. Existing researches in this field mostly focus on using control based methods that struggle to cater diverse falling scenarios and may introduce unsuitable human prior. On the other hand, large-scale Deep Reinforcement Learning and Curriculum Learning could be employed to incentivize humanoid agent discovering falling protection policy that fits its own nature and property. In this work, with carefully designed reward functions and domain diversification curriculum, we successfully train humanoid agent to explore falling protection behaviors and discover that by forming a `triangle' structure, the falling damages could be significantly reduced with its rigid-material body. With comprehensive metrics and experiments, we quantify its performance with comparison to other methods, visualize its falling behaviors and successfully transfer it to real world platform.

## Content
Humanoid robots have received significant research interests and advancements in recent years. Despite many successes, due to their morphology, dynamics and limitation of control policy, humanoid robots are prone to fall as compared to other embodiments like quadruped or wheeled robots. And its large weight, tall Center of Mass, high Degree-of-Freedom would cause serious hardware damages when falling uncontrolled, to both itself and surrounding objects. Existing researches in this field mostly focus on using control based methods that struggle to cater diverse falling scenarios and may introduce unsuitable human prior. On the other hand, large-scale Deep Reinforcement Learning and Curriculum Learning could be employed to incentivize humanoid agent discovering falling protection policy that fits its own nature and property. In this work, with carefully designed reward functions and domain diversification curriculum, we successfully train humanoid agent to explore falling protection behaviors and discover that by forming a `triangle' structure, the falling damages could be significantly reduced with its rigid-material body. With comprehensive metrics and experiments, we quantify its performance with comparison to other methods, visualize its falling behaviors and successfully transfer it to real world platform.

## 개요
휴머노이드 로봇은 최근 몇 년간 상당한 연구 관심과 발전을 이루었습니다. 많은 성공에도 불구하고, 휴머노이드 로봇은 형태, 역학 및 제어 정책의 한계로 인해 사족 보행 로봇이나 바퀴 달린 로봇과 같은 다른 형태에 비해 넘어지기 쉽습니다. 또한, 큰 무게, 높은 질량 중심, 높은 자유도는 통제되지 않은 낙하 시 로봇 자체와 주변 물체 모두에 심각한 하드웨어 손상을 초래할 수 있습니다. 이 분야의 기존 연구는 주로 다양한 낙하 시나리오를 처리하는 데 어려움을 겪고 부적절한 인간 사전 지식을 도입할 수 있는 제어 기반 방법에 초점을 맞추고 있습니다. 반면, 대규모 심층 강화 학습 및 커리큘럼 학습을 활용하여 휴머노이드 에이전트가 자신의 본성과 특성에 맞는 낙하 보호 정책을 발견하도록 유도할 수 있습니다. 본 연구에서는 신중하게 설계된 보상 함수와 도메인 다양화 커리큘럼을 통해 휴머노이드 에이전트가 낙하 보호 행동을 탐색하도록 성공적으로 훈련시켰으며, '삼각형' 구조를 형성함으로써 강체 재질의 몸체로 낙하 손상을 크게 줄일 수 있음을 발견했습니다. 포괄적인 지표와 실험을 통해 다른 방법과의 성능을 정량화하고, 낙하 행동을 시각화하며, 실제 세계 플랫폼으로 성공적으로 전이했습니다.

## 핵심 내용
휴머노이드 로봇은 최근 몇 년간 상당한 연구 관심과 발전을 이루었습니다. 많은 성공에도 불구하고, 휴머노이드 로봇은 형태, 역학 및 제어 정책의 한계로 인해 사족 보행 로봇이나 바퀴 달린 로봇과 같은 다른 형태에 비해 넘어지기 쉽습니다. 또한, 큰 무게, 높은 질량 중심, 높은 자유도는 통제되지 않은 낙하 시 로봇 자체와 주변 물체 모두에 심각한 하드웨어 손상을 초래할 수 있습니다. 이 분야의 기존 연구는 주로 다양한 낙하 시나리오를 처리하는 데 어려움을 겪고 부적절한 인간 사전 지식을 도입할 수 있는 제어 기반 방법에 초점을 맞추고 있습니다. 반면, 대규모 심층 강화 학습 및 커리큘럼 학습을 활용하여 휴머노이드 에이전트가 자신의 본성과 특성에 맞는 낙하 보호 정책을 발견하도록 유도할 수 있습니다. 본 연구에서는 신중하게 설계된 보상 함수와 도메인 다양화 커리큘럼을 통해 휴머노이드 에이전트가 낙하 보호 행동을 탐색하도록 성공적으로 훈련시켰으며, '삼각형' 구조를 형성함으로써 강체 재질의 몸체로 낙하 손상을 크게 줄일 수 있음을 발견했습니다. 포괄적인 지표와 실험을 통해 다른 방법과의 성능을 정량화하고, 낙하 행동을 시각화하며, 실제 세계 플랫폼으로 성공적으로 전이했습니다.
