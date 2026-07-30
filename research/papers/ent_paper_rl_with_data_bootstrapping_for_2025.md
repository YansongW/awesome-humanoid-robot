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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.02206v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
안전하고 실시간 내비게이션은 인간형 로봇 응용 분야의 기본 요소입니다. 그러나 기존의 이족 보행 로봇 내비게이션 프레임워크는 안정적인 보행에 필요한 정밀도와 계산 효율성 사이의 균형을 맞추는 데 어려움을 겪는 경우가 많습니다. 우리는 복잡한 환경에서 로봇을 안내하기 위해 동적 하위 목표를 지속적으로 생성하는 새로운 계층적 프레임워크를 제안합니다. 본 방법은 로봇 중심 좌표계에서 하위 목표를 선택하는 고수준 강화 학습(RL) 플래너와 이러한 하위 목표에 도달하기 위한 강건한 보행 패턴을 생성하는 저수준 모델 예측 제어(MPC) 기반 플래너로 구성됩니다. 훈련 과정을 가속화하고 안정화하기 위해, 모델 기반 내비게이션 접근 방식을 활용하여 다양하고 유용한 데이터셋을 생성하는 데이터 부트스트래핑 기법을 통합합니다. 우리는 Agility Robotics Digit 휴머노이드를 사용하여 무작위 장애물이 있는 여러 시나리오에서 시뮬레이션을 통해 방법을 검증합니다. 결과는 우리의 프레임워크가 원래의 모델 기반 방법 및 다른 학습 기반 방법과 비교하여 내비게이션 성공률과 적응성을 크게 향상시킴을 보여줍니다.

## 핵심 내용
안전하고 실시간 내비게이션은 인간형 로봇 응용 분야의 기본 요소입니다. 그러나 기존의 이족 보행 로봇 내비게이션 프레임워크는 안정적인 보행에 필요한 정밀도와 계산 효율성 사이의 균형을 맞추는 데 어려움을 겪는 경우가 많습니다. 우리는 복잡한 환경에서 로봇을 안내하기 위해 동적 하위 목표를 지속적으로 생성하는 새로운 계층적 프레임워크를 제안합니다. 본 방법은 로봇 중심 좌표계에서 하위 목표를 선택하는 고수준 강화 학습(RL) 플래너와 이러한 하위 목표에 도달하기 위한 강건한 보행 패턴을 생성하는 저수준 모델 예측 제어(MPC) 기반 플래너로 구성됩니다. 훈련 과정을 가속화하고 안정화하기 위해, 모델 기반 내비게이션 접근 방식을 활용하여 다양하고 유용한 데이터셋을 생성하는 데이터 부트스트래핑 기법을 통합합니다. 우리는 Agility Robotics Digit 휴머노이드를 사용하여 무작위 장애물이 있는 여러 시나리오에서 시뮬레이션을 통해 방법을 검증합니다. 결과는 우리의 프레임워크가 원래의 모델 기반 방법 및 다른 학습 기반 방법과 비교하여 내비게이션 성공률과 적응성을 크게 향상시킴을 보여줍니다.

## 参考
- http://arxiv.org/abs/2506.02206v1
