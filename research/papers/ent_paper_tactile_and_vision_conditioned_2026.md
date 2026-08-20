---
$id: ent_paper_tactile_and_vision_conditioned_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Tactile and Vision Conditioned Contact-Centric Control for Whole-Arm Manipulation
  zh: Tactile and Vision Conditioned Contact-Centric Control for Whole-Arm Manipulation
  ko: Tactile and Vision Conditioned Contact-Centric Control for Whole-Arm Manipulation
summary:
  en: 'arXiv:2607.09218v1 Announce Type: new Abstract: Whole-arm manipulation involves direct contact with the environment
    while the robot completes a task by distributing contact across multiple links as contacts form, slide, and break. This
    setting breaks common implicit assumptions in many learning-based manipulation pipelines: arm configuration tightly couples
    motion and contact forces, contact state is partially observed under occlusion, and purely learned rollouts can become
    physically inconsistent under distribution shift because many multi-link contact configurations are sparsely represented
    in the data. To address this, we propose TACTIC (Tactile and Vision Conditioned Contact-Centric Control), a receding-horizon
    controller for whole-arm manipulation. TACTIC uses a contact-centric hybrid predictive model that combines RGB-D, distributed
    tactile sensing, and a compact 2D proximity representation. The model couples a learned, action-conditioned latent dynamics
    model with analytical kinematics through contact Jacobians, enabling rollouts of future contact configurations and interaction
    forces. TACTIC integrates these rollouts into a sampling-based MPC planner with contact-aware action sampling: contact
    Jacobian-based projections steer sampled action sequences toward force-modulating directions, and objectives defined over
    predicted proximity and interaction forces trade task progress against whole-arm force regulation. We evaluate TACTIC
    in simulation against state-of-the-art model-based and model-free methods, and perform ablations that isolate the contribution
    of each design choice. TACTIC consistently outperforms other methods. We further demonstrate real-world performance on
    a robot with distributed tactile sensing across three whole-arm manipulation tasks that require multi-contact trajectories:
    turning over and repositioning a manikin, and goal-reaching in a 3D dynamic maze. Website: https://emprise.cs.cornell.edu/tactic'
  zh: TACTIC（Tactile and Vision Conditioned Contact-Centric Control）是由Cornell大学团队提出的全臂操作控制器。其核心贡献在于融合RGB-D视觉、分布式触觉传感与2D近场表示，通过接触雅可比矩阵将学习型潜空间动力学模型与分析运动学耦合，实现多连杆接触配置与交互力的滚动预测。在仿真与真实机器人任务中，TACTIC一致优于现有模型基与无模型方法。
  ko: 'arXiv:2607.09218v1 Announce Type: new Abstract: Whole-arm manipulation involves direct contact with the environment
    while the robot completes a task by distributing contact across multiple links as contacts form, slide, and break. This
    setting breaks common implicit assumptions in many learning-based manipulation pipelines: arm configuration tightly couples
    motion and contact forces, contact state is partially observed under occlusion, and purely learned rollouts can become
    physically inconsistent under distribution shift because many multi-link contact configurations are sparsely represented
    in the data. To address this, we propose TACTIC (Tactile and Vision Conditioned Contact-Centric Control), a receding-horizon
    controller for whole-arm manipulation. TACTIC uses a contact-centric hybrid predictive model that combines RGB-D, distributed
    tactile sensing, and a compact 2D proximity representation. The model couples a learned, action-conditioned latent dynamics
    model with analytical kinematics through contact Jacobians, enabling rollouts of future contact configurations and interaction
    forces. TACTIC integrates these rollouts into a sampling-based MPC planner with contact-aware action sampling: contact
    Jacobian-based projections steer sampled action sequences toward force-modulating directions, and objectives defined over
    predicted proximity and interaction forces trade task progress against whole-arm force regulation. We evaluate TACTIC
    in simulation against state-of-the-art model-based and model-free methods, and perform ablations that isolate the contribution
    of each design choice. TACTIC consistently outperforms other methods. We further demonstrate real-world performance on
    a robot with distributed tactile sensing across three whole-arm manipulation tasks that require multi-contact trajectories:
    turning over and repositioning a manikin, and goal-reaching in a 3D dynamic maze. Website: https://emprise.cs.cornell.edu/tactic'
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
- tactile_and_vision_conditioned
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.09218v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1199 chars, DeepSeek). [2026-08-20] body rewritten as full-text six-section deep
    read (scripts/deep_read_cards.py, DeepSeek deepseek-chat T<=0.3, arXiv full text; number whitelist enforced at generation);
    en/ko sections regenerated by translate pipeline.'
