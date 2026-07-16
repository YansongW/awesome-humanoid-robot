---
$id: ent_paper_li_embodiment_transfer_learning_f_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Embodiment Transfer Learning for Vision-Language-Action Models
  zh: ET-VLA
  ko: Embodiment Transfer Learning for Vision-Language-Action Models
summary:
  en: Embodiment Transfer Learning for Vision-Language-Action Models (ET-VLA), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Shanghai University.
  zh: Embodiment Transfer Learning for Vision-Language-Action Models (ET-VLA), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Shanghai University.
  ko: Embodiment Transfer Learning for Vision-Language-Action Models (ET-VLA), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Shanghai University.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- et_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.01224v1.
sources:
- id: src_001
  type: paper
  title: Embodiment Transfer Learning for Vision-Language-Action Models (arXiv)
  url: https://arxiv.org/abs/2511.01224
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ET-VLA source
  url: https://doi.org/10.48550/arXiv.2511.01224
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) models have significantly advanced robotic learning, enabling training on large-scale, cross-embodiment data and fine-tuning for specific robots. However, state-of-the-art autoregressive VLAs struggle with multi-robot collaboration. We introduce embodiment transfer learning, denoted as ET-VLA, a novel framework for efficient and effective transfer of pre-trained VLAs to multi-robot. ET-VLA's core is Synthetic Continued Pretraining (SCP), which uses synthetically generated data to warm up the model for the new embodiment, bypassing the need for real human demonstrations and reducing data collection costs. SCP enables the model to learn correct actions and precise action token numbers. Following SCP, the model is fine-tuned on target embodiment data. To further enhance the model performance on multi-embodiment, we present the Embodied Graph-of-Thought technique, a novel approach that formulates each sub-task as a node, that allows the VLA model to distinguish the functionalities and roles of each embodiment during task execution. Our work considers bimanual robots, a simple version of multi-robot to verify our approaches. We validate the effectiveness of our method on both simulation benchmarks and real robots covering three different bimanual embodiments. In particular, our proposed ET-VLA \space can outperform OpenVLA on six real-world tasks over 53.2%. We will open-source all codes to support the community in advancing VLA models for robot learning.

## 核心内容
Vision-language-action (VLA) models have significantly advanced robotic learning, enabling training on large-scale, cross-embodiment data and fine-tuning for specific robots. However, state-of-the-art autoregressive VLAs struggle with multi-robot collaboration. We introduce embodiment transfer learning, denoted as ET-VLA, a novel framework for efficient and effective transfer of pre-trained VLAs to multi-robot. ET-VLA's core is Synthetic Continued Pretraining (SCP), which uses synthetically generated data to warm up the model for the new embodiment, bypassing the need for real human demonstrations and reducing data collection costs. SCP enables the model to learn correct actions and precise action token numbers. Following SCP, the model is fine-tuned on target embodiment data. To further enhance the model performance on multi-embodiment, we present the Embodied Graph-of-Thought technique, a novel approach that formulates each sub-task as a node, that allows the VLA model to distinguish the functionalities and roles of each embodiment during task execution. Our work considers bimanual robots, a simple version of multi-robot to verify our approaches. We validate the effectiveness of our method on both simulation benchmarks and real robots covering three different bimanual embodiments. In particular, our proposed ET-VLA \space can outperform OpenVLA on six real-world tasks over 53.2%. We will open-source all codes to support the community in advancing VLA models for robot learning.

## 参考
- http://arxiv.org/abs/2511.01224v1

## Overview
Vision-language-action (VLA) models have significantly advanced robotic learning, enabling training on large-scale, cross-embodiment data and fine-tuning for specific robots. However, state-of-the-art autoregressive VLAs struggle with multi-robot collaboration. We introduce embodiment transfer learning, denoted as ET-VLA, a novel framework for efficient and effective transfer of pre-trained VLAs to multi-robot. ET-VLA's core is Synthetic Continued Pretraining (SCP), which uses synthetically generated data to warm up the model for the new embodiment, bypassing the need for real human demonstrations and reducing data collection costs. SCP enables the model to learn correct actions and precise action token numbers. Following SCP, the model is fine-tuned on target embodiment data. To further enhance the model performance on multi-embodiment, we present the Embodied Graph-of-Thought technique, a novel approach that formulates each sub-task as a node, that allows the VLA model to distinguish the functionalities and roles of each embodiment during task execution. Our work considers bimanual robots, a simple version of multi-robot to verify our approaches. We validate the effectiveness of our method on both simulation benchmarks and real robots covering three different bimanual embodiments. In particular, our proposed ET-VLA \space can outperform OpenVLA on six real-world tasks over 53.2%. We will open-source all codes to support the community in advancing VLA models for robot learning.

