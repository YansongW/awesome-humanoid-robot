---
$id: ent_paper_hafo_a_force_adaptive_control_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HAFO: A Force-Adaptive Control Framework for Humanoid Robots in Intense Interaction Environments'
  zh: 'HAFO: A Force-Adaptive Control Framework for Humanoid Robots in Intense Interaction Environments'
  ko: 'HAFO: A Force-Adaptive Control Framework for Humanoid Robots in Intense Interaction Environments'
summary:
  en: 'HAFO: A Force-Adaptive Control Framework for Humanoid Robots in Intense Interaction Environments is a 2025 work on
    loco-manipulation and whole-body-control for humanoid robots.'
  zh: 'HAFO: A Force-Adaptive Control Framework for Humanoid Robots in Intense Interaction Environments is a 2025 work on
    loco-manipulation and whole-body-control for humanoid robots.'
  ko: 'HAFO: A Force-Adaptive Control Framework for Humanoid Robots in Intense Interaction Environments is a 2025 work on
    loco-manipulation and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- hafo
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.20275v4.
sources:
- id: src_001
  type: paper
  title: 'HAFO: A Force-Adaptive Control Framework for Humanoid Robots in Intense Interaction Environments (arXiv)'
  url: https://arxiv.org/abs/2511.20275
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Reinforcement learning (RL) controllers have made impressive progress in humanoid locomotion and light-weight object manipulation. However, achieving robust and precise motion control with intense force interaction remains a significant challenge. To address these limitations, this paper proposes HAFO, a dual-agent reinforcement learning framework that concurrently optimizes both a robust locomotion strategy and a precise upper-body manipulation strategy via coupled training. We employ a constrained residual action space to improve dual-agent training stability and sample efficiency. The external tension disturbances are explicitly modeled using a spring-damper system, allowing for fine-grained force control through manipulation of the virtual spring. In this process, the reinforcement learning policy autonomously generates a disturbance-rejection response by utilizing environmental feedback. The experimental results demonstrate that HAFO achieves whole-body control for humanoid robots across diverse force-interaction environments using a single dual-agent policy, delivering outstanding performance under load-bearing and thrust-disturbance conditions, while maintaining stable operation even under rope suspension state.

## 核心内容
Reinforcement learning (RL) controllers have made impressive progress in humanoid locomotion and light-weight object manipulation. However, achieving robust and precise motion control with intense force interaction remains a significant challenge. To address these limitations, this paper proposes HAFO, a dual-agent reinforcement learning framework that concurrently optimizes both a robust locomotion strategy and a precise upper-body manipulation strategy via coupled training. We employ a constrained residual action space to improve dual-agent training stability and sample efficiency. The external tension disturbances are explicitly modeled using a spring-damper system, allowing for fine-grained force control through manipulation of the virtual spring. In this process, the reinforcement learning policy autonomously generates a disturbance-rejection response by utilizing environmental feedback. The experimental results demonstrate that HAFO achieves whole-body control for humanoid robots across diverse force-interaction environments using a single dual-agent policy, delivering outstanding performance under load-bearing and thrust-disturbance conditions, while maintaining stable operation even under rope suspension state.

## 参考
- http://arxiv.org/abs/2511.20275v4

## Overview
Reinforcement learning (RL) controllers have made impressive progress in humanoid locomotion and light-weight object manipulation. However, achieving robust and precise motion control with intense force interaction remains a significant challenge. To address these limitations, this paper proposes HAFO, a dual-agent reinforcement learning framework that concurrently optimizes both a robust locomotion strategy and a precise upper-body manipulation strategy via coupled training. We employ a constrained residual action space to improve dual-agent training stability and sample efficiency. The external tension disturbances are explicitly modeled using a spring-damper system, allowing for fine-grained force control through manipulation of the virtual spring. In this process, the reinforcement learning policy autonomously generates a disturbance-rejection response by utilizing environmental feedback. The experimental results demonstrate that HAFO achieves whole-body control for humanoid robots across diverse force-interaction environments using a single dual-agent policy, delivering outstanding performance under load-bearing and thrust-disturbance conditions, while maintaining stable operation even under rope suspension state.

