---
$id: ent_paper_learning_humanoid_locomotion_w_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Humanoid Locomotion with Perceptive Internal Model
  zh: Learning Humanoid Locomotion with Perceptive Internal Model
  ko: Learning Humanoid Locomotion with Perceptive Internal Model
summary:
  en: Learning Humanoid Locomotion with Perceptive Internal Model is a 2024 work on locomotion for humanoid robots.
  zh: Learning Humanoid Locomotion with Perceptive Internal Model is a 2024 work on locomotion for humanoid robots.
  ko: Learning Humanoid Locomotion with Perceptive Internal Model is a 2024 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- learning_humanoid_locomotion_w
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2411.14386v1.
sources:
- id: src_001
  type: paper
  title: Learning Humanoid Locomotion with Perceptive Internal Model (arXiv)
  url: https://arxiv.org/abs/2411.14386
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
In contrast to quadruped robots that can navigate diverse terrains using a "blind" policy, humanoid robots require accurate perception for stable locomotion due to their high degrees of freedom and inherently unstable morphology. However, incorporating perceptual signals often introduces additional disturbances to the system, potentially reducing its robustness, generalizability, and efficiency. This paper presents the Perceptive Internal Model (PIM), which relies on onboard, continuously updated elevation maps centered around the robot to perceive its surroundings. We train the policy using ground-truth obstacle heights surrounding the robot in simulation, optimizing it based on the Hybrid Internal Model (HIM), and perform inference with heights sampled from the constructed elevation map. Unlike previous methods that directly encode depth maps or raw point clouds, our approach allows the robot to perceive the terrain beneath its feet clearly and is less affected by camera movement or noise. Furthermore, since depth map rendering is not required in simulation, our method introduces minimal additional computational costs and can train the policy in 3 hours on an RTX 4090 GPU. We verify the effectiveness of our method across various humanoid robots, various indoor and outdoor terrains, stairs, and various sensor configurations. Our method can enable a humanoid robot to continuously climb stairs and has the potential to serve as a foundational algorithm for the development of future humanoid control methods.

## 核心内容
In contrast to quadruped robots that can navigate diverse terrains using a "blind" policy, humanoid robots require accurate perception for stable locomotion due to their high degrees of freedom and inherently unstable morphology. However, incorporating perceptual signals often introduces additional disturbances to the system, potentially reducing its robustness, generalizability, and efficiency. This paper presents the Perceptive Internal Model (PIM), which relies on onboard, continuously updated elevation maps centered around the robot to perceive its surroundings. We train the policy using ground-truth obstacle heights surrounding the robot in simulation, optimizing it based on the Hybrid Internal Model (HIM), and perform inference with heights sampled from the constructed elevation map. Unlike previous methods that directly encode depth maps or raw point clouds, our approach allows the robot to perceive the terrain beneath its feet clearly and is less affected by camera movement or noise. Furthermore, since depth map rendering is not required in simulation, our method introduces minimal additional computational costs and can train the policy in 3 hours on an RTX 4090 GPU. We verify the effectiveness of our method across various humanoid robots, various indoor and outdoor terrains, stairs, and various sensor configurations. Our method can enable a humanoid robot to continuously climb stairs and has the potential to serve as a foundational algorithm for the development of future humanoid control methods.

## 参考
- http://arxiv.org/abs/2411.14386v1

