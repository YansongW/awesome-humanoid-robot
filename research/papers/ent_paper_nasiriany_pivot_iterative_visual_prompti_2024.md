---
$id: ent_paper_nasiriany_pivot_iterative_visual_prompti_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PIVOT: Iterative Visual Prompting Elicits Actionable Knowledge for VLMs'
  zh: PIVOT
  ko: 'PIVOT: Iterative Visual Prompting Elicits Actionable Knowledge for VLMs'
summary:
  en: 'PIVOT: Iterative Visual Prompting Elicits Actionable Knowledge for VLMs (PIVOT), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by Google DeepMind, Stanford University, The University of Texas at Austin,
    and published at ICML 2024.'
  zh: 'PIVOT: Iterative Visual Prompting Elicits Actionable Knowledge for VLMs (PIVOT), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by Google DeepMind, Stanford University, The University of Texas at Austin,
    and published at ICML 2024.'
  ko: 'PIVOT: Iterative Visual Prompting Elicits Actionable Knowledge for VLMs (PIVOT), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by Google DeepMind, Stanford University, The University of Texas at Austin,
    and published at ICML 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- pivot
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2402.07872v1.
sources:
- id: src_001
  type: paper
  title: PIVOT source
  url: https://openreview.net/forum?id=051jaf8MQy
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Vision language models (VLMs) have shown impressive capabilities across a variety of tasks, from logical reasoning to visual understanding. This opens the door to richer interaction with the world, for example robotic control. However, VLMs produce only textual outputs, while robotic control and other spatial tasks require outputting continuous coordinates, actions, or trajectories. How can we enable VLMs to handle such settings without fine-tuning on task-specific data?   In this paper, we propose a novel visual prompting approach for VLMs that we call Prompting with Iterative Visual Optimization (PIVOT), which casts tasks as iterative visual question answering. In each iteration, the image is annotated with a visual representation of proposals that the VLM can refer to (e.g., candidate robot actions, localizations, or trajectories). The VLM then selects the best ones for the task. These proposals are iteratively refined, allowing the VLM to eventually zero in on the best available answer. We investigate PIVOT on real-world robotic navigation, real-world manipulation from images, instruction following in simulation, and additional spatial inference tasks such as localization. We find, perhaps surprisingly, that our approach enables zero-shot control of robotic systems without any robot training data, navigation in a variety of environments, and other capabilities. Although current performance is far from perfect, our work highlights potentials and limitations of this new regime and shows a promising approach for Internet-Scale VLMs in robotic and spatial reasoning domains. Website: pivot-prompt.github.io and HuggingFace: https://huggingface.co/spaces/pivot-prompt/pivot-prompt-demo.

## 核心内容
Vision language models (VLMs) have shown impressive capabilities across a variety of tasks, from logical reasoning to visual understanding. This opens the door to richer interaction with the world, for example robotic control. However, VLMs produce only textual outputs, while robotic control and other spatial tasks require outputting continuous coordinates, actions, or trajectories. How can we enable VLMs to handle such settings without fine-tuning on task-specific data?   In this paper, we propose a novel visual prompting approach for VLMs that we call Prompting with Iterative Visual Optimization (PIVOT), which casts tasks as iterative visual question answering. In each iteration, the image is annotated with a visual representation of proposals that the VLM can refer to (e.g., candidate robot actions, localizations, or trajectories). The VLM then selects the best ones for the task. These proposals are iteratively refined, allowing the VLM to eventually zero in on the best available answer. We investigate PIVOT on real-world robotic navigation, real-world manipulation from images, instruction following in simulation, and additional spatial inference tasks such as localization. We find, perhaps surprisingly, that our approach enables zero-shot control of robotic systems without any robot training data, navigation in a variety of environments, and other capabilities. Although current performance is far from perfect, our work highlights potentials and limitations of this new regime and shows a promising approach for Internet-Scale VLMs in robotic and spatial reasoning domains. Website: pivot-prompt.github.io and HuggingFace: https://huggingface.co/spaces/pivot-prompt/pivot-prompt-demo.

## 参考
- http://arxiv.org/abs/2402.07872v1

