---
$id: ent_paper_bytewrist_a_parallel_robotic_w_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ByteWrist: A Parallel Robotic Wrist Enabling Flexible and Anthropomorphic Motion for Confined Spaces'
  zh: 'ByteWrist: A Parallel Robotic Wrist Enabling Flexible and Anthropomorphic Motion for Confined Spaces'
  ko: 'ByteWrist: A Parallel Robotic Wrist Enabling Flexible and Anthropomorphic Motion for Confined Spaces'
summary:
  en: 'ByteWrist: A Parallel Robotic Wrist Enabling Flexible and Anthropomorphic Motion for Confined Spaces is a 2026 work
    on hardware design for humanoid robots.'
  zh: 'ByteWrist: A Parallel Robotic Wrist Enabling Flexible and Anthropomorphic Motion for Confined Spaces is a 2026 work
    on hardware design for humanoid robots.'
  ko: 'ByteWrist: A Parallel Robotic Wrist Enabling Flexible and Anthropomorphic Motion for Confined Spaces is a 2026 work
    on hardware design for humanoid robots.'
domains:
- 06_design_engineering
- 02_components
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
- system
tags:
- bytewrist
- hardware_design
- humanoid
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.18084v2.
sources:
- id: src_001
  type: website
  title: 'ByteWrist: A Parallel Robotic Wrist Enabling Flexible and Anthropomorphic Motion for Confined Spaces project page'
  url: https://bytewrist.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
This paper introduces ByteWrist, a novel highly-flexible and anthropomorphic parallel wrist for robotic manipulation. ByteWrist addresses the critical limitations of existing serial and parallel wrists in narrow-space operations through a compact three-stage parallel drive mechanism integrated with arc-shaped end linkages. The design achieves precise RPY (Roll-Pitch-Yaw) motion while maintaining exceptional compactness, making it particularly suitable for complex unstructured environments such as home services, medical assistance, and precision assembly. The key innovations include: (1) a nested three-stage motor-driven linkages that minimize volume while enabling independent multi-DOF control, (2) arc-shaped end linkages that optimize force transmission and expand motion range, and (3) a central supporting ball functioning as a spherical joint that enhances structural stiffness without compromising flexibility. Meanwhile, we present comprehensive kinematic modeling including forward / inverse kinematics and a numerical Jacobian solution for precise control. Empirically, we observe ByteWrist demonstrates strong performance in narrow-space maneuverability and dual-arm cooperative manipulation tasks, outperforming Kinova-based systems. Results indicate significant improvements in compactness, efficiency, and stiffness compared to traditional designs, establishing ByteWrist as a promising solution for next-generation robotic manipulation in constrained environments.

## 核心内容
This paper introduces ByteWrist, a novel highly-flexible and anthropomorphic parallel wrist for robotic manipulation. ByteWrist addresses the critical limitations of existing serial and parallel wrists in narrow-space operations through a compact three-stage parallel drive mechanism integrated with arc-shaped end linkages. The design achieves precise RPY (Roll-Pitch-Yaw) motion while maintaining exceptional compactness, making it particularly suitable for complex unstructured environments such as home services, medical assistance, and precision assembly. The key innovations include: (1) a nested three-stage motor-driven linkages that minimize volume while enabling independent multi-DOF control, (2) arc-shaped end linkages that optimize force transmission and expand motion range, and (3) a central supporting ball functioning as a spherical joint that enhances structural stiffness without compromising flexibility. Meanwhile, we present comprehensive kinematic modeling including forward / inverse kinematics and a numerical Jacobian solution for precise control. Empirically, we observe ByteWrist demonstrates strong performance in narrow-space maneuverability and dual-arm cooperative manipulation tasks, outperforming Kinova-based systems. Results indicate significant improvements in compactness, efficiency, and stiffness compared to traditional designs, establishing ByteWrist as a promising solution for next-generation robotic manipulation in constrained environments.

## 参考
- http://arxiv.org/abs/2509.18084v2

## Overview
This paper introduces ByteWrist, a novel highly-flexible and anthropomorphic parallel wrist for robotic manipulation. ByteWrist addresses the critical limitations of existing serial and parallel wrists in narrow-space operations through a compact three-stage parallel drive mechanism integrated with arc-shaped end linkages. The design achieves precise RPY (Roll-Pitch-Yaw) motion while maintaining exceptional compactness, making it particularly suitable for complex unstructured environments such as home services, medical assistance, and precision assembly. The key innovations include: (1) a nested three-stage motor-driven linkages that minimize volume while enabling independent multi-DOF control, (2) arc-shaped end linkages that optimize force transmission and expand motion range, and (3) a central supporting ball functioning as a spherical joint that enhances structural stiffness without compromising flexibility. Meanwhile, we present comprehensive kinematic modeling including forward / inverse kinematics and a numerical Jacobian solution for precise control. Empirically, we observe ByteWrist demonstrates strong performance in narrow-space maneuverability and dual-arm cooperative manipulation tasks, outperforming Kinova-based systems. Results indicate significant improvements in compactness, efficiency, and stiffness compared to traditional designs, establishing ByteWrist as a promising solution for next-generation robotic manipulation in constrained environments.

