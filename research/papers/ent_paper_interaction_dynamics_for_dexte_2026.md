---
$id: ent_paper_interaction_dynamics_for_dexte_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Interaction Dynamics for Dexterous Manipulation
  zh: Interaction Dynamics for Dexterous Manipulation
  ko: Interaction Dynamics for Dexterous Manipulation
summary:
  en: 'arXiv:2606.14606v2 Announce Type: replace Abstract: Dexterous manipulation is fundamentally a problem of interaction
    dynamics: the hand must track precise finger trajectories, regulate the contact force exchanged with grasped objects,
    respect actuation and safety limits, and remain predictable when contact persists -- objectives in tension for any fixed-gain
    controller. A sustained contact torque $\tau_{\text{ext}}$ through a joint stiffness $K_d$ produces the structural bias
    $e_\infty=\tau_{\text{ext}}/K_d$, so stiffening for accuracy sacrifices contact safety while softening yields by design.
    We make these interaction dynamics explicit and actuator-agnostic through a constant-$A_d$ double-integrator backbone,
    instantiating the offset-free architecture established for physical human-robot interaction (pHRI) and preserving its
    modeling assumptions on the reduced residual dynamics. An algebraic feedforward reduces the tendon transmission -- hydraulic,
    cable, pneumatic, twisted-string, or series-elastic -- to a constant-coefficient double integrator, so the QP cost inverse
    is precomputed offline and a 10-step receding-horizon QP runs at 500\,Hz under contact-force (ISO/TS 15066), actuation,
    and jerk constraints. An encoder-only augmented-Kalman disturbance state drives steady-state error to zero under constant
    contact loads in the nominal detectable case. In simulation, a hydraulically actuated finger -- the worked example, adding
    pressure and cavitation constraints -- attains 0.6\,mrad RMS, 0.1\,mrad steady-state, and 7.3\,mrad peak deflection under
    1.5\,Nm contact: 153$\times$, 1500$\times$, and 21$\times$ better than classical impedance. The realized first-move stiffness
    (18$\to$323\,Nm/rad with update rate) is independently verified, and the architecture scales to a 16-DOF LEAP Hand MuJoCo
    model, recovering from 2.5\,N grasp disturbances within 0.7\,s.'
  zh: 本文提出一种基于恒定$A_d$双积分器骨架的灵巧操作交互动力学框架，由作者团队开发。核心贡献在于将物理人机交互（pHRI）中的无偏架构推广至灵巧操作，通过代数前馈将多种肌腱传动统一为常系数双积分器，并实现500 Hz的10步滚动时域QP求解。在液压手指仿真中，该方法在1.5
    Nm接触下达到0.6 mrad RMS误差，比经典阻抗控制提升153倍。
  ko: 'arXiv:2606.14606v2 Announce Type: replace Abstract: Dexterous manipulation is fundamentally a problem of interaction
    dynamics: the hand must track precise finger trajectories, regulate the contact force exchanged with grasped objects,
    respect actuation and safety limits, and remain predictable when contact persists -- objectives in tension for any fixed-gain
    controller. A sustained contact torque $\tau_{\text{ext}}$ through a joint stiffness $K_d$ produces the structural bias
    $e_\infty=\tau_{\text{ext}}/K_d$, so stiffening for accuracy sacrifices contact safety while softening yields by design.
    We make these interaction dynamics explicit and actuator-agnostic through a constant-$A_d$ double-integrator backbone,
    instantiating the offset-free architecture established for physical human-robot interaction (pHRI) and preserving its
    modeling assumptions on the reduced residual dynamics. An algebraic feedforward reduces the tendon transmission -- hydraulic,
    cable, pneumatic, twisted-string, or series-elastic -- to a constant-coefficient double integrator, so the QP cost inverse
    is precomputed offline and a 10-step receding-horizon QP runs at 500\,Hz under contact-force (ISO/TS 15066), actuation,
    and jerk constraints. An encoder-only augmented-Kalman disturbance state drives steady-state error to zero under constant
    contact loads in the nominal detectable case. In simulation, a hydraulically actuated finger -- the worked example, adding
    pressure and cavitation constraints -- attains 0.6\,mrad RMS, 0.1\,mrad steady-state, and 7.3\,mrad peak deflection under
    1.5\,Nm contact: 153$\times$, 1500$\times$, and 21$\times$ better than classical impedance. The realized first-move stiffness
    (18$\to$323\,Nm/rad with update rate) is independently verified, and the architecture scales to a 16-DOF LEAP Hand MuJoCo
    model, recovering from 2.5\,N grasp disturbances within 0.7\,s.'
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
- interaction_dynamics_for_dexte
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.14606v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Interaction Dynamics for Dexterous Manipulation (arXiv)
  url: https://arxiv.org/abs/2606.14606
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
该研究将灵巧操作重新定义为交互动力学问题，指出固定增益控制器在精度与安全性之间存在根本矛盾。作者通过构建恒定$A_d$双积分器骨架，将pHRI中的无偏架构适配到灵巧操作场景，并保持其对简化残差动力学的建模假设。代数前馈设计将液压、缆绳、气动等不同肌腱传动统一为常系数双积分器，使得QP代价矩阵可离线预计算，在线仅需运行10步滚动时域QP（500 Hz）。编码器仅增强卡尔曼扰动状态估计器在可检测条件下实现稳态零误差。仿真验证中，液压手指在1.5 Nm接触下达到0.6 mrad RMS误差，刚度从18 Nm/rad动态调节至323 Nm/rad，并成功扩展到16自由度LEAP Hand MuJoCo模型。

