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
  en: A 2025 arXiv review that surveys how large language models are integrated into service-robot task planning, organizing
    recent work into text, vision, audio, and multimodal input categories and identifying open challenges for unstructured
    domestic environments.
  zh: With the rapid advancement of large language models (LLMs) and robotics, service robots are increasingly becoming an
    integral part of daily life, offering a wide range of services in complex environments. To deliver these services intelligently
    and efficiently, robust and accurate task planning capabilities are essential. This paper presents a comprehensive overview
    of the integration of LLMs into service robotics, with a particular focus on their role in enhancing robotic task planning.
    First, the development and foundational techniques of LLMs, including pre-training, fine-tuning, retrieval-
  ko: 2025년 arXiv 리뷰로, 대형 언어 모델이 서비스 로봇 작업 계획에 어떻게 통합되는지 조사하고 최근 연구를 텍스트, 비전, 오디오, 멀티모달 입력 범주로 정리하며 비구조화된 가정 환경에서의 공개 과제를
    식별한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.23357v1.
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

## 概述
With the rapid advancement of large language models (LLMs) and robotics, service robots are increasingly becoming an integral part of daily life, offering a wide range of services in complex environments. To deliver these services intelligently and efficiently, robust and accurate task planning capabilities are essential. This paper presents a comprehensive overview of the integration of LLMs into service robotics, with a particular focus on their role in enhancing robotic task planning. First, the development and foundational techniques of LLMs, including pre-training, fine-tuning, retrieval-augmented generation (RAG), and prompt engineering, are reviewed. We then explore the application of LLMs as the cognitive core-`brain'-of service robots, discussing how LLMs contribute to improved autonomy and decision-making. Furthermore, recent advancements in LLM-driven task planning across various input modalities are analyzed, including text, visual, audio, and multimodal inputs. Finally, we summarize key challenges and limitations in current research and propose future directions to advance the task planning capabilities of service robots in complex, unstructured domestic environments. This review aims to serve as a valuable reference for researchers and practitioners in the fields of artificial intelligence and robotics.

## 核心内容
With the rapid advancement of large language models (LLMs) and robotics, service robots are increasingly becoming an integral part of daily life, offering a wide range of services in complex environments. To deliver these services intelligently and efficiently, robust and accurate task planning capabilities are essential. This paper presents a comprehensive overview of the integration of LLMs into service robotics, with a particular focus on their role in enhancing robotic task planning. First, the development and foundational techniques of LLMs, including pre-training, fine-tuning, retrieval-augmented generation (RAG), and prompt engineering, are reviewed. We then explore the application of LLMs as the cognitive core-`brain'-of service robots, discussing how LLMs contribute to improved autonomy and decision-making. Furthermore, recent advancements in LLM-driven task planning across various input modalities are analyzed, including text, visual, audio, and multimodal inputs. Finally, we summarize key challenges and limitations in current research and propose future directions to advance the task planning capabilities of service robots in complex, unstructured domestic environments. This review aims to serve as a valuable reference for researchers and practitioners in the fields of artificial intelligence and robotics.

## 参考
- http://arxiv.org/abs/2510.23357v1

## Overview
With the rapid advancement of large language models (LLMs) and robotics, service robots are increasingly becoming an integral part of daily life, offering a wide range of services in complex environments. To deliver these services intelligently and efficiently, robust and accurate task planning capabilities are essential. This paper presents a comprehensive overview of the integration of LLMs into service robotics, with a particular focus on their role in enhancing robotic task planning. First, the development and foundational techniques of LLMs, including pre-training, fine-tuning, retrieval-augmented generation (RAG), and prompt engineering, are reviewed. We then explore the application of LLMs as the cognitive core—"brain"—of service robots, discussing how LLMs contribute to improved autonomy and decision-making. Furthermore, recent advancements in LLM-driven task planning across various input modalities are analyzed, including text, visual, audio, and multimodal inputs. Finally, we summarize key challenges and limitations in current research and propose future directions to advance the task planning capabilities of service robots in complex, unstructured domestic environments. This review aims to serve as a valuable reference for researchers and practitioners in the fields of artificial intelligence and robotics.

