---
$id: ent_paper_nakamoto_steering_your_generalists_impr_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance'
  zh: V-GPS
  ko: 'Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance'
summary:
  en: 'Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance (V-GPS), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by UC Berkeley, Carnegie Mellon University, and published at CoRL 2024.'
  zh: 'Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance (V-GPS), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by UC Berkeley, Carnegie Mellon University, and published at CoRL 2024.'
  ko: 'Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance (V-GPS), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by UC Berkeley, Carnegie Mellon University, and published at CoRL 2024.'
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
- robotic_manipulation
- v_gps
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.13816v2.
sources:
- id: src_001
  type: paper
  title: V-GPS source
  url: https://proceedings.mlr.press/v270/nakamoto25a.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Large, general-purpose robotic policies trained on diverse demonstration datasets have been shown to be remarkably effective both for controlling a variety of robots in a range of different scenes, and for acquiring broad repertoires of manipulation skills. However, the data that such policies are trained on is generally of mixed quality -- not only are human-collected demonstrations unlikely to perform the task perfectly, but the larger the dataset is, the harder it is to curate only the highest quality examples. It also remains unclear how optimal data from one embodiment is for training on another embodiment. In this paper, we present a general and broadly applicable approach that enhances the performance of such generalist robot policies at deployment time by re-ranking their actions according to a value function learned via offline RL. This approach, which we call Value-Guided Policy Steering (V-GPS), is compatible with a wide range of different generalist policies, without needing to fine-tune or even access the weights of the policy. We show that the same value function can improve the performance of five different state-of-the-art policies with different architectures, even though they were trained on distinct datasets, attaining consistent performance improvement on multiple robotic platforms across a total of 12 tasks. Code and videos can be found at: https://nakamotoo.github.io/V-GPS

## 核心内容
Large, general-purpose robotic policies trained on diverse demonstration datasets have been shown to be remarkably effective both for controlling a variety of robots in a range of different scenes, and for acquiring broad repertoires of manipulation skills. However, the data that such policies are trained on is generally of mixed quality -- not only are human-collected demonstrations unlikely to perform the task perfectly, but the larger the dataset is, the harder it is to curate only the highest quality examples. It also remains unclear how optimal data from one embodiment is for training on another embodiment. In this paper, we present a general and broadly applicable approach that enhances the performance of such generalist robot policies at deployment time by re-ranking their actions according to a value function learned via offline RL. This approach, which we call Value-Guided Policy Steering (V-GPS), is compatible with a wide range of different generalist policies, without needing to fine-tune or even access the weights of the policy. We show that the same value function can improve the performance of five different state-of-the-art policies with different architectures, even though they were trained on distinct datasets, attaining consistent performance improvement on multiple robotic platforms across a total of 12 tasks. Code and videos can be found at: https://nakamotoo.github.io/V-GPS

## 参考
- http://arxiv.org/abs/2410.13816v2

