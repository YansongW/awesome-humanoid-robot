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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.02764v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (601 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2607.02764v1

## 개요
MorphQuad는 기존 비행체가 최대 추력 벡터링, 전역 안정성, 그리고 컴팩트한 표준 설계를 동시에 구현하지 못하는 문제를 해결합니다. 하드웨어 측면에서 각 로터 시스템은 독립적인 2축 짐벌을 통해 자유롭게 편향됩니다. 제어 측면에서는 전역 안정 제어 전략과 에너지 최적 추력 분배를 사용하며, 다운워시 간섭과 짐벌 잠금을 피할 때에만 추력 상쇄를 허용합니다. 이 비행체는 완전한 온보드 자율 조건에서 다회전 비행, 밸브 조작, 단일 로터 내풍 등의 능력을 보여주며, 인간 수준의 성능을 달성합니다.

## 핵심 내용
### 방법
MorphQuad의 핵심은 하드웨어와 제어의 공동 설계입니다:
- **하드웨어**: 4개의 로터 시스템 각각에 2축 짐벌을 장착하여 독립적인 편향을 구현하고, 이를 통해 임의의 방향으로 최대 추력을 생성합니다.
- **제어**: 전역 안정 제어를 도입하여 비행체가 어떤 자세와 위치에서도 안정적으로 유지되도록 합니다. 에너지 최적 추력 분배 알고리즘은 다운워시 간섭과 짐벌 잠금을 피하기 위해 필요한 경우에만 로터 간 추력 상쇄를 허용합니다.

### 실험 설정 및 주요 수치
- **자율성**: 외부 계산이나 위치 보조 없이 완전한 온보드 자율 운영을 수행합니다.
- **기동성**: 병진 또는 호버링 상태에서 다회전 비행을 완료하며, 파이프라인 검사와 목표 추적에 사용됩니다.
- **조작 능력**: 밸브 회전, 착지, 물체 누르기 및 밀고 당기기를 구현하며, 힘은 인간 수준에 도달합니다.
- **탄력성**: 단일 로터에 대한 강풍을 포함한 임의 방향의 풍력 간섭을 견딜 수 있으며, 밀고 당기기 복구 능력을 갖추고 있습니다.

### 결론
MorphQuad는 하드웨어와 제어의 공동 설계를 통해 쿼드로터 플랫폼에서 처음으로 최대 추력 벡터링, 전역 안정성, 그리고 컴팩트한 표준 설계를 동시에 구현했습니다. 이를 통해 인프라 유지보수, 접촉식 검사, 그리고 긴급 대응을 위한 고성능 공중 조작 플랫폼을 제공합니다.