## Content
This paper introduces ByteWrist, a novel highly-flexible and anthropomorphic parallel wrist for robotic manipulation. ByteWrist addresses the critical limitations of existing serial and parallel wrists in narrow-space operations through a compact three-stage parallel drive mechanism integrated with arc-shaped end linkages. The design achieves precise RPY (Roll-Pitch-Yaw) motion while maintaining exceptional compactness, making it particularly suitable for complex unstructured environments such as home services, medical assistance, and precision assembly. The key innovations include: (1) a nested three-stage motor-driven linkages that minimize volume while enabling independent multi-DOF control, (2) arc-shaped end linkages that optimize force transmission and expand motion range, and (3) a central supporting ball functioning as a spherical joint that enhances structural stiffness without compromising flexibility. Meanwhile, we present comprehensive kinematic modeling including forward / inverse kinematics and a numerical Jacobian solution for precise control. Empirically, we observe ByteWrist demonstrates strong performance in narrow-space maneuverability and dual-arm cooperative manipulation tasks, outperforming Kinova-based systems. Results indicate significant improvements in compactness, efficiency, and stiffness compared to traditional designs, establishing ByteWrist as a promising solution for next-generation robotic manipulation in constrained environments.

## 개요  
본 논문은 로봇 조작을 위한 고유연성 및 인간형 병렬 손목인 ByteWrist를 소개합니다. ByteWrist는 아크형 엔드 링키지와 통합된 컴팩트한 3단 병렬 구동 메커니즘을 통해 기존 직렬 및 병렬 손목이 좁은 공간 작업에서 가지는 주요 한계를 해결합니다. 이 설계는 정밀한 RPY(Roll-Pitch-Yaw) 운동을 구현하면서도 뛰어난 컴팩트성을 유지하여, 가사 서비스, 의료 지원, 정밀 조립과 같은 복잡한 비정형 환경에 특히 적합합니다. 주요 혁신 사항은 다음과 같습니다: (1) 부피를 최소화하면서 독립적인 다자유도 제어를 가능하게 하는 중첩된 3단 모터 구동 링키지, (2) 힘 전달을 최적화하고 운동 범위를 확장하는 아크형 엔드 링키지, (3) 유연성을 저해하지 않으면서 구조적 강성을 향상시키는 구형 관절 역할을 하는 중앙 지지 볼. 또한, 정밀 제어를 위한 순기구학/역기구학 및 수치적 자코비안 해법을 포함한 포괄적인 기구학 모델링을 제시합니다. 실험적으로, ByteWrist는 좁은 공간 기동성 및 이중 팔 협력 조작 작업에서 강력한 성능을 보여주며, Kinova 기반 시스템을 능가하는 것을 관찰했습니다. 결과는 기존 설계 대비 컴팩트성, 효율성 및 강성에서 상당한 개선을 나타내며, ByteWrist가 제한된 환경에서의 차세대 로봇 조작을 위한 유망한 솔루션임을 입증합니다.

## 핵심 내용  
본 논문은 로봇 조작을 위한 고유연성 및 인간형 병렬 손목인 ByteWrist를 소개합니다. ByteWrist는 아크형 엔드 링키지와 통합된 컴팩트한 3단 병렬 구동 메커니즘을 통해 기존 직렬 및 병렬 손목이 좁은 공간 작업에서 가지는 주요 한계를 해결합니다. 이 설계는 정밀한 RPY(Roll-Pitch-Yaw) 운동을 구현하면서도 뛰어난 컴팩트성을 유지하여, 가사 서비스, 의료 지원, 정밀 조립과 같은 복잡한 비정형 환경에 특히 적합합니다. 주요 혁신 사항은 다음과 같습니다: (1) 부피를 최소화하면서 독립적인 다자유도 제어를 가능하게 하는 중첩된 3단 모터 구동 링키지, (2) 힘 전달을 최적화하고 운동 범위를 확장하는 아크형 엔드 링키지, (3) 유연성을 저해하지 않으면서 구조적 강성을 향상시키는 구형 관절 역할을 하는 중앙 지지 볼. 또한, 정밀 제어를 위한 순기구학/역기구학 및 수치적 자코비안 해법을 포함한 포괄적인 기구학 모델링을 제시합니다. 실험적으로, ByteWrist는 좁은 공간 기동성 및 이중 팔 협력 조작 작업에서 강력한 성능을 보여주며, Kinova 기반 시스템을 능가하는 것을 관찰했습니다. 결과는 기존 설계 대비 컴팩트성, 효율성 및 강성에서 상당한 개선을 나타내며, ByteWrist가 제한된 환경에서의 차세대 로봇 조작을 위한 유망한 솔루션임을 입증합니다.
