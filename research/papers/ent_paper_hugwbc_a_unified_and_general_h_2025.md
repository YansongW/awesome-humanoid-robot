---
$id: ent_paper_hugwbc_a_unified_and_general_h_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HugWBC: A Unified and General Humanoid Whole-Body Controller'
  zh: 'HugWBC: A Unified and General Humanoid Whole-Body Controller'
  ko: 'HugWBC: A Unified and General Humanoid Whole-Body Controller'
summary:
  en: 'HugWBC: A Unified and General Humanoid Whole-Body Controller is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  zh: 'HugWBC: A Unified and General Humanoid Whole-Body Controller is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  ko: 'HugWBC: A Unified and General Humanoid Whole-Body Controller is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- hugwbc
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.03206v3.
sources:
- id: src_001
  type: paper
  title: 'HugWBC: A Unified and General Humanoid Whole-Body Controller (arXiv)'
  url: https://arxiv.org/abs/2502.03206
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Locomotion is a fundamental skill for humanoid robots. However, most existing works make locomotion a single, tedious, unextendable, and unconstrained movement. This limits the kinematic capabilities of humanoid robots. In contrast, humans possess versatile athletic abilities-running, jumping, hopping, and finely adjusting gait parameters such as frequency and foot height. In this paper, we investigate solutions to bring such versatility into humanoid locomotion and thereby propose HugWBC: a unified and general humanoid whole-body controller for versatile locomotion. By designing a general command space in the aspect of tasks and behaviors, along with advanced techniques like symmetrical loss and intervention training for learning a whole-body humanoid controlling policy in simulation, HugWBC enables real-world humanoid robots to produce various natural gaits, including walking, jumping, standing, and hopping, with customizable parameters such as frequency, foot swing height, further combined with different body height, waist rotation, and body pitch. Beyond locomotion, HugWBC also supports real-time interventions from external upper-body controllers like teleoperation, enabling loco-manipulation with precision under any locomotive behavior. Extensive experiments validate the high tracking accuracy and robustness of HugWBC with/without upper-body intervention for all commands, and we further provide an in-depth analysis of how the various commands affect humanoid movement and offer insights into the relationships between these commands. To our knowledge, HugWBC is the first humanoid whole-body controller that supports such versatile locomotion behaviors with high robustness and flexibility.

## 核心内容
Locomotion is a fundamental skill for humanoid robots. However, most existing works make locomotion a single, tedious, unextendable, and unconstrained movement. This limits the kinematic capabilities of humanoid robots. In contrast, humans possess versatile athletic abilities-running, jumping, hopping, and finely adjusting gait parameters such as frequency and foot height. In this paper, we investigate solutions to bring such versatility into humanoid locomotion and thereby propose HugWBC: a unified and general humanoid whole-body controller for versatile locomotion. By designing a general command space in the aspect of tasks and behaviors, along with advanced techniques like symmetrical loss and intervention training for learning a whole-body humanoid controlling policy in simulation, HugWBC enables real-world humanoid robots to produce various natural gaits, including walking, jumping, standing, and hopping, with customizable parameters such as frequency, foot swing height, further combined with different body height, waist rotation, and body pitch. Beyond locomotion, HugWBC also supports real-time interventions from external upper-body controllers like teleoperation, enabling loco-manipulation with precision under any locomotive behavior. Extensive experiments validate the high tracking accuracy and robustness of HugWBC with/without upper-body intervention for all commands, and we further provide an in-depth analysis of how the various commands affect humanoid movement and offer insights into the relationships between these commands. To our knowledge, HugWBC is the first humanoid whole-body controller that supports such versatile locomotion behaviors with high robustness and flexibility.

## 参考
- http://arxiv.org/abs/2502.03206v3

## Overview
Locomotion is a fundamental skill for humanoid robots. However, most existing works make locomotion a single, tedious, unextendable, and unconstrained movement. This limits the kinematic capabilities of humanoid robots. In contrast, humans possess versatile athletic abilities—running, jumping, hopping, and finely adjusting gait parameters such as frequency and foot height. In this paper, we investigate solutions to bring such versatility into humanoid locomotion and thereby propose HugWBC: a unified and general humanoid whole-body controller for versatile locomotion. By designing a general command space in the aspect of tasks and behaviors, along with advanced techniques like symmetrical loss and intervention training for learning a whole-body humanoid controlling policy in simulation, HugWBC enables real-world humanoid robots to produce various natural gaits, including walking, jumping, standing, and hopping, with customizable parameters such as frequency, foot swing height, further combined with different body height, waist rotation, and body pitch. Beyond locomotion, HugWBC also supports real-time interventions from external upper-body controllers like teleoperation, enabling loco-manipulation with precision under any locomotive behavior. Extensive experiments validate the high tracking accuracy and robustness of HugWBC with/without upper-body intervention for all commands, and we further provide an in-depth analysis of how the various commands affect humanoid movement and offer insights into the relationships between these commands. To our knowledge, HugWBC is the first humanoid whole-body controller that supports such versatile locomotion behaviors with high robustness and flexibility.