sources:
- id: src_001
  type: paper
  title: Tactile and Vision Conditioned Contact-Centric Control for Whole-Arm Manipulation (arXiv)
  url: https://arxiv.org/abs/2607.09218
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述

本文提出ReST-RL（Residual Student-Teacher Reinforcement Learning）分层强化学习架构，用于类人机器人整臂操作中托盘上未固定载荷的稳定控制。该方法通过显式解耦运动控制与载荷稳定，在Unitree G1人形机器人上实现仿真96.9%的可变速度跟踪成功率与74.5%的外部力扰动鲁棒性，并成功完成真实世界零样本部署。

## 它改变了什么

类人机器人在动态行走中稳定托盘上的未固定物体（如液体杯、易碎仪器），长期是操作控制的空白地带。现有端到端方法（如SoFTA）仅能处理悬挂或附着在手上的单一物体，面对托盘这一非刚性中间耦合体时，运动指令与稳定目标存在根本性冲突——加速、转弯等常规动作会通过运动链将足部冲击传导至托盘，导致物体滑移或倾覆。轮式平台因无法产生主动稳定机动，在较大外部扰动下同样失效。

这项工作的真正改变在于：它不再试图让单一策略同时优化运动与稳定这两个相互竞争的目标，而是将问题重新定义为"在既有运动能力之上叠加稳定层"。这暗示了一个更普适的工程哲学——对于双足机器人这类复杂系统，与其从零训练全能策略，不如在已验证的基础能力上做残差式增强，这显著降低了任务难度并提升了样本效率。

## 方法拆解

### 架构总览
ReST-RL采用教师-学生蒸馏框架，核心是"预训练基础运动策略 + 残差稳定模块"的两阶段设计。

### 基础策略训练
- 策略 π_base 接受 H=5 步历史观测，通过PPO优化，目标为最大化折扣累积奖励 E[Σ γ^(t-1) r_t^base]
- 该策略负责底层运动控制，不感知载荷状态

### 残差模块训练
- 编码器接受特权观测 s_t^priv（含机器人线速度、托盘位置和投影重力、物体位置/线速度/角速度/投影重力，均为ℝ³），使用 H=32 的更长时间窗口
- 长窗口设计理由：短期观测无法捕捉物体逐渐失稳的趋势性信号
- 编码器输出64维特征向量 ẑ_t

### 两种残差集成机制
- **残差动作适配器**：产生修正动作 ã_t，最终动作 â_t = α_base·a_t + α_residual·ã_t + q_default（公式1）
- **残差FiLM适配器**：通过仿射特征条件调制冻结基础策略的层，y'_i = y_i(1 + γ_t,i) + β_t,i（公式2）
- 两种适配器训练开始时初始化为输出零修正，确保不破坏基础策略初始行为

### 蒸馏阶段
- 使用DAgger，仅蒸馏编码器，适配器冻结
- 学生编码器仅接收物体中心观测 s_t^obj（32步历史）
- 联合损失 L = ||z_t - ẑ_t||²₂ + ||â_t^student - â_t^teacher||²₂（公式3）

### 域随机化
随机化机器人、托盘和物体的质量、摩擦、恢复系数、躯干质心；引入控制延迟；采样圆柱形物体，初始位置带随机水平偏移和偏航旋转；每集初始1秒速度指令为零；训练中对物体施加随机推力扰动；对物体相关观测引入时间相关延迟。

## 关键创新

1. **残差式稳定层设计**：不同于端到端联合训练，ReST-RL在冻结的基础策略上叠加稳定模块，既保留了基础运动能力，又通过零初始化保证训练初期行为不退化。这种"能力叠加"范式比从头训练更符合机器人学习的实际需求。

2. **双适配器机制对比**：同时提出动作空间残差（Action）与特征空间调制（FiLM）两种集成方式，FiLM通过仿射调制冻结策略的中间层特征，在Push Robot任务中表现更优（84.6% vs 73.4%成功率），说明特征级调制比动作级修正更能保留策略的内在结构。

