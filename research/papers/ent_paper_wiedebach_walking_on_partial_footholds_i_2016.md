---
$id: ent_paper_wiedebach_walking_on_partial_footholds_i_2016
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Walking on Partial Footholds Including Line Contacts with the Humanoid Robot Atlas
  zh: Atlas人形机器人在部分支撑面（包括线接触）上的行走方法
  ko: 아틀라스 인간형 로봇을 이용한 선 접촉을 포함한 부분 발판 보행
summary:
  en: Presents a momentum-based control method that lets the Atlas humanoid walk and balance on partial, uncertain footholds
    such as line and point contacts by online contact-surface exploration and upper-body angular-momentum recovery.
  zh: 提出一种基于动量的控制方法，使Atlas人形机器人能够通过在线接触面探索与上半身角动量恢复，在部分、不确定的支撑面（如线接触和点接触）上行走并保持平衡。
  ko: 온라인 접촉면 탐색과 상체 각운동량 회복을 통해 아틀라스 인간형 로봇이 부분적이고 불확실한 발판(선 접촉 및 점 접촉)에서 보행하고 균형을 유지할 수 있는 운동량 기반 제어 방법을 제시한다.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid_locomotion
- partial_foothold
- line_contact
- point_contact
- center_of_pressure
- momentum_based_control
- atlas_robot
- dynamic_walking
- foothold_estimation
- angular_momentum
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1607.08089v2.
sources:
- id: src_001
  type: paper
  title: Walking on Partial Footholds Including Line Contacts with the Humanoid Robot Atlas
  url: https://arxiv.org/abs/1607.08089
  date: '2016'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
We present a method for humanoid robot walking on partial footholds such as small stepping stones and rocks with sharp surfaces. Our algorithm does not rely on prior knowledge of the foothold, but information about an expected foothold can be used to improve the stepping performance. After a step is taken, the robot explores the new contact surface by attempting to shift the center of pressure around the foot. The available foothold is inferred by the way in which the foot rotates about contact edges and/or by the achieved center of pressure locations on the foot during exploration. This estimated contact area is then used by a whole body momentum-based control algorithm. To walk and balance on partial footholds, we combine fast, dynamic stepping with the use of upper body angular momentum to regain balance. We applied this method to the Atlas humanoid designed by Boston Dynamics to walk over small contact surfaces, such as line and point contacts. We present experimental results and discuss performance limitations.

## 核心内容
We present a method for humanoid robot walking on partial footholds such as small stepping stones and rocks with sharp surfaces. Our algorithm does not rely on prior knowledge of the foothold, but information about an expected foothold can be used to improve the stepping performance. After a step is taken, the robot explores the new contact surface by attempting to shift the center of pressure around the foot. The available foothold is inferred by the way in which the foot rotates about contact edges and/or by the achieved center of pressure locations on the foot during exploration. This estimated contact area is then used by a whole body momentum-based control algorithm. To walk and balance on partial footholds, we combine fast, dynamic stepping with the use of upper body angular momentum to regain balance. We applied this method to the Atlas humanoid designed by Boston Dynamics to walk over small contact surfaces, such as line and point contacts. We present experimental results and discuss performance limitations.

## 参考
- http://arxiv.org/abs/1607.08089v2

