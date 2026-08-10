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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04260v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (777 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2607.04260v1

## 개요
이 드론은 공중 물리적 상호작용에서의 세 가지 핵심 요구 사항, 즉 다차원 힘 생성, 컴팩트함, 그리고 수평 힘 발생 시 목표물에 대한 측방 기류 감소를 위해 설계되었습니다. 동축 이중 로터 배치는 컴팩트한 동력 구조를 제공하며, 로터 하강 기류에 잠긴 제어면은 측방 힘과 모멘트를 생성하여 6자유도 힘 제어를 구현합니다. 힘 매칭 전산유체역학(CFD) 비교를 통해 경사 로터 방식과 비교하여 측방 기류 감소를 정량화했습니다. 로터와 제어면 사이의 비선형 결합을 해결하기 위해, 연구팀은 정밀 힘 측정에서 고충실도 다항식 공기역학 모델을 식별하고 이를 제약 비선형 할당기에 내장하여 실시간 힘 추적에 사용했습니다. 실험 결과, 이 프레임워크는 제어 정밀도에서 선형 할당 기준선보다 우수하며 지면 효과와 부하 외란을 억제할 수 있음을 보여주었습니다.

## 핵심 내용
### 방법 및 아키텍처
- **플랫폼 설계**: FLOAT Drone은 동축 이중 로터 배치를 채택하고 로터 직경이 작아 전체 구조가 컴팩트하며 제한된 공간에서 기동하기에 적합합니다. 제어면(서보 구동)은 로터 하강 기류에 위치하며, 편향을 통해 측방 힘과 모멘트를 생성하여 6자유도 힘 생성을 구현합니다.
- **공기역학 모델**: 로터 하강 기류와 제어면 사이의 비선형 결합에 대응하기 위해, 연구팀은 정밀 힘 센서로 데이터를 수집하여 고충실도 다항식 공기역학 모델을 식별했습니다. 이 모델은 제약 비선형 할당기에 내장되어 실시간 힘 추적에 사용되며, 기존의 선형 할당 방식을 대체합니다.

### 실험 설정 및 주요 수치
- **CFD 비교**: 힘 매칭 전산유체역학(CFD) 시뮬레이션을 통해 FLOAT Drone을 경사 로터 방식과 비교하여 목표 방향으로의 측방 기류 감소 정도를 정량화했습니다.
- **비행 및 상호작용 실험**: 비교 실험 결과, 제안된 프레임워크는 제어 정밀도에서 선형 할당 기준선보다 우수하며 지면 효과와 부하 외란을 효과적으로 억제할 수 있습니다. 근거리 서랍 밀고 당기기 작업에서 드론은 단 2cm의 핸들 간격만으로도 밀고 당기기 작업을 완료할 수 있습니다.

### 결론
FLOAT Drone은 컴팩트한 동축 이중 로터 설계와 고충실도 공기역학 모델 기반의 비선형 제어를 통해 안정적인 근거리 물리적 상호작용을 구현했습니다. 실험은 제어 정밀도, 외란 저항 능력, 그리고 좁은 공간에서의 조작에서의 우수성을 검증했으며, 차세대 드론의 접촉식 작업 적용을 위한 실현 가능한 솔루션을 제공합니다.
