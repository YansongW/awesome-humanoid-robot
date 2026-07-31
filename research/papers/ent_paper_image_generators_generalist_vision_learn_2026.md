---
$id: ent_paper_image_generators_generalist_vision_learn_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Image Generators are Generalist Vision Learners
  zh: Image Generators are Generalist Vision Learners
  ko: Image Generators are Generalist Vision Learners
summary:
  en: 'Recent works show that image and video generators exhibit zero-shot visual understanding behaviors, in a way reminiscent
    of how LLMs develop emergent capabilities of language understanding and reasoning from generative pretraining. Institutions
    per source list: Google DeepMind.'
  zh: 本文提出Vision Banana，一个基于Nano Banana Pro (NBP)模型通过指令微调构建的通用视觉模型。核心贡献在于证明图像生成训练能像LLM预训练一样学习通用视觉表征，并通过将视觉任务输出参数化为RGB图像，实现零样本SOTA性能，在2D/3D理解任务上超越Segment
    Anything Model 3和Depth Anything系列等专业模型。
  ko: 'Recent works show that image and video generators exhibit zero-shot visual understanding behaviors, in a way reminiscent
    of how LLMs develop emergent capabilities of language understanding and reasoning from generative pretraining. Institutions
    per source list: Google DeepMind.'
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
- image
- generators
- generalist
- vision
- learn
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 813 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2604.20329v3); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: arXiv:2604.20329 Image Generators are Generalist Vision Learners
  url: https://arxiv.org/abs/2604.20329
  accessed_at: '2026-07-31'
  date: '2026-04-22'
- id: src_002
  type: website
  title: Project page
  url: http://vision-banana.github.io
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

本研究揭示图像生成训练具备类似大语言模型预训练的能力，使模型学习到强大的通用视觉表征。作者通过将视觉任务输出空间参数化为RGB图像，将感知任务重新定义为图像生成问题，构建了通用模型Vision Banana。该模型在轻量级指令微调后，无需牺牲原有图像生成能力，即在分割、深度估计等2D/3D理解任务上达到SOTA水平。实验表明，图像生成可作为视觉任务的统一接口，预示着计算机视觉领域可能迎来以生成式预训练为核心的范式转变。

## 核心内容
### 核心方法
- 基于Nano Banana Pro (NBP)模型，在其原始训练数据与少量视觉任务数据混合集上进行指令微调
- 创新性地将视觉任务输出（如分割掩码、深度图）编码为RGB图像格式，使模型通过图像生成统一处理各类感知任务

### 实验设置
- 训练数据：保留NBP原有图像生成数据，仅添加少量标注的视觉任务样本
- 评估任务：涵盖2D分割（SAM 3基准）、3D度量深度估计（Depth Anything系列基准）等

### 关键结果
- 在分割任务上零样本超越Segment Anything Model 3
- 在度量深度估计任务上击败Depth Anything系列专业模型
- 轻量级指令微调后，模型原始图像生成能力未受影响
- 验证图像生成预训练可作为通用视觉学习器，其统一接口效果类比文本生成在语言理解中的作用

### 结论
- 图像生成训练能学习到与LLM预训练等效的通用视觉表征
- 视觉任务可被统一重构为图像生成问题，无需任务特定架构
- 该工作预示计算机视觉可能转向以生成式预训练为核心的基础模型构建范式

## Overview
Recent works show that image and video generators exhibit zero-shot visual understanding behaviors, in a way reminiscent of how LLMs develop emergent capabilities of language understanding and reasoning from generative pretraining. While it has long been conjectured that the ability to create visual content implies an ability to understand it, there has been limited evidence that generative vision models have developed strong understanding capabilities. In this work, we demonstrate that image generation training serves a role similar to LLM pretraining, and lets models learn powerful and general visual representations that enable SOTA performance on various vision tasks. We introduce Vision Banana, a generalist model built by instruction-tuning Nano Banana Pro (NBP) on a mixture of its original training data alongside a small amount of vision task data. By parameterizing the output space of vision tasks as RGB images, we seamlessly reframe perception as image generation. Our generalist model, Vision Banana, achieves SOTA results on a variety of vision tasks involving both 2D and 3D understanding, beating or rivaling zero-shot domain-specialists, including Segment Anything Model 3 on segmentation tasks, and the Depth Anything series on metric depth estimation. We show that these results can be achieved with lightweight instruction-tuning without sacrificing the base model's image generation capabilities. The superior results suggest that image generation pretraining is a generalist vision learner. It also shows that image generation serves as a unified and universal interface for vision tasks, similar to text generation's role in language understanding and reasoning. We could be witnessing a major paradigm shift for computer vision, where generative vision pretraining takes a central role in building Foundational Vision Models for both generation and understanding.

## 参考
- https://arxiv.org/abs/2604.20329
- http://vision-banana.github.io
- https://github.com/ImChong/Robotics_Notebooks

## 개요

본 연구는 이미지 생성 훈련이 대규모 언어 모델 사전 훈련과 유사한 능력을 지니며, 모델이 강력한 범용 시각 표현을 학습할 수 있음을 밝혀냅니다. 저자는 시각 작업의 출력 공간을 RGB 이미지로 매개변수화하여 인식 작업을 이미지 생성 문제로 재정의하고, 범용 모델 Vision Banana를 구축했습니다. 이 모델은 경량 명령어 미세 조정 후, 기존 이미지 생성 능력을 희생하지 않으면서 분할, 깊이 추정 등 2D/3D 이해 작업에서 SOTA 수준에 도달했습니다. 실험 결과, 이미지 생성이 시각 작업의 통합 인터페이스로 작용할 수 있음을 보여주며, 컴퓨터 비전 분야에서 생성적 사전 훈련을 핵심으로 하는 패러다임 전환이 도래할 수 있음을 시사합니다.

## 핵심 내용
### 핵심 방법
- Nano Banana Pro (NBP) 모델을 기반으로, 원본 훈련 데이터와 소량의 시각 작업 데이터 혼합 세트에서 명령어 미세 조정 수행
- 분할 마스크, 깊이 맵 등 시각 작업 출력을 RGB 이미지 형식으로 인코딩하는 혁신적 방법을 통해, 모델이 이미지 생성을 통해 다양한 인식 작업을 통합 처리

### 실험 설정
- 훈련 데이터: NBP의 기존 이미지 생성 데이터를 유지하고, 소량의 레이블링된 시각 작업 샘플만 추가
- 평가 작업: 2D 분할(SAM 3 벤치마크), 3D 메트릭 깊이 추정(Depth Anything 시리즈 벤치마크) 등 포함

### 주요 결과
- 분할 작업에서 Segment Anything Model 3를 제로샷으로 능가
- 메트릭 깊이 추정 작업에서 Depth Anything 시리즈 전문 모델을 압도
- 경량 명령어 미세 조정 후, 모델의 원본 이미지 생성 능력에 영향 없음
- 이미지 생성 사전 훈련이 범용 시각 학습기로 작용할 수 있음을 검증, 그 통합 인터페이스 효과는 텍스트 생성이 언어 이해에서 가지는 역할과 유사

### 결론
- 이미지 생성 훈련은 LLM 사전 훈련과 동등한 범용 시각 표현을 학습 가능
- 시각 작업은 작업별 아키텍처 없이 이미지 생성 문제로 통합 재구성 가능
- 본 연구는 컴퓨터 비전이 생성적 사전 훈련을 핵심으로 하는 기초 모델 구축 패러다임으로 전환될 수 있음을 시사
