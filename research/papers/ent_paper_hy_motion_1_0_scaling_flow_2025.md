---
$id: ent_paper_hy_motion_1_0_scaling_flow_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HY-Motion 1.0: Scaling Flow Matching Models for Text-To-Motion Generation'
  zh: 'HY-Motion 1.0: Scaling Flow Matching Models for Text-To-Motion Generation'
  ko: 'HY-Motion 1.0: Scaling Flow Matching Models for Text-To-Motion Generation'
summary:
  en: We present HY-Motion 1.0, a series of state-of-the-art, large-scale, motion generation models capable of generating
    3D human motions from textual descriptions.
  zh: HY-Motion 1.0 是一系列基于 Diffusion Transformer (DiT) 的流匹配模型，首次将文本到3D人体运动生成模型扩展至十亿参数规模。该模型通过全阶段训练范式（包括3000小时大规模预训练、400小时高质量微调及强化学习）实现指令跟随能力，覆盖6大类200余种运动类别，显著超越现有开源基准。
  ko: We present HY-Motion 1.0, a series of state-of-the-art, large-scale, motion generation models capable of generating
    3D human motions from textual descriptions.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- hy
- motion
- '1'
- '0'
- scaling
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Full ingest from Yuanxq lab paper list row 677 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2512.23464 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2512.23464v1); zh content by DeepSeek from the abstract. Institutions unknown (not in source list).'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2512.23464 HY-Motion 1.0: Scaling Flow Matching Models for Text-To-Motion Generation'
  url: https://arxiv.org/abs/2512.23464
  accessed_at: '2026-07-31'
  date: '2025-12-29'
- id: src_002
  type: website
  title: Project page
  url: https://github.com/Tencent-Hunyuan/HY-Motion-1.0
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

HY-Motion 1.0 由研究团队提出，采用 DiT 架构的流匹配方法，通过参数规模化突破运动生成领域瓶颈。其核心创新在于全阶段训练流程：首先在3000小时运动数据上预训练，随后用400小时精选数据微调，最后结合人类反馈与奖励模型进行强化学习。该模型通过严格的数据清洗与标注流程，最终覆盖200余种运动类别，在指令对齐与运动质量上达到新高度。

## 核心内容
### 方法架构
- 基于 Diffusion Transformer (DiT) 的流匹配模型，首次将参数规模扩展至十亿级别
- 采用全阶段训练范式：
  - **大规模预训练**：在3000小时运动数据上学习基础运动模式
  - **高质量微调**：使用400小时精选数据优化运动细节
  - **强化学习**：结合人类反馈与奖励模型，提升指令对齐精度

### 数据处理
- 构建严格的数据清洗与标注流程，确保运动数据质量
- 最终覆盖6大类运动（如行走、跳跃、舞蹈等），包含200余种具体类别

### 实验设置与结果
- 在公开基准测试中，指令跟随能力显著超越现有开源模型
- 运动生成质量（如平滑度、自然度）达到行业领先水平
- 模型已开源，旨在推动3D人体运动生成技术向商业成熟度过渡

### 结论
HY-Motion 1.0 验证了 DiT 流匹配模型在运动生成领域的规模化可行性，其全阶段训练范式为后续研究提供了可复现的框架。

## Overview
We present HY-Motion 1.0, a series of state-of-the-art, large-scale, motion generation models capable of generating 3D human motions from textual descriptions. HY-Motion 1.0 represents the first successful attempt to scale up Diffusion Transformer (DiT)-based flow matching models to the billion-parameter scale within the motion generation domain, delivering instruction-following capabilities that significantly outperform current open-source benchmarks. Uniquely, we introduce a comprehensive, full-stage training paradigm -- including large-scale pretraining on over 3,000 hours of motion data, high-quality fine-tuning on 400 hours of curated data, and reinforcement learning from both human feedback and reward models -- to ensure precise alignment with the text instruction and high motion quality. This framework is supported by our meticulous data processing pipeline, which performs rigorous motion cleaning and captioning. Consequently, our model achieves the most extensive coverage, spanning over 200 motion categories across 6 major classes. We release HY-Motion 1.0 to the open-source community to foster future research and accelerate the transition of 3D human motion generation models towards commercial maturity.

## 参考
- https://arxiv.org/abs/2512.23464
- https://github.com/Tencent-Hunyuan/HY-Motion-1.0
- https://github.com/ImChong/Robotics_Notebooks

## 개요

HY-Motion 1.0은 연구팀이 제안한 모델로, DiT 아키텍처의 흐름 매칭 방법을 사용하여 매개변수 규모 확장을 통해 운동 생성 분야의 병목 현상을 돌파했습니다. 핵심 혁신은 전 단계 훈련 프로세스에 있습니다: 먼저 3000시간의 운동 데이터로 사전 훈련을 진행하고, 이후 400시간의 정제된 데이터로 미세 조정을 수행하며, 마지막으로 인간 피드백과 보상 모델을 결합한 강화 학습을 적용합니다. 이 모델은 엄격한 데이터 정제 및 레이블링 프로세스를 통해 최종적으로 200여 가지 운동 범주를 포괄하며, 명령 정렬과 운동 품질에서 새로운 수준에 도달했습니다.

## 핵심 내용
### 방법 아키텍처
- Diffusion Transformer (DiT) 기반의 흐름 매칭 모델로, 처음으로 매개변수 규모를 10억 단위로 확장
- 전 단계 훈련 패러다임 채택:
  - **대규모 사전 훈련**: 3000시간의 운동 데이터에서 기본 운동 패턴 학습
  - **고품질 미세 조정**: 400시간의 정제된 데이터로 운동 세부 사항 최적화
  - **강화 학습**: 인간 피드백과 보상 모델을 결합하여 명령 정렬 정밀도 향상

### 데이터 처리
- 엄격한 데이터 정제 및 레이블링 프로세스를 구축하여 운동 데이터 품질 보장
- 최종적으로 6대 운동 범주(예: 걷기, 점프, 춤 등)를 포괄하며, 200여 가지 구체적인 범주 포함

### 실험 설정 및 결과
- 공개 벤치마크 테스트에서 명령 추종 능력이 기존 오픈소스 모델을 크게 능가
- 운동 생성 품질(예: 부드러움, 자연스러움)이 업계 선도 수준에 도달
- 모델은 오픈소스로 제공되며, 3D 인간 운동 생성 기술의 상업적 성숙도 전환을 촉진하는 것을 목표로 함

### 결론
HY-Motion 1.0은 DiT 흐름 매칭 모델의 운동 생성 분야에서의 규모화 가능성을 검증했으며, 전 단계 훈련 패러다임은 후속 연구에 재현 가능한 프레임워크를 제공합니다.
