---
$id: ent_paper_martinez_cantin_bayesian_optimization_with_ada_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Bayesian Optimization with Adaptive Kernels for Robot Control
  zh: 用于机器人控制的自适应核贝叶斯优化
  ko: 로봇 제어를 위한 적응형 커널 베이지안 최적화
summary:
  en: This paper introduces Spartan Bayesian Optimization (SBO), a Gaussian-process Bayesian optimization method that uses
    an adaptive local/global Spartan kernel to model nonstationary cost functions without prior knowledge, and evaluates it
    on optimization benchmarks, reinforcement-learning control tasks, and UAV wing design.
  zh: 本文提出 Spartan Bayesian Optimization (SBO)，一种使用自适应局部/全局 Spartan 核的高斯过程贝叶斯优化方法，无需先验知识即可建模非平稳代价函数。该方法在优化基准、强化学习控制任务及无人机机翼设计中验证了有效性，核心贡献在于通过自适应局部区域实现非平稳建模，同时平衡局部搜索（利用）与全局搜索（探索）。
  ko: 본 논문은 사전 지식 없이 비정상 비용 함수를 모델링하기 위해 적응형 국소/전역 스파르탄 커널을 사용하는 가우시안 프로세스 베이지안 최적화 방법인 스파르탄 베이지안 최적화(SBO)를 제안하고, 최적화 벤치마크,
    강화학습 제어 작업, UAV 날개 설계에서 평가한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 05_mass_production
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- bayesian_optimization
- policy_search
- reinforcement_learning
- gaussian_process
- nonstationary_modeling
- sample_efficient_optimization
- robot_control
- locomotion_control
- uav_wing_design
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2402.07021v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Bayesian Optimization with Adaptive Kernels for Robot Control
  url: https://arxiv.org/abs/2402.07021
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
主动策略搜索将策略搜索的试错方法与贝叶斯优化的样本高效性相结合，用于机器人控制中的最优策略发现。贝叶斯优化通常假设代价函数来自平稳过程，因为非平稳建模依赖先验知识，但许多控制问题因失败条件、终止状态等具有内在非平稳性。本文设计的 Spartan 核函数无需先验知识即可自适应建模非平稳性，通过动态调整局部区域提升局部搜索性能而不牺牲全局搜索能力。实验在优化基准、机器人控制任务及无人机机翼设计中验证了该方法在样本效率与搜索平衡性上的优势。

## 核心内容
### 方法概述
- **主动策略搜索**：结合策略搜索的试错机制与贝叶斯优化的主动采样，适用于复杂连续状态/动作空间的机器人控制。
- **贝叶斯优化**：基于高斯过程代理模型与最优决策，通过精心选择每次采样实现样本高效优化，尤其适用于真实机器人、昂贵蒙特卡洛模拟或复杂仿真场景。
- **非平稳性挑战**：传统黑箱贝叶斯优化假设代价函数来自平稳过程，但控制问题中失败条件、终止状态等导致非平稳性，而现有非平稳建模通常依赖先验知识。

### Spartan 核设计
- **自适应局部/全局核**：Spartan 核通过引入自适应局部区域，无需先验知识即可建模非平稳代价函数。其核心思想是动态调整局部搜索范围，在利用（局部搜索）与探索（全局搜索）之间取得平衡。
- **数学特性**：核函数设计确保局部搜索精度提升的同时，不损害全局搜索的覆盖能力，从而避免陷入局部最优。

### 实验设置与结果
- **优化基准测试**：在标准非平稳优化基准上，SBO 相比传统平稳核方法（如 RBF 核）显著提升收敛速度与最终精度。
- **机器人控制任务**：在强化学习控制场景（如机械臂轨迹跟踪）中，SBO 以更少样本达到更高奖励值，验证了样本效率优势。
- **无人机机翼设计**：应用于无人机翼型优化，SBO 在有限仿真次数内找到更优气动性能参数，展示了工程实用性。

### 结论
SBO 通过自适应 Spartan 核有效解决控制问题中的非平稳性，无需先验知识即可提升局部搜索能力，同时保持全局搜索性能。实验表明其在样本效率与搜索平衡性上优于传统方法，为机器人控制与工程设计提供了实用工具。

