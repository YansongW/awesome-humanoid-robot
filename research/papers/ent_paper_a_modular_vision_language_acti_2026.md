---
$id: ent_paper_a_modular_vision_language_acti_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Modular Vision-Language-Action Robotics Framework for Indoor Environments
  zh: A Modular Vision-Language-Action Robotics Framework for Indoor Environments
  ko: A Modular Vision-Language-Action Robotics Framework for Indoor Environments
summary:
  en: 'arXiv:2606.31144v1 Announce Type: new Abstract: This paper presents an integrated system for the CMU Vision-Language-Action
    (VLA) Challenge, designed to enable an autonomous agent to perform complex tasks based on natural language instructions.
    Our framework employs a modular architecture that orchestrates environment mapping, question processing, and navigation.
    The system operates in two parallel streams: a perception pipeline that constructs a semantic voxel map from real-time
    camera feeds using OwlViT embeddings, and a language pipeline that classifies user commands with a Vision-Language Model.
    The mapping is time-constrained; the system proceeds with a partial map if a 500-second exploration limit is reached.
    The classified query is then grounded in the geometric and semantic context of the map to generate a detailed prompt for
    the VLM. This yields an actionable output, demonstrating a capable solution for bridging the gap between human language
    and robotic action.'
  zh: 'arXiv:2606.31144v1 Announce Type: new Abstract: This paper presents an integrated system for the CMU Vision-Language-Action
    (VLA) Challenge, designed to enable an autonomous agent to perform complex tasks based on natural language instructions.
    Our framework employs a modular architecture that orchestrates environment mapping, question processing, and navigation.
    The system operates in two parallel streams: a perception pipeline that constructs a semantic voxel map from real-time
    camera feeds using OwlViT embeddings, and a language pipeline that classifies user commands with a Vision-Language Model.
    The mapping is time-constrained; the system proceeds with a partial map if a 500-second exploration limit is reached.
    The classified query is then grounded in the geometric and semantic context of the map to generate a detailed prompt for
    the VLM. This yields an actionable output, demonstrating a capable solution for bridging the gap between human language
    and robotic action.'
  ko: 'arXiv:2606.31144v1 Announce Type: new Abstract: This paper presents an integrated system for the CMU Vision-Language-Action
    (VLA) Challenge, designed to enable an autonomous agent to perform complex tasks based on natural language instructions.
    Our framework employs a modular architecture that orchestrates environment mapping, question processing, and navigation.
    The system operates in two parallel streams: a perception pipeline that constructs a semantic voxel map from real-time
    camera feeds using OwlViT embeddings, and a language pipeline that classifies user commands with a Vision-Language Model.
    The mapping is time-constrained; the system proceeds with a partial map if a 500-second exploration limit is reached.
    The classified query is then grounded in the geometric and semantic context of the map to generate a detailed prompt for
    the VLM. This yields an actionable output, demonstrating a capable solution for bridging the gap between human language
    and robotic action.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- a_modular_vision_language_acti
- humanoid
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31144v1.
sources:
- id: src_001
  type: paper
  title: A Modular Vision-Language-Action Robotics Framework for Indoor Environments
  url: https://arxiv.org/abs/2606.31144
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
This paper presents an integrated system for the CMU Vision-Language-Action (VLA) Challenge, designed to enable an autonomous agent to perform complex tasks based on natural language instructions. Our framework employs a modular architecture that orchestrates environment mapping, question processing, and navigation. The system operates in two parallel streams: a perception pipeline that constructs a semantic voxel map from real-time camera feeds using OwlViT embeddings, and a language pipeline that classifies user commands with a Vision-Language Model. The mapping is time-constrained; the system proceeds with a partial map if a 500-second exploration limit is reached. The classified query is then grounded in the geometric and semantic context of the map to generate a detailed prompt for the VLM. This yields an actionable output, demonstrating a capable solution for bridging the gap between human language and robotic action.

