---
$id: ent_paper_foresight_residual_rl_long_horizon_robot_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Foresight Residual RL for Long-Horizon Robot Manipulation with Vision-Language-Action Models
  zh: Foresight Residual RL for Long-Horizon Robot Manipulation with Vision-Language-Action Models
  ko: Foresight Residual RL for Long-Horizon Robot Manipulation with Vision-Language-Action Models
summary:
  en: 'Vision-Language-Action (VLA) policies offer strong general-purpose manipulation priors, but often fail on tight-tolerance,
    contact-rich assembly due to long-horizon credit assignment and subtask coupling: a state that is geometrically successful
    for the current skill can be brittle for downstream skills. We show this failure mode in residual reinforcement learning
    (RL) over a frozen VLA base.'
  zh: 本文提出 Foresight Residual RL 框架，用于解决长时程、因果耦合的机器人操作任务中，子任务成功但交接状态质量差导致下游失败的问题。该方法在基础 VLA 策略（π₀）之上训练残差策略，并用离线视觉预见预测器对子任务奖励进行重加权，以优化交接状态的可组合性。在
    Isaac Gym 的扳手-螺丝装配任务中，全任务成功率从恒定奖励残差 RL 的 54.5% 提升至 85.6%。
  ko: 'Vision-Language-Action (VLA) policies offer strong general-purpose manipulation priors, but often fail on tight-tolerance,
    contact-rich assembly due to long-horizon credit assignment and subtask coupling: a state that is geometrically successful
    for the current skill can be brittle for downstream skills. We show this failure mode in residual reinforcement learning
    (RL) over a frozen VLA base.'
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
- foresight
- residual
- rl
- long
- horizon
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Catch-up sweep 2026-08-05, source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section interpretation
    by DeepSeek (deepseek-chat, T<=0.3) with fact guardrails. 深读+数字白名单复核通过 2026-08-10（补网）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: arXiv:2607.16506 Foresight Residual RL for Long-Horizon Robot Manipulation with Vision-Language-A
  url: https://arxiv.org/abs/2607.16506
  date: '2026-07-17'
  accessed_at: '2026-08-05'
---

## 概述

本文提出 Foresight Residual RL 框架，用于解决长时程、因果耦合的机器人操作任务中，子任务成功但交接状态质量差导致下游失败的问题。该方法在基础 VLA 策略（π₀）之上训练残差策略，并用离线视觉预见预测器对子任务奖励进行重加权，以优化交接状态的可组合性。在 Isaac Gym 的扳手-螺丝装配任务中，全任务成功率从恒定奖励残差 RL 的 54.5% 提升至 85.6%。

## 它改变了什么

这项工作的核心改变在于，它把“子任务成功”这一传统优化目标，替换为“交接状态对下游任务的可组合性”这一更精细的优化目标。作者敏锐地指出，在接触丰富的装配任务中，子任务成功谓词定义了一个宽泛的终端状态等价类，但只有其中一部分状态能与下游阶段良好衔接。恒定奖励的残差 RL 虽然能大幅提升单子任务成功率（如 Insert 从 45.7% 提升至 92.2%），但全任务成功率却几乎无增益（54.5% vs 54.9%），这直接证明了“成功”与“可组合”之间的鸿沟。

该工作的真正贡献在于，它没有试图重新设计奖励函数或任务分解，而是引入了一个可学习的“前视值函数”来显式量化交接状态的下游价值。这改变了残差 RL 的训练信号：从“是否成功”变为“成功且对下游友好”。这种思路跳出了端到端学习和独立子任务训练的二元对立，为长时程操作任务提供了一种新的、可扩展的优化范式。

## 方法拆解

### 残差策略公式
动作由基础策略与残差策略加权组合：
a_t = π_k(o_t) ≜ π_k^0(o_t) + α · π_k^res(o_t)
其中 α ≪ 1（实验中 α = 0.1），确保训练初期保持基础策略行为。

### 前视值函数定义
对阶段 k < K，固定未来策略 π_{k+1:K}，前视值函数为：
V_{k+1:K}(s) = E_{π_{k+1:K}}[Σ_{t=0}^{T_{k+1:K}} γ^t β_K(s_{t+1}) | s_0^{(k+1)} = s]
其中 β_K 是最终阶段成功指示函数。