## 核心内容
### 核心问题与架构设计
- 灵巧操作面临精度与安全性的根本矛盾：持续接触力矩$\tau_{\text{ext}}$通过关节刚度$K_d$产生结构偏差$e_\infty=\tau_{\text{ext}}/K_d$，增大刚度提升精度但牺牲接触安全性。
- 提出恒定$A_d$双积分器骨架，将交互动力学显式化且与执行器无关，继承pHRI中的无偏架构并保持其对简化残差动力学的建模假设。

### 传动统一与优化求解
- 代数前馈将液压、缆绳、气动、扭绳或串联弹性等肌腱传动统一为常系数双积分器，使QP代价矩阵可离线预计算。
- 在线运行10步滚动时域QP，频率500 Hz，同时满足接触力（ISO/TS 15066标准）、执行器约束和加加速度约束。

### 扰动估计与稳态性能
- 仅使用编码器的增强卡尔曼扰动状态估计器，在名义可检测条件下实现恒定接触负载下的稳态零误差。

### 仿真验证结果
- 液压手指（工作示例，额外添加压力和空化约束）在1.5 Nm接触下达到：
  - RMS误差：0.6 mrad
  - 稳态误差：0.1 mrad
  - 峰值偏差：7.3 mrad
  - 相比经典阻抗控制分别提升153倍、1500倍和21倍
- 首次移动刚度从18 Nm/rad动态调节至323 Nm/rad（随更新率变化），经独立验证。
- 架构成功扩展至16自由度LEAP Hand MuJoCo模型，在2.5 N抓取扰动下0.7秒内恢复。

## Overview
Dexterous manipulation is fundamentally a problem of interaction dynamics: the hand must track precise finger trajectories, regulate the contact force exchanged with grasped objects, respect actuation and safety limits, and remain predictable when contact persists -- objectives in tension for any fixed-gain controller. A sustained contact torque $τ_{\text{ext}}$ through a joint stiffness $K_d$ produces the structural bias $e_\infty=τ_{\text{ext}}/K_d$, so stiffening for accuracy sacrifices contact safety while softening yields by design. We make these interaction dynamics explicit and actuator-agnostic through a constant-$A_d$ double-integrator backbone, instantiating the offset-free architecture established for physical human-robot interaction (pHRI) and preserving its modeling assumptions on the reduced residual dynamics. An algebraic feedforward reduces the tendon transmission -- hydraulic, cable, pneumatic, twisted-string, or series-elastic -- to a constant-coefficient double integrator, so the QP cost inverse is precomputed offline and a 10-step receding-horizon QP runs at 500\,Hz under contact-force (ISO/TS 15066), actuation, and jerk constraints. An encoder-only augmented-Kalman disturbance state drives steady-state error to zero under constant contact loads in the nominal detectable case. In simulation, a hydraulically actuated finger -- the worked example, adding pressure and cavitation constraints -- attains 0.6\,mrad RMS, 0.1\,mrad steady-state, and 7.3\,mrad peak deflection under 1.5\,Nm contact: 153$\times$, 1500$\times$, and 21$\times$ better than classical impedance. The realized first-move stiffness (18$\to$323\,Nm/rad with update rate) is independently verified, and the architecture scales to a 16-DOF LEAP Hand MuJoCo model, recovering from 2.5\,N grasp disturbances within 0.7\,s.

