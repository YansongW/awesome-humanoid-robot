---
$id: ent_paper_li_vision_language_foundation_mod_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Vision-Language Foundation Models as Effective Robot Imitators
  zh: RoboFlamingo
  ko: Vision-Language Foundation Models as Effective Robot Imitators
summary:
  en: Vision-Language Foundation Models as Effective Robot Imitators (RoboFlamingo), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by ByteDance Research, Tsinghua University, Shanghai Jiao Tong University,
    National University of Singapore, and published at ICLR 2024.
  zh: Vision-Language Foundation Models as Effective Robot Imitators (RoboFlamingo), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by ByteDance Research, Tsinghua University, Shanghai Jiao Tong University,
    National University of Singapore, and published at ICLR 2024.
  ko: Vision-Language Foundation Models as Effective Robot Imitators (RoboFlamingo), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by ByteDance Research, Tsinghua University, Shanghai Jiao Tong University,
    National University of Singapore, and published at ICLR 2024.
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
- roboflamingo
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2311.01378v3.
sources:
- id: src_001
  type: paper
  title: RoboFlamingo source
  url: https://openreview.net/forum?id=lFYj0oibGR
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
Recent progress in vision language foundation models has shown their ability to understand multimodal data and resolve complicated vision language tasks, including robotics manipulation. We seek a straightforward way of making use of existing vision-language models (VLMs) with simple fine-tuning on robotics data. To this end, we derive a simple and novel vision-language manipulation framework, dubbed RoboFlamingo, built upon the open-source VLMs, OpenFlamingo. Unlike prior works, RoboFlamingo utilizes pre-trained VLMs for single-step vision-language comprehension, models sequential history information with an explicit policy head, and is slightly fine-tuned by imitation learning only on language-conditioned manipulation datasets. Such a decomposition provides RoboFlamingo the flexibility for open-loop control and deployment on low-performance platforms. By exceeding the state-of-the-art performance with a large margin on the tested benchmark, we show RoboFlamingo can be an effective and competitive alternative to adapt VLMs to robot control. Our extensive experimental results also reveal several interesting conclusions regarding the behavior of different pre-trained VLMs on manipulation tasks. We believe RoboFlamingo has the potential to be a cost-effective and easy-to-use solution for robotics manipulation, empowering everyone with the ability to fine-tune their own robotics policy.

## 核心内容
Recent progress in vision language foundation models has shown their ability to understand multimodal data and resolve complicated vision language tasks, including robotics manipulation. We seek a straightforward way of making use of existing vision-language models (VLMs) with simple fine-tuning on robotics data. To this end, we derive a simple and novel vision-language manipulation framework, dubbed RoboFlamingo, built upon the open-source VLMs, OpenFlamingo. Unlike prior works, RoboFlamingo utilizes pre-trained VLMs for single-step vision-language comprehension, models sequential history information with an explicit policy head, and is slightly fine-tuned by imitation learning only on language-conditioned manipulation datasets. Such a decomposition provides RoboFlamingo the flexibility for open-loop control and deployment on low-performance platforms. By exceeding the state-of-the-art performance with a large margin on the tested benchmark, we show RoboFlamingo can be an effective and competitive alternative to adapt VLMs to robot control. Our extensive experimental results also reveal several interesting conclusions regarding the behavior of different pre-trained VLMs on manipulation tasks. We believe RoboFlamingo has the potential to be a cost-effective and easy-to-use solution for robotics manipulation, empowering everyone with the ability to fine-tune their own robotics policy.

## 参考
- http://arxiv.org/abs/2311.01378v3