### 局部前视值函数
将阶段 k 的终端奖励 β_k 乘以前视值函数：
V_k^∘(s) = E_{π_k}[Σ_{t=0}^{T_k} γ^t β_k(s_{t+1}) V_{k+1:K}(s_{t+1}) | s_0^{(k)} = s]
该修正仅修改终端奖励，保持阶段内优化过程不变。

### 后向前视归纳（Algorithm 1）
从最后阶段 K 开始向前训练：
- k = K 时，V_{K+1:K} ≜ 1，用标准任务奖励训练 π_K
- k < K 时，先训练并固定下游策略 π_{k+1}，再训练前视预测器，然后用奖励 r_t = β_k(s_{t+1}) · p_φ(o_{t+1}) 训练 π_k^res

### 前视预测器训练（Algorithm 2）
三阶段流程：
1. 用基础策略 π_k^0 滚动收集 N 个成功终端状态
2. 对每个终端状态执行 K_rep 次下游策略独立滚动，记录成功计数 κ_i
3. 用二项负对数似然优化预测器 p_φ

训练目标：
L(φ) = -Σ_{i=1}^{N} [κ_i log p_φ(o_i) + (K_rep - κ_i) log(1 - p_φ(o_i))]

### 关键设计决策
- **离线估计**：在线蒙特卡洛估计方差高且计算开销大（评估单个终端状态需滚动最多 200 步乘以重复次数）；离线预测器直接拟合蒙特卡洛成功标签，提供校准估计
- **使用基础策略分布收集数据**：预测器需要在残差训练将其移向更好配置之前，对残差将访问的状态保持准确
- **小残差尺度 α**：限制策略改进导致的终端分布偏移，使增强策略的终端分布接近基础策略且在预测器插值范围内

### 架构细节
- **预测器**：DINOv2-S/14 CLS token（两个相机视角），自注意力融合，线性层，sigmoid 头；DINO 骨干用 LoRA 微调（秩 8）
- **残差策略**：仅腕部视角，冻结 DINOv2-S/14 提取 16×16 patch 特征，CNN（384→12），2 层 LSTM（256），MLP（512→256→128），actor 输出零初始化

## 关键创新

1. **前视值函数作为奖励调制信号**：这是首次将“下游成功概率”作为子任务终端奖励的乘性权重，直接优化交接状态的可组合性。与分布匹配方法（如 initiation overlapping）不同，它优化的是最终任务成功而非代理目标。

2. **离线二项式预测器**：用 K_rep 次蒙特卡洛滚动生成计数标签，并用二项负对数似然训练，尊重标签的计数结构而非回归目标。训练时间少于 5 分钟，计算开销极低。

3. **后向归纳训练顺序**：从最后阶段向前训练，确保每个子任务策略训练时下游策略已固定，前视值函数有明确的计算基础。这种顺序是必要的，因为训练子任务 k 需要滚动下游策略来估计 V_{k+1:K}。

## 实验与结果

**任务**：Isaac Gym 中扳手-螺丝装配，7-DoF Kuka IIWA + 11-DoF Robotiq 3 指夹爪，三阶段（Grasp 160 步、Move-Insert 200 步、Rotate 200 步），控制频率 20 Hz。

**主结果**（512 回合，4 种子）：

| 方法 | Grasp | Insert | Rotate | Grasp+Insert | Insert+Rotate | Full Task |
|------|-------|--------|--------|--------------|---------------|-----------|
| π₀（链式） | 87.1±1.4 | 45.7±6.1 | 93.4±3.0 | 37.1±1.5 | 61.5±4.6 | 41.4±3.3 |
| π₀ + Residual | 98.4±0.6 | 92.2±1.1 | 99.2±0.6 | 55.5±3.4 | 83.4±3.2 | 54.5±3.6 |
| π₀ + Residual with Foresight | 95.7±3.3 | 91.4±0.6 | 99.8±0.4 | 87.3±1.3 | 91.8±3.3 | **85.6±3.9** |

**关键发现**：
- 恒定奖励残差 RL 的 Full Task（54.5%）不优于端到端 π₀（54.9%），尽管 Insert 成功率翻倍（45.7%→92.2%）
- 前视修正达到 85.6%，比恒定奖励变体提升超过 30%
- Grasp→Insert 连续成功率从 55.5% 提升至 87.3%（+31.8%）

