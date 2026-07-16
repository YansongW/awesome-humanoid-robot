---
$id: ent_paper_learning_human_like_badminton_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Human-Like Badminton Skills for Humanoid Robots
  zh: Learning Human-Like Badminton Skills for Humanoid Robots
  ko: Learning Human-Like Badminton Skills for Humanoid Robots
summary:
  en: Learning Human-Like Badminton Skills for Humanoid Robots is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.
  zh: Learning Human-Like Badminton Skills for Humanoid Robots is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.
  ko: Learning Human-Like Badminton Skills for Humanoid Robots is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- learning_human_like_badminton
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.08370v1.
sources:
- id: src_001
  type: paper
  title: Learning Human-Like Badminton Skills for Humanoid Robots (arXiv)
  url: https://arxiv.org/abs/2602.08370
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Realizing versatile and human-like performance in high-demand sports like badminton remains a formidable challenge for humanoid robotics. Unlike standard locomotion or static manipulation, this task demands a seamless integration of explosive whole-body coordination and precise, timing-critical interception. While recent advances have achieved lifelike motion mimicry, bridging the gap between kinematic imitation and functional, physics-aware striking without compromising stylistic naturalness is non-trivial. To address this, we propose Imitation-to-Interaction, a progressive reinforcement learning framework designed to evolve a robot from a "mimic" to a capable "striker." Our approach establishes a robust motor prior from human data, distills it into a compact, model-based state representation, and stabilizes dynamics via adversarial priors. Crucially, to overcome the sparsity of expert demonstrations, we introduce a manifold expansion strategy that generalizes discrete strike points into a dense interaction volume. We validate our framework through the mastery of diverse skills, including lifts and drop shots, in simulation. Furthermore, we demonstrate the first zero-shot sim-to-real transfer of anthropomorphic badminton skills to a humanoid robot, successfully replicating the kinetic elegance and functional precision of human athletes in the physical world.

## 核心内容
Realizing versatile and human-like performance in high-demand sports like badminton remains a formidable challenge for humanoid robotics. Unlike standard locomotion or static manipulation, this task demands a seamless integration of explosive whole-body coordination and precise, timing-critical interception. While recent advances have achieved lifelike motion mimicry, bridging the gap between kinematic imitation and functional, physics-aware striking without compromising stylistic naturalness is non-trivial. To address this, we propose Imitation-to-Interaction, a progressive reinforcement learning framework designed to evolve a robot from a "mimic" to a capable "striker." Our approach establishes a robust motor prior from human data, distills it into a compact, model-based state representation, and stabilizes dynamics via adversarial priors. Crucially, to overcome the sparsity of expert demonstrations, we introduce a manifold expansion strategy that generalizes discrete strike points into a dense interaction volume. We validate our framework through the mastery of diverse skills, including lifts and drop shots, in simulation. Furthermore, we demonstrate the first zero-shot sim-to-real transfer of anthropomorphic badminton skills to a humanoid robot, successfully replicating the kinetic elegance and functional precision of human athletes in the physical world.

## 参考
- http://arxiv.org/abs/2602.08370v1

## Overview
Realizing versatile and human-like performance in high-demand sports like badminton remains a formidable challenge for humanoid robotics. Unlike standard locomotion or static manipulation, this task demands a seamless integration of explosive whole-body coordination and precise, timing-critical interception. While recent advances have achieved lifelike motion mimicry, bridging the gap between kinematic imitation and functional, physics-aware striking without compromising stylistic naturalness is non-trivial. To address this, we propose Imitation-to-Interaction, a progressive reinforcement learning framework designed to evolve a robot from a "mimic" to a capable "striker." Our approach establishes a robust motor prior from human data, distills it into a compact, model-based state representation, and stabilizes dynamics via adversarial priors. Crucially, to overcome the sparsity of expert demonstrations, we introduce a manifold expansion strategy that generalizes discrete strike points into a dense interaction volume. We validate our framework through the mastery of diverse skills, including lifts and drop shots, in simulation. Furthermore, we demonstrate the first zero-shot sim-to-real transfer of anthropomorphic badminton skills to a humanoid robot, successfully replicating the kinetic elegance and functional precision of human athletes in the physical world.

