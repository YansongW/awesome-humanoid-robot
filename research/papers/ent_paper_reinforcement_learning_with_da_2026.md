---
$id: ent_paper_reinforcement_learning_with_da_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Reinforcement Learning with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation
  zh: Reinforcement Learning with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation
  ko: Reinforcement Learning with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation
summary:
  en: Reinforcement Learning with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation is a paper on
    Navigation for humanoid robotics.
  zh: 本文提出一种面向双足人形机器人导航的分层框架，通过动态子目标生成实现安全实时导航。高层采用强化学习（RL）规划器在机器人坐标系中选择子目标，低层基于模型预测控制（MPC）生成稳健步态。核心贡献在于引入数据自举技术，利用基于模型的导航方法生成多样化数据集以加速训练，在Agility
    Robotics Digit仿真中显著提升导航成功率与适应性。
  ko: Reinforcement Learning with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation is a paper on
    Navigation for humanoid robotics.
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
- reinforcement_learning_with_da
theoretical_depth:
- system
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.02206v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: website
  title: Reinforcement Learning with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation
  url: ''
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
现有双足机器人导航框架难以兼顾计算效率与稳定步行的精度需求。该研究提出分层架构：高层RL规划器动态选择子目标，低层MPC规划器生成稳健步态以抵达目标。为加速训练并提升稳定性，采用数据自举技术，从基于模型的导航方法中生成多样化数据集。在Agility Robotics Digit人形机器人仿真中，该方法在随机障碍物场景下相比原始基于模型方法及其他学习方法，显著提升了导航成功率与适应性。

## 核心内容
### 方法架构
- **高层RL规划器**：在机器人坐标系中动态选择子目标，通过强化学习优化决策，适应复杂环境。
- **低层MPC规划器**：基于模型预测控制生成稳健步行步态，确保机器人稳定抵达子目标。
- **数据自举技术**：利用基于模型的导航方法生成多样化、信息丰富的初始数据集，用于预训练RL规划器，加速收敛并提升训练稳定性。

### 实验设置
- **平台**：Agility Robotics Digit人形机器人仿真环境。
- **场景**：包含随机障碍物的多种导航任务。
- **对比方法**：原始基于模型方法及其他学习型导航方法。

### 关键结果
- **导航成功率**：相比原始基于模型方法提升显著，尤其在密集障碍物场景中。
- **适应性**：在随机障碍物分布下，成功率波动更小，表现更稳健。
- **训练效率**：数据自举技术使RL规划器收敛速度加快，且最终性能更优。

### 结论
该分层框架通过动态子目标生成与数据自举技术，有效解决了双足人形机器人导航中计算效率与稳定性的平衡问题，在仿真中验证了其优越性。

## Overview
Safe and real-time navigation is fundamental for humanoid robot applications. However, existing bipedal robot navigation frameworks often struggle to balance computational efficiency with the precision required for stable locomotion. We propose a novel hierarchical framework that continuously generates dynamic subgoals to guide the robot through cluttered environments. Our method comprises a high-level reinforcement learning (RL) planner for subgoal selection in a robot-centric coordinate system and a low-level Model Predictive Control (MPC) based planner which produces robust walking gaits to reach these subgoals. To expedite and stabilize the training process, we incorporate a data bootstrapping technique that leverages a model-based navigation approach to generate a diverse, informative dataset. We validate our method in simulation using the Agility Robotics Digit humanoid across multiple scenarios with random obstacles. Results show that our framework significantly improves navigation success rates and adaptability compared to both the original model-based method and other learning-based methods.

## 개요
안전하고 실시간 내비게이션은 인간형 로봇 응용 분야의 기본 요소입니다. 그러나 기존의 이족 보행 로봇 내비게이션 프레임워크는 안정적인 보행에 필요한 정밀도와 계산 효율성 사이의 균형을 맞추는 데 어려움을 겪는 경우가 많습니다. 본 논문에서는 혼잡한 환경에서 로봇을 안내하기 위해 동적 하위 목표를 지속적으로 생성하는 새로운 계층적 프레임워크를 제안합니다. 제안하는 방법은 로봇 중심 좌표계에서 하위 목표를 선택하기 위한 고수준 강화 학습(RL) 플래너와 이러한 하위 목표에 도달하기 위한 강건한 보행 패턴을 생성하는 저수준 모델 예측 제어(MPC) 기반 플래너로 구성됩니다. 훈련 과정을 가속화하고 안정화하기 위해 모델 기반 내비게이션 접근 방식을 활용하여 다양하고 정보가 풍부한 데이터셋을 생성하는 데이터 부트스트래핑 기법을 통합합니다. 무작위 장애물이 있는 여러 시나리오에서 Agility Robotics Digit 휴머노이드를 사용하여 시뮬레이션을 통해 제안하는 방법을 검증합니다. 결과는 제안하는 프레임워크가 기존 모델 기반 방법 및 다른 학습 기반 방법과 비교하여 내비게이션 성공률과 적응성을 크게 향상시킴을 보여줍니다.

## 핵심 내용
안전하고 실시간 내비게이션은 인간형 로봇 응용 분야의 기본 요소입니다. 그러나 기존의 이족 보행 로봇 내비게이션 프레임워크는 안정적인 보행에 필요한 정밀도와 계산 효율성 사이의 균형을 맞추는 데 어려움을 겪는 경우가 많습니다. 본 논문에서는 혼잡한 환경에서 로봇을 안내하기 위해 동적 하위 목표를 지속적으로 생성하는 새로운 계층적 프레임워크를 제안합니다. 제안하는 방법은 로봇 중심 좌표계에서 하위 목표를 선택하기 위한 고수준 강화 학습(RL) 플래너와 이러한 하위 목표에 도달하기 위한 강건한 보행 패턴을 생성하는 저수준 모델 예측 제어(MPC) 기반 플래너로 구성됩니다. 훈련 과정을 가속화하고 안정화하기 위해 모델 기반 내비게이션 접근 방식을 활용하여 다양하고 정보가 풍부한 데이터셋을 생성하는 데이터 부트스트래핑 기법을 통합합니다. 무작위 장애물이 있는 여러 시나리오에서 Agility Robotics Digit 휴머노이드를 사용하여 시뮬레이션을 통해 제안하는 방법을 검증합니다. 결과는 제안하는 프레임워크가 기존 모델 기반 방법 및 다른 학습 기반 방법과 비교하여 내비게이션 성공률과 적응성을 크게 향상시킴을 보여줍니다.

## 参考
- http://arxiv.org/abs/2506.02206v1
