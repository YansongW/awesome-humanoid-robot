---
$id: ent_paper_cosmos_policy_fine_tuning_video_models_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning'
  zh: 'Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning'
  ko: 'Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning'
summary:
  en: Recent video generation models demonstrate remarkable ability to capture complex physical interactions and scene evolution
    over time. To leverage their spatiotemporal priors, robotics works have adapted video models for policy learning but introduce
    complexity by requiring multiple stages of post-training and new architectural components for action generation.
  zh: Cosmos Policy 由 NVIDIA 提出，是一种通过单阶段微调将预训练视频模型 Cosmos-Predict2 转化为机器人策略的简洁方法。其核心贡献在于无需修改架构，直接利用视频模型的潜在扩散过程生成动作、未来状态图像和累积奖励值，在
    LIBERO 和 RoboCasa 基准上分别达到 98.5% 和 67.1% 的平均成功率，并在真实世界双臂操作任务中取得最高平均分。
  ko: Recent video generation models demonstrate remarkable ability to capture complex physical interactions and scene evolution
    over time. To leverage their spatiotemporal priors, robotics works have adapted video models for policy learning but introduce
    complexity by requiring multiple stages of post-training and new architectural components for action generation.
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
- cosmos
- policy
- fine
- tuning
- video
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Full ingest from Yuanxq lab paper list row 777 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2601.16163v1); zh content by DeepSeek from the abstract. Institutions unknown
    (not in source list).'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2601.16163 Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning'
  url: https://arxiv.org/abs/2601.16163
  accessed_at: '2026-07-31'
  date: '2026-01-22'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

Cosmos Policy 通过单阶段后训练将预训练视频模型 Cosmos-Predict2 适配为机器人策略，避免了传统方法中多阶段训练和架构修改的复杂性。该方法将机器人动作编码为视频模型潜在扩散过程中的潜在帧，从而利用模型预训练的先验知识捕捉复杂动作分布。此外，Cosmos Policy 还能生成未来状态图像和累积奖励值，支持测试时规划更高成功率的动作轨迹。在 LIBERO 和 RoboCasa 仿真基准上，它分别实现了 98.5% 和 67.1% 的平均成功率，并在真实世界双臂操作任务中超越从头训练的扩散策略、基于视频模型的策略以及微调后的视觉-语言-动作模型。通过策略部署数据，Cosmos Policy 还能从经验中学习以改进世界模型和价值函数，进一步提升挑战性任务的成功率。

## 核心内容
### 方法
Cosmos Policy 的核心是将预训练视频模型 Cosmos-Predict2 通过单阶段后训练直接转化为机器人策略，无需修改架构。它利用视频模型的潜在扩散过程，将机器人动作编码为潜在帧，从而利用模型预训练的先验知识捕捉复杂动作分布。此外，该方法还生成未来状态图像和累积奖励值，这些同样编码为潜在帧，支持测试时规划更高成功率的动作轨迹。

### 实验设置
- **仿真基准**：LIBERO 和 RoboCasa，分别评估任务成功率和泛化能力。
- **真实世界任务**：挑战性双臂操作任务，评估实际部署性能。
- **对比方法**：包括从头训练的扩散策略、基于视频模型的策略以及微调后的视觉-语言-动作模型。

### 关键数字
- **LIBERO 基准**：平均成功率 98.5%。
- **RoboCasa 基准**：平均成功率 67.1%。
- **真实世界任务**：在双臂操作任务中取得最高平均分，超越所有对比方法。

### 结论
Cosmos Policy 通过单阶段微调预训练视频模型，实现了高效且强大的机器人策略学习。其无需架构修改的特性降低了部署复杂度，同时通过生成未来状态和奖励值支持规划，显著提升了任务成功率。此外，该方法还能从策略部署数据中学习，进一步优化世界模型和价值函数，在挑战性任务中实现更高成功率。代码、模型和训练数据已开源。

