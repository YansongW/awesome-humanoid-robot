---
$id: ent_paper_towards_proprioception_aware_e_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Towards Proprioception-Aware Embodied Planning for Dual-Arm Humanoid Robots
  zh: Towards Proprioception-Aware Embodied Planning for Dual-Arm Humanoid Robots
  ko: Towards Proprioception-Aware Embodied Planning for Dual-Arm Humanoid Robots
summary:
  en: Towards Proprioception-Aware Embodied Planning for Dual-Arm Humanoid Robots is a 2025 work on manipulation for humanoid
    robots.
  zh: Towards Proprioception-Aware Embodied Planning for Dual-Arm Humanoid Robots is a 2025 work on manipulation for humanoid
    robots.
  ko: Towards Proprioception-Aware Embodied Planning for Dual-Arm Humanoid Robots is a 2025 work on manipulation for humanoid
    robots.
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
- manipulation
- towards_proprioception_aware_e
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.07882v2.
sources:
- id: src_001
  type: paper
  title: Towards Proprioception-Aware Embodied Planning for Dual-Arm Humanoid Robots (arXiv)
  url: https://arxiv.org/abs/2510.07882
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
In recent years, Multimodal Large Language Models (MLLMs) have demonstrated the ability to serve as high-level planners, enabling robots to follow complex human instructions. However, their effectiveness, especially in long-horizon tasks involving dual-arm humanoid robots, remains limited. This limitation arises from two main challenges: (i) the absence of simulation platforms that systematically support task evaluation and data collection for humanoid robots, and (ii) the insufficient embodiment awareness of current MLLMs, which hinders reasoning about dual-arm selection logic and body positions during planning. To address these issues, we present DualTHOR, a new dual-arm humanoid simulator, with continuous transition and a contingency mechanism. Building on this platform, we propose Proprio-MLLM, a model that enhances embodiment awareness by incorporating proprioceptive information with motion-based position embedding and a cross-spatial encoder. Experiments show that, while existing MLLMs struggle in this environment, Proprio-MLLM achieves an average improvement of 19.75% in planning performance. Our work provides both an essential simulation platform and an effective model to advance embodied intelligence in humanoid robotics. The code is available at https://anonymous.4open.science/r/DualTHOR-5F3B.

## 核心内容
In recent years, Multimodal Large Language Models (MLLMs) have demonstrated the ability to serve as high-level planners, enabling robots to follow complex human instructions. However, their effectiveness, especially in long-horizon tasks involving dual-arm humanoid robots, remains limited. This limitation arises from two main challenges: (i) the absence of simulation platforms that systematically support task evaluation and data collection for humanoid robots, and (ii) the insufficient embodiment awareness of current MLLMs, which hinders reasoning about dual-arm selection logic and body positions during planning. To address these issues, we present DualTHOR, a new dual-arm humanoid simulator, with continuous transition and a contingency mechanism. Building on this platform, we propose Proprio-MLLM, a model that enhances embodiment awareness by incorporating proprioceptive information with motion-based position embedding and a cross-spatial encoder. Experiments show that, while existing MLLMs struggle in this environment, Proprio-MLLM achieves an average improvement of 19.75% in planning performance. Our work provides both an essential simulation platform and an effective model to advance embodied intelligence in humanoid robotics. The code is available at https://anonymous.4open.science/r/DualTHOR-5F3B.

## 参考
- http://arxiv.org/abs/2510.07882v2

## Overview
In recent years, Multimodal Large Language Models (MLLMs) have demonstrated the ability to serve as high-level planners, enabling robots to follow complex human instructions. However, their effectiveness, especially in long-horizon tasks involving dual-arm humanoid robots, remains limited. This limitation arises from two main challenges: (i) the absence of simulation platforms that systematically support task evaluation and data collection for humanoid robots, and (ii) the insufficient embodiment awareness of current MLLMs, which hinders reasoning about dual-arm selection logic and body positions during planning. To address these issues, we present DualTHOR, a new dual-arm humanoid simulator, with continuous transition and a contingency mechanism. Building on this platform, we propose Proprio-MLLM, a model that enhances embodiment awareness by incorporating proprioceptive information with motion-based position embedding and a cross-spatial encoder. Experiments show that, while existing MLLMs struggle in this environment, Proprio-MLLM achieves an average improvement of 19.75% in planning performance. Our work provides both an essential simulation platform and an effective model to advance embodied intelligence in humanoid robotics. The code is available at https://anonymous.4open.science/r/DualTHOR-5F3B.

