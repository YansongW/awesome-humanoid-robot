---
$id: ent_paper_nomad_goal_masked_diffusion_po_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration'
  zh: 'NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration'
  ko: 'NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration'
summary:
  en: 'NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration is a 2023 work on navigation for humanoid robots.'
  zh: 'NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration is a 2023 work on navigation for humanoid robots.'
  ko: 'NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration is a 2023 work on navigation for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- navigation
- nomad
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2310.07896v1.
sources:
- id: src_001
  type: paper
  title: 'NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration (arXiv)'
  url: https://arxiv.org/abs/2310.07896
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
Robotic learning for navigation in unfamiliar environments needs to provide policies for both task-oriented navigation (i.e., reaching a goal that the robot has located), and task-agnostic exploration (i.e., searching for a goal in a novel setting). Typically, these roles are handled by separate models, for example by using subgoal proposals, planning, or separate navigation strategies. In this paper, we describe how we can train a single unified diffusion policy to handle both goal-directed navigation and goal-agnostic exploration, with the latter providing the ability to search novel environments, and the former providing the ability to reach a user-specified goal once it has been located. We show that this unified policy results in better overall performance when navigating to visually indicated goals in novel environments, as compared to approaches that use subgoal proposals from generative models, or prior methods based on latent variable models. We instantiate our method by using a large-scale Transformer-based policy trained on data from multiple ground robots, with a diffusion model decoder to flexibly handle both goal-conditioned and goal-agnostic navigation. Our experiments, conducted on a real-world mobile robot platform, show effective navigation in unseen environments in comparison with five alternative methods, and demonstrate significant improvements in performance and lower collision rates, despite utilizing smaller models than state-of-the-art approaches. For more videos, code, and pre-trained model checkpoints, see https://general-navigation-models.github.io/nomad/

## 核心内容
Robotic learning for navigation in unfamiliar environments needs to provide policies for both task-oriented navigation (i.e., reaching a goal that the robot has located), and task-agnostic exploration (i.e., searching for a goal in a novel setting). Typically, these roles are handled by separate models, for example by using subgoal proposals, planning, or separate navigation strategies. In this paper, we describe how we can train a single unified diffusion policy to handle both goal-directed navigation and goal-agnostic exploration, with the latter providing the ability to search novel environments, and the former providing the ability to reach a user-specified goal once it has been located. We show that this unified policy results in better overall performance when navigating to visually indicated goals in novel environments, as compared to approaches that use subgoal proposals from generative models, or prior methods based on latent variable models. We instantiate our method by using a large-scale Transformer-based policy trained on data from multiple ground robots, with a diffusion model decoder to flexibly handle both goal-conditioned and goal-agnostic navigation. Our experiments, conducted on a real-world mobile robot platform, show effective navigation in unseen environments in comparison with five alternative methods, and demonstrate significant improvements in performance and lower collision rates, despite utilizing smaller models than state-of-the-art approaches. For more videos, code, and pre-trained model checkpoints, see https://general-navigation-models.github.io/nomad/

## 参考
- http://arxiv.org/abs/2310.07896v1

