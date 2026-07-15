---
$id: ent_paper_guo_improving_vision_language_acti_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Improving Vision-Language-Action Model with Online Reinforcement Learning
  zh: iRe-VLA
  ko: Improving Vision-Language-Action Model with Online Reinforcement Learning
summary:
  en: Improving Vision-Language-Action Model with Online Reinforcement Learning (iRe-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, University of California, Berkeley, Shanghai Qi Zhi
    Institute, and published at ICRA 2025.
  zh: Improving Vision-Language-Action Model with Online Reinforcement Learning (iRe-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, University of California, Berkeley, Shanghai Qi Zhi
    Institute, and published at ICRA 2025.
  ko: Improving Vision-Language-Action Model with Online Reinforcement Learning (iRe-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, University of California, Berkeley, Shanghai Qi Zhi
    Institute, and published at ICRA 2025.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- ire_vla
- large_vla_model
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2501.16664v1.
sources:
- id: src_001
  type: website
  title: iRe-VLA source
  url: https://doi.org/10.1109/ICRA55743.2025.11127299
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent studies have successfully integrated large vision-language models (VLMs) into low-level robotic control by supervised fine-tuning (SFT) with expert robotic datasets, resulting in what we term vision-language-action (VLA) models. Although the VLA models are powerful, how to improve these large models during interaction with environments remains an open question. In this paper, we explore how to further improve these VLA models via Reinforcement Learning (RL), a commonly used fine-tuning technique for large models. However, we find that directly applying online RL to large VLA models presents significant challenges, including training instability that severely impacts the performance of large models, and computing burdens that exceed the capabilities of most local machines. To address these challenges, we propose iRe-VLA framework, which iterates between Reinforcement Learning and Supervised Learning to effectively improve VLA models, leveraging the exploratory benefits of RL while maintaining the stability of supervised learning. Experiments in two simulated benchmarks and a real-world manipulation suite validate the effectiveness of our method.

## 核心内容
Recent studies have successfully integrated large vision-language models (VLMs) into low-level robotic control by supervised fine-tuning (SFT) with expert robotic datasets, resulting in what we term vision-language-action (VLA) models. Although the VLA models are powerful, how to improve these large models during interaction with environments remains an open question. In this paper, we explore how to further improve these VLA models via Reinforcement Learning (RL), a commonly used fine-tuning technique for large models. However, we find that directly applying online RL to large VLA models presents significant challenges, including training instability that severely impacts the performance of large models, and computing burdens that exceed the capabilities of most local machines. To address these challenges, we propose iRe-VLA framework, which iterates between Reinforcement Learning and Supervised Learning to effectively improve VLA models, leveraging the exploratory benefits of RL while maintaining the stability of supervised learning. Experiments in two simulated benchmarks and a real-world manipulation suite validate the effectiveness of our method.

## 参考
- http://arxiv.org/abs/2501.16664v1

