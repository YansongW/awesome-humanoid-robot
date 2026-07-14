---
$id: ent_paper_h_rdt_human_manipulation_enhan_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation'
  zh: 'H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation'
  ko: 'H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation'
summary:
  en: 'H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation is a 2025 work on manipulation for humanoid robots.'
  zh: 'H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation is a 2025 work on manipulation for humanoid robots.'
  ko: 'H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation is a 2025 work on manipulation for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- h_rdt
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.23523v2.
sources:
- id: src_001
  type: paper
  title: 'H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2507.23523
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Imitation learning for robotic manipulation faces a fundamental challenge: the scarcity of large-scale, high-quality robot demonstration data. Recent robotic foundation models often pre-train on cross-embodiment robot datasets to increase data scale, while they face significant limitations as the diverse morphologies and action spaces across different robot embodiments make unified training challenging. In this paper, we present H-RDT (Human to Robotics Diffusion Transformer), a novel approach that leverages human manipulation data to enhance robot manipulation capabilities. Our key insight is that large-scale egocentric human manipulation videos with paired 3D hand pose annotations provide rich behavioral priors that capture natural manipulation strategies and can benefit robotic policy learning. We introduce a two-stage training paradigm: (1) pre-training on large-scale egocentric human manipulation data, and (2) cross-embodiment fine-tuning on robot-specific data with modular action encoders and decoders. Built on a diffusion transformer architecture with 2B parameters, H-RDT uses flow matching to model complex action distributions. Extensive evaluations encompassing both simulation and real-world experiments, single-task and multitask scenarios, as well as few-shot learning and robustness assessments, demonstrate that H-RDT outperforms training from scratch and existing state-of-the-art methods, including Pi0 and RDT, achieving significant improvements of 13.9% and 40.5% over training from scratch in simulation and real-world experiments, respectively. The results validate our core hypothesis that human manipulation data can serve as a powerful foundation for learning bimanual robotic manipulation policies.

## 核心内容
Imitation learning for robotic manipulation faces a fundamental challenge: the scarcity of large-scale, high-quality robot demonstration data. Recent robotic foundation models often pre-train on cross-embodiment robot datasets to increase data scale, while they face significant limitations as the diverse morphologies and action spaces across different robot embodiments make unified training challenging. In this paper, we present H-RDT (Human to Robotics Diffusion Transformer), a novel approach that leverages human manipulation data to enhance robot manipulation capabilities. Our key insight is that large-scale egocentric human manipulation videos with paired 3D hand pose annotations provide rich behavioral priors that capture natural manipulation strategies and can benefit robotic policy learning. We introduce a two-stage training paradigm: (1) pre-training on large-scale egocentric human manipulation data, and (2) cross-embodiment fine-tuning on robot-specific data with modular action encoders and decoders. Built on a diffusion transformer architecture with 2B parameters, H-RDT uses flow matching to model complex action distributions. Extensive evaluations encompassing both simulation and real-world experiments, single-task and multitask scenarios, as well as few-shot learning and robustness assessments, demonstrate that H-RDT outperforms training from scratch and existing state-of-the-art methods, including Pi0 and RDT, achieving significant improvements of 13.9% and 40.5% over training from scratch in simulation and real-world experiments, respectively. The results validate our core hypothesis that human manipulation data can serve as a powerful foundation for learning bimanual robotic manipulation policies.

## 参考
- http://arxiv.org/abs/2507.23523v2

