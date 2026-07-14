---
$id: ent_paper_chen_intentionvla_generalizable_and_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'IntentionVLA: Generalizable and Efficient Embodied Intention Reasoning for Human-Robot Interaction'
  zh: IntentionVLA
  ko: 'IntentionVLA: Generalizable and Efficient Embodied Intention Reasoning for Human-Robot Interaction'
summary:
  en: 'IntentionVLA: Generalizable and Efficient Embodied Intention Reasoning for Human-Robot Interaction (IntentionVLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Harbin Institute of Technology (Shenzhen),
    Nanjing University, University of Science and Technology of China, Dexmal.'
  zh: 'IntentionVLA: Generalizable and Efficient Embodied Intention Reasoning for Human-Robot Interaction (IntentionVLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Harbin Institute of Technology (Shenzhen),
    Nanjing University, University of Science and Technology of China, Dexmal.'
  ko: 'IntentionVLA: Generalizable and Efficient Embodied Intention Reasoning for Human-Robot Interaction (IntentionVLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Harbin Institute of Technology (Shenzhen),
    Nanjing University, University of Science and Technology of China, Dexmal.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- intentionvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.07778v1.
sources:
- id: src_001
  type: paper
  title: 'IntentionVLA: Generalizable and Efficient Embodied Intention Reasoning for Human-Robot Interaction (arXiv)'
  url: https://arxiv.org/abs/2510.07778
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: IntentionVLA source
  url: https://doi.org/10.48550/arXiv.2510.07778
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models leverage pretrained vision-language models (VLMs) to couple perception with robotic control, offering a promising path toward general-purpose embodied intelligence. However, current SOTA VLAs are primarily pretrained on multimodal tasks with limited relevance to embodied scenarios, and then finetuned to map explicit instructions to actions. Consequently, due to the lack of reasoning-intensive pretraining and reasoning-guided manipulation, these models are unable to perform implicit human intention reasoning required for complex, real-world interactions. To overcome these limitations, we propose \textbf{IntentionVLA}, a VLA framework with a curriculum training paradigm and an efficient inference mechanism. Our proposed method first leverages carefully designed reasoning data that combine intention inference, spatial grounding, and compact embodied reasoning, endowing the model with both reasoning and perception capabilities. In the following finetuning stage, IntentionVLA employs the compact reasoning outputs as contextual guidance for action generation, enabling fast inference under indirect instructions. Experimental results show that IntentionVLA substantially outperforms $π_0$, achieving 18\% higher success rates with direct instructions and 28\% higher than ECoT under intention instructions. On out-of-distribution intention tasks, IntentionVLA achieves over twice the success rate of all baselines, and further enables zero-shot human-robot interaction with 40\% success rate. These results highlight IntentionVLA as a promising paradigm for next-generation human-robot interaction (HRI) systems.

## 核心内容
Vision-Language-Action (VLA) models leverage pretrained vision-language models (VLMs) to couple perception with robotic control, offering a promising path toward general-purpose embodied intelligence. However, current SOTA VLAs are primarily pretrained on multimodal tasks with limited relevance to embodied scenarios, and then finetuned to map explicit instructions to actions. Consequently, due to the lack of reasoning-intensive pretraining and reasoning-guided manipulation, these models are unable to perform implicit human intention reasoning required for complex, real-world interactions. To overcome these limitations, we propose \textbf{IntentionVLA}, a VLA framework with a curriculum training paradigm and an efficient inference mechanism. Our proposed method first leverages carefully designed reasoning data that combine intention inference, spatial grounding, and compact embodied reasoning, endowing the model with both reasoning and perception capabilities. In the following finetuning stage, IntentionVLA employs the compact reasoning outputs as contextual guidance for action generation, enabling fast inference under indirect instructions. Experimental results show that IntentionVLA substantially outperforms $π_0$, achieving 18\% higher success rates with direct instructions and 28\% higher than ECoT under intention instructions. On out-of-distribution intention tasks, IntentionVLA achieves over twice the success rate of all baselines, and further enables zero-shot human-robot interaction with 40\% success rate. These results highlight IntentionVLA as a promising paradigm for next-generation human-robot interaction (HRI) systems.

## 参考
- http://arxiv.org/abs/2510.07778v1

