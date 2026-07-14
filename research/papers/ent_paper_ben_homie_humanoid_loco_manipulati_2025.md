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
  en: HOMIE is a low-cost, open-source semi-autonomous teleoperation cockpit for humanoid loco-manipulation that combines
    an RL-trained lower-body policy, isomorphic 7-DoF exoskeleton arms, and Hall-sensor motion-sensing gloves, and validates
    a real-world data flywheel for imitation learning.
  zh: HOMIE是一种低成本、开源的半自主遥操作驾驶舱，用于人形机器人移动操作，结合了强化学习训练的下半身策略、同构7自由度外骨骼手臂以及霍尔传感器运动感知手套，并验证了用于模仿学习的真实数据飞轮。
  ko: HOMIE는 강화학습으로 학습된 하반신 정책, 동형 7자유도 외골격 팔, 그리고 홀 센서 동작 감지 장갑을 결합한 저비용 오픈소스 반자율 원격조종 조종석으로, 휴머노이드 이동-조작을 위한 모방학습 데이터 플라이휠을
    실제로 검증하였다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.13013v2.
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
## 概述
Generalizable humanoid loco-manipulation poses significant challenges, requiring coordinated whole-body control and precise, contact-rich object manipulation. To address this, this paper introduces HOMIE, a semi-autonomous teleoperation system that combines a reinforcement learning policy for body control mapped to a pedal, an isomorphic exoskeleton arm for arm control, and motion-sensing gloves for hand control, forming a unified cockpit to freely operate humanoids and establish a data flywheel. The policy incorporates novel designs, including an upper-body pose curriculum, a height-tracking reward, and symmetry utilization. These features enable the system to perform walking and squatting to specific heights while seamlessly adapting to arbitrary upper-body poses. The exoskeleton, by eliminating the reliance on inverse dynamics, delivers faster and more precise arm control. The gloves utilize Hall sensors instead of servos, allowing even compact devices to achieve 15 or more degrees of freedom and freely adapt to any model of dexterous hands. Compared to previous teleoperation systems, HOMIE stands out for its exceptional efficiency, completing tasks in half the time; its expanded working range, allowing users to freely reach high and low areas as well as interact with any objects; and its affordability, with a price of just $500. The system is fully open-source, demos and code can be found in our https://homietele.github.io/.

## 核心内容
Generalizable humanoid loco-manipulation poses significant challenges, requiring coordinated whole-body control and precise, contact-rich object manipulation. To address this, this paper introduces HOMIE, a semi-autonomous teleoperation system that combines a reinforcement learning policy for body control mapped to a pedal, an isomorphic exoskeleton arm for arm control, and motion-sensing gloves for hand control, forming a unified cockpit to freely operate humanoids and establish a data flywheel. The policy incorporates novel designs, including an upper-body pose curriculum, a height-tracking reward, and symmetry utilization. These features enable the system to perform walking and squatting to specific heights while seamlessly adapting to arbitrary upper-body poses. The exoskeleton, by eliminating the reliance on inverse dynamics, delivers faster and more precise arm control. The gloves utilize Hall sensors instead of servos, allowing even compact devices to achieve 15 or more degrees of freedom and freely adapt to any model of dexterous hands. Compared to previous teleoperation systems, HOMIE stands out for its exceptional efficiency, completing tasks in half the time; its expanded working range, allowing users to freely reach high and low areas as well as interact with any objects; and its affordability, with a price of just $500. The system is fully open-source, demos and code can be found in our https://homietele.github.io/.

## 参考
- http://arxiv.org/abs/2502.13013v2

