---
$id: ent_paper_wang_sigma_the_key_for_vision_langu_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Sigma: The Key for Vision-Language-Action Models toward Telepathic Alignment'
  zh: Sigma
  ko: 'Sigma: The Key for Vision-Language-Action Models toward Telepathic Alignment'
summary:
  en: 'Sigma: The Key for Vision-Language-Action Models toward Telepathic Alignment (Sigma), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by UCSI University.'
  zh: Sigma 是 UCSI University 于 2025 年提出的大型视觉-语言-动作模型，旨在解决认知系统中语义与连续控制之间缺乏可时间更新的中介思维空间这一根本局限。该模型基于 pi0.5_base 骨干网络，通过独立设计的
    VLA 架构整合深度语义理解与联想推理，实现感知与动作的“心灵感应式”对齐。实验表明，Sigma 在控制均方误差上持续降低，同时保持了语义-文本对齐质量，无需重新训练基础模型即可实现意图驱动的行为对齐。
  ko: 'Sigma: The Key for Vision-Language-Action Models toward Telepathic Alignment (Sigma), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by UCSI University.'
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
- sigma
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.00783v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Sigma: The Key for Vision-Language-Action Models toward Telepathic Alignment (arXiv)'
  url: https://arxiv.org/abs/2512.00783
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Sigma source
  url: https://doi.org/10.48550/arXiv.2512.00783
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Sigma 模型部署于单张 RTX 4090 上，利用开源 pi0.5_base 作为骨干，并将 svla_so101_pickplace 数据集预处理为结构化训练语料。其核心创新在于引入独立设计的 VLA 架构，该架构在语义与连续控制之间建立了一个可随时间更新的中介思维空间，从而实现深度语义理解与联想推理的融合。训练过程包括数据预处理迭代优化、基于 LoRA 的微调以及推理阶段适配器设计。通过离线闭环回放评估，Sigma 与未经调优的 pi0.5_base 在相同数据条件下对比，在向量、片段和轨迹三个尺度上均实现了控制 MSE 的一致降低，同时保持了“心灵感应范数”的稳定性和语义-文本对齐质量。

## 核心内容
### 方法
- **核心问题**：现有认知系统缺乏一个可随时间更新的中介思维空间，导致语义理解与连续控制之间存在鸿沟。
- **模型架构**：Sigma 基于开源 pi0.5_base 骨干网络，并引入独立设计的 VLA 架构。该架构通过整合深度语义理解与联想推理，在语义与动作之间建立“心灵感应式”对齐。
- **训练流程**：
  - 数据预处理：将 svla_so101_pickplace 数据集转化为结构化训练语料。
  - 微调：采用 LoRA 方法进行参数高效微调。
  - 推理适配：设计推理阶段适配器以优化输出。

### 实验设置
- **硬件**：单张 RTX 4090 GPU。
- **评估方法**：离线闭环回放，对比 Sigma 与未经调优的 pi0.5_base，两者使用相同数据条件。
- **评估指标**：控制 MSE（向量、片段、轨迹三个尺度）、心灵感应范数稳定性、语义-文本对齐质量。

### 关键结果
- **控制精度**：Sigma 在向量、片段和轨迹三个尺度上均实现控制 MSE 的一致降低。
- **对齐稳定性**：心灵感应范数保持稳定，语义-文本对齐质量未下降。
- **结论**：通过语义与联想架构的整合，无需重新训练基础模型即可实现可量化的意图驱动对齐控制，为语义对齐和意图驱动行为提供了可复现的路径。

