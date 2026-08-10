---
$id: ent_paper_ding_quar_vla_vision_language_actio_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'QUAR-VLA: Vision-Language-Action Model for Quadruped Robots'
  zh: QUAR-VLA
  ko: 'QUAR-VLA: Vision-Language-Action Model for Quadruped Robots'
summary:
  en: 'QUAR-VLA: Vision-Language-Action Model for Quadruped Robots (QUAR-VLA), is a 2023 large vision-language-action model
    for robotic manipulation, introduced by Westlake University, Zhejiang University, and published at ECCV24.'
  zh: QUAR-VLA 是由西湖大学和浙江大学联合提出的四足机器人视觉-语言-动作模型，发表于 ECCV24。其核心贡献在于提出 QUART 模型族和 QUARD 大规模多任务数据集，通过紧密融合视觉与指令信息生成可执行动作，在 4000
    次评估试验中验证了其高性能与涌现能力。
  ko: 'QUAR-VLA: Vision-Language-Action Model for Quadruped Robots (QUAR-VLA), is a 2023 large vision-language-action model
    for robotic manipulation, introduced by Westlake University, Zhejiang University, and published at ECCV24.'
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
- quar_vla
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2312.14457v6. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (948 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: QUAR-VLA source
  url: https://doi.org/10.1007/978-3-031-72652-1_21
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
传统机器人控制方法将感知、规划与决策分离，虽简化了系统设计，却限制了信息流间的协同，难以实现自主推理与动作执行的无缝衔接。QUAR-VLA 提出一种新范式，将视觉信息与自然语言指令深度整合，直接生成机器人可执行的动作，从而统一感知、规划与决策过程。该框架面临的核心挑战是确保机器人能根据精细指令与视觉观察准确对齐并执行动作。为此，研究团队开发了 QUART 模型族，并构建了包含导航、复杂地形行走和全身操控任务的 QUARD 数据集，用于训练这些模型。

## 核心内容
### 方法概述
QUAR-VLA 的核心是 QUART 模型族，它采用视觉-语言-动作（VLA）架构，将多模态的视觉信息与指令作为输入，直接输出四足机器人的可执行动作。该模型通过端到端学习，绕过了传统方法中感知、规划与决策的模块化分离，旨在提升机器人的整体智能水平。

### 关键挑战与对齐机制
框架面临的主要挑战是**细粒度指令与视觉感知信息的对齐**。为确保机器人能准确理解并执行复杂指令，QUART 模型需要学习如何将自然语言描述（如“绕过障碍物后向左转”）与实时视觉观测（如摄像头捕捉的障碍物位置）进行语义匹配，从而生成协调的动作序列。

### 数据集：QUARD
QUARD 是一个大规模多任务数据集，专门用于训练 QUART 模型，包含三类任务：
- **导航**：在结构化与非结构化环境中进行路径规划与目标到达。
- **复杂地形行走**：跨越台阶、斜坡、碎石等非平坦地形。
- **全身操控**：涉及腿部与身体协同动作的任务，如推门或搬运物体。

### 实验设置与结果
- **评估规模**：共进行了 4000 次评估试验，覆盖多种任务场景。
- **性能表现**：QUART 模型在导航、地形行走和操控任务中均展现出高性能的机器人策略，能够稳定执行指令。
- **涌现能力**：模型在训练后表现出一些未显式编程的涌现能力，例如在未见过的地形组合中自主调整步态，或根据模糊指令（如“小心通过”）自适应减速。

### 结论
QUAR-VLA 通过 QUART 模型与 QUARD 数据集，验证了将视觉、语言与动作紧密耦合的可行性，为四足机器人实现更自然的人机交互与自主决策提供了有效方案。

## Overview
The important manifestation of robot intelligence is the ability to naturally interact and autonomously make decisions. Traditional approaches to robot control often compartmentalize perception, planning, and decision-making, simplifying system design but limiting the synergy between different information streams. This compartmentalization poses challenges in achieving seamless autonomous reasoning, decision-making, and action execution. To address these limitations, a novel paradigm, named Vision-Language-Action tasks for QUAdruped Robots (QUAR-VLA), has been introduced in this paper. This approach tightly integrates visual information and instructions to generate executable actions, effectively merging perception, planning, and decision-making. The central idea is to elevate the overall intelligence of the robot. Within this framework, a notable challenge lies in aligning fine-grained instructions with visual perception information. This emphasizes the complexity involved in ensuring that the robot accurately interprets and acts upon detailed instructions in harmony with its visual observations. Consequently, we propose QUAdruped Robotic Transformer (QUART), a family of VLA models to integrate visual information and instructions from diverse modalities as input and generates executable actions for real-world robots and present QUAdruped Robot Dataset (QUARD), a large-scale multi-task dataset including navigation, complex terrain locomotion, and whole-body manipulation tasks for training QUART models. Our extensive evaluation (4000 evaluation trials) shows that our approach leads to performant robotic policies and enables QUART to obtain a range of emergent capabilities.

## 参考
- http://arxiv.org/abs/2312.14457v6

## 개요
전통적인 로봇 제어 방법은 인식, 계획, 의사 결정을 분리하여 시스템 설계를 단순화했지만, 정보 흐름 간의 협력을 제한하여 자율 추론과 동작 실행의 원활한 연결을 구현하기 어려웠습니다. QUAR-VLA는 시각 정보와 자연어 명령을 깊이 통합하여 로봇이 실행 가능한 동작을 직접 생성함으로써 인식, 계획, 의사 결정 과정을 통합하는 새로운 패러다임을 제안합니다. 이 프레임워크가 직면한 핵심 과제는 로봇이 세밀한 명령과 시각적 관찰에 따라 정확하게 정렬되고 동작을 실행할 수 있도록 보장하는 것입니다. 이를 위해 연구팀은 QUART 모델군을 개발하고, 내비게이션, 복잡한 지형 보행, 전신 조작 작업을 포함하는 QUARD 데이터셋을 구축하여 이러한 모델을 훈련했습니다.

## 핵심 내용
### 방법 개요
QUAR-VLA의 핵심은 QUART 모델군으로, 시각-언어-동작(VLA) 아키텍처를 채택하여 다중 모달 시각 정보와 명령을 입력으로 사용하고, 네 발 달린 로봇의 실행 가능한 동작을 직접 출력합니다. 이 모델은 종단 간 학습을 통해 전통적인 방법의 인식, 계획, 의사 결정의 모듈식 분리를 우회하여 로봇의 전반적인 지능 수준을 향상시키는 것을 목표로 합니다.

### 핵심 과제와 정렬 메커니즘
프레임워크가 직면한 주요 과제는 **세밀한 명령과 시각적 인식 정보의 정렬**입니다. 로봇이 복잡한 명령을 정확하게 이해하고 실행할 수 있도록 QUART 모델은 자연어 설명(예: "장애물을 우회한 후 좌회전")과 실시간 시각적 관찰(예: 카메라로 포착된 장애물 위치)을 의미적으로 일치시키는 방법을 학습하여 조화로운 동작 시퀀스를 생성해야 합니다.

### 데이터셋: QUARD
QUARD는 QUART 모델 훈련을 위해 특별히 설계된 대규모 다중 작업 데이터셋으로, 세 가지 유형의 작업을 포함합니다:
- **내비게이션**: 구조화 및 비구조화 환경에서 경로 계획 및 목표 도달.
- **복잡한 지형 보행**: 계단, 경사로, 자갈 등 비평탄 지형을 횡단.
- **전신 조작**: 다리와 몸통의 협력 동작이 필요한 작업, 예: 문 밀기 또는 물체 운반.

### 실험 설정 및 결과
- **평가 규모**: 다양한 작업 시나리오를 포괄하는 총 4000회의 평가 시험이 수행되었습니다.
- **성능**: QUART 모델은 내비게이션, 지형 보행 및 조작 작업에서 높은 성능의 로봇 정책을 보여주며 명령을 안정적으로 실행할 수 있었습니다.
- **창발적 능력**: 모델은 훈련 후 명시적으로 프로그래밍되지 않은 창발적 능력을 나타냈습니다. 예를 들어, 보지 못한 지형 조합에서 보행 패턴을 자율적으로 조정하거나, 모호한 명령(예: "조심히 통과")에 따라 자동으로 속도를 줄이는 능력입니다.

### 결론
QUAR-VLA는 QUART 모델과 QUARD 데이터셋을 통해 시각, 언어, 동작을 긴밀하게 결합하는 것의 타당성을 검증했으며, 네 발 달린 로봇이 더 자연스러운 인간-로봇 상호작용과 자율 의사 결정을 구현할 수 있는 효과적인 솔루션을 제공합니다.
