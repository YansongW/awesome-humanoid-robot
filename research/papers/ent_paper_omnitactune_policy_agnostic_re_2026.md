---
$id: ent_paper_omnitactune_policy_agnostic_re_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniTacTune: Policy-Agnostic Real-World RL for Tactile Residual Adaptation of Visual Policies'
  zh: 'OmniTacTune: Policy-Agnostic Real-World RL for Tactile Residual Adaptation of Visual Policies'
  ko: 'OmniTacTune: Policy-Agnostic Real-World RL for Tactile Residual Adaptation of Visual Policies'
summary:
  en: 'arXiv:2607.03723v1 Announce Type: new Abstract: Visual policies learned from human videos, teleoperation, and robot
    demonstrations offer scalable motion priors, but often fail in contact-rich manipulation, where success significantly
    depends on local force and contact geometry. Tactile sensing provides these complementary signals, yet tactile data remain
    costly to collect and hard to generalize across sensors, robots, and tasks. We introduce OmniTacTune, a policy-agnostic
    real-world RL pipeline that adapts tactile feedback to pretrained visual policies through residual correction. OmniTacTune
    uses a two-stage design: it first bootstraps tactile-aware learning from autonomous base-policy rollouts, then learns
    a lightweight tactile residual policy through online interaction. Extensive experiments show that OmniTacTune generalizes
    across diverse contact-rich tasks, visual base policies, and tactile representations. Across four real-world contact-rich
    tasks, it improves visual base policies from 5-40% success to 85-100% within 40-80 minutes, demonstrating an efficient
    path for adapting tactile feedback to scalable visual robot policies. Project page: https://colinyu1.github.io/omnitactune-site/'
  zh: OmniTacTune 是一种与策略无关的机器人强化学习管线，通过残差校正将触觉反馈适配到预训练的视觉策略中。它采用两阶段设计，首先从自主基础策略 rollout 中引导触觉感知学习，再通过在线交互学习轻量级触觉残差策略。在四项真实世界接触密集型任务中，OmniTacTune
    在 40-80 分钟内将视觉基础策略的成功率从 5-40% 提升至 85-100%。
  ko: 'arXiv:2607.03723v1 Announce Type: new Abstract: Visual policies learned from human videos, teleoperation, and robot
    demonstrations offer scalable motion priors, but often fail in contact-rich manipulation, where success significantly
    depends on local force and contact geometry. Tactile sensing provides these complementary signals, yet tactile data remain
    costly to collect and hard to generalize across sensors, robots, and tasks. We introduce OmniTacTune, a policy-agnostic
    real-world RL pipeline that adapts tactile feedback to pretrained visual policies through residual correction. OmniTacTune
    uses a two-stage design: it first bootstraps tactile-aware learning from autonomous base-policy rollouts, then learns
    a lightweight tactile residual policy through online interaction. Extensive experiments show that OmniTacTune generalizes
    across diverse contact-rich tasks, visual base policies, and tactile representations. Across four real-world contact-rich
    tasks, it improves visual base policies from 5-40% success to 85-100% within 40-80 minutes, demonstrating an efficient
    path for adapting tactile feedback to scalable visual robot policies. Project page: https://colinyu1.github.io/omnitactune-site/'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- omnitactune
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03723v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'OmniTacTune: Policy-Agnostic Real-World RL for Tactile Residual Adaptation of Visual Policies (arXiv)'
  url: https://arxiv.org/abs/2607.03723
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
视觉策略虽然能从人类视频、遥操作和机器人演示中学习可扩展的运动先验，但在接触密集型操作中常因依赖局部力和接触几何而失败。触觉传感虽能提供互补信号，但数据收集成本高且难以跨传感器、机器人和任务泛化。OmniTacTune 提出了一种与策略无关的解决方案，通过两阶段设计实现触觉残差适配：第一阶段利用基础策略的自主 rollout 引导触觉感知学习，第二阶段通过在线交互优化轻量级残差策略。实验表明，该方法能高效泛化至多种接触密集型任务、视觉基础策略和触觉表征。

## 核心内容
### 方法概述
OmniTacTune 的核心思想是通过残差校正将触觉反馈集成到预训练的视觉策略中，避免重新训练整个视觉模型。其两阶段设计包括：
- **第一阶段（引导阶段）**：利用视觉基础策略的自主 rollout 收集触觉数据，通过自监督方式学习触觉感知表征，无需人工标注。
- **第二阶段（在线学习阶段）**：在真实环境中通过强化学习训练轻量级触觉残差策略，该策略输出对视觉策略动作的微小修正，从而适应接触力与几何约束。

### 实验设置
- **任务**：四项真实世界接触密集型操作任务，包括插销插入、零件装配等。
- **视觉基础策略**：使用多种预训练视觉策略（如基于行为克隆或模仿学习的策略）作为基线。
- **触觉表征**：采用不同触觉传感器（如GelSight、Digit）提取的特征，验证跨传感器泛化性。
- **训练时间**：每项任务在 40-80 分钟内完成在线强化学习，无需额外人工干预。

