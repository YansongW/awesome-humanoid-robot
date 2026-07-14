---
$id: ent_paper_yu_quasi_direct_drive_actuation_f_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Quasi-Direct Drive Actuation for a Lightweight Hip Exoskeleton with High Backdrivability and High Bandwidth
  zh: 用于高反驱性和高带宽轻量化髋关节外骨骼的准直驱驱动
  ko: 높은 역구동성 및 높은 대역폭을 가진 경량 고관절 외골격용 준직구동 구동
summary:
  en: This paper presents a custom quasi-direct-drive actuator and a 3.4 kg bilateral hip exoskeleton that achieves 17.5 Nm
    nominal torque, 0.4 Nm backdrive torque, 62.4 Hz bandwidth, and a simple controller validated during walking and squatting.
  zh: 本文介绍了一种定制准直驱执行器和一个3.4公斤的双侧髋关节外骨骼，实现了17.5牛·米额定扭矩、0.4牛·米反驱扭矩、62.4赫兹带宽，并在行走和蹲起中验证了简单的控制器。
  ko: 본 논문은 맞춤형 준직구동 구동기와 17.5 Nm 정격 토크, 0.4 Nm 역구동 토크, 62.4 Hz 대역폭을 달성하고 보행 및 스쿼팅에서 간단한 제어기를 검증한 3.4 kg 양측 고관절 외골격을 제시한다.
domains:
- 02_components
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
- component
tags:
- quasi_direct_drive
- qdd
- hip_exoskeleton
- wearable_robot
- actuator
- backdrivability
- high_bandwidth
- bldc_motor
- planetary_gearbox
- design_for_control
- lower_limb_assist
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2004.00467v1.
sources:
- id: src_001
  type: paper
  title: Quasi-Direct Drive Actuation for a Lightweight Hip Exoskeleton with High Backdrivability and High Bandwidth
  url: https://arxiv.org/abs/2004.00467
  date: '2020'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
High-performance actuators are crucial to enable mechanical versatility of lower-limb wearable robots, which are required to be lightweight, highly backdrivable, and with high bandwidth. State-of-the-art actuators, e.g., series elastic actuators (SEAs), have to compromise bandwidth to improve compliance (i.e., backdrivability). In this paper, we describe the design and human-robot interaction modeling of a portable hip exoskeleton based on our custom quasi-direct drive (QDD) actuation (i.e., a high torque density motor with low ratio gear). We also present a model-based performance benchmark comparison of representative actuators in terms of torque capability, control bandwidth, backdrivability, and force tracking accuracy. This paper aims to corroborate the underlying philosophy of "design for control", namely meticulous robot design can simplify control algorithms while ensuring high performance. Following this idea, we create a lightweight bilateral hip exoskeleton (overall mass is 3.4 kg) to reduce joint loadings during normal activities, including walking and squatting. Experimental results indicate that the exoskeleton is able to produce high nominal torque (17.5 Nm), high backdrivability (0.4 Nm backdrive torque), high bandwidth (62.4 Hz), and high control accuracy (1.09 Nm root mean square tracking error, i.e., 5.4% of the desired peak torque). Its controller is versatile to assist walking at different speeds (0.8-1.4 m/s) and squatting at 2 s cadence. This work demonstrates significant improvement in backdrivability and control bandwidth compared with state-of-the-art exoskeletons powered by the conventional actuation or SEA.

## 核心内容
High-performance actuators are crucial to enable mechanical versatility of lower-limb wearable robots, which are required to be lightweight, highly backdrivable, and with high bandwidth. State-of-the-art actuators, e.g., series elastic actuators (SEAs), have to compromise bandwidth to improve compliance (i.e., backdrivability). In this paper, we describe the design and human-robot interaction modeling of a portable hip exoskeleton based on our custom quasi-direct drive (QDD) actuation (i.e., a high torque density motor with low ratio gear). We also present a model-based performance benchmark comparison of representative actuators in terms of torque capability, control bandwidth, backdrivability, and force tracking accuracy. This paper aims to corroborate the underlying philosophy of "design for control", namely meticulous robot design can simplify control algorithms while ensuring high performance. Following this idea, we create a lightweight bilateral hip exoskeleton (overall mass is 3.4 kg) to reduce joint loadings during normal activities, including walking and squatting. Experimental results indicate that the exoskeleton is able to produce high nominal torque (17.5 Nm), high backdrivability (0.4 Nm backdrive torque), high bandwidth (62.4 Hz), and high control accuracy (1.09 Nm root mean square tracking error, i.e., 5.4% of the desired peak torque). Its controller is versatile to assist walking at different speeds (0.8-1.4 m/s) and squatting at 2 s cadence. This work demonstrates significant improvement in backdrivability and control bandwidth compared with state-of-the-art exoskeletons powered by the conventional actuation or SEA.

## 参考
- http://arxiv.org/abs/2004.00467v1

