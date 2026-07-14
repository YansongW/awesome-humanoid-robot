---
$id: ent_paper_wang_vla_adapter_an_effective_parad_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model'
  zh: VLA-Adapter
  ko: 'VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model'
summary:
  en: 'VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model (VLA-Adapter), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Beijing University of Posts and Telecommunications, Westlake University,
    Zhejiang University, OpenHelix Team, State Key Laboratory of Networking and Switching Technology, The Hong Kong University
    of Science and Technology (Guangzhou).'
  zh: 'VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model (VLA-Adapter), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Beijing University of Posts and Telecommunications, Westlake University,
    Zhejiang University, OpenHelix Team, State Key Laboratory of Networking and Switching Technology, The Hong Kong University
    of Science and Technology (Guangzhou).'
  ko: 'VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model (VLA-Adapter), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Beijing University of Posts and Telecommunications, Westlake University,
    Zhejiang University, OpenHelix Team, State Key Laboratory of Networking and Switching Technology, The Hong Kong University
    of Science and Technology (Guangzhou).'
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
- vla_adapter
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.09372v2.
sources:
- id: src_001
  type: paper
  title: 'VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model (arXiv)'
  url: https://arxiv.org/abs/2509.09372
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLA-Adapter source
  url: https://doi.org/10.48550/arXiv.2509.09372
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models typically bridge the gap between perceptual and action spaces by pre-training a large-scale Vision-Language Model (VLM) on robotic data. While this approach greatly enhances performance, it also incurs significant training costs. In this paper, we investigate how to effectively bridge vision-language (VL) representations to action (A). We introduce VLA-Adapter, a novel paradigm designed to reduce the reliance of VLA models on large-scale VLMs and extensive pre-training. To this end, we first systematically analyze the effectiveness of various VL conditions and present key findings on which conditions are essential for bridging perception and action spaces. Based on these insights, we propose a lightweight Policy module with Bridge Attention, which autonomously injects the optimal condition into the action space. In this way, our method achieves high performance using only a 0.5B-parameter backbone, without any robotic data pre-training. Extensive experiments on both simulated and real-world robotic benchmarks demonstrate that VLA-Adapter not only achieves state-of-the-art level performance, but also offers the fast inference speed reported to date. Furthermore, thanks to the proposed advanced bridging paradigm, VLA-Adapter enables the training of a powerful VLA model in just 8 hours on a single consumer-grade GPU, greatly lowering the barrier to deploying the VLA model. Project page: https://vla-adapter.github.io/.

## 核心内容
Vision-Language-Action (VLA) models typically bridge the gap between perceptual and action spaces by pre-training a large-scale Vision-Language Model (VLM) on robotic data. While this approach greatly enhances performance, it also incurs significant training costs. In this paper, we investigate how to effectively bridge vision-language (VL) representations to action (A). We introduce VLA-Adapter, a novel paradigm designed to reduce the reliance of VLA models on large-scale VLMs and extensive pre-training. To this end, we first systematically analyze the effectiveness of various VL conditions and present key findings on which conditions are essential for bridging perception and action spaces. Based on these insights, we propose a lightweight Policy module with Bridge Attention, which autonomously injects the optimal condition into the action space. In this way, our method achieves high performance using only a 0.5B-parameter backbone, without any robotic data pre-training. Extensive experiments on both simulated and real-world robotic benchmarks demonstrate that VLA-Adapter not only achieves state-of-the-art level performance, but also offers the fast inference speed reported to date. Furthermore, thanks to the proposed advanced bridging paradigm, VLA-Adapter enables the training of a powerful VLA model in just 8 hours on a single consumer-grade GPU, greatly lowering the barrier to deploying the VLA model. Project page: https://vla-adapter.github.io/.

## 参考
- http://arxiv.org/abs/2509.09372v2

