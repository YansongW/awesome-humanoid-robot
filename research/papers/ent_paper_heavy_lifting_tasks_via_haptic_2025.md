---
$id: ent_paper_heavy_lifting_tasks_via_haptic_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Heavy lifting tasks via haptic teleoperation of a wheeled humanoid
  zh: Heavy lifting tasks via haptic teleoperation of a wheeled humanoid
  ko: Heavy lifting tasks via haptic teleoperation of a wheeled humanoid
summary:
  en: Heavy lifting tasks via haptic teleoperation of a wheeled humanoid is a 2025 work on teleoperation for humanoid robots.
  zh: Heavy lifting tasks via haptic teleoperation of a wheeled humanoid is a 2025 work on teleoperation for humanoid robots.
  ko: Heavy lifting tasks via haptic teleoperation of a wheeled humanoid is a 2025 work on teleoperation for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- heavy_lifting_tasks_via_haptic
- humanoid
- teleoperation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.19530v1.
sources:
- id: src_001
  type: paper
  title: Heavy lifting tasks via haptic teleoperation of a wheeled humanoid (arXiv)
  url: https://arxiv.org/abs/2505.19530
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots can support human workers in physically demanding environments by performing tasks that require whole-body coordination, such as lifting and transporting heavy objects.These tasks, which we refer to as Dynamic Mobile Manipulation (DMM), require the simultaneous control of locomotion, manipulation, and posture under dynamic interaction forces. This paper presents a teleoperation framework for DMM on a height-adjustable wheeled humanoid robot for carrying heavy payloads. A Human-Machine Interface (HMI) enables whole-body motion retargeting from the human pilot to the robot by capturing the motion of the human and applying haptic feedback. The pilot uses body motion to regulate robot posture and locomotion, while arm movements guide manipulation.Real time haptic feedback delivers end effector wrenches and balance related cues, closing the loop between human perception and robot environment interaction. We evaluate the different telelocomotion mappings that offer varying levels of balance assistance, allowing the pilot to either manually or automatically regulate the robot's lean in response to payload-induced disturbances. The system is validated in experiments involving dynamic lifting of barbells and boxes up to 2.5 kg (21% of robot mass), demonstrating coordinated whole-body control, height variation, and disturbance handling under pilot guidance. Video demo can be found at: https://youtu.be/jF270_bG1h8?feature=shared

## 核心内容
Humanoid robots can support human workers in physically demanding environments by performing tasks that require whole-body coordination, such as lifting and transporting heavy objects.These tasks, which we refer to as Dynamic Mobile Manipulation (DMM), require the simultaneous control of locomotion, manipulation, and posture under dynamic interaction forces. This paper presents a teleoperation framework for DMM on a height-adjustable wheeled humanoid robot for carrying heavy payloads. A Human-Machine Interface (HMI) enables whole-body motion retargeting from the human pilot to the robot by capturing the motion of the human and applying haptic feedback. The pilot uses body motion to regulate robot posture and locomotion, while arm movements guide manipulation.Real time haptic feedback delivers end effector wrenches and balance related cues, closing the loop between human perception and robot environment interaction. We evaluate the different telelocomotion mappings that offer varying levels of balance assistance, allowing the pilot to either manually or automatically regulate the robot's lean in response to payload-induced disturbances. The system is validated in experiments involving dynamic lifting of barbells and boxes up to 2.5 kg (21% of robot mass), demonstrating coordinated whole-body control, height variation, and disturbance handling under pilot guidance. Video demo can be found at: https://youtu.be/jF270_bG1h8?feature=shared

## 参考
- http://arxiv.org/abs/2505.19530v1

## Overview
Humanoid robots can support human workers in physically demanding environments by performing tasks that require whole-body coordination, such as lifting and transporting heavy objects. These tasks, which we refer to as Dynamic Mobile Manipulation (DMM), require the simultaneous control of locomotion, manipulation, and posture under dynamic interaction forces. This paper presents a teleoperation framework for DMM on a height-adjustable wheeled humanoid robot for carrying heavy payloads. A Human-Machine Interface (HMI) enables whole-body motion retargeting from the human pilot to the robot by capturing the motion of the human and applying haptic feedback. The pilot uses body motion to regulate robot posture and locomotion, while arm movements guide manipulation. Real-time haptic feedback delivers end effector wrenches and balance-related cues, closing the loop between human perception and robot environment interaction. We evaluate different telelocomotion mappings that offer varying levels of balance assistance, allowing the pilot to either manually or automatically regulate the robot's lean in response to payload-induced disturbances. The system is validated in experiments involving dynamic lifting of barbells and boxes up to 2.5 kg (21% of robot mass), demonstrating coordinated whole-body control, height variation, and disturbance handling under pilot guidance. A video demo can be found at: https://youtu.be/jF270_bG1h8?feature=shared

