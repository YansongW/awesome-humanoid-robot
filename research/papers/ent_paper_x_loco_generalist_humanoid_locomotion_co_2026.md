---
$id: ent_paper_x_loco_generalist_humanoid_locomotion_co_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'X-Loco: Towards Generalist Humanoid Locomotion Control via Synergetic Policy Distillation'
  zh: 'X-Loco: Towards Generalist Humanoid Locomotion Control via Synergetic Policy Distillation'
  ko: 'X-Loco: Towards Generalist Humanoid Locomotion Control via Synergetic Policy Distillation'
summary:
  en: While recent advances have demonstrated strong performance in individual humanoid skills such as upright locomotion,
    fall recovery and whole-body coordination, learning a single policy that masters all these skills remains challenging
    due to the diverse dynamics and conflicting control objectives involved. To address this, we introduce X-Loco, a framework
    for training a vision-based generalist.
  zh: X-Loco 提出一种协同策略蒸馏框架，将三个特权专家策略（直立行走、跌倒恢复、全身协调）整合为单一视觉学生策略，在 Unitree G1 人形机器人上实现无需参考运动的通用运动控制。核心贡献在于通过 CASS 动态专家选择、SAR
    退火混合和 SFI 随机跌倒注入，弥合了专家能力与通用策略之间的鸿沟，并在仿真和真实世界验证了跨任务泛化能力。
  ko: While recent advances have demonstrated strong performance in individual humanoid skills such as upright locomotion,
    fall recovery and whole-body coordination, learning a single policy that masters all these skills remains challenging
    due to the diverse dynamics and conflicting control objectives involved. To address this, we introduce X-Loco, a framework
    for training a vision-based generalist.
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
- x
- loco
- generalist
- humanoid
- locomotion
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Catch-up sweep 2026-08-05, source channel(s): xiaoze_P128. Full text from arXiv (HTML or PDF); zh six-section interpretation
    by DeepSeek (deepseek-chat, T<=0.3) with fact guardrails. [2026-08-05] guardrail fix: unverifiable numbers corrected to
    full-text-verbatim or marked as computed/未提取 (catchup sweep audit). 深读+数字白名单复核通过 2026-08-10（补网）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2603.03733 X-Loco: Towards Generalist Humanoid Locomotion Control via Synergetic Policy Dis'
  url: https://arxiv.org/abs/2603.03733
  date: '2026-03-04'
  accessed_at: '2026-08-05'
---

## 概述

X-Loco 提出一种协同策略蒸馏框架，将三个特权专家策略（直立行走、跌倒恢复、全身协调）整合为单一视觉学生策略，在 Unitree G1 人形机器人上实现无需参考运动的通用运动控制。核心贡献在于通过 CASS 动态专家选择、SAR 退火混合和 SFI 随机跌倒注入，弥合了专家能力与通用策略之间的鸿沟，并在仿真和真实世界验证了跨任务泛化能力。

## 它改变了什么

现有的人形运动控制研究长期处于"碎片化"状态：有的方法专攻地形穿越，有的专攻跌倒恢复，但没有任何单一框架能同时处理"跌倒后自主爬起并继续穿越复杂地形"这类复合场景。X-Loco 真正改变的是将"专家能力整合"从手工设计奖励的困境中解放出来——它不再试图让一个策略学会所有技能，而是通过蒸馏机制让通用策略继承多个专家的行为模式。

这一转变的深层意义在于：它承认了"通用性"与"专业性"之间的张力无法通过单一策略的容量扩展解决，转而通过架构设计（MoE）和训练调度（SAR 退火）来调和。相比 BeyondMimic 等依赖参考运动的方法，X-Loco 在无参考运动条件下实现了全身协调技能（如攀爬、翻滚），这标志着通用人形控制从"模仿已知"迈向"组合已知"的范式转变。

## 方法拆解

