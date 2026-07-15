---
$id: ent_paper_liu_robomamba_efficient_vision_lan_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation'
  zh: RoboMamba
  ko: 'RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation'
summary:
  en: 'RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation (RoboMamba), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia Information Processing,
    School of Computer Science, Peking University, AI2Robotics, Beijing Academy of Artificial Intelligence (BAAI), and published
    at NIPS 2024.'
  zh: 'RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation (RoboMamba), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia Information Processing,
    School of Computer Science, Peking University, AI2Robotics, Beijing Academy of Artificial Intelligence (BAAI), and published
    at NIPS 2024.'
  ko: 'RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation (RoboMamba), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia Information Processing,
    School of Computer Science, Peking University, AI2Robotics, Beijing Academy of Artificial Intelligence (BAAI), and published
    at NIPS 2024.'
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
- robomamba
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.04339v2.
sources:
- id: src_001
  type: website
  title: RoboMamba source
  url: http://papers.nips.cc/paper_files/paper/2024/hash/46a126492ea6fb87410e55a58df2e189-Abstract-Conference.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
A fundamental objective in robot manipulation is to enable models to comprehend visual scenes and execute actions. Although existing Vision-Language-Action (VLA) models for robots can handle a range of basic tasks, they still face challenges in two areas: (1) insufficient reasoning ability to tackle complex tasks, and (2) high computational costs for VLA model fine-tuning and inference. The recently proposed state space model (SSM) known as Mamba demonstrates promising capabilities in non-trivial sequence modeling with linear inference complexity. Inspired by this, we introduce RoboMamba, an end-to-end robotic VLA model that leverages Mamba to deliver both robotic reasoning and action capabilities, while maintaining efficient fine-tuning and inference. Specifically, we first integrate the vision encoder with Mamba, aligning visual tokens with language embedding through co-training, empowering our model with visual common sense and robotic-related reasoning. To further equip RoboMamba with SE(3) pose prediction abilities, we explore an efficient fine-tuning strategy with a simple policy head. We find that once RoboMamba possesses sufficient reasoning capability, it can acquire manipulation skills with minimal fine-tuning parameters (0.1\% of the model) and time. In experiments, RoboMamba demonstrates outstanding reasoning capabilities on general and robotic evaluation benchmarks. Meanwhile, our model showcases impressive pose prediction results in both simulation and real-world experiments, achieving inference speeds 3 times faster than existing VLA models. Our project web page: https://sites.google.com/view/robomamba-web

## 核心内容
A fundamental objective in robot manipulation is to enable models to comprehend visual scenes and execute actions. Although existing Vision-Language-Action (VLA) models for robots can handle a range of basic tasks, they still face challenges in two areas: (1) insufficient reasoning ability to tackle complex tasks, and (2) high computational costs for VLA model fine-tuning and inference. The recently proposed state space model (SSM) known as Mamba demonstrates promising capabilities in non-trivial sequence modeling with linear inference complexity. Inspired by this, we introduce RoboMamba, an end-to-end robotic VLA model that leverages Mamba to deliver both robotic reasoning and action capabilities, while maintaining efficient fine-tuning and inference. Specifically, we first integrate the vision encoder with Mamba, aligning visual tokens with language embedding through co-training, empowering our model with visual common sense and robotic-related reasoning. To further equip RoboMamba with SE(3) pose prediction abilities, we explore an efficient fine-tuning strategy with a simple policy head. We find that once RoboMamba possesses sufficient reasoning capability, it can acquire manipulation skills with minimal fine-tuning parameters (0.1\% of the model) and time. In experiments, RoboMamba demonstrates outstanding reasoning capabilities on general and robotic evaluation benchmarks. Meanwhile, our model showcases impressive pose prediction results in both simulation and real-world experiments, achieving inference speeds 3 times faster than existing VLA models. Our project web page: https://sites.google.com/view/robomamba-web

## 参考
- http://arxiv.org/abs/2406.04339v2

