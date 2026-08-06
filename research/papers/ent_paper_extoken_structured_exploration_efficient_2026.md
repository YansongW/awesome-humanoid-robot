---
$id: ent_paper_extoken_structured_exploration_efficient_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ExToken: Structured Exploration for Efficient Vision-Language-Action Reinforcement Fine-tuning'
  zh: 'ExToken: Structured Exploration for Efficient Vision-Language-Action Reinforcement Fine-tuning'
  ko: 'ExToken: Structured Exploration for Efficient Vision-Language-Action Reinforcement Fine-tuning'
summary:
  en: Reinforcement Learning (RL) has demonstrated significant potential for improving Vision-Language-Action (VLA) models
    on complex manipulation tasks. However, its practical scalability remains severely limited by the substantial cost of
    environmental interactions. In this work, we first investigate the exploration stagnation bottleneck in current VLA-RL
    frameworks and reveal that trajectory.
  zh: ExToken 是一种面向视觉-语言-动作（VLA）模型强化学习（RL）后训练的结构化探索框架，由研究团队提出，旨在解决 RL 微调中因动作模式坍缩导致的探索停滞与样本效率低下问题。其核心贡献在于通过离散探索 token 显式引导策略探索多样化行为模式，在不增加交互预算的前提下显著提升轨迹多样性，从而在
    LIBERO 仿真基准和真实世界操作任务中取得优于现有基线的成功率。
  ko: Reinforcement Learning (RL) has demonstrated significant potential for improving Vision-Language-Action (VLA) models
    on complex manipulation tasks. However, its practical scalability remains severely limited by the substantial cost of
    environmental interactions. In this work, we first investigate the exploration stagnation bottleneck in current VLA-RL
    frameworks and reveal that trajectory.
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
- extoken
- structured
- exploration
- efficient
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-continuation (2026-08-05), source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh
    six-section interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2607.12931 ExToken: Structured Exploration for Efficient Vision-Language-Action Reinforceme'
  url: https://arxiv.org/abs/2607.12931
  date: '2026-07-14'
  accessed_at: '2026-08-05'
---

## 概述

ExToken 是一种面向视觉-语言-动作（VLA）模型强化学习（RL）后训练的结构化探索框架，由研究团队提出，旨在解决 RL 微调中因动作模式坍缩导致的探索停滞与样本效率低下问题。其核心贡献在于通过离散探索 token 显式引导策略探索多样化行为模式，在不增加交互预算的前提下显著提升轨迹多样性，从而在 LIBERO 仿真基准和真实世界操作任务中取得优于现有基线的成功率。

## 它改变了什么

现有 VLA-RL 工作多聚焦于奖励塑形、价值函数设计或离线-在线范式转换，却普遍回避了一个更底层的问题：策略在 RL 优化中如何主动、高效地探索状态-动作空间。作者通过实证揭示，标准随机采样在优化推进中会导致轨迹相似度持续上升，即动作模式坍缩，使任务性能过早停滞于次优水平。这一观察将问题从“如何更优地利用已有数据”转向“如何生成更有信息量的新数据”，改变了样本效率讨论的焦点。

其真正改变的是对“探索”这一 RL 核心环节的建模方式：不再依赖隐式的随机性（如噪声或熵正则），而是将探索显式地结构化为离散的行为模式选择。这相当于在策略输入空间引入一个可学习的“探索意图”变量，使得 RL 优化既能保持多样性，又能逐步偏向状态相关的有效行为，从而在固定交互预算下获得更高的数据利用率和更快的收敛速度。

## 方法拆解

ExToken 框架由四个关键组件构成，其核心思想是将探索问题分解为“选择何种行为模式”与“如何执行该模式”两个层次。

### Token 构建：从演示数据中提取行为模式
- 使用预训练视频嵌入模型 E（如 RZEN-Embed）提取离线演示轨迹的潜在时空特征。
- 在潜在空间执行 K-means 聚类，得到 K 个质心 {c₁, c₂, …, c_K}，每个质心 c_k 定义一个离散探索 token k。
- 每条演示轨迹被分配到其最近质心对应的簇，同一簇内轨迹共享同一 token，代表一种不同的行为模式。

