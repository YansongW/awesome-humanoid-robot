---
$id: ent_paper_morphquad_morphable_quadrotor_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MorphQuad: Morphable Quadrotor for Superhuman Maneuverability, Manipulation, and Resiliency'
  zh: 'MorphQuad: Morphable Quadrotor for Superhuman Maneuverability, Manipulation, and Resiliency'
  ko: 'MorphQuad: Morphable Quadrotor for Superhuman Maneuverability, Manipulation, and Resiliency'
summary:
  en: 'arXiv:2607.02764v1 Announce Type: new Abstract: Infrastructure maintenance, contact-based inspection, and emergency
    response can benefit from aerial vehicles that act as a flying human hand with extreme maneuverability, manipulation,
    and resiliency (MMR): maneuverability to fly in arbitrary orientations to reach remote and tight locations; manipulation
    to point sensors, turn valves, and press tools at arbitrary orientations; resiliency to maintain accurate motion and force
    control despite disturbances from arbitrary directions, such as wind, ground effects, and friction. Realizing MMR on aerial
    vehicles requires not only omnidirectional flight; it also requires (I) vectoring of maximum thrust in any direction,
    to maximize capacity for contact-force application and disturbance rejection, (II) global stability, to enable control
    over any orientation/position, and (III) compact, standard designs that build upon platforms such as quadrotors to inherit
    technological know-how. No current aerial vehicle simultaneously enables I--III, due to structural and control limitations
    that constrain actuation. We present MorphQuad: a morphable quadrotor that enjoys MMR. Key to our approach is a hardware
    and control co-design: on hardware, we independently articulate each of the four rotor systems via two-axis gimbals; on
    control, we introduce globally-stable control, and energy-optimal thrust allocation that permits inter-rotor thrust cancellations
    only to avoid downwash interference and gimbal lock. With fully-onboard autonomy, MorphQuad demonstrates multi-revolution
    rotation while translating or hovering, for pipe inspection and target tracking (maneuverability); valve turning, perching,
    and object pressing and pushing with human-level strengths (manipulation); and wind rejection from any direction, even
    directed to a single rotor, and push-pull recovery (resiliency).'
  zh: MorphQuad 是一种可变形四旋翼飞行器，由研究团队通过硬件与控制协同设计实现，旨在同时具备超机动性、操作能力和抗干扰韧性。其核心创新在于为每个旋翼配备双轴云台，并结合全局稳定控制与能量最优推力分配算法，使飞行器能在任意方向输出最大推力，并避免下洗干扰和万向节锁死。
  ko: 'arXiv:2607.02764v1 Announce Type: new Abstract: Infrastructure maintenance, contact-based inspection, and emergency
    response can benefit from aerial vehicles that act as a flying human hand with extreme maneuverability, manipulation,
    and resiliency (MMR): maneuverability to fly in arbitrary orientations to reach remote and tight locations; manipulation
    to point sensors, turn valves, and press tools at arbitrary orientations; resiliency to maintain accurate motion and force
    control despite disturbances from arbitrary directions, such as wind, ground effects, and friction. Realizing MMR on aerial
    vehicles requires not only omnidirectional flight; it also requires (I) vectoring of maximum thrust in any direction,
    to maximize capacity for contact-force application and disturbance rejection, (II) global stability, to enable control
    over any orientation/position, and (III) compact, standard designs that build upon platforms such as quadrotors to inherit
    technological know-how. No current aerial vehicle simultaneously enables I--III, due to structural and control limitations
    that constrain actuation. We present MorphQuad: a morphable quadrotor that enjoys MMR. Key to our approach is a hardware
    and control co-design: on hardware, we independently articulate each of the four rotor systems via two-axis gimbals; on
    control, we introduce globally-stable control, and energy-optimal thrust allocation that permits inter-rotor thrust cancellations
    only to avoid downwash interference and gimbal lock. With fully-onboard autonomy, MorphQuad demonstrates multi-revolution
    rotation while translating or hovering, for pipe inspection and target tracking (maneuverability); valve turning, perching,
    and object pressing and pushing with human-level strengths (manipulation); and wind rejection from any direction, even
    directed to a single rotor, and push-pull recovery (resiliency).'
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
- morphquad
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.02764v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'MorphQuad: Morphable Quadrotor for Superhuman Maneuverability, Manipulation, and Resiliency (arXiv)'
  url: https://arxiv.org/abs/2607.02764
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
MorphQuad 解决了现有飞行器无法同时实现最大推力矢量、全局稳定性和紧凑标准设计的问题。硬件上，每个旋翼系统通过独立双轴云台实现自由偏转；控制上，采用全局稳定控制策略和能量最优推力分配，仅在避免下洗干扰和万向节锁死时允许推力抵消。该飞行器在完全机载自主条件下，展示了多圈旋转飞行、阀门操作、单旋翼抗风等能力，性能达到人类水平。

