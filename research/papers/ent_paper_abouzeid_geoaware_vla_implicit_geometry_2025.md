---
$id: ent_paper_abouzeid_geoaware_vla_implicit_geometry_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model'
  zh: GeoAware-VLA
  ko: 'GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model'
summary:
  en: 'GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model (GeoAware-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Mohamed bin Zayed University of Artificial Intelligence.'
  zh: 'GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model (GeoAware-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Mohamed bin Zayed University of Artificial Intelligence.'
  ko: 'GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model (GeoAware-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Mohamed bin Zayed University of Artificial Intelligence.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- geoaware_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.14117v4.
sources:
- id: src_001
  type: paper
  title: 'GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model (arXiv)'
  url: https://arxiv.org/abs/2509.14117
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: GeoAware-VLA source
  url: https://doi.org/10.48550/arXiv.2509.14117
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models often fail to generalize to unseen camera viewpoints, a limitation stemming from their difficulty in inferring robust 3D geometry from 2D images. We introduce GeoAware-VLA, a simple yet effective approach that enhances viewpoint invariance by integrating strong geometric priors into the vision backbone. Instead of training a visual encoder or relying on explicit 3D data, we leverage a frozen, pretrained geometric vision model as a feature extractor. A lightweight, trainable projection layer then adapts these geometrically-rich features for the policy decoder, relieving it of the burden of learning 3D consistency from scratch. Through extensive evaluations on the LIBERO and CALVIN benchmarks, we show that GeoAware-VLA preserves and even improves in-distribution performance while achieving substantial gains in zero-shot generalization to unseen camera poses, improving unseen-view success rates by an average of 35 percentage points on LIBERO and over 11 percentage points on CALVIN compared to their respective baselines. Crucially, these gains transfer to the physical world, where our model shows significant improvement on a real robotic platform. Our approach proves effective across both continuous and discrete action spaces, highlighting that robust geometric grounding is a key ingredient for building more generalizable robotic agents.

## 核心内容
Vision-Language-Action (VLA) models often fail to generalize to unseen camera viewpoints, a limitation stemming from their difficulty in inferring robust 3D geometry from 2D images. We introduce GeoAware-VLA, a simple yet effective approach that enhances viewpoint invariance by integrating strong geometric priors into the vision backbone. Instead of training a visual encoder or relying on explicit 3D data, we leverage a frozen, pretrained geometric vision model as a feature extractor. A lightweight, trainable projection layer then adapts these geometrically-rich features for the policy decoder, relieving it of the burden of learning 3D consistency from scratch. Through extensive evaluations on the LIBERO and CALVIN benchmarks, we show that GeoAware-VLA preserves and even improves in-distribution performance while achieving substantial gains in zero-shot generalization to unseen camera poses, improving unseen-view success rates by an average of 35 percentage points on LIBERO and over 11 percentage points on CALVIN compared to their respective baselines. Crucially, these gains transfer to the physical world, where our model shows significant improvement on a real robotic platform. Our approach proves effective across both continuous and discrete action spaces, highlighting that robust geometric grounding is a key ingredient for building more generalizable robotic agents.

## 参考
- http://arxiv.org/abs/2509.14117v4