### 专家策略训练
- **π_l（直立行走）**：使用历史编码器（10 步窗口）和海拔图编码器，AMP 风格奖励权重 3.0，速度跟踪权重 5.0，存活奖励 2.0。参考动作来自 LAFAN1 数据集重定向。
- **π_r（跌倒恢复）**：忽略地形信息，仅用历史编码器和 actor，在仰卧/俯卧姿态初始化并加入大关节噪声。AMP 奖励权重高达 80.0，角速度惩罚 25.0，髋关节偏差惩罚 -10.0，大腿方向奖励 10.0。
- **π_w（全身协调）**：使用海拔图编码器（1.6m×1.0m 网格，0.1m 分辨率），跟踪箱体攀爬和翻滚等全身运动，奖励函数包含身体位置/姿态/速度跟踪和锚点约束。

### 协同蒸馏机制
- **CASS 选择**：基于头部高度 b_t 和地形上下文 I_t 选择专家。b_t < 1.1m → π_r；b_t ≥ 1.1m 且 I_t=1（高平台）→ π_w；I_t=2（悬挂障碍）→ π_w；否则 → π_l。
- **SAR 混合**：a_env = b_t·a*_t + (1−b_t)·π_g(o_{g,t})，其中 b_t ~ Bernoulli(ρ)。ρ 初始为 1.0，当蒸馏损失 < 0.005 时衰减 1e−4，损失 > 0.010 时暂停衰减（滞回区间）。
- **SFI 注入**：在脆弱场景（高速转弯、翻滚）施加随机外力，迫使机器人进入恢复状态。额外终止条件：头部高度缓冲方差低于阈值 δ 时终止 episode，防止 OOD 数据污染。

### 学生策略架构
- MoE 架构：门控网络 + 3 个专家（均为 3 层 MLP [512, 256, 128]）
- CNN 深度编码器：64×64 深度图 → 128 维潜表征
- 历史编码器：10 步本体感觉序列 → 128 维
- 蒸馏损失：ℒ_distill = MSE(π_g(o_{u,t}), a*_t)

### 深度 sim-to-real 桥接
- 多阶段管线：加性高斯噪声（σ=0.02m）、高斯滤波（3×3 核，σ=1.0）、相机外参随机化（位置 ±0.05m，俯仰 ±10°）、FOV 随机化（±10°）
- 真实深度图像应用孔洞填充和高斯滤波

## 关键创新

1. **CASS 动态专家选择**：不同于静态 MoE 或固定任务切换，CASS 根据机器人实时状态（头部高度）和地形上下文动态选择指导专家，使得蒸馏过程能自适应处理"行走→跌倒→恢复→继续行走"的连续状态转换。这是首个将跌倒恢复纳入通用蒸馏框架的设计。

2. **SAR 退火调度**：通过滞回区间（τ_low=0.005, τ_high=0.010）控制 ρ 衰减，避免了蒸馏损失波动导致的训练不稳定。这一机制本质上是"课程学习"的变体——先完全跟随专家，再逐步放开自主探索，但比传统课程学习更精细地控制了探索-利用平衡。

3. **SFI 随机跌倒注入**：在训练中主动制造"跌倒-恢复"循环，而非被动等待失败发生。这解决了通用策略在长 horizon 任务中"一旦跌倒就永久失败"的稀疏奖励问题，使策略学会从失败中恢复而非简单规避风险。

## 实验与结果


| 方法 | Slope R_succ | Pit R_succ | Stairs R_succ | WBC R̄_succ | Recovery R_succ |
|------|-------------|------------|---------------|------------|----------------|
| MoRE | 0.992 | 0.844 | 0.926 | - | - |
| PPO | 0.823 | 0.793 | 0.781 | - | - |
| AHC | 0.968 | 0.403 | 0.278 | - | 1.000 |
| X-Loco | 0.982 | 0.878 | 0.958 | 0.871 | 1.000 |