## Content
Vision-language-action (VLA) models have significantly advanced robotic learning, enabling training on large-scale, cross-embodiment data and fine-tuning for specific robots. However, state-of-the-art autoregressive VLAs struggle with multi-robot collaboration. We introduce embodiment transfer learning, denoted as ET-VLA, a novel framework for efficient and effective transfer of pre-trained VLAs to multi-robot. ET-VLA's core is Synthetic Continued Pretraining (SCP), which uses synthetically generated data to warm up the model for the new embodiment, bypassing the need for real human demonstrations and reducing data collection costs. SCP enables the model to learn correct actions and precise action token numbers. Following SCP, the model is fine-tuned on target embodiment data. To further enhance the model performance on multi-embodiment, we present the Embodied Graph-of-Thought technique, a novel approach that formulates each sub-task as a node, that allows the VLA model to distinguish the functionalities and roles of each embodiment during task execution. Our work considers bimanual robots, a simple version of multi-robot to verify our approaches. We validate the effectiveness of our method on both simulation benchmarks and real robots covering three different bimanual embodiments. In particular, our proposed ET-VLA \space can outperform OpenVLA on six real-world tasks over 53.2%. We will open-source all codes to support the community in advancing VLA models for robot learning.

## 개요
Vision-language-action (VLA) 모델은 로봇 학습을 크게 발전시켜 대규모 교차 체현 데이터를 학습하고 특정 로봇에 미세 조정할 수 있게 했습니다. 그러나 최첨단 자기회귀 VLA는 다중 로봇 협업에 어려움을 겪습니다. 우리는 사전 학습된 VLA를 다중 로봇에 효율적이고 효과적으로 전이하는 새로운 프레임워크인 체현 전이 학습(ET-VLA)을 소개합니다. ET-VLA의 핵심은 합성 지속 사전 학습(SCP)으로, 합성 생성 데이터를 사용하여 새로운 체현에 모델을 예열함으로써 실제 인간 시연의 필요성을 없애고 데이터 수집 비용을 줄입니다. SCP는 모델이 올바른 동작과 정확한 동작 토큰 수를 학습할 수 있게 합니다. SCP 이후 모델은 대상 체현 데이터로 미세 조정됩니다. 다중 체현에서 모델 성능을 더욱 향상시키기 위해, 우리는 각 하위 작업을 노드로 구성하여 VLA 모델이 작업 실행 중 각 체현의 기능과 역할을 구분할 수 있게 하는 새로운 접근 방식인 체현 사고 그래프(Embodied Graph-of-Thought) 기술을 제시합니다. 우리의 연구는 다중 로봇의 간단한 버전인 양팔 로봇을 고려하여 접근 방식을 검증합니다. 우리는 세 가지 다른 양팔 체현을 포함한 시뮬레이션 벤치마크와 실제 로봇 모두에서 방법의 효과를 검증합니다. 특히, 제안된 ET-VLA는 6가지 실제 작업에서 OpenVLA보다 53.2% 이상 뛰어난 성능을 보입니다. 우리는 모든 코드를 오픈소스로 공개하여 로봇 학습을 위한 VLA 모델 발전을 지원할 것입니다.

## 핵심 내용
Vision-language-action (VLA) 모델은 로봇 학습을 크게 발전시켜 대규모 교차 체현 데이터를 학습하고 특정 로봇에 미세 조정할 수 있게 했습니다. 그러나 최첨단 자기회귀 VLA는 다중 로봇 협업에 어려움을 겪습니다. 우리는 사전 학습된 VLA를 다중 로봇에 효율적이고 효과적으로 전이하는 새로운 프레임워크인 체현 전이 학습(ET-VLA)을 소개합니다. ET-VLA의 핵심은 합성 지속 사전 학습(SCP)으로, 합성 생성 데이터를 사용하여 새로운 체현에 모델을 예열함으로써 실제 인간 시연의 필요성을 없애고 데이터 수집 비용을 줄입니다. SCP는 모델이 올바른 동작과 정확한 동작 토큰 수를 학습할 수 있게 합니다. SCP 이후 모델은 대상 체현 데이터로 미세 조정됩니다. 다중 체현에서 모델 성능을 더욱 향상시키기 위해, 우리는 각 하위 작업을 노드로 구성하여 VLA 모델이 작업 실행 중 각 체현의 기능과 역할을 구분할 수 있게 하는 새로운 접근 방식인 체현 사고 그래프(Embodied Graph-of-Thought) 기술을 제시합니다. 우리의 연구는 다중 로봇의 간단한 버전인 양팔 로봇을 고려하여 접근 방식을 검증합니다. 우리는 세 가지 다른 양팔 체현을 포함한 시뮬레이션 벤치마크와 실제 로봇 모두에서 방법의 효과를 검증합니다. 특히, 제안된 ET-VLA는 6가지 실제 작업에서 OpenVLA보다 53.2% 이상 뛰어난 성능을 보입니다. 우리는 모든 코드를 오픈소스로 공개하여 로봇 학습을 위한 VLA 모델 발전을 지원할 것입니다.
