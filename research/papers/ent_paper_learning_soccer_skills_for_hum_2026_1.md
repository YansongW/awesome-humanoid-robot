---
$id: ent_paper_learning_soccer_skills_for_hum_2026_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Learning Soccer Skills for Humanoid Robots:   A Progressive Perception-Action Framework'
  zh: 'Learning Soccer Skills for Humanoid Robots:   A Progressive Perception-Action Framework'
  ko: 'Learning Soccer Skills for Humanoid Robots:   A Progressive Perception-Action Framework'
summary:
  en: 'Learning Soccer Skills for Humanoid Robots: A Progressive Perception-Action Framework is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: 'Learning Soccer Skills for Humanoid Robots: A Progressive Perception-Action Framework is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  ko: 'Learning Soccer Skills for Humanoid Robots: A Progressive Perception-Action Framework is a 2026 work on loco-manipulation
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
- humanoid
- learning_soccer_skills_for_hum
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.05310v1.
sources:
- id: src_001
  type: paper
  title: 'Learning Soccer Skills for Humanoid Robots:   A Progressive Perception-Action Framework (arXiv)'
  url: https://arxiv.org/abs/2602.05310
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Soccer presents a significant challenge for humanoid robots, demanding tightly integrated perception-action capabilities for tasks like perception-guided kicking and whole-body balance control. Existing approaches suffer from inter-module instability in modular pipelines or conflicting training objectives in end-to-end frameworks. We propose Perception-Action integrated Decision-making (PAiD), a progressive architecture that decomposes soccer skill acquisition into three stages: motion-skill acquisition via human motion tracking, lightweight perception-action integration for positional generalization, and physics-aware sim-to-real transfer. This staged decomposition establishes stable foundational skills, avoids reward conflicts during perception integration, and minimizes sim-to-real gaps. Experiments on the Unitree G1 demonstrate high-fidelity human-like kicking with robust performance under diverse conditions-including static or rolling balls, various positions, and disturbances-while maintaining consistent execution across indoor and outdoor scenarios. Our divide-and-conquer strategy advances robust humanoid soccer capabilities and offers a scalable framework for complex embodied skill acquisition. The project page is available at https://soccer-humanoid.github.io/.

## 核心内容
Soccer presents a significant challenge for humanoid robots, demanding tightly integrated perception-action capabilities for tasks like perception-guided kicking and whole-body balance control. Existing approaches suffer from inter-module instability in modular pipelines or conflicting training objectives in end-to-end frameworks. We propose Perception-Action integrated Decision-making (PAiD), a progressive architecture that decomposes soccer skill acquisition into three stages: motion-skill acquisition via human motion tracking, lightweight perception-action integration for positional generalization, and physics-aware sim-to-real transfer. This staged decomposition establishes stable foundational skills, avoids reward conflicts during perception integration, and minimizes sim-to-real gaps. Experiments on the Unitree G1 demonstrate high-fidelity human-like kicking with robust performance under diverse conditions-including static or rolling balls, various positions, and disturbances-while maintaining consistent execution across indoor and outdoor scenarios. Our divide-and-conquer strategy advances robust humanoid soccer capabilities and offers a scalable framework for complex embodied skill acquisition. The project page is available at https://soccer-humanoid.github.io/.

## 参考
- http://arxiv.org/abs/2602.05310v1

## Overview
Soccer presents a significant challenge for humanoid robots, demanding tightly integrated perception-action capabilities for tasks like perception-guided kicking and whole-body balance control. Existing approaches suffer from inter-module instability in modular pipelines or conflicting training objectives in end-to-end frameworks. We propose Perception-Action integrated Decision-making (PAiD), a progressive architecture that decomposes soccer skill acquisition into three stages: motion-skill acquisition via human motion tracking, lightweight perception-action integration for positional generalization, and physics-aware sim-to-real transfer. This staged decomposition establishes stable foundational skills, avoids reward conflicts during perception integration, and minimizes sim-to-real gaps. Experiments on the Unitree G1 demonstrate high-fidelity human-like kicking with robust performance under diverse conditions—including static or rolling balls, various positions, and disturbances—while maintaining consistent execution across indoor and outdoor scenarios. Our divide-and-conquer strategy advances robust humanoid soccer capabilities and offers a scalable framework for complex embodied skill acquisition. The project page is available at https://soccer-humanoid.github.io/.

