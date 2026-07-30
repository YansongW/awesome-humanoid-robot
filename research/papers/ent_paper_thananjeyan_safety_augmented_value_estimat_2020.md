---
$id: ent_paper_thananjeyan_safety_augmented_value_estimat_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Safety Augmented Value Estimation from Demonstrations (SAVED): Safe Deep Model-Based RL for Sparse Cost Robotic Tasks'
  zh: 基于演示的安全增强价值估计（SAVED）：面向稀疏代价机器人任务的安全深度模型强化学习
  ko: '시연으로부터의 안전 강화 가치 추정(SAVED): 희소 비용 로봇 작업을 위한 안전한 심층 모델 기반 강화학습'
summary:
  en: SAVED is a deep model-based reinforcement learning algorithm that uses sparse task-completion supervision and a modest
    set of suboptimal demonstrations, together with a learned value function, a kernel-density safe set, and probabilistic
    chance constraints over an ensemble dynamics model, to safely and efficiently learn robotic control tasks.
  zh: SAVED 是一种基于深度模型的强化学习算法，由研究团队提出，用于解决机器人控制任务中的稀疏奖励和动态不确定性挑战。其核心贡献在于结合稀疏任务完成监督、次优演示、核密度安全集和概率机会约束，在保证安全性的同时高效学习策略。
  ko: SAVED는 희소한 작업 완료 감독 신호와 소량의 비최적 시연, 학습된 가치 함수, 커널 밀도 안전 집합, 그리고 앙상블 동역학 모델 기반 확률적 기회 제약을 활용하여 로봇 제어 작업을 안전하고 효율적으로 학습하는
    알고리즘이다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- safe_reinforcement_learning
- model_based_rl
- deep_model_predictive_control
- sparse_rewards
- chance_constraints
- safe_set
- kernel_density_estimation
- demonstration_guided_learning
- sample_efficient_rl
- robotic_manipulation
- surgical_robotics
- da_vinci_research_kit
- pr2_robot
- fetch_robot
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1905.13402v8. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Safety Augmented Value Estimation from Demonstrations (SAVED): Safe Deep Model-Based RL for Sparse Cost Robotic
    Tasks'
  url: https://arxiv.org/abs/1905.13402
  date: '2020'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
SAVED 通过利用仅标识任务完成的稀疏监督和少量次优演示，约束探索并高效学习，同时处理复杂约束。该算法在 6 个标准仿真基准（包括导航和操作任务）以及 da Vinci 手术机器人上的物理打结任务中，与 3 种最先进的基于模型和无模型 RL 算法进行了对比。结果表明，SAVED 在成功率、约束满足和样本效率方面均优于先前方法，使其能够在真实机器人上安全地学习控制策略，且训练时间不到一小时。

## 核心内容
### 方法
SAVED 是一种基于深度模型的强化学习算法，其核心组件包括：
- **稀疏任务完成监督**：仅使用任务是否完成的二元信号作为奖励，避免手工设计密集成本函数。
- **次优演示**：利用少量非最优演示来引导探索，提高学习效率。
- **核密度安全集**：通过核密度估计构建安全状态集，限制探索范围，避免危险行为。
- **概率机会约束**：基于集成动力学模型的概率预测，确保策略满足安全约束。

### 实验设置
- **仿真基准**：在 6 个标准仿真任务上进行测试，涵盖导航和操作场景。
- **真实机器人任务**：在 da Vinci 手术机器人上执行物理打结任务。
- **对比算法**：与 3 种最先进的基于模型和无模型 RL 算法进行比较。

### 关键结果
- **成功率**：在机器人任务中，基线方法的成功率低于 5%，而 SAVED 在前 50 次训练迭代中成功率超过 75%。
- **约束满足**：SAVED 在所有任务中均能有效满足安全约束，避免危险行为。
- **样本效率**：SAVED 在不到一小时的训练时间内即可在真实机器人上学习到有效策略，显著优于基线方法。

### 结论
SAVED 通过结合稀疏监督、次优演示和安全约束，在机器人控制任务中实现了高效且安全的学习，尤其适用于稀疏奖励和动态不确定性场景。代码和补充材料可在 https://tinyurl.com/saved-rl 获取。

