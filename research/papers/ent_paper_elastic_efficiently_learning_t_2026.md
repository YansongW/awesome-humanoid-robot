---
$id: ent_paper_elastic_efficiently_learning_t_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ELASTIC: Efficiently Learning to Adaptively Scale Test-Time Compute for Generative Control Policies'
  zh: 'ELASTIC: Efficiently Learning to Adaptively Scale Test-Time Compute for Generative Control Policies'
  ko: 'ELASTIC: Efficiently Learning to Adaptively Scale Test-Time Compute for Generative Control Policies'
summary:
  en: 'arXiv:2606.31132v1 Announce Type: new Abstract: Generative control policies (GCPs), such as diffusion policies and
    flow-based vision-language-action models, enable test-time scaling in robot control. Test-time compute can be allocated
    along two axes: sequential scaling, which increases denoising steps to refine actions, and parallel scaling, which samples
    multiple candidate actions to search across modes of the policy distribution. However, the optimal allocation of sequential
    and parallel compute is hard to know a priori as it is state-, task-, and policy-dependent. For example, early stages
    of a grasp may benefit from broader parallel exploration, while near-contact phases may require more sequential refinement
    for precision. We present ELASTIC, an algorithm that learns state-dependent test-time compute schedules for GCPs. We formulate
    compute allocation as a meta-Markov Decision Process in which a meta-policy interacts with a frozen pretrained robot policy
    and selects sequential steps and parallel samples at each denoising iteration to maximize task success while minimizing
    compute. Using reinforcement learning, this meta-policy also learns adaptive compute schedules without access to the GCP''s
    training data. Across simulated manipulation benchmarks with diffusion policies, ELASTIC Pareto-dominates fixed and single-axis
    scaling baselines at matched compute budgets. On real-world robot manipulation with the $\pi_{0.5}$ vision-language-action
    model, ELASTIC matches best-of-$10$ success while reducing wall-clock latency by 34%.'
  zh: ELASTIC 是一种为生成式控制策略（GCP）学习状态依赖型测试时计算调度算法的算法。它由研究团队提出，核心贡献在于将计算分配建模为元马尔可夫决策过程，通过强化学习训练元策略，在固定计算预算下自适应地分配去噪步数和并行采样数，从而在模拟和真实机器人操作任务中实现帕累托最优性能。
  ko: 'arXiv:2606.31132v1 Announce Type: new Abstract: Generative control policies (GCPs), such as diffusion policies and
    flow-based vision-language-action models, enable test-time scaling in robot control. Test-time compute can be allocated
    along two axes: sequential scaling, which increases denoising steps to refine actions, and parallel scaling, which samples
    multiple candidate actions to search across modes of the policy distribution. However, the optimal allocation of sequential
    and parallel compute is hard to know a priori as it is state-, task-, and policy-dependent. For example, early stages
    of a grasp may benefit from broader parallel exploration, while near-contact phases may require more sequential refinement
    for precision. We present ELASTIC, an algorithm that learns state-dependent test-time compute schedules for GCPs. We formulate
    compute allocation as a meta-Markov Decision Process in which a meta-policy interacts with a frozen pretrained robot policy
    and selects sequential steps and parallel samples at each denoising iteration to maximize task success while minimizing
    compute. Using reinforcement learning, this meta-policy also learns adaptive compute schedules without access to the GCP''s
    training data. Across simulated manipulation benchmarks with diffusion policies, ELASTIC Pareto-dominates fixed and single-axis
    scaling baselines at matched compute budgets. On real-world robot manipulation with the $\pi_{0.5}$ vision-language-action
    model, ELASTIC matches best-of-$10$ success while reducing wall-clock latency by 34%.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- elastic
