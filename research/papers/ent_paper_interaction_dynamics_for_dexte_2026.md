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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.14606v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (944 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2606.14606v2

## 개요
이 연구는 정밀 조작을 상호작용 동역학 문제로 재정의하며, 고정 이득 제어기가 정밀도와 안전성 사이에 근본적인 모순을 지니고 있음을 지적한다. 저자들은 일정한 $A_d$ 이중 적분기 골격을 구축하여 pHRI의 불편향 아키텍처를 정밀 조작 시나리오에 적용하고, 단순화된 잔차 동역학에 대한 모델링 가정을 유지한다. 대수적 피드포워드 설계는 유압, 케이블, 공압 등 다양한 힘줄 구동을 상수 계수 이중 적분기로 통합하여 QP 비용 행렬을 오프라인으로 사전 계산할 수 있게 하며, 온라인에서는 10단계 롤링 호라이즌 QP(500 Hz)만 실행하면 된다. 엔코더만 사용하는 강화 칼만 외란 상태 추정기는 검출 가능 조건에서 정상 상태 오차를 0으로 달성한다. 시뮬레이션 검증에서 유압 손가락은 1.5 Nm 접촉 하중에서 0.6 mrad RMS 오차를 달성하고, 강성은 18 Nm/rad에서 323 Nm/rad로 동적으로 조정되며, 16자유도 LEAP Hand MuJoCo 모델로 성공적으로 확장되었다.

## 핵심 내용
### 핵심 문제와 아키텍처 설계
- 정밀 조작은 정밀도와 안전성의 근본적인 모순에 직면한다: 지속적인 접촉 토크 $\tau_{\text{ext}}$는 관절 강성 $K_d$를 통해 구조적 편차 $e_\infty=\tau_{\text{ext}}/K_d$를 생성하며, 강성을 높이면 정밀도가 향상되지만 접촉 안전성이 희생된다.
- 일정한 $A_d$ 이중 적분기 골격을 제안하여 상호작용 동역학을 명시적이고 액추에이터와 무관하게 만들고, pHRI의 불편향 아키텍처를 계승하며 단순화된 잔차 동역학에 대한 모델링 가정을 유지한다.

### 구동 통합과 최적화 솔루션
- 대수적 피드포워드는 유압, 케이블, 공압, 꼬임 케이블 또는 직렬 탄성과 같은 힘줄 구동을 상수 계수 이중 적분기로 통합하여 QP 비용 행렬을 오프라인으로 사전 계산할 수 있게 한다.
- 온라인에서는 10단계 롤링 호라이즌 QP를 500 Hz 주파수로 실행하며, 접촉력(ISO/TS 15066 표준), 액추에이터 제약 및 가속도 제약을 동시에 충족한다.

### 외란 추정과 정상 상태 성능
- 엔코더만 사용하는 강화 칼만 외란 상태 추정기는 명목상 검출 가능 조건에서 일정한 접촉 하중 하에 정상 상태 오차를 0으로 달성한다.

### 시뮬레이션 검증 결과
- 유압 손가락(작동 예시, 추가 압력 및 공동화 제약 포함)은 1.5 Nm 접촉 하중에서 다음을 달성:
  - RMS 오차: 0.6 mrad
  - 정상 상태 오차: 0.1 mrad
  - 최대 편차: 7.3 mrad
  - 기존 임피던스 제어 대비 각각 153배, 1500배, 21배 향상
- 이동 강성은 18 Nm/rad에서 323 Nm/rad로 동적으로 조정되며(업데이트율에 따라 변화), 독립적으로 검증되었다.
- 아키텍처는 16자유도 LEAP Hand MuJoCo 모델로 성공적으로 확장되었으며, 2.5 N 파지 외란 하에서 0.7초 내에 복구된다.
