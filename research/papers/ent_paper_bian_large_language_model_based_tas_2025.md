---
$id: ent_paper_bian_large_language_model_based_tas_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Large language model-based task planning for service robots: A review'
  zh: 基于大语言模型的服务机器人任务规划：综述
  ko: '대형 언어 모델 기반 서비스 로봇 작업 계획: 리뷰'
summary:
  en: A 2025 arXiv review that surveys how large language models are integrated into
    service-robot task planning, organizing recent work into text, vision, audio,
    and multimodal input categories and identifying open challenges for unstructured
    domestic environments.
  zh: 2025年arXiv综述，调查大语言模型如何融入服务机器人任务规划，将近期研究按文本、视觉、音频和多模态输入分类，并指出非结构化家庭环境中的开放挑战。
  ko: 2025년 arXiv 리뷰로, 대형 언어 모델이 서비스 로봇 작업 계획에 어떻게 통합되는지 조사하고 최근 연구를 텍스트, 비전, 오디오,
    멀티모달 입력 범주로 정리하며 비구조화된 가정 환경에서의 공개 과제를 식별한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- llm
- task_planning
- service_robot
- multimodal
- rag
- prompt_engineering
- vision_language_model
- domestic_robotics
- embodied_ai
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full paper was not independently
    retrieved for sentence-level verification.; approved by autonomous review workflow.
sources:
- id: src_001
  type: paper
  title: 'Large language model-based task planning for service robots: A review'
  url: https://arxiv.org/abs/2510.23357
  date: '2025'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

This paper provides a systematic review of how large language models (LLMs) are being applied to task planning in service robotics. It first surveys LLM foundations, including pre-training, fine-tuning, retrieval-augmented generation (RAG), and prompt engineering. It then positions LLMs as the cognitive "brain" of service robots and examines how they improve autonomy and decision-making in complex environments. The bulk of the review organizes recent advances according to input modality—text, vision, audio, and multimodal—and discusses how each modality contributes to perception, reasoning, and action generation for robotic task planning.

The authors adopt a modality-centric taxonomy rather than a method-by-method comparison. Text-based planning is treated as the earliest and most mature strand, while vision- and audio-based approaches are reviewed as rapidly growing areas driven by vision-language models and audio understanding models. Multimodal fusion is highlighted as a key frontier, with the authors noting that effective integration across text, vision, audio, and tactile sensing remains unresolved.

The review concludes with a critical discussion of limitations, including LLM hallucination, high inference latency, insufficient active task cognition, the scarcity of tactile language models, and the absence of unified evaluation benchmarks for single-modal and multimodal service-robot task planning. Future directions emphasize improving real-time performance, robustness, and multimodal fusion for unstructured domestic environments.

## Key Contributions

- Systematic review of LLM development and core techniques including pre-training, fine-tuning, RAG, and prompt engineering.
- First modality-centric taxonomy for LLM-based task planning in domestic service robotics covering text, vision, audio, and multimodal inputs.
- Critical analysis of deployment obstacles and actionable future research directions for service robot task planning in complex, unstructured home environments.

## Relevance to Humanoid Robotics

The review explicitly connects LLM-driven service-robot task planning to general-purpose humanoid robots, citing systems such as Gemini Robotics and NVIDIA GR00T as examples of embodied intelligence that rely on the same cognitive decision-making stack. The surveyed text, visual, audio, and multimodal planning methods map directly onto the perception-reasoning-action pipeline required by humanoid robots operating in unstructured home and service environments. Consequently, advances in robust multimodal fusion, real-time LLM inference, and active task cognition identified in the paper are highly relevant to scaling general-purpose humanoid systems.
