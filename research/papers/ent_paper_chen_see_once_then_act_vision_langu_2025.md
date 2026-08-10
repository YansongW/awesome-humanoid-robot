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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.07582v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (983 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2512.07582v1

## 개요
ViVLA는 기존 VLA 모델의 일반화 능력이 제한적인 문제를 해결하고자, 인간의 "한 번 보면 바로 배우는" 능력을 모방하여 단일 전문가 시연 비디오에서 새로운 조작 기술을 효율적으로 학습하는 것을 목표로 합니다. 이 모델은 전문가 시연 비디오와 로봇 자체의 시각적 관측을 동시에 처리하여, 시연 동작 시퀀스와 후속 로봇 동작을 예측함으로써 전문가 행동의 세밀한 조작 지식을 추출하여 에이전트로 전이합니다. 성능을 향상시키기 위해 연구팀은 확장 가능한 전문가-에이전트 쌍 데이터 생성 파이프라인을 개발했으며, 이는 쉽게 얻을 수 있는 인간 비디오에서 쌍을 이루는 궤적을 합성하고 공개 데이터셋을 결합하여 확장함으로써 최종적으로 892,911개의 훈련 샘플을 생성합니다. 실험 결과, ViVLA는 보지 못한 작업에서 우수한 성능을 보였으며, 교차 엔티티 및 실제 세계 시나리오를 효과적으로 처리할 수 있음을 입증했습니다.

## 핵심 내용
### 방법
ViVLA의 핵심 아키텍처는 비전-언어-동작 모델을 기반으로 하며, 입력은 다음과 같습니다:
- 전문가 시연 비디오 한 개 (단일 작업 실행)
- 로봇의 현재 시각적 관측 (예: 카메라 이미지)
- 작업 설명 (자연어 명령)

모델은 위 입력을 공동으로 인코딩하여 두 가지 핵심 예측을 출력합니다:
1. 시연 비디오의 동작 시퀀스 (전문가 행동 정렬용)
2. 로봇이 이후에 실행해야 할 동작 (실제 제어용)

이 설계 덕분에 ViVLA는 전문가 행동에서 세밀한 조작 지식을 추출하여 에이전트로 직접 전이할 수 있으며, 미세 조정이나 추가 훈련이 필요 없습니다.

### 데이터 생성 파이프라인
ViVLA를 훈련시키기 위해 연구팀은 확장 가능한 전문가-에이전트 쌍 데이터 생성 프로세스를 구축했습니다:
- 쉽게 얻을 수 있는 인간 비디오에서 자동 주석 및 궤적 합성을 통해 쌍 데이터 생성
- 공개 데이터셋 (예: LIBERO)의 고품질 조작 궤적 결합
- 최종 데이터셋은 **892,911**개의 전문가-에이전트 샘플을 포함하며, 다양한 조작 시나리오를 포괄합니다

### 실험 설정 및 결과
ViVLA는 다음 시나리오에서 평가되었습니다:

- **LIBERO 벤치마크 테스트**:
  - 보지 못한 작업(unseen tasks)에서 ViVLA는 기준 모델 대비 **30% 이상**의 성공률 향상을 달성
  - 교차 엔티티(cross-embodiment) 시연 비디오를 사용할 때, 향상 폭은 **35% 이상** 유지

- **실제 세계 실험**:
  - 인간 시연 비디오에서 학습한 ViVLA는 보지 못한 작업에서 **38% 이상**의 성능 향상을 기록
  - 비로봇 비디오에서 조작 지식을 전이하는 모델의 능력을 검증

### 결론
ViVLA는 단일 비디오 시연에서 새로운 조작 기술을 효율적으로 학습할 수 있는 잠재력을 보여주며, VLA 모델의 일반화 능력을 크게 향상시켰습니다. 이 데이터 생성 파이프라인은 향후 연구, 특히 교차 엔티티 및 실제 세계 시나리오에 재사용 가능한 프레임워크를 제공합니다.
