---
$id: ent_paper_vine_taming_generative_control_policies_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VINE: Taming Generative Control Policies for Reinforcement Learning'
  zh: 'VINE: Taming Generative Control Policies for Reinforcement Learning'
  ko: 'VINE: Taming Generative Control Policies for Reinforcement Learning'
summary:
  en: Flow-matching policies have emerged as an effective policy parameterization for robot learning. They iteratively generate
    actions from noise, enabling highly expressive modeling of complex and multimodal action distributions. However, prior
    works observed that scaling these policies with value-gradient reinforcement learning (RL) often leads to training instability.
    Existing methods attribute.
  zh: VINE（Value-gradient Iterative Noise Exploration）是一种面向强化学习（RL）微调的采样方法，由论文作者提出，用于解决生成控制策略（如流匹配模型）在值梯度优化下的训练不稳定性。其核心贡献在于，通过在每个去噪步骤注入噪声并重建插值状态，在不改变生成目标或添加辅助模型的前提下，实现了对预训练流匹配策略的稳定端到端值梯度优化。
  ko: Flow-matching policies have emerged as an effective policy parameterization for robot learning. They iteratively generate
    actions from noise, enabling highly expressive modeling of complex and multimodal action distributions. However, prior
    works observed that scaling these policies with value-gradient reinforcement learning (RL) often leads to training instability.
    Existing methods attribute.
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
- vine
- taming
- generative
- control
- policies
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch4-catchup (2026-08-05), source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2607.10369 VINE: Taming Generative Control Policies for Reinforcement Learning'
  url: https://arxiv.org/abs/2607.10369
  date: '2026-07-11'
  accessed_at: '2026-08-05'
---

## 概述

VINE（Value-gradient Iterative Noise Exploration）是一种面向强化学习（RL）微调的采样方法，由论文作者提出，用于解决生成控制策略（如流匹配模型）在值梯度优化下的训练不稳定性。其核心贡献在于，通过在每个去噪步骤注入噪声并重建插值状态，在不改变生成目标或添加辅助模型的前提下，实现了对预训练流匹配策略的稳定端到端值梯度优化。

## 它改变了什么

此前，社区普遍将生成策略在RL微调中的不稳定性归咎于迭代生成过程本身，因此采取了一系列规避手段：冻结策略参数、将多步生成蒸馏为一步策略、或仅将标量值函数作为权重而非梯度信号。这些方法虽然稳定了训练，却牺牲了生成模型的表达力与迭代精化的能力。VINE的提出者给出了一个相反的诊断：不稳定的根源并非迭代生成本身，而是为行为克隆（BC）设计的原始采样策略——即仅在初始化时采样一次噪声、随后沿确定性轨迹去噪的Euler采样器——在值梯度信号下变得脆弱。这一重新归因改变了问题的求解方向：不再需要修改生成目标或网络架构，只需替换采样器，即可让预训练策略在RL微调中保持稳定。这意味着一类此前被认为难以直接微调的模型（如流匹配策略）现在可以无缝接入标准的actor-critic框架，无需任何蒸馏或冻结操作。

## 方法拆解

VINE的采样过程可拆解为两个关键设计：**每步随机插值**（per-step stochastic interpolation）与**迭代端点预测**（iterative endpoint-prediction）。

### 算法流程（K步去噪）
1. **初始化**：从标准正态分布采样初始动作估计 `â_0 ~ N(0, I_d)`。
2. **循环**（k = 0 到 K-1）：
   - **重建插值状态**：`x̂_k = t_k * â_k + (1 - t_k) * z_k`，其中 `z_k ~ N(0, I_d)`，`t_k` 为单调递增时间表（实验中固定为 `{0.0, 0.1, …, 0.9}`）。
   - **端点预测**：`â_{k+1} = x̂_k + (1 - t_k) * v_θ(x̂_k, t_k; s)`，其中 `v_θ` 为预训练的流匹配速度场，`s` 为观测状态。
3. **返回**：`â_K` 作为最终动作。

