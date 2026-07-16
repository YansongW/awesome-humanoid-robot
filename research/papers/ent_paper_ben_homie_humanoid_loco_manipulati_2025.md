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

## Overview
Generalizable humanoid loco-manipulation poses significant challenges, requiring coordinated whole-body control and precise, contact-rich object manipulation. To address this, this paper introduces HOMIE, a semi-autonomous teleoperation system that combines a reinforcement learning policy for body control mapped to a pedal, an isomorphic exoskeleton arm for arm control, and motion-sensing gloves for hand control, forming a unified cockpit to freely operate humanoids and establish a data flywheel. The policy incorporates novel designs, including an upper-body pose curriculum, a height-tracking reward, and symmetry utilization. These features enable the system to perform walking and squatting to specific heights while seamlessly adapting to arbitrary upper-body poses. The exoskeleton, by eliminating the reliance on inverse dynamics, delivers faster and more precise arm control. The gloves utilize Hall sensors instead of servos, allowing even compact devices to achieve 15 or more degrees of freedom and freely adapt to any model of dexterous hands. Compared to previous teleoperation systems, HOMIE stands out for its exceptional efficiency, completing tasks in half the time; its expanded working range, allowing users to freely reach high and low areas as well as interact with any objects; and its affordability, with a price of just $500. The system is fully open-source, demos and code can be found in our https://homietele.github.io/.

## Content
Generalizable humanoid loco-manipulation poses significant challenges, requiring coordinated whole-body control and precise, contact-rich object manipulation. To address this, this paper introduces HOMIE, a semi-autonomous teleoperation system that combines a reinforcement learning policy for body control mapped to a pedal, an isomorphic exoskeleton arm for arm control, and motion-sensing gloves for hand control, forming a unified cockpit to freely operate humanoids and establish a data flywheel. The policy incorporates novel designs, including an upper-body pose curriculum, a height-tracking reward, and symmetry utilization. These features enable the system to perform walking and squatting to specific heights while seamlessly adapting to arbitrary upper-body poses. The exoskeleton, by eliminating the reliance on inverse dynamics, delivers faster and more precise arm control. The gloves utilize Hall sensors instead of servos, allowing even compact devices to achieve 15 or more degrees of freedom and freely adapt to any model of dexterous hands. Compared to previous teleoperation systems, HOMIE stands out for its exceptional efficiency, completing tasks in half the time; its expanded working range, allowing users to freely reach high and low areas as well as interact with any objects; and its affordability, with a price of just $500. The system is fully open-source, demos and code can be found in our https://homietele.github.io/.

## 개요
일반화 가능한 휴머노이드 로코-매니퓰레이션은 조화로운 전신 제어와 정밀하고 접촉이 많은 물체 조작을 필요로 하여 상당한 도전 과제를 제시합니다. 이를 해결하기 위해, 본 논문은 HOMIE를 소개합니다. HOMIE는 페달에 매핑된 신체 제어를 위한 강화 학습 정책, 팔 제어를 위한 동형 외골격 팔, 손 제어를 위한 모션 센싱 장갑을 결합한 반자율 원격 조작 시스템으로, 통합된 조종석을 형성하여 휴머노이드를 자유롭게 작동하고 데이터 플라이휠을 구축합니다. 이 정책은 상체 자세 커리큘럼, 높이 추적 보상, 대칭 활용을 포함한 새로운 설계를 통합합니다. 이러한 기능을 통해 시스템은 특정 높이로 걷기와 스쿼트를 수행하면서 임의의 상체 자세에 원활하게 적응할 수 있습니다. 외골격은 역동역학에 대한 의존성을 제거하여 더 빠르고 정밀한 팔 제어를 제공합니다. 장갑은 서보 대신 홀 센서를 사용하여 소형 장치에서도 15자유도 이상을 달성하고 모든 모델의 다지 손에 자유롭게 적응할 수 있습니다. 이전 원격 조작 시스템과 비교하여 HOMIE는 작업을 절반 시간에 완료하는 뛰어난 효율성, 사용자가 높은 곳과 낮은 곳에 자유롭게 도달하고 모든 물체와 상호작용할 수 있는 확장된 작업 범위, 그리고 단 500달러의 가격으로 경제성을 자랑합니다. 이 시스템은 완전히 오픈 소스이며, 데모와 코드는 https://homietele.github.io/에서 확인할 수 있습니다.

## 핵심 내용
일반화 가능한 휴머노이드 로코-매니퓰레이션은 조화로운 전신 제어와 정밀하고 접촉이 많은 물체 조작을 필요로 하여 상당한 도전 과제를 제시합니다. 이를 해결하기 위해, 본 논문은 HOMIE를 소개합니다. HOMIE는 페달에 매핑된 신체 제어를 위한 강화 학습 정책, 팔 제어를 위한 동형 외골격 팔, 손 제어를 위한 모션 센싱 장갑을 결합한 반자율 원격 조작 시스템으로, 통합된 조종석을 형성하여 휴머노이드를 자유롭게 작동하고 데이터 플라이휠을 구축합니다. 이 정책은 상체 자세 커리큘럼, 높이 추적 보상, 대칭 활용을 포함한 새로운 설계를 통합합니다. 이러한 기능을 통해 시스템은 특정 높이로 걷기와 스쿼트를 수행하면서 임의의 상체 자세에 원활하게 적응할 수 있습니다. 외골격은 역동역학에 대한 의존성을 제거하여 더 빠르고 정밀한 팔 제어를 제공합니다. 장갑은 서보 대신 홀 센서를 사용하여 소형 장치에서도 15자유도 이상을 달성하고 모든 모델의 다지 손에 자유롭게 적응할 수 있습니다. 이전 원격 조작 시스템과 비교하여 HOMIE는 작업을 절반 시간에 완료하는 뛰어난 효율성, 사용자가 높은 곳과 낮은 곳에 자유롭게 도달하고 모든 물체와 상호작용할 수 있는 확장된 작업 범위, 그리고 단 500달러의 가격으로 경제성을 자랑합니다. 이 시스템은 완전히 오픈 소스이며, 데모와 코드는 https://homietele.github.io/에서 확인할 수 있습니다.
