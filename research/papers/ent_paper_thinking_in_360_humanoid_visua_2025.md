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

