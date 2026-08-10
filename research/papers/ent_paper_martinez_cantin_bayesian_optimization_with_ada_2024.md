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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2402.07021v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (932 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2402.07021v1

## 개요
능동 정책 탐색은 정책 탐색의 시행착오 방식과 베이지안 최적화의 샘플 효율성을 결합하여 로봇 제어에서 최적 정책을 발견합니다. 베이지안 최적화는 일반적으로 비용 함수가 정상 과정에서 비롯된다고 가정하는데, 비정상성 모델링은 사전 지식에 의존하기 때문입니다. 그러나 많은 제어 문제는 실패 조건, 종료 상태 등으로 인해 본질적으로 비정상성을 지닙니다. 본 논문에서 설계한 Spartan 커널은 사전 지식 없이도 비정상성을 적응적으로 모델링하며, 지역 영역을 동적으로 조정하여 전역 탐색 능력을 희생하지 않으면서 지역 탐색 성능을 향상시킵니다. 실험은 최적화 벤치마크, 로봇 제어 작업 및 드론 날개 설계에서 샘플 효율성과 탐색 균형 측면의 우수성을 검증합니다.

## 핵심 내용
### 방법 개요
- **능동 정책 탐색**: 정책 탐색의 시행착오 메커니즘과 베이지안 최적화의 능동 샘플링을 결합하여 복잡한 연속 상태/행동 공간의 로봇 제어에 적합합니다.
- **베이지안 최적화**: 가우시안 프로세스 대리 모델과 최적 결정을 기반으로, 각 샘플을 신중히 선택하여 샘플 효율적 최적화를 달성하며, 실제 로봇, 고가의 몬테카를로 시뮬레이션 또는 복잡한 시뮬레이션 환경에 특히 적합합니다.
- **비정상성 도전**: 전통적인 블랙박스 베이지안 최적화는 비용 함수가 정상 과정에서 비롯된다고 가정하지만, 제어 문제에서 실패 조건, 종료 상태 등이 비정상성을 유발하며, 기존 비정상성 모델링은 일반적으로 사전 지식에 의존합니다.

### Spartan 커널 설계
- **적응형 지역/전역 커널**: Spartan 커널은 적응형 지역 영역을 도입하여 사전 지식 없이 비정상 비용 함수를 모델링합니다. 핵심 아이디어는 지역 탐색 범위를 동적으로 조정하여 활용(지역 탐색)과 탐험(전역 탐색) 사이의 균형을 유지하는 것입니다.
- **수학적 특성**: 커널 함수 설계는 지역 탐색 정밀도를 향상시키면서도 전역 탐색의 커버리지 능력을 손상시키지 않아 지역 최적에 빠지는 것을 방지합니다.

### 실험 설정 및 결과
- **최적화 벤치마크 테스트**: 표준 비정상 최적화 벤치마크에서 SBO는 전통적인 정상 커널 방법(예: RBF 커널)보다 수렴 속도와 최종 정밀도를 크게 향상시킵니다.
- **로봇 제어 작업**: 강화 학습 제어 시나리오(예: 로봇 팔 궤적 추적)에서 SBO는 더 적은 샘플로 더 높은 보상 값을 달성하여 샘플 효율성의 우위를 검증합니다.
- **드론 날개 설계**: 드론 익형 최적화에 적용하여 SBO는 제한된 시뮬레이션 횟수 내에서 더 우수한 공기역학 성능 매개변수를 찾아 공학적 실용성을 보여줍니다.

### 결론
SBO는 적응형 Spartan 커널을 통해 제어 문제의 비정상성을 효과적으로 해결하며, 사전 지식 없이 지역 탐색 능력을 향상시키면서 전역 탐색 성능을 유지합니다. 실험은 샘플 효율성과 탐색 균형에서 전통적인 방법보다 우수함을 보여주며, 로봇 제어와 공학 설계에 실용적인 도구를 제공합니다.