**消融实验**：
- Ours w/o CASS：平均 R̄_succ = 0.783（Locomotion 0.903, WBC 0.446）
- Ours w/o MoE：平均 R̄_succ = 0.749（Locomotion 0.692, WBC 0.561）
- MoE-3：平均 R̄_succ = 0.779（Locomotion 0.628, WBC 0.709）
- MoE-2 (Ours)：平均 R̄_succ = 0.928（Locomotion 0.939, WBC 0.845）
- Ours w/o SFI：Recovery R_succ = 0.912 vs Ours 0.958

**关键解读**：
- X-Loco 在直立行走任务中平均成功率 0.939，超过 PPO（0.799）和 AHC（0.550），与 MoRE（0.921）竞争，但 MoRE 无法处理 WBC 和 Recovery。
- WBC 任务成功率 0.871 是"无参考运动"条件下的首次成功，但相比专家（1.000）仍有 0.129 的性能差距（由 1.000−0.871 计算，约 12.9%），作者承认这是最困难的迁移场景。
- SFI 将恢复成功率从 0.912 提升至 0.958，验证了主动注入失败场景的必要性。
- MoE-2 优于 MoE-3 表明：专家数量并非越多越好，任务重叠可能导致门控网络混淆。

## 边界与局限

- **感知范围受限**：窄 FOV 相机（RealSense D435i）导致有限的感知时域，无法提前规划远距离地形。
- **传感器噪声建模不完美**：深度增强管线（高斯噪声+滤波）无法完全模拟真实传感器的系统性误差（如边缘伪影、反射干扰）。
- **专家性能上界**：蒸馏依赖行为克隆，策略无法超越专家示范。在专家未覆盖的边缘情况（如极端地形组合）下性能显著下降。
- **未验证的泛化**：未测试松软地面、动态障碍、多机器人平台迁移；未与其他通用控制框架（如大模型方法）对比。
- **计算资源未量化**：未报告训练 GPU 型号、总训练时间、内存占用等关键工程指标。

## 工程启示

1. **复现优先级**：先核对 CASS 的阈值（b_t=1.1m）和地形上下文映射（I_t=1/2），这是蒸馏正确性的关键。若头部高度估计有偏差，会导致专家选择错误，整个蒸馏过程失效。

2. **最易踩坑点**：SAR 的 ρ 调度——滞回区间（0.005/0.010）和衰减步长（1e−4）需要精确匹配。ρ 衰减过快会导致学生策略过早自主探索而崩溃；过慢则蒸馏效率低下。建议先在小规模环境验证 ρ 曲线。

3. **SFI 的终止条件**：头部高度缓冲方差阈值 δ 未给出具体值，这是防止 OOD 数据破坏的关键。建议根据机器人身高（G1 约 1.3m）和步态周期（约 0.5s）经验设定，并做敏感性分析。

4. **深度增强管线**：相机外参随机化范围（位置 ±0.05m，俯仰 ±10°）和 FOV 随机化（±10°）是 sim-to-real 成功的关键。真实部署时务必先做相机标定，确保随机化范围覆盖实际安装误差。

5. **PD 参数不可随意修改**：Table V 的 K_p/K_d 值直接来自文献 [28]，且与动作缩放（Action Scale）耦合。修改任一参数都会改变动作空间的有效范围，需重新训练所有专家策略。

## 参考
- https://arxiv.org/abs/2603.03733

## Overview

X-Loco proposes a collaborative policy distillation framework that integrates three privileged expert policies (upright walking, fall recovery, whole-body coordination) into a single vision-based student policy, achieving reference-motion-free general locomotion control on the Unitree G1 humanoid robot. The core contribution lies in bridging the gap between expert capabilities and a general policy through CASS dynamic expert selection, SAR annealed mixing, and SFI stochastic fall injection, with cross-task generalization validated in both simulation and the real world.

## What It Changes

