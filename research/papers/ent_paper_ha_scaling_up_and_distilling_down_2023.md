---
$id: ent_paper_ha_scaling_up_and_distilling_down_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Scaling Up and Distilling Down: Language-Guided Robot Skill Acquisition'
  zh: SUDD
  ko: 'Scaling Up and Distilling Down: Language-Guided Robot Skill Acquisition'
summary:
  en: 'Scaling Up and Distilling Down: Language-Guided Robot Skill Acquisition (SUDD), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Columbia University, Google DeepMind, and published at CoRL 2023.'
  zh: 'Scaling Up and Distilling Down: Language-Guided Robot Skill Acquisition (SUDD), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Columbia University, Google DeepMind, and published at CoRL 2023.'
  ko: 'Scaling Up and Distilling Down: Language-Guided Robot Skill Acquisition (SUDD), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Columbia University, Google DeepMind, and published at CoRL 2023.'
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
- robotic_manipulation
- sudd
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2307.14535v2.
sources:
- id: src_001
  type: paper
  title: SUDD source
  url: https://proceedings.mlr.press/v229/ha23a.html
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
We present a framework for robot skill acquisition, which 1) efficiently scale up data generation of language-labelled robot data and 2) effectively distills this data down into a robust multi-task language-conditioned visuo-motor policy. For (1), we use a large language model (LLM) to guide high-level planning, and sampling-based robot planners (e.g. motion or grasp samplers) for generating diverse and rich manipulation trajectories. To robustify this data-collection process, the LLM also infers a code-snippet for the success condition of each task, simultaneously enabling the data-collection process to detect failure and retry as well as the automatic labeling of trajectories with success/failure. For (2), we extend the diffusion policy single-task behavior-cloning approach to multi-task settings with language conditioning. Finally, we propose a new multi-task benchmark with 18 tasks across five domains to test long-horizon behavior, common-sense reasoning, tool-use, and intuitive physics. We find that our distilled policy successfully learned the robust retrying behavior in its data collection procedure, while improving absolute success rates by 33.2% on average across five domains. Code, data, and additional qualitative results are available on https://www.cs.columbia.edu/~huy/scalingup/.

## 核心内容
We present a framework for robot skill acquisition, which 1) efficiently scale up data generation of language-labelled robot data and 2) effectively distills this data down into a robust multi-task language-conditioned visuo-motor policy. For (1), we use a large language model (LLM) to guide high-level planning, and sampling-based robot planners (e.g. motion or grasp samplers) for generating diverse and rich manipulation trajectories. To robustify this data-collection process, the LLM also infers a code-snippet for the success condition of each task, simultaneously enabling the data-collection process to detect failure and retry as well as the automatic labeling of trajectories with success/failure. For (2), we extend the diffusion policy single-task behavior-cloning approach to multi-task settings with language conditioning. Finally, we propose a new multi-task benchmark with 18 tasks across five domains to test long-horizon behavior, common-sense reasoning, tool-use, and intuitive physics. We find that our distilled policy successfully learned the robust retrying behavior in its data collection procedure, while improving absolute success rates by 33.2% on average across five domains. Code, data, and additional qualitative results are available on https://www.cs.columbia.edu/~huy/scalingup/.

## 参考
- http://arxiv.org/abs/2307.14535v2

