---
$id: ent_paper_li_cogvla_cognition_aligned_visio_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CogVLA: Cognition-Aligned Vision-Language-Action Model via Instruction-Driven Routing & Sparsification'
  zh: CogVLA
  ko: 'CogVLA: Cognition-Aligned Vision-Language-Action Model via Instruction-Driven Routing & Sparsification'
summary:
  en: 'CogVLA: Cognition-Aligned Vision-Language-Action Model via Instruction-Driven Routing & Sparsification (CogVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by School of Computer Science and Technology,
    Harbin Institute of Technology, Harbin Institute of Technology, and published at NIPS25.'
  zh: 'CogVLA: Cognition-Aligned Vision-Language-Action Model via Instruction-Driven Routing & Sparsification (CogVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by School of Computer Science and Technology,
    Harbin Institute of Technology, Harbin Institute of Technology, and published at NIPS25.'
  ko: 'CogVLA: Cognition-Aligned Vision-Language-Action Model via Instruction-Driven Routing & Sparsification (CogVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by School of Computer Science and Technology,
    Harbin Institute of Technology, Harbin Institute of Technology, and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- cogvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.21046v3.
sources:
- id: src_001
  type: paper
  title: 'CogVLA: Cognition-Aligned Vision-Language-Action Model via Instruction-Driven Routing & Sparsification (arXiv)'
  url: https://arxiv.org/abs/2508.21046
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: CogVLA source
  url: https://doi.org/10.48550/arXiv.2508.21046
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent Vision-Language-Action (VLA) models built on pre-trained Vision-Language Models (VLMs) require extensive post-training, resulting in high computational overhead that limits scalability and deployment.We propose CogVLA, a Cognition-Aligned Vision-Language-Action framework that leverages instruction-driven routing and sparsification to improve both efficiency and performance. CogVLA draws inspiration from human multimodal coordination and introduces a 3-stage progressive architecture. 1) Encoder-FiLM based Aggregation Routing (EFA-Routing) injects instruction information into the vision encoder to selectively aggregate and compress dual-stream visual tokens, forming a instruction-aware latent representation. 2) Building upon this compact visual encoding, LLM-FiLM based Pruning Routing (LFP-Routing) introduces action intent into the language model by pruning instruction-irrelevant visually grounded tokens, thereby achieving token-level sparsity. 3) To ensure that compressed perception inputs can still support accurate and coherent action generation, we introduce V-L-A Coupled Attention (CAtten), which combines causal vision-language attention with bidirectional action parallel decoding. Extensive experiments on the LIBERO benchmark and real-world robotic tasks demonstrate that CogVLA achieves state-of-the-art performance with success rates of 97.4% and 70.0%, respectively, while reducing training costs by 2.5-fold and decreasing inference latency by 2.8-fold compared to OpenVLA. CogVLA is open-sourced and publicly available at https://github.com/JiuTian-VL/CogVLA.

## 核心内容
Recent Vision-Language-Action (VLA) models built on pre-trained Vision-Language Models (VLMs) require extensive post-training, resulting in high computational overhead that limits scalability and deployment.We propose CogVLA, a Cognition-Aligned Vision-Language-Action framework that leverages instruction-driven routing and sparsification to improve both efficiency and performance. CogVLA draws inspiration from human multimodal coordination and introduces a 3-stage progressive architecture. 1) Encoder-FiLM based Aggregation Routing (EFA-Routing) injects instruction information into the vision encoder to selectively aggregate and compress dual-stream visual tokens, forming a instruction-aware latent representation. 2) Building upon this compact visual encoding, LLM-FiLM based Pruning Routing (LFP-Routing) introduces action intent into the language model by pruning instruction-irrelevant visually grounded tokens, thereby achieving token-level sparsity. 3) To ensure that compressed perception inputs can still support accurate and coherent action generation, we introduce V-L-A Coupled Attention (CAtten), which combines causal vision-language attention with bidirectional action parallel decoding. Extensive experiments on the LIBERO benchmark and real-world robotic tasks demonstrate that CogVLA achieves state-of-the-art performance with success rates of 97.4% and 70.0%, respectively, while reducing training costs by 2.5-fold and decreasing inference latency by 2.8-fold compared to OpenVLA. CogVLA is open-sourced and publicly available at https://github.com/JiuTian-VL/CogVLA.

## 参考
- http://arxiv.org/abs/2508.21046v3