- humanoid
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31132v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'ELASTIC: Efficiently Learning to Adaptively Scale Test-Time Compute for Generative Control Policies'
  url: https://arxiv.org/abs/2606.31132
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
生成式控制策略（如扩散策略和基于流的视觉-语言-动作模型）在机器人控制中支持测试时计算扩展，但最优的串行与并行计算分配因状态、任务和策略而异。ELASTIC 将计算分配问题形式化为元马尔可夫决策过程，其中元策略与冻结的预训练机器人策略交互，在每个去噪迭代中选择串行步数和并行样本数，以最大化任务成功率并最小化计算量。通过强化学习，该元策略无需访问 GCP 的训练数据即可学习自适应计算调度。在模拟操作基准测试中，ELASTIC 在相同计算预算下帕累托优于固定和单轴缩放基线；在真实机器人操作中，使用 π0.5 视觉-语言-动作模型时，ELASTIC 在匹配最佳-10 采样成功率的同时将墙钟延迟降低了 34%。

## 核心内容
### 方法
ELASTIC 的核心是将测试时计算分配建模为元马尔可夫决策过程（meta-MDP）。在该框架中：
- **元策略**：一个可学习的智能体，与冻结的预训练机器人策略交互。
- **动作空间**：在每个去噪迭代中，元策略选择串行步数（sequential steps）和并行样本数（parallel samples）。
- **奖励函数**：最大化任务成功率，同时最小化计算量（如去噪步数或采样数）。
- **训练方式**：使用强化学习（如 PPO）训练元策略，无需访问 GCP 的训练数据或梯度。

### 架构
- **输入**：当前状态信息（如机器人关节角度、视觉观测）和去噪迭代的进度。
- **输出**：每个去噪迭代的串行步数和并行样本数。
- **与 GCP 的交互**：元策略在测试时动态调整计算分配，GCP 本身保持冻结。

### 实验设置
- **模拟基准**：使用扩散策略在多个操作任务（如抓取、放置）上进行测试。
- **真实机器人**：使用 π0.5 视觉-语言-动作模型进行真实世界操作实验。
- **基线对比**：固定计算分配（如固定步数和样本数）、单轴缩放（仅增加串行步数或仅增加并行样本数）。

### 关键数字
- **模拟结果**：ELASTIC 在相同计算预算下帕累托优于所有基线，即在相同计算量下获得更高成功率，或在相同成功率下使用更少计算。
- **真实机器人结果**：ELASTIC 匹配最佳-10 采样（即从 10 个候选动作中选择最佳）的成功率，同时将墙钟延迟降低 34%。

### 结论
ELASTIC 证明了通过强化学习学习自适应测试时计算调度可以显著提升生成式控制策略的效率，无需修改预训练策略本身。该方法在模拟和真实场景中均有效，尤其适用于需要动态平衡探索与精度的任务（如抓取）。

## Overview
Generative control policies (GCPs), such as diffusion policies and flow-based vision-language-action models, enable test-time scaling in robot control. Test-time compute can be allocated along two axes: sequential scaling, which increases denoising steps to refine actions, and parallel scaling, which samples multiple candidate actions to search across modes of the policy distribution. However, the optimal allocation of sequential and parallel compute is hard to know a priori as it is state-, task-, and policy-dependent. For example, early stages of a grasp may benefit from broader parallel exploration, while near-contact phases may require more sequential refinement for precision. We present ELASTIC, an algorithm that learns state-dependent test-time compute schedules for GCPs. We formulate compute allocation as a meta-Markov Decision Process in which a meta-policy interacts with a frozen pretrained robot policy and selects sequential steps and parallel samples at each denoising iteration to maximize task success while minimizing compute. Using reinforcement learning, this meta-policy also learns adaptive compute schedules without access to the GCP's training data. Across simulated manipulation benchmarks with diffusion policies, ELASTIC Pareto-dominates fixed and single-axis scaling baselines at matched compute budgets. On real-world robot manipulation with the $π_{0.5}$ vision-language-action model, ELASTIC matches best-of-$10$ success while reducing wall-clock latency by 34%.