**终端状态质量**（Table III，平均预测器分数）：

| 方法 | Grasp 终端 | Insert 终端 |
|------|-----------|------------|
| π₀（基础） | 0.64 | 0.97 |
| + Residual | 0.32 | 0.86 |
| + Residual with Foresight | **0.73** | 0.91 |

恒定奖励残差 RL 在 Grasp 终端的分数从 0.64 降至 0.32，尽管子任务成功率提升；前视修正达到最高 Grasp 终端分数 0.73。

**预测器质量**（Table I）：Grasp→Insert 边界准确率 86.2%，Insert→Rotate 边界准确率 93.9%。

## 边界与局限

- **仿真局限**：所有评估均在 Isaac Gym 仿真中，未在真实硬件上验证。作者预期实际部署的主要障碍是残差策略的在线 RL 硬件成本，而非接触动力学差距。
- **任务单一性**：仅在单一扳手-螺丝任务上验证，且使用已知的阶段分解。未测试其他任务、其他阶段分解、其他 VLA 骨干网络。
- **一步前视近似**：仅在 k = K-1 或子任务 k+2,…,K 的成功率在子任务 k+1 成功条件下恒定时精确；更深前视需链式滚动所有剩余阶段（作者提及但未实现）。
- **分布偏移未定量分析**：作者未提供预测器在策略改进后分布偏移的定量分析，仅声称小的 α 限制偏移在插值范围内。
- **缺乏对比实验**：未与其他分布匹配方法（如 T-STAR、SCaR、Sequential Dexterity）直接对比。
- **视觉鲁棒性未分析**：未测试预测器对相机视角变化、光照变化等视觉扰动的鲁棒性。

## 工程启示

- **复现优先级**：先核对预测器训练数据收集流程——必须用基础策略（而非增强策略）的终端状态，且 K_rep = 5 次滚动是平衡方差与计算的关键。预测器训练仅需 20 epoch（<5 分钟），是成本最低的组件。
- **最易踩坑点**：残差尺度 α = 0.1 是分布偏移控制的核心。若 α 过大，增强策略的终端分布会超出预测器插值范围，导致奖励信号失真；若过小，残差策略无法有效改进终端状态。建议在 α 上做消融。
- **阶段转换检测**：基于标志的反应式检测（Grasp→Move-Insert 在抓取谓词激活时触发）是工程实现的关键细节。若检测不准确，会破坏前视值函数的时序对齐。
- **对下游团队的指导**：若你的任务具有因果耦合特性（如装配中需在旋转时保持插入），且已有可用的 VLA 基础策略，此框架可直接套用。但需注意：前视预测器需要下游策略可重复滚动（仿真中可行，真实硬件成本高）；若下游策略本身不稳定，预测器标签噪声会增大。
- **数据效率**：每子任务 2,560 个演示 + 每边界 2,560 个终端状态（各 5 次滚动）即可达到 85.6% 全任务成功率，数据需求相对可控。

## Overview
Vision-Language-Action (VLA) policies offer strong general-purpose manipulation priors, but often fail on tight-tolerance, contact-rich assembly due to long-horizon credit assignment and subtask coupling: a state that is geometrically successful for the current skill can be brittle for downstream skills. We show this failure mode in residual reinforcement learning (RL) over a frozen VLA base policy: constant sparse success rewards improve each subtask in isolation yet yield little or no gain when skills are chained, because terminal state quality is uncontrolled. We propose Foresight Residual RL, which optimizes handoff quality by augmenting each subtask's sparse success reward with an offline-estimated foresight value -- the probability of future subtask success conditioned on the terminal state of the current subtask. Concretely, we (i) train a visual foresight predictor from images of terminal states of the base policy, labeled using downstream rollout statistics, and (ii) train residual policies via backward foresight induction, using the predictor output as a reward multiplier. On a three-phase wrench-based nut-tightening assembly task in Isaac Gym (grasp, move-insert, rotate), our method achieves 85.6% full-task success, outperforming standard subtask residual RL (54.5%) and VLA baselines, while leaving per-subtask success unchanged. These results highlight that improving long-horizon performance requires shaping which successful states are produced at each sub-task, not only whether success occurs.