## Content
In recent years, Multimodal Large Language Models (MLLMs) have demonstrated the ability to serve as high-level planners, enabling robots to follow complex human instructions. However, their effectiveness, especially in long-horizon tasks involving dual-arm humanoid robots, remains limited. This limitation arises from two main challenges: (i) the absence of simulation platforms that systematically support task evaluation and data collection for humanoid robots, and (ii) the insufficient embodiment awareness of current MLLMs, which hinders reasoning about dual-arm selection logic and body positions during planning. To address these issues, we present DualTHOR, a new dual-arm humanoid simulator, with continuous transition and a contingency mechanism. Building on this platform, we propose Proprio-MLLM, a model that enhances embodiment awareness by incorporating proprioceptive information with motion-based position embedding and a cross-spatial encoder. Experiments show that, while existing MLLMs struggle in this environment, Proprio-MLLM achieves an average improvement of 19.75% in planning performance. Our work provides both an essential simulation platform and an effective model to advance embodied intelligence in humanoid robotics. The code is available at https://anonymous.4open.science/r/DualTHOR-5F3B.

## 개요
최근 멀티모달 대규모 언어 모델(MLLM)은 고수준 계획자 역할을 수행하여 로봇이 복잡한 인간 명령을 따를 수 있게 하는 능력을 입증했습니다. 그러나 특히 이중 팔 휴머노이드 로봇을 포함한 장기적 과제에서 그 효과성은 여전히 제한적입니다. 이러한 한계는 두 가지 주요 문제에서 비롯됩니다: (i) 휴머노이드 로봇의 작업 평가와 데이터 수집을 체계적으로 지원하는 시뮬레이션 플랫폼의 부재, (ii) 현재 MLLM의 불충분한 체화 인식으로 인해 계획 중 이중 팔 선택 논리와 신체 위치 추론이 저해된다는 점입니다. 이러한 문제를 해결하기 위해 우리는 연속적 전환과 우발 메커니즘을 갖춘 새로운 이중 팔 휴머노이드 시뮬레이터인 DualTHOR를 제시합니다. 이 플랫폼을 기반으로, 우리는 고유수용성 정보를 동작 기반 위치 임베딩 및 교차 공간 인코더와 통합하여 체화 인식을 강화하는 모델인 Proprio-MLLM을 제안합니다. 실험 결과, 기존 MLLM이 이 환경에서 어려움을 겪는 반면, Proprio-MLLM은 계획 성능에서 평균 19.75%의 향상을 달성했습니다. 우리의 연구는 휴머노이드 로봇공학에서 체화 지능을 발전시키기 위한 필수 시뮬레이션 플랫폼과 효과적인 모델을 모두 제공합니다. 코드는 https://anonymous.4open.science/r/DualTHOR-5F3B에서 확인할 수 있습니다.

## 핵심 내용
최근 멀티모달 대규모 언어 모델(MLLM)은 고수준 계획자 역할을 수행하여 로봇이 복잡한 인간 명령을 따를 수 있게 하는 능력을 입증했습니다. 그러나 특히 이중 팔 휴머노이드 로봇을 포함한 장기적 과제에서 그 효과성은 여전히 제한적입니다. 이러한 한계는 두 가지 주요 문제에서 비롯됩니다: (i) 휴머노이드 로봇의 작업 평가와 데이터 수집을 체계적으로 지원하는 시뮬레이션 플랫폼의 부재, (ii) 현재 MLLM의 불충분한 체화 인식으로 인해 계획 중 이중 팔 선택 논리와 신체 위치 추론이 저해된다는 점입니다. 이러한 문제를 해결하기 위해 우리는 연속적 전환과 우발 메커니즘을 갖춘 새로운 이중 팔 휴머노이드 시뮬레이터인 DualTHOR를 제시합니다. 이 플랫폼을 기반으로, 우리는 고유수용성 정보를 동작 기반 위치 임베딩 및 교차 공간 인코더와 통합하여 체화 인식을 강화하는 모델인 Proprio-MLLM을 제안합니다. 실험 결과, 기존 MLLM이 이 환경에서 어려움을 겪는 반면, Proprio-MLLM은 계획 성능에서 평균 19.75%의 향상을 달성했습니다. 우리의 연구는 휴머노이드 로봇공학에서 체화 지능을 발전시키기 위한 필수 시뮬레이션 플랫폼과 효과적인 모델을 모두 제공합니다. 코드는 https://anonymous.4open.science/r/DualTHOR-5F3B에서 확인할 수 있습니다.
