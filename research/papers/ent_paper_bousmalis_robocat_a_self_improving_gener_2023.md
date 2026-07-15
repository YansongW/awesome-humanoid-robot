---
$id: ent_paper_bousmalis_robocat_a_self_improving_gener_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation'
  zh: RoboCat
  ko: 'RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation'
summary:
  en: 'RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation (RoboCat), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Google DeepMind, and published at Trans. Mach. Learn. Res. 2024.'
  zh: 'RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation (RoboCat), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Google DeepMind, and published at Trans. Mach. Learn. Res. 2024.'
  ko: 'RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation (RoboCat), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Google DeepMind, and published at Trans. Mach. Learn. Res. 2024.'
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
- robocat
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2306.11706v2.
sources:
- id: src_001
  type: paper
  title: RoboCat source
  url: https://openreview.net/forum?id=vsCpILiWHu
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
The ability to leverage heterogeneous robotic experience from different robots and tasks to quickly master novel skills and embodiments has the potential to transform robot learning. Inspired by recent advances in foundation models for vision and language, we propose a multi-embodiment, multi-task generalist agent for robotic manipulation. This agent, named RoboCat, is a visual goal-conditioned decision transformer capable of consuming action-labelled visual experience. This data spans a large repertoire of motor control skills from simulated and real robotic arms with varying sets of observations and actions. With RoboCat, we demonstrate the ability to generalise to new tasks and robots, both zero-shot as well as through adaptation using only 100-1000 examples for the target task. We also show how a trained model itself can be used to generate data for subsequent training iterations, thus providing a basic building block for an autonomous improvement loop. We investigate the agent's capabilities, with large-scale evaluations both in simulation and on three different real robot embodiments. We find that as we grow and diversify its training data, RoboCat not only shows signs of cross-task transfer, but also becomes more efficient at adapting to new tasks.

## 核心内容
The ability to leverage heterogeneous robotic experience from different robots and tasks to quickly master novel skills and embodiments has the potential to transform robot learning. Inspired by recent advances in foundation models for vision and language, we propose a multi-embodiment, multi-task generalist agent for robotic manipulation. This agent, named RoboCat, is a visual goal-conditioned decision transformer capable of consuming action-labelled visual experience. This data spans a large repertoire of motor control skills from simulated and real robotic arms with varying sets of observations and actions. With RoboCat, we demonstrate the ability to generalise to new tasks and robots, both zero-shot as well as through adaptation using only 100-1000 examples for the target task. We also show how a trained model itself can be used to generate data for subsequent training iterations, thus providing a basic building block for an autonomous improvement loop. We investigate the agent's capabilities, with large-scale evaluations both in simulation and on three different real robot embodiments. We find that as we grow and diversify its training data, RoboCat not only shows signs of cross-task transfer, but also becomes more efficient at adapting to new tasks.

## 参考
- http://arxiv.org/abs/2306.11706v2