## 核心内容
### 方法
MorphQuad 的核心是硬件与控制协同设计：
- **硬件**：四个旋翼系统各配备双轴云台，实现独立偏转，从而在任意方向产生最大推力。
- **控制**：引入全局稳定控制，确保飞行器在任何姿态和位置下均可稳定；能量最优推力分配算法仅在必要时允许旋翼间推力抵消，以避免下洗干扰和万向节锁死。

### 实验设置与关键数字
- **自主性**：完全机载自主运行，无需外部计算或定位辅助。
- **机动性**：在平移或悬停状态下完成多圈旋转，用于管道检测和目标跟踪。
- **操作能力**：实现阀门转动、栖息、物体按压和推拉，力量达到人类水平。
- **韧性**：可抵御任意方向的风力干扰，包括针对单个旋翼的强风，并具备推拉恢复能力。

### 结论
MorphQuad 通过硬件与控制协同设计，首次在四旋翼平台上同时实现了最大推力矢量、全局稳定性和紧凑标准设计，为基础设施维护、接触式检测和应急响应提供了高性能空中操作平台。

## Overview
Infrastructure maintenance, contact-based inspection, and emergency response can benefit from aerial vehicles that act as a flying human hand with extreme maneuverability, manipulation, and resiliency (MMR): maneuverability to fly in arbitrary orientations to reach remote and tight locations; manipulation to point sensors, turn valves, and press tools at arbitrary orientations; resiliency to maintain accurate motion and force control despite disturbances from arbitrary directions, such as wind, ground effects, and friction. Realizing MMR on aerial vehicles requires not only omnidirectional flight; it also requires (I) vectoring of maximum thrust in any direction, to maximize capacity for contact-force application and disturbance rejection, (II) global stability, to enable control over any orientation/position, and (III) compact, standard designs that build upon platforms such as quadrotors to inherit technological know-how. No current aerial vehicle simultaneously enables I--III, due to structural and control limitations that constrain actuation. We present MorphQuad: a morphable quadrotor that enjoys MMR. Key to our approach is a hardware and control co-design: on hardware, we independently articulate each of the four rotor systems via two-axis gimbals; on control, we introduce globally-stable control, and energy-optimal thrust allocation that permits inter-rotor thrust cancellations only to avoid downwash interference and gimbal lock. With fully-onboard autonomy, MorphQuad demonstrates multi-revolution rotation while translating or hovering, for pipe inspection and target tracking (maneuverability); valve turning, perching, and object pressing and pushing with human-level strengths (manipulation); and wind rejection from any direction, even directed to a single rotor, and push-pull recovery (resiliency).

