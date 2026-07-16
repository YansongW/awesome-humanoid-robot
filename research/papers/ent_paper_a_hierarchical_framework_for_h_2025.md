---
$id: ent_paper_a_hierarchical_framework_for_h_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Hierarchical Framework for Humanoid Locomotion with Supernumerary Limbs
  zh: A Hierarchical Framework for Humanoid Locomotion with Supernumerary Limbs
  ko: A Hierarchical Framework for Humanoid Locomotion with Supernumerary Limbs
summary:
  en: A Hierarchical Framework for Humanoid Locomotion with Supernumerary Limbs is a 2025 work on locomotion for humanoid
    robots.
  zh: A Hierarchical Framework for Humanoid Locomotion with Supernumerary Limbs is a 2025 work on locomotion for humanoid
    robots.
  ko: A Hierarchical Framework for Humanoid Locomotion with Supernumerary Limbs is a 2025 work on locomotion for humanoid
    robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- a_hierarchical_framework_for_h
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.00077v1.
sources:
- id: src_001
  type: paper
  title: A Hierarchical Framework for Humanoid Locomotion with Supernumerary Limbs (arXiv)
  url: https://arxiv.org/abs/2512.00077
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The integration of Supernumerary Limbs (SLs) on humanoid robots poses a significant stability challenge due to the dynamic perturbations they introduce. This thesis addresses this issue by designing a novel hierarchical control architecture to improve humanoid locomotion stability with SLs. The core of this framework is a decoupled strategy that combines learning-based locomotion with model-based balancing. The low-level component consists of a walking gait for a Unitree H1 humanoid through imitation learning and curriculum learning. The high-level component actively utilizes the SLs for dynamic balancing. The effectiveness of the system is evaluated in a physics-based simulation under three conditions: baseline gait for an unladen humanoid (baseline walking), walking with a static SL payload (static payload), and walking with the active dynamic balancing controller (dynamic balancing). Our evaluation shows that the dynamic balancing controller improves stability. Compared to the static payload condition, the balancing strategy yields a gait pattern closer to the baseline and decreases the Dynamic Time Warping (DTW) distance of the CoM trajectory by 47\%. The balancing controller also improves the re-stabilization within gait cycles and achieves a more coordinated anti-phase pattern of Ground Reaction Forces (GRF). The results demonstrate that a decoupled, hierarchical design can effectively mitigate the internal dynamic disturbances arising from the mass and movement of the SLs, enabling stable locomotion for humanoids equipped with functional limbs. Code and videos are available here: https://github.com/heyzbw/HuSLs.

## 核心内容
The integration of Supernumerary Limbs (SLs) on humanoid robots poses a significant stability challenge due to the dynamic perturbations they introduce. This thesis addresses this issue by designing a novel hierarchical control architecture to improve humanoid locomotion stability with SLs. The core of this framework is a decoupled strategy that combines learning-based locomotion with model-based balancing. The low-level component consists of a walking gait for a Unitree H1 humanoid through imitation learning and curriculum learning. The high-level component actively utilizes the SLs for dynamic balancing. The effectiveness of the system is evaluated in a physics-based simulation under three conditions: baseline gait for an unladen humanoid (baseline walking), walking with a static SL payload (static payload), and walking with the active dynamic balancing controller (dynamic balancing). Our evaluation shows that the dynamic balancing controller improves stability. Compared to the static payload condition, the balancing strategy yields a gait pattern closer to the baseline and decreases the Dynamic Time Warping (DTW) distance of the CoM trajectory by 47\%. The balancing controller also improves the re-stabilization within gait cycles and achieves a more coordinated anti-phase pattern of Ground Reaction Forces (GRF). The results demonstrate that a decoupled, hierarchical design can effectively mitigate the internal dynamic disturbances arising from the mass and movement of the SLs, enabling stable locomotion for humanoids equipped with functional limbs. Code and videos are available here: https://github.com/heyzbw/HuSLs.

## 参考
- http://arxiv.org/abs/2512.00077v1

## Overview
The integration of Supernumerary Limbs (SLs) on humanoid robots poses a significant stability challenge due to the dynamic perturbations they introduce. This thesis addresses this issue by designing a novel hierarchical control architecture to improve humanoid locomotion stability with SLs. The core of this framework is a decoupled strategy that combines learning-based locomotion with model-based balancing. The low-level component consists of a walking gait for a Unitree H1 humanoid through imitation learning and curriculum learning. The high-level component actively utilizes the SLs for dynamic balancing. The effectiveness of the system is evaluated in a physics-based simulation under three conditions: baseline gait for an unladen humanoid (baseline walking), walking with a static SL payload (static payload), and walking with the active dynamic balancing controller (dynamic balancing). Our evaluation shows that the dynamic balancing controller improves stability. Compared to the static payload condition, the balancing strategy yields a gait pattern closer to the baseline and decreases the Dynamic Time Warping (DTW) distance of the CoM trajectory by 47\%. The balancing controller also improves the re-stabilization within gait cycles and achieves a more coordinated anti-phase pattern of Ground Reaction Forces (GRF). The results demonstrate that a decoupled, hierarchical design can effectively mitigate the internal dynamic disturbances arising from the mass and movement of the SLs, enabling stable locomotion for humanoids equipped with functional limbs. Code and videos are available here: https://github.com/heyzbw/HuSLs.

