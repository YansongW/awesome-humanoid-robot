---
$id: ent_paper_steadytray_learning_object_bal_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SteadyTray: Learning Object Balancing Tasks in Humanoid Tray Transport via Residual Reinforcement Learning'
  zh: 'SteadyTray: Learning Object Balancing Tasks in Humanoid Tray Transport via Residual Reinforcement Learning'
  ko: 'SteadyTray: Learning Object Balancing Tasks in Humanoid Tray Transport via Residual Reinforcement Learning'
summary:
  en: 'SteadyTray: Learning Object Balancing Tasks in Humanoid Tray Transport via Residual Reinforcement Learning is a 2026
    work on loco-manipulation and whole-body-control for humanoid robots.'
  zh: 'SteadyTray: Learning Object Balancing Tasks in Humanoid Tray Transport via Residual Reinforcement Learning is a 2026
    work on loco-manipulation and whole-body-control for humanoid robots.'
  ko: 'SteadyTray: Learning Object Balancing Tasks in Humanoid Tray Transport via Residual Reinforcement Learning is a 2026
    work on loco-manipulation and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- loco_manipulation
- steadytray
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.10306v1.
sources:
- id: src_001
  type: paper
  title: 'SteadyTray: Learning Object Balancing Tasks in Humanoid Tray Transport via Residual Reinforcement Learning (arXiv)'
  url: https://arxiv.org/abs/2603.10306
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'SteadyTray: Learning Object Balancing Tasks in Humanoid Tray Transport via Residual Reinforcement Learning project
    page'
  url: https://steadytray.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Stabilizing unsecured payloads against the inherent oscillations of dynamic bipedal locomotion remains a critical engineering bottleneck for humanoids in unstructured environments. To solve this, we introduce ReST-RL, a hierarchical reinforcement learning architecture that explicitly decouples locomotion from payload stabilization, evaluated via the SteadyTray benchmark. Rather than relying on monolithic end-to-end learning, our framework integrates a robust base locomotion policy with a dynamic residual module engineered to actively cancel gait-induced perturbations at the end-effector. This architectural separation ensures steady tray transport without degrading the underlying bipedal stability. In simulation, the residual design significantly outperforms end-to-end baselines in gait smoothness and orientation accuracy, achieving a 96.9% success rate in variable velocity tracking and 74.5% robustness against external force disturbances. Successfully deployed on the Unitree G1 humanoid hardware, this modular approach demonstrates highly reliable zero-shot sim-to-real generalization across various objects and external force disturbances.

## 核心内容
Stabilizing unsecured payloads against the inherent oscillations of dynamic bipedal locomotion remains a critical engineering bottleneck for humanoids in unstructured environments. To solve this, we introduce ReST-RL, a hierarchical reinforcement learning architecture that explicitly decouples locomotion from payload stabilization, evaluated via the SteadyTray benchmark. Rather than relying on monolithic end-to-end learning, our framework integrates a robust base locomotion policy with a dynamic residual module engineered to actively cancel gait-induced perturbations at the end-effector. This architectural separation ensures steady tray transport without degrading the underlying bipedal stability. In simulation, the residual design significantly outperforms end-to-end baselines in gait smoothness and orientation accuracy, achieving a 96.9% success rate in variable velocity tracking and 74.5% robustness against external force disturbances. Successfully deployed on the Unitree G1 humanoid hardware, this modular approach demonstrates highly reliable zero-shot sim-to-real generalization across various objects and external force disturbances.

## 参考
- http://arxiv.org/abs/2603.10306v1

## Overview
Stabilizing unsecured payloads against the inherent oscillations of dynamic bipedal locomotion remains a critical engineering bottleneck for humanoids in unstructured environments. To solve this, we introduce ReST-RL, a hierarchical reinforcement learning architecture that explicitly decouples locomotion from payload stabilization, evaluated via the SteadyTray benchmark. Rather than relying on monolithic end-to-end learning, our framework integrates a robust base locomotion policy with a dynamic residual module engineered to actively cancel gait-induced perturbations at the end-effector. This architectural separation ensures steady tray transport without degrading the underlying bipedal stability. In simulation, the residual design significantly outperforms end-to-end baselines in gait smoothness and orientation accuracy, achieving a 96.9% success rate in variable velocity tracking and 74.5% robustness against external force disturbances. Successfully deployed on the Unitree G1 humanoid hardware, this modular approach demonstrates highly reliable zero-shot sim-to-real generalization across various objects and external force disturbances.

