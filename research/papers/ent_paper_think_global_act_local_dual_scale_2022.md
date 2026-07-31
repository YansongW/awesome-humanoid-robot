---
$id: ent_paper_think_global_act_local_dual_scale_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Think Global, Act Local: Dual-scale Graph Transformer for Vision-and-Language Navigation'
  zh: 'Think Global, Act Local: Dual-scale Graph Transformer for Vision-and-Language Navigation'
  ko: 'Think Global, Act Local: Dual-scale Graph Transformer for Vision-and-Language Navigation'
summary:
  en: 'Following language instructions to navigate in unseen environments is a challenging problem for autonomous embodied
    agents. The agent not only needs to ground languages in visual scenes, but also should explore the environment to reach
    its target. Institutions per source list: 法国国家信息与自动化研究所.'
  zh: DUET 是一种双尺度图变换器，由研究团队提出用于视觉与语言导航任务。其核心贡献在于通过动态结合局部观测的细粒度编码与全局地图的粗粒度编码，实现了长期动作规划与跨模态理解的平衡。该方法在 REVERIE 和 SOON 基准上显著超越现有技术，并在
    R2R 基准上提升了成功率。
  ko: 'Following language instructions to navigate in unseen environments is a challenging problem for autonomous embodied
    agents. The agent not only needs to ground languages in visual scenes, but also should explore the environment to reach
    its target. Institutions per source list: 法国国家信息与自动化研究所.'
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
- think
- global
- act
- local
- dual
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 822 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2202.11742v1); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2202.11742 Think Global, Act Local: Dual-scale Graph Transformer for Vision-and-Language Navigation'
  url: https://arxiv.org/abs/2202.11742
  accessed_at: '2026-07-31'
  date: '2022-02-23'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

针对自主具身代理在未知环境中遵循语言指令导航的挑战，DUET 提出了一种双尺度图变换器架构。它通过在线构建拓扑地图支持全局动作空间的高效探索，并利用图变换器动态融合局部细粒度编码与全局粗粒度编码，以平衡大规模动作推理与细粒度语言定位的复杂度。实验表明，该方法在目标导向的 VLN 基准 REVERIE 和 SOON 上大幅领先现有方法，同时在细粒度基准 R2R 上也取得了成功率提升。

## 核心内容
### 方法概述
DUET 的核心创新在于双尺度图变换器设计，用于联合长期动作规划与细粒度跨模态理解。它通过在线构建拓扑地图，使代理能够在全局动作空间中高效探索，同时避免传统方法中动作空间过大导致的推理困难。

### 架构细节
- **双尺度编码**：动态结合两种编码尺度：
  - **局部细粒度编码**：对当前观测的视觉场景进行精细编码，支持语言指令的细粒度定位。
  - **全局粗粒度编码**：基于拓扑地图的全局结构进行编码，支持长期动作规划。
- **图变换器融合**：通过图变换器机制动态融合两种尺度的编码，平衡推理复杂度与语言定位精度。

### 实验设置与结果
- **基准测试**：在目标导向的 VLN 基准 REVERIE 和 SOON 上，DUET 显著优于现有方法；在细粒度基准 R2R 上，成功率也得到提升。
- **关键性能**：具体数值未在摘要中给出，但强调在 REVERIE 和 SOON 上大幅超越 SOTA，在 R2R 上改进成功率。

### 结论
DUET 通过双尺度图变换器有效解决了 VLN 中动作规划与语言定位的权衡问题，为自主导航代理提供了更高效的解决方案。

## Overview
Following language instructions to navigate in unseen environments is a challenging problem for autonomous embodied agents. The agent not only needs to ground languages in visual scenes, but also should explore the environment to reach its target. In this work, we propose a dual-scale graph transformer (DUET) for joint long-term action planning and fine-grained cross-modal understanding. We build a topological map on-the-fly to enable efficient exploration in global action space. To balance the complexity of large action space reasoning and fine-grained language grounding, we dynamically combine a fine-scale encoding over local observations and a coarse-scale encoding on a global map via graph transformers. The proposed approach, DUET, significantly outperforms state-of-the-art methods on goal-oriented vision-and-language navigation (VLN) benchmarks REVERIE and SOON. It also improves the success rate on the fine-grained VLN benchmark R2R.

## 参考
- https://arxiv.org/abs/2202.11742
- https://github.com/ImChong/Robotics_Notebooks

## 개요

자율 임베디드 에이전트가未知 환경에서 언어 지시를 따라 탐색하는 과제를 해결하기 위해, DUET는 이중 스케일 그래프 트랜스포머 아키텍처를 제안합니다. 이는 온라인으로 토폴로지 맵을 구축하여 전역 행동 공간에서 효율적인 탐색을 지원하며, 그래프 트랜스포머를 통해 로컬 세밀한 인코딩과 전역 거친 인코딩을 동적으로 융합하여 대규모 행동 추론과 세밀한 언어 위치 파악의 복잡성을 균형 있게 조정합니다. 실험 결과, 이 방법은 목표 지향 VLN 벤치마크 REVERIE와 SOON에서 기존 방법을 크게 앞서며, 세밀한 벤치마크 R2R에서도 성공률 향상을 달성했습니다.

## 핵심 내용
### 방법 개요
DUET의 핵심 혁신은 장기 행동 계획과 세밀한 교차 양식 이해를 결합하기 위한 이중 스케일 그래프 트랜스포머 설계에 있습니다. 이는 온라인으로 토폴로지 맵을 구축하여 에이전트가 전역 행동 공간에서 효율적으로 탐색할 수 있게 하면서, 기존 방법에서 행동 공간이 너무 커서 발생하는 추론 어려움을 피합니다.

### 아키텍처 세부 사항
- **이중 스케일 인코딩**: 두 가지 인코딩 스케일을 동적으로 결합합니다:
  - **로컬 세밀한 인코딩**: 현재 관측된 시각적 장면을 정밀하게 인코딩하여 언어 지시의 세밀한 위치 파악을 지원합니다.
  - **전역 거친 인코딩**: 토폴로지 맵의 전역 구조를 기반으로 인코딩하여 장기 행동 계획을 지원합니다.
- **그래프 트랜스포머 융합**: 그래프 트랜스포머 메커니즘을 통해 두 스케일의 인코딩을 동적으로 융합하여 추론 복잡성과 언어 위치 파악 정확도를 균형 있게 조정합니다.

### 실험 설정 및 결과
- **벤치마크 테스트**: 목표 지향 VLN 벤치마크 REVERIE와 SOON에서 DUET는 기존 방법보다 현저히 우수하며, 세밀한 벤치마크 R2R에서도 성공률이 향상되었습니다.
- **주요 성능**: 구체적인 수치는 요약에 제시되지 않았지만, REVERIE와 SOON에서 SOTA를 크게 능가하고 R2R에서 성공률을 개선한다는 점이 강조됩니다.

### 결론
DUET는 이중 스케일 그래프 트랜스포머를 통해 VLN에서 행동 계획과 언어 위치 파악 간의 균형 문제를 효과적으로 해결하여, 자율 탐색 에이전트에 더 효율적인 솔루션을 제공합니다.
