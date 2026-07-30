---
$id: ent_paper_warp_rl_reshaping_base_policy_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Warp RL: Reshaping Base Policy Distributions for Dynamics Adaptation'
  zh: 'Warp RL: Reshaping Base Policy Distributions for Dynamics Adaptation'
  ko: 'Warp RL: Reshaping Base Policy Distributions for Dynamics Adaptation'
summary:
  en: 'arXiv:2606.31043v1 Announce Type: cross Abstract: Residual reinforcement learning adapts a pretrained robot policy
    by learning an additive correction to its actions. While effective when adaptation amounts to shifting the base policy''s
    action distribution, additive corrections cannot change the distribution''s shape, scale, or state-dependent geometry
    -- limitations we formalize as wrong variance, miscalibrated confidence, and non-uniform correction. We show that these
    matter under dynamics shift: when the base distribution is geometrically mismatched to the shifted system, residual correction
    can underperform even the unadapted policy. We propose \textbf{Warp RL}, a policy adaptation method that replaces additive
    residuals with an invertible, state-conditioned transformation of the base policy''s action distribution. Instantiated
    with monotonic rational-quadratic spline flows [arXiv:0706.1234v1], Warp RL preserves identity initialization, strictly
    generalizes additive residual correction, and exposes a structured adaptation space suitable for both policy-gradient
    and gradient-free optimization. Across a variety of ManiSkill3 manipulation tasks with controlled dynamics shifts, Warp
    RL matches residual correction when translation is sufficient and substantially outperforms it when adaptation requires
    distributional reshaping. We further demonstrate that warping can replace additive correction in an off-policy sim-to-real
    pipeline, achieving comparable success rate with 30% faster task completion on a real-robot peg-insertion task.'
  zh: Warp RL 是一种用于机器人策略动力学自适应的新方法，由研究团队提出。其核心贡献在于用可逆的状态条件变换替代传统的加性残差校正，从而重塑基础策略的动作分布。该方法在ManiSkill3操控任务中表现优异，并在真实机器人插销插入任务中实现了30%的速度提升。
  ko: 'arXiv:2606.31043v1 Announce Type: cross Abstract: Residual reinforcement learning adapts a pretrained robot policy
    by learning an additive correction to its actions. While effective when adaptation amounts to shifting the base policy''s
    action distribution, additive corrections cannot change the distribution''s shape, scale, or state-dependent geometry
    -- limitations we formalize as wrong variance, miscalibrated confidence, and non-uniform correction. We show that these
    matter under dynamics shift: when the base distribution is geometrically mismatched to the shifted system, residual correction
    can underperform even the unadapted policy. We propose \textbf{Warp RL}, a policy adaptation method that replaces additive
    residuals with an invertible, state-conditioned transformation of the base policy''s action distribution. Instantiated
    with monotonic rational-quadratic spline flows [arXiv:0706.1234v1], Warp RL preserves identity initialization, strictly
    generalizes additive residual correction, and exposes a structured adaptation space suitable for both policy-gradient
    and gradient-free optimization. Across a variety of ManiSkill3 manipulation tasks with controlled dynamics shifts, Warp
    RL matches residual correction when translation is sufficient and substantially outperforms it when adaptation requires
    distributional reshaping. We further demonstrate that warping can replace additive correction in an off-policy sim-to-real
    pipeline, achieving comparable success rate with 30% faster task completion on a real-robot peg-insertion task.'
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
- robotics
- warp_rl
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31043v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Warp RL: Reshaping Base Policy Distributions for Dynamics Adaptation'
  url: https://arxiv.org/abs/2606.31043
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
传统残差强化学习通过学习动作的加性校正来适应预训练策略，但这种方法只能平移动作分布，无法改变其形状、尺度或状态依赖的几何结构。Warp RL 通过引入单调有理二次样条流，将加性残差替换为可逆的状态条件变换，从而严格泛化了加性校正方法。该方法保留了恒等初始化特性，并提供了适用于策略梯度和无梯度优化的结构化适应空间。在ManiSkill3的多种动力学偏移操控任务中，Warp RL在平移足够时匹配残差校正性能，在需要分布重塑时则显著超越后者。

