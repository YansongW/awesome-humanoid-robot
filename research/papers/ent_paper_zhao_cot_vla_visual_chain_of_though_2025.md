---
$id: ent_paper_zhao_cot_vla_visual_chain_of_though_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models'
  zh: CoT-VLA
  ko: 'CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models'
summary:
  en: 'CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models (CoT-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by NVIDIA, Stanford University, MIT, and published at CVPR25.'
  zh: 'CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models (CoT-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by NVIDIA, Stanford University, MIT, and published at CVPR25.'
  ko: 'CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models (CoT-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by NVIDIA, Stanford University, MIT, and published at CVPR25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- cot_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.22020v1.
sources:
- id: src_001
  type: website
  title: CoT-VLA source
  url: https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.html
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action models (VLAs) have shown potential in leveraging pretrained vision-language models and diverse robot demonstrations for learning generalizable sensorimotor control. While this paradigm effectively utilizes large-scale data from both robotic and non-robotic sources, current VLAs primarily focus on direct input--output mappings, lacking the intermediate reasoning steps crucial for complex manipulation tasks. As a result, existing VLAs lack temporal planning or reasoning capabilities. In this paper, we introduce a method that incorporates explicit visual chain-of-thought (CoT) reasoning into vision-language-action models (VLAs) by predicting future image frames autoregressively as visual goals before generating a short action sequence to achieve these goals. We introduce CoT-VLA, a state-of-the-art 7B VLA that can understand and generate visual and action tokens. Our experimental results demonstrate that CoT-VLA achieves strong performance, outperforming the state-of-the-art VLA model by 17% in real-world manipulation tasks and 6% in simulation benchmarks. Project website: https://cot-vla.github.io/

## 核心内容
Vision-language-action models (VLAs) have shown potential in leveraging pretrained vision-language models and diverse robot demonstrations for learning generalizable sensorimotor control. While this paradigm effectively utilizes large-scale data from both robotic and non-robotic sources, current VLAs primarily focus on direct input--output mappings, lacking the intermediate reasoning steps crucial for complex manipulation tasks. As a result, existing VLAs lack temporal planning or reasoning capabilities. In this paper, we introduce a method that incorporates explicit visual chain-of-thought (CoT) reasoning into vision-language-action models (VLAs) by predicting future image frames autoregressively as visual goals before generating a short action sequence to achieve these goals. We introduce CoT-VLA, a state-of-the-art 7B VLA that can understand and generate visual and action tokens. Our experimental results demonstrate that CoT-VLA achieves strong performance, outperforming the state-of-the-art VLA model by 17% in real-world manipulation tasks and 6% in simulation benchmarks. Project website: https://cot-vla.github.io/

## 参考
- http://arxiv.org/abs/2503.22020v1

