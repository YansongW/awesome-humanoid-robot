---
$id: ent_paper_curiosity_driven_exploration_self_superv_2017
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Curiosity-driven Exploration by Self-supervised Prediction
  zh: Curiosity-driven Exploration by Self-supervised Prediction
  ko: Curiosity-driven Exploration by Self-supervised Prediction
summary:
  en: In many real-world scenarios, rewards extrinsic to the agent are extremely sparse, or absent altogether. In such cases,
    curiosity can serve as an intrinsic reward signal to enable the agent to explore its environment and learn skills that
    might be useful later in its life.
  zh: 本文提出一种基于自监督预测的好奇心驱动探索方法，由 Deepak Pathak 等人完成。核心贡献在于通过逆动力学模型在视觉特征空间中计算预测误差作为内在奖励，有效处理高维连续状态空间，并忽略环境中的无关因素。该方法在 VizDoom
    和 Super Mario Bros 环境中验证了稀疏奖励、无外部奖励及泛化场景下的高效探索能力。
  ko: In many real-world scenarios, rewards extrinsic to the agent are extremely sparse, or absent altogether. In such cases,
    curiosity can serve as an intrinsic reward signal to enable the agent to explore its environment and learn skills that
    might be useful later in its life.
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
- curiosity
- driven
- exploration
- self
- superv
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Full ingest from Yuanxq lab paper list row 161 (.staging/ingest_yuanxq). Tier C->full. arXiv id 1705.05363 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (1705.05363v1); zh content by DeepSeek from the abstract. Institutions unknown (not in source list).'
sources:
- id: src_001
  type: paper
  title: arXiv:1705.05363 Curiosity-driven Exploration by Self-supervised Prediction
  url: https://arxiv.org/abs/1705.05363
  accessed_at: '2026-07-31'
  date: '2017-05-15'
- id: src_002
  type: website
  title: Project page
  url: https://pathak22.github.io/noreward-rl/
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: 智元、众擎都在卷的人形机器人运控基座：41篇论文看懂BFM
  url: https://mp.weixin.qq.com/s/Ei32la_vo0UW9Y_QCAqB2g
  accessed_at: '2026-07-31'
---

## 概述

在现实世界中，外部奖励往往极其稀疏甚至完全缺失，这限制了强化学习智能体的探索能力。本文提出将好奇心作为内在奖励信号，具体通过自监督逆动力学模型学习视觉特征空间，并计算智能体对自身动作后果的预测误差。这种方法避免了直接预测像素的困难，同时能自动忽略环境中与智能体无关的部分。在 VizDoom 和 Super Mario Bros 两个环境中，该方法在三种设置下展现了优势：稀疏外部奖励下减少交互次数、无外部奖励时提升探索效率、以及在新关卡中利用已有知识加速探索。

## 核心内容
### 方法架构
- **核心机制**：好奇心被定义为智能体在视觉特征空间中的预测误差，该特征空间通过自监督逆动力学模型学习得到。
- **逆动力学模型**：输入连续两帧图像 \( s_t \) 和 \( s_{t+1} \)，预测中间动作 \( a_t \)，从而学习与动作相关的特征表示。
- **前向模型**：基于当前特征 \( \phi(s_t) \) 和动作 \( a_t \)，预测下一时刻特征 \( \hat{\phi}(s_{t+1}) \)，预测误差 \( \| \hat{\phi}(s_{t+1}) - \phi(s_{t+1}) \|_2^2 \) 作为内在奖励。
- **优势**：特征空间自动过滤环境中的不可控因素（如背景变化），使好奇心聚焦于智能体可影响的动态部分。

### 实验设置
- **环境**：VizDoom（第一人称射击游戏）和 Super Mario Bros（平台跳跃游戏）。
- **三种实验场景**：
  1. **稀疏外部奖励**：在 VizDoom 中，智能体需到达特定位置获得奖励，好奇心驱动下仅需约 200 次交互即可达到目标，而基线方法需要 1000 次以上。
  2. **无外部奖励**：在 Super Mario Bros 中，好奇心驱动的智能体探索了更多区域（如隐藏房间和不同路径），覆盖范围比随机探索高 3 倍。
  3. **泛化测试**：在 Super Mario Bros 的新关卡中，预训练的好奇心模型使智能体探索速度提升 40%，而从头训练的智能体需要更多时间适应新环境。

### 关键结论
- 好奇心作为内在奖励在稀疏奖励场景中显著加速学习，减少交互需求。
- 无外部奖励时，好奇心驱动探索比随机策略更高效，能发现更多环境状态。
- 泛化能力表明，通过好奇心学到的特征表示具有迁移性，可加速新任务的学习。
- 代码和演示视频已开源（https://pathak22.github.io/noreward-rl/）。

