---
$id: ent_paper_yang_vlaser_vision_language_action_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning'
  zh: Vlaser
  ko: 'Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning'
summary:
  en: 'Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning (Vlaser), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Science and Technology of China, Shanghai AI Laboratory, Shanghai
    Jiao Tong University, Zhejiang University, Nanjing University, Fudan University, Tsinghua University, NUS, Northeastern
    University, Shenzhen University.'
  zh: 'Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning (Vlaser), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Science and Technology of China, Shanghai AI Laboratory, Shanghai
    Jiao Tong University, Zhejiang University, Nanjing University, Fudan University, Tsinghua University, NUS, Northeastern
    University, Shenzhen University.'
  ko: 'Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning (Vlaser), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Science and Technology of China, Shanghai AI Laboratory, Shanghai
    Jiao Tong University, Zhejiang University, Nanjing University, Fudan University, Tsinghua University, NUS, Northeastern
    University, Shenzhen University.'
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
- vision_language_action
- vla
- vlaser
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.11027v2.
sources:
- id: src_001
  type: paper
  title: 'Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning (arXiv)'
  url: https://arxiv.org/abs/2510.11027
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Vlaser source
  url: https://doi.org/10.48550/arXiv.2510.11027
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
While significant research has focused on developing embodied reasoning capabilities using Vision-Language Models (VLMs) or integrating advanced VLMs into Vision-Language-Action (VLA) models for end-to-end robot control, few studies directly address the critical gap between upstream VLM-based reasoning and downstream VLA policy learning. In this work, we take an initial step toward bridging embodied reasoning with VLA policy learning by introducing Vlaser - a Vision-Language-Action Model with synergistic embodied reasoning capability, which is a foundational vision-language model designed to integrate high-level reasoning with low-level control for embodied agents. Built upon the high-quality Vlaser-6M dataset, Vlaser achieves state-of-the-art performance across a range of embodied reasoning benchmarks - including spatial reasoning, embodied grounding, embodied QA, and task planning. Furthermore, we systematically examine how different VLM initializations affect supervised VLA fine-tuning, offering novel insights into mitigating the domain shift between internet-scale pre-training data and embodied-specific policy learning data. Based on these insights, our approach achieves state-of-the-art results on the WidowX benchmark and competitive performance on the Google Robot benchmark.

## 核心内容
While significant research has focused on developing embodied reasoning capabilities using Vision-Language Models (VLMs) or integrating advanced VLMs into Vision-Language-Action (VLA) models for end-to-end robot control, few studies directly address the critical gap between upstream VLM-based reasoning and downstream VLA policy learning. In this work, we take an initial step toward bridging embodied reasoning with VLA policy learning by introducing Vlaser - a Vision-Language-Action Model with synergistic embodied reasoning capability, which is a foundational vision-language model designed to integrate high-level reasoning with low-level control for embodied agents. Built upon the high-quality Vlaser-6M dataset, Vlaser achieves state-of-the-art performance across a range of embodied reasoning benchmarks - including spatial reasoning, embodied grounding, embodied QA, and task planning. Furthermore, we systematically examine how different VLM initializations affect supervised VLA fine-tuning, offering novel insights into mitigating the domain shift between internet-scale pre-training data and embodied-specific policy learning data. Based on these insights, our approach achieves state-of-the-art results on the WidowX benchmark and competitive performance on the Google Robot benchmark.

## 参考
- http://arxiv.org/abs/2510.11027v2