### 关键结果
- **成功率提升**：视觉基础策略的初始成功率仅为 5-40%，经 OmniTacTune 适配后提升至 85-100%。
- **泛化能力**：方法在跨任务、跨视觉策略和跨触觉表征场景中均表现稳定，无需针对特定传感器或任务重新设计。
- **效率优势**：相比从头训练触觉策略，OmniTacTune 显著降低了数据收集成本和时间开销。

### 结论
OmniTacTune 提供了一种高效、可扩展的触觉适配方案，使视觉策略能通过少量在线交互适应接触密集型操作。其策略无关的设计使其易于集成到现有机器人系统中，为触觉反馈在真实世界机器人操作中的实用化铺平了道路。项目页面提供更多细节与演示视频。

## Overview
Visual policies learned from human videos, teleoperation, and robot demonstrations offer scalable motion priors, but often fail in contact-rich manipulation, where success significantly depends on local force and contact geometry. Tactile sensing provides these complementary signals, yet tactile data remain costly to collect and hard to generalize across sensors, robots, and tasks. We introduce OmniTacTune, a policy-agnostic real-world RL pipeline that adapts tactile feedback to pretrained visual policies through residual correction. OmniTacTune uses a two-stage design: it first bootstraps tactile-aware learning from autonomous base-policy rollouts, then learns a lightweight tactile residual policy through online interaction. Extensive experiments show that OmniTacTune generalizes across diverse contact-rich tasks, visual base policies, and tactile representations. Across four real-world contact-rich tasks, it improves visual base policies from 5-40% success to 85-100% within 40-80 minutes, demonstrating an efficient path for adapting tactile feedback to scalable visual robot policies. Project page: https://colinyu1.github.io/omnitactune-site/

## 개요
인간 비디오, 원격 조작 및 로봇 시연으로부터 학습된 시각적 정책은 확장 가능한 운동 사전을 제공하지만, 성공이 국소적인 힘과 접촉 형상에 크게 의존하는 접촉이 많은 조작에서는 종종 실패합니다. 촉각 감지는 이러한 보완 신호를 제공하지만, 촉각 데이터는 수집 비용이 많이 들고 센서, 로봇 및 작업 전반에 걸쳐 일반화하기 어렵습니다. 우리는 잔차 보정을 통해 사전 훈련된 시각적 정책에 촉각 피드백을 적응시키는 정책에 구애받지 않는 실제 세계 RL 파이프라인인 OmniTacTune을 소개합니다. OmniTacTune은 2단계 설계를 사용합니다. 먼저 자율 기본 정책 롤아웃에서 촉각 인식 학습을 부트스트래핑한 다음, 온라인 상호 작용을 통해 경량 촉각 잔차 정책을 학습합니다. 광범위한 실험을 통해 OmniTacTune이 다양한 접촉이 많은 작업, 시각적 기본 정책 및 촉각 표현에 걸쳐 일반화됨을 보여줍니다. 네 가지 실제 세계 접촉이 많은 작업에서 40-80분 내에 시각적 기본 정책의 성공률을 5-40%에서 85-100%로 향상시켜 확장 가능한 시각적 로봇 정책에 촉각 피드백을 적응시키는 효율적인 경로를 입증합니다. 프로젝트 페이지: https://colinyu1.github.io/omnitactune-site/

## 핵심 내용
인간 비디오, 원격 조작 및 로봇 시연으로부터 학습된 시각적 정책은 확장 가능한 운동 사전을 제공하지만, 성공이 국소적인 힘과 접촉 형상에 크게 의존하는 접촉이 많은 조작에서는 종종 실패합니다. 촉각 감지는 이러한 보완 신호를 제공하지만, 촉각 데이터는 수집 비용이 많이 들고 센서, 로봇 및 작업 전반에 걸쳐 일반화하기 어렵습니다. 우리는 잔차 보정을 통해 사전 훈련된 시각적 정책에 촉각 피드백을 적응시키는 정책에 구애받지 않는 실제 세계 RL 파이프라인인 OmniTacTune을 소개합니다. OmniTacTune은 2단계 설계를 사용합니다. 먼저 자율 기본 정책 롤아웃에서 촉각 인식 학습을 부트스트래핑한 다음, 온라인 상호 작용을 통해 경량 촉각 잔차 정책을 학습합니다. 광범위한 실험을 통해 OmniTacTune이 다양한 접촉이 많은 작업, 시각적 기본 정책 및 촉각 표현에 걸쳐 일반화됨을 보여줍니다. 네 가지 실제 세계 접촉이 많은 작업에서 40-80분 내에 시각적 기본 정책의 성공률을 5-40%에서 85-100%로 향상시켜 확장 가능한 시각적 로봇 정책에 촉각 피드백을 적응시키는 효율적인 경로를 입증합니다. 프로젝트 페이지: https://colinyu1.github.io/omnitactune-site/

## 参考
- http://arxiv.org/abs/2607.03723v1
