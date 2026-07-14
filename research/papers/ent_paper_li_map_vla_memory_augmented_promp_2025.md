---
$id: ent_paper_li_map_vla_memory_augmented_promp_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MAP-VLA: Memory-Augmented Prompting for Vision-Language-Action Model in Robotic Manipulation'
  zh: MAP-VLA
  ko: 'MAP-VLA: Memory-Augmented Prompting for Vision-Language-Action Model in Robotic Manipulation'
summary:
  en: 'MAP-VLA: Memory-Augmented Prompting for Vision-Language-Action Model in Robotic Manipulation (MAP-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Nanyang Technological University, VinUniversity,
    Beijing University of Posts and Telecommunications, Tsinghua University, South China University of Technolog.'
  zh: 'MAP-VLA: Memory-Augmented Prompting for Vision-Language-Action Model in Robotic Manipulation (MAP-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Nanyang Technological University, VinUniversity,
    Beijing University of Posts and Telecommunications, Tsinghua University, South China University of Technolog.'
  ko: 'MAP-VLA: Memory-Augmented Prompting for Vision-Language-Action Model in Robotic Manipulation (MAP-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Nanyang Technological University, VinUniversity,
    Beijing University of Posts and Telecommunications, Tsinghua University, South China University of Technolog.'
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
- map_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.09516v1.
sources:
- id: src_001
  type: paper
  title: 'MAP-VLA: Memory-Augmented Prompting for Vision-Language-Action Model in Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2511.09516
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MAP-VLA source
  url: https://doi.org/10.48550/arXiv.2511.09516
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Pre-trained Vision-Language-Action (VLA) models have achieved remarkable success in improving robustness and generalization for end-to-end robotic manipulation. However, these models struggle with long-horizon tasks due to their lack of memory and reliance solely on immediate sensory inputs. To address this limitation, we propose Memory-Augmented Prompting for Vision-Language-Action model (MAP-VLA), a novel framework that empowers pre-trained VLA models with demonstration-derived memory prompts to augment action generation for long-horizon robotic manipulation tasks. To achieve this, MAP-VLA first constructs a memory library from historical demonstrations, where each memory unit captures information about a specific stage of a task. These memory units are implemented as learnable soft prompts optimized through prompt tuning. Then, during real-time task execution, MAP-VLA retrieves relevant memory through trajectory similarity matching and dynamically integrates it into the VLA model for augmented action generation. Importantly, this prompt tuning and retrieval augmentation approach operates as a plug-and-play module for a frozen VLA model, offering a lightweight and flexible solution to improve task performance. Experimental results show that MAP-VLA delivers up to 7.0% absolute performance gains in the simulation benchmark and 25.0% on real robot evaluations for long-horizon tasks, surpassing the current state-of-the-art methods.

## 核心内容
Pre-trained Vision-Language-Action (VLA) models have achieved remarkable success in improving robustness and generalization for end-to-end robotic manipulation. However, these models struggle with long-horizon tasks due to their lack of memory and reliance solely on immediate sensory inputs. To address this limitation, we propose Memory-Augmented Prompting for Vision-Language-Action model (MAP-VLA), a novel framework that empowers pre-trained VLA models with demonstration-derived memory prompts to augment action generation for long-horizon robotic manipulation tasks. To achieve this, MAP-VLA first constructs a memory library from historical demonstrations, where each memory unit captures information about a specific stage of a task. These memory units are implemented as learnable soft prompts optimized through prompt tuning. Then, during real-time task execution, MAP-VLA retrieves relevant memory through trajectory similarity matching and dynamically integrates it into the VLA model for augmented action generation. Importantly, this prompt tuning and retrieval augmentation approach operates as a plug-and-play module for a frozen VLA model, offering a lightweight and flexible solution to improve task performance. Experimental results show that MAP-VLA delivers up to 7.0% absolute performance gains in the simulation benchmark and 25.0% on real robot evaluations for long-horizon tasks, surpassing the current state-of-the-art methods.

## 参考
- http://arxiv.org/abs/2511.09516v1