## 参考
- https://arxiv.org/abs/2607.16506

## 개요

본 논문은 장시간, 인과적으로 결합된 로봇 조작 작업에서 하위 작업은 성공하지만 인계 상태의 품질이 낮아 하류 작업이 실패하는 문제를 해결하기 위해 Foresight Residual RL 프레임워크를 제안한다. 이 방법은 기본 VLA 정책(π₀) 위에 잔차 정책을 훈련하고, 오프라인 시각적 전방 예측기를 사용하여 하위 작업 보상을 재가중함으로써 인계 상태의 조합 가능성을 최적화한다. Isaac Gym의 렌치-나사 조립 작업에서 전체 작업 성공률이 일정 보상 잔차 RL의 54.5%에서 85.6%로 향상되었다.

## 그것이 바꾸는 것

이 작업의 핵심 변화는 "하위 작업 성공"이라는 전통적 최적화 목표를 "하류 작업에 대한 인계 상태의 조합 가능성"이라는 더 세밀한 최적화 목표로 대체한 것이다. 저자들은 접촉이 풍부한 조립 작업에서 하위 작업 성공 술어가 광범위한 종단 상태 동치 클래스를 정의하지만, 그중 일부 상태만이 하류 단계와 잘 연결된다는 점을 날카롭게 지적한다. 일정 보상의 잔차 RL은 단일 하위 작업 성공률을 크게 향상시킬 수 있지만(예: Insert가 45.7%에서 92.2%로), 전체 작업 성공률은 거의 개선되지 않으며(54.5% vs 54.9%), 이는 "성공"과 "조합 가능성" 사이의 간극을 직접적으로 증명한다.

이 작업의 진정한 기여는 보상 함수나 작업 분해를 재설계하려 하지 않고, 학습 가능한 "전방 시야 가치 함수"를 도입하여 인계 상태의 하류 가치를 명시적으로 정량화한 것이다. 이는 잔차 RL의 훈련 신호를 "성공 여부"에서 "성공하고 하류에 우호적인" 것으로 변경한다. 이러한 접근 방식은 종단 간 학습과 독립 하위 작업 훈련의 이분법을 벗어나, 장시간 조작 작업을 위한 새롭고 확장 가능한 최적화 패러다임을 제공한다.

## 방법 분해

### 잔차 정책 공식
행동은 기본 정책과 잔차 정책의 가중 결합으로 구성된다:
a_t = π_k(o_t) ≜ π_k^0(o_t) + α · π_k^res(o_t)
여기서 α ≪ 1(실험에서 α = 0.1)로, 훈련 초기에 기본 정책의 행동을 유지한다.

### 전방 시야 가치 함수 정의
단계 k < K에 대해, 미래 정책 π_{k+1:K}를 고정하면 전방 시야 가치 함수는 다음과 같다:
V_{k+1:K}(s) = E_{π_{k+1:K}}[Σ_{t=0}^{T_{k+1:K}} γ^t β_K(s_{t+1}) | s_0^{(k+1)} = s]
여기서 β_K는 최종 단계 성공 지시 함수이다.

### 국소 전방 시야 가치 함수
단계 k의 종단 보상 β_k에 전방 시야 가치 함수를 곱한다:
V_k^∘(s) = E_{π_k}[Σ_{t=0}^{T_k} γ^t β_k(s_{t+1}) V_{k+1:K}(s_{t+1}) | s_0^{(k)} = s]
이 수정은 종단 보상만 변경하며, 단계 내 최적화 과정은 유지한다.

### 후방 전방 귀납(Algorithm 1)
마지막 단계 K에서 시작하여 앞으로 훈련한다:
- k = K일 때, V_{K+1:K} ≜ 1, 표준 작업 보상으로 π_K 훈련
- k < K일 때, 먼저 하류 정책 π_{k+1}을 훈련하고 고정한 다음, 전방 예측기를 훈련하고, 보상 r_t = β_k(s_{t+1}) · p_φ(o_{t+1})로 π_k^res 훈련

