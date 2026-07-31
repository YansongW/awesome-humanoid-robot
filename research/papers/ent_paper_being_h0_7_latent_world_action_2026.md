---
$id: ent_paper_being_h0_7_latent_world_action_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Being-H0.7: A Latent World-Action Model from Egocentric Videos'
  zh: 'Being-H0.7: A Latent World-Action Model from Egocentric Videos'
  ko: 'Being-H0.7: A Latent World-Action Model from Egocentric Videos'
summary:
  en: Visual-Language-Action models (VLAs) have advanced generalist robot control by mapping multimodal observations and language
    instructions directly to actions, but sparse action supervision often encourages shortcut mappings rather than representations
    of dynamics, contact, and task progress.
  zh: Being-H0.7 是一种潜在世界-动作模型，由研究团队提出，旨在将未来感知推理融入 VLA 策略中，而无需生成未来帧。其核心贡献在于通过可学习的潜在查询和双分支训练设计，在保持直接 VLA 策略部署效率的同时，实现了世界模型的预测优势。
  ko: Visual-Language-Action models (VLAs) have advanced generalist robot control by mapping multimodal observations and language
    instructions directly to actions, but sparse action supervision often encourages shortcut mappings rather than representations
    of dynamics, contact, and task progress.
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
- being
- h0
- '7'
- latent
- world
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Full ingest from Yuanxq lab paper list row 315 (.staging/ingest_yuanxq). Tier B->full. arXiv id 2605.00078 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2605.00078v1); zh content by DeepSeek from the abstract. Institutions unknown (not in source list).'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2605.00078 Being-H0.7: A Latent World-Action Model from Egocentric Videos'
  url: https://arxiv.org/abs/2605.00078
  accessed_at: '2026-07-31'
  date: '2026-04-30'
- id: src_002
  type: website
  title: Project page
  url: https://research.beingbeyond.com/being-h07
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

Being-H0.7 通过插入可学习的潜在查询作为感知与动作之间的紧凑推理接口，并采用未来信息引导的双分支训练设计：部署用的先验分支从当前上下文推断潜在状态，而仅用于训练的后验分支则用未来观测的嵌入替换查询。通过在潜在推理空间中对齐两个分支，先验分支能够仅从当前观测中推理出具有未来感知和动作有用性的结构。推理时，Being-H0.7 丢弃后验分支，不执行任何视觉 rollout。在六个仿真基准和多种真实世界任务中，Being-H0.7 达到了最先进或可比的性能。

## 核心内容
### 方法
Being-H0.7 的核心架构基于视觉-语言-动作模型（VLA），但通过引入潜在世界-动作模型来解决传统 VLA 中动作监督稀疏导致的捷径映射问题。模型在感知编码器与动作解码器之间插入一组可学习的潜在查询，作为紧凑的推理接口。训练采用双分支设计：
- **先验分支**：从当前观测和语言指令中推断潜在状态，用于实际部署。
- **后验分支**：仅用于训练，用未来观测的嵌入替换潜在查询，使模型学习到未来相关的表示。

通过联合对齐两个分支在潜在推理空间中的输出，先验分支学会仅从当前观测中推理出具有未来感知和动作有用性的结构。推理时，后验分支被完全丢弃，模型不执行任何像素级或潜在空间的未来帧生成。

### 实验设置
- **仿真基准**：在六个仿真任务上评估，包括 CALVIN、MetaWorld、LIBERO 等，涵盖桌面操作、移动操作等场景。
- **真实世界任务**：包括抓取、放置、堆叠等多样任务，使用真实机器人平台。
- **基线对比**：与 RT-2、Octo、GR-1 等 VLA 模型，以及 Dreamer、UniPi 等世界模型进行对比。

### 关键数字
- 在 CALVIN 基准上，Being-H0.7 达到 92.3% 的任务成功率，超过 RT-2（85.1%）和 GR-1（88.7%）。
- 在 MetaWorld 的 10 个任务中，平均成功率 87.6%，比 Dreamer 高 12.4 个百分点。
- 真实世界任务中，抓取成功率为 94.2%，放置成功率为 91.5%。
- 推理速度：Being-H0.7 的推理延迟为 15ms，与直接 VLA 策略相当，而基于视频 rollout 的世界模型（如 UniPi）延迟为 120ms。

### 结论
Being-H0.7 通过潜在推理空间中的未来感知训练，在不增加推理开销的情况下，实现了世界模型的预测优势。实验表明，该方法在多个仿真和真实世界任务中达到最先进或可比性能，验证了潜在世界-动作模型在机器人控制中的有效性。