## 개요
생성적 제어 정책(GCP), 예를 들어 확산 정책(diffusion policies) 및 흐름 기반 비전-언어-행동 모델(flow-based vision-language-action models)은 로봇 제어에서 테스트 시간 확장(test-time scaling)을 가능하게 합니다. 테스트 시간 연산은 두 가지 축을 따라 할당될 수 있습니다: 순차적 확장(sequential scaling)은 노이즈 제거 단계를 증가시켜 행동을 정제하고, 병렬 확장(parallel scaling)은 여러 후보 행동을 샘플링하여 정책 분포의 모드 간을 탐색합니다. 그러나 순차적 및 병렬 연산의 최적 할당은 상태, 작업 및 정책에 따라 달라지므로 사전에 알기 어렵습니다. 예를 들어, 잡기(grasp)의 초기 단계는 더 넓은 병렬 탐색의 이점을 얻을 수 있는 반면, 접촉 근접 단계에서는 정밀도를 위해 더 많은 순차적 정제가 필요할 수 있습니다. 우리는 GCP를 위한 상태 의존적 테스트 시간 연산 스케줄을 학습하는 알고리즘인 ELASTIC을 제시합니다. 우리는 연산 할당을 메타-마르코프 결정 과정(meta-Markov Decision Process)으로 공식화하며, 여기서 메타 정책은 고정된 사전 훈련된 로봇 정책과 상호작용하고 각 노이즈 제거 반복에서 순차적 단계와 병렬 샘플을 선택하여 연산을 최소화하면서 작업 성공을 극대화합니다. 강화 학습을 사용하여, 이 메타 정책은 GCP의 훈련 데이터에 접근하지 않고도 적응형 연산 스케줄을 학습합니다. 확산 정책을 사용한 시뮬레이션 조작 벤치마크에서 ELASTIC은 동일한 연산 예산에서 고정 및 단일 축 확장 기준선을 파레토 지배(Pareto-dominates)합니다. $π_{0.5}$ 비전-언어-행동 모델을 사용한 실제 로봇 조작에서 ELASTIC은 최고-10(best-of-$10$) 성공률과 일치하면서 벽시계 지연 시간(wall-clock latency)을 34% 줄입니다.

## 핵심 내용
생성적 제어 정책(GCP), 예를 들어 확산 정책(diffusion policies) 및 흐름 기반 비전-언어-행동 모델(flow-based vision-language-action models)은 로봇 제어에서 테스트 시간 확장(test-time scaling)을 가능하게 합니다. 테스트 시간 연산은 두 가지 축을 따라 할당될 수 있습니다: 순차적 확장(sequential scaling)은 노이즈 제거 단계를 증가시켜 행동을 정제하고, 병렬 확장(parallel scaling)은 여러 후보 행동을 샘플링하여 정책 분포의 모드 간을 탐색합니다. 그러나 순차적 및 병렬 연산의 최적 할당은 상태, 작업 및 정책에 따라 달라지므로 사전에 알기 어렵습니다. 예를 들어, 잡기(grasp)의 초기 단계는 더 넓은 병렬 탐색의 이점을 얻을 수 있는 반면, 접촉 근접 단계에서는 정밀도를 위해 더 많은 순차적 정제가 필요할 수 있습니다. 우리는 GCP를 위한 상태 의존적 테스트 시간 연산 스케줄을 학습하는 알고리즘인 ELASTIC을 제시합니다. 우리는 연산 할당을 메타-마르코프 결정 과정(meta-Markov Decision Process)으로 공식화하며, 여기서 메타 정책은 고정된 사전 훈련된 로봇 정책과 상호작용하고 각 노이즈 제거 반복에서 순차적 단계와 병렬 샘플을 선택하여 연산을 최소화하면서 작업 성공을 극대화합니다. 강화 학습을 사용하여, 이 메타 정책은 GCP의 훈련 데이터에 접근하지 않고도 적응형 연산 스케줄을 학습합니다. 확산 정책을 사용한 시뮬레이션 조작 벤치마크에서 ELASTIC은 동일한 연산 예산에서 고정 및 단일 축 확장 기준선을 파레토 지배(Pareto-dominates)합니다. $π_{0.5}$ 비전-언어-행동 모델을 사용한 실제 로봇 조작에서 ELASTIC은 최고-10(best-of-$10$) 성공률과 일치하면서 벽시계 지연 시간(wall-clock latency)을 34% 줄입니다.

## 参考
- http://arxiv.org/abs/2606.31132v1