## Overview
To address a fundamental limitation in cognitive systems, namely the absence of a time-updatable mediating thought space between semantics and continuous control, this work constructs and trains a vision-language-action model termed Sigma, deployed on a single RTX 4090. The model is built upon the open-source pi0.5_base backbone, with the svla_so101_pickplace dataset preprocessed into a structured training corpus. An independently designed VLA architecture is introduced to integrate deep semantic understanding with associative reasoning, enabling telepathic-style alignment between perception and action. Training proceeds through iterative optimization of data preprocessing, LoRA-based fine-tuning, and inference-stage adapter design. Evaluation is conducted using offline closed-loop replay, comparing Sigma against the untuned pi0.5_base under identical data conditions. Experimental results indicate a consistent reduction in control MSE across vector-, fragment-, and trajectory-level scales, while preserving the stability of the telepathy norm and semantic-text alignment quality. These findings demonstrate that mind-responsive alignment control can be quantitatively achieved through semantic and associative architectural integration without retraining the base model, providing a reproducible pathway for semantic alignment and intention-driven behavior.

## 개요
인지 시스템의 근본적인 한계, 즉 의미론과 연속 제어 사이에 시간적으로 업데이트 가능한 매개 사고 공간이 없다는 문제를 해결하기 위해, 본 연구는 Sigma라는 비전-언어-행동 모델을 구축 및 훈련하여 단일 RTX 4090에 배포했습니다. 이 모델은 오픈소스 pi0.5_base 백본을 기반으로 하며, svla_so101_pickplace 데이터셋을 구조화된 훈련 코퍼스로 전처리했습니다. 독자적으로 설계된 VLA 아키텍처를 도입하여 심층 의미 이해와 연관 추론을 통합함으로써, 지각과 행동 간의 텔레파시 스타일 정렬을 가능하게 했습니다. 훈련은 데이터 전처리, LoRA 기반 미세 조정, 추론 단계 어댑터 설계의 반복적 최적화를 통해 진행됩니다. 평가는 오프라인 폐루프 재생을 사용하여 동일한 데이터 조건에서 Sigma와 튜닝되지 않은 pi0.5_base를 비교합니다. 실험 결과는 벡터, 조각, 궤적 수준에서 제어 MSE가 일관되게 감소하는 동시에 텔레파시 노름과 의미-텍스트 정렬 품질의 안정성을 유지함을 보여줍니다. 이러한 결과는 기본 모델을 재훈련하지 않고도 의미론적 및 연관 아키텍처 통합을 통해 마음 반응 정렬 제어를 정량적으로 달성할 수 있음을 입증하며, 의미 정렬 및 의도 기반 행동을 위한 재현 가능한 경로를 제공합니다.

## 핵심 내용
인지 시스템의 근본적인 한계, 즉 의미론과 연속 제어 사이에 시간적으로 업데이트 가능한 매개 사고 공간이 없다는 문제를 해결하기 위해, 본 연구는 Sigma라는 비전-언어-행동 모델을 구축 및 훈련하여 단일 RTX 4090에 배포했습니다. 이 모델은 오픈소스 pi0.5_base 백본을 기반으로 하며, svla_so101_pickplace 데이터셋을 구조화된 훈련 코퍼스로 전처리했습니다. 독자적으로 설계된 VLA 아키텍처를 도입하여 심층 의미 이해와 연관 추론을 통합함으로써, 지각과 행동 간의 텔레파시 스타일 정렬을 가능하게 했습니다. 훈련은 데이터 전처리, LoRA 기반 미세 조정, 추론 단계 어댑터 설계의 반복적 최적화를 통해 진행됩니다. 평가는 오프라인 폐루프 재생을 사용하여 동일한 데이터 조건에서 Sigma와 튜닝되지 않은 pi0.5_base를 비교합니다. 실험 결과는 벡터, 조각, 궤적 수준에서 제어 MSE가 일관되게 감소하는 동시에 텔레파시 노름과 의미-텍스트 정렬 품질의 안정성을 유지함을 보여줍니다. 이러한 결과는 기본 모델을 재훈련하지 않고도 의미론적 및 연관 아키텍처 통합을 통해 마음 반응 정렬 제어를 정량적으로 달성할 수 있음을 입증하며, 의미 정렬 및 의도 기반 행동을 위한 재현 가능한 경로를 제공합니다.

## 参考
- http://arxiv.org/abs/2512.00783v3