## Content
Humanoid robots can support human workers in physically demanding environments by performing tasks that require whole-body coordination, such as lifting and transporting heavy objects. These tasks, which we refer to as Dynamic Mobile Manipulation (DMM), require the simultaneous control of locomotion, manipulation, and posture under dynamic interaction forces. This paper presents a teleoperation framework for DMM on a height-adjustable wheeled humanoid robot for carrying heavy payloads. A Human-Machine Interface (HMI) enables whole-body motion retargeting from the human pilot to the robot by capturing the motion of the human and applying haptic feedback. The pilot uses body motion to regulate robot posture and locomotion, while arm movements guide manipulation. Real-time haptic feedback delivers end effector wrenches and balance-related cues, closing the loop between human perception and robot environment interaction. We evaluate different telelocomotion mappings that offer varying levels of balance assistance, allowing the pilot to either manually or automatically regulate the robot's lean in response to payload-induced disturbances. The system is validated in experiments involving dynamic lifting of barbells and boxes up to 2.5 kg (21% of robot mass), demonstrating coordinated whole-body control, height variation, and disturbance handling under pilot guidance. A video demo can be found at: https://youtu.be/jF270_bG1h8?feature=shared

## 개요
휴머노이드 로봇은 무거운 물체를 들어 올리거나 운반하는 등 전신 협응이 필요한 작업을 수행함으로써 육체적으로 힘든 환경에서 인간 작업자를 지원할 수 있습니다. 이러한 작업을 동적 이동 조작(DMM)이라고 하며, 동적 상호작용 힘 하에서 이동, 조작 및 자세를 동시에 제어해야 합니다. 본 논문은 무거운 페이로드를 운반하기 위한 높이 조절 가능한 바퀴형 휴머노이드 로봇에서 DMM을 위한 원격 조작 프레임워크를 제시합니다. 인간-기계 인터페이스(HMI)는 인간의 움직임을 포착하고 햅틱 피드백을 적용하여 인간 조종사에서 로봇으로의 전신 동작 재타겟팅을 가능하게 합니다. 조종사는 신체 움직임을 사용하여 로봇의 자세와 이동을 조절하고, 팔 움직임은 조작을 안내합니다. 실시간 햅틱 피드백은 엔드 이펙터의 힘과 균형 관련 신호를 전달하여 인간의 인지와 로봇 환경 상호작용 간의 루프를 닫습니다. 우리는 다양한 수준의 균형 지원을 제공하는 여러 원격 이동 매핑을 평가하여, 조종사가 페이로드로 인한 교란에 대응하여 로봇의 기울기를 수동 또는 자동으로 조절할 수 있도록 합니다. 시스템은 최대 2.5kg(로봇 질량의 21%)의 바벨과 상자를 동적으로 들어 올리는 실험을 통해 검증되었으며, 조종사의 안내 하에 협응된 전신 제어, 높이 변화 및 교란 처리를 입증합니다. 비디오 데모는 다음에서 확인할 수 있습니다: https://youtu.be/jF270_bG1h8?feature=shared

## 핵심 내용
휴머노이드 로봇은 무거운 물체를 들어 올리거나 운반하는 등 전신 협응이 필요한 작업을 수행함으로써 육체적으로 힘든 환경에서 인간 작업자를 지원할 수 있습니다. 이러한 작업을 동적 이동 조작(DMM)이라고 하며, 동적 상호작용 힘 하에서 이동, 조작 및 자세를 동시에 제어해야 합니다. 본 논문은 무거운 페이로드를 운반하기 위한 높이 조절 가능한 바퀴형 휴머노이드 로봇에서 DMM을 위한 원격 조작 프레임워크를 제시합니다. 인간-기계 인터페이스(HMI)는 인간의 움직임을 포착하고 햅틱 피드백을 적용하여 인간 조종사에서 로봇으로의 전신 동작 재타겟팅을 가능하게 합니다. 조종사는 신체 움직임을 사용하여 로봇의 자세와 이동을 조절하고, 팔 움직임은 조작을 안내합니다. 실시간 햅틱 피드백은 엔드 이펙터의 힘과 균형 관련 신호를 전달하여 인간의 인지와 로봇 환경 상호작용 간의 루프를 닫습니다. 우리는 다양한 수준의 균형 지원을 제공하는 여러 원격 이동 매핑을 평가하여, 조종사가 페이로드로 인한 교란에 대응하여 로봇의 기울기를 수동 또는 자동으로 조절할 수 있도록 합니다. 시스템은 최대 2.5kg(로봇 질량의 21%)의 바벨과 상자를 동적으로 들어 올리는 실험을 통해 검증되었으며, 조종사의 안내 하에 협응된 전신 제어, 높이 변화 및 교란 처리를 입증합니다. 비디오 데모는 다음에서 확인할 수 있습니다: https://youtu.be/jF270_bG1h8?feature=shared
