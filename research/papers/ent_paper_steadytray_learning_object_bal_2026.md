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
  zh: SteadyTray 是 2026 年提出的一项针对人形机器人托盘运输中物体平衡任务的研究。该工作由 ReST-RL 框架实现，通过将运动控制与负载稳定解耦，在仿真中达到 96.9% 的速度跟踪成功率，并成功在 Unitree G1
    人形机器人上实现零样本 sim-to-real 迁移。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.10306v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (611 chars, DeepSeek).'
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
针对双足动态行走中未固定负载的稳定难题，该研究提出了 ReST-RL 分层强化学习架构。该架构将基础运动策略与动态残差模块分离，使末端执行器能主动抵消步态扰动，从而在不破坏双足稳定性的前提下实现托盘平稳运输。在仿真环境中，残差设计在步态平滑度和方向精度上显著优于端到端基线，并在外力干扰下保持 74.5% 的鲁棒性。该模块化方法已成功部署于 Unitree G1 硬件，展现出对不同物体和外力干扰的可靠零样本泛化能力。

## 核心内容
### 核心问题
- 动态双足行走产生的固有振荡是未固定负载稳定的关键瓶颈，尤其在非结构化环境中。

### 方法架构
- **ReST-RL 框架**：采用分层强化学习，将运动控制与负载稳定显式解耦。
- **基础运动策略**：提供稳健的双足行走能力。
- **动态残差模块**：专门设计用于主动抵消步态引起的末端执行器扰动，确保托盘运输平稳。

### 实验设置与关键结果
- **仿真环境**：在 SteadyTray 基准上进行评估。
- **性能对比**：残差设计在步态平滑度和方向精度上显著优于端到端基线。
- **关键数字**：
  - 变速度跟踪成功率：96.9%
  - 外力干扰鲁棒性：74.5%
- **硬件部署**：成功在 Unitree G1 人形机器人上实现零样本 sim-to-real 迁移，验证了模块化方法在不同物体和外部扰动下的可靠性。

## Overview
Stabilizing unsecured payloads against the inherent oscillations of dynamic bipedal locomotion remains a critical engineering bottleneck for humanoids in unstructured environments. To solve this, we introduce ReST-RL, a hierarchical reinforcement learning architecture that explicitly decouples locomotion from payload stabilization, evaluated via the SteadyTray benchmark. Rather than relying on monolithic end-to-end learning, our framework integrates a robust base locomotion policy with a dynamic residual module engineered to actively cancel gait-induced perturbations at the end-effector. This architectural separation ensures steady tray transport without degrading the underlying bipedal stability. In simulation, the residual design significantly outperforms end-to-end baselines in gait smoothness and orientation accuracy, achieving a 96.9% success rate in variable velocity tracking and 74.5% robustness against external force disturbances. Successfully deployed on the Unitree G1 humanoid hardware, this modular approach demonstrates highly reliable zero-shot sim-to-real generalization across various objects and external force disturbances.

## 参考
- http://arxiv.org/abs/2603.10306v1

## 개요
동적 이족 보행 중 고정되지 않은 부하의 안정성 문제를 해결하기 위해, 본 연구는 ReST-RL 계층적 강화 학습 아키텍처를 제안합니다. 이 아키텍처는 기본 운동 정책과 동적 잔차 모듈을 분리하여, 말단 실행기가 보행 교란을 능동적으로 상쇄함으로써 이족 안정성을 해치지 않으면서 트레이를 안정적으로 운반할 수 있게 합니다. 시뮬레이션 환경에서 잔차 설계는 보행 평활도와 방향 정밀도에서 엔드투엔드 기준선보다 현저히 우수했으며, 외부 힘 교란 하에서도 74.5%의 강건성을 유지했습니다. 이 모듈식 접근법은 Unitree G1 하드웨어에 성공적으로 배포되어, 다양한 물체와 외부 힘 교란에 대한 신뢰할 수 있는 제로샷 일반화 능력을 입증했습니다.

## 핵심 내용
### 핵심 문제
- 동적 이족 보행에서 발생하는 고유 진동은 고정되지 않은 부하 안정성의 핵심 병목이며, 특히 비구조화 환경에서 두드러집니다.

### 방법 아키텍처
- **ReST-RL 프레임워크**: 계층적 강화 학습을 사용하여 운동 제어와 부하 안정성을 명시적으로 분리합니다.
- **기본 운동 정책**: 견고한 이족 보행 능력을 제공합니다.
- **동적 잔차 모듈**: 보행으로 인한 말단 실행기 교란을 능동적으로 상쇄하도록 특별히 설계되어, 트레이 운반의 안정성을 보장합니다.

### 실험 설정 및 주요 결과
- **시뮬레이션 환경**: SteadyTray 벤치마크에서 평가되었습니다.
- **성능 비교**: 잔차 설계는 보행 평활도와 방향 정밀도에서 엔드투엔드 기준선보다 현저히 우수했습니다.
- **주요 수치**:
  - 가변 속도 추적 성공률: 96.9%
  - 외부 힘 교란 강건성: 74.5%
- **하드웨어 배포**: Unitree G1 휴머노이드 로봇에서 제로샷 sim-to-real 전이에 성공하여, 다양한 물체와 외부 교란 하에서 모듈식 접근법의 신뢰성을 검증했습니다.
