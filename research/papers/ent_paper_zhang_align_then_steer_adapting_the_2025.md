---
$id: ent_paper_zhang_align_then_steer_adapting_the_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Align-Then-stEer: Adapting the Vision-Language Action Models through Unified Latent Guidance'
  zh: ATE
  ko: 'Align-Then-stEer: Adapting the Vision-Language Action Models through Unified Latent Guidance'
summary:
  en: 'Align-Then-stEer: Adapting the Vision-Language Action Models through Unified Latent Guidance (ATE), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute of Artificial Intelligence, China Telecom,
    Tsinghua University, The Chinese University of Hong Kong, Shenzhen, Northwestern Polytechnical University.'
  zh: 'Align-Then-stEer: Adapting the Vision-Language Action Models through Unified Latent Guidance (ATE), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute of Artificial Intelligence, China Telecom,
    Tsinghua University, The Chinese University of Hong Kong, Shenzhen, Northwestern Polytechnical University.'
  ko: 'Align-Then-stEer: Adapting the Vision-Language Action Models through Unified Latent Guidance (ATE), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute of Artificial Intelligence, China Telecom,
    Tsinghua University, The Chinese University of Hong Kong, Shenzhen, Northwestern Polytechnical University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- ate
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.02055v2.
sources:
- id: src_001
  type: paper
  title: 'Align-Then-stEer: Adapting the Vision-Language Action Models through Unified Latent Guidance (arXiv)'
  url: https://arxiv.org/abs/2509.02055
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ATE source
  url: https://doi.org/10.48550/arXiv.2509.02055
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models pre-trained on large, diverse datasets show remarkable potential for general-purpose robotic manipulation. However, a primary bottleneck remains in adapting these models to downstream tasks, especially when the robot's embodiment or the task itself differs from the pre-training data. This discrepancy leads to a significant mismatch in action distributions, demanding extensive data and compute for effective fine-tuning. To address this challenge, we introduce \textbf{Align-Then-stEer (\texttt{ATE})}, a novel, data-efficient, and plug-and-play adaptation framework. \texttt{ATE} first aligns disparate action spaces by constructing a unified latent space, where a variational autoencoder constrained by reverse KL divergence embeds adaptation actions into modes of the pre-training action latent distribution. Subsequently, it steers the diffusion- or flow-based VLA's generation process during fine-tuning via a guidance mechanism that pushes the model's output distribution towards the target domain. We conduct extensive experiments on cross-embodiment and cross-task manipulation in both simulation and real world. Compared to direct fine-tuning of representative VLAs, our method improves the average multi-task success rate by up to \textbf{9.8\%} in simulation and achieves a striking \textbf{32\% success rate gain} in a real-world cross-embodiment setting. Our work presents a general and lightweight solution that greatly enhances the practicality of deploying VLA models to new robotic platforms and tasks.

## 核心内容
Vision-Language-Action (VLA) models pre-trained on large, diverse datasets show remarkable potential for general-purpose robotic manipulation. However, a primary bottleneck remains in adapting these models to downstream tasks, especially when the robot's embodiment or the task itself differs from the pre-training data. This discrepancy leads to a significant mismatch in action distributions, demanding extensive data and compute for effective fine-tuning. To address this challenge, we introduce \textbf{Align-Then-stEer (\texttt{ATE})}, a novel, data-efficient, and plug-and-play adaptation framework. \texttt{ATE} first aligns disparate action spaces by constructing a unified latent space, where a variational autoencoder constrained by reverse KL divergence embeds adaptation actions into modes of the pre-training action latent distribution. Subsequently, it steers the diffusion- or flow-based VLA's generation process during fine-tuning via a guidance mechanism that pushes the model's output distribution towards the target domain. We conduct extensive experiments on cross-embodiment and cross-task manipulation in both simulation and real world. Compared to direct fine-tuning of representative VLAs, our method improves the average multi-task success rate by up to \textbf{9.8\%} in simulation and achieves a striking \textbf{32\% success rate gain} in a real-world cross-embodiment setting. Our work presents a general and lightweight solution that greatly enhances the practicality of deploying VLA models to new robotic platforms and tasks.

## 参考
- http://arxiv.org/abs/2509.02055v2