Existing humanoid locomotion control research has long been in a "fragmented" state: some methods specialize in terrain traversal, others in fall recovery, but no single framework can simultaneously handle composite scenarios such as "autonomously getting up after a fall and continuing to traverse complex terrain." What X-Loco truly changes is liberating "expert capability integration" from the困境 of hand-crafted reward design—it no longer attempts to make a single policy learn all skills, but instead enables a general policy to inherit behavioral patterns from multiple experts through a distillation mechanism.

The deeper significance of this shift is that it acknowledges the tension between "generality" and "specialization" cannot be resolved by scaling up the capacity of a single policy, and instead reconciles it through architectural design (MoE) and training scheduling (SAR annealing). Compared to methods like BeyondMimic that rely on reference motions, X-Loco achieves whole-body coordination skills (e.g., climbing, rolling) without reference motions, marking a paradigm shift in general humanoid control from "imitating the known" to "combining the known."

## Method Breakdown

### Expert Policy Training
- **π_l (upright walking)**: Uses a history encoder (10-step window) and elevation map encoder, with AMP-style reward weight 3.0, velocity tracking weight 5.0, and survival reward 2.0. Reference motions come from LAFAN1 dataset retargeting.
- **π_r (fall recovery)**: Ignores terrain information, using only the history encoder and actor, initialized in supine/prone postures with large joint noise. AMP reward weight is as high as 80.0, angular velocity penalty 25.0, hip deviation penalty -10.0, and thigh orientation reward 10.0.
- **π_w (whole-body coordination)**: Uses an elevation map encoder (1.6m×1.0m grid, 0.1m resolution), tracking whole-body motions such as box climbing and rolling, with a reward function including body position/orientation/velocity tracking and anchor constraints.

### Collaborative Distillation Mechanism
- **CASS selection**: Selects experts based on head height b_t and terrain context I_t. b_t < 1.1m → π_r; b_t ≥ 1.1m and I_t=1 (high platform) → π_w; I_t=2 (overhead obstacle) → π_w; otherwise → π_l.
- **SAR mixing**: a_env = b_t·a*_t + (1−b_t)·π_g(o_{g,t}), where b_t ~ Bernoulli(ρ). ρ is initially 1.0, decays by 1e−4 when distillation loss < 0.005, and pauses decay when loss > 0.010 (hysteresis interval).
- **SFI injection**: Applies random external forces in fragile scenarios (high-speed turning, rolling) to force the robot into recovery states. Additional termination condition: episode terminates when head height buffer variance falls below threshold δ, preventing OOD data contamination.

### Student Policy Architecture
- MoE architecture: gating network + 3 experts (all 3-layer MLPs [512, 256, 128])
- CNN depth encoder: 64×64 depth image → 128-dimensional latent representation
- History encoder: 10-step proprioceptive sequence → 128 dimensions
- Distillation loss: ℒ_distill = MSE(π_g(o_{u,t}), a*_t)

### Deep Sim-to-Real Bridging
- Multi-stage pipeline: additive Gaussian noise (σ=0.02m), Gaussian filtering (3×3 kernel, σ=1.0), camera extrinsic randomization (position ±0.05m, pitch ±10°), FOV randomization (±10°)
- Real depth images undergo hole filling and Gaussian filtering

## Key Innovations

1. **CASS dynamic expert selection**: Unlike static MoE or fixed task switching, CASS dynamically selects the guiding expert based on the robot's real-time state (head height) and terrain context, enabling the distillation process to adaptively handle continuous state transitions of "walking → falling → recovering → continuing to walk." This is the first design to incorporate fall recovery into a general distillation framework.

2. **SAR annealed scheduling**: Controls ρ decay through a hysteresis interval (τ_low=0.005, τ_high=0.010), avoiding training instability caused by distillation loss fluctuations. This mechanism is essentially a variant of "curriculum learning"—first fully following the expert, then gradually releasing autonomous exploration—but with finer control over the exploration-exploitation balance than traditional curriculum learning.

3. **SFI stochastic fall injection**: Actively creates "fall-recovery" cycles during training rather than passively waiting for failures to occur. This addresses the sparse reward problem in long-horizon tasks where a general policy "permanently fails once it falls," enabling the policy to learn recovery from failure rather than simply avoiding risk.