### 关键设计决策
- **语义兼容性**：每个网络查询的输入 `x̂_k` 始终是噪声插值状态（即 `t_k` 时刻的带噪样本），这与原始流匹配训练时的输入分布一致。因此，VINE无需新的生成目标或辅助引导模型，仅修改采样器实现即可应用于任何预训练流匹配策略。
- **噪声注入的调度**：噪声权重 `(1 - t_k)` 随 `t_k` 增加而单调递减。这实现了从粗粒度随机探索（早期步骤）到细粒度确定性细化（后期步骤）的平滑过渡，类似于模拟退火中的温度调度。
- **理论保证**：定理1（FM-VINE一致性）表明，对于条件流匹配损失的点态最小化器 `v*`，端点预测 `â_k = x̂_k + (1-t_k)v*(x̂_k, t_k; s)` 是给定噪声中间状态 `x̂_k` 的贝叶斯最优动作估计。推论1进一步证明，在确定性VINE（`z_k=0`）下，动作估计以收缩因子 `λ_k = t_k²σ_a² / (t_k²σ_a² + (1-t_k)²)` 指数级收敛到条件均值 `μ_s`。

### 训练目标
- **Actor损失**：`-Q_φ(s, â_K) + α * ||â_K - a||²`，其中 `α` 为BC系数（各任务取值见实验部分），`a` 为行为克隆参考动作。
- **Critic损失**：`(Q_φ(s, a) - r - γQ_φ̄(s', a'))²`，采用裁剪双Q学习（clipped double Q-learning），训练两个Q函数，actor目标取均值，critic目标取最小值。

## 关键创新

1. **重新归因训练不稳定性**：这是首个明确指出不稳定性源于采样器而非迭代生成过程的系统性工作。通过将问题从"如何规避迭代生成"转变为"如何设计RL友好的采样器"，VINE开辟了一条无需修改生成目标或网络架构的微调路径。这一诊断的普适性意味着，任何基于流匹配或扩散的预训练策略都可以直接受益。

2. **采样器即探索机制**：VINE将噪声注入重新定义为一种结构化的局部探索策略。与传统的动作空间噪声（如高斯扰动）不同，VINE的噪声是在去噪轨迹的中间状态上注入的，这保证了探索方向与生成模型的流形结构一致。随 `t_k` 增加，探索粒度从粗到细自动调整，无需人工设计探索噪声的方差调度。

3. **零成本兼容性**：VINE仅修改采样器实现，不改变生成目标、不添加辅助模型、不引入新的训练损失。这意味着预训练策略可以直接加载，无需任何适配层或重新训练。对于工业界已有的流匹配策略资产，这是一个即插即用的升级路径。

## 实验与结果

实验在OGBench离线RL基准（8个域，40个任务）和真实世界机器人操作任务上评估。

### 离线RL结果（成功率%，均值 [95%置信区间]）
| 任务 | VINE | 最佳基线 | 基线名称 |
|------|------|----------|----------|
| antmaze-large | 99 [98, 100] | 94 [94, 95] | ReBRAC |
| antmaze-giant | 76 [68, 83] | 57 [53, 60] | ReBRAC |
| humanoidmaze-large | 46 [36, 56] | 24 [21, 27] | 基线未明确 |
| scene-sparse | 65 [61, 69] | 50 [43, 57] | 基线未明确 |
| puzzle-3x3-sparse | 100 [100, 100] | 96 [93, 98] | 基线未明确 |
| cube-double | 74 [72, 76] | 64 [62, 66] | 基线未明确 |
| cube-triple | 8 [7, 9] | 5 [3, 6] | 基线未明确 |

注：VINE在40个任务中的整体表现优于所有基线（论文未明确给出聚合分数）。在antmaze-giant等困难任务上，VINE显著超越基线（76 vs 57），而FQL、FAWAC等基线得分接近0。

### 消融实验
- **去噪步数K**：K=10时表现最佳；K=1或4时，智能体大多停留在起始区域，无法到达目标（图5）。
- **梯度稳定性**：VINE在5个OGBench任务上成功率更高，且反向传播梯度更小更稳定（图4）。

### 真实世界实验
插座插入任务，20次试验评估。VINE与SAC-Flow、Hil-SERL等在线基线对比（论文未明确给出具体成功率数字，表2为图片未提取）。

## 边界与局限

