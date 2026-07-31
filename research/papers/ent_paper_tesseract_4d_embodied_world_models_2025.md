---
$id: ent_paper_tesseract_4d_embodied_world_models_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TesserAct: Learning 4D Embodied World Models'
  zh: 'TesserAct: Learning 4D Embodied World Models'
  ko: 'TesserAct: Learning 4D Embodied World Models'
summary:
  en: This paper presents an effective approach for learning novel 4D embodied world models, which predict the dynamic evolution
    of 3D scenes over time in response to an embodied agent's actions, providing both spatial and temporal consistency.
  zh: TesserAct 提出了一种学习 4D 具身世界模型的新方法，通过预测 3D 场景在智能体动作下的动态演化，实现时空一致性。该方法利用 RGB-DN（RGB、深度和法线）视频训练模型，超越了传统 2D 模型，并支持高效学习逆动力学模型。核心贡献在于将生成视频直接转换为高质量
    4D 场景，显著提升了策略学习性能。
  ko: This paper presents an effective approach for learning novel 4D embodied world models, which predict the dynamic evolution
    of 3D scenes over time in response to an embodied agent's actions, providing both spatial and temporal consistency.
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
- tesseract
- 4d
- embodied
- world
- models
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Full ingest from Yuanxq lab paper list row 767 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2504.20995 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2504.20995v1); zh content by DeepSeek from the abstract. Institutions unknown (not in source list).'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2504.20995 TesserAct: Learning 4D Embodied World Models'
  url: https://arxiv.org/abs/2504.20995
  accessed_at: '2026-07-31'
  date: '2025-04-29'
- id: src_002
  type: website
  title: Project page
  url: https://tesseractworld.github.io/
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

TesserAct 通过扩展机器人操作视频数据集，添加深度和法线信息，并微调视频生成模型来联合预测每帧的 RGB-DN 数据。随后，该研究提出一种算法，将生成的 RGB、深度和法线视频直接转换为高质量的 4D 世界场景。这种方法确保了具身场景中 4D 预测的时空连贯性，支持新视角合成，并使得基于此学习的策略性能显著优于先前基于视频的世界模型。

## 核心内容
### 方法概述
TesserAct 的核心是学习一个 4D 具身世界模型，该模型能预测 3D 场景在智能体动作下的动态演化，同时保持空间和时间一致性。研究通过训练 RGB-DN（RGB、深度和法线）视频来实现这一目标，这比传统 2D 模型更全面地捕捉形状、配置和时序变化。

### 架构与流程
- **数据扩展**：首先，利用现成模型为现有机器人操作视频数据集添加深度和法线信息，生成 RGB-DN 视频。
- **模型微调**：在标注后的数据集上微调视频生成模型，使其能联合预测每帧的 RGB、深度和法线。
- **4D 场景转换**：提出一种算法，将生成的 RGB、深度和法线视频直接转换为高质量的 4D 世界场景，确保时空连贯性。

### 实验设置与关键数字
- 实验在具身场景中进行，评估模型在 4D 场景预测、新视角合成和策略学习方面的表现。
- 策略学习性能显著优于基于先前视频世界模型的方法，具体提升幅度在文中通过对比实验量化（例如，在特定任务上成功率提升 X%）。
- 模型生成的 4D 场景在时空一致性上表现优异，支持从任意视角观察环境演化。

### 结论
TesserAct 通过 RGB-DN 视频学习 4D 世界模型，有效解决了具身场景中的动态预测问题。其生成的 4D 场景不仅具备时空一致性，还能用于新视角合成和策略学习，为机器人操作等任务提供了更强大的基础模型。

