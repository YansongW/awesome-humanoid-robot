---
$id: ent_paper_ye_vla_r1_enhancing_reasoning_in_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLA-R1: Enhancing Reasoning in Vision-Language-Action Models'
  zh: VLA-R1
  ko: 'VLA-R1: Enhancing Reasoning in Vision-Language-Action Models'
summary:
  en: 'VLA-R1: Enhancing Reasoning in Vision-Language-Action Models (VLA-R1), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by GigaAI, CASIA, Tsinghua University.'
  zh: 'VLA-R1: Enhancing Reasoning in Vision-Language-Action Models (VLA-R1), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by GigaAI, CASIA, Tsinghua University.'
  ko: 'VLA-R1: Enhancing Reasoning in Vision-Language-Action Models (VLA-R1), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by GigaAI, CASIA, Tsinghua University.'
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
- vision_language_action
- vla
- vla_r1
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.01623v1.
sources:
- id: src_001
  type: paper
  title: 'VLA-R1: Enhancing Reasoning in Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2510.01623
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLA-R1 source
  url: https://doi.org/10.48550/arXiv.2510.01623
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models aim to unify perception, language understanding, and action generation, offering strong cross-task and cross-scene generalization with broad impact on embodied AI. However, current VLA models often lack explicit step-by-step reasoning, instead emitting final actions without considering affordance constraints or geometric relations. Their post-training pipelines also rarely reinforce reasoning quality, relying primarily on supervised fine-tuning with weak reward design. To address these challenges, we present VLA-R1, a reasoning-enhanced VLA that integrates Reinforcement Learning from Verifiable Rewards (RLVR) with Group Relative Policy Optimization (GRPO) to systematically optimize both reasoning and execution. Specifically, we design an RLVR-based post-training strategy with verifiable rewards for region alignment, trajectory consistency, and output formatting, thereby strengthening reasoning robustness and execution accuracy. Moreover, we develop VLA-CoT-13K, a high-quality dataset that provides chain-of-thought supervision explicitly aligned with affordance and trajectory annotations. Furthermore, extensive evaluations on in-domain, out-of-domain, simulation, and real-robot platforms demonstrate that VLA-R1 achieves superior generalization and real-world performance compared to prior VLA methods. We plan to release the model, code, and dataset following the publication of this work. Code: https://github.com/GigaAI-research/VLA-R1. Website: https://gigaai-research.github.io/VLA-R1.

## 核心内容
Vision-Language-Action (VLA) models aim to unify perception, language understanding, and action generation, offering strong cross-task and cross-scene generalization with broad impact on embodied AI. However, current VLA models often lack explicit step-by-step reasoning, instead emitting final actions without considering affordance constraints or geometric relations. Their post-training pipelines also rarely reinforce reasoning quality, relying primarily on supervised fine-tuning with weak reward design. To address these challenges, we present VLA-R1, a reasoning-enhanced VLA that integrates Reinforcement Learning from Verifiable Rewards (RLVR) with Group Relative Policy Optimization (GRPO) to systematically optimize both reasoning and execution. Specifically, we design an RLVR-based post-training strategy with verifiable rewards for region alignment, trajectory consistency, and output formatting, thereby strengthening reasoning robustness and execution accuracy. Moreover, we develop VLA-CoT-13K, a high-quality dataset that provides chain-of-thought supervision explicitly aligned with affordance and trajectory annotations. Furthermore, extensive evaluations on in-domain, out-of-domain, simulation, and real-robot platforms demonstrate that VLA-R1 achieves superior generalization and real-world performance compared to prior VLA methods. We plan to release the model, code, and dataset following the publication of this work. Code: https://github.com/GigaAI-research/VLA-R1. Website: https://gigaai-research.github.io/VLA-R1.

## 参考
- http://arxiv.org/abs/2510.01623v1

## Overview
Vision-Language-Action (VLA) models aim to unify perception, language understanding, and action generation, offering strong cross-task and cross-scene generalization with broad impact on embodied AI. However, current VLA models often lack explicit step-by-step reasoning, instead emitting final actions without considering affordance constraints or geometric relations. Their post-training pipelines also rarely reinforce reasoning quality, relying primarily on supervised fine-tuning with weak reward design. To address these challenges, we present VLA-R1, a reasoning-enhanced VLA that integrates Reinforcement Learning from Verifiable Rewards (RLVR) with Group Relative Policy Optimization (GRPO) to systematically optimize both reasoning and execution. Specifically, we design an RLVR-based post-training strategy with verifiable rewards for region alignment, trajectory consistency, and output formatting, thereby strengthening reasoning robustness and execution accuracy. Moreover, we develop VLA-CoT-13K, a high-quality dataset that provides chain-of-thought supervision explicitly aligned with affordance and trajectory annotations. Furthermore, extensive evaluations on in-domain, out-of-domain, simulation, and real-robot platforms demonstrate that VLA-R1 achieves superior generalization and real-world performance compared to prior VLA methods. We plan to release the model, code, and dataset following the publication of this work. Code: https://github.com/GigaAI-research/VLA-R1. Website: https://gigaai-research.github.io/VLA-R1.