### Token 条件化 Warm-Up
- 将 token 嵌入直接追加到策略输入序列末尾（在 token 嵌入层内）。
- 每条演示轨迹与其分配簇的中心 token 配对，进行监督微调（SFT）warm-up。
- 目的：让策略学习 token 与对应行为模式之间的关联，为 RL 阶段的结构化探索建立先验。

### RL 期间的结构化探索
- 每条 rollout 均匀采样一个探索 token：token_k ~ U(1, K)，并将其前置到策略输入。
- 相比传统随机探索，token 显式引导策略朝向不同行为模式，显著提升 rollout 多样性和状态-动作覆盖。
- 该设计仅通过输入条件化引入，不改变策略网络结构，因此可无缝集成到不同 VLA 架构。

### 状态条件 Token 选择器（State-Conditioned Token Selector）
- 给定初始观测 s₀（图像观测 o₀ + 语言指令 l），选择器 φ 预测 token 空间上的类别分布：
  - P_φ(token_k | s₀; τ) = exp(z_k/τ) / Σⱼ exp(z_j/τ)，其中 z = MLP(SigLIP(s₀)) ∈ R^K，τ 为采样温度。
- 在聚类后的离线数据集上用分配的簇标签作为监督进行 warm-up。
- RL 期间从温度缩放分布中采样 token，保持探索多样性同时逐步偏向状态相关的行为模式。
- 推理时确定性输出 arg max 的 token。

### REINFORCE 双层优化
- Token 选择器 φ 与 VLA 策略 π_θ 联合优化。
- VLA 策略使用标准 RL 目标（如 GRPO）更新。
- Token 选择器在 episode 级别作为单步决策过程使用 REINFORCE 优化：
  - ∇_φ J(φ) = Σₖ P_φ(token_k | s₀) · (R(τ) − b) · ∇_φ log P_φ(token_k | s₀)
  - R(τ) 为轨迹奖励，b 为方差缩减基线（按任务分别计算）。
- 设计理由：选择器随策略学习演化，逐步学习为不同初始状态预测有效行为模式。

## 关键创新

1. **探索的结构化离散化**：将连续的动作探索空间映射为 K 个离散行为模式 token，这是对传统连续探索（如噪声扰动）或隐式探索（如熵正则）的根本性替代。其新颖性在于将“探索什么”从策略优化中解耦出来，形成一个可学习的、状态条件的选择问题，使得探索更具目的性和可解释性。

2. **双层优化架构**：将 token 选择器 φ 与策略 π_θ 联合优化，但采用不同的更新机制——策略用 RL 目标，选择器用 REINFORCE。这种设计允许选择器在策略学习过程中动态调整其对不同行为模式的偏好，实现探索-利用的自动平衡，而无需手工设计探索调度策略。

3. **框架无关性与低侵入性**：token 仅通过输入条件化引入，不改变策略网络结构或 RL 算法本身，因此可无缝集成到不同 VLA 架构（如 OpenVLA、π₀.₅）和不同 RL 框架（如 GRPO、Evo-RL）。这种设计降低了采用门槛，使现有 VLA-RL 系统可以低成本升级为结构化探索版本。

## 实验与结果

实验覆盖 LIBERO 仿真基准和真实世界操作任务，核心对照为同预算下的 RLinf-GRPO 基线。

### LIBERO 仿真结果（Table 1，交互预算 512 rollouts/步，100 步）

| 模型 | Spatial | Object | Goal | Long | Average |
|------|---------|--------|------|------|---------|
| RLinf-GRPO † | 98.6 | 98.4 | 95.1 | 95.2 | 96.8 |
| ExToken (Ours) † | 99.0 | 99.4 | 96.5 | 97.8 | 98.2 |