## Experiments and Results

| Method | Slope R_succ | Pit R_succ | Stairs R_succ | WBC R̄_succ | Recovery R_succ |
|--------|-------------|------------|---------------|------------|----------------|
| MoRE | 0.992 | 0.844 | 0.926 | - | - |
| PPO | 0.823 | 0.793 | 0.781 | - | - |
| AHC | 0.968 | 0.403 | 0.278 | - | 1.000 |
| X-Loco | 0.982 | 0.878 | 0.958 | 0.871 | 1.000 |

**Ablation studies**:
- Ours w/o CASS: average R̄_succ = 0.783 (Locomotion 0.903, WBC 0.446)
- Ours w/o MoE: average R̄_succ = 0.749 (Locomotion 0.692, WBC 0.561)
- MoE-3: average R̄_succ = 0.779 (Locomotion 0.628, WBC 0.709)
- MoE-2 (Ours): average R̄_succ = 0.928 (Locomotion 0.939, WBC 0.845)
- Ours w/o SFI: Recovery R_succ = 0.912 vs Ours 0.958

**Key interpretations**:
- X-Loco achieves an average success rate of 0.939 in upright walking tasks, surpassing PPO (0.799) and AHC (0.550), and competing with MoRE (0.921), but MoRE cannot handle WBC and Recovery.
- The WBC task success rate of 0.871 is the first success under "reference-motion-free" conditions, but still has a performance gap of 0.129 compared to the expert (1.000) (calculated as 1.000−0.871, approximately 12.9%), which the authors acknowledge as the most difficult transfer scenario.
- SFI improves the recovery success rate from 0.912 to 0.958, validating the necessity of actively injecting failure scenarios.
- MoE-2 outperforming MoE-3 indicates that more experts is not necessarily better; task overlap may confuse the gating network.

## Boundaries and Limitations

- **Limited perception range**: The narrow FOV camera (RealSense D435i) results in a limited perception horizon, preventing advance planning of distant terrain.
- **Imperfect sensor noise modeling**: The depth augmentation pipeline (Gaussian noise + filtering) cannot fully simulate systematic errors of real sensors (e.g., edge artifacts, reflection interference).
- **Expert performance upper bound**: Distillation relies on behavior cloning, so the policy cannot surpass expert demonstrations. Performance degrades significantly in edge cases not covered by experts (e.g., extreme terrain combinations).
- **Unverified generalization**: Soft ground, dynamic obstacles, and multi-robot platform transfer are not tested; no comparison with other general control frameworks (e.g., large model methods).
- **Unquantified computational resources**: Key engineering metrics such as training GPU model, total training time, and memory usage are not reported.

## Engineering Insights

1. **Reproduction priority**: First verify the CASS thresholds (b_t=1.1m) and terrain context mapping (I_t=1/2), as these are critical to distillation correctness. If head height estimation is biased, expert selection will be incorrect and the entire distillation process will fail.

2. **Most common pitfall**: The SAR ρ scheduling—the hysteresis interval (0.005/0.010) and decay step size (1e−4) need to be precisely matched. Too-fast ρ decay causes the student policy to prematurely explore autonomously and collapse; too-slow decay results in inefficient distillation. It is recommended to validate the ρ curve in a small-scale environment first.

3. **SFI termination condition**: The head height buffer variance threshold δ is not given a specific value, which is key to preventing OOD data corruption. It is recommended to set it empirically based on the robot's height (G1 approximately 1.3m) and gait cycle (approximately 0.5s), with sensitivity analysis.

4. **Depth augmentation pipeline**: The camera extrinsic randomization range (position ±0.05m, pitch ±10°) and FOV randomization (±10°) are critical to sim-to-real success. In real deployment, camera calibration must be performed first to ensure the randomization range covers actual installation errors.

