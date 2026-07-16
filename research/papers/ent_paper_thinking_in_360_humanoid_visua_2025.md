---
$id: ent_paper_thinking_in_360_humanoid_visua_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Thinking in 360: Humanoid Visual Search in the Wild'
  zh: 'Thinking in 360: Humanoid Visual Search in the Wild'
  ko: 'Thinking in 360: Humanoid Visual Search in the Wild'
summary:
  en: 'Thinking in 360: Humanoid Visual Search in the Wild is a 2025 work on navigation for humanoid robots.'
  zh: 'Thinking in 360: Humanoid Visual Search in the Wild is a 2025 work on navigation for humanoid robots.'
  ko: 'Thinking in 360: Humanoid Visual Search in the Wild is a 2025 work on navigation for humanoid robots.'
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
- navigation
- thinking_in_360
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.20351v2.
sources:
- id: src_001
  type: paper
  title: 'Thinking in 360: Humanoid Visual Search in the Wild (arXiv)'
  url: https://arxiv.org/abs/2511.20351
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humans rely on the synergistic control of head (cephalomotor) and eye (oculomotor) to efficiently search for visual information in 360°. However, prior approaches to visual search are limited to a static image, neglecting the physical embodiment and its interaction with the 3D world. How can we develop embodied visual search agents as efficient as humans while bypassing the constraints imposed by real-world hardware? To this end, we propose humanoid visual search where a humanoid agent actively rotates its head to search for objects or paths in an immersive world represented by a 360° panoramic image. To study visual search in visually-crowded real-world scenarios, we build H* Bench, a new benchmark that moves beyond household scenes to challenging in-the-wild scenes that necessitate advanced visual-spatial reasoning capabilities, such as transportation hubs, large-scale retail spaces, urban streets, and public institutions. Our experiments first reveal that even top-tier proprietary models falter, achieving only ~30% success in object and path search. We then use post-training techniques to enhance the open-source Qwen2.5-VL, increasing its success rate by over threefold for both object search (14.83% to 47.38%) and path search (6.44% to 24.94%). Notably, the lower ceiling of path search reveals its inherent difficulty, which we attribute to the demand for sophisticated spatial commonsense. Our results not only show a promising path forward but also quantify the immense challenge that remains in building MLLM agents that can be seamlessly integrated into everyday human life.

## 核心内容
Humans rely on the synergistic control of head (cephalomotor) and eye (oculomotor) to efficiently search for visual information in 360°. However, prior approaches to visual search are limited to a static image, neglecting the physical embodiment and its interaction with the 3D world. How can we develop embodied visual search agents as efficient as humans while bypassing the constraints imposed by real-world hardware? To this end, we propose humanoid visual search where a humanoid agent actively rotates its head to search for objects or paths in an immersive world represented by a 360° panoramic image. To study visual search in visually-crowded real-world scenarios, we build H* Bench, a new benchmark that moves beyond household scenes to challenging in-the-wild scenes that necessitate advanced visual-spatial reasoning capabilities, such as transportation hubs, large-scale retail spaces, urban streets, and public institutions. Our experiments first reveal that even top-tier proprietary models falter, achieving only ~30% success in object and path search. We then use post-training techniques to enhance the open-source Qwen2.5-VL, increasing its success rate by over threefold for both object search (14.83% to 47.38%) and path search (6.44% to 24.94%). Notably, the lower ceiling of path search reveals its inherent difficulty, which we attribute to the demand for sophisticated spatial commonsense. Our results not only show a promising path forward but also quantify the immense challenge that remains in building MLLM agents that can be seamlessly integrated into everyday human life.

## 参考
- http://arxiv.org/abs/2511.20351v2

## Overview
Humans rely on the synergistic control of head (cephalomotor) and eye (oculomotor) to efficiently search for visual information in 360°. However, prior approaches to visual search are limited to a static image, neglecting the physical embodiment and its interaction with the 3D world. How can we develop embodied visual search agents as efficient as humans while bypassing the constraints imposed by real-world hardware? To this end, we propose humanoid visual search where a humanoid agent actively rotates its head to search for objects or paths in an immersive world represented by a 360° panoramic image. To study visual search in visually-crowded real-world scenarios, we build H* Bench, a new benchmark that moves beyond household scenes to challenging in-the-wild scenes that necessitate advanced visual-spatial reasoning capabilities, such as transportation hubs, large-scale retail spaces, urban streets, and public institutions. Our experiments first reveal that even top-tier proprietary models falter, achieving only ~30% success in object and path search. We then use post-training techniques to enhance the open-source Qwen2.5-VL, increasing its success rate by over threefold for both object search (14.83% to 47.38%) and path search (6.44% to 24.94%). Notably, the lower ceiling of path search reveals its inherent difficulty, which we attribute to the demand for sophisticated spatial commonsense. Our results not only show a promising path forward but also quantify the immense challenge that remains in building MLLM agents that can be seamlessly integrated into everyday human life.

