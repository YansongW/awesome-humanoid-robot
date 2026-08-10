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
  zh: 本文提出一种面向CMU VLA挑战赛的模块化机器人框架，用于在室内环境中根据自然语言指令执行复杂任务。系统通过并行感知与语言管道，结合OwlViT语义地图构建和VLM指令分类，在500秒探索时限内生成可执行动作，实现了语言到机器人动作的端到端衔接。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31144v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (601 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: A Modular Vision-Language-Action Robotics Framework for Indoor Environments
  url: https://arxiv.org/abs/2606.31144
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
该框架采用模块化架构，将环境建图、指令处理和导航功能有机整合。系统包含两条并行处理流：感知流利用OwlViT嵌入从实时摄像头数据构建语义体素地图，语言流则通过Vision-Language Model对用户指令进行分类。建图过程受时间约束，若达到500秒探索上限则使用部分地图继续执行。分类后的查询指令被映射到地图的几何与语义上下文中，生成详细提示输入VLM，最终输出可执行动作指令。

## 核心内容
### 系统架构
- 采用模块化设计，集成环境建图、指令处理与导航三大模块
- 双并行处理流：感知流与语言流同步运行

### 感知管道
- 使用OwlViT嵌入从实时摄像头流构建语义体素地图
- 建图受500秒时间约束，超时后使用部分地图继续执行

### 语言管道
- 通过Vision-Language Model对用户自然语言指令进行分类
- 分类后的查询与地图的几何及语义上下文进行关联

### 动作生成
- 将关联后的查询生成详细提示输入VLM
- VLM输出可执行的动作指令，实现语言到机器人动作的转换

### 实验设置
- 系统在CMU VLA挑战赛环境中进行测试
- 关键参数：500秒探索时间限制、OwlViT嵌入、VLM分类模型

### 结论
该框架成功展示了模块化架构在连接人类语言与机器人动作方面的有效性，为室内环境中的自主机器人任务执行提供了可行方案。

## Overview
This paper presents an integrated system for the CMU Vision-Language-Action (VLA) Challenge, designed to enable an autonomous agent to perform complex tasks based on natural language instructions. Our framework employs a modular architecture that orchestrates environment mapping, question processing, and navigation. The system operates in two parallel streams: a perception pipeline that constructs a semantic voxel map from real-time camera feeds using OwlViT embeddings, and a language pipeline that classifies user commands with a Vision-Language Model. The mapping is time-constrained; the system proceeds with a partial map if a 500-second exploration limit is reached. The classified query is then grounded in the geometric and semantic context of the map to generate a detailed prompt for the VLM. This yields an actionable output, demonstrating a capable solution for bridging the gap between human language and robotic action.

## 参考
- http://arxiv.org/abs/2606.31144v1

## 개요
이 프레임워크는 모듈식 아키텍처를 채택하여 환경 매핑, 명령 처리 및 내비게이션 기능을 유기적으로 통합합니다. 시스템은 두 개의 병렬 처리 흐름을 포함합니다: 인식 흐름은 OwlViT 임베딩을 사용하여 실시간 카메라 데이터에서 의미론적 복셀 맵을 구축하고, 언어 흐름은 Vision-Language Model을 통해 사용자 명령을 분류합니다. 매핑 과정은 시간 제약을 받으며, 500초 탐색 상한에 도달하면 부분 맵을 사용하여 계속 실행합니다. 분류된 쿼리 명령은 맵의 기하학적 및 의미론적 컨텍스트에 매핑되어 상세 프롬프트를 생성하고 VLM에 입력하며, 최종적으로 실행 가능한 동작 명령을 출력합니다.

## 핵심 내용
### 시스템 아키텍처
- 모듈식 설계를 채택하여 환경 매핑, 명령 처리 및 내비게이션의 세 가지 모듈을 통합
- 이중 병렬 처리 흐름: 인식 흐름과 언어 흐름이 동시에 실행

### 인식 파이프라인
- OwlViT 임베딩을 사용하여 실시간 카메라 스트림에서 의미론적 복셀 맵 구축
- 매핑은 500초 시간 제약을 받으며, 시간 초과 시 부분 맵을 사용하여 계속 실행

### 언어 파이프라인
- Vision-Language Model을 통해 사용자 자연어 명령을 분류
- 분류된 쿼리는 맵의 기하학적 및 의미론적 컨텍스트와 연관

### 동작 생성
- 연관된 쿼리를 사용하여 상세 프롬프트를 생성하고 VLM에 입력
- VLM은 실행 가능한 동작 명령을 출력하여 언어에서 로봇 동작으로의 변환을 실현

### 실험 설정
- 시스템은 CMU VLA 챌린지 환경에서 테스트됨
- 주요 매개변수: 500초 탐색 시간 제한, OwlViT 임베딩, VLM 분류 모델

### 결론
이 프레임워크는 인간 언어와 로봇 동작을 연결하는 데 있어 모듈식 아키텍처의 효과성을 성공적으로 입증했으며, 실내 환경에서의 자율 로봇 작업 실행을 위한 실현 가능한 솔루션을 제공합니다.