论文未明确列出局限性，但可从方法设计中推断出以下边界：
- **适用性范围**：VINE针对流匹配策略设计，虽声称可应用于扩散策略，但未提供扩散模型的系统验证。对于非迭代生成策略（如一步生成模型），VINE的噪声注入机制不适用。
- **在线RL场景**：算法1提及可选在线RL收集，但论文未提供在线RL的详细实验数据，仅给出真实世界任务的有限结果。
- **大规模基础模型**：作者在"未来方向"中提及扩展VINE到大型基础模型，但当前实验仅覆盖中小规模策略网络（MLP隐藏层[512, 512, 512, 512]），未验证在数十亿参数模型上的表现。
- **理论保证的假设**：定理1和推论1依赖条件流匹配损失的点态最小化器假设，实际训练中网络可能未完全收敛到该最优解，理论保证的严格性在实践中有待验证。

## 工程启示

对复现和下游团队的工程指导：
- **先核对采样器实现**：VINE的核心改动仅在采样器层面，复现时优先确认 `x̂_k = t_k * â_k + (1 - t_k) * z_k` 的插值公式与时间表 `t_k ∈ {0.0, 0.1, …, 0.9}` 是否与原文一致。最容易踩坑的是时间表的单调性——若 `t_k` 不严格递增，噪声注入的退火调度将失效。
- **BC系数α的敏感性**：α在各任务间差异极大（antmaze-large为10，scene-sparse为300，puzzle-3x3-sparse为1000）。复现时需按任务调整α，不可使用统一值。建议从论文表4的数值出发，以10倍为步长进行网格搜索。
- **Q函数数量**：训练两个Q函数是稳定性的关键（actor取均值，critic取最小值）。若下游实现仅使用单Q函数，VINE的稳定性收益可能显著下降。
- **梯度步数与评估频率**：离线训练1M梯度步，每20k步用50个episode评估。复现时需确保足够的训练步数——VINE的稳定收益在训练后期（>500k步）才充分显现，过早停止可能低估其性能。
- **预训练策略的兼容性**：VINE直接加载预训练流匹配策略，无需微调生成目标。但需确认预训练策略的噪声调度与VINE的插值公式兼容——若预训练时使用了不同的噪声调度（如cosine schedule），可能需要重新对齐时间表。

## Overview
Flow-matching policies have emerged as an effective policy parameterization for robot learning. They iteratively generate actions from noise, enabling highly expressive modeling of complex and multimodal action distributions. However, prior works observed that scaling these policies with value-gradient reinforcement learning (RL) often leads to training instability. Existing methods attribute this instability to iterative generation and therefore avoid end-to-end value-gradient optimization by sacrificing iterative generation, high expressiveness, or value-gradient optimization. Contrary to prior belief, we show the instability does not stem from iterative generation itself, but from the vanilla sampling strategy originally designed for behavior cloning, which becomes brittle under value-gradient RL. Motivated by this insight, we propose VINE, an RL-oriented sampling method that enables stable end-to-end value-gradient optimization for flow-matching policies. Instead of following a single flow trajectory, VINE reconstructs a new interpolation state at every denoising step, creating a stable differentiable path for value-gradient propagation while remaining compatible with the original flow-matching denoising process. As a result, VINE preserves the expressiveness and iterative generation of flow-matching without sacrificing end-to-end value-gradient optimization. Despite performing end-to-end backpropagation through all ten denoising steps, VINE achieves stable policy improvement and consistently outperforms state-of-the-art RL methods on the OGBench offline RL benchmark and real-world robotic manipulation task. Videos are available on our website: https://agibottech.github.io/vine.

## 参考
- https://arxiv.org/abs/2607.10369

## 개요

VINE(Value-gradient Iterative Noise Exploration)는 강화 학습(RL) 미세 조정을 위한 샘플링 방법으로, 논문 저자가 생성 제어 정책(예: 흐름 매칭 모델)의 값 그래디언트 최적화에서의 훈련 불안정성을 해결하기 위해 제안했습니다. 핵심 기여는 각 디노이징 단계에서 노이즈를 주입하고 보간 상태를 재구성함으로써, 생성 목표를 변경하거나 보조 모델을 추가하지 않고 사전 훈련된 흐름 매칭 정책의 안정적인 종단 간 값 그래디언트 최적화를 달성하는 것입니다.