- ExToken 总体平均成功率 98.2%，优于同设置基线 RLinf-GRPO（96.8%），提升 1.4 个百分点（由表内数值 96.8→98.2 计算）。
- LIBERO-Long 套件上从 95.2% 提升至 97.8%，提升 2.6 个百分点（由表内数值 95.2→97.8 计算），表明结构化探索对长视界任务尤其有效。
- ExToken 优于强 SFT 基线 π₀.₅（96.9%）和 OpenVLA-OFT（97.1%），说明 RL 后训练在结构化探索下能超越纯 SFT 上限。

### 真实世界结果（Table 2，每任务 20 条 rollout 评估）

| 方法 | Fold clothes 原始 | Wipe table 原始 | Pour water 原始 | Insert pen 原始 |
|------|------|---------|-----------|-----------|
| π₀.₅ | 75 | 70 | 65 | 65 |
| Evo-RL | 90 | 90 | 80 | 85 |
| ExToken | 95 | 95 | 90 | 90 |

- ExToken 在所有任务的“原始”设置中优于 Evo-RL 基线，平均提升 6.25%（由表内数值计算）。
- 在泛化设置（-Object、-BG、-Lighting）中，ExToken 的性能下降通常限制在 5%–10%，而基线在相同扰动下经历更大退化（如 Fold clothes -Lighting 下 ExToken 下降 15%，Evo-RL 下降 25%）。

### 极端交互约束实验（图 6）
- 将每优化步 rollout 预算从 512 降至 128。
- RLinf-GRPO 在 256 条 rollout 时降至 90.3% 成功率，在 128 条 rollout 时训练动态不稳定。
- ExToken 仅用 256 条 rollout（93.4%）直接匹敌 RLinf 使用双倍数据预算（512 条 rollout）的表现（96.8%），差距 3.4 个百分点（由表内数值 93.4→96.8 计算）。
- ExToken 在 128 条 rollout 的极端限制下也变得不太稳定。

### Token 粒度敏感性（图 7）
- 评估 K ∈ {3, 6, 10}。
- K = 3 与 K = 6 的结果高度可比，K = 10 时出现轻微性能下降。

## 边界与局限

- 当前 token 利用方式相对基础，未联合优化 token 表征与策略，也未引入概率性 token dropout 以无条件捕获轨迹多样性。
- token 来源于预训练编码器对视频表征的聚类，采用更结构化的方法（如状态条件潜在模型）可能产生更好地捕获任务动态的探索 token。
- ExToken 仅使用从初始状态预测的单一 token 条件化策略，对短视界任务有效，但扩展到细粒度、时间条件化 token 可使智能体为复杂长视界操作任务动态切换探索策略。
- 在 128 条 rollout 的极端限制下 ExToken 变得不稳定，归因于从极少数初始状态采样多样化 token 导致的梯度方差增大；在此类受限预算下自适应减少簇数量是未来方向。
- 真实世界实验仅涉及 4 个任务，且每任务仅 20 条 rollout 评估，统计显著性有限。

## 工程启示

- **复现优先核对**：仿真实验的关键超参数为 K = 6、warm-up 数据量（LIBERO-Long 每簇 6 条，其余套件每簇 2 条）、REINFORCE 学习率 1e-6、采样温度 2.0、token 选择器每 5 步更新一次。这些参数对性能影响敏感，建议严格遵循。
- **最易踩坑点**：token 选择器的 REINFORCE 优化对基线 b 的计算方式敏感（按任务分别计算），若全局共享基线可能导致梯度方差增大；此外，聚类应在每个任务内独立进行，跨任务聚类会引入任务间差异偏差。
- **工程选型建议**：ExToken 的框架无关性使其可作为现有 VLA-RL 系统的即插即用模块。对于交互预算紧张（如每步少于 256 条 rollout）的场景，建议先验证 K 值敏感性（K = 3 或 6 更稳健），并考虑自适应减少簇数量以缓解梯度方差问题。
- **下游团队注意**：真实世界实验中，视频编码时转换为灰度以减轻颜色和光照变化干扰，这一预处理对泛化性能有显著影响，建议在部署时保留。