5. **PD parameters must not be arbitrarily modified**: The K_p/K_d values in Table V come directly from reference [28] and are coupled with action scaling. Modifying any parameter changes the effective range of the action space and requires retraining all expert policies.

## 개요

X-Loco는 세 가지 특권 전문가 정책(직립 보행, 낙상 회복, 전신 협응)을 단일 시각 학생 정책으로 통합하는 협력 증류 프레임워크를 제안하며, Unitree G1 휴머노이드 로봇에서 참조 동작 없이 범용 운동 제어를 구현한다. 핵심 기여는 CASS 동적 전문가 선택, SAR 어닐링 혼합, SFI 무작위 낙상 주입을 통해 전문가 능력과 범용 정책 간의 격차를 해소하고, 시뮬레이션 및 실제 환경에서 교차 작업 일반화 능력을 검증한 것이다.

## 무엇을 바꾸었는가

기존 휴머노이드 운동 제어 연구는 오랫동안 "파편화" 상태에 머물러 있었다. 어떤 방법은 지형 횡단에 특화되고, 어떤 방법은 낙상 회복에 특화되었지만, "낙상 후 자율적으로 기어 일어나 복잡한 지형을 계속 횡단하는" 복합 시나리오를 동시에 처리할 수 있는 단일 프레임워크는 없었다. X-Loco가 실제로 바꾼 것은 "전문가 능력 통합"을 수작업 보상 설계의 한계에서 해방시킨 것이다. 더 이상 하나의 정책이 모든 기술을 학습하도록 강요하지 않고, 증류 메커니즘을 통해 범용 정책이 여러 전문가의 행동 패턴을 상속받도록 한다.

이 전환의 심층적 의미는 "범용성"과 "전문성" 사이의 긴장이 단일 정책의 용량 확장으로 해결될 수 없음을 인정하고, 대신 아키텍처 설계(MoE)와 훈련 스케줄링(SAR 어닐링)을 통해 조화를 모색한다는 점이다. BeyondMimic 등 참조 동작에 의존하는 방법과 달리, X-Loco는 참조 동작 없이 전신 협응 기술(예: 등반, 구르기)을 구현하여 범용 휴머노이드 제어가 "알려진 것을 모방"에서 "알려진 것을 조합"으로 패러다임 전환을 이루었음을 보여준다.

## 방법 분석

### 전문가 정책 훈련
- **π_l(직립 보행)**: 히스토리 인코더(10스텝 윈도우)와 고도 지도 인코더 사용, AMP 스타일 보상 가중치 3.0, 속도 추적 가중치 5.0, 생존 보상 2.0. 참조 동작은 LAFAN1 데이터셋 리타겟팅에서 가져옴.
- **π_r(낙상 회복)**: 지형 정보를 무시하고 히스토리 인코더와 액터만 사용, 앙와위/복와위 자세로 초기화하고 큰 관절 노이즈 주입. AMP 보상 가중치 최대 80.0, 각속도 패널티 25.0, 고관절 편차 패널티 -10.0, 대퇴 방향 보상 10.0.
- **π_w(전신 협응)**: 고도 지도 인코더(1.6m×1.0m 그리드, 0.1m 해상도) 사용, 박스 등반 및 구르기 등 전신 동작 추적, 보상 함수에 신체 위치/자세/속도 추적 및 앵커 제약 포함.

### 협력 증류 메커니즘
- **CASS 선택**: 머리 높이 b_t와 지형 컨텍스트 I_t를 기반으로 전문가 선택. b_t < 1.1m → π_r; b_t ≥ 1.1m 및 I_t=1(높은 플랫폼) → π_w; I_t=2(매달린 장애물) → π_w; 그 외 → π_l.
- **SAR 혼합**: a_env = b_t·a*_t + (1−b_t)·π_g(o_{g,t}), 여기서 b_t ~ Bernoulli(ρ). ρ는 초기 1.0, 증류 손실 < 0.005일 때 1e−4씩 감소, 손실 > 0.010일 때 감소 일시 중지(히스테리시스 구간).
- **SFI 주입**: 취약한 시나리오(고속 회전, 구르기)에서 무작위 외력을 가해 로봇이 회복 상태에 들어가도록 강제. 추가 종료 조건: 머리 높이 버퍼 분산이 임계값 δ 미만일 때 에피소드 종료, OOD 데이터 오염 방지.