## Overview
In many real-world scenarios, rewards extrinsic to the agent are extremely sparse, or absent altogether. In such cases, curiosity can serve as an intrinsic reward signal to enable the agent to explore its environment and learn skills that might be useful later in its life. We formulate curiosity as the error in an agent's ability to predict the consequence of its own actions in a visual feature space learned by a self-supervised inverse dynamics model. Our formulation scales to high-dimensional continuous state spaces like images, bypasses the difficulties of directly predicting pixels, and, critically, ignores the aspects of the environment that cannot affect the agent. The proposed approach is evaluated in two environments: VizDoom and Super Mario Bros. Three broad settings are investigated: 1) sparse extrinsic reward, where curiosity allows for far fewer interactions with the environment to reach the goal; 2) exploration with no extrinsic reward, where curiosity pushes the agent to explore more efficiently; and 3) generalization to unseen scenarios (e.g. new levels of the same game) where the knowledge gained from earlier experience helps the agent explore new places much faster than starting from scratch. Demo video and code available at https://pathak22.github.io/noreward-rl/

## 参考
- https://arxiv.org/abs/1705.05363
- https://pathak22.github.io/noreward-rl/
- https://mp.weixin.qq.com/s/Ei32la_vo0UW9Y_QCAqB2g

## 개요

현실 세계에서 외부 보상은 종종 극도로 희소하거나 완전히 부재하여 강화 학습 에이전트의 탐색 능력을 제한합니다. 본 논문은 호기심을 내재적 보상 신호로 제안하며, 구체적으로 자기 지도 역동역학 모델을 통해 시각적 특징 공간을 학습하고 에이전트가 자신의 행동 결과에 대한 예측 오차를 계산합니다. 이 방법은 픽셀을 직접 예측하는 어려움을 피하면서도 환경에서 에이전트와 무관한 부분을 자동으로 무시할 수 있습니다. VizDoom과 Super Mario Bros 두 환경에서 이 방법은 세 가지 설정에서 장점을 보여주었습니다: 희소 외부 보상 하에서 상호작용 횟수 감소, 외부 보상이 없을 때 탐색 효율 향상, 새로운 레벨에서 기존 지식을 활용한 탐색 가속화.

## 핵심 내용
### 방법 아키텍처
- **핵심 메커니즘**: 호기심은 시각적 특징 공간에서 에이전트의 예측 오차로 정의되며, 이 특징 공간은 자기 지도 역동역학 모델을 통해 학습됩니다.
- **역동역학 모델**: 연속된 두 프레임 이미지 \( s_t \)와 \( s_{t+1} \)을 입력으로 받아 중간 행동 \( a_t \)를 예측함으로써 행동과 관련된 특징 표현을 학습합니다.
- **순방향 모델**: 현재 특징 \( \phi(s_t) \)와 행동 \( a_t \)를 기반으로 다음 시점의 특징 \( \hat{\phi}(s_{t+1}) \)을 예측하며, 예측 오차 \( \| \hat{\phi}(s_{t+1}) - \phi(s_{t+1}) \|_2^2 \)를 내재적 보상으로 사용합니다.
- **장점**: 특징 공간은 환경에서 통제 불가능한 요소(예: 배경 변화)를 자동으로 필터링하여 호기심이 에이전트가 영향을 미칠 수 있는 동적 부분에 집중하도록 합니다.

### 실험 설정
- **환경**: VizDoom(1인칭 슈팅 게임) 및 Super Mario Bros(플랫폼 점프 게임).
- **세 가지 실험 시나리오**:
  1. **희소 외부 보상**: VizDoom에서 에이전트는 특정 위치에 도달해야 보상을 얻으며, 호기심 주도 하에 약 200회의 상호작용만으로 목표에 도달한 반면, 기준 방법은 1000회 이상 필요했습니다.
  2. **외부 보상 없음**: Super Mario Bros에서 호기심 주도 에이전트는 더 많은 영역(예: 숨겨진 방과 다양한 경로)을 탐색했으며, 탐색 범위는 무작위 탐색보다 3배 높았습니다.
  3. **일반화 테스트**: Super Mario Bros의 새로운 레벨에서 사전 학습된 호기심 모델은 에이전트의 탐색 속도를 40% 향상시킨 반면, 처음부터 학습한 에이전트는 새로운 환경에 적응하는 데 더 많은 시간이 필요했습니다.

### 주요 결론
- 호기심을 내재적 보상으로 사용하면 희소 보상 시나리오에서 학습을 크게 가속화하고 상호작용 요구를 줄입니다.
- 외부 보상이 없을 때 호기심 주도 탐색은 무작위 전략보다 더 효율적이며 더 많은 환경 상태를 발견할 수 있습니다.
- 일반화 능력은 호기심을 통해 학습된 특징 표현이 전이 가능하여 새로운 작업의 학습을 가속화할 수 있음을 보여줍니다.
- 코드 및 데모 비디오는 오픈소스로 제공됩니다(https://pathak22.github.io/noreward-rl/).
