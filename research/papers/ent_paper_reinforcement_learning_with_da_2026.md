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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.02206v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (682 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2506.02206v1

## 개요
기존 이족 보행 로봇 내비게이션 프레임워크는 계산 효율성과 안정적인 보행의 정밀도 요구를 동시에 충족하기 어렵습니다. 본 연구는 계층적 아키텍처를 제안합니다: 상위 레벨 RL 플래너가 동적으로 하위 목표를 선택하고, 하위 레벨 MPC 플래너가 목표 도달을 위한 견고한 보행 패턴을 생성합니다. 훈련을 가속화하고 안정성을 향상시키기 위해 데이터 부트스트래핑 기술을 사용하여 모델 기반 내비게이션 방법에서 다양한 데이터 세트를 생성합니다. Agility Robotics Digit 휴머노이드 로봇 시뮬레이션에서 이 방법은 무작위 장애물 시나리오에서 원래 모델 기반 방법 및 기타 학습 방법에 비해 내비게이션 성공률과 적응성을 크게 향상시켰습니다.

## 핵심 내용
### 방법 아키텍처
- **상위 레벨 RL 플래너**: 로봇 좌표계에서 동적으로 하위 목표를 선택하고 강화 학습을 통해 의사 결정을 최적화하여 복잡한 환경에 적응합니다.
- **하위 레벨 MPC 플래너**: 모델 예측 제어를 기반으로 견고한 보행 패턴을 생성하여 로봇이 하위 목표에 안정적으로 도달하도록 보장합니다.
- **데이터 부트스트래핑 기술**: 모델 기반 내비게이션 방법을 활용하여 다양하고 정보가 풍부한 초기 데이터 세트를 생성하고, 이를 RL 플래너 사전 훈련에 사용하여 수렴을 가속화하고 훈련 안정성을 향상시킵니다.

### 실험 설정
- **플랫폼**: Agility Robotics Digit 휴머노이드 로봇 시뮬레이션 환경.
- **시나리오**: 무작위 장애물을 포함한 다양한 내비게이션 작업.
- **비교 방법**: 원래 모델 기반 방법 및 기타 학습 기반 내비게이션 방법.

### 주요 결과
- **내비게이션 성공률**: 원래 모델 기반 방법에 비해 크게 향상되었으며, 특히 밀집된 장애물 시나리오에서 두드러집니다.
- **적응성**: 무작위 장애물 분포에서 성공률 변동이 더 작고 더 견고한 성능을 보입니다.
- **훈련 효율성**: 데이터 부트스트래핑 기술 덕분에 RL 플래너의 수렴 속도가 빨라지고 최종 성능도 더 우수합니다.

### 결론
본 계층적 프레임워크는 동적 하위 목표 생성과 데이터 부트스트래핑 기술을 통해 이족 보행 휴머노이드 로봇 내비게이션에서 계산 효율성과 안정성 간의 균형 문제를 효과적으로 해결하며, 시뮬레이션에서 그 우수성을 검증했습니다.
