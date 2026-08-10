---
$id: ent_paper_sombolestan_hierarchical_adaptive_loco_man_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Hierarchical Adaptive Loco-manipulation Control for Quadruped Robots
  zh: 面向四足机器人的分层自适应移动操作控制
  ko: 사족 로봇을 위한 계층적 적응형 이동-조작 제어
summary:
  en: Proposes a hierarchical adaptive control framework that enables quadruped robots to perform loco-manipulation without
    assuming object mass, terrain friction, or slope, and experimentally validates it on a Unitree A1 robot manipulating unknown
    time-varying loads up to 7 kg.
  zh: 本文提出一种分层自适应控制框架，使四足机器人在无需预知物体质量、地形摩擦系数或坡度的情况下完成移动操作任务。该方法在Unitree A1机器人上实验验证，成功操控未知时变负载达7千克（占机器人自重的60%），并能快速适应20°斜坡及不同摩擦系数的地面。
  ko: 사족 로봇이 물체 질량, 지형 마찰 또는 경사를 사전에 알 필요 없이 이동-조작 작업을 수행할 수 있게 하는 계층적 적응형 제어 프레임워크를 제안하고, Unitree A1 로봇에서 최대 7 kg의 미지 시변
    하중을 조작하여 실험적으로 검증한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- loco_manipulation
- adaptive_control
- model_predictive_control
- quadruped_robot
- unitree_a1
- force_control
- whole_body_control
- unknown_object_manipulation
- terrain_adaptation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2209.13145v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (564 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Hierarchical Adaptive Loco-manipulation Control for Quadruped Robots
  url: https://arxiv.org/abs/2209.13145
  date: '2023'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
针对四足机器人在未知环境中同时执行移动与操作任务的挑战，本文提出分层自适应控制框架。该框架首先通过自适应操作控制模块调节接触力，以操控未知物体于未知地形；随后引入统一模型预测控制（MPC），将操作力纳入机器人动力学模型，在保持平衡的同时有效调节机器人与物体间的交互力。实验在Unitree A1机器人上验证，可操控未知时变负载达7千克（占自重的60%），并快速适应20°斜坡及不同摩擦系数的地面。

## 核心内容
### 方法架构
- **分层自适应控制框架**：包含两层核心模块
  - **自适应操作控制**：无需物体质量、摩擦系数或地形坡度先验信息，通过实时调节接触力实现未知物体操控
  - **统一模型预测控制（MPC）**：将操作力显式纳入机器人动力学模型，在平衡约束下优化交互力调控

### 实验设置
- **硬件平台**：Unitree A1四足机器人
- **负载测试**：操控未知时变负载，最大负载达7千克（占机器人自重的60%）
- **地形适应性**：成功适应20°未知斜坡及不同摩擦系数的地面表面

### 关键结论
- 框架无需任何物体或地形参数先验假设，实现端到端自适应控制
- 在最大负载条件下仍能保持机器人平衡与操作稳定性
- 对未知地形参数（坡度、摩擦系数）展现出快速适应能力

## Overview
Legged robots have shown remarkable advantages in navigating uneven terrain. However, realizing effective locomotion and manipulation tasks on quadruped robots is still challenging. In addition, object and terrain parameters are generally unknown to the robot in these problems. Therefore, this paper proposes a hierarchical adaptive control framework that enables legged robots to perform loco-manipulation tasks without any given assumption on the object's mass, the friction coefficient, or the slope of the terrain. In our approach, we first present an adaptive manipulation control to regulate the contact force to manipulate an unknown object on unknown terrain. We then introduce a unified model predictive control (MPC) for loco-manipulation that takes into account the manipulation force in our robot dynamics. The proposed MPC framework thus can effectively regulate the interaction force between the robot and the object while keeping the robot balance. Experimental validation of our proposed approach is successfully conducted on a Unitree A1 robot, allowing it to manipulate an unknown time-varying load up to $7$ $kg$ ($60\%$ of the robot's weight). Moreover, our framework enables fast adaptation to unknown slopes (up to $20^\circ$) or different surfaces with different friction coefficients.

## 参考
- http://arxiv.org/abs/2209.13145v2

## 개요
사족 로봇이 알려지지 않은 환경에서 이동과 조작 작업을 동시에 수행하는 과제에 대해, 본 논문은 계층적 적응 제어 프레임워크를 제안한다. 이 프레임워크는 먼저 적응형 조작 제어 모듈을 통해 접촉력을 조절하여 알려지지 않은 지형에서 미지의 물체를 조작한다. 이후 통합 모델 예측 제어(MPC)를 도입하여 조작력을 로봇 동역학 모델에 포함시키고, 균형을 유지하면서 로봇과 물체 간의 상호작용력을 효과적으로 조절한다. 실험은 Unitree A1 로봇에서 검증되었으며, 알려지지 않은 시변 하중 최대 7kg(자체 중량의 60%)을 조작하고, 20° 경사 및 다양한 마찰 계수의 지면에 빠르게 적응할 수 있었다.

## 핵심 내용
### 방법 구조
- **계층적 적응 제어 프레임워크**: 두 개의 핵심 모듈을 포함
  - **적응형 조작 제어**: 물체 질량, 마찰 계수 또는 지형 경사에 대한 사전 정보 없이 실시간 접촉력 조절을 통해 미지의 물체를 조작
  - **통합 모델 예측 제어(MPC)**: 조작력을 로봇 동역학 모델에 명시적으로 포함시키고, 균형 제약 조건 하에서 상호작용력 조절을 최적화

### 실험 설정
- **하드웨어 플랫폼**: Unitree A1 사족 로봇
- **하중 테스트**: 알려지지 않은 시변 하중 조작, 최대 하중 7kg(로봇 자체 중량의 60%)
- **지형 적응성**: 20° 알려지지 않은 경사 및 다양한 마찰 계수의 지면 표면에 성공적으로 적응

### 핵심 결론
- 프레임워크는 물체 또는 지형 매개변수에 대한 사전 가정 없이 종단 간 적응 제어를 구현
- 최대 하중 조건에서도 로봇 균형과 조작 안정성을 유지
- 알려지지 않은 지형 매개변수(경사, 마찰 계수)에 대한 빠른 적응 능력을 입증
