---
$id: ent_paper_grover_enhancing_generalization_in_vi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations
  zh: Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations
  ko: Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations
summary:
  en: Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations (Enhancing Generalization
    in Vision-Language-Action Models by Preserving Pretrained Representations), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by UC San Diego, Hillbot.
  zh: Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations (Enhancing Generalization
    in Vision-Language-Action Models by Preserving Pretrained Representations), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by UC San Diego, Hillbot.
  ko: Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations (Enhancing Generalization
    in Vision-Language-Action Models by Preserving Pretrained Representations), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by UC San Diego, Hillbot.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- enhancing_generalization_in_vi
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.11417v2.
sources:
- id: src_001
  type: paper
  title: Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations (arXiv)
  url: https://arxiv.org/abs/2509.11417
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations source
  url: https://doi.org/10.48550/arXiv.2509.11417
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) models finetuned from vision-language models (VLMs) hold the promise of leveraging rich pretrained representations to build generalist robots across diverse tasks and environments. However, direct fine-tuning on robot data often disrupts these representations and limits generalization. We present a framework that better preserves pretrained features while adapting them for robot manipulation. Our approach introduces three components: (i) a dual-encoder design with one frozen vision encoder to retain pretrained features and another trainable for task adaptation, (ii) a string-based action tokenizer that casts continuous actions into character sequences aligned with the model's pretraining domain, and (iii) a co-training strategy that combines robot demonstrations with vision-language datasets emphasizing spatial reasoning and affordances. Evaluations in simulation and on real robots show that our method improves robustness to visual perturbations, generalization to novel instructions and environments, and overall task success compared to baselines.

## 核心内容
Vision-language-action (VLA) models finetuned from vision-language models (VLMs) hold the promise of leveraging rich pretrained representations to build generalist robots across diverse tasks and environments. However, direct fine-tuning on robot data often disrupts these representations and limits generalization. We present a framework that better preserves pretrained features while adapting them for robot manipulation. Our approach introduces three components: (i) a dual-encoder design with one frozen vision encoder to retain pretrained features and another trainable for task adaptation, (ii) a string-based action tokenizer that casts continuous actions into character sequences aligned with the model's pretraining domain, and (iii) a co-training strategy that combines robot demonstrations with vision-language datasets emphasizing spatial reasoning and affordances. Evaluations in simulation and on real robots show that our method improves robustness to visual perturbations, generalization to novel instructions and environments, and overall task success compared to baselines.

## 参考
- http://arxiv.org/abs/2509.11417v2

## Overview
Vision-language-action (VLA) models finetuned from vision-language models (VLMs) hold the promise of leveraging rich pretrained representations to build generalist robots across diverse tasks and environments. However, direct fine-tuning on robot data often disrupts these representations and limits generalization. We present a framework that better preserves pretrained features while adapting them for robot manipulation. Our approach introduces three components: (i) a dual-encoder design with one frozen vision encoder to retain pretrained features and another trainable for task adaptation, (ii) a string-based action tokenizer that casts continuous actions into character sequences aligned with the model's pretraining domain, and (iii) a co-training strategy that combines robot demonstrations with vision-language datasets emphasizing spatial reasoning and affordances. Evaluations in simulation and on real robots show that our method improves robustness to visual perturbations, generalization to novel instructions and environments, and overall task success compared to baselines.

## Content
Vision-language-action (VLA) models finetuned from vision-language models (VLMs) hold the promise of leveraging rich pretrained representations to build generalist robots across diverse tasks and environments. However, direct fine-tuning on robot data often disrupts these representations and limits generalization. We present a framework that better preserves pretrained features while adapting them for robot manipulation. Our approach introduces three components: (i) a dual-encoder design with one frozen vision encoder to retain pretrained features and another trainable for task adaptation, (ii) a string-based action tokenizer that casts continuous actions into character sequences aligned with the model's pretraining domain, and (iii) a co-training strategy that combines robot demonstrations with vision-language datasets emphasizing spatial reasoning and affordances. Evaluations in simulation and on real robots show that our method improves robustness to visual perturbations, generalization to novel instructions and environments, and overall task success compared to baselines.

## 개요
Vision-language-action (VLA) 모델은 vision-language models (VLMs)에서 미세 조정되어, 다양한 작업과 환경에서 일반화된 로봇을 구축하기 위해 풍부한 사전 학습 표현을 활용할 가능성을 지니고 있습니다. 그러나 로봇 데이터에 대한 직접적인 미세 조정은 종종 이러한 표현을 방해하고 일반화를 제한합니다. 우리는 사전 학습된 특징을 더 잘 보존하면서 로봇 조작에 적응시키는 프레임워크를 제시합니다. 본 접근법은 세 가지 구성 요소를 도입합니다: (i) 사전 학습된 특징을 유지하기 위한 고정된 비전 인코더와 작업 적응을 위한 학습 가능한 인코더로 구성된 이중 인코더 설계, (ii) 연속적인 행동을 모델의 사전 학습 도메인에 맞춰진 문자 시퀀스로 변환하는 문자열 기반 행동 토크나이저, (iii) 공간 추론과 어포던스에 중점을 둔 비전-언어 데이터셋과 로봇 시연을 결합한 공동 학습 전략. 시뮬레이션 및 실제 로봇에서의 평가는 우리의 방법이 시각적 교란에 대한 강건성, 새로운 명령 및 환경에 대한 일반화, 그리고 기준선 대비 전반적인 작업 성공률을 향상시킴을 보여줍니다.

## 핵심 내용
Vision-language-action (VLA) 모델은 vision-language models (VLMs)에서 미세 조정되어, 다양한 작업과 환경에서 일반화된 로봇을 구축하기 위해 풍부한 사전 학습 표현을 활용할 가능성을 지니고 있습니다. 그러나 로봇 데이터에 대한 직접적인 미세 조정은 종종 이러한 표현을 방해하고 일반화를 제한합니다. 우리는 사전 학습된 특징을 더 잘 보존하면서 로봇 조작에 적응시키는 프레임워크를 제시합니다. 본 접근법은 세 가지 구성 요소를 도입합니다: (i) 사전 학습된 특징을 유지하기 위한 고정된 비전 인코더와 작업 적응을 위한 학습 가능한 인코더로 구성된 이중 인코더 설계, (ii) 연속적인 행동을 모델의 사전 학습 도메인에 맞춰진 문자 시퀀스로 변환하는 문자열 기반 행동 토크나이저, (iii) 공간 추론과 어포던스에 중점을 둔 비전-언어 데이터셋과 로봇 시연을 결합한 공동 학습 전략. 시뮬레이션 및 실제 로봇에서의 평가는 우리의 방법이 시각적 교란에 대한 강건성, 새로운 명령 및 환경에 대한 일반화, 그리고 기준선 대비 전반적인 작업 성공률을 향상시킴을 보여줍니다.
