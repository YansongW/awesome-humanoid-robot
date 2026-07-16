---
$id: ent_paper_contrastive_representation_lea_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Contrastive Representation Learning for Robust Sim-to-Real Transfer of Adaptive Humanoid Locomotion
  zh: Contrastive Representation Learning for Robust Sim-to-Real Transfer of Adaptive Humanoid Locomotion
  ko: Contrastive Representation Learning for Robust Sim-to-Real Transfer of Adaptive Humanoid Locomotion
summary:
  en: Contrastive Representation Learning for Robust Sim-to-Real Transfer of Adaptive Humanoid Locomotion is a 2025 work on
    sim-to-real for humanoid robots.
  zh: Contrastive Representation Learning for Robust Sim-to-Real Transfer of Adaptive Humanoid Locomotion is a 2025 work on
    sim-to-real for humanoid robots.
  ko: Contrastive Representation Learning for Robust Sim-to-Real Transfer of Adaptive Humanoid Locomotion is a 2025 work on
    sim-to-real for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- contrastive_representation_lea
- humanoid
- sim_to_real
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.12858v1.
sources:
- id: src_001
  type: paper
  title: Contrastive Representation Learning for Robust Sim-to-Real Transfer of Adaptive Humanoid Locomotion (arXiv)
  url: https://arxiv.org/abs/2509.12858
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Reinforcement learning has produced remarkable advances in humanoid locomotion, yet a fundamental dilemma persists for real-world deployment: policies must choose between the robustness of reactive proprioceptive control or the proactivity of complex, fragile perception-driven systems. This paper resolves this dilemma by introducing a paradigm that imbues a purely proprioceptive policy with proactive capabilities, achieving the foresight of perception without its deployment-time costs. Our core contribution is a contrastive learning framework that compels the actor's latent state to encode privileged environmental information from simulation. Crucially, this ``distilled awareness" empowers an adaptive gait clock, allowing the policy to proactively adjust its rhythm based on an inferred understanding of the terrain. This synergy resolves the classic trade-off between rigid, clocked gaits and unstable clock-free policies. We validate our approach with zero-shot sim-to-real transfer to a full-sized humanoid, demonstrating highly robust locomotion over challenging terrains, including 30 cm high steps and 26.5° slopes, proving the effectiveness of our method. Website: https://lu-yidan.github.io/cra-loco.

## 核心内容
Reinforcement learning has produced remarkable advances in humanoid locomotion, yet a fundamental dilemma persists for real-world deployment: policies must choose between the robustness of reactive proprioceptive control or the proactivity of complex, fragile perception-driven systems. This paper resolves this dilemma by introducing a paradigm that imbues a purely proprioceptive policy with proactive capabilities, achieving the foresight of perception without its deployment-time costs. Our core contribution is a contrastive learning framework that compels the actor's latent state to encode privileged environmental information from simulation. Crucially, this ``distilled awareness" empowers an adaptive gait clock, allowing the policy to proactively adjust its rhythm based on an inferred understanding of the terrain. This synergy resolves the classic trade-off between rigid, clocked gaits and unstable clock-free policies. We validate our approach with zero-shot sim-to-real transfer to a full-sized humanoid, demonstrating highly robust locomotion over challenging terrains, including 30 cm high steps and 26.5° slopes, proving the effectiveness of our method. Website: https://lu-yidan.github.io/cra-loco.

## 参考
- http://arxiv.org/abs/2509.12858v1

## Overview
Reinforcement learning has produced remarkable advances in humanoid locomotion, yet a fundamental dilemma persists for real-world deployment: policies must choose between the robustness of reactive proprioceptive control or the proactivity of complex, fragile perception-driven systems. This paper resolves this dilemma by introducing a paradigm that imbues a purely proprioceptive policy with proactive capabilities, achieving the foresight of perception without its deployment-time costs. Our core contribution is a contrastive learning framework that compels the actor's latent state to encode privileged environmental information from simulation. Crucially, this ``distilled awareness" empowers an adaptive gait clock, allowing the policy to proactively adjust its rhythm based on an inferred understanding of the terrain. This synergy resolves the classic trade-off between rigid, clocked gaits and unstable clock-free policies. We validate our approach with zero-shot sim-to-real transfer to a full-sized humanoid, demonstrating highly robust locomotion over challenging terrains, including 30 cm high steps and 26.5° slopes, proving the effectiveness of our method. Website: https://lu-yidan.github.io/cra-loco.