## Overview
Reinforcement Learning (RL) has demonstrated significant potential for improving Vision-Language-Action (VLA) models on complex manipulation tasks. However, its practical scalability remains severely limited by the substantial cost of environmental interactions. In this work, we first investigate the exploration stagnation bottleneck in current VLA-RL frameworks and reveal that trajectory diversity is fundamentally more important to sample efficiency than the sheer quantity of collected rollouts. Motivated by these insights, we introduce RL Exploration Token (ExToken), a simple yet general framework that condition VLA policies on discrete behavioral priors derived from offline demonstrations for structured exploration. By conditioning the policy on different tokens during rollout collection, ExToken encourages the agent to explore diverse behavioral modes, substantially improving state-action coverage and exploration efficiency. To bridge exploration during training with deterministic inference at deployment, ExToken further incorporates a state-conditioned token selector that adaptively predicts effective behavioral modes for unseen scenarios. Extensive experiments across simulated and real-world robotic manipulation tasks demonstrate that ExToken consistently accelerates convergence, improves task performance, and exhibits strong robustness under highly constrained interaction budgets.

## 参考
- https://arxiv.org/abs/2607.12931

## 개요

ExToken은 시각-언어-행동(VLA) 모델 강화학습(RL) 후속 학습을 위한 구조화된 탐색 프레임워크로, 연구팀이 제안했으며, RL 미세조정에서 행동 패턴 붕괴로 인한 탐색 정체와 샘플 효율성 저하 문제를 해결하는 것을 목표로 한다. 핵심 기여는 이산 탐색 토큰을 통해 정책이 다양한 행동 패턴을 명시적으로 탐색하도록 유도하여, 상호작용 예산을 늘리지 않고도 궤적 다양성을 크게 향상시키고, 이를 통해 LIBERO 시뮬레이션 벤치마크와 실제 로봇 조작 작업에서 기존 기준선보다 우수한 성공률을 달성하는 데 있다.

## 무엇을 바꾸었는가

기존 VLA-RL 연구는 주로 보상 형성, 가치 함수 설계 또는 오프라인-온라인 패러다임 전환에 초점을 맞췄지만, 정책이 RL 최적화 중에 상태-행동 공간을 어떻게 능동적이고 효율적으로 탐색할 것인지라는 더 근본적인 문제는 대체로 회피해 왔다. 저자들은 실증 분석을 통해 표준 무작위 샘플링이 최적화가 진행됨에 따라 궤적 유사도가 지속적으로 증가한다는 것, 즉 행동 패턴 붕괴가 발생하여 작업 성능이 조기에 차선 수준에서 정체된다는 것을 밝혀냈다. 이 관찰은 문제의 초점을 "기존 데이터를 더 잘 활용하는 방법"에서 "더 정보량이 많은 새 데이터를 생성하는 방법"으로 전환하여 샘플 효율성 논의의 초점을 바꾸었다.

실제로 바꾼 것은 RL의 핵심 요소인 "탐색"을 모델링하는 방식이다. 더 이상 암묵적 무작위성(예: 노이즈 또는 엔트로피 정규화)에 의존하지 않고, 탐색을 명시적으로 이산적인 행동 패턴 선택으로 구조화한다. 이는 정책 입력 공간에 학습 가능한 "탐색 의도" 변수를 도입하는 것과 같아서, RL 최적화가 다양성을 유지하면서도 상태와 관련된 유효한 행동으로 점진적으로 편향될 수 있게 하여, 고정된 상호작용 예산 내에서 더 높은 데이터 활용률과 더 빠른 수렴 속도를 얻을 수 있다.

## 방법 분해

ExToken 프레임워크는 네 가지 핵심 구성 요소로 이루어져 있으며, 핵심 아이디어는 탐색 문제를 "어떤 행동 패턴을 선택할 것인가"와 "해당 패턴을 어떻게 실행할 것인가"라는 두 계층으로 분해하는 것이다.