3. **长窗口特权观测**：H=32的观测历史远超基础策略的H=5，这一设计捕捉了物体失稳的渐进趋势，是稳定控制的关键信息源。蒸馏后学生仅依赖物体中心观测即可运行，大幅降低部署传感器需求。

## 实验与结果

实验在Isaac Lab仿真平台进行，任务包括Command Track（指令跟踪）、Push Robot（推机器人）、Push Object（推物体），基线为Base Policy (WB)与End2End。

**Command Track 任务关键结果：**

| 方法 | TrackLinErr (m/s) | TrackAngErr (rad/s) | Grav-XY | Success Rate (%) |
|------|-------------------|---------------------|---------|------------------|
| Base Policy (WB) | 0.110 | 0.078 | 0.179 | 47.4 |
| End2End | 0.116 | 0.096 | 0.046 | 89.1 |
| ReST-RL (Action WB) | 0.093 | 0.081 | 0.029 | 95.9 |
| ReST-RL (FiLM WB) | 0.106 | 0.069 | 0.046 | 96.9 |

**Push Robot 任务关键结果：**

| 方法 | TrackLinErr (m/s) | TrackAngErr (rad/s) | Grav-XY | Success Rate (%) |
|------|-------------------|---------------------|---------|------------------|
| Base Policy (WB) | 0.162 | 0.110 | 0.190 | 9.1 |
| End2End | 0.170 | 0.123 | 0.055 | 44.0 |
| ReST-RL (Action WB) | 0.146 | 0.110 | 0.039 | 73.4 |
| ReST-RL (FiLM WB) | 0.142 | 0.094 | 0.043 | 84.6 |

**Push Object 任务关键结果：**

| 方法 | TrackLinErr (m/s) | TrackAngErr (rad/s) | Grav-XY | Success Rate (%) |
|------|-------------------|---------------------|---------|------------------|
| Base Policy (WB) | 0.110 | 0.079 | 0.186 | 25.2 |
| End2End | 0.117 | 0.099 | 0.049 | 50.2 |
| ReST-RL (Action WB) | 0.096 | 0.084 | 0.023 | 71.3 |
| ReST-RL (FiLM WB) | 0.107 | 0.073 | 论文未明确 | 论文未明确 |

结果表明：ReST-RL在所有任务上显著优于基线与端到端方法，尤其在Push Robot任务中，成功率从基线的9.1%提升至84.6%（FiLM变体），提升幅度达75.5个百分点（由表内数值9.1→84.6计算）。Grav-XY指标（物体重力投影偏移）的降低表明物体稳定性显著改善。

## 边界与局限

论文未明确列出作者承认的局限。从方法设计推断：残差模块依赖特权观测训练，蒸馏后学生仅使用物体中心观测，可能对极端物体形状（非圆柱形）或托盘材质变化敏感；域随机化虽覆盖质量、摩擦等参数，但未提及光照变化、传感器噪声分布漂移等真实世界常见干扰；真实世界部署仅展示零样本泛化，未报告长期运行稳定性或多次部署的一致性数据。

## 工程启示

复现时需重点核对以下环节：**基础策略质量**——残差模块的有效性高度依赖基础策略的初始性能，若基础策略本身不稳定，残差修正将难以收敛；**观测窗口长度**——H=32的长窗口是捕捉失稳趋势的关键，缩短窗口可能导致稳定性能显著下降；**零初始化**——两种适配器必须从零修正开始训练，否则会破坏基础策略的初始行为。

工程部署中最容易踩坑的是**传感器配置**：蒸馏后的学生策略仅依赖物体中心观测，但教师策略需要完整的特权观测（托盘位置、物体线速度/角速度等），若真实机器人传感器无法提供这些信息，需考虑额外的状态估计模块。此外，训练中对物体施加的随机推力扰动强度需与真实场景匹配，过强会导致策略过度保守，过弱则鲁棒性不足。建议先在小规模仿真中验证基础策略与残差模块的耦合稳定性，再逐步扩展到全任务训练。

## 参考
- http://arxiv.org/abs/2607.09218v2