## Content
Humans rely on the synergistic control of head (cephalomotor) and eye (oculomotor) to efficiently search for visual information in 360°. However, prior approaches to visual search are limited to a static image, neglecting the physical embodiment and its interaction with the 3D world. How can we develop embodied visual search agents as efficient as humans while bypassing the constraints imposed by real-world hardware? To this end, we propose humanoid visual search where a humanoid agent actively rotates its head to search for objects or paths in an immersive world represented by a 360° panoramic image. To study visual search in visually-crowded real-world scenarios, we build H* Bench, a new benchmark that moves beyond household scenes to challenging in-the-wild scenes that necessitate advanced visual-spatial reasoning capabilities, such as transportation hubs, large-scale retail spaces, urban streets, and public institutions. Our experiments first reveal that even top-tier proprietary models falter, achieving only ~30% success in object and path search. We then use post-training techniques to enhance the open-source Qwen2.5-VL, increasing its success rate by over threefold for both object search (14.83% to 47.38%) and path search (6.44% to 24.94%). Notably, the lower ceiling of path search reveals its inherent difficulty, which we attribute to the demand for sophisticated spatial commonsense. Our results not only show a promising path forward but also quantify the immense challenge that remains in building MLLM agents that can be seamlessly integrated into everyday human life.

## 개요
인간은 머리(두부 운동)와 눈(안구 운동)의 협력적 제어를 통해 360° 시각 정보를 효율적으로 탐색합니다. 그러나 기존의 시각 탐색 접근법은 정적 이미지에 국한되어 물리적 구현체와 3D 세계와의 상호작용을 간과했습니다. 실제 하드웨어의 제약을 우회하면서 인간처럼 효율적인 구현형 시각 탐색 에이전트를 어떻게 개발할 수 있을까요? 이를 위해 우리는 360° 파노라마 이미지로 표현된 몰입형 세계에서 인간형 에이전트가 능동적으로 머리를 회전하며 객체나 경로를 탐색하는 인간형 시각 탐색을 제안합니다. 시각적으로 혼잡한 실제 세계 시나리오에서의 시각 탐색을 연구하기 위해, 우리는 가정용 장면을 넘어 교통 허브, 대규모 소매 공간, 도시 거리, 공공 기관 등 고급 시각-공간 추론 능력이 필요한 까다로운 실제 환경으로 확장된 새로운 벤치마크 H* Bench를 구축했습니다. 실험 결과, 최고 수준의 독점 모델조차 객체 및 경로 탐색에서 약 30%의 성공률에 그치는 것으로 나타났습니다. 이후 사후 훈련 기법을 통해 오픈소스 Qwen2.5-VL을 개선하여 객체 탐색(14.83% → 47.38%)과 경로 탐색(6.44% → 24.94%) 모두에서 성공률을 3배 이상 향상시켰습니다. 특히 경로 탐색의 낮은 상한선은 정교한 공간 상식에 대한 요구로 인한 본질적 어려움을 드러냅니다. 우리의 결과는 유망한 발전 방향을 제시할 뿐만 아니라 일상생활에 원활히 통합될 수 있는 MLLM 에이전트 구축에 남아 있는 엄청난 과제를 정량화합니다.

## 핵심 내용
인간은 머리(두부 운동)와 눈(안구 운동)의 협력적 제어를 통해 360° 시각 정보를 효율적으로 탐색합니다. 그러나 기존의 시각 탐색 접근법은 정적 이미지에 국한되어 물리적 구현체와 3D 세계와의 상호작용을 간과했습니다. 실제 하드웨어의 제약을 우회하면서 인간처럼 효율적인 구현형 시각 탐색 에이전트를 어떻게 개발할 수 있을까요? 이를 위해 우리는 360° 파노라마 이미지로 표현된 몰입형 세계에서 인간형 에이전트가 능동적으로 머리를 회전하며 객체나 경로를 탐색하는 인간형 시각 탐색을 제안합니다. 시각적으로 혼잡한 실제 세계 시나리오에서의 시각 탐색을 연구하기 위해, 우리는 가정용 장면을 넘어 교통 허브, 대규모 소매 공간, 도시 거리, 공공 기관 등 고급 시각-공간 추론 능력이 필요한 까다로운 실제 환경으로 확장된 새로운 벤치마크 H* Bench를 구축했습니다. 실험 결과, 최고 수준의 독점 모델조차 객체 및 경로 탐색에서 약 30%의 성공률에 그치는 것으로 나타났습니다. 이후 사후 훈련 기법을 통해 오픈소스 Qwen2.5-VL을 개선하여 객체 탐색(14.83% → 47.38%)과 경로 탐색(6.44% → 24.94%) 모두에서 성공률을 3배 이상 향상시켰습니다. 특히 경로 탐색의 낮은 상한선은 정교한 공간 상식에 대한 요구로 인한 본질적 어려움을 드러냅니다. 우리의 결과는 유망한 발전 방향을 제시할 뿐만 아니라 일상생활에 원활히 통합될 수 있는 MLLM 에이전트 구축에 남아 있는 엄청난 과제를 정량화합니다.