## 核心内容
This paper presents an integrated system for the CMU Vision-Language-Action (VLA) Challenge, designed to enable an autonomous agent to perform complex tasks based on natural language instructions. Our framework employs a modular architecture that orchestrates environment mapping, question processing, and navigation. The system operates in two parallel streams: a perception pipeline that constructs a semantic voxel map from real-time camera feeds using OwlViT embeddings, and a language pipeline that classifies user commands with a Vision-Language Model. The mapping is time-constrained; the system proceeds with a partial map if a 500-second exploration limit is reached. The classified query is then grounded in the geometric and semantic context of the map to generate a detailed prompt for the VLM. This yields an actionable output, demonstrating a capable solution for bridging the gap between human language and robotic action.

## 参考
- http://arxiv.org/abs/2606.31144v1

## Overview
This paper presents an integrated system for the CMU Vision-Language-Action (VLA) Challenge, designed to enable an autonomous agent to perform complex tasks based on natural language instructions. Our framework employs a modular architecture that orchestrates environment mapping, question processing, and navigation. The system operates in two parallel streams: a perception pipeline that constructs a semantic voxel map from real-time camera feeds using OwlViT embeddings, and a language pipeline that classifies user commands with a Vision-Language Model. The mapping is time-constrained; the system proceeds with a partial map if a 500-second exploration limit is reached. The classified query is then grounded in the geometric and semantic context of the map to generate a detailed prompt for the VLM. This yields an actionable output, demonstrating a capable solution for bridging the gap between human language and robotic action.

## Content
This paper presents an integrated system for the CMU Vision-Language-Action (VLA) Challenge, designed to enable an autonomous agent to perform complex tasks based on natural language instructions. Our framework employs a modular architecture that orchestrates environment mapping, question processing, and navigation. The system operates in two parallel streams: a perception pipeline that constructs a semantic voxel map from real-time camera feeds using OwlViT embeddings, and a language pipeline that classifies user commands with a Vision-Language Model. The mapping is time-constrained; the system proceeds with a partial map if a 500-second exploration limit is reached. The classified query is then grounded in the geometric and semantic context of the map to generate a detailed prompt for the VLM. This yields an actionable output, demonstrating a capable solution for bridging the gap between human language and robotic action.

## 개요
본 논문은 자연어 명령을 기반으로 자율 에이전트가 복잡한 작업을 수행할 수 있도록 설계된 CMU Vision-Language-Action (VLA) 챌린지를 위한 통합 시스템을 제시합니다. 우리의 프레임워크는 환경 매핑, 질문 처리 및 탐색을 조율하는 모듈식 아키텍처를 사용합니다. 시스템은 두 개의 병렬 스트림으로 작동합니다: OwlViT 임베딩을 사용하여 실시간 카메라 피드에서 의미론적 복셀 맵을 구축하는 인식 파이프라인과, Vision-Language Model을 사용하여 사용자 명령을 분류하는 언어 파이프라인입니다. 매핑에는 시간 제약이 있으며, 500초의 탐색 한계에 도달하면 시스템은 부분 맵으로 진행합니다. 분류된 쿼리는 맵의 기하학적 및 의미론적 맥락에 기반하여 VLM을 위한 상세한 프롬프트를 생성합니다. 이는 실행 가능한 출력을 생성하여 인간 언어와 로봇 동작 간의 격차를 해소하는 유능한 솔루션을 보여줍니다.

## 핵심 내용
본 논문은 자연어 명령을 기반으로 자율 에이전트가 복잡한 작업을 수행할 수 있도록 설계된 CMU Vision-Language-Action (VLA) 챌린지를 위한 통합 시스템을 제시합니다. 우리의 프레임워크는 환경 매핑, 질문 처리 및 탐색을 조율하는 모듈식 아키텍처를 사용합니다. 시스템은 두 개의 병렬 스트림으로 작동합니다: OwlViT 임베딩을 사용하여 실시간 카메라 피드에서 의미론적 복셀 맵을 구축하는 인식 파이프라인과, Vision-Language Model을 사용하여 사용자 명령을 분류하는 언어 파이프라인입니다. 매핑에는 시간 제약이 있으며, 500초의 탐색 한계에 도달하면 시스템은 부분 맵으로 진행합니다. 분류된 쿼리는 맵의 기하학적 및 의미론적 맥락에 기반하여 VLM을 위한 상세한 프롬프트를 생성합니다. 이는 실행 가능한 출력을 생성하여 인간 언어와 로봇 동작 간의 격차를 해소하는 유능한 솔루션을 보여줍니다.
