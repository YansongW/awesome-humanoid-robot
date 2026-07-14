---
$id: ent_paper_gu_manualvla_a_unified_vla_model_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ManualVLA: A Unified VLA Model for Chain-of-Thought Manual Generation and Robotic Manipulation'
  zh: ManualVLA
  ko: 'ManualVLA: A Unified VLA Model for Chain-of-Thought Manual Generation and Robotic Manipulation'
summary:
  en: 'ManualVLA: A Unified VLA Model for Chain-of-Thought Manual Generation and Robotic Manipulation (ManualVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia Information
    Processing, School of Computer Science, Peking University, The Chinese University of Hong Kong, Simplexity Robotics.'
  zh: 'ManualVLA: A Unified VLA Model for Chain-of-Thought Manual Generation and Robotic Manipulation (ManualVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia Information
    Processing, School of Computer Science, Peking University, The Chinese University of Hong Kong, Simplexity Robotics.'
  ko: 'ManualVLA: A Unified VLA Model for Chain-of-Thought Manual Generation and Robotic Manipulation (ManualVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia Information
    Processing, School of Computer Science, Peking University, The Chinese University of Hong Kong, Simplexity Robotics.'
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
- manualvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.02013v1.
sources:
- id: src_001
  type: paper
  title: 'ManualVLA: A Unified VLA Model for Chain-of-Thought Manual Generation and Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2512.02013
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ManualVLA source
  url: https://doi.org/10.48550/arXiv.2512.02013
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have recently emerged, demonstrating strong generalization in robotic scene understanding and manipulation. However, when confronted with long-horizon tasks that require defined goal states, such as LEGO assembly or object rearrangement, existing VLA models still face challenges in coordinating high-level planning with precise manipulation. Therefore, we aim to endow a VLA model with the capability to infer the "how" process from the "what" outcomes, transforming goal states into executable procedures. In this paper, we introduce ManualVLA, a unified VLA framework built upon a Mixture-of-Transformers (MoT) architecture, enabling coherent collaboration between multimodal manual generation and action execution. Unlike prior VLA models that directly map sensory inputs to actions, we first equip ManualVLA with a planning expert that generates intermediate manuals consisting of images, position prompts, and textual instructions. Building upon these multimodal manuals, we design a Manual Chain-of-Thought (ManualCoT) reasoning process that feeds them into the action expert, where each manual step provides explicit control conditions, while its latent representation offers implicit guidance for accurate manipulation. To alleviate the burden of data collection, we develop a high-fidelity digital-twin toolkit based on 3D Gaussian Splatting, which automatically generates manual data for planning expert training. ManualVLA demonstrates strong real-world performance, achieving an average success rate 32% higher than the previous hierarchical SOTA baseline on LEGO assembly and object rearrangement tasks.

## 核心内容
Vision-Language-Action (VLA) models have recently emerged, demonstrating strong generalization in robotic scene understanding and manipulation. However, when confronted with long-horizon tasks that require defined goal states, such as LEGO assembly or object rearrangement, existing VLA models still face challenges in coordinating high-level planning with precise manipulation. Therefore, we aim to endow a VLA model with the capability to infer the "how" process from the "what" outcomes, transforming goal states into executable procedures. In this paper, we introduce ManualVLA, a unified VLA framework built upon a Mixture-of-Transformers (MoT) architecture, enabling coherent collaboration between multimodal manual generation and action execution. Unlike prior VLA models that directly map sensory inputs to actions, we first equip ManualVLA with a planning expert that generates intermediate manuals consisting of images, position prompts, and textual instructions. Building upon these multimodal manuals, we design a Manual Chain-of-Thought (ManualCoT) reasoning process that feeds them into the action expert, where each manual step provides explicit control conditions, while its latent representation offers implicit guidance for accurate manipulation. To alleviate the burden of data collection, we develop a high-fidelity digital-twin toolkit based on 3D Gaussian Splatting, which automatically generates manual data for planning expert training. ManualVLA demonstrates strong real-world performance, achieving an average success rate 32% higher than the previous hierarchical SOTA baseline on LEGO assembly and object rearrangement tasks.

## 参考
- http://arxiv.org/abs/2512.02013v1

