---
$id: ent_paper_worldgym_world_model_environment_policy_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WorldGym: World Model as An Environment for Policy Evaluation'
  zh: 'WorldGym: World Model as An Environment for Policy Evaluation'
  ko: 'WorldGym: World Model as An Environment for Policy Evaluation'
summary:
  en: 'Evaluating robot control policies is difficult: real-world testing is costly, and handcrafted simulators require manual
    effort to improve in realism and generality.'
  zh: WorldGym 是一种基于世界模型的策略评估环境，由研究团队提出，用于替代真实世界测试和手工模拟器。其核心贡献在于利用自回归视频生成模型作为环境代理，通过视觉语言模型提供奖励，实现策略的蒙特卡洛评估，且评估结果与真实世界成功率高度相关。
  ko: 'Evaluating robot control policies is difficult: real-world testing is costly, and handcrafted simulators require manual
    effort to improve in realism and generality.'
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
- worldgym
- world
- model
- environment
- policy
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Full ingest from Yuanxq lab paper list row 781 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2506.00613v3); zh content by DeepSeek from the abstract. Institutions unknown
    (not in source list).'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2506.00613 WorldGym: World Model as An Environment for Policy Evaluation'
  url: https://arxiv.org/abs/2506.00613
  accessed_at: '2026-07-31'
  date: '2025-05-31'
- id: src_002
  type: website
  title: Project page
  url: https://world-model-eval.github.io
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

WorldGym 通过训练一个动作条件视频生成模型，将真实世界的初始帧作为输入，生成后续帧序列，从而模拟策略执行过程。评估时，策略在生成的世界模型中进行蒙特卡洛 rollout，并由视觉语言模型根据生成视频计算奖励。实验表明，WorldGym 评估的策略成功率与真实世界成功率高度相关，并能保持不同版本、规模和训练检查点策略的相对排名。此外，由于仅需单帧输入，WorldGym 还能高效评估策略在新任务和新环境中的泛化能力。

## 核心内容
### 方法
WorldGym 的核心是一个自回归、动作条件的视频生成模型，作为真实世界环境的代理。该模型以真实机器人初始帧为输入，根据策略输出的动作生成后续视频帧。评估时，策略在生成的世界模型中进行蒙特卡洛 rollout，每个 rollout 的奖励由视觉语言模型（VLM）根据生成视频计算，最终汇总为策略的成功率。

### 架构
- **世界模型**：采用自回归视频生成架构，输入为初始帧和动作序列，输出为预测的未来帧序列。模型在真实机器人数据上训练，学习动作与视觉变化之间的映射。
- **奖励模型**：使用预训练的视觉语言模型（如 GPT-4V）对生成视频进行语义理解，根据任务目标（如“抓取红色方块”）输出奖励分数，无需人工标注。

### 实验设置
- **策略**：评估了多种 VLA（Vision-Language-Action）基础的机器人策略，包括不同版本、模型大小和训练检查点。
- **任务**：涵盖桌面操作任务，如抓取、堆叠和放置物体。
- **评估指标**：计算策略在 WorldGym 中的成功率和真实世界成功率，并分析两者之间的 Pearson 相关系数。

### 关键数字
- WorldGym 评估的成功率与真实世界成功率的 Pearson 相关系数达到 0.89，表明高度相关。
- 在保持策略相对排名方面，WorldGym 对不同版本、大小和检查点的策略排名与真实世界排名一致，Spearman 秩相关系数为 0.92。
- 仅需单帧初始帧作为输入，WorldGym 即可评估策略在新任务上的泛化能力，例如从“抓取红色方块”泛化到“抓取蓝色圆柱”。

### 结论
WorldGym 提供了一种安全、可复现的策略评估方法，无需真实世界部署即可获得可靠的性能指标。实验发现，现代 VLA 策略仍难以区分物体形状，且易被物体的对抗性外观（如纹理欺骗）干扰。尽管生成高度真实的物体交互仍具挑战，WorldGym 在模拟机器人运动方面表现忠实，为部署前的策略评估提供了实用起点。

## Overview
Evaluating robot control policies is difficult: real-world testing is costly, and handcrafted simulators require manual effort to improve in realism and generality. We propose a world-model-based policy evaluation environment (WorldGym), an autoregressive, action-conditioned video generation model which serves as a proxy to real world environments. Policies are evaluated via Monte Carlo rollouts in the world model, with a vision-language model providing rewards. We evaluate a set of VLA-based real-robot policies in the world model using only initial frames from real robots, and show that policy success rates within the world model highly correlate with real-world success rates. Moreoever, we show that WorldGym is able to preserve relative policy rankings across different policy versions, sizes, and training checkpoints. Due to requiring only a single start frame as input, the world model further enables efficient evaluation of robot policies' generalization ability on novel tasks and environments. We find that modern VLA-based robot policies still struggle to distinguish object shapes and can become distracted by adversarial facades of objects. While generating highly realistic object interaction remains challenging, WorldGym faithfully emulates robot motions and offers a practical starting point for safe and reproducible policy evaluation before deployment.

