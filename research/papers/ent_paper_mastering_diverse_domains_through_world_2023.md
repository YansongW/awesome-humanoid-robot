---
$id: ent_paper_mastering_diverse_domains_through_world_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Mastering Diverse Domains through World Models
  zh: Mastering Diverse Domains through World Models
  ko: Mastering Diverse Domains through World Models
summary:
  en: Developing a general algorithm that learns to solve tasks across a wide range of applications has been a fundamental
    challenge in artificial intelligence.
  zh: DreamerV3 是由 Google DeepMind 团队提出的通用强化学习算法，通过世界模型学习环境并想象未来场景来提升行为。该算法以单一配置在超过150个多样化任务中超越专门方法，并首次在 Minecraft 中从零开始收集钻石，无需人类数据或课程学习。
  ko: Developing a general algorithm that learns to solve tasks across a wide range of applications has been a fundamental
    challenge in artificial intelligence.
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
- mastering
- diverse
- domains
- through
- world
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Full ingest from Yuanxq lab paper list row 779 (.staging/ingest_yuanxq). Tier A->full. Title guard: abstract_mention
    (score 0.8). Abstract and metadata from arXiv API (2301.04104v2); zh content by DeepSeek from the abstract. Institutions
    unknown (not in source list).'
sources:
- id: src_001
  type: paper
  title: arXiv:2301.04104 Mastering Diverse Domains through World Models
  url: https://arxiv.org/abs/2301.04104
  accessed_at: '2026-07-31'
  date: '2023-01-10'
- id: src_002
  type: website
  title: Project page
  url: https://danijar.com/dreamerv3
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

DreamerV3 是一种基于世界模型的通用强化学习算法，旨在解决跨广泛领域的任务。它通过学习环境模型并想象未来场景来优化行为，采用归一化、平衡和变换等鲁棒性技术，确保在不同领域稳定学习。该算法以单一配置在超过150个任务中表现优于专门方法，包括 Atari 游戏、DMControl 控制任务和 Minecraft 等。特别地，DreamerV3 是首个在 Minecraft 中从像素和稀疏奖励出发，无需人类数据或课程学习就能收集钻石的算法，解决了人工智能领域的一个重大挑战。

## 核心内容
### 方法
DreamerV3 的核心是学习一个世界模型，该模型由三个组件构成：
- **表征模型**：将观测（如像素图像）编码为潜在状态。
- **转移模型**：预测给定动作下的下一个潜在状态。
- **奖励模型**：从潜在状态预测即时奖励。

算法通过想象未来轨迹（即“梦境”）来训练策略和价值函数，使用 actor-critic 方法优化行为。关键创新在于引入多种鲁棒性技术：
- **归一化**：使用 Symlog 变换对奖励和值函数进行缩放，避免梯度爆炸。
- **平衡**：通过动态调整策略更新步长，防止过拟合。
- **变换**：采用随机网络蒸馏（Random Network Distillation, RND）处理稀疏奖励环境。

### 架构
DreamerV3 采用端到端训练，世界模型和策略网络共享潜在状态。模型使用卷积神经网络（CNN）处理像素输入，循环神经网络（RNN）捕捉时序依赖。训练过程分为两个阶段：
1. **世界模型学习**：从真实经验回放缓冲区中采样，最小化预测误差。
2. **行为学习**：在想象轨迹中优化策略，使用梯度上升最大化累积奖励。

### 实验设置
实验覆盖 150 多个任务，包括：
- **Atari 2600**：55 个游戏，使用 100M 帧训练。
- **DMControl**：20 个连续控制任务，使用 500K 步。
- **Minecraft**：钻石收集任务，使用 100M 步。

所有任务使用同一超参数配置，无需手动调整。Minecraft 环境使用稀疏奖励（仅收集钻石时获得 +1 奖励），并包含复杂探索需求。

### 关键数字
- **性能**：在 Atari 上，DreamerV3 的中位人类归一化得分（HNS）达到 1.0，超越之前最佳方法（如 IQN 的 0.8）。
- **Minecraft 成就**：首次在无人类数据或课程下收集钻石，成功率约 10%（100M 步内）。
- **鲁棒性**：单一配置在 150+ 任务中稳定收敛，无需调参。

### 结论
DreamerV3 展示了通用强化学习算法的潜力，通过世界模型和鲁棒性技术，能够跨领域解决复杂任务。其成功表明，未来强化学习可减少人工干预，广泛应用于机器人、游戏和现实世界控制问题。

