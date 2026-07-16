---
$id: ent_paper_crisp_contact_guided_real2sim_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives'
  zh: 'CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives'
  ko: 'CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives'
summary:
  en: 'CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives is a 2025 work on physics-based character
    animation for humanoid robots.'
  zh: 'CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives is a 2025 work on physics-based character
    animation for humanoid robots.'
  ko: 'CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives is a 2025 work on physics-based character
    animation for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- crisp
- humanoid
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.14696v3.
sources:
- id: src_001
  type: paper
  title: 'CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives (arXiv)'
  url: https://arxiv.org/abs/2512.14696
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We introduce CRISP, a method that recovers simulatable human motion and scene geometry from monocular video. Prior work on joint human-scene reconstruction relies on data-driven priors and joint optimization with no physics in the loop, or recovers noisy geometry with artifacts that cause motion tracking policies with scene interactions to fail. In contrast, our key insight is to recover convex, clean, and simulation-ready geometry by fitting planar primitives to a point cloud reconstruction of the scene, via a simple clustering pipeline over depth, normals, and flow. To reconstruct scene geometry that might be occluded during interactions, we make use of human-scene contact modeling (e.g., we use human posture to reconstruct the occluded seat of a chair). Finally, we ensure that human and scene reconstructions are physically-plausible by using them to drive a humanoid controller via reinforcement learning. Our approach reduces motion tracking failure rates from 55.2\% to 6.9\% on human-centric video benchmarks (EMDB, PROX), while delivering a 43\% faster RL simulation throughput. We further validate it on in-the-wild videos including casually-captured videos, Internet videos, and even Sora-generated videos. This demonstrates CRISP's ability to generate physically-valid human motion and interaction environments at scale, greatly advancing real-to-sim applications for robotics and AR/VR.

## 核心内容
We introduce CRISP, a method that recovers simulatable human motion and scene geometry from monocular video. Prior work on joint human-scene reconstruction relies on data-driven priors and joint optimization with no physics in the loop, or recovers noisy geometry with artifacts that cause motion tracking policies with scene interactions to fail. In contrast, our key insight is to recover convex, clean, and simulation-ready geometry by fitting planar primitives to a point cloud reconstruction of the scene, via a simple clustering pipeline over depth, normals, and flow. To reconstruct scene geometry that might be occluded during interactions, we make use of human-scene contact modeling (e.g., we use human posture to reconstruct the occluded seat of a chair). Finally, we ensure that human and scene reconstructions are physically-plausible by using them to drive a humanoid controller via reinforcement learning. Our approach reduces motion tracking failure rates from 55.2\% to 6.9\% on human-centric video benchmarks (EMDB, PROX), while delivering a 43\% faster RL simulation throughput. We further validate it on in-the-wild videos including casually-captured videos, Internet videos, and even Sora-generated videos. This demonstrates CRISP's ability to generate physically-valid human motion and interaction environments at scale, greatly advancing real-to-sim applications for robotics and AR/VR.

## 参考
- http://arxiv.org/abs/2512.14696v3

## Overview
We introduce CRISP, a method that recovers simulatable human motion and scene geometry from monocular video. Prior work on joint human-scene reconstruction relies on data-driven priors and joint optimization with no physics in the loop, or recovers noisy geometry with artifacts that cause motion tracking policies with scene interactions to fail. In contrast, our key insight is to recover convex, clean, and simulation-ready geometry by fitting planar primitives to a point cloud reconstruction of the scene, via a simple clustering pipeline over depth, normals, and flow. To reconstruct scene geometry that might be occluded during interactions, we make use of human-scene contact modeling (e.g., we use human posture to reconstruct the occluded seat of a chair). Finally, we ensure that human and scene reconstructions are physically-plausible by using them to drive a humanoid controller via reinforcement learning. Our approach reduces motion tracking failure rates from 55.2\% to 6.9\% on human-centric video benchmarks (EMDB, PROX), while delivering a 43\% faster RL simulation throughput. We further validate it on in-the-wild videos including casually-captured videos, Internet videos, and even Sora-generated videos. This demonstrates CRISP's ability to generate physically-valid human motion and interaction environments at scale, greatly advancing real-to-sim applications for robotics and AR/VR.