## 무엇을 바꾸었는가

이전에는 커뮤니티에서 생성 정책의 RL 미세 조정 불안정성을 반복적 생성 과정 자체의 탓으로 돌려, 일련의 회피 수단을 사용했습니다: 정책 파라미터 동결, 다단계 생성을 단일 단계 정책으로 증류, 또는 스칼라 값 함수를 그래디언트 신호가 아닌 가중치로만 사용하는 방법 등이었습니다. 이러한 방법들은 훈련을 안정화했지만 생성 모델의 표현력과 반복 정제 능력을 희생했습니다. VINE의 제안자는 반대의 진단을 내렸습니다: 불안정성의 근원은 반복 생성 자체가 아니라, 행동 복제(BC)를 위해 설계된 원래 샘플링 전략——즉 초기화 시에만 노이즈를 한 번 샘플링하고 이후 결정적 궤적을 따라 디노이징하는 Euler 샘플러——이 값 그래디언트 신호 하에서 취약해진다는 것입니다. 이러한 재귀인은 문제 해결 방향을 바꾸었습니다: 더 이상 생성 목표나 네트워크 아키텍처를 수정할 필요 없이 샘플러만 교체하면 사전 훈련된 정책이 RL 미세 조정에서 안정적으로 유지될 수 있습니다. 이는 이전에 직접 미세 조정이 어렵다고 여겨졌던 모델 클래스(예: 흐름 매칭 정책)가 이제 증류나 동결 없이 표준 actor-critic 프레임워크에 원활하게 통합될 수 있음을 의미합니다.

## 방법 분석

VINE의 샘플링 과정은 두 가지 핵심 설계로 분해할 수 있습니다: **단계별 확률적 보간**(per-step stochastic interpolation)과 **반복적 엔드포인트 예측**(iterative endpoint-prediction).

### 알고리즘 흐름(K단계 디노이징)
1. **초기화**: 표준 정규 분포에서 초기 행동 추정 `â_0 ~ N(0, I_d)`를 샘플링합니다.
2. **반복**(k = 0 ~ K-1):
   - **보간 상태 재구성**: `x̂_k = t_k * â_k + (1 - t_k) * z_k`, 여기서 `z_k ~ N(0, I_d)`, `t_k`는 단조 증가 시간표(실험에서는 `{0.0, 0.1, …, 0.9}`로 고정).
   - **엔드포인트 예측**: `â_{k+1} = x̂_k + (1 - t_k) * v_θ(x̂_k, t_k; s)`, 여기서 `v_θ`는 사전 훈련된 흐름 매칭 속도장, `s`는 관측 상태.
3. **반환**: `â_K`를 최종 행동으로 반환.

### 핵심 설계 결정
- **의미론적 호환성**: 각 네트워크 쿼리의 입력 `x̂_k`는 항상 노이즈 보간 상태(즉, `t_k` 시점의 노이즈가 섞인 샘플)이며, 이는 원래 흐름 매칭 훈련 시의 입력 분포와 일치합니다. 따라서 VINE은 새로운 생성 목표나 보조 안내 모델 없이 샘플러 구현만 수정하여 모든 사전 훈련된 흐름 매칭 정책에 적용할 수 있습니다.
- **노이즈 주입 스케줄링**: 노이즈 가중치 `(1 - t_k)`는 `t_k`가 증가함에 따라 단조 감소합니다. 이는 초기 단계의 거친 확률적 탐색에서 후기 단계의 세밀한 결정적 정제로의 부드러운 전환을 구현하며, 이는 시뮬레이션 어닐링의 온도 스케줄링과 유사합니다.
- **이론적 보장**: 정리 1(FM-VINE 일관성)은 조건부 흐름 매칭 손실의 점별 최소화기 `v*`에 대해, 엔드포인트 예측 `â_k = x̂_k + (1-t_k)v*(x̂_k, t_k; s)`이 주어진 노이즈 중간 상태 `x̂_k`에 대한 베이즈 최적 행동 추정임을 보여줍니다. 추론 1은 결정적 VINE(`z_k=0`)에서 행동 추정이 수축 인자 `λ_k = t_k²σ_a² / (t_k²σ_a² + (1-t_k)²)`로 조건부 평균 `μ_s`에 지수적으로 수렴함을 추가로 증명합니다.