### 학생 정책 아키텍처
- MoE 아키텍처: 게이팅 네트워크 + 3개 전문가(모두 3층 MLP [512, 256, 128])
- CNN 깊이 인코더: 64×64 깊이 맵 → 128차원 잠재 표현
- 히스토리 인코더: 10스텝 고유수용감각 시퀀스 → 128차원
- 증류 손실: ℒ_distill = MSE(π_g(o_{u,t}), a*_t)

### 심층 sim-to-real 브리징
- 다단계 파이프라인: 가산 가우시안 노이즈(σ=0.02m), 가우시안 필터(3×3 커널, σ=1.0), 카메라 외부 파라미터 무작위화(위치 ±0.05m, 피치 ±10°), FOV 무작위화(±10°)
- 실제 깊이 이미지에 홀 필링 및 가우시안 필터 적용

## 핵심 혁신

1. **CASS 동적 전문가 선택**: 정적 MoE 또는 고정 작업 전환과 달리, CASS는 로봇의 실시간 상태(머리 높이)와 지형 컨텍스트에 따라 안내 전문가를 동적으로 선택하여 증류 과정이 "보행→낙상→회복→계속 보행"의 연속적 상태 전환에 적응적으로 처리할 수 있게 한다. 낙상 회복을 범용 증류 프레임워크에 통합한 최초의 설계다.

2. **SAR 어닐링 스케줄링**: 히스테리시스 구간(τ_low=0.005, τ_high=0.010)을 통해 ρ 감소를 제어하여 증류 손실 변동으로 인한 훈련 불안정을 방지한다. 이 메커니즘은 본질적으로 "커리큘럼 학습"의 변형이다. 먼저 전문가를 완전히 따라가고, 점차 자율 탐색을 허용하지만, 전통적인 커리큘럼 학습보다 탐색-활용 균형을 더 정밀하게 제어한다.

3. **SFI 무작위 낙상 주입**: 훈련 중 수동적으로 실패를 기다리는 대신 적극적으로 "낙상-회복" 루프를 생성한다. 이는 범용 정책이 긴 호라이즌 작업에서 "한 번 낙상하면 영구 실패"라는 희소 보상 문제를 해결하여, 정책이 단순히 위험을 회피하는 대신 실패로부터 회복하는 법을 학습하게 한다.

## 실험 및 결과

| 방법 | Slope R_succ | Pit R_succ | Stairs R_succ | WBC R̄_succ | Recovery R_succ |
|------|-------------|------------|---------------|------------|----------------|
| MoRE | 0.992 | 0.844 | 0.926 | - | - |
| PPO | 0.823 | 0.793 | 0.781 | - | - |
| AHC | 0.968 | 0.403 | 0.278 | - | 1.000 |
| X-Loco | 0.982 | 0.878 | 0.958 | 0.871 | 1.000 |

**절제 실험**:
- Ours w/o CASS: 평균 R̄_succ = 0.783(Locomotion 0.903, WBC 0.446)
- Ours w/o MoE: 평균 R̄_succ = 0.749(Locomotion 0.692, WBC 0.561)
- MoE-3: 평균 R̄_succ = 0.779(Locomotion 0.628, WBC 0.709)
- MoE-2 (Ours): 평균 R̄_succ = 0.928(Locomotion 0.939, WBC 0.845)
- Ours w/o SFI: Recovery R_succ = 0.912 vs Ours 0.958