### 전방 예측기 훈련(Algorithm 2)
3단계 프로세스:
1. 기본 정책 π_k^0으로 롤아웃하여 N개의 성공 종단 상태 수집
2. 각 종단 상태에 대해 K_rep번 하류 정책 독립 롤아웃을 실행하고 성공 횟수 κ_i 기록
3. 이항 음의 로그 우도로 예측기 p_φ 최적화

훈련 목표:
L(φ) = -Σ_{i=1}^{N} [κ_i log p_φ(o_i) + (K_rep - κ_i) log(1 - p_φ(o_i))]

### 핵심 설계 결정
- **오프라인 추정**: 온라인 몬테카를로 추정은 분산이 높고 계산 비용이 크다(단일 종단 상태 평가에 최대 200스텝 × 반복 횟수 필요); 오프라인 예측기는 몬테카를로 성공 레이블을 직접 피팅하여 보정된 추정을 제공한다
- **기본 정책 분포로 데이터 수집**: 예측기는 잔차 훈련이 상태를 더 좋은 구성으로 이동시키기 전에 잔차가 방문할 상태에 대해 정확해야 한다
- **작은 잔차 스케일 α**: 정책 개선으로 인한 종단 분포 이동을 제한하여, 강화된 정책의 종단 분포가 기본 정책에 가깝고 예측기 보간 범위 내에 있도록 한다

### 아키텍처 세부 사항
- **예측기**: DINOv2-S/14 CLS 토큰(두 카메라 뷰), 자기 주의 융합, 선형 레이어, 시그모이드 헤드; DINO 백본은 LoRA로 미세 조정(랭크 8)
- **잔차 정책**: 손목 뷰만 사용, 동결된 DINOv2-S/14로 16×16 패치 특징 추출, CNN(384→12), 2층 LSTM(256), MLP(512→256→128), actor 출력은 0으로 초기화

## 핵심 혁신

1. **전방 시야 가치 함수를 보상 변조 신호로 사용**: 하류 성공 확률을 하위 작업 종단 보상의 곱셈 가중치로 사용한 최초의 사례로, 인계 상태의 조합 가능성을 직접 최적화한다. 분포 정합 방법(예: initiation overlapping)과 달리 대리 목표가 아닌 최종 작업 성공을 최적화한다.

2. **오프라인 이항 예측기**: K_rep번 몬테카를로 롤아웃으로 카운트 레이블을 생성하고 이항 음의 로그 우도로 훈련하여, 회귀 목표가 아닌 레이블의 카운트 구조를 존중한다. 훈련 시간은 5분 미만으로 계산 비용이 매우 낮다.

3. **후방 귀납 훈련 순서**: 마지막 단계에서 앞으로 훈련하여 각 하위 작업 정책 훈련 시 하류 정책이 고정되고 전방 시야 가치 함수가 명확한 계산 기반을 갖도록 한다. 이 순서는 하위 작업 k 훈련 시 V_{k+1:K}를 추정하기 위해 하류 정책을 롤아웃해야 하므로 필수적이다.

## 실험 및 결과

**작업**: Isaac Gym의 렌치-나사 조립, 7-DoF Kuka IIWA + 11-DoF Robotiq 3핑거 그리퍼, 3단계(Grasp 160스텝, Move-Insert 200스텝, Rotate 200스텝), 제어 주파수 20Hz.

**주요 결과**(512 에피소드, 4 시드):

| 방법 | Grasp | Insert | Rotate | Grasp+Insert | Insert+Rotate | Full Task |
|------|-------|--------|--------|--------------|---------------|-----------|
| π₀(체인) | 87.1±1.4 | 45.7±6.1 | 93.4±3.0 | 37.1±1.5 | 61.5±4.6 | 41.4±3.3 |
| π₀ + Residual | 98.4±0.6 | 92.2±1.1 | 99.2±0.6 | 55.5±3.4 | 83.4±3.2 | 54.5±3.6 |
| π₀ + Residual with Foresight | 95.7±3.3 | 91.4±0.6 | 99.8±0.4 | 87.3±1.3 | 91.8±3.3 | **85.6±3.9** |

**핵심 발견**:
- 일정 보상 잔차 RL의 Full Task(54.5%)는 종단 간 π₀(54.9%)보다 우수하지 않으며, Insert 성공률이 두 배(45.7%→92.2%)임에도 불구하고
- 전방 시야 수정은 85.6%에 도달하여 일정 보상 변형보다 30% 이상 향상
- Grasp→Insert 연속 성공률이 55.5%에서 87.3%로 향상(+31.8%)

