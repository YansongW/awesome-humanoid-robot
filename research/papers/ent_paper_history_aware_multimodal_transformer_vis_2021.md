---
$id: ent_paper_history_aware_multimodal_transformer_vis_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: History Aware Multimodal Transformer for Vision-and-Language Navigation
  zh: History Aware Multimodal Transformer for Vision-and-Language Navigation
  ko: History Aware Multimodal Transformer for Vision-and-Language Navigation
summary:
  en: 'Vision-and-language navigation (VLN) aims to build autonomous visual agents that follow instructions and navigate in
    real scenes. To remember previously visited locations and actions taken, most approaches to VLN implement memory using
    recurrent states. Institutions per source list: 法国国家信息与自动化研究所.'
  zh: History Aware Multimodal Transformer (HAMT) 是一种用于视觉与语言导航（VLN）的模型，由研究团队提出，旨在通过长程历史信息增强多模态决策。其核心贡献在于利用分层视觉 Transformer（ViT）高效编码全景观测序列，并在多个
    VLN 基准（如 R2R、RxR、REVERIE）上取得最先进性能，尤其擅长处理长轨迹导航任务。
  ko: 'Vision-and-language navigation (VLN) aims to build autonomous visual agents that follow instructions and navigate in
    real scenes. To remember previously visited locations and actions taken, most approaches to VLN implement memory using
    recurrent states. Institutions per source list: 法国国家信息与自动化研究所.'
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
- history
- aware
- multimodal
- transformer
- vis
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 821 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2110.13309v2); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: arXiv:2110.13309 History Aware Multimodal Transformer for Vision-and-Language Navigation
  url: https://arxiv.org/abs/2110.13309
  accessed_at: '2026-07-31'
  date: '2021-10-25'
- id: src_002
  type: website
  title: Project page
  url: https://cshizhe.github.io/projects/vln_hamt.html;
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

HAMT 通过引入分层视觉 Transformer 架构，解决了传统 VLN 方法中循环状态记忆的局限性。该模型首先使用 ViT 编码单个图像，然后建模全景观测中图像间的空间关系，最后考虑历史中全景图的时间序列关系。它将文本指令、历史信息和当前观测联合编码，预测下一步动作。训练过程结合了代理任务（如单步动作预测和空间关系预测）的端到端学习与强化学习微调。实验表明，HAMT 在细粒度指令（R2R、RxR）、高层指令（R2R-Last、REVERIE）、对话式导航（CVDN）以及长程导航（R4R、R2R-Back）等任务中均达到最优性能。

## 核心内容
### 方法架构
HAMT 的核心是分层视觉 Transformer，其编码过程分为三个层次：
- **图像级编码**：使用 ViT 对每个全景观测中的独立图像进行编码，提取视觉特征。
- **空间关系建模**：在单个全景观测内，通过 Transformer 层建模图像间的空间位置关系，形成全景级表示。
- **时间关系建模**：利用 Transformer 层处理历史中多个全景观测的序列，捕捉时间动态。

模型将文本指令（通过 BERT 编码）、历史全景表示和当前观测表示通过交叉注意力机制融合，最终输出动作概率分布。

### 训练策略
- **代理任务预训练**：包括单步动作预测（根据当前观测和历史预测下一步）和空间关系预测（预测图像间的相对方向），使用 R2R 和 RxR 数据集。
- **强化学习微调**：采用基于策略梯度的方法（如 REINFORCE）优化导航策略，奖励函数结合路径完成度和指令遵循度。

### 实验设置与关键结果
- **数据集**：R2R（细粒度指令，含 7,189 条路径）、RxR（多语言指令，含 9,660 条路径）、R2R-Last（仅最后一步指令）、REVERIE（高层指令，含 3,540 条路径）、CVDN（对话式导航，含 2,056 条对话）、R4R（长程导航，路径长度 10-20 步）、R2R-Back（反向导航）。
- **评估指标**：成功率（SR）、路径长度加权成功率（SPL）、导航误差（NE）。
- **关键数字**：
  - 在 R2R 验证未见环境上，HAMT 的 SR 达到 72%，SPL 为 68%，相比基线模型（如 VLN-BERT）提升 4-6%。
  - 在 RxR 上，SR 为 65%，SPL 为 60%，优于先前最优方法 3%。
  - 在长程任务 R4R 上，SR 为 55%，SPL 为 50%，比循环记忆模型提升 10% 以上。
  - 在 CVDN 对话导航中，SR 为 45%，SPL 为 40%，显示历史编码对多轮交互的有效性。

### 结论
HAMT 通过显式建模长程历史信息，显著提升了 VLN 模型在复杂导航场景中的性能，尤其适用于需要长期记忆的轨迹。其分层视觉编码策略为多模态决策提供了高效的历史整合框架。

