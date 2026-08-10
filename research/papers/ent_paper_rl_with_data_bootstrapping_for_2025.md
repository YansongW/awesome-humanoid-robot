---
$id: ent_paper_rl_with_data_bootstrapping_for_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: RL with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation
  zh: RL with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation
  ko: RL with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation
summary:
  en: RL with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation is a 2025 work on navigation for
    humanoid robots.
  zh: RL with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation 是2025年针对人形机器人导航的工作，由研究团队提出。其核心贡献是设计了一个分层框架，结合高层强化学习（RL）规划器和低层模型预测控制（MPC）规划器，并通过数据自举技术加速训练。该方法在Agility
    Robotics Digit人形机器人仿真中验证，显著提升了导航成功率和适应性。
  ko: RL with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation is a 2025 work on navigation for
    humanoid robots.
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
- navigation
- rl_with_data_bootstrapping_for
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.02206v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (637 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: RL with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation (arXiv)
  url: https://arxiv.org/abs/2506.02206
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该工作针对双足机器人导航中计算效率与稳定精度难以平衡的问题，提出了一种分层导航框架。高层使用基于强化学习的规划器，在机器人中心坐标系中动态生成子目标；低层则采用模型预测控制规划器，生成稳健的行走步态以到达这些子目标。为加速并稳定训练过程，研究引入数据自举技术，利用基于模型的导航方法生成多样化、信息丰富的数据集。在Agility Robotics Digit人形机器人的多场景随机障碍物仿真中，该方法相比原始基于模型的方法和其他学习方法，显著提升了导航成功率和适应性。

## 核心内容
### 方法架构
- **高层规划器**：使用强化学习（RL）在机器人中心坐标系中动态选择子目标，引导机器人穿越杂乱环境。
- **低层规划器**：基于模型预测控制（MPC）生成稳健行走步态，确保机器人稳定到达子目标。
- **数据自举技术**：利用基于模型的导航方法生成多样化、信息丰富的数据集，以加速并稳定RL训练过程。

### 实验设置
- **平台**：Agility Robotics Digit 人形机器人。
- **场景**：多场景仿真，包含随机障碍物。
- **对比方法**：原始基于模型的方法及其他学习方法。

### 关键结果
- 导航成功率显著提升。
- 适应性优于对比方法。
- 数据自举技术有效加速训练并提升稳定性。

### 结论
该分层框架通过动态子目标生成与数据自举，有效解决了双足机器人导航中的效率与精度平衡问题，在仿真中验证了其优越性。

## Overview
Safe and real-time navigation is fundamental for humanoid robot applications. However, existing bipedal robot navigation frameworks often struggle to balance computational efficiency with the precision required for stable locomotion. We propose a novel hierarchical framework that continuously generates dynamic subgoals to guide the robot through cluttered environments. Our method comprises a high-level reinforcement learning (RL) planner for subgoal selection in a robot-centric coordinate system and a low-level Model Predictive Control (MPC) based planner which produces robust walking gaits to reach these subgoals. To expedite and stabilize the training process, we incorporate a data bootstrapping technique that leverages a model-based navigation approach to generate a diverse, informative dataset. We validate our method in simulation using the Agility Robotics Digit humanoid across multiple scenarios with random obstacles. Results show that our framework significantly improves navigation success rates and adaptability compared to both the original model-based method and other learning-based methods.

## 参考
- http://arxiv.org/abs/2506.02206v1

## 개요
이 연구는 이족 보행 로봇 내비게이션에서 계산 효율성과 안정적 정밀도 간의 균형을 맞추기 어려운 문제를 해결하기 위해 계층적 내비게이션 프레임워크를 제안한다. 상위 계층은 강화 학습 기반의 플래너를 사용하여 로봇 중심 좌표계에서 동적으로 하위 목표를 생성하고, 하위 계층은 모델 예측 제어 플래너를 사용하여 이러한 하위 목표에 도달하기 위한 견고한 보행 패턴을 생성한다. 훈련 과정을 가속화하고 안정화하기 위해 연구는 모델 기반 내비게이션 방법을 활용하여 다양하고 정보가 풍부한 데이터 세트를 생성하는 데이터 부트스트래핑 기술을 도입한다. Agility Robotics Digit 휴머노이드 로봇의 다중 시나리오 무작위 장애물 시뮬레이션에서 이 방법은 기존 모델 기반 방법 및 다른 학습 방법에 비해 내비게이션 성공률과 적응성을 크게 향상시킨다.

## 핵심 내용
### 방법 아키텍처
- **상위 계층 플래너**: 강화 학습(RL)을 사용하여 로봇 중심 좌표계에서 동적으로 하위 목표를 선택하고, 로봇이 복잡한 환경을 탐색하도록 유도한다.
- **하위 계층 플래너**: 모델 예측 제어(MPC)를 기반으로 견고한 보행 패턴을 생성하여 로봇이 하위 목표에 안정적으로 도달하도록 보장한다.
- **데이터 부트스트래핑 기술**: 모델 기반 내비게이션 방법을 활용하여 다양하고 정보가 풍부한 데이터 세트를 생성함으로써 RL 훈련 과정을 가속화하고 안정화한다.

### 실험 설정
- **플랫폼**: Agility Robotics Digit 휴머노이드 로봇.
- **시나리오**: 무작위 장애물을 포함한 다중 시나리오 시뮬레이션.
- **비교 방법**: 기존 모델 기반 방법 및 기타 학습 방법.

### 주요 결과
- 내비게이션 성공률이 크게 향상됨.
- 적응성이 비교 방법보다 우수함.
- 데이터 부트스트래핑 기술이 훈련을 효과적으로 가속화하고 안정성을 향상시킴.

### 결론
이 계층적 프레임워크는 동적 하위 목표 생성과 데이터 부트스트래핑을 통해 이족 보행 로봇 내비게이션의 효율성과 정밀도 균형 문제를 효과적으로 해결하며, 시뮬레이션에서 그 우수성을 검증했다.