## Content
Locomotion is a fundamental skill for humanoid robots. However, most existing works make locomotion a single, tedious, unextendable, and unconstrained movement. This limits the kinematic capabilities of humanoid robots. In contrast, humans possess versatile athletic abilities—running, jumping, hopping, and finely adjusting gait parameters such as frequency and foot height. In this paper, we investigate solutions to bring such versatility into humanoid locomotion and thereby propose HugWBC: a unified and general humanoid whole-body controller for versatile locomotion. By designing a general command space in the aspect of tasks and behaviors, along with advanced techniques like symmetrical loss and intervention training for learning a whole-body humanoid controlling policy in simulation, HugWBC enables real-world humanoid robots to produce various natural gaits, including walking, jumping, standing, and hopping, with customizable parameters such as frequency, foot swing height, further combined with different body height, waist rotation, and body pitch. Beyond locomotion, HugWBC also supports real-time interventions from external upper-body controllers like teleoperation, enabling loco-manipulation with precision under any locomotive behavior. Extensive experiments validate the high tracking accuracy and robustness of HugWBC with/without upper-body intervention for all commands, and we further provide an in-depth analysis of how the various commands affect humanoid movement and offer insights into the relationships between these commands. To our knowledge, HugWBC is the first humanoid whole-body controller that supports such versatile locomotion behaviors with high robustness and flexibility.

## 개요
로코모션은 휴머노이드 로봇의 기본 기술입니다. 그러나 기존 연구 대부분은 로코모션을 단일하고, 단조롭고, 확장 불가능하며, 제약이 없는 움직임으로 만듭니다. 이는 휴머노이드 로봇의 운동 능력을 제한합니다. 반면, 인간은 달리기, 점프, 깡충깡충 뛰기, 그리고 주파수와 발 높이 같은 보행 매개변수를 미세 조정하는 등 다양한 운동 능력을 가지고 있습니다. 본 논문에서는 이러한 다양성을 휴머노이드 로코모션에 도입하는 솔루션을 연구하고, 그 결과 HugWBC를 제안합니다: 다양한 로코모션을 위한 통합적이고 일반적인 휴머노이드 전신 제어기입니다. 작업 및 행동 측면에서 일반 명령 공간을 설계하고, 시뮬레이션에서 휴머노이드 전신 제어 정책을 학습하기 위한 대칭 손실 및 개입 훈련과 같은 고급 기술을 통해 HugWBC는 실제 휴머노이드 로봇이 걷기, 점프, 서기, 깡충깡충 뛰기를 포함한 다양한 자연스러운 보행을 생성할 수 있게 하며, 주파수, 발 스윙 높이와 같은 사용자 정의 가능한 매개변수와 함께 다양한 신체 높이, 허리 회전, 몸통 기울기를 결합할 수 있습니다. 로코모션 외에도 HugWBC는 원격 조작과 같은 외부 상체 제어기의 실시간 개입을 지원하여 모든 로코모션 동작 하에서 정밀한 로코-조작을 가능하게 합니다. 광범위한 실험을 통해 상체 개입 유무에 관계없이 모든 명령에 대한 HugWBC의 높은 추적 정확도와 견고성을 검증했으며, 다양한 명령이 휴머노이드 움직임에 미치는 영향에 대한 심층 분석과 명령 간 관계에 대한 통찰력을 제공합니다. 우리가 아는 한, HugWBC는 높은 견고성과 유연성을 갖춘 이러한 다양한 로코모션 동작을 지원하는 최초의 휴머노이드 전신 제어기입니다.

## 핵심 내용
로코모션은 휴머노이드 로봇의 기본 기술입니다. 그러나 기존 연구 대부분은 로코모션을 단일하고, 단조롭고, 확장 불가능하며, 제약이 없는 움직임으로 만듭니다. 이는 휴머노이드 로봇의 운동 능력을 제한합니다. 반면, 인간은 달리기, 점프, 깡충깡충 뛰기, 그리고 주파수와 발 높이 같은 보행 매개변수를 미세 조정하는 등 다양한 운동 능력을 가지고 있습니다. 본 논문에서는 이러한 다양성을 휴머노이드 로코모션에 도입하는 솔루션을 연구하고, 그 결과 HugWBC를 제안합니다: 다양한 로코모션을 위한 통합적이고 일반적인 휴머노이드 전신 제어기입니다. 작업 및 행동 측면에서 일반 명령 공간을 설계하고, 시뮬레이션에서 휴머노이드 전신 제어 정책을 학습하기 위한 대칭 손실 및 개입 훈련과 같은 고급 기술을 통해 HugWBC는 실제 휴머노이드 로봇이 걷기, 점프, 서기, 깡충깡충 뛰기를 포함한 다양한 자연스러운 보행을 생성할 수 있게 하며, 주파수, 발 스윙 높이와 같은 사용자 정의 가능한 매개변수와 함께 다양한 신체 높이, 허리 회전, 몸통 기울기를 결합할 수 있습니다. 로코모션 외에도 HugWBC는 원격 조작과 같은 외부 상체 제어기의 실시간 개입을 지원하여 모든 로코모션 동작 하에서 정밀한 로코-조작을 가능하게 합니다. 광범위한 실험을 통해 상체 개입 유무에 관계없이 모든 명령에 대한 HugWBC의 높은 추적 정확도와 견고성을 검증했으며, 다양한 명령이 휴머노이드 움직임에 미치는 영향에 대한 심층 분석과 명령 간 관계에 대한 통찰력을 제공합니다. 우리가 아는 한, HugWBC는 높은 견고성과 유연성을 갖춘 이러한 다양한 로코모션 동작을 지원하는 최초의 휴머노이드 전신 제어기입니다.