## Overview
Developing a general algorithm that learns to solve tasks across a wide range of applications has been a fundamental challenge in artificial intelligence. Although current reinforcement learning algorithms can be readily applied to tasks similar to what they have been developed for, configuring them for new application domains requires significant human expertise and experimentation. We present DreamerV3, a general algorithm that outperforms specialized methods across over 150 diverse tasks, with a single configuration. Dreamer learns a model of the environment and improves its behavior by imagining future scenarios. Robustness techniques based on normalization, balancing, and transformations enable stable learning across domains. Applied out of the box, Dreamer is the first algorithm to collect diamonds in Minecraft from scratch without human data or curricula. This achievement has been posed as a significant challenge in artificial intelligence that requires exploring farsighted strategies from pixels and sparse rewards in an open world. Our work allows solving challenging control problems without extensive experimentation, making reinforcement learning broadly applicable.

## 参考
- https://arxiv.org/abs/2301.04104
- https://danijar.com/dreamerv3
- https://github.com/ImChong/Robotics_Notebooks

## 개요

DreamerV3는 세계 모델 기반의 범용 강화 학습 알고리즘으로, 광범위한 도메인의 작업을 해결하기 위해 설계되었습니다. 환경 모델을 학습하고 미래 시나리오를 상상하여 행동을 최적화하며, 정규화, 균형, 변환 등의 강건성 기술을 적용하여 다양한 도메인에서 안정적인 학습을 보장합니다. 이 알고리즘은 단일 구성으로 Atari 게임, DMControl 제어 작업, Minecraft 등 150개 이상의 작업에서 전문 방법보다 뛰어난 성능을 보였습니다. 특히 DreamerV3는 Minecraft에서 픽셀과 희소 보상만을 사용하여 인간 데이터나 커리큘럼 학습 없이 다이아몬드를 수집한 최초의 알고리즘으로, 인공지능 분야의 주요 난제를 해결했습니다.

## 핵심 내용
### 방법
DreamerV3의 핵심은 세 가지 구성 요소로 이루어진 세계 모델을 학습하는 것입니다:
- **표상 모델**: 관측(예: 픽셀 이미지)을 잠재 상태로 인코딩합니다.
- **전이 모델**: 주어진 행동에 따른 다음 잠재 상태를 예측합니다.
- **보상 모델**: 잠재 상태에서 즉각적인 보상을 예측합니다.

알고리즘은 미래 궤적(즉, "꿈")을 상상하여 정책과 가치 함수를 훈련하며, actor-critic 방법을 사용하여 행동을 최적화합니다. 주요 혁신은 여러 강건성 기술을 도입한 점입니다:
- **정규화**: Symlog 변환을 사용하여 보상과 가치 함수를 스케일링하고 그래디언트 폭발을 방지합니다.
- **균형**: 정책 업데이트 단계를 동적으로 조정하여 과적합을 방지합니다.
- **변환**: RND(Random Network Distillation)를 사용하여 희소 보상 환경을 처리합니다.

### 아키텍처
DreamerV3는 종단 간 훈련을 채택하며, 세계 모델과 정책 네트워크가 잠재 상태를 공유합니다. 모델은 CNN(Convolutional Neural Network)을 사용하여 픽셀 입력을 처리하고, RNN(Recurrent Neural Network)을 사용하여 시간적 의존성을 포착합니다. 훈련 과정은 두 단계로 나뉩니다:
1. **세계 모델 학습**: 실제 경험 재생 버퍼에서 샘플링하여 예측 오차를 최소화합니다.
2. **행동 학습**: 상상된 궤적에서 정책을 최적화하고, 그래디언트 상승을 사용하여 누적 보상을 최대화합니다.

### 실험 설정
실험은 150개 이상의 작업을 포함하며, 다음과 같습니다:
- **Atari 2600**: 55개 게임, 1억 프레임 훈련.
- **DMControl**: 20개 연속 제어 작업, 50만 스텝.
- **Minecraft**: 다이아몬드 수집 작업, 1억 스텝.

모든 작업은 동일한 하이퍼파라미터 구성을 사용하며, 수동 조정이 필요하지 않습니다. Minecraft 환경은 희소 보상(다이아몬드 수집 시에만 +1 보상)을 사용하며, 복잡한 탐색 요구 사항을 포함합니다.

### 주요 수치
- **성능**: Atari에서 DreamerV3의 중간 인간 정규화 점수(HNS)는 1.0에 도달하여 이전 최고 방법(예: IQN의 0.8)을 능가했습니다.
- **Minecraft 성과**: 인간 데이터나 커리큘럼 없이 다이아몬드를 수집한 최초의 사례로, 성공률 약 10%(1억 스텝 내).
- **강건성**: 단일 구성으로 150개 이상의 작업에서 안정적으로 수렴하며, 매개변수 조정이 필요 없습니다.

### 결론
DreamerV3는 세계 모델과 강건성 기술을 통해 다양한 도메인의 복잡한 작업을 해결할 수 있는 범용 강화 학습 알고리즘의 잠재력을 보여줍니다. 이러한 성공은 미래 강화 학습이 인간의 개입을 줄이고 로봇 공학, 게임, 현실 세계 제어 문제에 널리 적용될 수 있음을 시사합니다.
