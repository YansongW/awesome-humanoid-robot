---
$id: ent_paper_kim_fine_tuning_vision_language_ac_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success'
  zh: OpenVLA-OFT
  ko: 'Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success'
summary:
  en: 'Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success (OpenVLA-OFT), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Stanford University, and published at RSS 2025.'
  zh: 'Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success (OpenVLA-OFT), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Stanford University, and published at RSS 2025.'
  ko: 'Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success (OpenVLA-OFT), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Stanford University, and published at RSS 2025.'
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
- openvla_oft
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.19645v2.
sources:
- id: src_001
  type: paper
  title: 'Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success (arXiv)'
  url: https://arxiv.org/abs/2502.19645
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: OpenVLA-OFT source
  url: https://doi.org/10.48550/arXiv.2502.19645
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent vision-language-action models (VLAs) build upon pretrained vision-language models and leverage diverse robot datasets to demonstrate strong task execution, language following ability, and semantic generalization. Despite these successes, VLAs struggle with novel robot setups and require fine-tuning to achieve good performance, yet how to most effectively fine-tune them is unclear given many possible strategies. In this work, we study key VLA adaptation design choices such as different action decoding schemes, action representations, and learning objectives for fine-tuning, using OpenVLA as our representative base model. Our empirical analysis informs an Optimized Fine-Tuning (OFT) recipe that integrates parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective to altogether improve inference efficiency, policy performance, and flexibility in the model's input-output specifications. We propose OpenVLA-OFT, an instantiation of this recipe, which sets a new state of the art on the LIBERO simulation benchmark, significantly boosting OpenVLA's average success rate across four task suites from 76.5% to 97.1% while increasing action generation throughput by 26$\times$. In real-world evaluations, our fine-tuning recipe enables OpenVLA to successfully execute dexterous, high-frequency control tasks on a bimanual ALOHA robot and outperform other VLAs ($π_0$ and RDT-1B) fine-tuned using their default recipes, as well as strong imitation learning policies trained from scratch (Diffusion Policy and ACT) by up to 15% (absolute) in average success rate. We release code for OFT and pretrained model checkpoints at https://openvla-oft.github.io/.

## 核心内容
Recent vision-language-action models (VLAs) build upon pretrained vision-language models and leverage diverse robot datasets to demonstrate strong task execution, language following ability, and semantic generalization. Despite these successes, VLAs struggle with novel robot setups and require fine-tuning to achieve good performance, yet how to most effectively fine-tune them is unclear given many possible strategies. In this work, we study key VLA adaptation design choices such as different action decoding schemes, action representations, and learning objectives for fine-tuning, using OpenVLA as our representative base model. Our empirical analysis informs an Optimized Fine-Tuning (OFT) recipe that integrates parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective to altogether improve inference efficiency, policy performance, and flexibility in the model's input-output specifications. We propose OpenVLA-OFT, an instantiation of this recipe, which sets a new state of the art on the LIBERO simulation benchmark, significantly boosting OpenVLA's average success rate across four task suites from 76.5% to 97.1% while increasing action generation throughput by 26$\times$. In real-world evaluations, our fine-tuning recipe enables OpenVLA to successfully execute dexterous, high-frequency control tasks on a bimanual ALOHA robot and outperform other VLAs ($π_0$ and RDT-1B) fine-tuned using their default recipes, as well as strong imitation learning policies trained from scratch (Diffusion Policy and ACT) by up to 15% (absolute) in average success rate. We release code for OFT and pretrained model checkpoints at https://openvla-oft.github.io/.

## 参考
- http://arxiv.org/abs/2502.19645v2