### 훈련 목표
- **Actor 손실**: `-Q_φ(s, â_K) + α * ||â_K - a||²`, 여기서 `α`는 BC 계수(각 작업의 값은 실험 부분 참조), `a`는 행동 클로닝 참조 행동.
- **Critic 손실**: `(Q_φ(s, a) - r - γQ_φ̄(s', a'))²`, 클리핑된 이중 Q 학습(clipped double Q-learning)을 사용하여 두 개의 Q 함수를 훈련하고, actor 목표는 평균을, critic 목표는 최솟값을 취합니다.

## 핵심 혁신

1. **훈련 불안정성의 재귀인**: 이는 불안정성의 근원이 반복 생성 과정이 아닌 샘플러에 있음을 명시적으로 지적한 최초의 체계적 연구입니다. 문제를 "반복 생성을 회피하는 방법"에서 "RL 친화적인 샘플러를 설계하는 방법"으로 전환함으로써, VINE은 생성 목표나 네트워크 아키텍처 수정 없이 미세 조정 경로를 개척했습니다. 이 진단의 보편성은 흐름 매칭 또는 확산 기반의 모든 사전 훈련된 정책이 직접 혜택을 받을 수 있음을 의미합니다.

2. **샘플러로서의 탐색 메커니즘**: VINE은 노이즈 주입을 구조화된 국소 탐색 전략으로 재정의합니다. 전통적인 행동 공간 노이즈(예: 가우시안 섭동)와 달리, VINE의 노이즈는 디노이징 궤적의 중간 상태에 주입되어 탐색 방향이 생성 모델의 다양체 구조와 일치하도록 보장합니다. `t_k`가 증가함에 따라 탐색 입자는 거친 것에서 미세한 것으로 자동 조정되며, 탐색 노이즈의 분산 스케줄링을 수동으로 설계할 필요가 없습니다.

3. **제로 비용 호환성**: VINE은 샘플러 구현만 수정하며, 생성 목표를 변경하지 않고, 보조 모델을 추가하지 않으며, 새로운 훈련 손실을 도입하지 않습니다. 이는 사전 훈련된 정책을 직접 로드할 수 있고, 적응 레이어나 재훈련이 필요 없음을 의미합니다. 산업계에 이미 존재하는 흐름 매칭 정책 자산에 대해 이는 플러그 앤 플레이 업그레이드 경로입니다.

## 실험 및 결과

실험은 OGBench 오프라인 RL 벤치마크(8개 도메인, 40개 작업)와 실제 로봇 조작 작업에서 평가되었습니다.

### 오프라인 RL 결과(성공률%, 평균 [95% 신뢰 구간])
| 작업 | VINE | 최고 기준선 | 기준선 이름 |
|------|------|----------|----------|
| antmaze-large | 99 [98, 100] | 94 [94, 95] | ReBRAC |
| antmaze-giant | 76 [68, 83] | 57 [53, 60] | ReBRAC |
| humanoidmaze-large | 46 [36, 56] | 24 [21, 27] | 기준선 미명시 |
| scene-sparse | 65 [61, 69] | 50 [43, 57] | 기준선 미명시 |
| puzzle-3x3-sparse | 100 [100, 100] | 96 [93, 98] | 기준선 미명시 |
| cube-double | 74 [72, 76] | 64 [62, 66] | 기준선 미명시 |
| cube-triple | 8 [7, 9] | 5 [3, 6] | 기준선 미명시 |

참고: VINE는 40개 작업 전체에서 모든 기준선보다 우수한 성능을 보였습니다(논문에서 통합 점수는 명시되지 않음). antmaze-giant와 같은 어려운 작업에서 VINE는 기준선을 크게 능가했으며(76 vs 57), FQL, FAWAC 등의 기준선은 점수가 0에 가까웠습니다.

### 소거 실험
- **디노이징 단계 수 K**: K=10에서 최상의 성능을 보였습니다. K=1 또는 4에서는 에이전트가 대부분 시작 영역에 머물며 목표에 도달하지 못했습니다(그림 5).
- **그래디언트 안정성**: VINE는 5개 OGBench 작업에서 더 높은 성공률을 보였고, 역전파 그래디언트가 더 작고 안정적이었습니다(그림 4).

