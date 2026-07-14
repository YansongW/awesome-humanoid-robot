---
$id: ent_paper_wen_tinyvla_towards_fast_data_effi_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation'
  zh: TinyVLA
  ko: 'TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation'
summary:
  en: 'TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation (TinyVLA), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Shanghai University, Syracuse University, Beijing
    Innovation Center of Humanoid Robotics, East China Normal University, Midea Group AI Lab.'
  zh: 'TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation (TinyVLA), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Shanghai University, Syracuse University, Beijing
    Innovation Center of Humanoid Robotics, East China Normal University, Midea Group AI Lab.'
  ko: 'TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation (TinyVLA), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Shanghai University, Syracuse University, Beijing
    Innovation Center of Humanoid Robotics, East China Normal University, Midea Group AI Lab.'
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
- tinyvla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2409.12514v5.
sources:
- id: src_001
  type: paper
  title: 'TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2409.12514
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: TinyVLA source
  url: https://doi.org/10.48550/arXiv.2409.12514
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have shown remarkable potential in visuomotor control and instruction comprehension through end-to-end learning processes. However, current VLA models face significant challenges: they are slow during inference and require extensive pre-training on large amounts of robotic data, making real-world deployment difficult. In this paper, we introduce a new family of compact vision-language-action models, called TinyVLA, which offers two key advantages over existing VLA models: (1) faster inference speeds, and (2) improved data efficiency, eliminating the need for pre-training stage. Our framework incorporates two essential components to build TinyVLA: (1) initializing the policy backbone with robust, high-speed multimodal models, and (2) integrating a diffusion policy decoder during fine-tuning to enable precise robot actions. We conducted extensive evaluations of TinyVLA in both simulation and on real robots, demonstrating that our approach significantly outperforms the state-of-the-art VLA model, OpenVLA, in terms of speed and data efficiency, while delivering comparable or superior performance. Additionally, TinyVLA exhibits strong generalization capabilities across various dimensions, including language instructions, novel objects, unseen positions, changes in object appearance, background variations, and environmental shifts, often matching or exceeding the performance of OpenVLA. We believe that \methodname offers an interesting perspective on utilizing pre-trained multimodal models for policy learning. Our project is at https://tiny-vla.github.io.

## 核心内容
Vision-Language-Action (VLA) models have shown remarkable potential in visuomotor control and instruction comprehension through end-to-end learning processes. However, current VLA models face significant challenges: they are slow during inference and require extensive pre-training on large amounts of robotic data, making real-world deployment difficult. In this paper, we introduce a new family of compact vision-language-action models, called TinyVLA, which offers two key advantages over existing VLA models: (1) faster inference speeds, and (2) improved data efficiency, eliminating the need for pre-training stage. Our framework incorporates two essential components to build TinyVLA: (1) initializing the policy backbone with robust, high-speed multimodal models, and (2) integrating a diffusion policy decoder during fine-tuning to enable precise robot actions. We conducted extensive evaluations of TinyVLA in both simulation and on real robots, demonstrating that our approach significantly outperforms the state-of-the-art VLA model, OpenVLA, in terms of speed and data efficiency, while delivering comparable or superior performance. Additionally, TinyVLA exhibits strong generalization capabilities across various dimensions, including language instructions, novel objects, unseen positions, changes in object appearance, background variations, and environmental shifts, often matching or exceeding the performance of OpenVLA. We believe that \methodname offers an interesting perspective on utilizing pre-trained multimodal models for policy learning. Our project is at https://tiny-vla.github.io.

## 参考
- http://arxiv.org/abs/2409.12514v5

