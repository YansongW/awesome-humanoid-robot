---
$id: ent_paper_lynch_language_conditioned_imitation_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Language Conditioned Imitation Learning over Unstructured Data
  zh: MCIL
  ko: Language Conditioned Imitation Learning over Unstructured Data
summary:
  en: Language Conditioned Imitation Learning over Unstructured Data (MCIL), is a 2020 generalized vision-language-action
    model for robotic manipulation, introduced by Robotics at Google, and published at RSS 2021.
  zh: Language Conditioned Imitation Learning over Unstructured Data (MCIL), is a 2020 generalized vision-language-action
    model for robotic manipulation, introduced by Robotics at Google, and published at RSS 2021.
  ko: Language Conditioned Imitation Learning over Unstructured Data (MCIL), is a 2020 generalized vision-language-action
    model for robotic manipulation, introduced by Robotics at Google, and published at RSS 2021.
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
- mcil
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2005.07648v2.
sources:
- id: src_001
  type: website
  title: MCIL source
  url: https://doi.org/10.1109/LRA.2022.3196123
  date: '2020'
  accessed_at: '2026-07-01'
---
## 概述
Natural language is perhaps the most flexible and intuitive way for humans to communicate tasks to a robot. Prior work in imitation learning typically requires each task be specified with a task id or goal image -- something that is often impractical in open-world environments. On the other hand, previous approaches in instruction following allow agent behavior to be guided by language, but typically assume structure in the observations, actuators, or language that limit their applicability to complex settings like robotics. In this work, we present a method for incorporating free-form natural language conditioning into imitation learning. Our approach learns perception from pixels, natural language understanding, and multitask continuous control end-to-end as a single neural network. Unlike prior work in imitation learning, our method is able to incorporate unlabeled and unstructured demonstration data (i.e. no task or language labels). We show this dramatically improves language conditioned performance, while reducing the cost of language annotation to less than 1% of total data. At test time, a single language conditioned visuomotor policy trained with our method can perform a wide variety of robotic manipulation skills in a 3D environment, specified only with natural language descriptions of each task (e.g. "open the drawer...now pick up the block...now press the green button..."). To scale up the number of instructions an agent can follow, we propose combining text conditioned policies with large pretrained neural language models. We find this allows a policy to be robust to many out-of-distribution synonym instructions, without requiring new demonstrations. See videos of a human typing live text commands to our agent at language-play.github.io

## 核心内容
Natural language is perhaps the most flexible and intuitive way for humans to communicate tasks to a robot. Prior work in imitation learning typically requires each task be specified with a task id or goal image -- something that is often impractical in open-world environments. On the other hand, previous approaches in instruction following allow agent behavior to be guided by language, but typically assume structure in the observations, actuators, or language that limit their applicability to complex settings like robotics. In this work, we present a method for incorporating free-form natural language conditioning into imitation learning. Our approach learns perception from pixels, natural language understanding, and multitask continuous control end-to-end as a single neural network. Unlike prior work in imitation learning, our method is able to incorporate unlabeled and unstructured demonstration data (i.e. no task or language labels). We show this dramatically improves language conditioned performance, while reducing the cost of language annotation to less than 1% of total data. At test time, a single language conditioned visuomotor policy trained with our method can perform a wide variety of robotic manipulation skills in a 3D environment, specified only with natural language descriptions of each task (e.g. "open the drawer...now pick up the block...now press the green button..."). To scale up the number of instructions an agent can follow, we propose combining text conditioned policies with large pretrained neural language models. We find this allows a policy to be robust to many out-of-distribution synonym instructions, without requiring new demonstrations. See videos of a human typing live text commands to our agent at language-play.github.io

## 参考
- http://arxiv.org/abs/2005.07648v2