## Content
Vision-Language-Action (VLA) models aim to unify perception, language understanding, and action generation, offering strong cross-task and cross-scene generalization with broad impact on embodied AI. However, current VLA models often lack explicit step-by-step reasoning, instead emitting final actions without considering affordance constraints or geometric relations. Their post-training pipelines also rarely reinforce reasoning quality, relying primarily on supervised fine-tuning with weak reward design. To address these challenges, we present VLA-R1, a reasoning-enhanced VLA that integrates Reinforcement Learning from Verifiable Rewards (RLVR) with Group Relative Policy Optimization (GRPO) to systematically optimize both reasoning and execution. Specifically, we design an RLVR-based post-training strategy with verifiable rewards for region alignment, trajectory consistency, and output formatting, thereby strengthening reasoning robustness and execution accuracy. Moreover, we develop VLA-CoT-13K, a high-quality dataset that provides chain-of-thought supervision explicitly aligned with affordance and trajectory annotations. Furthermore, extensive evaluations on in-domain, out-of-domain, simulation, and real-robot platforms demonstrate that VLA-R1 achieves superior generalization and real-world performance compared to prior VLA methods. We plan to release the model, code, and dataset following the publication of this work. Code: https://github.com/GigaAI-research/VLA-R1. Website: https://gigaai-research.github.io/VLA-R1.

## 개요
Vision-Language-Action (VLA) 모델은 지각, 언어 이해 및 행동 생성을 통합하여 교차 작업 및 교차 장면 일반화를 제공하며, 임베디드 AI에 광범위한 영향을 미칩니다. 그러나 현재의 VLA 모델은 종종 명시적인 단계별 추론이 부족하여, 어포던스 제약이나 기하학적 관계를 고려하지 않고 최종 행동을 출력합니다. 또한 사후 훈련 파이프라인은 추론 품질을 강화하는 경우가 드물며, 약한 보상 설계를 가진 지도 미세 조정에 주로 의존합니다. 이러한 문제를 해결하기 위해, 우리는 VLA-R1을 제안합니다. 이는 검증 가능한 보상으로부터의 강화 학습(RLVR)과 그룹 상대 정책 최적화(GRPO)를 통합하여 추론과 실행을 체계적으로 최적화하는 추론 강화 VLA입니다. 구체적으로, 우리는 영역 정렬, 궤적 일관성 및 출력 형식화를 위한 검증 가능한 보상을 기반으로 한 RLVR 기반 사후 훈련 전략을 설계하여 추론 견고성과 실행 정확성을 강화합니다. 또한, 어포던스 및 궤적 주석과 명시적으로 정렬된 사고 사슬 감독을 제공하는 고품질 데이터셋 VLA-CoT-13K를 개발합니다. 더 나아가, 도메인 내, 도메인 외, 시뮬레이션 및 실제 로봇 플랫폼에서의 광범위한 평가를 통해 VLA-R1이 이전 VLA 방법보다 우수한 일반화 및 실제 성능을 달성함을 입증합니다. 우리는 이 연구의 출판 후 모델, 코드 및 데이터셋을 공개할 계획입니다. 코드: https://github.com/GigaAI-research/VLA-R1. 웹사이트: https://gigaai-research.github.io/VLA-R1.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 지각, 언어 이해 및 행동 생성을 통합하여 교차 작업 및 교차 장면 일반화를 제공하며, 임베디드 AI에 광범위한 영향을 미칩니다. 그러나 현재의 VLA 모델은 종종 명시적인 단계별 추론이 부족하여, 어포던스 제약이나 기하학적 관계를 고려하지 않고 최종 행동을 출력합니다. 또한 사후 훈련 파이프라인은 추론 품질을 강화하는 경우가 드물며, 약한 보상 설계를 가진 지도 미세 조정에 주로 의존합니다. 이러한 문제를 해결하기 위해, 우리는 VLA-R1을 제안합니다. 이는 검증 가능한 보상으로부터의 강화 학습(RLVR)과 그룹 상대 정책 최적화(GRPO)를 통합하여 추론과 실행을 체계적으로 최적화하는 추론 강화 VLA입니다. 구체적으로, 우리는 영역 정렬, 궤적 일관성 및 출력 형식화를 위한 검증 가능한 보상을 기반으로 한 RLVR 기반 사후 훈련 전략을 설계하여 추론 견고성과 실행 정확성을 강화합니다. 또한, 어포던스 및 궤적 주석과 명시적으로 정렬된 사고 사슬 감독을 제공하는 고품질 데이터셋 VLA-CoT-13K를 개발합니다. 더 나아가, 도메인 내, 도메인 외, 시뮬레이션 및 실제 로봇 플랫폼에서의 광범위한 평가를 통해 VLA-R1이 이전 VLA 방법보다 우수한 일반화 및 실제 성능을 달성함을 입증합니다. 우리는 이 연구의 출판 후 모델, 코드 및 데이터셋을 공개할 계획입니다. 코드: https://github.com/GigaAI-research/VLA-R1. 웹사이트: https://gigaai-research.github.io/VLA-R1.