### 토큰 구축: 시연 데이터에서 행동 패턴 추출
- 사전 훈련된 비디오 임베딩 모델 E(예: RZEN-Embed)를 사용하여 오프라인 시연 궤적의 잠재 시공간 특징을 추출한다.
- 잠재 공간에서 K-means 클러스터링을 수행하여 K개의 중심점 {c₁, c₂, …, c_K}을 얻고, 각 중심점 c_k는 이산 탐색 토큰 k를 정의한다.
- 각 시연 궤적은 가장 가까운 중심점에 해당하는 클러스터에 할당되며, 동일한 클러스터 내 궤적은 동일한 토큰을 공유하여 서로 다른 행동 패턴을 나타낸다.

### 토큰 조건화 워밍업
- 토큰 임베딩을 정책 입력 시퀀스 끝에 직접 추가한다(토큰 임베딩 레이어 내).
- 각 시연 궤적은 할당된 클러스터의 중심 토큰과 짝을 이루어 지도 미세조정(SFT) 워밍업을 수행한다.
- 목적: 정책이 토큰과 해당 행동 패턴 간의 연관성을 학습하도록 하여, RL 단계의 구조화된 탐색을 위한 사전 지식을 확립한다.

### RL 중 구조화된 탐색
- 각 롤아웃에서 탐색 토큰을 균일하게 샘플링한다: token_k ~ U(1, K), 이를 정책 입력 앞에 추가한다.
- 기존의 무작위 탐색과 달리, 토큰은 정책이 서로 다른 행동 패턴을 향하도록 명시적으로 유도하여 롤아웃 다양성과 상태-행동 커버리지를 크게 향상시킨다.
- 이 설계는 입력 조건화를 통해서만 도입되며 정책 네트워크 구조를 변경하지 않으므로, 다양한 VLA 아키텍처에 매끄럽게 통합될 수 있다.

### 상태 조건 토큰 선택기
- 초기 관측 s₀(이미지 관측 o₀ + 언어 명령 l)가 주어지면, 선택기 φ는 토큰 공간에 대한 클래스 분포를 예측한다:
  - P_φ(token_k | s₀; τ) = exp(z_k/τ) / Σⱼ exp(z_j/τ), 여기서 z = MLP(SigLIP(s₀)) ∈ R^K, τ는 샘플링 온도이다.
- 클러스터링된 오프라인 데이터셋에서 할당된 클러스터 레이블을 지도 신호로 사용하여 워밍업한다.
- RL 중에는 온도 조정 분포에서 토큰을 샘플링하여 탐색 다양성을 유지하면서 상태와 관련된 행동 패턴으로 점진적으로 편향된다.
- 추론 시에는 arg max 토큰을 결정적으로 출력한다.

### REINFORCE 이중 레벨 최적화
- 토큰 선택기 φ와 VLA 정책 π_θ를 공동 최적화한다.
- VLA 정책은 표준 RL 목표(예: GRPO)로 업데이트된다.
- 토큰 선택기는 에피소드 레벨에서 단일 단계 결정 과정으로 REINFORCE를 사용하여 최적화된다:
  - ∇_φ J(φ) = Σₖ P_φ(token_k | s₀) · (R(τ) − b) · ∇_φ log P_φ(token_k | s₀)
  - R(τ)는 궤적 보상, b는 분산 감소 기준선(작업별로 각각 계산)이다.
- 설계 근거: 선택기는 정책 학습과 함께 진화하여, 다양한 초기 상태에 대해 유효한 행동 패턴을 점진적으로 예측하는 법을 학습한다.

## 핵심 혁신

