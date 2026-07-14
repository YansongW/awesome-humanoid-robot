---
$id: ent_paper_wang_trackvla_embodied_visual_track_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TrackVLA: Embodied Visual Tracking in the Wild'
  zh: TrackVLA
  ko: 'TrackVLA: Embodied Visual Tracking in the Wild'
summary:
  en: 'TrackVLA: Embodied Visual Tracking in the Wild (TrackVLA), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by Peking University, Galbot, Beihang University, Beijing Normal University, Beijing Academy
    of Artificial Intelligence, and published at CoRL25.'
  zh: 'TrackVLA: Embodied Visual Tracking in the Wild (TrackVLA), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by Peking University, Galbot, Beihang University, Beijing Normal University, Beijing Academy
    of Artificial Intelligence, and published at CoRL25.'
  ko: 'TrackVLA: Embodied Visual Tracking in the Wild (TrackVLA), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by Peking University, Galbot, Beihang University, Beijing Normal University, Beijing Academy
    of Artificial Intelligence, and published at CoRL25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- trackvla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.23189v1.
sources:
- id: src_001
  type: paper
  title: 'TrackVLA: Embodied Visual Tracking in the Wild (arXiv)'
  url: https://arxiv.org/abs/2505.23189
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: TrackVLA source
  url: https://doi.org/10.48550/arXiv.2505.23189
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Embodied visual tracking is a fundamental skill in Embodied AI, enabling an agent to follow a specific target in dynamic environments using only egocentric vision. This task is inherently challenging as it requires both accurate target recognition and effective trajectory planning under conditions of severe occlusion and high scene dynamics. Existing approaches typically address this challenge through a modular separation of recognition and planning. In this work, we propose TrackVLA, a Vision-Language-Action (VLA) model that learns the synergy between object recognition and trajectory planning. Leveraging a shared LLM backbone, we employ a language modeling head for recognition and an anchor-based diffusion model for trajectory planning. To train TrackVLA, we construct an Embodied Visual Tracking Benchmark (EVT-Bench) and collect diverse difficulty levels of recognition samples, resulting in a dataset of 1.7 million samples. Through extensive experiments in both synthetic and real-world environments, TrackVLA demonstrates SOTA performance and strong generalizability. It significantly outperforms existing methods on public benchmarks in a zero-shot manner while remaining robust to high dynamics and occlusion in real-world scenarios at 10 FPS inference speed. Our project page is: https://pku-epic.github.io/TrackVLA-web.

## 核心内容
Embodied visual tracking is a fundamental skill in Embodied AI, enabling an agent to follow a specific target in dynamic environments using only egocentric vision. This task is inherently challenging as it requires both accurate target recognition and effective trajectory planning under conditions of severe occlusion and high scene dynamics. Existing approaches typically address this challenge through a modular separation of recognition and planning. In this work, we propose TrackVLA, a Vision-Language-Action (VLA) model that learns the synergy between object recognition and trajectory planning. Leveraging a shared LLM backbone, we employ a language modeling head for recognition and an anchor-based diffusion model for trajectory planning. To train TrackVLA, we construct an Embodied Visual Tracking Benchmark (EVT-Bench) and collect diverse difficulty levels of recognition samples, resulting in a dataset of 1.7 million samples. Through extensive experiments in both synthetic and real-world environments, TrackVLA demonstrates SOTA performance and strong generalizability. It significantly outperforms existing methods on public benchmarks in a zero-shot manner while remaining robust to high dynamics and occlusion in real-world scenarios at 10 FPS inference speed. Our project page is: https://pku-epic.github.io/TrackVLA-web.

## 参考
- http://arxiv.org/abs/2505.23189v1

