---
$id: ent_paper_reuss_flower_democratizing_generalis_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FLOWER: Democratizing Generalist Robot Policies with Efficient Vision-Language-Action Flow Policies'
  zh: FLOWER
  ko: 'FLOWER: Democratizing Generalist Robot Policies with Efficient Vision-Language-Action Flow Policies'
summary:
  en: 'FLOWER: Democratizing Generalist Robot Policies with Efficient Vision-Language-Action Flow Policies (FLOWER), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Karlsruhe Institute of Technology, Microsoft
    Research, and published at CoRL25.'
  zh: 'FLOWER: Democratizing Generalist Robot Policies with Efficient Vision-Language-Action Flow Policies (FLOWER), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Karlsruhe Institute of Technology, Microsoft
    Research, and published at CoRL25.'
  ko: 'FLOWER: Democratizing Generalist Robot Policies with Efficient Vision-Language-Action Flow Policies (FLOWER), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Karlsruhe Institute of Technology, Microsoft
    Research, and published at CoRL25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- flower
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.04996v1.
sources:
- id: src_001
  type: paper
  title: 'FLOWER: Democratizing Generalist Robot Policies with Efficient Vision-Language-Action Flow Policies (arXiv)'
  url: https://arxiv.org/abs/2509.04996
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: FLOWER source
  url: https://doi.org/10.48550/arXiv.2509.04996
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Developing efficient Vision-Language-Action (VLA) policies is crucial for practical robotics deployment, yet current approaches face prohibitive computational costs and resource requirements. Existing diffusion-based VLA policies require multi-billion-parameter models and massive datasets to achieve strong performance. We tackle this efficiency challenge with two contributions: intermediate-modality fusion, which reallocates capacity to the diffusion head by pruning up to $50\%$ of LLM layers, and action-specific Global-AdaLN conditioning, which cuts parameters by $20\%$ through modular adaptation. We integrate these advances into a novel 950 M-parameter VLA called FLOWER. Pretrained in just 200 H100 GPU hours, FLOWER delivers competitive performance with bigger VLAs across $190$ tasks spanning ten simulation and real-world benchmarks and demonstrates robustness across diverse robotic embodiments. In addition, FLOWER achieves a new SoTA of 4.53 on the CALVIN ABC benchmark. Demos, code and pretrained weights are available at https://intuitive-robots.github.io/flower_vla/.

## 核心内容
Developing efficient Vision-Language-Action (VLA) policies is crucial for practical robotics deployment, yet current approaches face prohibitive computational costs and resource requirements. Existing diffusion-based VLA policies require multi-billion-parameter models and massive datasets to achieve strong performance. We tackle this efficiency challenge with two contributions: intermediate-modality fusion, which reallocates capacity to the diffusion head by pruning up to $50\%$ of LLM layers, and action-specific Global-AdaLN conditioning, which cuts parameters by $20\%$ through modular adaptation. We integrate these advances into a novel 950 M-parameter VLA called FLOWER. Pretrained in just 200 H100 GPU hours, FLOWER delivers competitive performance with bigger VLAs across $190$ tasks spanning ten simulation and real-world benchmarks and demonstrates robustness across diverse robotic embodiments. In addition, FLOWER achieves a new SoTA of 4.53 on the CALVIN ABC benchmark. Demos, code and pretrained weights are available at https://intuitive-robots.github.io/flower_vla/.

## 参考
- http://arxiv.org/abs/2509.04996v1