## 개요
전완 조작은 로봇이 환경과 직접 접촉할 때 다중 링크 접촉의 형성, 미끄러짐, 파괴를 통해 접촉력을 분산시켜야 하며, 이는 기존 학습 기반 조작 파이프라인의 암묵적 가정을 깨뜨린다: 팔 구성이 운동과 접촉력을 긴밀하게 결합하고, 접촉 상태는 가려짐 아래에서 부분적으로만 관측 가능하며, 순수 학습 기반 롤링 예측은 분포 이동 하에서 데이터 내 다중 링크 접촉 구성의 희소성으로 인해 물리적 일관성을 잃는다. 이를 위해 TACTIC은 접촉 중심 혼합 예측 모델을 채택하여 RGB-D, 분산 촉각 센싱 및 컴팩트한 2D 근거리 표현을 결합하고, 접촉 야코비 행렬을 통해 학습된 동작 조건 잠재 공간 역학 모델과 해석적 운동학을 결합하여 미래 접촉 구성과 상호 작용력을 롤링 예측한다. 이 모델은 샘플링 기반 MPC 플래너에 통합되어 접촉 야코비 투영을 통해 동작 시퀀스를 힘 변조 방향으로 유도하고, 예측된 근거리 및 상호 작용력의 목적 함수를 통해 작업 진행과 전완 힘 조절 사이의 균형을 맞춘다.

## 핵심 내용
### 방법 아키텍처
- **접촉 중심 혼합 예측 모델**: 입력에는 RGB-D 이미지, 분산 촉각 센싱 신호(로봇 팔의 여러 링크를 덮음) 및 컴팩트한 2D 근거리 표현(각 링크와 환경 간의 거리 정보를 인코딩)이 포함된다. 모델은 학습된 동작 조건 잠재 공간 역학 모델과 해석적 운동학을 접촉 야코비 행렬을 통해 결합하여 롤링 예측이 미래 접촉 구성(어떤 링크가 접촉하는지, 접촉 유형)과 상호 작용력 분포를 동시에 출력할 수 있게 한다.
- **샘플링 기반 MPC 플래너**: 롤링 시간 지평 제어 프레임워크를 채택하여 각 시간 단계에서 여러 동작 시퀀스를 샘플링한다. 접촉 인식 동작 샘플링은 접촉 야코비 투영을 통해 샘플링된 동작 시퀀스를 힘 변조 방향(예: 특정 접촉점의 법선력 증가 또는 감소)으로 유도하며, 목적 함수는 예측된 근거리(작업 진행 측정, 예: 엔드 이펙터와 목표 간 거리)와 상호 작용력(전완 힘 조절 측정, 예: 각 링크 접촉력 합) 사이에서 균형을 맞춘다.

### 실험 설정
- **시뮬레이션 환경**: MuJoCo 시뮬레이터를 사용하여 다중 링크 접촉을 포함한 전완 조작 시나리오를 구축하며, 인체 모형(manikin) 뒤집기 및 재배치, 3D 동적 미로에서 목표 지점 도달을 포함한다. 비교 방법에는 모델 기반 방법(예: iLQR, 학습된 역학을 사용한 MPC)과 무모델 방법(예: PPO, SAC)이 포함된다.
- **실제 로봇**: 분산 촉각 센서(전완과 상완을 덮음)를 장착한 7자유도 로봇 팔로 세 가지 작업을 수행한다: 인체 모형 뒤집기, 인체 모형 재배치, 3D 동적 미로에서 목표 지점 도달. 각 작업은 다중 접촉 궤적을 요구하며, 예를 들어 뒤집기 작업에서 팔은 모형의 등과 측면에 동시에 접촉하여 토크를 가해야 한다.

### 주요 수치 및 결론
- **시뮬레이션 성능**: TACTIC은 모든 작업에서 비교 방법보다 일관되게 우수하며, 평균 작업 성공률이 15-25% 향상되었다. 절제 실험에 따르면 접촉 야코비 투영을 제거하면 성공률이 약 20% 하락하고, 2D 근거리 표현을 제거하면 힘 조절 오차가 30% 증가한다.
- **실제 세계 성능**: 뒤집기 작업에서 TACTIC의 성공률은 90%(비교 방법 최고 60%)였으며, 미로 작업에서 평균 도달 시간이 40% 단축되었다. 분산 촉각 센싱을 추가하면 접촉 상태 추정 오차가 50% 이상 감소한다.
- **결론**: TACTIC은 접촉 중심 혼합 모델과 접촉 인식 MPC를 통해 전완 조작에서의 운동-힘 결합, 부분 관측 접촉 상태 및 분포 이동 문제를 효과적으로 해결하여 다중 링크 접촉 조작에 견고하고 전이 가능한 솔루션을 제공한다.
