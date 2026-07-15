---
$id: ent_paper_jia_learning_efficient_and_robust_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Efficient and Robust Language-conditioned Manipulation using Textual-Visual Relevancy and Equivariant Language
    Mapping
  zh: Learning Efficient and Robust Language-conditioned Manipulation using Textual-Visual Relevancy and Equivariant Language
    Mapping
  ko: Learning Efficient and Robust Language-conditioned Manipulation using Textual-Visual Relevancy and Equivariant Language
    Mapping
summary:
  en: Learning Efficient and Robust Language-conditioned Manipulation using Textual-Visual Relevancy and Equivariant Language
    Mapping (Learning Efficient and Robust Language-conditioned Manipulation using Textual-Visual Relevancy and Equivariant
    Language Mapping), is a 2024 large vision-language-action model for robotic manipulation, introduced by Brown University,
    Northeastern University, and published at IEEE Robotics Autom. Lett. 2024.
  zh: Learning Efficient and Robust Language-conditioned Manipulation using Textual-Visual Relevancy and Equivariant Language
    Mapping (Learning Efficient and Robust Language-conditioned Manipulation using Textual-Visual Relevancy and Equivariant
    Language Mapping), is a 2024 large vision-language-action model for robotic manipulation, introduced by Brown University,
    Northeastern University, and published at IEEE Robotics Autom. Lett. 2024.
  ko: Learning Efficient and Robust Language-conditioned Manipulation using Textual-Visual Relevancy and Equivariant Language
    Mapping (Learning Efficient and Robust Language-conditioned Manipulation using Textual-Visual Relevancy and Equivariant
    Language Mapping), is a 2024 large vision-language-action model for robotic manipulation, introduced by Brown University,
    Northeastern University, and published at IEEE Robotics Autom. Lett. 2024.
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
- learning_efficient_and_robust
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.15677v2.
sources:
- id: src_001
  type: website
  title: Learning Efficient and Robust Language-conditioned Manipulation using Textual-Visual Relevancy and Equivariant Language
    Mapping source
  url: https://doi.org/10.1109/LRA.2025.3583614
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Controlling robots through natural language is pivotal for enhancing human-robot collaboration and synthesizing complex robot behaviors. Recent works that are trained on large robot datasets show impressive generalization abilities. However, such pretrained methods are (1) often fragile to unseen scenarios, and (2) expensive to adapt to new tasks. This paper introduces Grounded Equivariant Manipulation (GEM), a robust yet efficient approach that leverages pretrained vision-language models with equivariant language mapping for language-conditioned manipulation tasks. Our experiments demonstrate GEM's high sample efficiency and generalization ability across diverse tasks in both simulation and the real world. GEM achieves similar or higher performance with orders of magnitude fewer robot data compared with major data-efficient baselines such as CLIPort and VIMA. Finally, our approach demonstrates greater robustness compared to large VLA model, e.g, OpenVLA, at correctly interpreting natural language commands on unseen objects and poses. Code, data, and training details are available https://saulbatman.github.io/gem_page/

## 核心内容
Controlling robots through natural language is pivotal for enhancing human-robot collaboration and synthesizing complex robot behaviors. Recent works that are trained on large robot datasets show impressive generalization abilities. However, such pretrained methods are (1) often fragile to unseen scenarios, and (2) expensive to adapt to new tasks. This paper introduces Grounded Equivariant Manipulation (GEM), a robust yet efficient approach that leverages pretrained vision-language models with equivariant language mapping for language-conditioned manipulation tasks. Our experiments demonstrate GEM's high sample efficiency and generalization ability across diverse tasks in both simulation and the real world. GEM achieves similar or higher performance with orders of magnitude fewer robot data compared with major data-efficient baselines such as CLIPort and VIMA. Finally, our approach demonstrates greater robustness compared to large VLA model, e.g, OpenVLA, at correctly interpreting natural language commands on unseen objects and poses. Code, data, and training details are available https://saulbatman.github.io/gem_page/

## 参考
- http://arxiv.org/abs/2406.15677v2

