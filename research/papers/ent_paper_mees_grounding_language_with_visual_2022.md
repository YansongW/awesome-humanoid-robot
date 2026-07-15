---
$id: ent_paper_mees_grounding_language_with_visual_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Grounding Language with Visual Affordances over Unstructured Data
  zh: HULC++
  ko: Grounding Language with Visual Affordances over Unstructured Data
summary:
  en: Grounding Language with Visual Affordances over Unstructured Data (HULC++), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by University of Freiburg, University of Technology Nuremberg, and published
    at ICRA 2023.
  zh: Grounding Language with Visual Affordances over Unstructured Data (HULC++), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by University of Freiburg, University of Technology Nuremberg, and published
    at ICRA 2023.
  ko: Grounding Language with Visual Affordances over Unstructured Data (HULC++), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by University of Freiburg, University of Technology Nuremberg, and published
    at ICRA 2023.
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
- hulc
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2210.01911v3.
sources:
- id: src_001
  type: website
  title: HULC++ source
  url: https://doi.org/10.1109/ICRA48891.2023.10160396
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
Recent works have shown that Large Language Models (LLMs) can be applied to ground natural language to a wide variety of robot skills. However, in practice, learning multi-task, language-conditioned robotic skills typically requires large-scale data collection and frequent human intervention to reset the environment or help correcting the current policies. In this work, we propose a novel approach to efficiently learn general-purpose language-conditioned robot skills from unstructured, offline and reset-free data in the real world by exploiting a self-supervised visuo-lingual affordance model, which requires annotating as little as 1% of the total data with language. We evaluate our method in extensive experiments both in simulated and real-world robotic tasks, achieving state-of-the-art performance on the challenging CALVIN benchmark and learning over 25 distinct visuomotor manipulation tasks with a single policy in the real world. We find that when paired with LLMs to break down abstract natural language instructions into subgoals via few-shot prompting, our method is capable of completing long-horizon, multi-tier tasks in the real world, while requiring an order of magnitude less data than previous approaches. Code and videos are available at http://hulc2.cs.uni-freiburg.de

## 核心内容
Recent works have shown that Large Language Models (LLMs) can be applied to ground natural language to a wide variety of robot skills. However, in practice, learning multi-task, language-conditioned robotic skills typically requires large-scale data collection and frequent human intervention to reset the environment or help correcting the current policies. In this work, we propose a novel approach to efficiently learn general-purpose language-conditioned robot skills from unstructured, offline and reset-free data in the real world by exploiting a self-supervised visuo-lingual affordance model, which requires annotating as little as 1% of the total data with language. We evaluate our method in extensive experiments both in simulated and real-world robotic tasks, achieving state-of-the-art performance on the challenging CALVIN benchmark and learning over 25 distinct visuomotor manipulation tasks with a single policy in the real world. We find that when paired with LLMs to break down abstract natural language instructions into subgoals via few-shot prompting, our method is capable of completing long-horizon, multi-tier tasks in the real world, while requiring an order of magnitude less data than previous approaches. Code and videos are available at http://hulc2.cs.uni-freiburg.de

## 参考
- http://arxiv.org/abs/2210.01911v3

