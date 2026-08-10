---
$id: ent_paper_long_on_llms_driven_synthetic_data_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'On LLMs-Driven Synthetic Data Generation, Curation, and Evaluation: A Survey'
  zh: 基于大语言模型的合成数据生成、整理与评估：综述
  ko: '대형 언어 모델 기반 합성 데이터 생성, 큐레이션 및 평가: 서베이'
summary:
  en: A 2024 survey that organizes research on LLM-driven synthetic data generation, curation, and evaluation around a unified
    workflow, and identifies research gaps and future directions.
  zh: 这是一篇2024年的综述论文，系统梳理了由大型语言模型（LLMs）驱动的合成数据生成、筛选与评估研究。论文围绕一个统一的工作流框架组织现有工作，并指出了当前研究中的空白与未来方向。
  ko: 2024년에 발표된 서베이로, 대형 언어 모델 기반 합성 데이터 생성, 큐레이션 및 평가 연구를 통합된 워크플로우 중심으로 정리하고 연구 공백과 미래 방향을 제시한다.
domains:
- 09_data_datasets
- 07_ai_models_algorithms
- 10_evaluation_benchmarks
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
tags:
- synthetic_data
- llm
- data_curation
- data_generation
- evaluation
- survey
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.15126v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (814 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'On LLMs-Driven Synthetic Data Generation, Curation, and Evaluation: A Survey'
  url: https://arxiv.org/abs/2406.15126
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
在深度学习不断演进的背景下，数据数量与质量的矛盾始终是一个长期难题。大型语言模型（LLMs）的兴起提供了一种以数据为中心的解决方案，通过合成数据生成来缓解真实世界数据的局限性。然而，当前该领域的研究缺乏统一框架，大多停留在表面。为此，本文基于合成数据生成的通用工作流，对相关研究进行了系统组织，从而凸显现有研究中的空白，并勾勒出未来研究的潜在方向。这项工作旨在引导学术界和工业界对LLMs驱动的合成数据生成的能力与应用进行更深入、更有条理的探索。

## 核心内容
### 研究背景与问题
- 深度学习领域长期面临数据数量与质量的矛盾，真实世界数据往往存在标注成本高、隐私限制或分布偏差等问题。
- 大型语言模型（LLMs）的兴起为数据稀缺问题提供了新的解决思路：通过合成数据生成来补充或替代真实数据。

### 核心贡献：统一工作流框架
- 论文提出一个通用的合成数据生成工作流，将现有研究组织到以下阶段：
  - **生成（Generation）**：利用LLMs根据提示或模板生成原始合成数据。
  - **筛选（Curation）**：对生成的原始数据进行质量过滤、去重或多样性增强。
  - **评估（Evaluation）**：通过下游任务性能、数据质量指标或人工评估来验证合成数据的有效性。

### 研究空白与未来方向
- 现有研究大多聚焦于生成阶段，而对筛选与评估的系统性研究不足。
- 缺乏标准化的评估基准和指标来比较不同合成数据生成方法的优劣。
- 未来方向包括：
  - 开发更高效的筛选策略，以自动识别高质量合成数据。
  - 建立跨任务、跨领域的统一评估框架。
  - 探索LLMs在生成多模态合成数据（如文本+图像）中的潜力。

### 结论
- 本文通过统一工作流框架，为LLMs驱动的合成数据生成研究提供了系统化视角，并呼吁社区在筛选与评估环节投入更多努力，以推动该领域的成熟应用。

## Overview
Within the evolving landscape of deep learning, the dilemma of data quantity and quality has been a long-standing problem. The recent advent of Large Language Models (LLMs) offers a data-centric solution to alleviate the limitations of real-world data with synthetic data generation. However, current investigations into this field lack a unified framework and mostly stay on the surface. Therefore, this paper provides an organization of relevant studies based on a generic workflow of synthetic data generation. By doing so, we highlight the gaps within existing research and outline prospective avenues for future study. This work aims to shepherd the academic and industrial communities towards deeper, more methodical inquiries into the capabilities and applications of LLMs-driven synthetic data generation.

## 参考
- http://arxiv.org/abs/2406.15126v1

## 개요
딥러닝이 지속적으로 진화하는 배경 속에서, 데이터의 양과 질 사이의 모순은 오랫동안 해결하기 어려운 과제로 남아 있습니다. 대규모 언어 모델(LLMs)의 부상은 데이터 중심의 해결책을 제공하며, 합성 데이터 생성을 통해 실제 세계 데이터의 한계를 완화합니다. 그러나 현재 이 분야의 연구는 통일된 프레임워크가 부족하고 대부분 표면적인 수준에 머물러 있습니다. 이에 본 논문은 합성 데이터 생성의 일반적인 워크플로우를 기반으로 관련 연구를 체계적으로 정리하여, 기존 연구의 공백을 부각시키고 향후 연구의 잠재적 방향을 제시합니다. 이 작업은 학계와 산업계가 LLMs 기반 합성 데이터 생성의 역량과 응용을 더 깊고 체계적으로 탐구하도록 이끄는 것을 목표로 합니다.

## 핵심 내용
### 연구 배경 및 문제
- 딥러닝 분야는 오랫동안 데이터 양과 질의 모순에 직면해 있으며, 실제 세계 데이터는 종종 높은 주석 비용, 개인정보 보호 제한, 또는 분포 편향 등의 문제를 지닙니다.
- 대규모 언어 모델(LLMs)의 부상은 데이터 부족 문제에 대한 새로운 해결 방안을 제시합니다: 합성 데이터 생성을 통해 실제 데이터를 보완하거나 대체하는 것입니다.

### 핵심 기여: 통일된 워크플로우 프레임워크
- 본 논문은 일반적인 합성 데이터 생성 워크플로우를 제안하며, 기존 연구를 다음 단계로 구성합니다:
  - **생성(Generation)**: LLMs를 활용하여 프롬프트나 템플릿에 따라 원시 합성 데이터를 생성합니다.
  - **선별(Curation)**: 생성된 원시 데이터에 대해 품질 필터링, 중복 제거, 또는 다양성 강화를 수행합니다.
  - **평가(Evaluation)**: 다운스트림 작업 성능, 데이터 품질 지표, 또는 인간 평가를 통해 합성 데이터의 유효성을 검증합니다.

### 연구 공백 및 향후 방향
- 기존 연구는 대부분 생성 단계에 집중되어 있으며, 선별과 평가에 대한 체계적인 연구는 부족합니다.
- 서로 다른 합성 데이터 생성 방법의 우열을 비교하기 위한 표준화된 평가 기준과 지표가 부재합니다.
- 향후 방향은 다음과 같습니다:
  - 고품질 합성 데이터를 자동으로 식별하기 위한 더 효율적인 선별 전략 개발.
  - 작업 및 도메인을 아우르는 통일된 평가 프레임워크 구축.
  - 다중 모달 합성 데이터(예: 텍스트+이미지) 생성에서 LLMs의 잠재력 탐구.

### 결론
- 본 논문은 통일된 워크플로우 프레임워크를 통해 LLMs 기반 합성 데이터 생성 연구에 체계적인 관점을 제공하며, 커뮤니티가 선별과 평가 단계에 더 많은 노력을 기울여 이 분야의 성숙한 응용을 촉진할 것을 촉구합니다.
