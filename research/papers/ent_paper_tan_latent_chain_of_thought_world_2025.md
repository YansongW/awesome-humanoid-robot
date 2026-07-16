---
$id: ent_paper_tan_latent_chain_of_thought_world_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Latent Chain-of-Thought World Modeling for End-to-End Driving
  zh: LCDrive
  ko: Latent Chain-of-Thought World Modeling for End-to-End Driving
summary:
  en: Latent Chain-of-Thought World Modeling for End-to-End Driving (LCDrive), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by University of Tübingen.
  zh: Latent Chain-of-Thought World Modeling for End-to-End Driving (LCDrive), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by University of Tübingen.
  ko: Latent Chain-of-Thought World Modeling for End-to-End Driving (LCDrive), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by University of Tübingen.
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
- lcdrive
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.10226v2.
sources:
- id: src_001
  type: paper
  title: Latent Chain-of-Thought World Modeling for End-to-End Driving (arXiv)
  url: https://arxiv.org/abs/2512.10226
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: LCDrive source
  url: https://doi.org/10.48550/arXiv.2512.10226
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent Vision-Language-Action (VLA) models for autonomous driving explore inference-time reasoning as a way to improve driving performance and safety in challenging scenarios. Most prior work uses natural language to express chain-of-thought (CoT) reasoning before producing driving actions. However, text may not be the most efficient representation for reasoning. In this work, we present Latent-CoT-Drive (LCDrive): a model that expresses CoT in a latent language that captures possible outcomes of the driving actions being considered. Our approach unifies CoT reasoning and decision making by representing both in an action-aligned latent space. Instead of natural language, the model reasons by interleaving (1) action-proposal tokens, which use the same vocabulary as the model's output actions; and (2) world model tokens, which are grounded in a learned latent world model and express future outcomes of these actions. We cold start latent CoT by supervising the model's action proposals and world model tokens based on ground-truth future rollouts of the scene. We then post-train with closed-loop reinforcement learning to strengthen reasoning capabilities. On a large-scale end-to-end driving benchmark, LCDrive achieves faster inference, better trajectory quality, and larger improvements from interactive reinforcement learning compared to both non-reasoning and text-reasoning baselines.

## 核心内容
Recent Vision-Language-Action (VLA) models for autonomous driving explore inference-time reasoning as a way to improve driving performance and safety in challenging scenarios. Most prior work uses natural language to express chain-of-thought (CoT) reasoning before producing driving actions. However, text may not be the most efficient representation for reasoning. In this work, we present Latent-CoT-Drive (LCDrive): a model that expresses CoT in a latent language that captures possible outcomes of the driving actions being considered. Our approach unifies CoT reasoning and decision making by representing both in an action-aligned latent space. Instead of natural language, the model reasons by interleaving (1) action-proposal tokens, which use the same vocabulary as the model's output actions; and (2) world model tokens, which are grounded in a learned latent world model and express future outcomes of these actions. We cold start latent CoT by supervising the model's action proposals and world model tokens based on ground-truth future rollouts of the scene. We then post-train with closed-loop reinforcement learning to strengthen reasoning capabilities. On a large-scale end-to-end driving benchmark, LCDrive achieves faster inference, better trajectory quality, and larger improvements from interactive reinforcement learning compared to both non-reasoning and text-reasoning baselines.

## 参考
- http://arxiv.org/abs/2512.10226v2

## Overview
Recent Vision-Language-Action (VLA) models for autonomous driving explore inference-time reasoning as a way to improve driving performance and safety in challenging scenarios. Most prior work uses natural language to express chain-of-thought (CoT) reasoning before producing driving actions. However, text may not be the most efficient representation for reasoning. In this work, we present Latent-CoT-Drive (LCDrive): a model that expresses CoT in a latent language that captures possible outcomes of the driving actions being considered. Our approach unifies CoT reasoning and decision making by representing both in an action-aligned latent space. Instead of natural language, the model reasons by interleaving (1) action-proposal tokens, which use the same vocabulary as the model's output actions; and (2) world model tokens, which are grounded in a learned latent world model and express future outcomes of these actions. We cold start latent CoT by supervising the model's action proposals and world model tokens based on ground-truth future rollouts of the scene. We then post-train with closed-loop reinforcement learning to strengthen reasoning capabilities. On a large-scale end-to-end driving benchmark, LCDrive achieves faster inference, better trajectory quality, and larger improvements from interactive reinforcement learning compared to both non-reasoning and text-reasoning baselines.