## Content
Realizing versatile and human-like performance in high-demand sports like badminton remains a formidable challenge for humanoid robotics. Unlike standard locomotion or static manipulation, this task demands a seamless integration of explosive whole-body coordination and precise, timing-critical interception. While recent advances have achieved lifelike motion mimicry, bridging the gap between kinematic imitation and functional, physics-aware striking without compromising stylistic naturalness is non-trivial. To address this, we propose Imitation-to-Interaction, a progressive reinforcement learning framework designed to evolve a robot from a "mimic" to a capable "striker." Our approach establishes a robust motor prior from human data, distills it into a compact, model-based state representation, and stabilizes dynamics via adversarial priors. Crucially, to overcome the sparsity of expert demonstrations, we introduce a manifold expansion strategy that generalizes discrete strike points into a dense interaction volume. We validate our framework through the mastery of diverse skills, including lifts and drop shots, in simulation. Furthermore, we demonstrate the first zero-shot sim-to-real transfer of anthropomorphic badminton skills to a humanoid robot, successfully replicating the kinetic elegance and functional precision of human athletes in the physical world.

## 개요
배드민턴과 같은 고난도 스포츠에서 다재다능하고 인간다운 성능을 구현하는 것은 휴머노이드 로봇 공학에게 여전히 어려운 과제입니다. 표준적인 보행이나 정적 조작과 달리, 이 작업은 폭발적인 전신 협응과 정밀하고 타이밍이 중요한 차단 동작의 완벽한 통합을 요구합니다. 최근의 발전이 생생한 동작 모방을 달성했지만, 운동학적 모방과 기능적이고 물리학을 인식한 타격 사이의 간극을 스타일의 자연스러움을 희생하지 않고 메우는 것은 쉽지 않습니다. 이를 해결하기 위해, 우리는 로봇을 '모방자'에서 유능한 '타격자'로 진화시키도록 설계된 점진적 강화 학습 프레임워크인 Imitation-to-Interaction을 제안합니다. 우리의 접근 방식은 인간 데이터로부터 강건한 운동 사전 지식을 구축하고, 이를 컴팩트한 모델 기반 상태 표현으로 증류하며, 적대적 사전 지식을 통해 동역학을 안정화합니다. 결정적으로, 전문가 시연의 희소성을 극복하기 위해, 우리는 이산적인 타격 지점을 밀집된 상호작용 공간으로 일반화하는 다양체 확장 전략을 도입합니다. 우리는 시뮬레이션에서 리프트와 드롭샷을 포함한 다양한 기술의 숙달을 통해 프레임워크를 검증합니다. 또한, 우리는 인간형 로봇에 대한 의인화된 배드민턴 기술의 최초의 제로샷 시뮬레이션-실제 전이를 시연하여, 물리적 세계에서 인간 운동선수의 운동학적 우아함과 기능적 정밀성을 성공적으로 재현합니다.

## 핵심 내용
배드민턴과 같은 고난도 스포츠에서 다재다능하고 인간다운 성능을 구현하는 것은 휴머노이드 로봇 공학에게 여전히 어려운 과제입니다. 표준적인 보행이나 정적 조작과 달리, 이 작업은 폭발적인 전신 협응과 정밀하고 타이밍이 중요한 차단 동작의 완벽한 통합을 요구합니다. 최근의 발전이 생생한 동작 모방을 달성했지만, 운동학적 모방과 기능적이고 물리학을 인식한 타격 사이의 간극을 스타일의 자연스러움을 희생하지 않고 메우는 것은 쉽지 않습니다. 이를 해결하기 위해, 우리는 로봇을 '모방자'에서 유능한 '타격자'로 진화시키도록 설계된 점진적 강화 학습 프레임워크인 Imitation-to-Interaction을 제안합니다. 우리의 접근 방식은 인간 데이터로부터 강건한 운동 사전 지식을 구축하고, 이를 컴팩트한 모델 기반 상태 표현으로 증류하며, 적대적 사전 지식을 통해 동역학을 안정화합니다. 결정적으로, 전문가 시연의 희소성을 극복하기 위해, 우리는 이산적인 타격 지점을 밀집된 상호작용 공간으로 일반화하는 다양체 확장 전략을 도입합니다. 우리는 시뮬레이션에서 리프트와 드롭샷을 포함한 다양한 기술의 숙달을 통해 프레임워크를 검증합니다. 또한, 우리는 인간형 로봇에 대한 의인화된 배드민턴 기술의 최초의 제로샷 시뮬레이션-실제 전이를 시연하여, 물리적 세계에서 인간 운동선수의 운동학적 우아함과 기능적 정밀성을 성공적으로 재현합니다.
