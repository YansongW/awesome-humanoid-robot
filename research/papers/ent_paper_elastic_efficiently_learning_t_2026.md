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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31132v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1097 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2606.31132v1

## 개요
생성형 제어 정책(예: 확산 정책 및 흐름 기반 비전-언어-행동 모델)은 로봇 제어에서 테스트 시 계산 확장을 지원하지만, 최적의 직렬 및 병렬 계산 할당은 상태, 작업, 정책에 따라 달라집니다. ELASTIC은 계산 할당 문제를 메타 마르코프 결정 과정(meta-MDP)으로 공식화하며, 여기서 메타 정책은 동결된 사전 훈련된 로봇 정책과 상호작용하여 각 노이즈 제거 반복에서 직렬 단계 수와 병렬 샘플 수를 선택하여 작업 성공률을 최대화하고 계산량을 최소화합니다. 강화 학습을 통해 이 메타 정책은 GCP의 훈련 데이터에 접근하지 않고도 적응형 계산 스케줄링을 학습할 수 있습니다. 시뮬레이션 조작 벤치마크에서 ELASTIC은 동일한 계산 예산 하에서 고정 및 단일 축 스케일링 기준선보다 파레토 우위를 보였습니다. 실제 로봇 조작에서 π0.5 비전-언어-행동 모델을 사용할 때, ELASTIC은 최상의 10개 샘플링 성공률을 일치시키면서 벽시계 지연 시간을 34% 줄였습니다.

## 핵심 내용
### 방법
ELASTIC의 핵심은 테스트 시 계산 할당을 메타 마르코프 결정 과정(meta-MDP)으로 모델링하는 것입니다. 이 프레임워크에서:
- **메타 정책**: 동결된 사전 훈련된 로봇 정책과 상호작용하는 학습 가능한 에이전트.
- **행동 공간**: 각 노이즈 제거 반복에서 메타 정책은 직렬 단계 수(sequential steps)와 병렬 샘플 수(parallel samples)를 선택합니다.
- **보상 함수**: 계산량(예: 노이즈 제거 단계 수 또는 샘플 수)을 최소화하면서 작업 성공률을 최대화합니다.
- **훈련 방식**: 강화 학습(예: PPO)을 사용하여 메타 정책을 훈련하며, GCP의 훈련 데이터나 기울기에 접근할 필요가 없습니다.

### 아키텍처
- **입력**: 현재 상태 정보(예: 로봇 관절 각도, 시각 관측) 및 노이즈 제거 반복의 진행 상황.
- **출력**: 각 노이즈 제거 반복의 직렬 단계 수와 병렬 샘플 수.
- **GCP와의 상호작용**: 메타 정책은 테스트 시 계산 할당을 동적으로 조정하며, GCP 자체는 동결 상태를 유지합니다.

### 실험 설정
- **시뮬레이션 벤치마크**: 여러 조작 작업(예: 잡기, 놓기)에서 확산 정책을 사용하여 테스트.
- **실제 로봇**: π0.5 비전-언어-행동 모델을 사용하여 실제 세계 조작 실험 수행.
- **기준선 비교**: 고정 계산 할당(예: 고정 단계 수 및 샘플 수), 단일 축 스케일링(직렬 단계 수만 증가 또는 병렬 샘플 수만 증가).

### 주요 수치
- **시뮬레이션 결과**: ELASTIC은 동일한 계산 예산 하에서 모든 기준선보다 파레토 우위를 보였으며, 즉 동일한 계산량에서 더 높은 성공률을 얻거나 동일한 성공률에서 더 적은 계산을 사용했습니다.
- **실제 로봇 결과**: ELASTIC은 최상의 10개 샘플링(즉, 10개의 후보 행동 중 최적 선택)의 성공률을 일치시키면서 벽시계 지연 시간을 34% 줄였습니다.

### 결론
ELASTIC은 강화 학습을 통해 적응형 테스트 시 계산 스케줄링을 학습하면 사전 훈련된 정책 자체를 수정하지 않고도 생성형 제어 정책의 효율성을 크게 향상시킬 수 있음을 입증했습니다. 이 방법은 시뮬레이션 및 실제 시나리오 모두에서 효과적이며, 특히 탐색과 정밀도의 동적 균형이 필요한 작업(예: 잡기)에 적합합니다.
