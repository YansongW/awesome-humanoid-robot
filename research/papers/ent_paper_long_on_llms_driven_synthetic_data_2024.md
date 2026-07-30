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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.15126v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
딥러닝 환경이 진화함에 따라 데이터의 양과 질에 관한 딜레마는 오랜 문제로 남아 있습니다. 최근 대규모 언어 모델(LLM)의 등장은 합성 데이터 생성을 통해 실제 데이터의 한계를 완화하는 데이터 중심 솔루션을 제공합니다. 그러나 이 분야에 대한 현재 연구는 통일된 프레임워크가 부족하고 대부분 표면적인 수준에 머물러 있습니다. 따라서 본 논문은 합성 데이터 생성의 일반적인 워크플로우를 기반으로 관련 연구를 체계화합니다. 이를 통해 기존 연구의 공백을 강조하고 향후 연구를 위한 잠재적 방향을 제시합니다. 이 작업은 학계와 산업계가 LLM 기반 합성 데이터 생성의 역량과 응용에 대해 더 깊고 체계적인 탐구를 하도록 이끄는 것을 목표로 합니다.

## 핵심 내용
딥러닝 환경이 진화함에 따라 데이터의 양과 질에 관한 딜레마는 오랜 문제로 남아 있습니다. 최근 대규모 언어 모델(LLM)의 등장은 합성 데이터 생성을 통해 실제 데이터의 한계를 완화하는 데이터 중심 솔루션을 제공합니다. 그러나 이 분야에 대한 현재 연구는 통일된 프레임워크가 부족하고 대부분 표면적인 수준에 머물러 있습니다. 따라서 본 논문은 합성 데이터 생성의 일반적인 워크플로우를 기반으로 관련 연구를 체계화합니다. 이를 통해 기존 연구의 공백을 강조하고 향후 연구를 위한 잠재적 방향을 제시합니다. 이 작업은 학계와 산업계가 LLM 기반 합성 데이터 생성의 역량과 응용에 대해 더 깊고 체계적인 탐구를 하도록 이끄는 것을 목표로 합니다.

## 参考
- http://arxiv.org/abs/2406.15126v1