## 개요
인프라 유지보수, 접촉 기반 점검 및 긴급 대응은 극한의 기동성, 조작성 및 복원력(MMR)을 갖춘 비행하는 인간의 손 역할을 하는 항공기로부터 이점을 얻을 수 있습니다: 기동성은 원격지 및 협소한 위치에 도달하기 위해 임의의 방향으로 비행하는 능력; 조작성은 임의의 방향으로 센서를 지향하고, 밸브를 돌리며, 도구를 누르는 능력; 복원력은 바람, 지면 효과 및 마찰과 같은 임의의 방향에서 발생하는 외란에도 불구하고 정확한 운동 및 힘 제어를 유지하는 능력입니다. 항공기에서 MMR을 구현하려면 전방향 비행뿐만 아니라 (I) 접촉력 적용 및 외란 제거 능력을 극대화하기 위해 모든 방향으로 최대 추력을 벡터링하는 능력, (II) 모든 자세/위치에 대한 제어를 가능하게 하는 전역적 안정성, (III) 쿼드로터와 같은 플랫폼을 기반으로 기술 노하우를 계승하는 소형 표준 설계가 필요합니다. 현재의 항공기 중 작동을 제한하는 구조적 및 제어적 한계로 인해 I~III을 동시에 구현하는 것은 없습니다. 우리는 MMR을 갖춘 변형 가능한 쿼드로터인 MorphQuad를 제시합니다. 우리 접근법의 핵심은 하드웨어와 제어의 공동 설계입니다: 하드웨어에서는 2축 짐벌을 통해 4개의 로터 시스템을 각각 독립적으로 관절화하고; 제어에서는 전역적으로 안정적인 제어와 다운워시 간섭 및 짐벌 잠금을 피하기 위해서만 로터 간 추력 상쇄를 허용하는 에너지 최적 추력 할당을 도입합니다. 완전 온보드 자율성을 갖춘 MorphQuad는 파이프 검사 및 표적 추적(기동성)을 위해 이동 또는 호버링 중 다회전 회전을 시연하고; 인간 수준의 힘으로 밸브 돌리기, 착지, 물체 누르기 및 밀기(조작성); 그리고 단일 로터에 직접 향하는 경우를 포함한 모든 방향의 바람 저항 및 푸시-풀 복구(복원력)를 시연합니다.

## 핵심 내용
인프라 유지보수, 접촉 기반 점검 및 긴급 대응은 극한의 기동성, 조작성 및 복원력(MMR)을 갖춘 비행하는 인간의 손 역할을 하는 항공기로부터 이점을 얻을 수 있습니다: 기동성은 원격지 및 협소한 위치에 도달하기 위해 임의의 방향으로 비행하는 능력; 조작성은 임의의 방향으로 센서를 지향하고, 밸브를 돌리며, 도구를 누르는 능력; 복원력은 바람, 지면 효과 및 마찰과 같은 임의의 방향에서 발생하는 외란에도 불구하고 정확한 운동 및 힘 제어를 유지하는 능력입니다. 항공기에서 MMR을 구현하려면 전방향 비행뿐만 아니라 (I) 접촉력 적용 및 외란 제거 능력을 극대화하기 위해 모든 방향으로 최대 추력을 벡터링하는 능력, (II) 모든 자세/위치에 대한 제어를 가능하게 하는 전역적 안정성, (III) 쿼드로터와 같은 플랫폼을 기반으로 기술 노하우를 계승하는 소형 표준 설계가 필요합니다. 현재의 항공기 중 작동을 제한하는 구조적 및 제어적 한계로 인해 I~III을 동시에 구현하는 것은 없습니다. 우리는 MMR을 갖춘 변형 가능한 쿼드로터인 MorphQuad를 제시합니다. 우리 접근법의 핵심은 하드웨어와 제어의 공동 설계입니다: 하드웨어에서는 2축 짐벌을 통해 4개의 로터 시스템을 각각 독립적으로 관절화하고; 제어에서는 전역적으로 안정적인 제어와 다운워시 간섭 및 짐벌 잠금을 피하기 위해서만 로터 간 추력 상쇄를 허용하는 에너지 최적 추력 할당을 도입합니다. 완전 온보드 자율성을 갖춘 MorphQuad는 파이프 검사 및 표적 추적(기동성)을 위해 이동 또는 호버링 중 다회전 회전을 시연하고; 인간 수준의 힘으로 밸브 돌리기, 착지, 물체 누르기 및 밀기(조작성); 그리고 단일 로터에 직접 향하는 경우를 포함한 모든 방향의 바람 저항 및 푸시-풀 복구(복원력)를 시연합니다.

## 参考
- http://arxiv.org/abs/2607.02764v1
