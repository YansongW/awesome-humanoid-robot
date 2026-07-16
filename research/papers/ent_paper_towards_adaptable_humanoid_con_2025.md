---
$id: ent_paper_towards_adaptable_humanoid_con_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Towards Adaptable Humanoid Control via Adaptive Motion Tracking
  zh: Towards Adaptable Humanoid Control via Adaptive Motion Tracking
  ko: Towards Adaptable Humanoid Control via Adaptive Motion Tracking
summary:
  en: Towards Adaptable Humanoid Control via Adaptive Motion Tracking is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.
  zh: Towards Adaptable Humanoid Control via Adaptive Motion Tracking is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.
  ko: Towards Adaptable Humanoid Control via Adaptive Motion Tracking is a 2025 work on loco-manipulation and whole-body-control
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
- loco_manipulation
- towards_adaptable_humanoid_con
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.14454v1.
sources:
- id: src_001
  type: paper
  title: Towards Adaptable Humanoid Control via Adaptive Motion Tracking (arXiv)
  url: https://arxiv.org/abs/2510.14454
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots are envisioned to adapt demonstrated motions to diverse real-world conditions while accurately preserving motion patterns. Existing motion prior approaches enable well adaptability with a few motions but often sacrifice imitation accuracy, whereas motion-tracking methods achieve accurate imitation yet require many training motions and a test-time target motion to adapt. To combine their strengths, we introduce AdaMimic, a novel motion tracking algorithm that enables adaptable humanoid control from a single reference motion. To reduce data dependence while ensuring adaptability, our method first creates an augmented dataset by sparsifying the single reference motion into keyframes and applying light editing with minimal physical assumptions. A policy is then initialized by tracking these sparse keyframes to generate dense intermediate motions, and adapters are subsequently trained to adjust tracking speed and refine low-level actions based on the adjustment, enabling flexible time warping that further improves imitation accuracy and adaptability. We validate these significant improvements in our approach in both simulation and the real-world Unitree G1 humanoid robot in multiple tasks across a wide range of adaptation conditions. Videos and code are available at https://taohuang13.github.io/adamimic.github.io/.

## 核心内容
Humanoid robots are envisioned to adapt demonstrated motions to diverse real-world conditions while accurately preserving motion patterns. Existing motion prior approaches enable well adaptability with a few motions but often sacrifice imitation accuracy, whereas motion-tracking methods achieve accurate imitation yet require many training motions and a test-time target motion to adapt. To combine their strengths, we introduce AdaMimic, a novel motion tracking algorithm that enables adaptable humanoid control from a single reference motion. To reduce data dependence while ensuring adaptability, our method first creates an augmented dataset by sparsifying the single reference motion into keyframes and applying light editing with minimal physical assumptions. A policy is then initialized by tracking these sparse keyframes to generate dense intermediate motions, and adapters are subsequently trained to adjust tracking speed and refine low-level actions based on the adjustment, enabling flexible time warping that further improves imitation accuracy and adaptability. We validate these significant improvements in our approach in both simulation and the real-world Unitree G1 humanoid robot in multiple tasks across a wide range of adaptation conditions. Videos and code are available at https://taohuang13.github.io/adamimic.github.io/.

## 参考
- http://arxiv.org/abs/2510.14454v1

## Overview
Humanoid robots are envisioned to adapt demonstrated motions to diverse real-world conditions while accurately preserving motion patterns. Existing motion prior approaches enable well adaptability with a few motions but often sacrifice imitation accuracy, whereas motion-tracking methods achieve accurate imitation yet require many training motions and a test-time target motion to adapt. To combine their strengths, we introduce AdaMimic, a novel motion tracking algorithm that enables adaptable humanoid control from a single reference motion. To reduce data dependence while ensuring adaptability, our method first creates an augmented dataset by sparsifying the single reference motion into keyframes and applying light editing with minimal physical assumptions. A policy is then initialized by tracking these sparse keyframes to generate dense intermediate motions, and adapters are subsequently trained to adjust tracking speed and refine low-level actions based on the adjustment, enabling flexible time warping that further improves imitation accuracy and adaptability. We validate these significant improvements in our approach in both simulation and the real-world Unitree G1 humanoid robot in multiple tasks across a wide range of adaptation conditions. Videos and code are available at https://taohuang13.github.io/adamimic.github.io/.