## Content
The integration of Supernumerary Limbs (SLs) on humanoid robots poses a significant stability challenge due to the dynamic perturbations they introduce. This thesis addresses this issue by designing a novel hierarchical control architecture to improve humanoid locomotion stability with SLs. The core of this framework is a decoupled strategy that combines learning-based locomotion with model-based balancing. The low-level component consists of a walking gait for a Unitree H1 humanoid through imitation learning and curriculum learning. The high-level component actively utilizes the SLs for dynamic balancing. The effectiveness of the system is evaluated in a physics-based simulation under three conditions: baseline gait for an unladen humanoid (baseline walking), walking with a static SL payload (static payload), and walking with the active dynamic balancing controller (dynamic balancing). Our evaluation shows that the dynamic balancing controller improves stability. Compared to the static payload condition, the balancing strategy yields a gait pattern closer to the baseline and decreases the Dynamic Time Warping (DTW) distance of the CoM trajectory by 47\%. The balancing controller also improves the re-stabilization within gait cycles and achieves a more coordinated anti-phase pattern of Ground Reaction Forces (GRF). The results demonstrate that a decoupled, hierarchical design can effectively mitigate the internal dynamic disturbances arising from the mass and movement of the SLs, enabling stable locomotion for humanoids equipped with functional limbs. Code and videos are available here: https://github.com/heyzbw/HuSLs.

## 개요
휴머노이드 로봇에 초과 팔다리(SLs)를 통합하면 동적 교란으로 인해 심각한 안정성 문제가 발생합니다. 본 논문은 이러한 문제를 해결하기 위해 SLs를 갖춘 휴머노이드의 보행 안정성을 향상시키는 새로운 계층적 제어 아키텍처를 설계합니다. 이 프레임워크의 핵심은 학습 기반 보행과 모델 기반 균형을 결합한 분리 전략입니다. 하위 수준 구성 요소는 모방 학습과 커리큘럼 학습을 통해 Unitree H1 휴머노이드의 보행 걸음걸이로 구성됩니다. 상위 수준 구성 요소는 동적 균형을 위해 SLs를 적극적으로 활용합니다. 시스템의 효과는 세 가지 조건(무부하 휴머노이드의 기준 걸음걸이(기준 보행), 정적 SL 페이로드로 보행(정적 페이로드), 능동 동적 균형 제어기로 보행(동적 균형))에서 물리 기반 시뮬레이션을 통해 평가됩니다. 평가 결과, 동적 균형 제어기가 안정성을 향상시키는 것으로 나타났습니다. 정적 페이로드 조건과 비교하여 균형 전략은 기준에 더 가까운 걸음걸이 패턴을 생성하고 CoM 궤적의 DTW(Dynamic Time Warping) 거리를 47% 감소시킵니다. 균형 제어기는 또한 걸음걸이 주기 내 재안정화를 개선하고 지면 반력(GRF)의 더 조화로운 역위상 패턴을 달성합니다. 결과는 분리된 계층적 설계가 SLs의 질량과 움직임에서 발생하는 내부 동적 교란을 효과적으로 완화하여 기능적 팔다리를 장착한 휴머노이드의 안정적인 보행을 가능하게 함을 보여줍니다. 코드와 비디오는 여기에서 확인할 수 있습니다: https://github.com/heyzbw/HuSLs.

## 핵심 내용
휴머노이드 로봇에 초과 팔다리(SLs)를 통합하면 동적 교란으로 인해 심각한 안정성 문제가 발생합니다. 본 논문은 이러한 문제를 해결하기 위해 SLs를 갖춘 휴머노이드의 보행 안정성을 향상시키는 새로운 계층적 제어 아키텍처를 설계합니다. 이 프레임워크의 핵심은 학습 기반 보행과 모델 기반 균형을 결합한 분리 전략입니다. 하위 수준 구성 요소는 모방 학습과 커리큘럼 학습을 통해 Unitree H1 휴머노이드의 보행 걸음걸이로 구성됩니다. 상위 수준 구성 요소는 동적 균형을 위해 SLs를 적극적으로 활용합니다. 시스템의 효과는 세 가지 조건(무부하 휴머노이드의 기준 걸음걸이(기준 보행), 정적 SL 페이로드로 보행(정적 페이로드), 능동 동적 균형 제어기로 보행(동적 균형))에서 물리 기반 시뮬레이션을 통해 평가됩니다. 평가 결과, 동적 균형 제어기가 안정성을 향상시키는 것으로 나타났습니다. 정적 페이로드 조건과 비교하여 균형 전략은 기준에 더 가까운 걸음걸이 패턴을 생성하고 CoM 궤적의 DTW(Dynamic Time Warping) 거리를 47% 감소시킵니다. 균형 제어기는 또한 걸음걸이 주기 내 재안정화를 개선하고 지면 반력(GRF)의 더 조화로운 역위상 패턴을 달성합니다. 결과는 분리된 계층적 설계가 SLs의 질량과 움직임에서 발생하는 내부 동적 교란을 효과적으로 완화하여 기능적 팔다리를 장착한 휴머노이드의 안정적인 보행을 가능하게 함을 보여줍니다. 코드와 비디오는 여기에서 확인할 수 있습니다: https://github.com/heyzbw/HuSLs.
