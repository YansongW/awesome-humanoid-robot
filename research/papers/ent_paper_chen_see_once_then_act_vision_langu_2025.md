---
$id: ent_paper_chen_see_once_then_act_vision_langu_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'See Once, Then Act: Vision-Language-Action Model with Task Learning from One-Shot Video Demonstrations'
  zh: ViVLA
  ko: 'See Once, Then Act: Vision-Language-Action Model with Task Learning from One-Shot Video Demonstrations'
summary:
  en: 'See Once, Then Act: Vision-Language-Action Model with Task Learning from One-Shot Video Demonstrations (ViVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Beijing Institute of Technology, LimX
    Dynamics.'
  zh: ViVLA 是一个由北京理工大学与 LimX Dynamics 于 2025 年提出的大型视觉-语言-动作模型，用于机器人操作。其核心贡献在于仅需一段专家演示视频，即可在测试时让机器人学会新任务，无需额外训练。在 LIBERO 基准上，ViVLA
    对未见任务实现了超过 30% 的性能提升，跨实体演示下增益保持在 35% 以上，真实世界实验中从人类视频学习的效果提升超过 38%。
  ko: 'See Once, Then Act: Vision-Language-Action Model with Task Learning from One-Shot Video Demonstrations (ViVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Beijing Institute of Technology, LimX
    Dynamics.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- vision_language_action
- vivla
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.07582v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'See Once, Then Act: Vision-Language-Action Model with Task Learning from One-Shot Video Demonstrations (arXiv)'
  url: https://arxiv.org/abs/2512.07582
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ViVLA source
  url: https://doi.org/10.48550/arXiv.2512.07582
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
ViVLA 旨在解决现有 VLA 模型泛化能力有限的问题，通过模仿人类“看一次就会”的能力，实现从单段专家演示视频中高效学习新操作技能。该模型同时处理专家演示视频与机器人自身视觉观测，预测演示动作序列与后续机器人动作，从而将专家行为中的细粒度操作知识蒸馏并迁移至智能体。为提升性能，研究团队开发了可扩展的专家-智能体对数据生成流水线，能从易获取的人类视频中合成配对轨迹，并结合公开数据集进行扩充，最终生成 892,911 个训练样本。实验表明，ViVLA 在未见任务上表现优异，且能有效处理跨实体与真实世界场景。

## 核心内容
### 方法
ViVLA 的核心架构基于视觉-语言-动作模型，其输入包括：
- 一段专家演示视频（单次任务执行）
- 机器人当前视觉观测（如摄像头图像）
- 任务描述（自然语言指令）

模型通过联合编码上述输入，输出两个关键预测：
1. 演示视频中的动作序列（用于对齐专家行为）
2. 机器人后续应执行的动作（用于实际控制）

这种设计使得 ViVLA 能够从专家行为中提取细粒度操作知识，并直接迁移至智能体，无需微调或额外训练。

### 数据生成流水线
为训练 ViVLA，研究团队构建了可扩展的专家-智能体对数据生成流程：
- 从易获取的人类视频中，通过自动标注与轨迹合成，生成配对数据
- 结合公开数据集（如 LIBERO）中的高质量操作轨迹
- 最终数据集包含 **892,911** 个专家-智能体样本，覆盖多种操作场景

### 实验设置与结果
ViVLA 在以下场景中进行了评估：

- **LIBERO 基准测试**：
  - 对未见任务（unseen tasks），ViVLA 相比基线模型实现 **超过 30%** 的成功率提升
  - 当使用跨实体（cross-embodiment）演示视频时，增益保持在 **35% 以上**

- **真实世界实验**：
  - 从人类演示视频中学习，ViVLA 在未见任务上取得 **超过 38%** 的性能提升
  - 验证了模型从非机器人视频中迁移操作知识的能力

### 结论
ViVLA 展示了从单段视频演示中高效学习新操作技能的潜力，显著提升了 VLA 模型的泛化能力。其数据生成流水线为未来研究提供了可复用的框架，尤其适用于跨实体与真实世界场景。

## Overview
Developing robust and general-purpose manipulation policies represents a fundamental objective in robotics research. While Vision-Language-Action (VLA) models have demonstrated promising capabilities for end-to-end robot control, existing approaches still exhibit limited generalization to tasks beyond their training distributions. In contrast, humans possess remarkable proficiency in acquiring novel skills by simply observing others performing them once. Inspired by this capability, we propose ViVLA, a generalist robotic manipulation policy that achieves efficient task learning from a single expert demonstration video at test time. Our approach jointly processes an expert demonstration video alongside the robot's visual observations to predict both the demonstrated action sequences and subsequent robot actions, effectively distilling fine-grained manipulation knowledge from expert behavior and transferring it seamlessly to the agent. To enhance the performance of ViVLA, we develop a scalable expert-agent pair data generation pipeline capable of synthesizing paired trajectories from easily accessible human videos, further augmented by curated pairs from publicly available datasets. This pipeline produces a total of 892,911 expert-agent samples for training ViVLA. Experimental results demonstrate that our ViVLA is able to acquire novel manipulation skills from only a single expert demonstration video at test time. Our approach achieves over 30% improvement on unseen LIBERO tasks and maintains above 35% gains with cross-embodiment videos. Real-world experiments demonstrate effective learning from human videos, yielding more than 38% improvement on unseen tasks.