## Content
Humanoid robots are envisioned to adapt demonstrated motions to diverse real-world conditions while accurately preserving motion patterns. Existing motion prior approaches enable well adaptability with a few motions but often sacrifice imitation accuracy, whereas motion-tracking methods achieve accurate imitation yet require many training motions and a test-time target motion to adapt. To combine their strengths, we introduce AdaMimic, a novel motion tracking algorithm that enables adaptable humanoid control from a single reference motion. To reduce data dependence while ensuring adaptability, our method first creates an augmented dataset by sparsifying the single reference motion into keyframes and applying light editing with minimal physical assumptions. A policy is then initialized by tracking these sparse keyframes to generate dense intermediate motions, and adapters are subsequently trained to adjust tracking speed and refine low-level actions based on the adjustment, enabling flexible time warping that further improves imitation accuracy and adaptability. We validate these significant improvements in our approach in both simulation and the real-world Unitree G1 humanoid robot in multiple tasks across a wide range of adaptation conditions. Videos and code are available at https://taohuang13.github.io/adamimic.github.io/.

## 개요
휴머노이드 로봇은 다양한 실제 환경에서 시연된 동작을 적응시키면서도 동작 패턴을 정확히 보존할 수 있도록 구상됩니다. 기존의 동작 사전 접근법은 적은 수의 동작으로도 우수한 적응성을 제공하지만 종종 모방 정확도를 희생하는 반면, 동작 추적 방법은 정확한 모방을 달성하지만 많은 훈련 동작과 테스트 시점의 목표 동작을 필요로 합니다. 이들의 장점을 결합하기 위해, 우리는 단일 참조 동작으로부터 적응 가능한 휴머노이드 제어를 가능하게 하는 새로운 동작 추적 알고리즘인 AdaMimic을 소개합니다. 데이터 의존성을 줄이면서 적응성을 보장하기 위해, 우리의 방법은 먼저 단일 참조 동작을 키프레임으로 희소화하고 최소한의 물리적 가정으로 가벼운 편집을 적용하여 증강 데이터셋을 생성합니다. 그런 다음 이러한 희소 키프레임을 추적하여 밀집된 중간 동작을 생성하도록 정책을 초기화하고, 이후 어댑터를 훈련하여 추적 속도를 조정하고 조정에 기반한 저수준 동작을 개선함으로써 유연한 시간 왜곡을 가능하게 하여 모방 정확도와 적응성을 더욱 향상시킵니다. 우리는 시뮬레이션과 실제 Unitree G1 휴머노이드 로봇에서 다양한 적응 조건에 걸친 여러 작업을 통해 이러한 중요한 개선 사항을 검증합니다. 비디오와 코드는 https://taohuang13.github.io/adamimic.github.io/에서 확인할 수 있습니다.

## 핵심 내용
휴머노이드 로봇은 다양한 실제 환경에서 시연된 동작을 적응시키면서도 동작 패턴을 정확히 보존할 수 있도록 구상됩니다. 기존의 동작 사전 접근법은 적은 수의 동작으로도 우수한 적응성을 제공하지만 종종 모방 정확도를 희생하는 반면, 동작 추적 방법은 정확한 모방을 달성하지만 많은 훈련 동작과 테스트 시점의 목표 동작을 필요로 합니다. 이들의 장점을 결합하기 위해, 우리는 단일 참조 동작으로부터 적응 가능한 휴머노이드 제어를 가능하게 하는 새로운 동작 추적 알고리즘인 AdaMimic을 소개합니다. 데이터 의존성을 줄이면서 적응성을 보장하기 위해, 우리의 방법은 먼저 단일 참조 동작을 키프레임으로 희소화하고 최소한의 물리적 가정으로 가벼운 편집을 적용하여 증강 데이터셋을 생성합니다. 그런 다음 이러한 희소 키프레임을 추적하여 밀집된 중간 동작을 생성하도록 정책을 초기화하고, 이후 어댑터를 훈련하여 추적 속도를 조정하고 조정에 기반한 저수준 동작을 개선함으로써 유연한 시간 왜곡을 가능하게 하여 모방 정확도와 적응성을 더욱 향상시킵니다. 우리는 시뮬레이션과 실제 Unitree G1 휴머노이드 로봇에서 다양한 적응 조건에 걸친 여러 작업을 통해 이러한 중요한 개선 사항을 검증합니다. 비디오와 코드는 https://taohuang13.github.io/adamimic.github.io/에서 확인할 수 있습니다.
