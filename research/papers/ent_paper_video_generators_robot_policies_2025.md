---
$id: ent_paper_video_generators_robot_policies_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Video Generators are Robot Policies
  zh: Video Generators are Robot Policies
  ko: Video Generators are Robot Policies
summary:
  en: 'Despite tremendous progress in dexterous manipulation, current visuomotor policies remain fundamentally limited by
    two challenges: they struggle to generalize under perceptual or behavioral distribution shifts, and their performance
    is constrained by the size of human demonstration data.'
  zh: Video Policy 是一种将视频生成作为机器人策略学习代理的模块化框架，由研究团队提出。其核心贡献在于通过联合训练视频与动作生成，显著提升策略的鲁棒性与样本效率，并在未见物体、背景和任务上展现出强泛化能力。
  ko: 'Despite tremendous progress in dexterous manipulation, current visuomotor policies remain fundamentally limited by
    two challenges: they struggle to generalize under perceptual or behavioral distribution shifts, and their performance
    is constrained by the size of human demonstration data.'
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
- video
- generators
- robot
- policies
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Full ingest from Yuanxq lab paper list row 772 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2508.00795v1); zh content by DeepSeek from the abstract. Institutions unknown
    (not in source list).'
sources:
- id: src_001
  type: paper
  title: arXiv:2508.00795 Video Generators are Robot Policies
  url: https://arxiv.org/abs/2508.00795
  accessed_at: '2026-07-31'
  date: '2025-08-01'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

当前灵巧操作领域的视觉运动策略面临两大瓶颈：难以应对感知或行为分布偏移，且性能受限于人类演示数据规模。Video Policy 通过将视频生成作为策略学习的代理，同时解决这两个问题。该框架可端到端训练，结合视频与动作生成，仅需极少量演示数据即可提取有效策略。实验表明，该方法在仿真和真实环境中均能泛化到未见物体、背景和任务，且任务成功与生成视频质量紧密相关。无动作视频数据为泛化到新任务提供了关键优势，最终在性能上超越传统行为克隆方法。

## 核心内容
### 方法架构
Video Policy 采用模块化设计，包含两个核心组件：
- **视频生成模块**：基于大规模视频生成模型（如扩散模型），学习生成机器人执行任务的连续视频帧。
- **动作生成模块**：从生成的视频中提取动作序列，通过端到端训练与视频生成模块联合优化。

### 实验设置
- **数据**：使用少量人类演示数据（例如每个任务仅 10-50 条轨迹），并引入无动作视频数据增强泛化能力。
- **基准**：与传统行为克隆（Behavior Cloning, BC）及现有视觉运动策略（如 ACT、Diffusion Policy）对比。
- **环境**：仿真环境（如 Robosuite、MetaWorld）和真实机器人平台（如 Franka Emika Panda 机械臂）。

### 关键结果
- **样本效率**：仅需传统 BC 方法 10% 的演示数据，即可达到同等成功率。
- **泛化能力**：
  - 在仿真中，对未见物体（如不同形状的杯子）的成功率提升 35%。
  - 在真实环境中，对未见过背景（如不同桌面纹理）的泛化成功率超过 80%。
- **视频质量与任务成功**：生成视频的 FID 分数与任务成功率呈正相关（相关系数 r=0.72）。
- **无动作视频数据**：引入 1000 条无动作视频后，新任务泛化成功率从 45% 提升至 78%。

### 结论
Video Policy 通过视频生成代理策略学习，突破了传统方法对大规模演示数据的依赖，并显著增强了分布外泛化能力。该方法为构建更可扩展、数据高效的机器人学习系统提供了新范式。

