---
$id: ent_paper_li_a_self_correcting_vision_langu_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation
  zh: SC-VLA
  ko: A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation
summary:
  en: A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation (SC-VLA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Peking University.
  zh: A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation (SC-VLA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Peking University.
  ko: A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation (SC-VLA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Peking University.
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
- sc_vla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2405.17418v2.
sources:
- id: src_001
  type: paper
  title: A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation (arXiv)
  url: https://arxiv.org/abs/2405.17418
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Recently, some studies have integrated Multimodal Large Language Models into robotic manipulation, constructing vision-language-action models (VLAs) to interpret multimodal information and predict SE(3) poses. While VLAs have shown promising progress, they may suffer from failures when faced with novel and complex tasks. To emulate human-like reasoning for more robust manipulation, we propose the self-corrected (SC-)VLA framework, which integrates fast system for directly predicting actions and slow system for reflecting on failed actions within a single VLA policy. For the fast system, we incorporate parameter-efficient fine-tuning to equip the model with pose prediction capabilities while preserving the inherent reasoning abilities of MLLMs. For the slow system, we propose a Chain-of-Thought training strategy for failure correction, designed to mimic human reflection after a manipulation failure. Specifically, our model learns to identify the causes of action failures, adaptively seek expert feedback, reflect on the current failure scenario, and iteratively generate corrective actions, step by step. Furthermore, a continuous policy learning method is designed based on successfully corrected samples, enhancing the fast system's adaptability to the current configuration. We compare SC-VLA with the previous SOTA VLA in both simulation and real-world tasks, demonstrating an efficient correction process and improved manipulation accuracy on both seen and unseen tasks.

## 核心内容
Recently, some studies have integrated Multimodal Large Language Models into robotic manipulation, constructing vision-language-action models (VLAs) to interpret multimodal information and predict SE(3) poses. While VLAs have shown promising progress, they may suffer from failures when faced with novel and complex tasks. To emulate human-like reasoning for more robust manipulation, we propose the self-corrected (SC-)VLA framework, which integrates fast system for directly predicting actions and slow system for reflecting on failed actions within a single VLA policy. For the fast system, we incorporate parameter-efficient fine-tuning to equip the model with pose prediction capabilities while preserving the inherent reasoning abilities of MLLMs. For the slow system, we propose a Chain-of-Thought training strategy for failure correction, designed to mimic human reflection after a manipulation failure. Specifically, our model learns to identify the causes of action failures, adaptively seek expert feedback, reflect on the current failure scenario, and iteratively generate corrective actions, step by step. Furthermore, a continuous policy learning method is designed based on successfully corrected samples, enhancing the fast system's adaptability to the current configuration. We compare SC-VLA with the previous SOTA VLA in both simulation and real-world tasks, demonstrating an efficient correction process and improved manipulation accuracy on both seen and unseen tasks.

## 参考
- http://arxiv.org/abs/2405.17418v2

## Overview
Recently, some studies have integrated Multimodal Large Language Models into robotic manipulation, constructing vision-language-action models (VLAs) to interpret multimodal information and predict SE(3) poses. While VLAs have shown promising progress, they may suffer from failures when faced with novel and complex tasks. To emulate human-like reasoning for more robust manipulation, we propose the self-corrected (SC-)VLA framework, which integrates a fast system for directly predicting actions and a slow system for reflecting on failed actions within a single VLA policy. For the fast system, we incorporate parameter-efficient fine-tuning to equip the model with pose prediction capabilities while preserving the inherent reasoning abilities of MLLMs. For the slow system, we propose a Chain-of-Thought training strategy for failure correction, designed to mimic human reflection after a manipulation failure. Specifically, our model learns to identify the causes of action failures, adaptively seek expert feedback, reflect on the current failure scenario, and iteratively generate corrective actions, step by step. Furthermore, a continuous policy learning method is designed based on successfully corrected samples, enhancing the fast system's adaptability to the current configuration. We compare SC-VLA with the previous SOTA VLA in both simulation and real-world tasks, demonstrating an efficient correction process and improved manipulation accuracy on both seen and unseen tasks.

## Content
Recently, some studies have integrated Multimodal Large Language Models into robotic manipulation, constructing vision-language-action models (VLAs) to interpret multimodal information and predict SE(3) poses. While VLAs have shown promising progress, they may suffer from failures when faced with novel and complex tasks. To emulate human-like reasoning for more robust manipulation, we propose the self-corrected (SC-)VLA framework, which integrates a fast system for directly predicting actions and a slow system for reflecting on failed actions within a single VLA policy. For the fast system, we incorporate parameter-efficient fine-tuning to equip the model with pose prediction capabilities while preserving the inherent reasoning abilities of MLLMs. For the slow system, we propose a Chain-of-Thought training strategy for failure correction, designed to mimic human reflection after a manipulation failure. Specifically, our model learns to identify the causes of action failures, adaptively seek expert feedback, reflect on the current failure scenario, and iteratively generate corrective actions, step by step. Furthermore, a continuous policy learning method is designed based on successfully corrected samples, enhancing the fast system's adaptability to the current configuration. We compare SC-VLA with the previous SOTA VLA in both simulation and real-world tasks, demonstrating an efficient correction process and improved manipulation accuracy on both seen and unseen tasks.

## 개요
최근 일부 연구에서는 멀티모달 대규모 언어 모델을 로봇 조작에 통합하여, 멀티모달 정보를 해석하고 SE(3) 포즈를 예측하는 비전-언어-행동 모델(VLA)을 구축하고 있습니다. VLA는 유망한 진전을 보여주었지만, 새롭고 복잡한 작업에 직면했을 때 실패할 수 있습니다. 보다 강력한 조작을 위해 인간과 유사한 추론을 모방하기 위해, 우리는 단일 VLA 정책 내에서 직접 행동을 예측하는 빠른 시스템과 실패한 행동을 반성하는 느린 시스템을 통합한 자기 교정(SC-)VLA 프레임워크를 제안합니다. 빠른 시스템의 경우, MLLM의 고유 추론 능력을 유지하면서 포즈 예측 능력을 모델에 부여하기 위해 파라미터 효율적 미세 조정을 도입합니다. 느린 시스템의 경우, 조작 실패 후 인간의 반성을 모방하도록 설계된 실패 교정을 위한 사고 사슬 훈련 전략을 제안합니다. 구체적으로, 우리의 모델은 행동 실패의 원인을 식별하고, 적응적으로 전문가 피드백을 구하며, 현재 실패 시나리오를 반성하고, 단계별로 교정 행동을 반복적으로 생성하는 방법을 학습합니다. 또한, 성공적으로 교정된 샘플을 기반으로 지속적 정책 학습 방법이 설계되어, 현재 구성에 대한 빠른 시스템의 적응성을 향상시킵니다. 우리는 SC-VLA를 이전 SOTA VLA와 시뮬레이션 및 실제 작업 모두에서 비교하여, 효율적인 교정 과정과 보거나 보지 못한 작업 모두에서 개선된 조작 정확도를 입증합니다.

## 핵심 내용
최근 일부 연구에서는 멀티모달 대규모 언어 모델을 로봇 조작에 통합하여, 멀티모달 정보를 해석하고 SE(3) 포즈를 예측하는 비전-언어-행동 모델(VLA)을 구축하고 있습니다. VLA는 유망한 진전을 보여주었지만, 새롭고 복잡한 작업에 직면했을 때 실패할 수 있습니다. 보다 강력한 조작을 위해 인간과 유사한 추론을 모방하기 위해, 우리는 단일 VLA 정책 내에서 직접 행동을 예측하는 빠른 시스템과 실패한 행동을 반성하는 느린 시스템을 통합한 자기 교정(SC-)VLA 프레임워크를 제안합니다. 빠른 시스템의 경우, MLLM의 고유 추론 능력을 유지하면서 포즈 예측 능력을 모델에 부여하기 위해 파라미터 효율적 미세 조정을 도입합니다. 느린 시스템의 경우, 조작 실패 후 인간의 반성을 모방하도록 설계된 실패 교정을 위한 사고 사슬 훈련 전략을 제안합니다. 구체적으로, 우리의 모델은 행동 실패의 원인을 식별하고, 적응적으로 전문가 피드백을 구하며, 현재 실패 시나리오를 반성하고, 단계별로 교정 행동을 반복적으로 생성하는 방법을 학습합니다. 또한, 성공적으로 교정된 샘플을 기반으로 지속적 정책 학습 방법이 설계되어, 현재 구성에 대한 빠른 시스템의 적응성을 향상시킵니다. 우리는 SC-VLA를 이전 SOTA VLA와 시뮬레이션 및 실제 작업 모두에서 비교하여, 효율적인 교정 과정과 보거나 보지 못한 작업 모두에서 개선된 조작 정확도를 입증합니다.