## Overview
Recent video generation models demonstrate remarkable ability to capture complex physical interactions and scene evolution over time. To leverage their spatiotemporal priors, robotics works have adapted video models for policy learning but introduce complexity by requiring multiple stages of post-training and new architectural components for action generation. In this work, we introduce Cosmos Policy, a simple approach for adapting a large pretrained video model (Cosmos-Predict2) into an effective robot policy through a single stage of post-training on the robot demonstration data collected on the target platform, with no architectural modifications. Cosmos Policy learns to directly generate robot actions encoded as latent frames within the video model's latent diffusion process, harnessing the model's pretrained priors and core learning algorithm to capture complex action distributions. Additionally, Cosmos Policy generates future state images and values (expected cumulative rewards), which are similarly encoded as latent frames, enabling test-time planning of action trajectories with higher likelihood of success. In our evaluations, Cosmos Policy achieves state-of-the-art performance on the LIBERO and RoboCasa simulation benchmarks (98.5% and 67.1% average success rates, respectively) and the highest average score in challenging real-world bimanual manipulation tasks, outperforming strong diffusion policies trained from scratch, video model-based policies, and state-of-the-art vision-language-action models fine-tuned on the same robot demonstrations. Furthermore, given policy rollout data, Cosmos Policy can learn from experience to refine its world model and value function and leverage model-based planning to achieve even higher success rates in challenging tasks. We release code, models, and training data at https://research.nvidia.com/labs/dir/cosmos-policy/

## 参考
- https://arxiv.org/abs/2601.16163
- https://github.com/ImChong/Robotics_Notebooks

## 개요

Cosmos Policy는 단일 단계 후훈련을 통해 사전 훈련된 비디오 모델 Cosmos-Predict2를 로봇 정책으로 직접 변환하여, 기존 방법의 다단계 훈련 및 아키텍처 수정의 복잡성을 피합니다. 이 방법은 로봇 동작을 비디오 모델의 잠재 확산 과정에서 잠재 프레임으로 인코딩함으로써, 모델 사전 훈련의 사전 지식을 활용하여 복잡한 동작 분포를 포착합니다. 또한 Cosmos Policy는 미래 상태 이미지와 누적 보상 값을 생성하여, 테스트 시 더 높은 성공률의 동작 궤적을 계획할 수 있도록 지원합니다. LIBERO 및 RoboCasa 시뮬레이션 벤치마크에서 각각 98.5% 및 67.1%의 평균 성공률을 달성했으며, 실제 세계 양팔 조작 작업에서 처음부터 훈련된 확산 정책, 비디오 기반 정책, 미세 조정된 시각-언어-동작 모델을 능가했습니다. 정책 배포 데이터를 통해 Cosmos Policy는 경험으로부터 학습하여 세계 모델과 가치 함수를 개선하고, 도전적인 작업의 성공률을 더욱 향상시킬 수 있습니다.

## 핵심 내용
### 방법
Cosmos Policy의 핵심은 사전 훈련된 비디오 모델 Cosmos-Predict2를 단일 단계 후훈련을 통해 아키텍처 수정 없이 직접 로봇 정책으로 변환하는 것입니다. 이는 비디오 모델의 잠재 확산 과정을 활용하여 로봇 동작을 잠재 프레임으로 인코딩함으로써, 모델 사전 훈련의 사전 지식을 활용하여 복잡한 동작 분포를 포착합니다. 또한 이 방법은 미래 상태 이미지와 누적 보상 값을 생성하며, 이 역시 잠재 프레임으로 인코딩되어 테스트 시 더 높은 성공률의 동작 궤적을 계획할 수 있도록 지원합니다.

### 실험 설정
- **시뮬레이션 벤치마크**: LIBERO 및 RoboCasa, 각각 작업 성공률과 일반화 능력을 평가합니다.
- **실제 세계 작업**: 도전적인 양팔 조작 작업, 실제 배포 성능을 평가합니다.
- **비교 방법**: 처음부터 훈련된 확산 정책, 비디오 기반 정책, 미세 조정된 시각-언어-동작 모델을 포함합니다.

### 주요 수치
- **LIBERO 벤치마크**: 평균 성공률 98.5%.
- **RoboCasa 벤치마크**: 평균 성공률 67.1%.
- **실제 세계 작업**: 양팔 조작 작업에서 최고 평균 점수를 기록하며 모든 비교 방법을 능가했습니다.

### 결론
Cosmos Policy는 단일 단계 미세 조정을 통해 사전 훈련된 비디오 모델을 활용하여 효율적이고 강력한 로봇 정책 학습을 구현했습니다. 아키텍처 수정이 필요 없는 특성은 배포 복잡성을 낮추고, 미래 상태와 보상 값을 생성하여 계획을 지원함으로써 작업 성공률을 크게 향상시켰습니다. 또한 이 방법은 정책 배포 데이터로부터 학습하여 세계 모델과 가치 함수를 더욱 최적화하고, 도전적인 작업에서 더 높은 성공률을 달성할 수 있습니다. 코드, 모델 및 훈련 데이터는 오픈소스로 공개되었습니다.
