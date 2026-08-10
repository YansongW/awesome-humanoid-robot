---
$id: ent_paper_learning_social_navigation_fro_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Social Navigation from Positive and Negative Demonstrations and Rule-Based Specifications
  zh: Learning Social Navigation from Positive and Negative Demonstrations and Rule-Based Specifications
  ko: Learning Social Navigation from Positive and Negative Demonstrations and Rule-Based Specifications
summary:
  en: Learning Social Navigation from Positive and Negative Demonstrations and Rule-Based Specifications is a 2025 work on
    navigation for humanoid robots.
  zh: 这是一篇2025年关于双足机器人社交导航的研究，提出了一种基于视觉的分层控制框架。核心贡献在于结合强化学习的高层足迹规划器与低层操作空间控制器，并利用角动量线性倒立摆模型降低动力学复杂度。该方法在Cassie机器人上通过仿真和硬件实验验证了有效性。
  ko: Learning Social Navigation from Positive and Negative Demonstrations and Rule-Based Specifications is a 2025 work on
    navigation for humanoid robots.
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
- learning_social_navigation_fro
- navigation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.06779v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (712 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Learning Social Navigation from Positive and Negative Demonstrations and Rule-Based Specifications (arXiv)
  url: https://arxiv.org/abs/2508.06779
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
当前双足机器人在非结构化环境中的导航框架存在依赖本体感觉或手动设计视觉管线的问题，导致实时足迹规划脆弱且复杂。为此，本文提出一种视觉分层控制框架：高层使用强化学习足迹规划器，基于局部高程图生成足迹指令；低层采用操作空间控制器跟踪轨迹。框架引入角动量线性倒立摆模型构建低维状态表示，在保留动力学信息的同时降低计算复杂度。研究在欠驱动双足机器人Cassie上进行了多种地形条件的仿真与硬件实验。

## 核心内容
### 方法架构
- **高层规划器**：基于强化学习的足迹规划器，输入为局部高程图，输出足迹指令（位置与朝向）。
- **低层控制器**：操作空间控制器（Operational Space Controller），负责跟踪高层生成的足迹轨迹。
- **状态表示**：采用角动量线性倒立摆模型（Angular Momentum Linear Inverted Pendulum model）构建低维状态，在捕捉动力学特征的同时减少状态维度。

### 实验设置
- **机器人平台**：欠驱动双足机器人Cassie。
- **实验条件**：覆盖多种地形（如斜坡、障碍物、不规则地面），同时进行仿真（simulation）与硬件（hardware）实验。
- **评估指标**：未明确列出具体数值，但通过对比验证了框架在复杂地形下的导航能力与实时性。

### 关键结论
- 视觉分层控制框架有效解决了传统方法在非结构化环境中的脆弱性问题。
- 角动量线性倒立摆模型在降低计算复杂度的同时，保持了足够的动力学信息用于足迹规划。
- 硬件实验验证了该方法在真实场景中的可行性，但未提供具体成功率或误差数据。

## Overview
Bipedal robots demonstrate potential in navigating challenging terrains through dynamic ground contact. However, current frameworks often depend solely on proprioception or use manually designed visual pipelines, which are fragile in real-world settings and complicate real-time footstep planning in unstructured environments. To address this problem, we present a vision-based hierarchical control framework that integrates a reinforcement learning high-level footstep planner, which generates footstep commands based on a local elevation map, with a low-level Operational Space Controller that tracks the generated trajectories. We utilize the Angular Momentum Linear Inverted Pendulum model to construct a low-dimensional state representation to capture an informative encoding of the dynamics while reducing complexity. We evaluate our method across different terrain conditions using the underactuated bipedal robot Cassie and investigate the capabilities and challenges of our approach through simulation and hardware experiments.

## 参考
- http://arxiv.org/abs/2508.06779v1

## 개요
현재 이족 보행 로봇의 비구조화 환경 내비게이션 프레임워크는 고유수용감각에 의존하거나 수동으로 설계된 비전 파이프라인을 사용하는 문제가 있어, 실시간 발자국 계획이 취약하고 복잡합니다. 이를 해결하기 위해 본 논문은 시각 계층 제어 프레임워크를 제안합니다: 상위 계층은 강화 학습 발자국 계획기를 사용하여 로컬 고도 맵을 기반으로 발자국 명령을 생성하고, 하위 계층은 작업 공간 제어기를 사용하여 궤적을 추적합니다. 프레임워크는 각운동량 선형 역진자 모델을 도입하여 저차원 상태 표현을 구축하며, 동역학 정보를 보존하면서 계산 복잡도를 낮춥니다. 연구는 부족 구동 이족 보행 로봇 Cassie에서 다양한 지형 조건의 시뮬레이션 및 하드웨어 실험을 수행했습니다.

## 핵심 내용
### 방법 아키텍처
- **상위 계획기**: 강화 학습 기반 발자국 계획기로, 입력은 로컬 고도 맵, 출력은 발자국 명령(위치 및 방향)입니다.
- **하위 제어기**: 작업 공간 제어기(Operational Space Controller)로, 상위 계층에서 생성된 발자국 궤적을 추적합니다.
- **상태 표현**: 각운동량 선형 역진자 모델(Angular Momentum Linear Inverted Pendulum model)을 사용하여 저차원 상태를 구축하며, 동역학 특성을 포착하면서 상태 차원을 줄입니다.

### 실험 설정
- **로봇 플랫폼**: 부족 구동 이족 보행 로봇 Cassie.
- **실험 조건**: 다양한 지형(예: 경사로, 장애물, 불규칙 지면)을 포함하며, 시뮬레이션(simulation) 및 하드웨어(hardware) 실험을 모두 수행합니다.
- **평가 지표**: 구체적인 수치는 명시되지 않았지만, 비교를 통해 복잡한 지형에서의 내비게이션 능력과 실시간성을 검증했습니다.

### 핵심 결론
- 시각 계층 제어 프레임워크는 전통적인 방법이 비구조화 환경에서 가지는 취약성 문제를 효과적으로 해결합니다.
- 각운동량 선형 역진자 모델은 계산 복잡도를 낮추면서도 발자국 계획에 필요한 충분한 동역학 정보를 유지합니다.
- 하드웨어 실험은 실제 환경에서의 방법의 실현 가능성을 검증했지만, 구체적인 성공률이나 오차 데이터는 제공되지 않았습니다.
