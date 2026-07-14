---
$id: ent_paper_cai_seeing_space_and_motion_enhanc_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Seeing Space and Motion: Enhancing Latent Actions with Spatial and Dynamic Awareness for VLA'
  zh: SSM-VLA
  ko: 'Seeing Space and Motion: Enhancing Latent Actions with Spatial and Dynamic Awareness for VLA'
summary:
  en: 'Seeing Space and Motion: Enhancing Latent Actions with Spatial and Dynamic Awareness for VLA (SSM-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Tsinghua Shenzhen International Graduate School,
    Tsinghua University, Amap, Alibaba Group, School of Software Engineering, Xi’an Jiaotong University, Xi’an Jiaotong University..'
  zh: 'Seeing Space and Motion: Enhancing Latent Actions with Spatial and Dynamic Awareness for VLA (SSM-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Tsinghua Shenzhen International Graduate School,
    Tsinghua University, Amap, Alibaba Group, School of Software Engineering, Xi’an Jiaotong University, Xi’an Jiaotong University..'
  ko: 'Seeing Space and Motion: Enhancing Latent Actions with Spatial and Dynamic Awareness for VLA (SSM-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Tsinghua Shenzhen International Graduate School,
    Tsinghua University, Amap, Alibaba Group, School of Software Engineering, Xi’an Jiaotong University, Xi’an Jiaotong University..'
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
- ssm_vla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.26251v2.
sources:
- id: src_001
  type: paper
  title: 'Seeing Space and Motion: Enhancing Latent Actions with Spatial and Dynamic Awareness for VLA (arXiv)'
  url: https://arxiv.org/abs/2509.26251
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: SSM-VLA source
  url: https://doi.org/10.48550/arXiv.2509.26251
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Latent Action Models (LAMs) enable Vision- Language-Action (VLA) systems to learn semantic action representations from large-scale unannotated data. Yet, we identify two bottlenecks of LAMs: 1) the commonly adopted end-to-end trained image encoder suffers from poor spatial understanding; 2) LAMs can be fragile when input frames are temporally distant, leading to limited temporal percep- tion. Such factors inevitably hinder stable and clear action modeling. To this end, we propose Farsighted-LAM, a latent action framework with geometry-aware spatial encoding and multi-scale temporal modeling, capturing structural priors and dynamic motion patterns from consecutive frames. We further propose SSM-VLA, an end-to-end VLA framework built upon Farsighted-LAM, which integrates structured perception with a visual Chain-of-Thought module to explicitly reason about environmental dynamics, enhancing decision consistency and interpretability. We validate SSM-VLA on multiple VLA tasks in both simulation and real-world settings, and achieve state-of- the-art performance. Our results demonstrate that our strategy of combining geometry-aware modeling, temporal coherence, and explicit reasoning is effective in enhancing the robustness and generalizability of embodied intelligence.

## 核心内容
Latent Action Models (LAMs) enable Vision- Language-Action (VLA) systems to learn semantic action representations from large-scale unannotated data. Yet, we identify two bottlenecks of LAMs: 1) the commonly adopted end-to-end trained image encoder suffers from poor spatial understanding; 2) LAMs can be fragile when input frames are temporally distant, leading to limited temporal percep- tion. Such factors inevitably hinder stable and clear action modeling. To this end, we propose Farsighted-LAM, a latent action framework with geometry-aware spatial encoding and multi-scale temporal modeling, capturing structural priors and dynamic motion patterns from consecutive frames. We further propose SSM-VLA, an end-to-end VLA framework built upon Farsighted-LAM, which integrates structured perception with a visual Chain-of-Thought module to explicitly reason about environmental dynamics, enhancing decision consistency and interpretability. We validate SSM-VLA on multiple VLA tasks in both simulation and real-world settings, and achieve state-of- the-art performance. Our results demonstrate that our strategy of combining geometry-aware modeling, temporal coherence, and explicit reasoning is effective in enhancing the robustness and generalizability of embodied intelligence.

## 参考
- http://arxiv.org/abs/2509.26251v2