## Content
We introduce CRISP, a method that recovers simulatable human motion and scene geometry from monocular video. Prior work on joint human-scene reconstruction relies on data-driven priors and joint optimization with no physics in the loop, or recovers noisy geometry with artifacts that cause motion tracking policies with scene interactions to fail. In contrast, our key insight is to recover convex, clean, and simulation-ready geometry by fitting planar primitives to a point cloud reconstruction of the scene, via a simple clustering pipeline over depth, normals, and flow. To reconstruct scene geometry that might be occluded during interactions, we make use of human-scene contact modeling (e.g., we use human posture to reconstruct the occluded seat of a chair). Finally, we ensure that human and scene reconstructions are physically-plausible by using them to drive a humanoid controller via reinforcement learning. Our approach reduces motion tracking failure rates from 55.2\% to 6.9\% on human-centric video benchmarks (EMDB, PROX), while delivering a 43\% faster RL simulation throughput. We further validate it on in-the-wild videos including casually-captured videos, Internet videos, and even Sora-generated videos. This demonstrates CRISP's ability to generate physically-valid human motion and interaction environments at scale, greatly advancing real-to-sim applications for robotics and AR/VR.

## 개요
우리는 단안 비디오에서 시뮬레이션 가능한 인간 동작과 장면 기하학을 복원하는 방법인 CRISP를 소개합니다. 인간-장면 공동 복원에 관한 기존 연구는 물리적 상호작용 없이 데이터 기반 사전 지식과 공동 최적화에 의존하거나, 잡음이 있는 기하학을 복원하여 장면 상호작용을 포함한 동작 추적 정책이 실패하게 만듭니다. 반면, 우리의 핵심 통찰은 깊이, 법선, 흐름에 대한 간단한 클러스터링 파이프라인을 통해 장면의 포인트 클라우드 복원에 평면 프리미티브를 피팅하여 볼록하고 깨끗하며 시뮬레이션 준비가 된 기하학을 복원하는 것입니다. 상호작용 중에 가려질 수 있는 장면 기하학을 복원하기 위해 인간-장면 접촉 모델링을 활용합니다(예: 인간 자세를 사용하여 가려진 의자 좌석을 복원). 마지막으로, 강화 학습을 통해 휴머노이드 컨트롤러를 구동하는 데 이를 사용하여 인간과 장면 복원이 물리적으로 타당하도록 보장합니다. 우리의 접근 방식은 인간 중심 비디오 벤치마크(EMDB, PROX)에서 동작 추적 실패율을 55.2%에서 6.9%로 줄이고, RL 시뮬레이션 처리량을 43% 향상시킵니다. 또한 캐주얼하게 촬영된 비디오, 인터넷 비디오, 심지어 Sora 생성 비디오를 포함한 실제 비디오에서 이를 검증합니다. 이는 CRISP가 대규모로 물리적으로 유효한 인간 동작과 상호작용 환경을 생성할 수 있는 능력을 보여주며, 로봇공학 및 AR/VR을 위한 실물-시뮬레이션 응용을 크게 발전시킵니다.

## 핵심 내용
우리는 단안 비디오에서 시뮬레이션 가능한 인간 동작과 장면 기하학을 복원하는 방법인 CRISP를 소개합니다. 인간-장면 공동 복원에 관한 기존 연구는 물리적 상호작용 없이 데이터 기반 사전 지식과 공동 최적화에 의존하거나, 잡음이 있는 기하학을 복원하여 장면 상호작용을 포함한 동작 추적 정책이 실패하게 만듭니다. 반면, 우리의 핵심 통찰은 깊이, 법선, 흐름에 대한 간단한 클러스터링 파이프라인을 통해 장면의 포인트 클라우드 복원에 평면 프리미티브를 피팅하여 볼록하고 깨끗하며 시뮬레이션 준비가 된 기하학을 복원하는 것입니다. 상호작용 중에 가려질 수 있는 장면 기하학을 복원하기 위해 인간-장면 접촉 모델링을 활용합니다(예: 인간 자세를 사용하여 가려진 의자 좌석을 복원). 마지막으로, 강화 학습을 통해 휴머노이드 컨트롤러를 구동하는 데 이를 사용하여 인간과 장면 복원이 물리적으로 타당하도록 보장합니다. 우리의 접근 방식은 인간 중심 비디오 벤치마크(EMDB, PROX)에서 동작 추적 실패율을 55.2%에서 6.9%로 줄이고, RL 시뮬레이션 처리량을 43% 향상시킵니다. 또한 캐주얼하게 촬영된 비디오, 인터넷 비디오, 심지어 Sora 생성 비디오를 포함한 실제 비디오에서 이를 검증합니다. 이는 CRISP가 대규모로 물리적으로 유효한 인간 동작과 상호작용 환경을 생성할 수 있는 능력을 보여주며, 로봇공학 및 AR/VR을 위한 실물-시뮬레이션 응용을 크게 발전시킵니다.
