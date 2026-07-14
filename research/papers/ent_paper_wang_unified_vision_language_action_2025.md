---
$id: ent_paper_wang_unified_vision_language_action_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Unified Vision-Language-Action Model
  zh: UniVLA
  ko: Unified Vision-Language-Action Model
summary:
  en: Unified Vision-Language-Action Model (UniVLA), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by CASIA, BAAI, THU, HKISI.
  zh: Unified Vision-Language-Action Model (UniVLA), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by CASIA, BAAI, THU, HKISI.
  ko: Unified Vision-Language-Action Model (UniVLA), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by CASIA, BAAI, THU, HKISI.
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
- univla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.19850v1.
sources:
- id: src_001
  type: paper
  title: Unified Vision-Language-Action Model (arXiv)
  url: https://arxiv.org/abs/2506.19850
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: UniVLA source
  url: https://dblp.org/rec/journals/corr/abs-2506-19850
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action models (VLAs) have garnered significant attention for their potential in advancing robotic manipulation. However, previous approaches predominantly rely on the general comprehension capabilities of vision-language models (VLMs) to generate action signals, often overlooking the rich temporal and causal structure embedded in visual observations. In this paper, we present UniVLA, a unified and native multimodal VLA model that autoregressively models vision, language, and action signals as discrete token sequences. This formulation enables flexible multimodal tasks learning, particularly from large-scale video data. By incorporating world modeling during post-training, UniVLA captures causal dynamics from videos, facilitating effective transfer to downstream policy learning--especially for long-horizon tasks. Our approach sets new state-of-the-art results across several widely used simulation benchmarks, including CALVIN, LIBERO, and Simplenv-Bridge, significantly surpassing previous methods. For example, UniVLA achieves 95.5% average success rate on LIBERO benchmark, surpassing pi0-FAST's 85.5%. We further demonstrate its broad applicability on real-world ALOHA manipulation and autonomous driving.

## 核心内容
Vision-language-action models (VLAs) have garnered significant attention for their potential in advancing robotic manipulation. However, previous approaches predominantly rely on the general comprehension capabilities of vision-language models (VLMs) to generate action signals, often overlooking the rich temporal and causal structure embedded in visual observations. In this paper, we present UniVLA, a unified and native multimodal VLA model that autoregressively models vision, language, and action signals as discrete token sequences. This formulation enables flexible multimodal tasks learning, particularly from large-scale video data. By incorporating world modeling during post-training, UniVLA captures causal dynamics from videos, facilitating effective transfer to downstream policy learning--especially for long-horizon tasks. Our approach sets new state-of-the-art results across several widely used simulation benchmarks, including CALVIN, LIBERO, and Simplenv-Bridge, significantly surpassing previous methods. For example, UniVLA achieves 95.5% average success rate on LIBERO benchmark, surpassing pi0-FAST's 85.5%. We further demonstrate its broad applicability on real-world ALOHA manipulation and autonomous driving.

## 参考
- http://arxiv.org/abs/2506.19850v1