## Content
Stabilizing unsecured payloads against the inherent oscillations of dynamic bipedal locomotion remains a critical engineering bottleneck for humanoids in unstructured environments. To solve this, we introduce ReST-RL, a hierarchical reinforcement learning architecture that explicitly decouples locomotion from payload stabilization, evaluated via the SteadyTray benchmark. Rather than relying on monolithic end-to-end learning, our framework integrates a robust base locomotion policy with a dynamic residual module engineered to actively cancel gait-induced perturbations at the end-effector. This architectural separation ensures steady tray transport without degrading the underlying bipedal stability. In simulation, the residual design significantly outperforms end-to-end baselines in gait smoothness and orientation accuracy, achieving a 96.9% success rate in variable velocity tracking and 74.5% robustness against external force disturbances. Successfully deployed on the Unitree G1 humanoid hardware, this modular approach demonstrates highly reliable zero-shot sim-to-real generalization across various objects and external force disturbances.

## 개요
동적 이족 보행의 고유한 진동에 대해 고정되지 않은 탑재물을 안정화하는 것은 비정형 환경에서 휴머노이드 로봇의 핵심적인 공학적 병목 현상으로 남아 있습니다. 이를 해결하기 위해, 우리는 SteadyTray 벤치마크를 통해 평가된, 보행과 탑재물 안정화를 명시적으로 분리하는 계층적 강화 학습 아키텍처인 ReST-RL을 소개합니다. 단일 종단 간 학습에 의존하는 대신, 우리의 프레임워크는 강력한 기본 보행 정책과 말단 효과기에서 보행 유발 섭동을 능동적으로 상쇄하도록 설계된 동적 잔차 모듈을 통합합니다. 이러한 아키텍처 분리는 기본적인 이족 안정성을 저하시키지 않으면서 안정적인 트레이 운반을 보장합니다. 시뮬레이션에서 잔차 설계는 보행 부드러움과 방향 정확도에서 종단 간 기준선을 크게 능가하며, 가변 속도 추적에서 96.9%의 성공률과 외부 힘 섭동에 대해 74.5%의 강건성을 달성합니다. Unitree G1 휴머노이드 하드웨어에 성공적으로 배치된 이 모듈식 접근 방식은 다양한 물체와 외부 힘 섭동에 걸쳐 높은 신뢰성의 제로샷 시뮬레이션-실제 일반화를 입증합니다.

## 핵심 내용
동적 이족 보행의 고유한 진동에 대해 고정되지 않은 탑재물을 안정화하는 것은 비정형 환경에서 휴머노이드 로봇의 핵심적인 공학적 병목 현상으로 남아 있습니다. 이를 해결하기 위해, 우리는 SteadyTray 벤치마크를 통해 평가된, 보행과 탑재물 안정화를 명시적으로 분리하는 계층적 강화 학습 아키텍처인 ReST-RL을 소개합니다. 단일 종단 간 학습에 의존하는 대신, 우리의 프레임워크는 강력한 기본 보행 정책과 말단 효과기에서 보행 유발 섭동을 능동적으로 상쇄하도록 설계된 동적 잔차 모듈을 통합합니다. 이러한 아키텍처 분리는 기본적인 이족 안정성을 저하시키지 않으면서 안정적인 트레이 운반을 보장합니다. 시뮬레이션에서 잔차 설계는 보행 부드러움과 방향 정확도에서 종단 간 기준선을 크게 능가하며, 가변 속도 추적에서 96.9%의 성공률과 외부 힘 섭동에 대해 74.5%의 강건성을 달성합니다. Unitree G1 휴머노이드 하드웨어에 성공적으로 배치된 이 모듈식 접근 방식은 다양한 물체와 외부 힘 섭동에 걸쳐 높은 신뢰성의 제로샷 시뮬레이션-실제 일반화를 입증합니다.
