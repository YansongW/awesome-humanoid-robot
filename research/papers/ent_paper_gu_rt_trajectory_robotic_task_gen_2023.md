---
$id: ent_paper_gu_rt_trajectory_robotic_task_gen_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches'
  zh: RT-Trajectory
  ko: 'RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches'
summary:
  en: 'RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches (RT-Trajectory), is a 2023 generalized
    vision-language-action model for robotic manipulation, introduced by Google DeepMind, University of California San Diego,
    Stanford University, Intrinsic, and published at ICLR 2023.'
  zh: 'RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches (RT-Trajectory), is a 2023 generalized
    vision-language-action model for robotic manipulation, introduced by Google DeepMind, University of California San Diego,
    Stanford University, Intrinsic, and published at ICLR 2023.'
  ko: 'RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches (RT-Trajectory), is a 2023 generalized
    vision-language-action model for robotic manipulation, introduced by Google DeepMind, University of California San Diego,
    Stanford University, Intrinsic, and published at ICLR 2023.'
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
- rt_trajectory
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2311.01977v2.
sources:
- id: src_001
  type: paper
  title: RT-Trajectory source
  url: https://openreview.net/forum?id=F1TKzG8LJO
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
Generalization remains one of the most important desiderata for robust robot learning systems. While recently proposed approaches show promise in generalization to novel objects, semantic concepts, or visual distribution shifts, generalization to new tasks remains challenging. For example, a language-conditioned policy trained on pick-and-place tasks will not be able to generalize to a folding task, even if the arm trajectory of folding is similar to pick-and-place. Our key insight is that this kind of generalization becomes feasible if we represent the task through rough trajectory sketches. We propose a policy conditioning method using such rough trajectory sketches, which we call RT-Trajectory, that is practical, easy to specify, and allows the policy to effectively perform new tasks that would otherwise be challenging to perform. We find that trajectory sketches strike a balance between being detailed enough to express low-level motion-centric guidance while being coarse enough to allow the learned policy to interpret the trajectory sketch in the context of situational visual observations. In addition, we show how trajectory sketches can provide a useful interface to communicate with robotic policies: they can be specified through simple human inputs like drawings or videos, or through automated methods such as modern image-generating or waypoint-generating methods. We evaluate RT-Trajectory at scale on a variety of real-world robotic tasks, and find that RT-Trajectory is able to perform a wider range of tasks compared to language-conditioned and goal-conditioned policies, when provided the same training data.

## 核心内容
Generalization remains one of the most important desiderata for robust robot learning systems. While recently proposed approaches show promise in generalization to novel objects, semantic concepts, or visual distribution shifts, generalization to new tasks remains challenging. For example, a language-conditioned policy trained on pick-and-place tasks will not be able to generalize to a folding task, even if the arm trajectory of folding is similar to pick-and-place. Our key insight is that this kind of generalization becomes feasible if we represent the task through rough trajectory sketches. We propose a policy conditioning method using such rough trajectory sketches, which we call RT-Trajectory, that is practical, easy to specify, and allows the policy to effectively perform new tasks that would otherwise be challenging to perform. We find that trajectory sketches strike a balance between being detailed enough to express low-level motion-centric guidance while being coarse enough to allow the learned policy to interpret the trajectory sketch in the context of situational visual observations. In addition, we show how trajectory sketches can provide a useful interface to communicate with robotic policies: they can be specified through simple human inputs like drawings or videos, or through automated methods such as modern image-generating or waypoint-generating methods. We evaluate RT-Trajectory at scale on a variety of real-world robotic tasks, and find that RT-Trajectory is able to perform a wider range of tasks compared to language-conditioned and goal-conditioned policies, when provided the same training data.

## 参考
- http://arxiv.org/abs/2311.01977v2