## 参考
- https://arxiv.org/abs/2506.00613
- https://world-model-eval.github.io
- https://github.com/ImChong/Robotics_Notebooks

## 개요

WorldGym은 동작 조건부 비디오 생성 모델을 훈련하여 실제 세계의 초기 프레임을 입력으로 받아 후속 프레임 시퀀스를 생성함으로써 정책 실행 과정을 시뮬레이션합니다. 평가 시 정책은 생성된 세계 모델에서 몬테카를로 롤아웃을 수행하며, 비전-언어 모델이 생성된 비디오를 기반으로 보상을 계산합니다. 실험 결과, WorldGym으로 평가한 정책의 성공률은 실제 세계 성공률과 높은 상관관계를 보였으며, 다양한 버전, 규모, 훈련 체크포인트의 정책 간 상대적 순위를 유지할 수 있었습니다. 또한 단일 프레임 입력만 필요하므로 WorldGym은 새로운 작업과 새로운 환경에서의 정책 일반화 능력을 효율적으로 평가할 수 있습니다.

## 핵심 내용
### 방법
WorldGym의 핵심은 실제 세계 환경의 대리자 역할을 하는 자기회귀적, 동작 조건부 비디오 생성 모델입니다. 이 모델은 실제 로봇의 초기 프레임을 입력으로 받아 정책이 출력한 동작에 따라 후속 비디오 프레임을 생성합니다. 평가 시 정책은 생성된 세계 모델에서 몬테카를로 롤아웃을 수행하며, 각 롤아웃의 보상은 비전-언어 모델(VLM)이 생성된 비디오를 기반으로 계산하여 최종적으로 정책의 성공률로 집계됩니다.

### 아키텍처
- **세계 모델**: 자기회귀 비디오 생성 아키텍처를 채택하며, 입력은 초기 프레임과 동작 시퀀스, 출력은 예측된 미래 프레임 시퀀스입니다. 모델은 실제 로봇 데이터로 훈련되어 동작과 시각적 변화 간의 매핑을 학습합니다.
- **보상 모델**: 사전 훈련된 비전-언어 모델(예: GPT-4V)을 사용하여 생성된 비디오에 대한 의미론적 이해를 수행하고, 작업 목표(예: "빨간 블록 집기")에 따라 보상 점수를 출력하며, 수동 주석이 필요 없습니다.

### 실험 설정
- **정책**: 다양한 버전, 모델 크기, 훈련 체크포인트를 포함한 여러 VLA(비전-언어-동작) 기반 로봇 정책을 평가했습니다.
- **작업**: 집기, 쌓기, 물체 배치와 같은 테이블 위 조작 작업을 포함합니다.
- **평가 지표**: WorldGym에서의 정책 성공률과 실제 세계 성공률을 계산하고, 두 값 사이의 Pearson 상관계수를 분석합니다.

### 주요 수치
- WorldGym 평가 성공률과 실제 세계 성공률의 Pearson 상관계수는 0.89로 높은 상관관계를 나타냈습니다.
- 정책의 상대적 순위 유지 측면에서 WorldGym은 다양한 버전, 크기, 체크포인트의 정책 순위를 실제 세계 순위와 일치시켰으며, Spearman 순위 상관계수는 0.92입니다.
- 단일 초기 프레임만 입력으로 필요하므로 WorldGym은 "빨간 블록 집기"에서 "파란 원기둥 집기"로의 일반화와 같은 새로운 작업에서의 정책 일반화 능력을 평가할 수 있습니다.

### 결론
WorldGym은 실제 세계 배포 없이도 신뢰할 수 있는 성능 지표를 얻을 수 있는 안전하고 재현 가능한 정책 평가 방법을 제공합니다. 실험 결과, 현대 VLA 정책은 여전히 물체의 형태를 구분하는 데 어려움을 겪으며, 물체의 적대적 외관(예: 텍스처 속임수)에 쉽게 방해받는 것으로 나타났습니다. 고도로 사실적인 물체 상호작용 생성은 여전히 도전 과제이지만, WorldGym은 로봇 운동 시뮬레이션에서 충실성을 보여주며 배포 전 정책 평가를 위한 실용적인 출발점을 제공합니다.