## Content
With the rapid advancement of large language models (LLMs) and robotics, service robots are increasingly becoming an integral part of daily life, offering a wide range of services in complex environments. To deliver these services intelligently and efficiently, robust and accurate task planning capabilities are essential. This paper presents a comprehensive overview of the integration of LLMs into service robotics, with a particular focus on their role in enhancing robotic task planning. First, the development and foundational techniques of LLMs, including pre-training, fine-tuning, retrieval-augmented generation (RAG), and prompt engineering, are reviewed. We then explore the application of LLMs as the cognitive core—"brain"—of service robots, discussing how LLMs contribute to improved autonomy and decision-making. Furthermore, recent advancements in LLM-driven task planning across various input modalities are analyzed, including text, visual, audio, and multimodal inputs. Finally, we summarize key challenges and limitations in current research and propose future directions to advance the task planning capabilities of service robots in complex, unstructured domestic environments. This review aims to serve as a valuable reference for researchers and practitioners in the fields of artificial intelligence and robotics.

## 개요
대규모 언어 모델(LLM)과 로봇 공학의 급속한 발전에 힘입어, 서비스 로봇은 점차 일상생활의 필수적인 부분이 되어 복잡한 환경에서 다양한 서비스를 제공하고 있습니다. 이러한 서비스를 지능적이고 효율적으로 제공하기 위해서는 강력하고 정확한 작업 계획 능력이 필수적입니다. 본 논문은 LLM을 서비스 로봇 공학에 통합하는 것에 대한 포괄적인 개요를 제공하며, 특히 로봇 작업 계획 향상에 있어서의 역할에 중점을 둡니다. 먼저, 사전 학습, 미세 조정, 검색 증강 생성(RAG), 프롬프트 엔지니어링을 포함한 LLM의 발전과 기반 기술을 검토합니다. 그런 다음 LLM을 서비스 로봇의 인지적 핵심인 '두뇌'로 적용하는 방안을 탐구하며, LLM이 자율성과 의사 결정 향상에 어떻게 기여하는지 논의합니다. 또한, 텍스트, 시각, 오디오 및 다중 모달 입력을 포함한 다양한 입력 양식에서 LLM 기반 작업 계획의 최근 발전을 분석합니다. 마지막으로, 현재 연구의 주요 과제와 한계를 요약하고, 복잡하고 비구조화된 가정 환경에서 서비스 로봇의 작업 계획 능력을 발전시키기 위한 미래 방향을 제안합니다. 본 리뷰는 인공지능 및 로봇 공학 분야의 연구자와 실무자에게 귀중한 참고 자료가 되고자 합니다.

## 핵심 내용
대규모 언어 모델(LLM)과 로봇 공학의 급속한 발전에 힘입어, 서비스 로봇은 점차 일상생활의 필수적인 부분이 되어 복잡한 환경에서 다양한 서비스를 제공하고 있습니다. 이러한 서비스를 지능적이고 효율적으로 제공하기 위해서는 강력하고 정확한 작업 계획 능력이 필수적입니다. 본 논문은 LLM을 서비스 로봇 공학에 통합하는 것에 대한 포괄적인 개요를 제공하며, 특히 로봇 작업 계획 향상에 있어서의 역할에 중점을 둡니다. 먼저, 사전 학습, 미세 조정, 검색 증강 생성(RAG), 프롬프트 엔지니어링을 포함한 LLM의 발전과 기반 기술을 검토합니다. 그런 다음 LLM을 서비스 로봇의 인지적 핵심인 '두뇌'로 적용하는 방안을 탐구하며, LLM이 자율성과 의사 결정 향상에 어떻게 기여하는지 논의합니다. 또한, 텍스트, 시각, 오디오 및 다중 모달 입력을 포함한 다양한 입력 양식에서 LLM 기반 작업 계획의 최근 발전을 분석합니다. 마지막으로, 현재 연구의 주요 과제와 한계를 요약하고, 복잡하고 비구조화된 가정 환경에서 서비스 로봇의 작업 계획 능력을 발전시키기 위한 미래 방향을 제안합니다. 본 리뷰는 인공지능 및 로봇 공학 분야의 연구자와 실무자에게 귀중한 참고 자료가 되고자 합니다.