**종단 상태 품질**(Table III, 평균 예측기 점수):

| 방법 | Grasp 종단 | Insert 종단 |
|------|-----------|------------|
| π₀(기본) | 0.64 | 0.97 |
| + Residual | 0.32 | 0.86 |
| + Residual with Foresight | **0.73** | 0.91 |

일정 보상 잔차 RL은 하위 작업 성공률이 향상되었음에도 Grasp 종단 점수가 0.64에서 0.32로 하락; 전방 시야 수정은 최고 Grasp 종단 점수 0.73에 도달.

**예측기 품질**(Table I): Grasp→Insert 경계 정확도 86.2%, Insert→Rotate 경계 정확도 93.9%.

## 경계 및 한계

- **시뮬레이션 한계**: 모든 평가는 Isaac Gym 시뮬레이션에서 수행되었으며 실제 하드웨어에서 검증되지 않았다. 저자들은 실제 배포의 주요 장애물이 접촉 역학 차이가 아닌 잔차 정책의 온라인 RL 하드웨어 비용일 것으로 예상한다.
- **작업 단일성**: 단일 렌치-나사 작업에서만 검증되었으며 알려진 단계 분해를 사용한다. 다른 작업, 다른 단계 분해, 다른 VLA 백본은 테스트되지 않았다.
- **1단계 전방 시야 근사**: k = K-1 또는 하위 작업 k+2,…,K의 성공률이 하위 작업 k+1 성공 조건에서 일정할 때만 정확; 더 깊은 전방 시야는 모든 남은 단계를 체인 롤아웃해야 한다(저자가 언급했지만 구현하지 않음).
- **분포 이동의 정량적 분석 부재**: 저자는 정책 개선 후 예측기의 분포 이동에 대한 정량적 분석을 제공하지 않으며, 작은 α가 이동을 보간 범위 내로 제한한다고만 주장한다.
- **비교 실험 부재**: 다른 분포 정합 방법(예: T-STAR, SCaR, Sequential Dexterity)과의 직접 비교가 없다.
- **시각적 강건성 분석 부재**: 카메라 뷰 변화, 조명 변화 등 시각적 교란에 대한 예측기의 강건성은 테스트되지 않았다.

## 공학적 시사점

- **재현 우선순위**: 예측기 훈련 데이터 수집 프로세스를 먼저 확인 — 기본 정책(강화 정책이 아닌)의 종단 상태를 사용해야 하며, K_rep = 5번 롤아웃이 분산과 계산의 균형을 맞추는 핵심이다. 예측기 훈련은 20 epoch(<5분)만 필요하며 가장 비용이 낮은 구성 요소이다.
- **가장 실수하기 쉬운 지점**: 잔차 스케일 α = 0.1은 분포 이동 제어의 핵심이다. α가 너무 크면 강화 정책의 종단 분포가 예측기 보간 범위를 벗어나 보상 신호가 왜곡된다; 너무 작으면 잔차 정책이 종단 상태를 효과적으로 개선할 수 없다. α에 대한 절제 실험을 권장한다.
- **단계 전환 감지**: 플래그 기반 반응형 감지(Grasp→Move-Insert는 그리핑 술어 활성화 시 트리거)는 공학 구현의 핵심 세부 사항이다. 감지가 부정확하면 전방 시야 가치 함수의 시간 정렬이 깨진다.
- **하류 팀에 대한 지침**: 작업이 인과적 결합 특성(예: 회전 중 삽입 유지)을 가지며 사용 가능한 VLA 기본 정책이 있다면 이 프레임워크를 직접 적용할 수 있다. 단, 전방 예측기는 하류 정책을 반복 롤아웃할 수 있어야 하며(시뮬레이션에서 가능, 실제 하드웨어 비용 높음); 하류 정책 자체가 불안정하면 예측기 레이블 노이즈가 증가한다.
- **데이터 효율성**: 하위 작업당 2,560개 데모 + 경계당 2,560개 종단 상태(각 5회 롤아웃)로 85.6% 전체 작업 성공률에 도달할 수 있어 데이터 요구량이 상대적으로 관리 가능하다.
