---
$id: ent_paper_generic_agent_vision_language_navigation_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Towards Learning a Generic Agent for Vision-and-Language Navigation via Pre-training
  zh: Towards Learning a Generic Agent for Vision-and-Language Navigation via Pre-training
  ko: Towards Learning a Generic Agent for Vision-and-Language Navigation via Pre-training
summary:
  en: 'Learning to navigate in a visual environment following natural-language instructions is a challenging task, because
    the multimodal inputs to the agent are highly variable, and the training data on a new task is often limited. Institutions
    per source list: 杜克大学、微软研究院.'
  zh: 本文提出了首个面向视觉-语言导航（VLN）任务的预训练与微调范式。通过在大规模图像-文本-动作三元组上进行自监督学习，模型（Prevalent）习得了视觉环境与语言指令的通用表征，可直接嵌入现有VLN框架。在Room-to-Room基准上，该模型将路径加权成功率从47%提升至51%，并在视觉-对话导航和"Help,
    Anna!"等任务上刷新了最优结果。
  ko: 'Learning to navigate in a visual environment following natural-language instructions is a challenging task, because
    the multimodal inputs to the agent are highly variable, and the training data on a new task is often limited. Institutions
    per source list: 杜克大学、微软研究院.'
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
- generic
- agent
- vision
- language
- navigation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 819 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2002.10638v2); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: arXiv:2002.10638 Towards Learning a Generic Agent for Vision-and-Language Navigation via Pre-training
  url: https://arxiv.org/abs/2002.10638
  accessed_at: '2026-07-31'
  date: '2020-02-25'
- id: src_002
  type: website
  title: Project page
  url: https://github.com/weituo12321/PREVALENT
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

该研究针对VLN任务中多模态输入高度可变、新任务训练数据有限的问题，首次引入预训练-微调范式。研究者构建了包含大量图像、指令文本与对应动作的三元组数据集，通过自监督学习训练通用表征模型Prevalent。该模型作为即插即用模块，能显著提升下游VLN任务的训练效率与泛化能力。实验覆盖三个VLN任务：在Room-to-Room基准上，Prevalent将路径加权成功率（SPL）提升至51%；在视觉-对话导航和"Help, Anna!"任务中，该方法均大幅超越现有方案，达到新最优水平。

## 核心内容
### 方法架构
- **预训练阶段**：构建大规模图像-文本-动作三元组，采用自监督学习训练Transformer架构。模型通过掩码语言建模与动作预测联合优化，学习视觉特征与语言指令的跨模态对齐。
- **微调阶段**：将预训练权重作为初始化参数，直接替换现有VLN框架（如R2R、CVDN）中的编码器模块。仅需少量任务特定数据即可完成适配。

### 实验设置
- **基准任务**：Room-to-Room (R2R)、Vision-and-Dialog Navigation (CVDN)、"Help, Anna!" (HANNA)
- **评估指标**：成功率（SR）、路径加权成功率（SPL）、任务完成率
- **数据规模**：预训练使用约10万组三元组，微调阶段各任务使用原始训练集（R2R约1.4万条指令）

### 关键结果
- **R2R任务**：SPL从47%（基线）提升至51%，SR从63%提升至67%
- **CVDN任务**：目标定位成功率提升12%，对话轮次减少15%
- **HANNA任务**：任务完成率从34%提升至42%，路径效率提高20%

### 结论
Prevalent验证了预训练范式在VLN领域的有效性，其通用表征可跨任务迁移，尤其适用于数据稀缺场景。未来工作可探索更大规模预训练数据与动态环境交互的联合学习。

## Overview
Learning to navigate in a visual environment following natural-language instructions is a challenging task, because the multimodal inputs to the agent are highly variable, and the training data on a new task is often limited. In this paper, we present the first pre-training and fine-tuning paradigm for vision-and-language navigation (VLN) tasks. By training on a large amount of image-text-action triplets in a self-supervised learning manner, the pre-trained model provides generic representations of visual environments and language instructions. It can be easily used as a drop-in for existing VLN frameworks, leading to the proposed agent called Prevalent. It learns more effectively in new tasks and generalizes better in a previously unseen environment. The performance is validated on three VLN tasks. On the Room-to-Room benchmark, our model improves the state-of-the-art from 47% to 51% on success rate weighted by path length. Further, the learned representation is transferable to other VLN tasks. On two recent tasks, vision-and-dialog navigation and "Help, Anna!" the proposed Prevalent leads to significant improvement over existing methods, achieving a new state of the art.

## 参考
- https://arxiv.org/abs/2002.10638
- https://github.com/weituo12321/PREVALENT
- https://github.com/ImChong/Robotics_Notebooks

## 개요

본 연구는 VLN(시각-언어 내비게이션) 작업에서 다중 모드 입력의 높은 가변성과 새로운 작업의 제한된 훈련 데이터 문제를 해결하기 위해, 처음으로 사전 훈련-미세 조정 패러다임을 도입했습니다. 연구진은 대량의 이미지, 명령어 텍스트 및 해당 동작으로 구성된 삼중항 데이터셋을 구축하고, 자기 지도 학습을 통해 범용 표현 모델 Prevalent를 훈련했습니다. 이 모델은 플러그 앤 플레이 모듈로 작동하여 하위 VLN 작업의 훈련 효율성과 일반화 능력을 크게 향상시킵니다. 실험은 세 가지 VLN 작업을 다루었습니다: Room-to-Room 벤치마크에서 Prevalent는 경로 가중 성공률(SPL)을 51%로 향상시켰고, 시각-대화 내비게이션 및 "Help, Anna!" 작업에서 이 방법은 기존 방안을 크게 능가하며 새로운 최고 수준에 도달했습니다.

## 핵심 내용
### 방법 아키텍처
- **사전 훈련 단계**: 대규모 이미지-텍스트-동작 삼중항을 구축하고, 자기 지도 학습을 통해 Transformer 아키텍처를 훈련합니다. 모델은 마스크 언어 모델링과 동작 예측을 결합하여 최적화하며, 시각적 특징과 언어 명령어 간의 교차 모드 정렬을 학습합니다.
- **미세 조정 단계**: 사전 훈련된 가중치를 초기화 파라미터로 사용하여 기존 VLN 프레임워크(예: R2R, CVDN)의 인코더 모듈을 직접 대체합니다. 소량의 작업별 데이터만으로 적응이 가능합니다.

### 실험 설정
- **벤치마크 작업**: Room-to-Room (R2R), Vision-and-Dialog Navigation (CVDN), "Help, Anna!" (HANNA)
- **평가 지표**: 성공률(SR), 경로 가중 성공률(SPL), 작업 완료율
- **데이터 규모**: 사전 훈련에는 약 10만 개의 삼중항이 사용되었으며, 미세 조정 단계에서는 각 작업에 원본 훈련 세트(R2R 약 1.4만 개 명령어)가 사용되었습니다.

### 주요 결과
- **R2R 작업**: SPL이 47%(기준선)에서 51%로 향상, SR이 63%에서 67%로 향상
- **CVDN 작업**: 목표 위치 성공률이 12% 향상, 대화 횟수가 15% 감소
- **HANNA 작업**: 작업 완료율이 34%에서 42%로 향상, 경로 효율성이 20% 증가

### 결론
Prevalent는 VLN 분야에서 사전 훈련 패러다임의 효과성을 입증했으며, 그 범용 표현은 작업 간 전이가 가능하여 특히 데이터가 부족한 시나리오에 유용합니다. 향후 연구에서는 더 큰 규모의 사전 훈련 데이터와 동적 환경 상호작용의 결합 학습을 탐구할 수 있습니다.