### 실제 세계 실험
소켓 삽입 작업, 20회 시도 평가. VINE는 SAC-Flow, Hil-SERL 등의 온라인 기준선과 비교되었습니다(논문에서 구체적인 성공률 수치는 명시되지 않았으며, 표 2는 이미지로 추출되지 않음).

## 경계 및 한계

논문은 한계를 명시적으로 나열하지 않았지만, 방법 설계에서 다음 경계를 추론할 수 있습니다:
- **적용 범위**: VINE는 흐름 매칭 정책을 위해 설계되었으며, 확산 정책에도 적용 가능하다고 주장하지만 확산 모델에 대한 체계적 검증은 제공되지 않았습니다. 비반복 생성 정책(예: 단일 단계 생성 모델)의 경우 VINE의 노이즈 주입 메커니즘은 적용할 수 없습니다.
- **온라인 RL 시나리오**: 알고리즘 1에서 선택적 온라인 RL 수집을 언급하지만, 논문은 온라인 RL에 대한 상세한 실험 데이터를 제공하지 않았으며 실제 세계 작업에 대한 제한된 결과만 제공합니다.
- **대규모 기반 모델**: 저자는 "향후 방향"에서 VINE를 대규모 기반 모델로 확장하는 것을 언급했지만, 현재 실험은 중소 규모 정책 네트워크(MLP 은닉층 [512, 512, 512, 512])만 다루며 수십억 파라미터 모델에서의 성능은 검증되지 않았습니다.
- **이론적 보장의 가정**: 정리 1과 추론 1은 조건부 흐름 매칭 손실의 점별 최소화기 가정에 의존하며, 실제 훈련에서 네트워크가 이 최적해에 완전히 수렴하지 않을 수 있으므로 이론적 보장의 엄밀성은 실무에서 검증이 필요합니다.

## 엔지니어링 시사점

재현 및 하류 팀을 위한 엔지니어링 지침:
- **샘플러 구현 먼저 확인**: VINE의 핵심 변경은 샘플러 계층에만 있으므로, 재현 시 `x̂_k = t_k * â_k + (1 - t_k) * z_k` 보간 공식과 시간표 `t_k ∈ {0.0, 0.1, …, 0.9}`가 원문과 일치하는지 우선 확인하십시오. 가장 흔한 실수는 시간표의 단조성입니다——`t_k`가 엄격히 증가하지 않으면 노이즈 주입의 어닐링 스케줄링이失效합니다.
- **BC 계수 α의 민감도**: α는 작업 간 차이가 매우 큽니다(antmaze-large는 10, scene-sparse는 300, puzzle-3x3-sparse는 1000). 재현 시 작업별로 α를 조정해야 하며, 통일된 값을 사용할 수 없습니다. 논문 표 4의 값을 출발점으로 10배 단위로 그리드 검색을 권장합니다.
- **Q 함수 수**: 두 개의 Q 함수 훈련은 안정성의 핵심입니다(actor는 평균, critic는 최솟값). 하류 구현이 단일 Q 함수만 사용하는 경우 VINE의 안정성 이점이 크게 감소할 수 있습니다.
- **그래디언트 단계 수 및 평가 빈도**: 오프라인 훈련 1M 그래디언트 단계, 20k 단계마다 50개 에피소드로 평가. 재현 시 충분한 훈련 단계를 보장해야 합니다——VINE의 안정성 이점은 훈련 후반(>500k 단계)에 충분히 나타나며, 조기 중단은 성능을 과소평가할 수 있습니다.
- **사전 훈련 정책의 호환성**: VINE는 사전 훈련된 흐름 매칭 정책을 직접 로드하며 생성 목표를 미세 조정할 필요가 없습니다. 그러나 사전 훈련 정책의 노이즈 스케줄링이 VINE의 보간 공식과 호환되는지 확인해야 합니다——사전 훈련 시 다른 노이즈 스케줄링(예: cosine schedule)을 사용한 경우 시간표를 다시 정렬해야 할 수 있습니다.
