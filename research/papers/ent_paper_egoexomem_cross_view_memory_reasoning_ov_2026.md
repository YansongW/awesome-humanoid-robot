---
$id: ent_paper_egoexomem_cross_view_memory_reasoning_ov_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EgoExoMem: Cross-View Memory Reasoning over Synchronized Egocentric and Exocentric Videos'
  zh: 'EgoExoMem: Cross-View Memory Reasoning over Synchronized Egocentric and Exocentric Videos'
  ko: 'EgoExoMem: Cross-View Memory Reasoning over Synchronized Egocentric and Exocentric Videos'
summary:
  en: 'Egocentric memory is widely used in embodied intelligence, but it may be insufficient for comprehensive spatial-temporal
    reasoning. Inspired by human recall from both field and observer perspectives, we introduce EgoExoMem, the first benchmark
    for cross-view memory reasoning over synchronized egocentric and exocentric videos. Institutions per source list: KIT、ETH
    Zurich、Oxford、湖南大学、INSAIT.'
  zh: EgoExoMem 是首个针对同步第一人称与第三人称视频的跨视角记忆推理基准，由研究团队提出。该基准包含 2.6K 道高质量选择题，覆盖时间、空间与跨视角三类问答类型。同时提出无需训练的 E²-Select 帧选择方法，在现有 MLLM
    上最高准确率仅 55.3%，而 E²-Select 达到 58.2% 的领先性能。
  ko: 'Egocentric memory is widely used in embodied intelligence, but it may be insufficient for comprehensive spatial-temporal
    reasoning. Inspired by human recall from both field and observer perspectives, we introduce EgoExoMem, the first benchmark
    for cross-view memory reasoning over synchronized egocentric and exocentric videos. Institutions per source list: KIT、ETH
    Zurich、Oxford、湖南大学、INSAIT.'
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
- egoexomem
- cross
- view
- memory
- reasoning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 280 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2605.18734v2); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2605.18734 EgoExoMem: Cross-View Memory Reasoning over Synchronized Egocentric and Exocentric Videos'
  url: https://arxiv.org/abs/2605.18734
  accessed_at: '2026-07-31'
  date: '2026-05-18'
- id: src_002
  type: website
  title: Project page
  url: https://github.com/RuipingL/EgoExoMem
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: 机器人下一代数据入口，可能就是Ego：9篇论文讲透第一视角技术路线
  url: https://mp.weixin.qq.com/s/4JQ1xa-cJ7J1ep_e4txNnA
  accessed_at: '2026-07-31'
---

## 概述

EgoExoMem 基准旨在解决具身智能中仅依赖第一人称记忆进行时空推理的局限性，灵感来源于人类同时从场内与场外视角回忆信息的能力。该基准包含 2.6K 道高质量选择题，涵盖时间、空间与跨视角三类问答类型，并同步提供第一人称与第三人称视频。为支持双视角检索，研究团队提出 E²-Select 方法，这是一种无需训练的帧选择技术，通过基于相关性的预算分配与每视角 k-DPP 采样，处理视角不对称性与跨视角时间一致性。实验表明，第一人称与第三人称视角提供互补的记忆线索，但现有多模态大语言模型（MLLM）在该基准上表现不佳，最佳模型仅达 55.3%。E²-Select 在帧选择与基于 RAG 的记忆基线中取得 58.2% 的最优性能。进一步分析揭示了问题框架与答案定位之间的系统性视角偏好冲突，凸显了跨视角记忆推理的新颖性与挑战性。

## 核心内容
### 方法
- **EgoExoMem 基准**：基于同步的第一人称（egocentric）与第三人称（exocentric）视频构建，包含 2.6K 道高质量选择题，分为八种类型：时间推理（如事件顺序）、空间推理（如物体位置）与跨视角推理（如视角转换）。
- **E²-Select 帧选择方法**：无需训练，通过两步实现双视角帧选择：
  - **基于相关性的预算分配**：根据每个视角与查询的相关性，动态分配帧选择预算，处理视角不对称性（如第一人称视角更关注手部动作，第三人称视角更关注全局场景）。
  - **每视角 k-DPP 采样**：在每个视角内使用 k-DPP（k-Determinantal Point Process）采样，确保所选帧的多样性与跨视角时间一致性。

### 实验设置
- **基线模型**：包括多种 MLLM（如 GPT-4V、LLaVA-NeXT）以及基于帧选择与 RAG（检索增强生成）的记忆方法。
- **评估指标**：准确率（Accuracy），在 2.6K 道选择题上计算。

### 关键数字
- **最佳 MLLM 性能**：GPT-4V 达到 55.3%，远低于人类水平（未报告具体数字，但暗示显著差距）。
- **E²-Select 性能**：在帧选择与 RAG 基线中达到 58.2%，超越所有对比方法。
- **视角互补性**：单独使用第一人称视角准确率为 48.1%，第三人称视角为 51.2%，而双视角联合使用提升至 58.2%，证实互补性。

### 结论
- **视角偏好冲突**：问题框架（如“从第一人称视角看”）与答案定位（如需要第三人称视角信息）之间存在系统性冲突，导致模型在跨视角推理中表现不稳定。
- **挑战性**：现有 MLLM 无法有效融合双视角信息，EgoExoMem 为跨视角记忆推理提供了新的评估标准与研究方向。