1. **탐색의 구조화된 이산화**: 연속적인 행동 탐색 공간을 K개의 이산 행동 패턴 토큰으로 매핑하는 것은 기존의 연속 탐색(예: 노이즈 섭동) 또는 암묵적 탐색(예: 엔트로피 정규화)에 대한 근본적인 대안이다. 그 참신함은 "무엇을 탐색할 것인가"를 정책 최적화에서 분리하여 학습 가능한 상태 조건 선택 문제로 만듦으로써, 탐색을 더 목적 지향적이고 해석 가능하게 만든다는 점에 있다.

2. **이중 레벨 최적화 아키텍처**: 토큰 선택기 φ와 정책 π_θ를 공동 최적화하지만 서로 다른 업데이트 메커니즘을 사용한다 — 정책은 RL 목표, 선택기는 REINFORCE. 이 설계는 선택기가 정책 학습 과정에서 서로 다른 행동 패턴에 대한 선호도를 동적으로 조정할 수 있게 하여, 수동으로 탐색 스케줄링 전략을 설계할 필요 없이 탐색-활용의 자동 균형을 달성한다.

3. **프레임워크 독립성과 낮은 침습성**: 토큰은 입력 조건화를 통해서만 도입되며 정책 네트워크 구조나 RL 알고리즘 자체를 변경하지 않으므로, 다양한 VLA 아키텍처(예: OpenVLA, π₀.₅)와 다양한 RL 프레임워크(예: GRPO, Evo-RL)에 매끄럽게 통합될 수 있다. 이 설계는 도입 장벽을 낮추어 기존 VLA-RL 시스템을 저비용으로 구조화된 탐색 버전으로 업그레이드할 수 있게 한다.

## 실험 및 결과

실험은 LIBERO 시뮬레이션 벤치마크와 실제 로봇 조작 작업을 포괄하며, 핵심 대조군은 동일 예산 하의 RLinf-GRPO 기준선이다.

### LIBERO 시뮬레이션 결과 (Table 1, 상호작용 예산 512 롤아웃/스텝, 100 스텝)

| 모델 | Spatial | Object | Goal | Long | Average |
|------|---------|--------|------|------|---------|
| RLinf-GRPO † | 98.6 | 98.4 | 95.1 | 95.2 | 96.8 |
| ExToken (Ours) † | 99.0 | 99.4 | 96.5 | 97.8 | 98.2 |

- ExToken의 전체 평균 성공률은 98.2%로, 동일 설정의 기준선 RLinf-GRPO(96.8%)보다 1.4% 포인트 높다(표 내 수치 96.8→98.2로 계산).
- LIBERO-Long 스위트에서 95.2%에서 97.8%로 2.6% 포인트 향상(표 내 수치 95.2→97.8로 계산), 구조화된 탐색이 긴 시야각 작업에 특히 효과적임을 시사한다.
- ExToken은 강력한 SFT 기준선 π₀.₅(96.9%)와 OpenVLA-OFT(97.1%)보다 우수하여, 구조화된 탐색 하의 RL 후속 학습이 순수 SFT 상한을 초과할 수 있음을 보여준다.

### 실제 로봇 결과 (Table 2, 작업당 20개 롤아웃 평가)

| 방법 | Fold clothes 원본 | Wipe table 원본 | Pour water 원본 | Insert pen 원본 |
|------|------|---------|-----------|-----------|
| π₀.₅ | 75 | 70 | 65 | 65 |
| Evo-RL | 90 | 90 | 80 | 85 |
| ExToken | 95 | 95 | 90 | 90 |

- ExToken은 모든 작업의 "원본" 설정에서 Evo-RL 기준선보다 우수하며, 평균 6.25% 향상(표 내 수치로 계산).
- 일반화 설정(-Object, -BG, -Lighting)에서 ExToken의 성능 저하는 일반적으로 5%–10%로 제한되는 반면, 기준선은 동일한 섭동에서 더 큰 성능 저하를 겪는다(예: Fold clothes -Lighting에서 ExToken은 15% 하락, Evo-RL은 25% 하락).

