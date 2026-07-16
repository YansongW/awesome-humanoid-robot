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
  zh: We present a method for humanoid robot walking on partial footholds such as small stepping stones and rocks with sharp
    surfaces. Our algorithm does not rely on prior knowledge of the foothold, but information about an expected foothold can
    be used to improve the stepping performance. After a step is taken, the robot explores the new contact surface by attempting
    to shift the center of pressure around the foot. The available foothold is inferred by the way in which the foot rotates
    about contact edges and/or by the achieved center of pressure locations on the foot during exploration. This estim
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

## Overview
We present a method for humanoid robot walking on partial footholds such as small stepping stones and rocks with sharp surfaces. Our algorithm does not rely on prior knowledge of the foothold, but information about an expected foothold can be used to improve the stepping performance. After a step is taken, the robot explores the new contact surface by attempting to shift the center of pressure around the foot. The available foothold is inferred by the way in which the foot rotates about contact edges and/or by the achieved center of pressure locations on the foot during exploration. This estimated contact area is then used by a whole body momentum-based control algorithm. To walk and balance on partial footholds, we combine fast, dynamic stepping with the use of upper body angular momentum to regain balance. We applied this method to the Atlas humanoid designed by Boston Dynamics to walk over small contact surfaces, such as line and point contacts. We present experimental results and discuss performance limitations.

## Content
We present a method for humanoid robot walking on partial footholds such as small stepping stones and rocks with sharp surfaces. Our algorithm does not rely on prior knowledge of the foothold, but information about an expected foothold can be used to improve the stepping performance. After a step is taken, the robot explores the new contact surface by attempting to shift the center of pressure around the foot. The available foothold is inferred by the way in which the foot rotates about contact edges and/or by the achieved center of pressure locations on the foot during exploration. This estimated contact area is then used by a whole body momentum-based control algorithm. To walk and balance on partial footholds, we combine fast, dynamic stepping with the use of upper body angular momentum to regain balance. We applied this method to the Atlas humanoid designed by Boston Dynamics to walk over small contact surfaces, such as line and point contacts. We present experimental results and discuss performance limitations.

## 개요
본 논문에서는 작은 디딤돌이나 날카로운 표면의 바위와 같은 부분적인 발판 위에서 인간형 로봇이 보행할 수 있는 방법을 제시합니다. 제안하는 알고리즘은 발판에 대한 사전 지식에 의존하지 않지만, 예상되는 발판에 대한 정보를 활용하여 보행 성능을 향상시킬 수 있습니다. 한 걸음을 내딛은 후, 로봇은 발 주변의 압력 중심을 이동시키려 시도함으로써 새로운 접촉 표면을 탐색합니다. 사용 가능한 발판은 발이 접촉 모서리를 중심으로 회전하는 방식 및/또는 탐색 중 발에서 달성된 압력 중심 위치를 통해 추론됩니다. 이렇게 추정된 접촉 영역은 전신 운동량 기반 제어 알고리즘에 사용됩니다. 부분적인 발판 위에서 보행하고 균형을 유지하기 위해, 빠르고 동적인 보폭과 상체 각운동량을 활용하여 균형을 회복하는 방법을 결합합니다. 본 방법을 Boston Dynamics가 설계한 Atlas 인간형 로봇에 적용하여 선 접촉 및 점 접촉과 같은 작은 접촉 표면 위를 보행하도록 했습니다. 실험 결과를 제시하고 성능 한계에 대해 논의합니다.

## 핵심 내용
본 논문에서는 작은 디딤돌이나 날카로운 표면의 바위와 같은 부분적인 발판 위에서 인간형 로봇이 보행할 수 있는 방법을 제시합니다. 제안하는 알고리즘은 발판에 대한 사전 지식에 의존하지 않지만, 예상되는 발판에 대한 정보를 활용하여 보행 성능을 향상시킬 수 있습니다. 한 걸음을 내딛은 후, 로봇은 발 주변의 압력 중심을 이동시키려 시도함으로써 새로운 접촉 표면을 탐색합니다. 사용 가능한 발판은 발이 접촉 모서리를 중심으로 회전하는 방식 및/또는 탐색 중 발에서 달성된 압력 중심 위치를 통해 추론됩니다. 이렇게 추정된 접촉 영역은 전신 운동량 기반 제어 알고리즘에 사용됩니다. 부분적인 발판 위에서 보행하고 균형을 유지하기 위해, 빠르고 동적인 보폭과 상체 각운동량을 활용하여 균형을 회복하는 방법을 결합합니다. 본 방법을 Boston Dynamics가 설계한 Atlas 인간형 로봇에 적용하여 선 접촉 및 점 접촉과 같은 작은 접촉 표면 위를 보행하도록 했습니다. 실험 결과를 제시하고 성능 한계에 대해 논의합니다.