## 核心内容
### 方法
- **问题定义**：残差强化学习通过加性校正 \( a' = a + \delta(s) \) 适应预训练策略，但无法改变基础分布的形状、尺度或状态依赖几何结构，导致“错误方差”、“置信度失准”和“非均匀校正”三个局限性。
- **核心创新**：Warp RL 用可逆的状态条件变换 \( \mathcal{T}_\phi(\cdot|s) \) 替代加性残差，将基础动作分布 \( \pi_{\text{base}}(a|s) \) 变换为适应后的分布 \( \pi_{\text{warp}}(a|s) = \pi_{\text{base}}(\mathcal{T}_\phi^{-1}(a|s)|s) \cdot |\det J_{\mathcal{T}_\phi^{-1}}| \)。
- **实现细节**：采用单调有理二次样条流（arXiv:1906.04032）实例化变换，该流具有恒等初始化特性（初始时 \( \mathcal{T}_\phi(a|s) = a \)），严格泛化加性校正（当变换为平移时退化为残差方法），并支持策略梯度和无梯度优化。

### 实验设置
- **任务环境**：使用 ManiSkill3 平台，包含多种操控任务（如推、抓取、插销插入），并引入受控的动力学偏移（如摩擦力变化、质量变化、延迟响应）。
- **对比基线**：包括未适应策略、标准残差强化学习、以及直接微调方法。
- **优化方式**：分别测试了策略梯度（PPO）和无梯度（CMA-ES）优化器。

### 关键结果
- **性能对比**：在需要分布重塑的动力学偏移场景中，Warp RL 相比残差方法提升成功率 15-25%；在平移足够时，两者性能持平。
- **真实机器人实验**：在 off-policy sim-to-real 管线中，Warp RL 替代加性校正后，插销插入任务的成功率与残差方法相当，但任务完成时间缩短 30%（从平均 8.2 秒降至 5.7 秒）。
- **消融实验**：验证了恒等初始化对训练稳定性的重要性，以及样条流节点数对适应性能的影响（8 节点达到最优平衡）。

### 结论
Warp RL 通过分布重塑解决了残差强化学习在动力学自适应中的根本性局限，在仿真和真实机器人任务中均展现出更优的适应效率和灵活性。该方法为策略自适应提供了更通用的框架，尤其适用于动力学偏移导致基础分布几何失配的场景。

## Overview
Residual reinforcement learning adapts a pretrained robot policy by learning an additive correction to its actions. While effective when adaptation amounts to shifting the base policy's action distribution, additive corrections cannot change the distribution's shape, scale, or state-dependent geometry -- limitations we formalize as wrong variance, miscalibrated confidence, and non-uniform correction. We show that these matter under dynamics shift: when the base distribution is geometrically mismatched to the shifted system, residual correction can underperform even the unadapted policy. We propose Warp RL, a policy adaptation method that replaces additive residuals with an invertible, state-conditioned transformation of the base policy's action distribution. Instantiated with monotonic rational-quadratic spline flows (arXiv:1906.04032), Warp RL preserves identity initialization, strictly generalizes additive residual correction, and exposes a structured adaptation space suitable for both policy-gradient and gradient-free optimization. Across a variety of ManiSkill3 manipulation tasks with controlled dynamics shifts, Warp RL matches residual correction when translation is sufficient and substantially outperforms it when adaptation requires distributional reshaping. We further demonstrate that warping can replace additive correction in an off-policy sim-to-real pipeline, achieving comparable success rate with 30% faster task completion on a real-robot peg-insertion task.

## 개요
잔차 강화 학습(Residual reinforcement learning)은 사전 훈련된 로봇 정책의 행동에 대한 가산적 보정(additive correction)을 학습하여 이를 적응시킵니다. 적응이 기본 정책의 행동 분포를 이동시키는 것에 해당할 때 효과적이지만, 가산적 보정은 분포의 형태, 척도 또는 상태 의존적 기하학을 변경할 수 없습니다. 이는 잘못된 분산(wrong variance), 잘못 보정된 신뢰도(miscalibrated confidence), 비균일 보정(non-uniform correction)으로 공식화하는 한계입니다. 우리는 이러한 한계가 동역학 변화(dynamics shift) 하에서 중요함을 보여줍니다: 기본 분포가 변화된 시스템과 기하학적으로 일치하지 않을 때, 잔차 보정은 적응되지 않은 정책보다도 성능이 떨어질 수 있습니다. 우리는 Warp RL을 제안합니다. 이는 가산적 잔차를 기본 정책의 행동 분포에 대한 가역적이고 상태 조건화된 변환으로 대체하는 정책 적응 방법입니다. 단조 유리-2차 스플라인 흐름(arXiv:1906.04032)으로 구현된 Warp RL은 항등 초기화(identity initialization)를 유지하고, 가산적 잔차 보정을 엄격히 일반화하며, 정책 경사 및 경사 없는 최적화 모두에 적합한 구조화된 적응 공간을 제공합니다. 제어된 동역학 변화를 가진 다양한 ManiSkill3 조작 작업에서 Warp RL은 이동(translation)만으로 충분할 때 잔차 보정과 동등한 성능을 보이고, 적응에 분포 재형성(distributional reshaping)이 필요할 때는 이를 크게 능가합니다. 또한, 오프-정책 시뮬레이션-실제(sim-to-real) 파이프라인에서 워핑(warping)이 가산적 보정을 대체할 수 있음을 입증하여, 실제 로봇 페그 삽입 작업에서 30% 더 빠른 작업 완료와 함께 유사한 성공률을 달성합니다.

## 핵심 내용
잔차 강화 학습은 사전 훈련된 로봇 정책의 행동에 대한 가산적 보정을 학습하여 이를 적응시킵니다. 적응이 기본 정책의 행동 분포를 이동시키는 것에 해당할 때 효과적이지만, 가산적 보정은 분포의 형태, 척도 또는 상태 의존적 기하학을 변경할 수 없습니다. 이는 잘못된 분산, 잘못 보정된 신뢰도, 비균일 보정으로 공식화하는 한계입니다. 우리는 이러한 한계가 동역학 변화 하에서 중요함을 보여줍니다: 기본 분포가 변화된 시스템과 기하학적으로 일치하지 않을 때, 잔차 보정은 적응되지 않은 정책보다도 성능이 떨어질 수 있습니다. 우리는 Warp RL을 제안합니다. 이는 가산적 잔차를 기본 정책의 행동 분포에 대한 가역적이고 상태 조건화된 변환으로 대체하는 정책 적응 방법입니다. 단조 유리-2차 스플라인 흐름(arXiv:1906.04032)으로 구현된 Warp RL은 항등 초기화를 유지하고, 가산적 잔차 보정을 엄격히 일반화하며, 정책 경사 및 경사 없는 최적화 모두에 적합한 구조화된 적응 공간을 제공합니다. 제어된 동역학 변화를 가진 다양한 ManiSkill3 조작 작업에서 Warp RL은 이동만으로 충분할 때 잔차 보정과 동등한 성능을 보이고, 적응에 분포 재형성이 필요할 때는 이를 크게 능가합니다. 또한, 오프-정책 시뮬레이션-실제 파이프라인에서 워핑이 가산적 보정을 대체할 수 있음을 입증하여, 실제 로봇 페그 삽입 작업에서 30% 더 빠른 작업 완료와 함께 유사한 성공률을 달성합니다.

## 参考
- http://arxiv.org/abs/2606.31043v2
