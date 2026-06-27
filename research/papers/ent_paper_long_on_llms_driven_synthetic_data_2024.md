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
  en: A 2024 survey that organizes research on LLM-driven synthetic data generation,
    curation, and evaluation around a unified workflow, and identifies research gaps
    and future directions.
  zh: 2024年发表的一篇综述，围绕统一工作流程梳理了大语言模型驱动的合成数据生成、整理与评估研究，并指出了研究空白与未来方向。
  ko: 2024년에 발표된 서베이로, 대형 언어 모델 기반 합성 데이터 생성, 큐레이션 및 평가 연구를 통합된 워크플로우 중심으로 정리하고 연구
    공백과 미래 방향을 제시한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full-text verification
    required before promotion to verified.
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

## Overview

This survey paper provides a systematic organization of research on synthetic data generation driven by Large Language Models (LLMs). It structures the literature around a generic workflow that spans data generation, data curation, and evaluation. The paper argues that prior work in the field has lacked a unified framework and has largely remained fragmented. By mapping existing studies onto the proposed workflow, the authors highlight where current methods succeed and where key gaps remain.

The surveyed generation techniques include prompt engineering strategies and multi-step generation approaches. For curation, the paper discusses high-quality sample filtering and label enhancement methods. The evaluation section covers both direct and indirect methods for assessing synthetic datasets. Throughout, the authors emphasize the difficulty of producing synthetic data that is simultaneously correct and diverse, and they outline future research directions such as complex task decomposition, knowledge enhancement, and human-model collaboration.

The survey is primarily focused on text data and LLM-centric approaches, with comparatively limited coverage of vision, speech, and other modalities. The authors note that page limits prevented a more detailed analysis of data annotation, tuning techniques, and downstream applications, and that the fast pace of the field means the latest works may not be fully covered.

## Key Contributions

- Proposes a unified generic workflow for LLM-driven synthetic data generation, curation, and evaluation.
- Systematically surveys generation techniques, including prompt engineering and multi-step generation.
- Reviews data curation methods such as high-quality sample filtering and label enhancement.
- Summarizes direct and indirect evaluation approaches for synthetic datasets.
- Identifies research gaps and future directions, including complex task decomposition, knowledge enhancement, and human-model collaboration.

## Relevance to Humanoid Robotics

The surveyed pipeline for LLM-driven synthetic data generation, curation, and evaluation can help scale the creation of high-quality, diverse training and evaluation data for humanoid robots. Synthetic data generated through this workflow could support the development of perception, reasoning, language interaction, and task-planning capabilities without relying solely on expensive real-world data collection. This is especially relevant for humanoid robotics, where real-world deployment data is often scarce, costly, or unsafe to gather at scale. The evaluation methods surveyed can also be adapted to benchmark synthetic data quality for humanoid-specific tasks.