### 극단적 상호작용 제약 실험 (그림 6)
- 각 최적화 스텝의 롤아웃 예산을 512에서 128로 줄임.
- RLinf-GRPO는 256개 롤아웃에서 90.3% 성공률로 하락하고, 128개 롤아웃에서는 훈련 동역학이 불안정해짐.
- ExToken은 256개 롤아웃(93.4%)만으로 RLinf가 두 배 데이터 예산(512개 롤아웃)으로 달성한 성능(96.8%)에 직접 맞먹으며, 차이는 3.4% 포인트(표 내 수치 93.4→96.8로 계산).
- ExToken도 128개 롤아웃의 극단적 제약에서는 다소 불안정해짐.

### 토큰 세분성 민감도 (그림 7)
- K ∈ {3, 6, 10} 평가.
- K = 3과 K = 6의 결과는 매우 유사하며, K = 10에서 약간의 성능 저하가 발생.

## 경계 및 한계

- 현재 토큰 활용 방식은 상대적으로 기본적이며, 토큰 표현과 정책을 공동 최적화하지 않고, 조건 없는 궤적 다양성을 포착하기 위한 확률적 토큰 드롭아웃도 도입하지 않았다.
- 토큰은 사전 훈련된 인코더의 비디오 표현 클러스터링에서 비롯되며, 상태 조건 잠재 모델과 같은 더 구조화된 방법을 사용하면 작업 동역학을 더 잘 포착하는 탐색 토큰을 생성할 수 있을 것이다.
- ExToken은 초기 상태에서 예측된 단일 토큰으로만 정책을 조건화하므로 짧은 시야각 작업에는 효과적이지만, 세분화된 시간 조건 토큰으로 확장하면 에이전트가 복잡한 긴 시야각 조작 작업에서 탐색 전략을 동적으로 전환할 수 있을 것이다.
- 128개 롤아웃의 극단적 제약에서 ExToken은 불안정해지며, 이는 극소수의 초기 상태에서 다양한 토큰을 샘플링하여 발생하는 그래디언트 분산 증가에 기인한다. 이러한 제한된 예산에서 클러스터 수를 적응적으로 줄이는 것이 향후 방향이다.
- 실제 로봇 실험은 4개 작업만 포함하며, 작업당 20개 롤아웃 평가로 통계적 유의성이 제한적이다.

## 엔지니어링 시사점

- **재현 우선 확인 사항**: 시뮬레이션 실험의 핵심 하이퍼파라미터는 K = 6, 워밍업 데이터 양(LIBERO-Long은 클러스터당 6개, 나머지 스위트는 클러스터당 2개), REINFORCE 학습률 1e-6, 샘플링 온도 2.0, 토큰 선택기 5스텝마다 업데이트이다. 이러한 파라미터는 성능에 민감하므로 엄격히 따르는 것이 좋다.
- **가장 실수하기 쉬운 지점**: 토큰 선택기의 REINFORCE 최적화는 기준선 b의 계산 방식에 민감하며(작업별로 각각 계산), 전역 공유 기준선을 사용하면 그래디언트 분산이 증가할 수 있다. 또한 클러스터링은 각 작업 내에서 독립적으로 수행해야 하며, 작업 간 클러스터링은 작업 간 차이 편향을 도입할 수 있다.
- **엔지니어링 선택 제안**: ExToken의 프레임워크 독립성은 기존 VLA-RL 시스템의 플러그 앤 플레이 모듈로 사용될 수 있게 한다. 상호작용 예산이 부족한(예: 스텝당 256개 미만 롤아웃) 시나리오에서는 먼저 K 값 민감도(K = 3 또는 6이 더 견고함)를 검증하고, 그래디언트 분산 문제를 완화하기 위해 클러스터 수를 적응적으로 줄이는 것을 고려하라.
- **하류 팀 주의 사항**: 실제 로봇 실험에서 비디오 인코딩 시 색상 및 조명 변화 간섭을 줄이기 위해 그레이스케일로 변환했으며, 이 전처리는 일반화 성능에 상당한 영향을 미치므로 배포 시 유지하는 것이 좋다.