## Content
Reinforcement learning has produced remarkable advances in humanoid locomotion, yet a fundamental dilemma persists for real-world deployment: policies must choose between the robustness of reactive proprioceptive control or the proactivity of complex, fragile perception-driven systems. This paper resolves this dilemma by introducing a paradigm that imbues a purely proprioceptive policy with proactive capabilities, achieving the foresight of perception without its deployment-time costs. Our core contribution is a contrastive learning framework that compels the actor's latent state to encode privileged environmental information from simulation. Crucially, this ``distilled awareness" empowers an adaptive gait clock, allowing the policy to proactively adjust its rhythm based on an inferred understanding of the terrain. This synergy resolves the classic trade-off between rigid, clocked gaits and unstable clock-free policies. We validate our approach with zero-shot sim-to-real transfer to a full-sized humanoid, demonstrating highly robust locomotion over challenging terrains, including 30 cm high steps and 26.5° slopes, proving the effectiveness of our method. Website: https://lu-yidan.github.io/cra-loco.

## 개요
강화 학습은 인간형 보행에서 놀라운 발전을 이루었지만, 실제 환경 배포에는 근본적인 딜레마가 존재합니다. 정책은 반응적 고유수용성 제어의 견고성과 복잡하고 취약한 인식 기반 시스템의 사전 대응성 사이에서 선택해야 합니다. 본 논문은 순수 고유수용성 정책에 사전 대응 능력을 부여하는 패러다임을 도입하여, 배포 시점의 비용 없이 인식의 예측력을 달성함으로써 이 딜레마를 해결합니다. 핵심 기여는 대조 학습 프레임워크로, 행위자의 잠재 상태가 시뮬레이션의 특권 환경 정보를 인코딩하도록 강제합니다. 결정적으로, 이 "증류된 인식"은 적응형 보행 시계를 가능하게 하여, 정책이 추론된 지형 이해를 기반으로 리듬을 사전에 조정할 수 있게 합니다. 이러한 시너지는 경직된 시계 기반 보행과 불안정한 시계 없는 정책 간의 고전적 트레이드오프를 해결합니다. 우리는 접근 방식을 전체 크기 인간형 로봇에 제로샷 시뮬레이션-실제 전이로 검증하여, 30cm 높이의 계단과 26.5° 경사를 포함한 도전적인 지형에서 매우 견고한 보행을 입증함으로써 방법의 효과를 증명합니다. 웹사이트: https://lu-yidan.github.io/cra-loco.

## 핵심 내용
강화 학습은 인간형 보행에서 놀라운 발전을 이루었지만, 실제 환경 배포에는 근본적인 딜레마가 존재합니다. 정책은 반응적 고유수용성 제어의 견고성과 복잡하고 취약한 인식 기반 시스템의 사전 대응성 사이에서 선택해야 합니다. 본 논문은 순수 고유수용성 정책에 사전 대응 능력을 부여하는 패러다임을 도입하여, 배포 시점의 비용 없이 인식의 예측력을 달성함으로써 이 딜레마를 해결합니다. 핵심 기여는 대조 학습 프레임워크로, 행위자의 잠재 상태가 시뮬레이션의 특권 환경 정보를 인코딩하도록 강제합니다. 결정적으로, 이 "증류된 인식"은 적응형 보행 시계를 가능하게 하여, 정책이 추론된 지형 이해를 기반으로 리듬을 사전에 조정할 수 있게 합니다. 이러한 시너지는 경직된 시계 기반 보행과 불안정한 시계 없는 정책 간의 고전적 트레이드오프를 해결합니다. 우리는 접근 방식을 전체 크기 인간형 로봇에 제로샷 시뮬레이션-실제 전이로 검증하여, 30cm 높이의 계단과 26.5° 경사를 포함한 도전적인 지형에서 매우 견고한 보행을 입증함으로써 방법의 효과를 증명합니다. 웹사이트: https://lu-yidan.github.io/cra-loco.