## Content
Recent Vision-Language-Action (VLA) models for autonomous driving explore inference-time reasoning as a way to improve driving performance and safety in challenging scenarios. Most prior work uses natural language to express chain-of-thought (CoT) reasoning before producing driving actions. However, text may not be the most efficient representation for reasoning. In this work, we present Latent-CoT-Drive (LCDrive): a model that expresses CoT in a latent language that captures possible outcomes of the driving actions being considered. Our approach unifies CoT reasoning and decision making by representing both in an action-aligned latent space. Instead of natural language, the model reasons by interleaving (1) action-proposal tokens, which use the same vocabulary as the model's output actions; and (2) world model tokens, which are grounded in a learned latent world model and express future outcomes of these actions. We cold start latent CoT by supervising the model's action proposals and world model tokens based on ground-truth future rollouts of the scene. We then post-train with closed-loop reinforcement learning to strengthen reasoning capabilities. On a large-scale end-to-end driving benchmark, LCDrive achieves faster inference, better trajectory quality, and larger improvements from interactive reinforcement learning compared to both non-reasoning and text-reasoning baselines.

## 개요
최근 자율주행을 위한 Vision-Language-Action(VLA) 모델은 까다로운 시나리오에서 주행 성능과 안전성을 향상시키기 위해 추론 시간 추론을 탐구하고 있습니다. 대부분의 기존 연구는 주행 동작을 생성하기 전에 자연어를 사용하여 사고 사슬(CoT) 추론을 표현합니다. 그러나 텍스트는 추론에 가장 효율적인 표현이 아닐 수 있습니다. 본 연구에서는 고려 중인 주행 동작의 가능한 결과를 포착하는 잠재 언어로 CoT를 표현하는 Latent-CoT-Drive(LCDrive)를 제시합니다. 우리의 접근 방식은 CoT 추론과 의사 결정을 모두 동작 정렬 잠재 공간에서 표현하여 통합합니다. 자연어 대신 모델은 (1) 모델의 출력 동작과 동일한 어휘를 사용하는 동작 제안 토큰과 (2) 학습된 잠재 세계 모델에 기반하여 이러한 동작의 미래 결과를 표현하는 세계 모델 토큰을 교차 배치하여 추론합니다. 우리는 장면의 실제 미래 롤아웃을 기반으로 모델의 동작 제안 및 세계 모델 토큰을 감독하여 잠재 CoT를 콜드 스타트합니다. 그런 다음 폐쇄 루프 강화 학습으로 사후 학습하여 추론 능력을 강화합니다. 대규모 엔드투엔드 주행 벤치마크에서 LCDrive는 비추론 및 텍스트 추론 기준선에 비해 더 빠른 추론, 더 나은 궤적 품질, 상호작용 강화 학습으로부터의 더 큰 개선을 달성합니다.

## 핵심 내용
최근 자율주행을 위한 Vision-Language-Action(VLA) 모델은 까다로운 시나리오에서 주행 성능과 안전성을 향상시키기 위해 추론 시간 추론을 탐구하고 있습니다. 대부분의 기존 연구는 주행 동작을 생성하기 전에 자연어를 사용하여 사고 사슬(CoT) 추론을 표현합니다. 그러나 텍스트는 추론에 가장 효율적인 표현이 아닐 수 있습니다. 본 연구에서는 고려 중인 주행 동작의 가능한 결과를 포착하는 잠재 언어로 CoT를 표현하는 Latent-CoT-Drive(LCDrive)를 제시합니다. 우리의 접근 방식은 CoT 추론과 의사 결정을 모두 동작 정렬 잠재 공간에서 표현하여 통합합니다. 자연어 대신 모델은 (1) 모델의 출력 동작과 동일한 어휘를 사용하는 동작 제안 토큰과 (2) 학습된 잠재 세계 모델에 기반하여 이러한 동작의 미래 결과를 표현하는 세계 모델 토큰을 교차 배치하여 추론합니다. 우리는 장면의 실제 미래 롤아웃을 기반으로 모델의 동작 제안 및 세계 모델 토큰을 감독하여 잠재 CoT를 콜드 스타트합니다. 그런 다음 폐쇄 루프 강화 학습으로 사후 학습하여 추론 능력을 강화합니다. 대규모 엔드투엔드 주행 벤치마크에서 LCDrive는 비추론 및 텍스트 추론 기준선에 비해 더 빠른 추론, 더 나은 궤적 품질, 상호작용 강화 학습으로부터의 더 큰 개선을 달성합니다.