**핵심 해석**:
- X-Loco는 직립 보행 작업에서 평균 성공률 0.939로 PPO(0.799)와 AHC(0.550)를 능가하고 MoRE(0.921)와 경쟁하지만, MoRE는 WBC와 Recovery를 처리할 수 없다.
- WBC 작업 성공률 0.871은 "참조 동작 없음" 조건에서의 첫 성공이지만, 전문가(1.000)와 비교해 여전히 0.129의 성능 격차(1.000−0.871로 계산, 약 12.9%)가 있으며, 저자는 이를 가장 어려운 전이 시나리오로 인정한다.
- SFI는 회복 성공률을 0.912에서 0.958로 향상시켜 실패 시나리오의 적극적 주입 필요성을 검증했다.
- MoE-2가 MoE-3보다 우수함은 전문가 수가 많을수록 좋은 것이 아니며, 작업 중복이 게이팅 네트워크를 혼란시킬 수 있음을 시사한다.

## 경계 및 한계

- **인식 범위 제한**: 좁은 FOV 카메라(RealSense D435i)로 인해 제한된 인식 시간적 범위를 가지며, 원거리 지형을 사전에 계획할 수 없다.
- **센서 노이즈 모델링 불완전**: 깊이 증강 파이프라인(가우시안 노이즈+필터)은 실제 센서의 체계적 오류(예: 가장자리 아티팩트, 반사 간섭)를 완전히 모사할 수 없다.
- **전문가 성능 상한**: 증류는 행동 복제에 의존하므로 정책은 전문가 시연을 능가할 수 없다. 전문가가 커버하지 않는 엣지 케이스(예: 극단적 지형 조합)에서 성능이 현저히 저하된다.
- **검증되지 않은 일반화**: 연약한 지면, 동적 장애물, 다중 로봇 플랫폼 전이를 테스트하지 않았으며, 다른 범용 제어 프레임워크(예: 대규모 모델 방법)와 비교하지 않았다.
- **계산 자원 미정량화**: 훈련 GPU 모델, 총 훈련 시간, 메모리 사용량 등 핵심 엔지니어링 지표를 보고하지 않았다.

## 엔지니어링 시사점

1. **재현 우선순위**: 먼저 CASS의 임계값(b_t=1.1m)과 지형 컨텍스트 매핑(I_t=1/2)을 확인하라. 이는 증류 정확성의 핵심이다. 머리 높이 추정에 편향이 있으면 전문가 선택이 잘못되어 전체 증류 과정이 무효화된다.

2. **가장 함정에 빠지기 쉬운 지점**: SAR의 ρ 스케줄링 — 히스테리시스 구간(0.005/0.010)과 감소 스텝(1e−4)을 정확히 일치시켜야 한다. ρ가 너무 빨리 감소하면 학생 정책이 조기에 자율 탐색을 시작하여 붕괴하고, 너무 느리면 증류 효율이 낮아진다. 소규모 환경에서 먼저 ρ 곡선을 검증할 것을 권장한다.

3. **SFI의 종료 조건**: 머리 높이 버퍼 분산 임계값 δ는 구체적인 값이 제공되지 않았다. 이는 OOD 데이터 파괴를 방지하는 핵심이다. 로봇 키(G1 약 1.3m)와 보행 주기(약 0.5초)를 기준으로 경험적으로 설정하고 민감도 분석을 수행할 것을 권장한다.

4. **깊이 증강 파이프라인**: 카메라 외부 파라미터 무작위화 범위(위치 ±0.05m, 피치 ±10°)와 FOV 무작위화(±10°)는 sim-to-real 성공의 핵심이다. 실제 배포 시 반드시 먼저 카메라 캘리브레이션을 수행하여 무작위화 범위가 실제 설치 오차를 커버하는지 확인하라.

5. **PD 파라미터 임의 수정 금지**: Table V의 K_p/K_d 값은 문헌 [28]에서 직접 가져온 것이며, 동작 스케일링(Action Scale)과 결합되어 있다. 어느 하나의 파라미터를 수정하면 동작 공간의 유효 범위가 변경되므로 모든 전문가 정책을 다시 훈련해야 한다.
