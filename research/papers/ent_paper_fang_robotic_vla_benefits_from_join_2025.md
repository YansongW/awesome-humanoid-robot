---
$id: ent_paper_fang_robotic_vla_benefits_from_join_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Robotic VLA Benefits from Joint Learning with Motion Image Diffusion
  zh: Robotic VLA Benefits from Joint Learning with Motion Image Diffusion
  ko: Robotic VLA Benefits from Joint Learning with Motion Image Diffusion
summary:
  en: Robotic VLA Benefits from Joint Learning with Motion Image Diffusion (Robotic VLA Benefits from Joint Learning with
    Motion Image Diffusion), is a 2025 large vision-language-action model for robotic manipulation, introduced by Salesforce,
    Stanford University.
  zh: Robotic VLA Benefits from Joint Learning with Motion Image Diffusion (Robotic VLA Benefits from Joint Learning with
    Motion Image Diffusion), is a 2025 large vision-language-action model for robotic manipulation, introduced by Salesforce,
    Stanford University.
  ko: Robotic VLA Benefits from Joint Learning with Motion Image Diffusion (Robotic VLA Benefits from Joint Learning with
    Motion Image Diffusion), is a 2025 large vision-language-action model for robotic manipulation, introduced by Salesforce,
    Stanford University.
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
- robotic_vla_benefits_from_join
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.18007v1.
sources:
- id: src_001
  type: paper
  title: Robotic VLA Benefits from Joint Learning with Motion Image Diffusion (arXiv)
  url: https://arxiv.org/abs/2512.18007
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Robotic VLA Benefits from Joint Learning with Motion Image Diffusion source
  url: https://doi.org/10.48550/arXiv.2512.18007
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have achieved remarkable progress in robotic manipulation by mapping multimodal observations and instructions directly to actions. However, they typically mimic expert trajectories without predictive motion reasoning, which limits their ability to reason about what actions to take. To address this limitation, we propose joint learning with motion image diffusion, a novel strategy that enhances VLA models with motion reasoning capabilities. Our method extends the VLA architecture with a dual-head design: while the action head predicts action chunks as in vanilla VLAs, an additional motion head, implemented as a Diffusion Transformer (DiT), predicts optical-flow-based motion images that capture future dynamics. The two heads are trained jointly, enabling the shared VLM backbone to learn representations that couple robot control with motion knowledge. This joint learning builds temporally coherent and physically grounded representations without modifying the inference pathway of standard VLAs, thereby maintaining test-time latency. Experiments in both simulation and real-world environments demonstrate that joint learning with motion image diffusion improves the success rate of pi-series VLAs to 97.5% on the LIBERO benchmark and 58.0% on the RoboTwin benchmark, yielding a 23% improvement in real-world performance and validating its effectiveness in enhancing the motion reasoning capability of large-scale VLAs.

## 核心内容
Vision-Language-Action (VLA) models have achieved remarkable progress in robotic manipulation by mapping multimodal observations and instructions directly to actions. However, they typically mimic expert trajectories without predictive motion reasoning, which limits their ability to reason about what actions to take. To address this limitation, we propose joint learning with motion image diffusion, a novel strategy that enhances VLA models with motion reasoning capabilities. Our method extends the VLA architecture with a dual-head design: while the action head predicts action chunks as in vanilla VLAs, an additional motion head, implemented as a Diffusion Transformer (DiT), predicts optical-flow-based motion images that capture future dynamics. The two heads are trained jointly, enabling the shared VLM backbone to learn representations that couple robot control with motion knowledge. This joint learning builds temporally coherent and physically grounded representations without modifying the inference pathway of standard VLAs, thereby maintaining test-time latency. Experiments in both simulation and real-world environments demonstrate that joint learning with motion image diffusion improves the success rate of pi-series VLAs to 97.5% on the LIBERO benchmark and 58.0% on the RoboTwin benchmark, yielding a 23% improvement in real-world performance and validating its effectiveness in enhancing the motion reasoning capability of large-scale VLAs.

## 参考
- http://arxiv.org/abs/2512.18007v1