## Content
Reinforcement learning (RL) controllers have made impressive progress in humanoid locomotion and light-weight object manipulation. However, achieving robust and precise motion control with intense force interaction remains a significant challenge. To address these limitations, this paper proposes HAFO, a dual-agent reinforcement learning framework that concurrently optimizes both a robust locomotion strategy and a precise upper-body manipulation strategy via coupled training. We employ a constrained residual action space to improve dual-agent training stability and sample efficiency. The external tension disturbances are explicitly modeled using a spring-damper system, allowing for fine-grained force control through manipulation of the virtual spring. In this process, the reinforcement learning policy autonomously generates a disturbance-rejection response by utilizing environmental feedback. The experimental results demonstrate that HAFO achieves whole-body control for humanoid robots across diverse force-interaction environments using a single dual-agent policy, delivering outstanding performance under load-bearing and thrust-disturbance conditions, while maintaining stable operation even under rope suspension state.

## 개요
강화 학습(RL) 기반 제어기는 인간형 로봇의 보행 및 경량 물체 조작 분야에서 인상적인 발전을 이루었습니다. 그러나 강한 힘 상호작용이 수반되는 환경에서 견고하고 정밀한 동작 제어를 달성하는 것은 여전히 중요한 과제로 남아 있습니다. 이러한 한계를 극복하기 위해 본 논문에서는 HAFO를 제안합니다. HAFO는 이중 에이전트 강화 학습 프레임워크로, 결합 훈련을 통해 견고한 보행 전략과 정밀한 상체 조작 전략을 동시에 최적화합니다. 제한된 잔여 행동 공간을 활용하여 이중 에이전트 훈련의 안정성과 샘플 효율성을 향상시킵니다. 외부 장력 교란은 스프링-댐퍼 시스템을 사용하여 명시적으로 모델링되며, 가상 스프링의 조작을 통해 세밀한 힘 제어가 가능합니다. 이 과정에서 강화 학습 정책은 환경 피드백을 활용하여 교란 억제 응답을 자동으로 생성합니다. 실험 결과는 HAFO가 단일 이중 에이전트 정책을 사용하여 다양한 힘 상호작용 환경에서 인간형 로봇의 전신 제어를 달성하며, 하중 지지 및 추력 교란 조건에서 뛰어난 성능을 발휘하고, 로프 매달림 상태에서도 안정적인 작동을 유지함을 보여줍니다.

## 핵심 내용
강화 학습(RL) 기반 제어기는 인간형 로봇의 보행 및 경량 물체 조작 분야에서 인상적인 발전을 이루었습니다. 그러나 강한 힘 상호작용이 수반되는 환경에서 견고하고 정밀한 동작 제어를 달성하는 것은 여전히 중요한 과제로 남아 있습니다. 이러한 한계를 극복하기 위해 본 논문에서는 HAFO를 제안합니다. HAFO는 이중 에이전트 강화 학습 프레임워크로, 결합 훈련을 통해 견고한 보행 전략과 정밀한 상체 조작 전략을 동시에 최적화합니다. 제한된 잔여 행동 공간을 활용하여 이중 에이전트 훈련의 안정성과 샘플 효율성을 향상시킵니다. 외부 장력 교란은 스프링-댐퍼 시스템을 사용하여 명시적으로 모델링되며, 가상 스프링의 조작을 통해 세밀한 힘 제어가 가능합니다. 이 과정에서 강화 학습 정책은 환경 피드백을 활용하여 교란 억제 응답을 자동으로 생성합니다. 실험 결과는 HAFO가 단일 이중 에이전트 정책을 사용하여 다양한 힘 상호작용 환경에서 인간형 로봇의 전신 제어를 달성하며, 하중 지지 및 추력 교란 조건에서 뛰어난 성능을 발휘하고, 로프 매달림 상태에서도 안정적인 작동을 유지함을 보여줍니다.