## 개요
정밀 조작은 근본적으로 상호작용 동역학의 문제입니다. 손은 정확한 손가락 궤적을 추적하고, 잡은 물체와 교환되는 접촉력을 조절하며, 작동 및 안전 한계를 준수하고, 접촉이 지속될 때 예측 가능성을 유지해야 합니다. 이는 고정 이득 제어기에게는 상충되는 목표들입니다. 관절 강성 $K_d$를 통한 지속적인 접촉 토크 $τ_{\text{ext}}$는 구조적 편향 $e_\infty=τ_{\text{ext}}/K_d$을 발생시키므로, 정확성을 위해 강성을 높이면 접촉 안전성이 희생되고, 반대로 강성을 낮추면 설계상 오차가 발생합니다. 우리는 이러한 상호작용 동역학을 명시적이고 액추에이터에 구애받지 않도록 상수-$A_d$ 이중 적분기 백본을 통해 구현하며, 물리적 인간-로봇 상호작용(pHRI)을 위해 확립된 오프셋 없는 아키텍처를 인스턴스화하고, 축소된 잔류 동역학에 대한 모델링 가정을 유지합니다. 대수적 피드포워드는 힘줄 전달(유압, 케이블, 공압, 꼬임 끈, 또는 직렬 탄성)을 상수 계수 이중 적분기로 축소하여, QP 비용 역행렬을 오프라인에서 미리 계산하고, 접촉력(ISO/TS 15066), 작동, 및 저크 제약 조건 하에서 10단계 후퇴 수평선 QP를 500Hz로 실행합니다. 엔코더 전용 증강-칼만 외란 상태는 공칭 검출 가능한 경우에서 일정한 접촉 하중 하에 정상 상태 오차를 0으로 만듭니다. 시뮬레이션에서, 유압식으로 작동되는 손가락(작업 예시로, 압력 및 캐비테이션 제약 조건 추가)은 1.5Nm 접촉 하에서 0.6mrad RMS, 0.1mrad 정상 상태, 7.3mrad 최대 편향을 달성하여, 고전적 임피던스보다 각각 153배, 1500배, 21배 더 우수합니다. 실현된 첫 움직임 강성(업데이트 속도에 따라 18→323Nm/rad)은 독립적으로 검증되었으며, 이 아키텍처는 16-DOF LEAP Hand MuJoCo 모델로 확장되어 2.5N 파지 외란으로부터 0.7초 이내에 회복합니다.

## 핵심 내용
정밀 조작은 근본적으로 상호작용 동역학의 문제입니다. 손은 정확한 손가락 궤적을 추적하고, 잡은 물체와 교환되는 접촉력을 조절하며, 작동 및 안전 한계를 준수하고, 접촉이 지속될 때 예측 가능성을 유지해야 합니다. 이는 고정 이득 제어기에게는 상충되는 목표들입니다. 관절 강성 $K_d$를 통한 지속적인 접촉 토크 $τ_{\text{ext}}$는 구조적 편향 $e_\infty=τ_{\text{ext}}/K_d$을 발생시키므로, 정확성을 위해 강성을 높이면 접촉 안전성이 희생되고, 반대로 강성을 낮추면 설계상 오차가 발생합니다. 우리는 이러한 상호작용 동역학을 명시적이고 액추에이터에 구애받지 않도록 상수-$A_d$ 이중 적분기 백본을 통해 구현하며, 물리적 인간-로봇 상호작용(pHRI)을 위해 확립된 오프셋 없는 아키텍처를 인스턴스화하고, 축소된 잔류 동역학에 대한 모델링 가정을 유지합니다. 대수적 피드포워드는 힘줄 전달(유압, 케이블, 공압, 꼬임 끈, 또는 직렬 탄성)을 상수 계수 이중 적분기로 축소하여, QP 비용 역행렬을 오프라인에서 미리 계산하고, 접촉력(ISO/TS 15066), 작동, 및 저크 제약 조건 하에서 10단계 후퇴 수평선 QP를 500Hz로 실행합니다. 엔코더 전용 증강-칼만 외란 상태는 공칭 검출 가능한 경우에서 일정한 접촉 하중 하에 정상 상태 오차를 0으로 만듭니다. 시뮬레이션에서, 유압식으로 작동되는 손가락(작업 예시로, 압력 및 캐비테이션 제약 조건 추가)은 1.5Nm 접촉 하에서 0.6mrad RMS, 0.1mrad 정상 상태, 7.3mrad 최대 편향을 달성하여, 고전적 임피던스보다 각각 153배, 1500배, 21배 더 우수합니다. 실현된 첫 움직임 강성(업데이트 속도에 따라 18→323Nm/rad)은 독립적으로 검증되었으며, 이 아키텍처는 16-DOF LEAP Hand MuJoCo 모델로 확장되어 2.5N 파지 외란으로부터 0.7초 이내에 회복합니다.

## 参考
- http://arxiv.org/abs/2606.14606v2
