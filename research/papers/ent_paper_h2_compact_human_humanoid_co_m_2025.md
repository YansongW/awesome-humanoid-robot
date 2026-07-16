---
$id: ent_paper_h2_compact_human_humanoid_co_m_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'H2-COMPACT: Human-Humanoid Co-Manipulation via Adaptive Contact Trajectory Policies'
  zh: 'H2-COMPACT: Human-Humanoid Co-Manipulation via Adaptive Contact Trajectory Policies'
  ko: 'H2-COMPACT: Human-Humanoid Co-Manipulation via Adaptive Contact Trajectory Policies'
summary:
  en: 'H2-COMPACT: Human-Humanoid Co-Manipulation via Adaptive Contact Trajectory Policies is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: 'H2-COMPACT: Human-Humanoid Co-Manipulation via Adaptive Contact Trajectory Policies is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  ko: 'H2-COMPACT: Human-Humanoid Co-Manipulation via Adaptive Contact Trajectory Policies is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- h2_compact
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.17627v1.
sources:
- id: src_001
  type: website
  title: 'H2-COMPACT: Human-Humanoid Co-Manipulation via Adaptive Contact Trajectory Policies project page'
  url: https://h2compact.github.io/h2compact/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We present a hierarchical policy-learning framework that enables a legged humanoid to cooperatively carry extended loads with a human partner using only haptic cues for intent inference. At the upper tier, a lightweight behavior-cloning network consumes six-axis force/torque streams from dual wrist-mounted sensors and outputs whole-body planar velocity commands that capture the leader's applied forces. At the lower tier, a deep-reinforcement-learning policy, trained under randomized payloads (0-3 kg) and friction conditions in Isaac Gym and validated in MuJoCo and on a real Unitree G1, maps these high-level twists to stable, under-load joint trajectories. By decoupling intent interpretation (force -> velocity) from legged locomotion (velocity -> joints), our method combines intuitive responsiveness to human inputs with robust, load-adaptive walking. We collect training data without motion-capture or markers, only synchronized RGB video and F/T readings, employing SAM2 and WHAM to extract 3D human pose and velocity. In real-world trials, our humanoid achieves cooperative carry-and-move performance (completion time, trajectory deviation, velocity synchrony, and follower-force) on par with a blindfolded human-follower baseline. This work is the first to demonstrate learned haptic guidance fused with full-body legged control for fluid human-humanoid co-manipulation. Code and videos are available on the H2-COMPACT website.

## 核心内容
We present a hierarchical policy-learning framework that enables a legged humanoid to cooperatively carry extended loads with a human partner using only haptic cues for intent inference. At the upper tier, a lightweight behavior-cloning network consumes six-axis force/torque streams from dual wrist-mounted sensors and outputs whole-body planar velocity commands that capture the leader's applied forces. At the lower tier, a deep-reinforcement-learning policy, trained under randomized payloads (0-3 kg) and friction conditions in Isaac Gym and validated in MuJoCo and on a real Unitree G1, maps these high-level twists to stable, under-load joint trajectories. By decoupling intent interpretation (force -> velocity) from legged locomotion (velocity -> joints), our method combines intuitive responsiveness to human inputs with robust, load-adaptive walking. We collect training data without motion-capture or markers, only synchronized RGB video and F/T readings, employing SAM2 and WHAM to extract 3D human pose and velocity. In real-world trials, our humanoid achieves cooperative carry-and-move performance (completion time, trajectory deviation, velocity synchrony, and follower-force) on par with a blindfolded human-follower baseline. This work is the first to demonstrate learned haptic guidance fused with full-body legged control for fluid human-humanoid co-manipulation. Code and videos are available on the H2-COMPACT website.

## 参考
- http://arxiv.org/abs/2505.17627v1

## Overview
We present a hierarchical policy-learning framework that enables a legged humanoid to cooperatively carry extended loads with a human partner using only haptic cues for intent inference. At the upper tier, a lightweight behavior-cloning network consumes six-axis force/torque streams from dual wrist-mounted sensors and outputs whole-body planar velocity commands that capture the leader's applied forces. At the lower tier, a deep-reinforcement-learning policy, trained under randomized payloads (0-3 kg) and friction conditions in Isaac Gym and validated in MuJoCo and on a real Unitree G1, maps these high-level twists to stable, under-load joint trajectories. By decoupling intent interpretation (force -> velocity) from legged locomotion (velocity -> joints), our method combines intuitive responsiveness to human inputs with robust, load-adaptive walking. We collect training data without motion-capture or markers, only synchronized RGB video and F/T readings, employing SAM2 and WHAM to extract 3D human pose and velocity. In real-world trials, our humanoid achieves cooperative carry-and-move performance (completion time, trajectory deviation, velocity synchrony, and follower-force) on par with a blindfolded human-follower baseline. This work is the first to demonstrate learned haptic guidance fused with full-body legged control for fluid human-humanoid co-manipulation. Code and videos are available on the H2-COMPACT website.

