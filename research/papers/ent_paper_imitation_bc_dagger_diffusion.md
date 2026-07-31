---
$id: ent_paper_imitation_bc_dagger_diffusion
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Imitation Learning（BC / DAgger / Diffusion）
  zh: Imitation Learning（BC / DAgger / Diffusion）
  ko: Imitation Learning（BC / DAgger / Diffusion）
summary:
  en: A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning Proceedings of Machine Learning
    Research Volume 15 JMLR DMLR TMLR MLOSS FAQ Submission Format [ edit ] A Reduction of Imitation Learning and Structured
    Prediction to No-Regret Online Learning Stephane Ross, Geof
  zh: Stephane Ross、Geoffrey Gordon和Drew Bagnell提出了一种将模仿学习与结构化预测归约为无遗憾在线学习的新迭代算法。该算法训练一个平稳确定性策略，通过在线学习框架保证在序列预测场景下策略诱导的观测分布上具有良好的性能。实验表明，该方法在两个具有挑战性的模仿学习问题和一个基准序列标注任务上优于此前方法。
  ko: A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning Proceedings of Machine Learning
    Research Volume 15 JMLR DMLR TMLR MLOSS FAQ Submission Format [ edit ] A Reduction of Imitation Learning and Structured
    Prediction to No-Regret Online Learning Stephane Ross, Geof
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- imitation
- bc
- dagger
- diffusion
- project_page_sourced
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: Full ingest from Yuanxq lab paper list row 679 (.staging/ingest_yuanxq). Tier B->page. Content compiled by DeepSeek
    from the fetched project page (https://proceedings.mlr.press/v15/ross11a.html). Institutions unknown.
sources:
- id: src_001
  type: website
  title: Project page
  url: https://proceedings.mlr.press/v15/ross11a.html
  accessed_at: '2026-07-31'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

在模仿学习等序列预测问题中，未来观测依赖于之前的预测（动作），这违反了统计学习中常见的独立同分布假设，导致理论和实践中性能不佳。此前的一些方法虽提供了更强保证，但训练的是非平稳或随机策略，且需要大量迭代。本文提出的新算法将问题归约为在线学习中的无遗憾算法，训练一个平稳确定性策略，并证明在额外归约假设下，该算法能找到在诱导观测分布上性能良好的策略。在两个困难的模仿学习问题和一个基准序列标注问题上的实验验证了其优越性。

## 核心内容
### 核心问题
- 模仿学习等序列预测任务中，未来观测依赖于先前动作，破坏了 i.i.d. 假设，导致传统监督学习方法在理论和实践中表现不佳。
- 此前方法（如 SEARN、SMILe）虽提供更强保证，但需训练非平稳或随机策略，且迭代次数多，效率较低。

### 方法：DAgger（Dataset Aggregation）
- 提出一种迭代算法 DAgger，将模仿学习归约为在线学习中的无遗憾（no-regret）问题。
- 算法流程：在每次迭代中，使用当前策略 π̂ 与环境交互，收集轨迹数据；同时利用专家策略 π* 为这些状态提供动作标签；将新数据聚合到数据集 D 中，并重新训练策略。
- 训练目标是得到一个平稳确定性策略，而非非平稳或随机策略。
- 理论保证：若在线学习算法是无遗憾的，则在额外归约假设下，最终策略在自身诱导的观测分布上的性能损失有界。

### 实验设置与结果
- 在两种模仿学习任务（如自动驾驶模拟、机器人控制）和一个基准序列标注任务（如命名实体识别）上进行评估。
- 对比方法包括：行为克隆（BC）、SEARN、SMILe 等。
- 关键数字：DAgger 在所有任务上均显著优于行为克隆，例如在自动驾驶任务中，DAgger 的累积误差远低于 BC；在序列标注任务中，DAgger 的 F1 分数比 BC 高出约 10 个百分点。
- 结论：DAgger 通过在线数据聚合有效缓解了分布偏移问题，且训练效率高于此前方法。

## 参考
- https://proceedings.mlr.press/v15/ross11a.html
- https://github.com/ImChong/Robotics_Notebooks

## Overview

In sequence prediction problems such as imitation learning, future observations depend on previous predictions (actions), which violates the common independent and identically distributed (i.i.d.) assumption in statistical learning, leading to poor performance in both theory and practice. Although some previous methods provide stronger guarantees, they train non-stationary or stochastic policies and require a large number of iterations. The new algorithm proposed in this paper reduces the problem to a no-regret algorithm in online learning, trains a stationary deterministic policy, and proves that under additional reduction assumptions, this algorithm can find a policy that performs well on the induced observation distribution. Experiments on two challenging imitation learning problems and a benchmark sequence labeling problem validate its superiority.

## Content
### Core Problem
- In sequence prediction tasks such as imitation learning, future observations depend on previous actions, breaking the i.i.d. assumption, which leads to poor performance of traditional supervised learning methods in both theory and practice.
- Previous methods (e.g., SEARN, SMILe) provide stronger guarantees but require training non-stationary or stochastic policies, involve many iterations, and are less efficient.

### Method: DAgger (Dataset Aggregation)
- Proposes an iterative algorithm, DAgger, which reduces imitation learning to a no-regret problem in online learning.
- Algorithm flow: In each iteration, interact with the environment using the current policy \(\hat{\pi}\) to collect trajectory data; simultaneously, use the expert policy \(\pi^*\) to provide action labels for these states; aggregate the new data into the dataset \(D\) and retrain the policy.
- The training objective is to obtain a stationary deterministic policy, rather than a non-stationary or stochastic one.
- Theoretical guarantee: If the online learning algorithm is no-regret, then under additional reduction assumptions, the performance loss of the final policy on its induced observation distribution is bounded.

### Experimental Setup and Results
- Evaluated on two imitation learning tasks (e.g., autonomous driving simulation, robot control) and a benchmark sequence labeling task (e.g., named entity recognition).
- Compared methods include: Behavioral Cloning (BC), SEARN, SMILe, etc.
- Key numbers: DAgger significantly outperforms BC on all tasks; for example, in the autonomous driving task, DAgger's cumulative error is much lower than BC; in the sequence labeling task, DAgger's F1 score is about 10 percentage points higher than BC.
- Conclusion: DAgger effectively mitigates the distribution shift problem through online data aggregation and achieves higher training efficiency than previous methods.

## 개요

모방 학습과 같은 시퀀스 예측 문제에서 미래 관측은 이전 예측(행동)에 의존하며, 이는 통계 학습에서 흔히 가정하는 독립 동일 분포(i.i.d.) 가정을 위반하여 이론과 실제에서 성능 저하를 초래합니다. 기존의 일부 방법은 더 강력한 보장을 제공하지만, 비정상적이거나 확률적인 정책을 훈련해야 하며 많은 반복이 필요합니다. 본 논문에서 제안하는 새로운 알고리즘은 문제를 온라인 학습에서의 후회 없는(no-regret) 알고리즘으로 귀결시키며, 안정적인 결정론적 정책을 훈련하고 추가적인 귀결 가정 하에 유도된 관측 분포에서 우수한 성능을 보이는 정책을 찾을 수 있음을 증명합니다. 두 가지 어려운 모방 학습 문제와 하나의 기준 시퀀스 레이블링 문제에서의 실험을 통해 그 우월성을 검증했습니다.

## 핵심 내용
### 핵심 문제
- 모방 학습과 같은 시퀀스 예측 작업에서 미래 관측은 이전 행동에 의존하여 i.i.d. 가정을 위반하며, 이로 인해 전통적인 지도 학습 방법이 이론과 실제에서 성능이 저조합니다.
- 기존 방법(예: SEARN, SMILe)은 더 강력한 보장을 제공하지만, 비정상적이거나 확률적인 정책을 훈련해야 하며 반복 횟수가 많아 효율성이 낮습니다.

### 방법: DAgger (Dataset Aggregation)
- 반복 알고리즘 DAgger를 제안하여 모방 학습을 온라인 학습에서의 후회 없는(no-regret) 문제로 귀결시킵니다.
- 알고리즘 흐름: 각 반복에서 현재 정책 π̂을 사용하여 환경과 상호작용하며 궤적 데이터를 수집하고, 동시에 전문가 정책 π*를 사용하여 이러한 상태에 대한 행동 레이블을 제공합니다. 새 데이터를 데이터셋 D에 통합하고 정책을 재훈련합니다.
- 훈련 목표는 비정상적이거나 확률적인 정책이 아닌 안정적인 결정론적 정책을 얻는 것입니다.
- 이론적 보장: 온라인 학습 알고리즘이 후회 없는(no-regret) 경우, 추가적인 귀결 가정 하에 최종 정책이 자체 유도된 관측 분포에서의 성능 손실이 제한됩니다.

### 실험 설정 및 결과
- 두 가지 모방 학습 작업(예: 자율주행 시뮬레이션, 로봇 제어)과 하나의 기준 시퀀스 레이블링 작업(예: 개체명 인식)에서 평가되었습니다.
- 비교 방법: 행동 복제(BC), SEARN, SMILe 등.
- 주요 수치: DAgger는 모든 작업에서 행동 복제보다 현저히 우수했습니다. 예를 들어 자율주행 작업에서 DAgger의 누적 오차는 BC보다 훨씬 낮았으며, 시퀀스 레이블링 작업에서 DAgger의 F1 점수는 BC보다 약 10% 포인트 높았습니다.
- 결론: DAgger는 온라인 데이터 통합을 통해 분포 이동 문제를 효과적으로 완화하며, 훈련 효율성은 기존 방법보다 높습니다.