## Overview
Reinforcement learning (RL) for robotics is challenging due to the difficulty in hand-engineering a dense cost function, which can lead to unintended behavior, and dynamical uncertainty, which makes exploration and constraint satisfaction challenging. We address these issues with a new model-based reinforcement learning algorithm, Safety Augmented Value Estimation from Demonstrations (SAVED), which uses supervision that only identifies task completion and a modest set of suboptimal demonstrations to constrain exploration and learn efficiently while handling complex constraints. We then compare SAVED with 3 state-of-the-art model-based and model-free RL algorithms on 6 standard simulation benchmarks involving navigation and manipulation and a physical knot-tying task on the da Vinci surgical robot. Results suggest that SAVED outperforms prior methods in terms of success rate, constraint satisfaction, and sample efficiency, making it feasible to safely learn a control policy directly on a real robot in less than an hour. For tasks on the robot, baselines succeed less than 5% of the time while SAVED has a success rate of over 75% in the first 50 training iterations. Code and supplementary material is available at https://tinyurl.com/saved-rl.

## 개요
로봇 공학을 위한 강화 학습(Reinforcement Learning, RL)은 조밀한 비용 함수를 수동으로 설계하기 어렵다는 점(의도치 않은 행동을 초래할 수 있음)과 동적 불확실성(탐색과 제약 조건 충족을 어렵게 만듦)으로 인해 도전적인 과제입니다. 우리는 이러한 문제를 해결하기 위해 새로운 모델 기반 강화 학습 알고리즘인 SAVED(Safety Augmented Value Estimation from Demonstrations)를 제안합니다. 이 알고리즘은 작업 완료만 식별하는 감독 정보와 소량의 최적이 아닌 시연 데이터를 활용하여 탐색을 제한하고 복잡한 제약 조건을 처리하면서 효율적으로 학습합니다. 이후 SAVED를 3개의 최신 모델 기반 및 모델 프리 강화 학습 알고리즘과 비교하여, 탐색 및 조작을 포함한 6개의 표준 시뮬레이션 벤치마크와 da Vinci 수술 로봇의 실제 매듭 묶기 작업에서 성능을 평가했습니다. 결과는 SAVED가 성공률, 제약 조건 충족, 샘플 효율성 측면에서 기존 방법보다 우수함을 보여주며, 실제 로봇에서 1시간 이내에 안전하게 제어 정책을 학습할 수 있게 합니다. 로봇 작업의 경우, 기준 알고리즘은 5% 미만의 성공률을 보인 반면, SAVED는 처음 50회의 학습 반복에서 75% 이상의 성공률을 기록했습니다. 코드와 추가 자료는 https://tinyurl.com/saved-rl에서 확인할 수 있습니다.

## 핵심 내용
로봇 공학을 위한 강화 학습(RL)은 조밀한 비용 함수를 수동으로 설계하기 어렵다는 점(의도치 않은 행동을 초래할 수 있음)과 동적 불확실성(탐색과 제약 조건 충족을 어렵게 만듦)으로 인해 도전적인 과제입니다. 우리는 이러한 문제를 해결하기 위해 새로운 모델 기반 강화 학습 알고리즘인 SAVED(Safety Augmented Value Estimation from Demonstrations)를 제안합니다. 이 알고리즘은 작업 완료만 식별하는 감독 정보와 소량의 최적이 아닌 시연 데이터를 활용하여 탐색을 제한하고 복잡한 제약 조건을 처리하면서 효율적으로 학습합니다. 이후 SAVED를 3개의 최신 모델 기반 및 모델 프리 강화 학습 알고리즘과 비교하여, 탐색 및 조작을 포함한 6개의 표준 시뮬레이션 벤치마크와 da Vinci 수술 로봇의 실제 매듭 묶기 작업에서 성능을 평가했습니다. 결과는 SAVED가 성공률, 제약 조건 충족, 샘플 효율성 측면에서 기존 방법보다 우수함을 보여주며, 실제 로봇에서 1시간 이내에 안전하게 제어 정책을 학습할 수 있게 합니다. 로봇 작업의 경우, 기준 알고리즘은 5% 미만의 성공률을 보인 반면, SAVED는 처음 50회의 학습 반복에서 75% 이상의 성공률을 기록했습니다. 코드와 추가 자료는 https://tinyurl.com/saved-rl에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/1905.13402v8
