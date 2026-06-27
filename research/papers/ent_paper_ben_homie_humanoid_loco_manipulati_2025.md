---
$id: ent_paper_ben_homie_humanoid_loco_manipulati_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit'
  zh: HOMIE：基于同构外骨骼驾驶舱的人形机器人移动操作
  ko: 'HOMIE: 동형 외골격 조종석을 활용한 휴머노이드 이동-조작'
summary:
  en: HOMIE is a low-cost, open-source semi-autonomous teleoperation cockpit for humanoid
    loco-manipulation that combines an RL-trained lower-body policy, isomorphic 7-DoF
    exoskeleton arms, and Hall-sensor motion-sensing gloves, and validates a real-world
    data flywheel for imitation learning.
  zh: HOMIE是一种低成本、开源的半自主遥操作驾驶舱，用于人形机器人移动操作，结合了强化学习训练的下半身策略、同构7自由度外骨骼手臂以及霍尔传感器运动感知手套，并验证了用于模仿学习的真实数据飞轮。
  ko: HOMIE는 강화학습으로 학습된 하반신 정책, 동형 7자유도 외골격 팔, 그리고 홀 센서 동작 감지 장갑을 결합한 저비용 오픈소스 반자율
    원격조종 조종석으로, 휴머노이드 이동-조작을 위한 모방학습 데이터 플라이휠을 실제로 검증하였다.
domains:
- 02_components
- 07_ai_models_algorithms
- 09_data_datasets
- 05_mass_production
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- system
- intelligence
tags:
- teleoperation
- humanoid_loco_manipulation
- whole_body_control
- exoskeleton
- reinforcement_learning
- imitation_learning
- data_flywheel
- dexterous_hand
- low_cost_hardware
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from abstract and supplied metadata; full paper review is needed
    to confirm section-level claims, exact hardware list, and open-source release
    details.
sources:
- id: src_001
  type: paper
  title: 'HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit'
  url: https://arxiv.org/abs/2502.13013
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
- system
---

## Overview

Generalizable humanoid loco-manipulation requires simultaneous whole-body control and precise, contact-rich manipulation, but prior systems typically excel at either locomotion or upper-body manipulation without integrating both. HOMIE addresses this gap with a unified, semi-autonomous teleoperation cockpit that lets a single operator control a humanoid robot’s full body in real time. The system combines a reinforcement-learning lower-body policy driven by a foot pedal, isomorphic 7-DoF exoskeleton arms for arm control, and Hall-sensor motion-sensing gloves for dexterous hand control.

The lower-body policy incorporates an upper-body pose curriculum, a height-tracking reward, and symmetry utilization, enabling the robot to walk and squat to specified heights while adapting to arbitrary upper-body poses. The exoskeleton maps the operator’s arm joints directly to the robot, avoiding inverse dynamics and thereby improving arm-control speed and precision. The gloves replace servos with Hall effect sensors and neodymium magnets, allowing compact hardware to capture 15 or more degrees of freedom and to adapt to different dexterous hand models.

Experiments demonstrate that HOMIE completes tasks roughly twice as fast as previous teleoperation systems, extends the reachable workspace to high and low regions, and costs about $500 in hardware. The system is fully open-source, and the authors further validate a real-world data flywheel by training an imitation-learning autonomous policy from HOMIE-collected demonstrations.

## Key Contributions

- A unified humanoid teleoperation cockpit enabling single-operator full-body control via RL-based locomotion, isomorphic exoskeleton arms, and motion-sensing gloves.
- The first teleoperation-compatible humanoid loco-manipulation system with dynamic squatting that does not rely on motion-prior data.
- A low-cost ($500) hardware design achieving faster and more precise whole-body control than prior VR/vision-based teleoperation systems.
- Validation of a real-world data flywheel by training an imitation-learning autonomous policy from HOMIE-collected demonstrations.

## Relevance to Humanoid Robotics

HOMIE is directly relevant to scalable humanoid deployment because it provides a low-cost, open-source, single-operator full-body teleoperation interface. By supporting locomotion, dual-arm manipulation, and dexterous hand control in one coherent system, it lowers the barrier to collecting high-quality demonstration data for humanoid robots. The paper’s emphasis on a $500 hardware bill of materials and open-source release aligns with mass-production and democratization goals for humanoid robotics.

Beyond teleoperation, HOMIE closes the loop between human demonstration and autonomous policy learning: the collected demonstrations feed an imitation-learning policy, illustrating a practical data flywheel. This makes the work relevant to component design, AI algorithms, datasets, and manufacturing scale-up within the humanoid-robot knowledge chain.