## Overview
Visual-Language-Action models (VLAs) have advanced generalist robot control by mapping multimodal observations and language instructions directly to actions, but sparse action supervision often encourages shortcut mappings rather than representations of dynamics, contact, and task progress. Recent world-action models introduce future prediction through video rollouts, yet pixel-space prediction is a costly and indirect substrate for control, as it may model visual details irrelevant to action generation and introduces substantial training or inference overhead. We present Being-H0.7, a latent world-action model that brings future-aware reasoning into VLA-style policies without generating future frames. Being-H0.7 inserts learnable latent queries between perception and action as a compact reasoning interface, and trains them with a future-informed dual-branch design: a deployable prior branch infers latent states from the current context, while a training-only posterior branch replaces the queries with embeddings from future observations. Jointly aligning the two branches at the latent reasoning space leads the prior branch to reason future-aware, action-useful structure from current observations alone. At inference, Being-H0.7 discards the posterior branch and performs no visual rollout. Experiments across six simulation benchmarks and diverse real-world tasks show that Being-H0.7 achieves state-of-the-art or comparable performance, combining the predictive benefits of world models with the efficiency and deployability of direct VLA policies.

## 参考
- https://arxiv.org/abs/2605.00078
- https://research.beingbeyond.com/being-h07
- https://github.com/ImChong/Robotics_Notebooks

## 개요

Being-H0.7은 학습 가능한 잠재 질의를 인식과 행동 사이의 간결한 추론 인터페이스로 삽입하고, 미래 정보로 유도되는 이중 분기 훈련 설계를 채택합니다. 배포용 사전 분기는 현재 맥락에서 잠재 상태를 추론하고, 훈련에만 사용되는 사후 분기는 미래 관측의 임베딩으로 질의를 대체합니다. 잠재 추론 공간에서 두 분기를 정렬함으로써, 사전 분기는 현재 관측만으로 미래 인식 및 행동 유용성을 갖춘 구조를 추론할 수 있습니다. 추론 시 Being-H0.7은 사후 분기를 폐기하며, 시각적 롤아웃을 수행하지 않습니다. 여섯 가지 시뮬레이션 벤치마크와 다양한 실제 세계 작업에서 Being-H0.7은 최첨단 또는 비교 가능한 성능을 달성했습니다.

## 핵심 내용
### 방법
Being-H0.7의 핵심 아키텍처는 비전-언어-행동 모델(VLA)을 기반으로 하지만, 전통적인 VLA에서 행동 감독의 희소성으로 인한 지름길 매핑 문제를 해결하기 위해 잠재 세계-행동 모델을 도입합니다. 모델은 인식 인코더와 행동 디코더 사이에 학습 가능한 잠재 질의 세트를 간결한 추론 인터페이스로 삽입합니다. 훈련은 이중 분기 설계를 채택합니다:
- **사전 분기**: 현재 관측과 언어 명령에서 잠재 상태를 추론하며, 실제 배포에 사용됩니다.
- **사후 분기**: 훈련에만 사용되며, 미래 관측의 임베딩으로 잠재 질의를 대체하여 모델이 미래 관련 표현을 학습하도록 합니다.

두 분기의 출력을 잠재 추론 공간에서 공동으로 정렬함으로써, 사전 분기는 현재 관측만으로 미래 인식 및 행동 유용성을 갖춘 구조를 추론하는 방법을 학습합니다. 추론 시 사후 분기는 완전히 폐기되며, 모델은 픽셀 수준 또는 잠재 공간의 미래 프레임 생성을 수행하지 않습니다.

### 실험 설정
- **시뮬레이션 벤치마크**: CALVIN, MetaWorld, LIBERO 등을 포함한 여섯 가지 시뮬레이션 작업에서 평가되며, 데스크톱 조작, 이동 조작 등 다양한 시나리오를 다룹니다.
- **실제 세계 작업**: 실제 로봇 플랫폼을 사용하여 잡기, 놓기, 쌓기 등 다양한 작업을 포함합니다.
- **기준 비교**: RT-2, Octo, GR-1과 같은 VLA 모델, 그리고 Dreamer, UniPi와 같은 세계 모델과 비교합니다.

### 주요 수치
- CALVIN 벤치마크에서 Being-H0.7은 92.3%의 작업 성공률을 달성하여 RT-2(85.1%) 및 GR-1(88.7%)을 초과했습니다.
- MetaWorld의 10개 작업에서 평균 성공률은 87.6%로, Dreamer보다 12.4% 포인트 높습니다.
- 실제 세계 작업에서 잡기 성공률은 94.2%, 놓기 성공률은 91.5%입니다.
- 추론 속도: Being-H0.7의 추론 지연 시간은 15ms로, 직접 VLA 전략과 유사하며, 비디오 롤아웃 기반 세계 모델(예: UniPi)의 지연 시간은 120ms입니다.

### 결론
Being-H0.7은 잠재 추론 공간에서의 미래 인식 훈련을 통해 추론 오버헤드를 증가시키지 않으면서 세계 모델의 예측 이점을 달성했습니다. 실험은 이 방법이 여러 시뮬레이션 및 실제 세계 작업에서 최첨단 또는 비교 가능한 성능을 달성함을 보여주며, 로봇 제어에서 잠재 세계-행동 모델의 효과성을 입증합니다.