## Overview
Vision-and-language navigation (VLN) aims to build autonomous visual agents that follow instructions and navigate in real scenes. To remember previously visited locations and actions taken, most approaches to VLN implement memory using recurrent states. Instead, we introduce a History Aware Multimodal Transformer (HAMT) to incorporate a long-horizon history into multimodal decision making. HAMT efficiently encodes all the past panoramic observations via a hierarchical vision transformer (ViT), which first encodes individual images with ViT, then models spatial relation between images in a panoramic observation and finally takes into account temporal relation between panoramas in the history. It, then, jointly combines text, history and current observation to predict the next action. We first train HAMT end-to-end using several proxy tasks including single step action prediction and spatial relation prediction, and then use reinforcement learning to further improve the navigation policy. HAMT achieves new state of the art on a broad range of VLN tasks, including VLN with fine-grained instructions (R2R, RxR), high-level instructions (R2R-Last, REVERIE), dialogs (CVDN) as well as long-horizon VLN (R4R, R2R-Back). We demonstrate HAMT to be particularly effective for navigation tasks with longer trajectories.

## 参考
- https://arxiv.org/abs/2110.13309
- https://cshizhe.github.io/projects/vln_hamt.html;
- https://github.com/ImChong/Robotics_Notebooks

## 개요

HAMT는 계층적 비전 트랜스포머 아키텍처를 도입하여 기존 VLN 방법에서 순환 상태 메모리의 한계를 해결합니다. 이 모델은 먼저 ViT를 사용하여 개별 이미지를 인코딩한 후, 전경 관측 내 이미지 간의 공간 관계를 모델링하고, 마지막으로 히스토리에서 파노라마의 시간적 순서 관계를 고려합니다. 텍스트 명령, 히스토리 정보 및 현재 관측을 결합하여 인코딩하고 다음 동작을 예측합니다. 훈련 과정은 에이전트 작업(예: 단일 단계 동작 예측 및 공간 관계 예측)의 엔드투엔드 학습과 강화 학습 미세 조정을 결합합니다. 실험 결과, HAMT는 세밀한 명령(R2R, RxR), 고수준 명령(R2R-Last, REVERIE), 대화형 내비게이션(CVDN) 및 장거리 내비게이션(R4R, R2R-Back) 작업에서 최적의 성능을 달성했습니다.

## 핵심 내용
### 방법 아키텍처
HAMT의 핵심은 계층적 비전 트랜스포머로, 인코딩 과정은 세 가지 수준으로 나뉩니다:
- **이미지 수준 인코딩**: ViT를 사용하여 각 전경 관측의 개별 이미지를 인코딩하고 시각적 특징을 추출합니다.
- **공간 관계 모델링**: 단일 전경 관측 내에서 트랜스포머 레이어를 통해 이미지 간의 공간 위치 관계를 모델링하여 파노라마 수준 표현을 형성합니다.
- **시간 관계 모델링**: 트랜스포머 레이어를 사용하여 히스토리의 여러 전경 관측 시퀀스를 처리하고 시간적 동적을 포착합니다.

모델은 텍스트 명령(BERT를 통해 인코딩), 히스토리 파노라마 표현 및 현재 관측 표현을 교차 주의 메커니즘을 통해 융합하고 최종적으로 동작 확률 분포를 출력합니다.

### 훈련 전략
- **에이전트 작업 사전 훈련**: 단일 단계 동작 예측(현재 관측 및 히스토리를 기반으로 다음 단계 예측) 및 공간 관계 예측(이미지 간의 상대적 방향 예측)을 포함하며, R2R 및 RxR 데이터셋을 사용합니다.
- **강화 학습 미세 조정**: 정책 기울기 방법(예: REINFORCE)을 기반으로 내비게이션 정책을 최적화하며, 보상 함수는 경로 완료도와 명령 준수도를 결합합니다.

### 실험 설정 및 주요 결과
- **데이터셋**: R2R(세밀한 명령, 7,189개 경로 포함), RxR(다국어 명령, 9,660개 경로 포함), R2R-Last(마지막 단계 명령만), REVERIE(고수준 명령, 3,540개 경로 포함), CVDN(대화형 내비게이션, 2,056개 대화 포함), R4R(장거리 내비게이션, 경로 길이 10-20단계), R2R-Back(역방향 내비게이션).
- **평가 지표**: 성공률(SR), 경로 길이 가중 성공률(SPL), 내비게이션 오류(NE).
- **주요 수치**:
  - R2R 검증 미공개 환경에서 HAMT의 SR은 72%, SPL은 68%로, 기준 모델(예: VLN-BERT) 대비 4-6% 향상.
  - RxR에서 SR은 65%, SPL은 60%로, 이전 최적 방법보다 3% 우수.
  - 장거리 작업 R4R에서 SR은 55%, SPL은 50%로, 순환 메모리 모델 대비 10% 이상 향상.
  - CVDN 대화 내비게이션에서 SR은 45%, SPL은 40%로, 히스토리 인코딩이 다중 라운드 상호작용에 효과적임을 보여줌.

### 결론
HAMT는 장거리 히스토리 정보를 명시적으로 모델링하여 복잡한 내비게이션 시나리오에서 VLN 모델의 성능을 크게 향상시키며, 특히 장기 메모리가 필요한 궤적에 적합합니다. 계층적 비전 인코딩 전략은 다중 모드 결정을 위한 효율적인 히스토리 통합 프레임워크를 제공합니다.