## Overview
This paper presents an effective approach for learning novel 4D embodied world models, which predict the dynamic evolution of 3D scenes over time in response to an embodied agent's actions, providing both spatial and temporal consistency. We propose to learn a 4D world model by training on RGB-DN (RGB, Depth, and Normal) videos. This not only surpasses traditional 2D models by incorporating detailed shape, configuration, and temporal changes into their predictions, but also allows us to effectively learn accurate inverse dynamic models for an embodied agent. Specifically, we first extend existing robotic manipulation video datasets with depth and normal information leveraging off-the-shelf models. Next, we fine-tune a video generation model on this annotated dataset, which jointly predicts RGB-DN (RGB, Depth, and Normal) for each frame. We then present an algorithm to directly convert generated RGB, Depth, and Normal videos into a high-quality 4D scene of the world. Our method ensures temporal and spatial coherence in 4D scene predictions from embodied scenarios, enables novel view synthesis for embodied environments, and facilitates policy learning that significantly outperforms those derived from prior video-based world models.

## 参考
- https://arxiv.org/abs/2504.20995
- https://tesseractworld.github.io/
- https://github.com/ImChong/Robotics_Notebooks

## 개요

TesserAct는 로봇 조작 비디오 데이터셋을 확장하여 깊이 및 법선 정보를 추가하고, 비디오 생성 모델을 미세 조정하여 각 프레임의 RGB-DN 데이터를 공동으로 예측합니다. 이후, 본 연구는 생성된 RGB, 깊이 및 법선 비디오를 직접 고품질 4D 세계 장면으로 변환하는 알고리즘을 제안합니다. 이 방법은 구현된 장면에서 4D 예측의 시공간적 일관성을 보장하고, 새로운 시점 합성을 지원하며, 이를 기반으로 학습된 정책이 이전의 비디오 기반 세계 모델보다 훨씬 우수한 성능을 보입니다.

## 핵심 내용
### 방법 개요
TesserAct의 핵심은 에이전트의 행동에 따른 3D 장면의 동적 진화를 예측하면서 공간적 및 시간적 일관성을 유지하는 4D 구현 세계 모델을 학습하는 것입니다. 연구는 RGB-DN(RGB, 깊이 및 법선) 비디오를 훈련하여 이를 달성하며, 이는 기존 2D 모델보다 형태, 구성 및 시간적 변화를 더 포괄적으로 포착합니다.

### 아키텍처 및 프로세스
- **데이터 확장**: 먼저, 기존 모델을 활용하여 기존 로봇 조작 비디오 데이터셋에 깊이 및 법선 정보를 추가하여 RGB-DN 비디오를 생성합니다.
- **모델 미세 조정**: 주석이 달린 데이터셋에서 비디오 생성 모델을 미세 조정하여 각 프레임의 RGB, 깊이 및 법선을 공동으로 예측할 수 있게 합니다.
- **4D 장면 변환**: 생성된 RGB, 깊이 및 법선 비디오를 직접 고품질 4D 세계 장면으로 변환하여 시공간적 일관성을 보장하는 알고리즘을 제안합니다.

### 실험 설정 및 주요 수치
- 실험은 구현된 장면에서 수행되며, 모델의 4D 장면 예측, 새로운 시점 합성 및 정책 학습 성능을 평가합니다.
- 정책 학습 성능은 이전의 비디오 기반 세계 모델 방법보다 현저히 우수하며, 구체적인 향상 폭은 비교 실험을 통해 정량화됩니다(예: 특정 작업에서 성공률 X% 향상).
- 모델이 생성한 4D 장면은 시공간적 일관성에서 우수한 성능을 보이며, 임의의 시점에서 환경 진화를 관찰할 수 있도록 지원합니다.

### 결론
TesserAct는 RGB-DN 비디오를 통해 4D 세계 모델을 학습하여 구현된 장면에서의 동적 예측 문제를 효과적으로 해결합니다. 생성된 4D 장면은 시공간적 일관성을 가질 뿐만 아니라 새로운 시점 합성 및 정책 학습에도 사용될 수 있어, 로봇 조작과 같은 작업에 더 강력한 기반 모델을 제공합니다.
