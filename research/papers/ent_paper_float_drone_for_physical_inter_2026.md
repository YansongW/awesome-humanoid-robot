---
$id: ent_paper_float_drone_for_physical_inter_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FLOAT Drone for Physical Interaction: Lateral Airflow Reduction, Wrench Modeling, and Adaptive Control'
  zh: 'FLOAT Drone for Physical Interaction: Lateral Airflow Reduction, Wrench Modeling, and Adaptive Control'
  ko: 'FLOAT Drone for Physical Interaction: Lateral Airflow Reduction, Wrench Modeling, and Adaptive Control'
summary:
  en: 'arXiv:2607.04260v1 Announce Type: new Abstract: Aerial physical interaction represents a promising direction for next-generation
    unmanned aerial vehicles (UAVs), but it requires an aerial platform that can exert contact forces while maintaining stable
    flight. For close-proximity tasks, this translates into three coupled design requirements: multidimensional wrench generation
    for stable contact, compactness for maneuverability and safety in confined spaces, and reduced lateral airflow toward
    the target when generating horizontal force. This article presents FLOAT Drone, a fully actuated coaxial UAV with servo-driven
    control surfaces for close-proximity physical interaction. The coaxial dual-rotor layout provides a compact propulsion
    layout, while the control surfaces, immersed in the rotor downwash, generate lateral forces and moments for 6-DoF wrench
    generation. A force-matched computational fluid dynamics (CFD) comparison with a tilted-rotor alternative quantifies the
    reduction in target-facing lateral airflow. To account for nonlinear rotor--control-surface coupling in the rotor wake,
    a high-fidelity polynomial aerodynamic wrench model is identified from precision force measurements and embedded in a
    constrained nonlinear allocator for real-time wrench tracking. Comparative flight and interaction experiments show that
    the proposed framework improves control accuracy over linear allocation baselines, rejects ground-effect and payload disturbances,
    and enables close-proximity drawer push--pull manipulation through a $2~\mathrm{cm}$ handle clearance.'
  zh: FLOAT Drone 是一种用于近距离物理交互的全驱动同轴无人机，由研究团队提出，通过伺服驱动控制面实现六自由度力与力矩生成。其核心贡献在于：采用同轴双旋翼布局减小侧向气流对目标的影响，并基于高保真多项式气动模型实现实时力跟踪，在抽屉推拉实验中仅需
    2 cm 手柄间隙即可完成操作。
  ko: 'arXiv:2607.04260v1 Announce Type: new Abstract: Aerial physical interaction represents a promising direction for next-generation
    unmanned aerial vehicles (UAVs), but it requires an aerial platform that can exert contact forces while maintaining stable
    flight. For close-proximity tasks, this translates into three coupled design requirements: multidimensional wrench generation
    for stable contact, compactness for maneuverability and safety in confined spaces, and reduced lateral airflow toward
    the target when generating horizontal force. This article presents FLOAT Drone, a fully actuated coaxial UAV with servo-driven
    control surfaces for close-proximity physical interaction. The coaxial dual-rotor layout provides a compact propulsion
    layout, while the control surfaces, immersed in the rotor downwash, generate lateral forces and moments for 6-DoF wrench
    generation. A force-matched computational fluid dynamics (CFD) comparison with a tilted-rotor alternative quantifies the
    reduction in target-facing lateral airflow. To account for nonlinear rotor--control-surface coupling in the rotor wake,
    a high-fidelity polynomial aerodynamic wrench model is identified from precision force measurements and embedded in a
    constrained nonlinear allocator for real-time wrench tracking. Comparative flight and interaction experiments show that
    the proposed framework improves control accuracy over linear allocation baselines, rejects ground-effect and payload disturbances,
    and enables close-proximity drawer push--pull manipulation through a $2~\mathrm{cm}$ handle clearance.'
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
- float_drone_for_physical_inter
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04260v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'FLOAT Drone for Physical Interaction: Lateral Airflow Reduction, Wrench Modeling, and Adaptive Control (arXiv)'
  url: https://arxiv.org/abs/2607.04260
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
该无人机针对空中物理交互中的三个关键需求设计：多维力生成、紧凑性以及减少水平力产生时对目标的侧向气流。同轴双旋翼布局提供了紧凑的动力结构，而浸没在旋翼下洗流中的控制面则产生侧向力和力矩，实现六自由度力控制。通过力匹配计算流体动力学（CFD）对比，量化了与倾斜旋翼方案相比侧向气流的减少。为解决旋翼与控制面之间的非线性耦合，研究团队从精密力测量中识别出高保真多项式气动模型，并将其嵌入约束非线性分配器中，用于实时力跟踪。实验表明，该框架在控制精度上优于线性分配基线，并能抑制地面效应和负载扰动。

## 核心内容
### 方法与架构
- **平台设计**：FLOAT Drone 采用同轴双旋翼布局，旋翼直径较小，整体结构紧凑，适合在受限空间中机动。控制面（伺服驱动）位于旋翼下洗流中，通过偏转产生侧向力和力矩，实现六自由度力生成。
- **气动模型**：为应对旋翼下洗流与控制面之间的非线性耦合，研究团队使用精密力传感器采集数据，识别出一个高保真多项式气动模型。该模型被嵌入约束非线性分配器中，用于实时力跟踪，替代了传统的线性分配方法。

