---
$id: ent_paper_yadav_robust_finetuning_of_vision_la_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Robust Finetuning of Vision-Language-Action Robot Policies via Parameter Merging
  zh: RETAIN
  ko: Robust Finetuning of Vision-Language-Action Robot Policies via Parameter Merging
summary:
  en: Robust Finetuning of Vision-Language-Action Robot Policies via Parameter Merging (RETAIN), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by UC Berkeley.
  zh: Robust Finetuning of Vision-Language-Action Robot Policies via Parameter Merging (RETAIN), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by UC Berkeley.
  ko: Robust Finetuning of Vision-Language-Action Robot Policies via Parameter Merging (RETAIN), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by UC Berkeley.
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
- retain
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.08333v3.
sources:
- id: src_001
  type: paper
  title: Robust Finetuning of Vision-Language-Action Robot Policies via Parameter Merging (arXiv)
  url: https://arxiv.org/abs/2512.08333
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RETAIN source
  url: https://doi.org/10.48550/arXiv.2512.08333
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Generalist robot policies, trained on large and diverse datasets, have demonstrated the ability to generalize across a wide spectrum of behaviors, enabling a single policy to act in varied real-world environments. However, they still fall short on new tasks not covered in the training data. When finetuned on limited demonstrations of a new task, these policies often overfit to the specific demonstrations--not only losing their prior abilities to solve a wide variety of generalist tasks but also failing to generalize within the new task itself. In this work, we aim to develop a method that preserves the generalization capabilities of the generalist policy during finetuning, allowing a single policy to robustly incorporate a new skill into its repertoire. Our goal is a single policy that both learns to generalize to variations of the new task and retains the broad competencies gained from pretraining. We show that this can be achieved through a simple yet effective strategy: interpolating the weights of a finetuned model with that of the pretrained model. We show, across extensive simulated and real-world experiments, that such model merging produces a single model that inherits the generalist abilities of the base model and learns to solve the new task robustly, outperforming both the pretrained and finetuned model on out-of-distribution variations of the new task. Moreover, we show that model merging performance scales with the amount of pretraining data, and enables continual acquisition of new skills in a lifelong learning setting, without sacrificing previously learned generalist abilities.

## 核心内容
Generalist robot policies, trained on large and diverse datasets, have demonstrated the ability to generalize across a wide spectrum of behaviors, enabling a single policy to act in varied real-world environments. However, they still fall short on new tasks not covered in the training data. When finetuned on limited demonstrations of a new task, these policies often overfit to the specific demonstrations--not only losing their prior abilities to solve a wide variety of generalist tasks but also failing to generalize within the new task itself. In this work, we aim to develop a method that preserves the generalization capabilities of the generalist policy during finetuning, allowing a single policy to robustly incorporate a new skill into its repertoire. Our goal is a single policy that both learns to generalize to variations of the new task and retains the broad competencies gained from pretraining. We show that this can be achieved through a simple yet effective strategy: interpolating the weights of a finetuned model with that of the pretrained model. We show, across extensive simulated and real-world experiments, that such model merging produces a single model that inherits the generalist abilities of the base model and learns to solve the new task robustly, outperforming both the pretrained and finetuned model on out-of-distribution variations of the new task. Moreover, we show that model merging performance scales with the amount of pretraining data, and enables continual acquisition of new skills in a lifelong learning setting, without sacrificing previously learned generalist abilities.

## 参考
- http://arxiv.org/abs/2512.08333v3

## Overview
Generalist robot policies, trained on large and diverse datasets, have demonstrated the ability to generalize across a wide spectrum of behaviors, enabling a single policy to act in varied real-world environments. However, they still fall short on new tasks not covered in the training data. When finetuned on limited demonstrations of a new task, these policies often overfit to the specific demonstrations--not only losing their prior abilities to solve a wide variety of generalist tasks but also failing to generalize within the new task itself. In this work, we aim to develop a method that preserves the generalization capabilities of the generalist policy during finetuning, allowing a single policy to robustly incorporate a new skill into its repertoire. Our goal is a single policy that both learns to generalize to variations of the new task and retains the broad competencies gained from pretraining. We show that this can be achieved through a simple yet effective strategy: interpolating the weights of a finetuned model with that of the pretrained model. We show, across extensive simulated and real-world experiments, that such model merging produces a single model that inherits the generalist abilities of the base model and learns to solve the new task robustly, outperforming both the pretrained and finetuned model on out-of-distribution variations of the new task. Moreover, we show that model merging performance scales with the amount of pretraining data, and enables continual acquisition of new skills in a lifelong learning setting, without sacrificing previously learned generalist abilities.

