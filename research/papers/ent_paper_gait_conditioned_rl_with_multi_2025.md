---
$id: ent_paper_gait_conditioned_rl_with_multi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Gait-Conditioned RL with Multi-Phase Curriculum for Humanoid Locomotion
  zh: Gait-Conditioned RL with Multi-Phase Curriculum for Humanoid Locomotion
  ko: Gait-Conditioned RL with Multi-Phase Curriculum for Humanoid Locomotion
summary:
  en: Gait-Conditioned RL with Multi-Phase Curriculum for Humanoid Locomotion is a 2025 work on locomotion for humanoid robots.
  zh: Gait-Conditioned RL with Multi-Phase Curriculum for Humanoid Locomotion is a 2025 work on locomotion for humanoid robots.
  ko: Gait-Conditioned RL with Multi-Phase Curriculum for Humanoid Locomotion is a 2025 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- gait_conditioned_rl_with_multi
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.20619v3.
sources:
- id: src_001
  type: paper
  title: Gait-Conditioned RL with Multi-Phase Curriculum for Humanoid Locomotion (arXiv)
  url: https://arxiv.org/abs/2505.20619
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We present a unified gait-conditioned reinforcement learning framework that enables humanoid robots to perform standing, walking, running, and smooth transitions within a single recurrent policy. A compact reward routing mechanism dynamically activates gait-specific objectives based on a one-hot gait ID, mitigating reward interference and supporting stable multi-gait learning. Human-inspired reward terms promote biomechanically natural motions, such as straight-knee stance and coordinated arm-leg swing, without requiring motion capture data. A structured curriculum progressively introduces gait complexity and expands command space over multiple phases. In simulation, the policy successfully achieves robust standing, walking, running, and gait transitions. On the real Unitree G1 humanoid, we validate standing, walking, and walk-to-stand transitions, demonstrating stable and coordinated locomotion. This work provides a scalable, reference-free solution toward versatile and naturalistic humanoid control across diverse modes and environments.

## 核心内容
We present a unified gait-conditioned reinforcement learning framework that enables humanoid robots to perform standing, walking, running, and smooth transitions within a single recurrent policy. A compact reward routing mechanism dynamically activates gait-specific objectives based on a one-hot gait ID, mitigating reward interference and supporting stable multi-gait learning. Human-inspired reward terms promote biomechanically natural motions, such as straight-knee stance and coordinated arm-leg swing, without requiring motion capture data. A structured curriculum progressively introduces gait complexity and expands command space over multiple phases. In simulation, the policy successfully achieves robust standing, walking, running, and gait transitions. On the real Unitree G1 humanoid, we validate standing, walking, and walk-to-stand transitions, demonstrating stable and coordinated locomotion. This work provides a scalable, reference-free solution toward versatile and naturalistic humanoid control across diverse modes and environments.

## 参考
- http://arxiv.org/abs/2505.20619v3

## Overview
We present a unified gait-conditioned reinforcement learning framework that enables humanoid robots to perform standing, walking, running, and smooth transitions within a single recurrent policy. A compact reward routing mechanism dynamically activates gait-specific objectives based on a one-hot gait ID, mitigating reward interference and supporting stable multi-gait learning. Human-inspired reward terms promote biomechanically natural motions, such as straight-knee stance and coordinated arm-leg swing, without requiring motion capture data. A structured curriculum progressively introduces gait complexity and expands command space over multiple phases. In simulation, the policy successfully achieves robust standing, walking, running, and gait transitions. On the real Unitree G1 humanoid, we validate standing, walking, and walk-to-stand transitions, demonstrating stable and coordinated locomotion. This work provides a scalable, reference-free solution toward versatile and naturalistic humanoid control across diverse modes and environments.

## Content
We present a unified gait-conditioned reinforcement learning framework that enables humanoid robots to perform standing, walking, running, and smooth transitions within a single recurrent policy. A compact reward routing mechanism dynamically activates gait-specific objectives based on a one-hot gait ID, mitigating reward interference and supporting stable multi-gait learning. Human-inspired reward terms promote biomechanically natural motions, such as straight-knee stance and coordinated arm-leg swing, without requiring motion capture data. A structured curriculum progressively introduces gait complexity and expands command space over multiple phases. In simulation, the policy successfully achieves robust standing, walking, running, and gait transitions. On the real Unitree G1 humanoid, we validate standing, walking, and walk-to-stand transitions, demonstrating stable and coordinated locomotion. This work provides a scalable, reference-free solution toward versatile and naturalistic humanoid control across diverse modes and environments.

## 개요
본 논문에서는 단일 순환 정책(recurrent policy) 내에서 인간형 로봇이 서기, 걷기, 달리기 및 부드러운 전환 동작을 수행할 수 있도록 하는 통합 보행 조건 강화 학습 프레임워크를 제시합니다. 간결한 보상 라우팅 메커니즘은 원-핫(one-hot) 보행 ID를 기반으로 보행별 목표를 동적으로 활성화하여 보상 간섭을 완화하고 안정적인 다중 보행 학습을 지원합니다. 인간에서 영감을 받은 보상 항목은 무릎을 편 자세와 팔-다리 협응 스윙과 같은 생체역학적으로 자연스러운 움직임을 촉진하며, 모션 캡처 데이터가 필요하지 않습니다. 구조화된 커리큘럼은 여러 단계에 걸쳐 점진적으로 보행 복잡성을 도입하고 명령 공간을 확장합니다. 시뮬레이션에서 정책은 강건한 서기, 걷기, 달리기 및 보행 전환을 성공적으로 달성합니다. 실제 Unitree G1 인간형 로봇에서는 서기, 걷기 및 걷기에서 서기로의 전환을 검증하여 안정적이고 협응된 보행을 입증합니다. 이 연구는 다양한 모드와 환경에서 다재다능하고 자연스러운 인간형 제어를 위한 확장 가능하고 참조 없는 솔루션을 제공합니다.

## 핵심 내용
본 논문에서는 단일 순환 정책 내에서 인간형 로봇이 서기, 걷기, 달리기 및 부드러운 전환 동작을 수행할 수 있도록 하는 통합 보행 조건 강화 학습 프레임워크를 제시합니다. 간결한 보상 라우팅 메커니즘은 원-핫 보행 ID를 기반으로 보행별 목표를 동적으로 활성화하여 보상 간섭을 완화하고 안정적인 다중 보행 학습을 지원합니다. 인간에서 영감을 받은 보상 항목은 무릎을 편 자세와 팔-다리 협응 스윙과 같은 생체역학적으로 자연스러운 움직임을 촉진하며, 모션 캡처 데이터가 필요하지 않습니다. 구조화된 커리큘럼은 여러 단계에 걸쳐 점진적으로 보행 복잡성을 도입하고 명령 공간을 확장합니다. 시뮬레이션에서 정책은 강건한 서기, 걷기, 달리기 및 보행 전환을 성공적으로 달성합니다. 실제 Unitree G1 인간형 로봇에서는 서기, 걷기 및 걷기에서 서기로의 전환을 검증하여 안정적이고 협응된 보행을 입증합니다. 이 연구는 다양한 모드와 환경에서 다재다능하고 자연스러운 인간형 제어를 위한 확장 가능하고 참조 없는 솔루션을 제공합니다.