### 实验设置与关键数字
- **CFD 对比**：通过力匹配计算流体动力学（CFD）模拟，将 FLOAT Drone 与倾斜旋翼方案对比，量化了目标方向侧向气流的减少程度。
- **飞行与交互实验**：比较实验显示，所提框架在控制精度上优于线性分配基线，能够有效抑制地面效应和负载扰动。在近距离抽屉推拉操作中，无人机仅需 2 cm 的手柄间隙即可完成推拉任务。

### 结论
FLOAT Drone 通过紧凑的同轴双旋翼设计和基于高保真气动模型的非线性控制，实现了稳定的近距离物理交互。实验验证了其在控制精度、抗干扰能力以及狭小空间操作中的优势，为下一代无人机在接触式任务中的应用提供了可行方案。

## Overview
Aerial physical interaction represents a promising direction for next-generation unmanned aerial vehicles (UAVs), but it requires an aerial platform that can exert contact forces while maintaining stable flight. For close-proximity tasks, this translates into three coupled design requirements: multidimensional wrench generation for stable contact, compactness for maneuverability and safety in confined spaces, and reduced lateral airflow toward the target when generating horizontal force. This article presents FLOAT Drone, a fully actuated coaxial UAV with servo-driven control surfaces for close-proximity physical interaction. The coaxial dual-rotor layout provides a compact propulsion layout, while the control surfaces, immersed in the rotor downwash, generate lateral forces and moments for 6-DoF wrench generation. A force-matched computational fluid dynamics (CFD) comparison with a tilted-rotor alternative quantifies the reduction in target-facing lateral airflow. To account for nonlinear rotor--control-surface coupling in the rotor wake, a high-fidelity polynomial aerodynamic wrench model is identified from precision force measurements and embedded in a constrained nonlinear allocator for real-time wrench tracking. Comparative flight and interaction experiments show that the proposed framework improves control accuracy over linear allocation baselines, rejects ground-effect and payload disturbances, and enables close-proximity drawer push--pull manipulation through a $2~\mathrm{cm}$ handle clearance.

## 개요
공중 물리적 상호작용은 차세대 무인 항공기(UAV)의 유망한 방향을 제시하지만, 안정적인 비행을 유지하면서 접촉력을 가할 수 있는 공중 플랫폼이 필요합니다. 근접 작업의 경우, 이는 세 가지 결합된 설계 요구 사항으로 이어집니다: 안정적인 접촉을 위한 다차원 렌치 생성, 제한된 공간에서의 기동성과 안전성을 위한 소형화, 그리고 수평력을 생성할 때 대상으로 향하는 측면 기류 감소입니다. 본 논문은 근접 물리적 상호작용을 위해 서보 구동 제어면을 갖춘 완전 구동 동축 UAV인 FLOAT Drone을 제시합니다. 동축 이중 로터 배치는 소형 추진 레이아웃을 제공하며, 로터 다운워시에 잠긴 제어면은 6자유도 렌치 생성을 위한 측면력과 모멘트를 생성합니다. 경사 로터 대안과의 힘 일치 전산 유체 역학(CFD) 비교를 통해 대상 방향 측면 기류 감소를 정량화합니다. 로터 후류에서의 비선형 로터-제어면 결합을 고려하기 위해, 정밀 힘 측정을 통해 고충실도 다항식 공기역학 렌치 모델을 식별하고, 이를 제약 조건이 있는 비선형 할당기에 내장하여 실시간 렌치 추적을 수행합니다. 비교 비행 및 상호작용 실험은 제안된 프레임워크가 선형 할당 기준선보다 제어 정확도를 향상시키고, 지면 효과 및 페이로드 교란을 억제하며, $2~\mathrm{cm}$ 핸들 틈새를 통한 근접 서랍 밀기-당기기 조작을 가능하게 함을 보여줍니다.

## 핵심 내용
공중 물리적 상호작용은 차세대 무인 항공기(UAV)의 유망한 방향을 제시하지만, 안정적인 비행을 유지하면서 접촉력을 가할 수 있는 공중 플랫폼이 필요합니다. 근접 작업의 경우, 이는 세 가지 결합된 설계 요구 사항으로 이어집니다: 안정적인 접촉을 위한 다차원 렌치 생성, 제한된 공간에서의 기동성과 안전성을 위한 소형화, 그리고 수평력을 생성할 때 대상으로 향하는 측면 기류 감소입니다. 본 논문은 근접 물리적 상호작용을 위해 서보 구동 제어면을 갖춘 완전 구동 동축 UAV인 FLOAT Drone을 제시합니다. 동축 이중 로터 배치는 소형 추진 레이아웃을 제공하며, 로터 다운워시에 잠긴 제어면은 6자유도 렌치 생성을 위한 측면력과 모멘트를 생성합니다. 경사 로터 대안과의 힘 일치 전산 유체 역학(CFD) 비교를 통해 대상 방향 측면 기류 감소를 정량화합니다. 로터 후류에서의 비선형 로터-제어면 결합을 고려하기 위해, 정밀 힘 측정을 통해 고충실도 다항식 공기역학 렌치 모델을 식별하고, 이를 제약 조건이 있는 비선형 할당기에 내장하여 실시간 렌치 추적을 수행합니다. 비교 비행 및 상호작용 실험은 제안된 프레임워크가 선형 할당 기준선보다 제어 정확도를 향상시키고, 지면 효과 및 페이로드 교란을 억제하며, $2~\mathrm{cm}$ 핸들 틈새를 통한 근접 서랍 밀기-당기기 조작을 가능하게 함을 보여줍니다.

## 参考
- http://arxiv.org/abs/2607.04260v1
