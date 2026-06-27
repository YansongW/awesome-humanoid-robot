---
$id: ent_paper_wiedebach_walking_on_partial_footholds_i_2016
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Walking on Partial Footholds Including Line Contacts with the Humanoid Robot
    Atlas
  zh: Atlas人形机器人在部分支撑面（包括线接触）上的行走方法
  ko: 아틀라스 인간형 로봇을 이용한 선 접촉을 포함한 부분 발판 보행
summary:
  en: Presents a momentum-based control method that lets the Atlas humanoid walk and
    balance on partial, uncertain footholds such as line and point contacts by online
    contact-surface exploration and upper-body angular-momentum recovery.
  zh: 提出一种基于动量的控制方法，使Atlas人形机器人能够通过在线接触面探索与上半身角动量恢复，在部分、不确定的支撑面（如线接触和点接触）上行走并保持平衡。
  ko: 온라인 접촉면 탐색과 상체 각운동량 회복을 통해 아틀라스 인간형 로봇이 부분적이고 불확실한 발판(선 접촉 및 점 접촉)에서 보행하고 균형을
    유지할 수 있는 운동량 기반 제어 방법을 제시한다.
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
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from the supplied abstract, key-contribution list, and limitations;
    human review against the PDF is needed before full verification.
sources:
- id: src_001
  type: paper
  title: Walking on Partial Footholds Including Line Contacts with the Humanoid Robot
    Atlas
  url: https://arxiv.org/abs/1607.08089
  date: '2016'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---

## Overview

The paper addresses locomotion over terrain where footholds are too small or sharp to provide a full flat support polygon. Instead of assuming known contact geometry, the controller first explores a newly placed foot by shifting the center of pressure and observing foot rotation; from these measurements it infers the usable contact area. This estimate is then fed into a whole-body momentum-based QP controller that trades off motion tracking against balance. To recover from disturbances on severely reduced contacts, the robot uses rapid stepping together with upper-body angular-momentum lunging.

## Key Contributions

- Reformulates desired motions as weighted objectives in a momentum-based QP controller so balance can be prioritized over motion tracking online.
- Adds a contact-force objective that keeps the center of pressure inside the estimated foothold.
- Introduces online foothold estimation by detecting foot rotation about contact edges and fitting measured CoP locations to expected contact geometries.
- Demonstrates dynamic walking on line and point contacts with the Atlas humanoid in simulation and on hardware.

## Relevance to Humanoid Robotics

Partial or uncertain contacts are common in cluttered indoor, industrial, and outdoor environments. A controller that can reason about limited support areas and recover using whole-body momentum is a key building block for robust humanoid locomotion outside structured flat floors.