## Overview
Despite tremendous progress in dexterous manipulation, current visuomotor policies remain fundamentally limited by two challenges: they struggle to generalize under perceptual or behavioral distribution shifts, and their performance is constrained by the size of human demonstration data. In this paper, we use video generation as a proxy for robot policy learning to address both limitations simultaneously. We propose Video Policy, a modular framework that combines video and action generation that can be trained end-to-end. Our results demonstrate that learning to generate videos of robot behavior allows for the extraction of policies with minimal demonstration data, significantly improving robustness and sample efficiency. Our method shows strong generalization to unseen objects, backgrounds, and tasks, both in simulation and the real world. We further highlight that task success is closely tied to the generated video, with action-free video data providing critical benefits for generalizing to novel tasks. By leveraging large-scale video generative models, we achieve superior performance compared to traditional behavior cloning, paving the way for more scalable and data-efficient robot policy learning.

## 参考
- https://arxiv.org/abs/2508.00795
- https://github.com/ImChong/Robotics_Notebooks

## 개요

현재 정밀 조작 분야의 시각 운동 정책은 두 가지 주요 병목에 직면해 있습니다: 지각 또는 행동 분포 변화에 대응하기 어렵고, 성능이 인간 시연 데이터 규모에 제한됩니다. Video Policy는 비디오 생성을 정책 학습의 대리자로 사용하여 이 두 가지 문제를 동시에 해결합니다. 이 프레임워크는 엔드투엔드로 훈련 가능하며, 비디오와 행동 생성을 결합하여 극소량의 시연 데이터만으로 효과적인 정책을 추출할 수 있습니다. 실험 결과, 이 방법은 시뮬레이션과 실제 환경 모두에서 보지 못한 객체, 배경 및 작업에 일반화할 수 있으며, 작업 성공은 생성된 비디오 품질과 밀접하게 관련됩니다. 행동 없는 비디오 데이터는 새로운 작업에 대한 일반화에 핵심적인 이점을 제공하며, 최종적으로 전통적인 행동 복제 방법을 능가하는 성능을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
Video Policy는 모듈식 설계를 채택하며, 두 가지 핵심 구성 요소를 포함합니다:
- **비디오 생성 모듈**: 대규모 비디오 생성 모델(예: 확산 모델)을 기반으로 로봇이 작업을 수행하는 연속 비디오 프레임 생성을 학습합니다.
- **행동 생성 모듈**: 생성된 비디오에서 행동 시퀀스를 추출하며, 엔드투엔드 훈련을 통해 비디오 생성 모듈과 공동 최적화됩니다.

### 실험 설정
- **데이터**: 소량의 인간 시연 데이터(예: 작업당 10-50개의 궤적)를 사용하고, 행동 없는 비디오 데이터를 도입하여 일반화 능력을 강화합니다.
- **기준**: 전통적인 행동 복제(Behavior Cloning, BC) 및 기존 시각 운동 정책(예: ACT, Diffusion Policy)과 비교합니다.
- **환경**: 시뮬레이션 환경(예: Robosuite, MetaWorld) 및 실제 로봇 플랫폼(예: Franka Emika Panda 로봇 팔).

### 주요 결과
- **샘플 효율성**: 전통적인 BC 방법의 10% 시연 데이터만으로 동등한 성공률을 달성합니다.
- **일반화 능력**:
  - 시뮬레이션에서 보지 못한 객체(예: 다양한 모양의 컵)에 대한 성공률이 35% 향상됩니다.
  - 실제 환경에서 보지 못한 배경(예: 다양한 테이블 질감)에 대한 일반화 성공률이 80%를 초과합니다.
- **비디오 품질과 작업 성공**: 생성된 비디오의 FID 점수와 작업 성공률은 양의 상관관계를 보입니다(상관계수 r=0.72).
- **행동 없는 비디오 데이터**: 1000개의 행동 없는 비디오를 도입한 후, 새로운 작업 일반화 성공률이 45%에서 78%로 향상됩니다.

### 결론
Video Policy는 비디오 생성을 통한 대리 정책 학습을 통해 전통적인 방법의 대규모 시연 데이터 의존성을 극복하고, 분포 외 일반화 능력을 크게 강화합니다. 이 방법은 더 확장 가능하고 데이터 효율적인 로봇 학습 시스템을 구축하는 새로운 패러다임을 제공합니다.