## Content
Soccer presents a significant challenge for humanoid robots, demanding tightly integrated perception-action capabilities for tasks like perception-guided kicking and whole-body balance control. Existing approaches suffer from inter-module instability in modular pipelines or conflicting training objectives in end-to-end frameworks. We propose Perception-Action integrated Decision-making (PAiD), a progressive architecture that decomposes soccer skill acquisition into three stages: motion-skill acquisition via human motion tracking, lightweight perception-action integration for positional generalization, and physics-aware sim-to-real transfer. This staged decomposition establishes stable foundational skills, avoids reward conflicts during perception integration, and minimizes sim-to-real gaps. Experiments on the Unitree G1 demonstrate high-fidelity human-like kicking with robust performance under diverse conditions—including static or rolling balls, various positions, and disturbances—while maintaining consistent execution across indoor and outdoor scenarios. Our divide-and-conquer strategy advances robust humanoid soccer capabilities and offers a scalable framework for complex embodied skill acquisition. The project page is available at https://soccer-humanoid.github.io/.

## 개요
축구는 인간형 로봇에게 중요한 도전 과제로, 인지 기반 킥 동작 및 전신 균형 제어와 같은 작업을 위해 긴밀하게 통합된 인지-행동 능력을 요구합니다. 기존 접근 방식은 모듈식 파이프라인에서 모듈 간 불안정성이나 종단 간 프레임워크에서 상충되는 훈련 목표로 인해 어려움을 겪습니다. 우리는 축구 기술 습득을 세 단계로 분해하는 점진적 아키텍처인 PAiD(Perception-Action integrated Decision-making)를 제안합니다: 인간 동작 추적을 통한 운동 기술 습득, 위치 일반화를 위한 경량 인지-행동 통합, 물리 인식 시뮬레이션-실제 전환. 이러한 단계적 분해는 안정적인 기초 기술을 확립하고, 인지 통합 중 보상 충돌을 방지하며, 시뮬레이션-실제 간 차이를 최소화합니다. Unitree G1 실험은 정지 또는 구르는 공, 다양한 위치, 외란을 포함한 다양한 조건에서 강건한 성능을 보이며, 실내 및 실외 시나리오에서 일관된 실행을 유지하는 고충실도 인간형 킥을 입증합니다. 우리의 분할 정복 전략은 강건한 인간형 축구 능력을 발전시키고, 복잡한 체화된 기술 습득을 위한 확장 가능한 프레임워크를 제공합니다. 프로젝트 페이지는 https://soccer-humanoid.github.io/에서 확인할 수 있습니다.

## 핵심 내용
축구는 인간형 로봇에게 중요한 도전 과제로, 인지 기반 킥 동작 및 전신 균형 제어와 같은 작업을 위해 긴밀하게 통합된 인지-행동 능력을 요구합니다. 기존 접근 방식은 모듈식 파이프라인에서 모듈 간 불안정성이나 종단 간 프레임워크에서 상충되는 훈련 목표로 인해 어려움을 겪습니다. 우리는 축구 기술 습득을 세 단계로 분해하는 점진적 아키텍처인 PAiD(Perception-Action integrated Decision-making)를 제안합니다: 인간 동작 추적을 통한 운동 기술 습득, 위치 일반화를 위한 경량 인지-행동 통합, 물리 인식 시뮬레이션-실제 전환. 이러한 단계적 분해는 안정적인 기초 기술을 확립하고, 인지 통합 중 보상 충돌을 방지하며, 시뮬레이션-실제 간 차이를 최소화합니다. Unitree G1 실험은 정지 또는 구르는 공, 다양한 위치, 외란을 포함한 다양한 조건에서 강건한 성능을 보이며, 실내 및 실외 시나리오에서 일관된 실행을 유지하는 고충실도 인간형 킥을 입증합니다. 우리의 분할 정복 전략은 강건한 인간형 축구 능력을 발전시키고, 복잡한 체화된 기술 습득을 위한 확장 가능한 프레임워크를 제공합니다. 프로젝트 페이지는 https://soccer-humanoid.github.io/에서 확인할 수 있습니다.