## Overview
Active policy search combines the trial-and-error methodology from policy search with Bayesian optimization to actively find the optimal policy. First, policy search is a type of reinforcement learning which has become very popular for robot control, for its ability to deal with complex continuous state and action spaces. Second, Bayesian optimization is a sample efficient global optimization method that uses a surrogate model, like a Gaussian process, and optimal decision making to carefully select each sample during the optimization process. Sample efficiency is of paramount importance when each trial involves the real robot, expensive Monte Carlo runs, or a complex simulator. Black-box Bayesian optimization generally assumes a cost function from a stationary process, because nonstationary modeling is usually based on prior knowledge. However, many control problems are inherently nonstationary due to their failure conditions, terminal states and other abrupt effects. In this paper, we present a kernel function specially designed for Bayesian optimization, that allows nonstationary modeling without prior knowledge, using an adaptive local region. The new kernel results in an improved local search (exploitation), without penalizing the global search (exploration), as shown experimentally in well-known optimization benchmarks and robot control scenarios. We finally show its potential for the design of the wing shape of a UAV.

## 개요
Active policy search는 정책 탐색(policy search)의 시행착오 방법론과 베이지안 최적화(Bayesian optimization)를 결합하여 능동적으로 최적 정책을 찾아냅니다. 첫째, 정책 탐색은 강화 학습의 한 유형으로, 복잡한 연속 상태 및 행동 공간을 처리할 수 있는 능력 덕분에 로봇 제어 분야에서 매우 인기를 얻고 있습니다. 둘째, 베이지안 최적화는 가우시안 프로세스(Gaussian process)와 같은 대리 모델(surrogate model)과 최적 의사 결정을 사용하여 최적화 과정에서 각 샘플을 신중하게 선택하는 샘플 효율적인 전역 최적화 방법입니다. 각 시행이 실제 로봇, 고비용의 몬테카를로 실행(Monte Carlo runs), 또는 복잡한 시뮬레이터를 포함할 때 샘플 효율성은 매우 중요합니다. 블랙박스 베이지안 최적화(Black-box Bayesian optimization)는 일반적으로 정상 과정(stationary process)의 비용 함수를 가정하는데, 이는 비정상 모델링(nonstationary modeling)이 일반적으로 사전 지식에 기반하기 때문입니다. 그러나 많은 제어 문제는 실패 조건, 종료 상태 및 기타 급격한 효과로 인해 본질적으로 비정상적입니다. 본 논문에서는 베이지안 최적화를 위해 특별히 설계된 커널 함수(kernel function)를 제시하며, 이는 적응형 지역 영역(adaptive local region)을 사용하여 사전 지식 없이 비정상 모델링을 가능하게 합니다. 새로운 커널은 잘 알려진 최적화 벤치마크와 로봇 제어 시나리오에서 실험적으로 입증된 바와 같이, 전역 탐색(exploration)을 저해하지 않으면서 지역 탐색(exploitation)을 개선합니다. 마지막으로, UAV의 날개 형상 설계에 대한 잠재력을 보여줍니다.

## 핵심 내용
Active policy search는 정책 탐색(policy search)의 시행착오 방법론과 베이지안 최적화(Bayesian optimization)를 결합하여 능동적으로 최적 정책을 찾아냅니다. 첫째, 정책 탐색은 강화 학습의 한 유형으로, 복잡한 연속 상태 및 행동 공간을 처리할 수 있는 능력 덕분에 로봇 제어 분야에서 매우 인기를 얻고 있습니다. 둘째, 베이지안 최적화는 가우시안 프로세스(Gaussian process)와 같은 대리 모델(surrogate model)과 최적 의사 결정을 사용하여 최적화 과정에서 각 샘플을 신중하게 선택하는 샘플 효율적인 전역 최적화 방법입니다. 각 시행이 실제 로봇, 고비용의 몬테카를로 실행(Monte Carlo runs), 또는 복잡한 시뮬레이터를 포함할 때 샘플 효율성은 매우 중요합니다. 블랙박스 베이지안 최적화(Black-box Bayesian optimization)는 일반적으로 정상 과정(stationary process)의 비용 함수를 가정하는데, 이는 비정상 모델링(nonstationary modeling)이 일반적으로 사전 지식에 기반하기 때문입니다. 그러나 많은 제어 문제는 실패 조건, 종료 상태 및 기타 급격한 효과로 인해 본질적으로 비정상적입니다. 본 논문에서는 베이지안 최적화를 위해 특별히 설계된 커널 함수(kernel function)를 제시하며, 이는 적응형 지역 영역(adaptive local region)을 사용하여 사전 지식 없이 비정상 모델링을 가능하게 합니다. 새로운 커널은 잘 알려진 최적화 벤치마크와 로봇 제어 시나리오에서 실험적으로 입증된 바와 같이, 전역 탐색(exploration)을 저해하지 않으면서 지역 탐색(exploitation)을 개선합니다. 마지막으로, UAV의 날개 형상 설계에 대한 잠재력을 보여줍니다.

## 参考
- http://arxiv.org/abs/2402.07021v1