## Overview
Egocentric memory is widely used in embodied intelligence, but it may be insufficient for comprehensive spatial-temporal reasoning. Inspired by human recall from both field and observer perspectives, we introduce EgoExoMem, the first benchmark for cross-view memory reasoning over synchronized egocentric and exocentric videos. EgoExoMem contains $2.6K$ high-quality MCQs across eight temporal, spatial, and cross-view QA types. To support dual-view retrieval, we propose E$^2$-Select, a training-free frame selection method for synchronized ego-exo videos. It combines relevance-based budget allocation with per-view k-DPP sampling to handle view asymmetry and cross-view temporal consistency. Experiments show that ego and exo views provide complementary memory cues, while existing MLLMs remain far from solving the benchmark: the best model reaches only $55.3\%$. E$^2$-Select achieves state-of-the-art performance of $58.2\%$ over frame-selection and RAG-based memory baselines. Further analysis reveals systematic view-preference conflicts between question framing and answer grounding, underscoring the novelty and challenge of cross-view memory reasoning.

## 参考
- https://arxiv.org/abs/2605.18734
- https://github.com/RuipingL/EgoExoMem
- https://mp.weixin.qq.com/s/4JQ1xa-cJ7J1ep_e4txNnA

## 개요

EgoExoMem 벤치마크는 인간이 경기장 내부와 외부 시점에서 동시에 정보를 회상하는 능력에서 영감을 받아, 구현 지능에서 1인칭 기억만으로 시공간 추론을 수행할 때의 한계를 해결하기 위해 설계되었습니다. 이 벤치마크는 시간, 공간, 교차 시점의 세 가지 질문 유형을 포함한 2.6K개의 고품질 객관식 문제로 구성되며, 1인칭 및 3인칭 비디오를 동시에 제공합니다. 이중 시점 검색을 지원하기 위해 연구팀은 E²-Select 방법을 제안했습니다. 이는 훈련이 필요 없는 프레임 선택 기술로, 관련성 기반 예산 할당과 각 시점별 k-DPP 샘플링을 통해 시점 비대칭성과 교차 시점 시간 일관성을 처리합니다. 실험 결과, 1인칭과 3인칭 시점이 상호 보완적인 기억 단서를 제공하지만, 기존의 다중 모달 대규모 언어 모델(MLLM)은 이 벤치마크에서 낮은 성능을 보였으며, 최고 모델도 55.3%에 그쳤습니다. E²-Select는 프레임 선택 및 RAG 기반 기억 기준선에서 58.2%의 최고 성능을 달성했습니다. 추가 분석은 문제 프레임과 답변 위치 간의 체계적인 시점 선호 충돌을 밝혀내며, 교차 시점 기억 추론의 새로운 특성과 도전 과제를 강조합니다.

## 핵심 내용
### 방법
- **EgoExoMem 벤치마크**: 동기화된 1인칭(egocentric) 및 3인칭(exocentric) 비디오를 기반으로 구축되었으며, 2.6K개의 고품질 객관식 문제를 포함합니다. 시간 추론(예: 사건 순서), 공간 추론(예: 물체 위치), 교차 시점 추론(예: 시점 전환)의 8가지 유형으로 나뉩니다.
- **E²-Select 프레임 선택 방법**: 훈련이 필요 없으며, 두 단계로 이중 시점 프레임 선택을 수행합니다:
  - **관련성 기반 예산 할당**: 각 시점과 쿼리의 관련성에 따라 프레임 선택 예산을 동적으로 할당하여 시점 비대칭성(예: 1인칭 시점은 손 동작에, 3인칭 시점은 전체 장면에 더 집중)을 처리합니다.
  - **각 시점별 k-DPP 샘플링**: 각 시점 내에서 k-DPP(k-Determinantal Point Process) 샘플링을 사용하여 선택된 프레임의 다양성과 교차 시점 시간 일관성을 보장합니다.

### 실험 설정
- **기준 모델**: 다양한 MLLM(예: GPT-4V, LLaVA-NeXT) 및 프레임 선택과 RAG(검색 증강 생성) 기반 기억 방법을 포함합니다.
- **평가 지표**: 정확도(Accuracy)로, 2.6K개의 객관식 문제에 대해 계산됩니다.

### 주요 수치
- **최고 MLLM 성능**: GPT-4V가 55.3%를 기록했으며, 인간 수준(구체적인 수치는 보고되지 않았지만 상당한 차이를 암시)에 크게 미치지 못합니다.
- **E²-Select 성능**: 프레임 선택 및 RAG 기준선에서 58.2%를 달성하여 모든 비교 방법을 능가했습니다.
- **시점 상호 보완성**: 1인칭 시점만 사용했을 때 정확도는 48.1%, 3인칭 시점만 사용했을 때는 51.2%였으나, 두 시점을 함께 사용하면 58.2%로 향상되어 상호 보완성을 확인했습니다.

### 결론
- **시점 선호 충돌**: 문제 프레임(예: "1인칭 시점에서 본")과 답변 위치(예: 3인칭 시점 정보 필요) 간의 체계적인 충돌로 인해 모델이 교차 시점 추론에서 불안정한 성능을 보입니다.
- **도전 과제**: 기존 MLLM은 이중 시점 정보를 효과적으로 통합하지 못하며, EgoExoMem은 교차 시점 기억 추론을 위한 새로운 평가 기준과 연구 방향을 제시합니다.