## Content
Generalist robot policies, trained on large and diverse datasets, have demonstrated the ability to generalize across a wide spectrum of behaviors, enabling a single policy to act in varied real-world environments. However, they still fall short on new tasks not covered in the training data. When finetuned on limited demonstrations of a new task, these policies often overfit to the specific demonstrations--not only losing their prior abilities to solve a wide variety of generalist tasks but also failing to generalize within the new task itself. In this work, we aim to develop a method that preserves the generalization capabilities of the generalist policy during finetuning, allowing a single policy to robustly incorporate a new skill into its repertoire. Our goal is a single policy that both learns to generalize to variations of the new task and retains the broad competencies gained from pretraining. We show that this can be achieved through a simple yet effective strategy: interpolating the weights of a finetuned model with that of the pretrained model. We show, across extensive simulated and real-world experiments, that such model merging produces a single model that inherits the generalist abilities of the base model and learns to solve the new task robustly, outperforming both the pretrained and finetuned model on out-of-distribution variations of the new task. Moreover, we show that model merging performance scales with the amount of pretraining data, and enables continual acquisition of new skills in a lifelong learning setting, without sacrificing previously learned generalist abilities.

## 개요
범용 로봇 정책(Generalist robot policies)은 대규모의 다양한 데이터셋으로 학습되어 광범위한 행동 스펙트럼에 걸쳐 일반화 능력을 입증했으며, 단일 정책이 다양한 실제 환경에서 작동할 수 있도록 합니다. 그러나 학습 데이터에 포함되지 않은 새로운 작업에서는 여전히 부족함을 보입니다. 새로운 작업의 제한된 시연 데이터로 미세 조정(finetuning)할 경우, 이러한 정책들은 특정 시연에 과적합(overfit)되어 이전의 다양한 범용 작업을 해결하는 능력을 상실할 뿐만 아니라 새로운 작업 내에서도 일반화에 실패합니다. 본 연구에서는 미세 조정 과정에서 범용 정책의 일반화 능력을 보존하여, 단일 정책이 새로운 기술을 견고하게 자신의 레퍼토리에 통합할 수 있는 방법을 개발하는 것을 목표로 합니다. 우리의 목표는 새로운 작업의 변형에 일반화하는 방법을 학습하면서 사전 학습에서 얻은 광범위한 역량을 유지하는 단일 정책을 만드는 것입니다. 우리는 이를 간단하면서도 효과적인 전략, 즉 미세 조정된 모델의 가중치와 사전 학습된 모델의 가중치를 보간(interpolating)함으로써 달성할 수 있음을 보여줍니다. 광범위한 시뮬레이션 및 실제 실험을 통해, 이러한 모델 병합(model merging)이 기본 모델의 범용 능력을 계승하고 새로운 작업을 견고하게 해결하는 단일 모델을 생성하며, 새로운 작업의 분포 외 변형(out-of-distribution variations)에서 사전 학습 모델과 미세 조정 모델 모두를 능가함을 입증합니다. 또한, 모델 병합 성능이 사전 학습 데이터 양에 따라 확장되며, 이전에 학습된 범용 능력을 희생하지 않고 평생 학습(lifelong learning) 환경에서 새로운 기술을 지속적으로 습득할 수 있게 함을 보여줍니다.

## 핵심 내용
범용 로봇 정책(Generalist robot policies)은 대규모의 다양한 데이터셋으로 학습되어 광범위한 행동 스펙트럼에 걸쳐 일반화 능력을 입증했으며, 단일 정책이 다양한 실제 환경에서 작동할 수 있도록 합니다. 그러나 학습 데이터에 포함되지 않은 새로운 작업에서는 여전히 부족함을 보입니다. 새로운 작업의 제한된 시연 데이터로 미세 조정(finetuning)할 경우, 이러한 정책들은 특정 시연에 과적합(overfit)되어 이전의 다양한 범용 작업을 해결하는 능력을 상실할 뿐만 아니라 새로운 작업 내에서도 일반화에 실패합니다. 본 연구에서는 미세 조정 과정에서 범용 정책의 일반화 능력을 보존하여, 단일 정책이 새로운 기술을 견고하게 자신의 레퍼토리에 통합할 수 있는 방법을 개발하는 것을 목표로 합니다. 우리의 목표는 새로운 작업의 변형에 일반화하는 방법을 학습하면서 사전 학습에서 얻은 광범위한 역량을 유지하는 단일 정책을 만드는 것입니다. 우리는 이를 간단하면서도 효과적인 전략, 즉 미세 조정된 모델의 가중치와 사전 학습된 모델의 가중치를 보간(interpolating)함으로써 달성할 수 있음을 보여줍니다. 광범위한 시뮬레이션 및 실제 실험을 통해, 이러한 모델 병합(model merging)이 기본 모델의 범용 능력을 계승하고 새로운 작업을 견고하게 해결하는 단일 모델을 생성하며, 새로운 작업의 분포 외 변형(out-of-distribution variations)에서 사전 학습 모델과 미세 조정 모델 모두를 능가함을 입증합니다. 또한, 모델 병합 성능이 사전 학습 데이터 양에 따라 확장되며, 이전에 학습된 범용 능력을 희생하지 않고 평생 학습(lifelong learning) 환경에서 새로운 기술을 지속적으로 습득할 수 있게 함을 보여줍니다.