## Content
We present a hierarchical policy-learning framework that enables a legged humanoid to cooperatively carry extended loads with a human partner using only haptic cues for intent inference. At the upper tier, a lightweight behavior-cloning network consumes six-axis force/torque streams from dual wrist-mounted sensors and outputs whole-body planar velocity commands that capture the leader's applied forces. At the lower tier, a deep-reinforcement-learning policy, trained under randomized payloads (0-3 kg) and friction conditions in Isaac Gym and validated in MuJoCo and on a real Unitree G1, maps these high-level twists to stable, under-load joint trajectories. By decoupling intent interpretation (force -> velocity) from legged locomotion (velocity -> joints), our method combines intuitive responsiveness to human inputs with robust, load-adaptive walking. We collect training data without motion-capture or markers, only synchronized RGB video and F/T readings, employing SAM2 and WHAM to extract 3D human pose and velocity. In real-world trials, our humanoid achieves cooperative carry-and-move performance (completion time, trajectory deviation, velocity synchrony, and follower-force) on par with a blindfolded human-follower baseline. This work is the first to demonstrate learned haptic guidance fused with full-body legged control for fluid human-humanoid co-manipulation. Code and videos are available on the H2-COMPACT website.

## 개요
본 연구에서는 촉각 신호만을 이용하여 의도를 추론함으로써, 보행형 휴머노이드가 인간 파트너와 협력하여 긴 물체를 운반할 수 있도록 하는 계층적 정책 학습 프레임워크를 제시합니다. 상위 계층에서는 가벼운 행동 복제 네트워크가 양쪽 손목에 장착된 센서로부터 6축 힘/토크 데이터를 입력받아, 리더가 가하는 힘을 반영하는 전신 평면 속도 명령을 출력합니다. 하위 계층에서는 Isaac Gym에서 무작위화된 페이로드(0-3kg) 및 마찰 조건 하에 훈련되고 MuJoCo 및 실제 Unitree G1에서 검증된 심층 강화 학습 정책이 이러한 고수준 회전 명령을 안정적이고 하중을 견디는 관절 궤적으로 매핑합니다. 의도 해석(힘 -> 속도)과 보행 운동(속도 -> 관절)을 분리함으로써, 본 방법은 인간 입력에 대한 직관적인 반응성과 하중에 적응하는 강건한 보행을 결합합니다. 모션 캡처나 마커 없이 동기화된 RGB 비디오와 F/T 데이터만으로 훈련 데이터를 수집하며, SAM2와 WHAM을 사용하여 3D 인간 자세와 속도를 추출합니다. 실제 실험에서, 우리의 휴머노이드는 완료 시간, 궤적 편차, 속도 동기화 및 추종자 힘 측면에서 눈을 가린 인간 추종자 기준과 동등한 협력적 운반 및 이동 성능을 달성했습니다. 이 연구는 학습된 촉각 안내와 전신 보행 제어를 융합하여 원활한 인간-휴머노이드 공동 조작을 최초로 시연한 것입니다. 코드와 비디오는 H2-COMPACT 웹사이트에서 확인할 수 있습니다.

## 핵심 내용
본 연구에서는 촉각 신호만을 이용하여 의도를 추론함으로써, 보행형 휴머노이드가 인간 파트너와 협력하여 긴 물체를 운반할 수 있도록 하는 계층적 정책 학습 프레임워크를 제시합니다. 상위 계층에서는 가벼운 행동 복제 네트워크가 양쪽 손목에 장착된 센서로부터 6축 힘/토크 데이터를 입력받아, 리더가 가하는 힘을 반영하는 전신 평면 속도 명령을 출력합니다. 하위 계층에서는 Isaac Gym에서 무작위화된 페이로드(0-3kg) 및 마찰 조건 하에 훈련되고 MuJoCo 및 실제 Unitree G1에서 검증된 심층 강화 학습 정책이 이러한 고수준 회전 명령을 안정적이고 하중을 견디는 관절 궤적으로 매핑합니다. 의도 해석(힘 -> 속도)과 보행 운동(속도 -> 관절)을 분리함으로써, 본 방법은 인간 입력에 대한 직관적인 반응성과 하중에 적응하는 강건한 보행을 결합합니다. 모션 캡처나 마커 없이 동기화된 RGB 비디오와 F/T 데이터만으로 훈련 데이터를 수집하며, SAM2와 WHAM을 사용하여 3D 인간 자세와 속도를 추출합니다. 실제 실험에서, 우리의 휴머노이드는 완료 시간, 궤적 편차, 속도 동기화 및 추종자 힘 측면에서 눈을 가린 인간 추종자 기준과 동등한 협력적 운반 및 이동 성능을 달성했습니다. 이 연구는 학습된 촉각 안내와 전신 보행 제어를 융합하여 원활한 인간-휴머노이드 공동 조작을 최초로 시연한 것입니다. 코드와 비디오는 H2-COMPACT 웹사이트에서 확인할 수 있습니다.
