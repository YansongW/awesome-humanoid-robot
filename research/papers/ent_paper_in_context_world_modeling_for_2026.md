---
$id: ent_paper_in_context_world_modeling_for_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: In-Context World Modeling for Robotic Control
  zh: In-Context World Modeling for Robotic Control
  ko: In-Context World Modeling for Robotic Control
summary:
  en: 'arXiv:2606.26025v3 Announce Type: replace Abstract: Modern Vision-Language-Action (VLA) models often fail to generalize
    to novel setups, such as altered camera viewpoints or robot morphologies, because they are typically conditioned only
    on current observations and language instructions. By ignoring the underlying system configuration as a variable, these
    models implicitly assume a fixed execution context encountered during training, necessitating data-intensive fine-tuning
    for any new environment. In this work, we introduce In-Context World Modeling (ICWM), a framework that treats system identification
    as an in-context adaptation problem. ICWM enables robot policies to autonomously infer essential system variables from
    a short history of self-generated, task-agnostic interactions. Unlike traditional In-Context Learning that uses demonstrations
    to specify what task to perform, ICWM leverages the context window to understand how the system operates. By processing
    these interactions before task execution, the model implicitly captures the world dynamics of the current system, enabling
    adaptation to novel configurations without parameter updates. Extensive experiments in simulation and on real-world robot
    platforms demonstrate that ICWM significantly outperforms standard VLA baselines on novel camera viewpoints.'
  zh: 'arXiv:2606.26025v3 Announce Type: replace Abstract: Modern Vision-Language-Action (VLA) models often fail to generalize
    to novel setups, such as altered camera viewpoints or robot morphologies, because they are typically conditioned only
    on current observations and language instructions. By ignoring the underlying system configuration as a variable, these
    models implicitly assume a fixed execution context encountered during training, necessitating data-intensive fine-tuning
    for any new environment. In this work, we introduce In-Context World Modeling (ICWM), a framework that treats system identification
    as an in-context adaptation problem. ICWM enables robot policies to autonomously infer essential system variables from
    a short history of self-generated, task-agnostic interactions. Unlike traditional In-Context Learning that uses demonstrations
    to specify what task to perform, ICWM leverages the context window to understand how the system operates. By processing
    these interactions before task execution, the model implicitly captures the world dynamics of the current system, enabling
    adaptation to novel configurations without parameter updates. Extensive experiments in simulation and on real-world robot
    platforms demonstrate that ICWM significantly outperforms standard VLA baselines on novel camera viewpoints.'
  ko: 'arXiv:2606.26025v3 Announce Type: replace Abstract: Modern Vision-Language-Action (VLA) models often fail to generalize
    to novel setups, such as altered camera viewpoints or robot morphologies, because they are typically conditioned only
    on current observations and language instructions. By ignoring the underlying system configuration as a variable, these
    models implicitly assume a fixed execution context encountered during training, necessitating data-intensive fine-tuning
    for any new environment. In this work, we introduce In-Context World Modeling (ICWM), a framework that treats system identification
    as an in-context adaptation problem. ICWM enables robot policies to autonomously infer essential system variables from
    a short history of self-generated, task-agnostic interactions. Unlike traditional In-Context Learning that uses demonstrations
    to specify what task to perform, ICWM leverages the context window to understand how the system operates. By processing
    these interactions before task execution, the model implicitly captures the world dynamics of the current system, enabling
    adaptation to novel configurations without parameter updates. Extensive experiments in simulation and on real-world robot
    platforms demonstrate that ICWM significantly outperforms standard VLA baselines on novel camera viewpoints.'
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
- robotics
- in_context_world_modeling_for
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.26025v3.
sources:
- id: src_001
  type: paper
  title: In-Context World Modeling for Robotic Control (arXiv)
  url: https://arxiv.org/abs/2606.26025
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Modern Vision-Language-Action (VLA) models often fail to generalize to novel setups, such as altered camera viewpoints or robot morphologies, because they are typically conditioned only on current observations and language instructions. By ignoring the underlying system configuration as a variable, these models implicitly assume a fixed execution context encountered during training, necessitating data-intensive fine-tuning for any new environment. In this work, we introduce In-Context World Modeling (ICWM), a framework that treats system identification as an in-context adaptation problem. ICWM enables robot policies to autonomously infer essential system variables from a short history of self-generated, task-agnostic interactions. Unlike traditional In-Context Learning that uses demonstrations to specify what task to perform, ICWM leverages the context window to understand how the system operates. By processing these interactions before task execution, the model implicitly captures the world dynamics of the current system, enabling adaptation to novel configurations without parameter updates. Extensive experiments in simulation and on real-world robot platforms demonstrate that ICWM significantly outperforms standard VLA baselines on novel camera viewpoints.

## 核心内容
Modern Vision-Language-Action (VLA) models often fail to generalize to novel setups, such as altered camera viewpoints or robot morphologies, because they are typically conditioned only on current observations and language instructions. By ignoring the underlying system configuration as a variable, these models implicitly assume a fixed execution context encountered during training, necessitating data-intensive fine-tuning for any new environment. In this work, we introduce In-Context World Modeling (ICWM), a framework that treats system identification as an in-context adaptation problem. ICWM enables robot policies to autonomously infer essential system variables from a short history of self-generated, task-agnostic interactions. Unlike traditional In-Context Learning that uses demonstrations to specify what task to perform, ICWM leverages the context window to understand how the system operates. By processing these interactions before task execution, the model implicitly captures the world dynamics of the current system, enabling adaptation to novel configurations without parameter updates. Extensive experiments in simulation and on real-world robot platforms demonstrate that ICWM significantly outperforms standard VLA baselines on novel camera viewpoints.

## 参考
- http://arxiv.org/abs/2606.26025v3

