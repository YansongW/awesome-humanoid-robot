---
$id: ent_paper_sun_transforming_monolithic_founda_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Transforming Monolithic Foundation Models into Embodied Multi-Agent Architectures for Human-Robot Collaboration
  zh: InteractGen
  ko: Transforming Monolithic Foundation Models into Embodied Multi-Agent Architectures for Human-Robot Collaboration
summary:
  en: Transforming Monolithic Foundation Models into Embodied Multi-Agent Architectures for Human-Robot Collaboration (InteractGen),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Tsinghua University, Beijing University
    of Posts and Telecommunications.
  zh: Transforming Monolithic Foundation Models into Embodied Multi-Agent Architectures for Human-Robot Collaboration (InteractGen),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Tsinghua University, Beijing University
    of Posts and Telecommunications.
  ko: Transforming Monolithic Foundation Models into Embodied Multi-Agent Architectures for Human-Robot Collaboration (InteractGen),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Tsinghua University, Beijing University
    of Posts and Telecommunications.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- interactgen
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.00797v1.
sources:
- id: src_001
  type: paper
  title: Transforming Monolithic Foundation Models into Embodied Multi-Agent Architectures for Human-Robot Collaboration (arXiv)
  url: https://arxiv.org/abs/2512.00797
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: InteractGen source
  url: https://doi.org/10.48550/arXiv.2512.00797
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Foundation models have become central to unifying perception and planning in robotics, yet real-world deployment exposes a mismatch between their monolithic assumption that a single model can handle all cognitive functions and the distributed, dynamic nature of practical service workflows. Vision-language models offer strong semantic understanding but lack embodiment-aware action capabilities while relying on hand-crafted skills. Vision-Language-Action policies enable reactive manipulation but remain brittle across embodiments, weak in geometric grounding, and devoid of proactive collaboration mechanisms. These limitations indicate that scaling a single model alone cannot deliver reliable autonomy for service robots operating in human-populated settings. To address this gap, we present InteractGen, an LLM-powered multi-agent framework that decomposes robot intelligence into specialized agents for continuous perception, dependency-aware planning, decision and verification, failure reflection, and dynamic human delegation, treating foundation models as regulated components within a closed-loop collective. Deployed on a heterogeneous robot team and evaluated in a three-month open-use study, InteractGen improves task success, adaptability, and human-robot collaboration, providing evidence that multi-agent orchestration offers a more feasible path toward socially grounded service autonomy than further scaling standalone models.

## 核心内容
Foundation models have become central to unifying perception and planning in robotics, yet real-world deployment exposes a mismatch between their monolithic assumption that a single model can handle all cognitive functions and the distributed, dynamic nature of practical service workflows. Vision-language models offer strong semantic understanding but lack embodiment-aware action capabilities while relying on hand-crafted skills. Vision-Language-Action policies enable reactive manipulation but remain brittle across embodiments, weak in geometric grounding, and devoid of proactive collaboration mechanisms. These limitations indicate that scaling a single model alone cannot deliver reliable autonomy for service robots operating in human-populated settings. To address this gap, we present InteractGen, an LLM-powered multi-agent framework that decomposes robot intelligence into specialized agents for continuous perception, dependency-aware planning, decision and verification, failure reflection, and dynamic human delegation, treating foundation models as regulated components within a closed-loop collective. Deployed on a heterogeneous robot team and evaluated in a three-month open-use study, InteractGen improves task success, adaptability, and human-robot collaboration, providing evidence that multi-agent orchestration offers a more feasible path toward socially grounded service autonomy than further scaling standalone models.

## 参考
- http://arxiv.org/abs/2512.00797v1