## 개요
강건하고 범용적인 조작 정책을 개발하는 것은 로봇 공학 연구의 근본적인 목표입니다. Vision-Language-Action(VLA) 모델은 엔드투엔드 로봇 제어에서 유망한 능력을 보여주었지만, 기존 접근 방식은 훈련 분포를 벗어난 작업에 대한 일반화가 여전히 제한적입니다. 반면, 인간은 다른 사람이 한 번 수행하는 것을 관찰하는 것만으로 새로운 기술을 습득하는 놀라운 능력을 가지고 있습니다. 이러한 능력에 영감을 받아, 우리는 테스트 시점에 단일 전문가 시연 비디오만으로 효율적인 작업 학습을 달성하는 범용 로봇 조작 정책인 ViVLA를 제안합니다. 우리의 접근 방식은 전문가 시연 비디오와 로봇의 시각적 관찰을 함께 처리하여 시연된 행동 시퀀스와 후속 로봇 행동을 모두 예측함으로써, 전문가 행동에서 세분화된 조작 지식을 효과적으로 추출하고 이를 에이전트에 원활하게 전이합니다. ViVLA의 성능을 향상시키기 위해, 우리는 쉽게 접근 가능한 인간 비디오에서 쌍을 이룬 궤적을 합성할 수 있는 확장 가능한 전문가-에이전트 쌍 데이터 생성 파이프라인을 개발하고, 공개 데이터셋에서 선별된 쌍으로 추가 보강했습니다. 이 파이프라인은 ViVLA 훈련을 위해 총 892,911개의 전문가-에이전트 샘플을 생성합니다. 실험 결과는 ViVLA가 테스트 시점에 단일 전문가 시연 비디오만으로 새로운 조작 기술을 습득할 수 있음을 보여줍니다. 우리의 접근 방식은 보지 못한 LIBERO 작업에서 30% 이상의 개선을 달성하고, 교차 체현 비디오에서도 35% 이상의 이득을 유지합니다. 실제 환경 실험은 인간 비디오로부터의 효과적인 학습을 입증하며, 보지 못한 작업에서 38% 이상의 개선을 보여줍니다.

## 핵심 내용
강건하고 범용적인 조작 정책을 개발하는 것은 로봇 공학 연구의 근본적인 목표입니다. Vision-Language-Action(VLA) 모델은 엔드투엔드 로봇 제어에서 유망한 능력을 보여주었지만, 기존 접근 방식은 훈련 분포를 벗어난 작업에 대한 일반화가 여전히 제한적입니다. 반면, 인간은 다른 사람이 한 번 수행하는 것을 관찰하는 것만으로 새로운 기술을 습득하는 놀라운 능력을 가지고 있습니다. 이러한 능력에 영감을 받아, 우리는 테스트 시점에 단일 전문가 시연 비디오만으로 효율적인 작업 학습을 달성하는 범용 로봇 조작 정책인 ViVLA를 제안합니다. 우리의 접근 방식은 전문가 시연 비디오와 로봇의 시각적 관찰을 함께 처리하여 시연된 행동 시퀀스와 후속 로봇 행동을 모두 예측함으로써, 전문가 행동에서 세분화된 조작 지식을 효과적으로 추출하고 이를 에이전트에 원활하게 전이합니다. ViVLA의 성능을 향상시키기 위해, 우리는 쉽게 접근 가능한 인간 비디오에서 쌍을 이룬 궤적을 합성할 수 있는 확장 가능한 전문가-에이전트 쌍 데이터 생성 파이프라인을 개발하고, 공개 데이터셋에서 선별된 쌍으로 추가 보강했습니다. 이 파이프라인은 ViVLA 훈련을 위해 총 892,911개의 전문가-에이전트 샘플을 생성합니다. 실험 결과는 ViVLA가 테스트 시점에 단일 전문가 시연 비디오만으로 새로운 조작 기술을 습득할 수 있음을 보여줍니다. 우리의 접근 방식은 보지 못한 LIBERO 작업에서 30% 이상의 개선을 달성하고, 교차 체현 비디오에서도 35% 이상의 이득을 유지합니다. 실제 환경 실험은 인간 비디오로부터의 효과적인 학습을 입증하며, 보지 못한 작업에서 38% 이상의 개선을 보여줍니다.

## 参考
- http://arxiv.org/abs/2512.07582v1
