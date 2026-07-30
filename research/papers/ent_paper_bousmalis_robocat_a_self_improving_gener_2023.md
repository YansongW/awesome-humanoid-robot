---
$id: ent_paper_bousmalis_robocat_a_self_improving_gener_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation'
  zh: RoboCat
  ko: 'RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation'
summary:
  en: 'RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation (RoboCat), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Google DeepMind, and published at Trans. Mach. Learn. Res. 2024.'
  zh: RoboCat 是 Google DeepMind 于 2023 年提出的多形态、多任务通用机器人操控智能体。其核心贡献在于：通过视觉目标条件决策 Transformer 架构，利用异构机器人经验实现零样本或少量样本（100-1000
    个示例）的新任务与新型机器人适应，并具备自我改进的数据生成能力。
  ko: 'RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation (RoboCat), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Google DeepMind, and published at Trans. Mach. Learn. Res. 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- robocat
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2306.11706v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: RoboCat source
  url: https://openreview.net/forum?id=vsCpILiWHu
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
RoboCat 是一种视觉目标条件决策 Transformer 模型，能够处理带有动作标签的视觉经验数据，这些数据覆盖了从仿真到真实机械臂的多种运动控制技能。该智能体通过大规模训练，展现出跨任务迁移能力，并且随着训练数据的增长和多样化，其适应新任务的效率显著提升。研究团队在仿真环境和三种不同真实机器人平台上进行了广泛评估，验证了 RoboCat 在零样本和少量样本场景下的泛化能力。

## 核心内容
### 方法架构
RoboCat 采用视觉目标条件决策 Transformer 架构，将视觉观察与目标状态作为输入，直接输出动作序列。该模型能够处理来自不同机器人平台（包括仿真和真实机械臂）的异构数据，这些数据包含不同的观测空间和动作空间。

### 训练与适应
- **初始训练**：使用大规模多任务数据集进行预训练，涵盖多种操控技能。
- **快速适应**：针对新任务或新机器人，仅需 100-1000 个目标示例即可完成微调。
- **自我改进循环**：训练后的模型可自主生成新数据，用于后续训练迭代，形成持续优化的闭环。

### 实验设置
- **仿真环境**：在多个标准机器人操控基准上进行评估。
- **真实机器人**：在三种不同形态的真实机械臂上测试，包括不同自由度、夹爪类型和传感器配置。
- **评估指标**：任务成功率、适应效率（所需样本数）和跨任务迁移效果。

### 关键结果
- **零样本泛化**：RoboCat 在未见过的任务和机器人上展现出零样本执行能力。
- **少量样本适应**：仅用 100-1000 个目标示例即可达到高成功率，且适应效率随训练数据增长而提升。
- **跨任务迁移**：随着训练数据多样性的增加，模型在相关任务间表现出正向迁移，新任务学习速度加快。
- **自我改进效果**：通过自主生成数据并重新训练，RoboCat 的性能在迭代中持续提升。

### 结论
RoboCat 证明了利用异构机器人经验构建通用操控智能体的可行性，其自我改进机制为机器人学习提供了可扩展的范式。该工作为未来开发能够持续适应新环境和新任务的通用机器人智能体奠定了基础。

## Overview
The ability to leverage heterogeneous robotic experience from different robots and tasks to quickly master novel skills and embodiments has the potential to transform robot learning. Inspired by recent advances in foundation models for vision and language, we propose a multi-embodiment, multi-task generalist agent for robotic manipulation. This agent, named RoboCat, is a visual goal-conditioned decision transformer capable of consuming action-labelled visual experience. This data spans a large repertoire of motor control skills from simulated and real robotic arms with varying sets of observations and actions. With RoboCat, we demonstrate the ability to generalise to new tasks and robots, both zero-shot as well as through adaptation using only 100-1000 examples for the target task. We also show how a trained model itself can be used to generate data for subsequent training iterations, thus providing a basic building block for an autonomous improvement loop. We investigate the agent's capabilities, with large-scale evaluations both in simulation and on three different real robot embodiments. We find that as we grow and diversify its training data, RoboCat not only shows signs of cross-task transfer, but also becomes more efficient at adapting to new tasks.

## 개요
다양한 로봇과 작업에서 얻은 이질적 로봇 경험을 활용하여 새로운 기술과 구현체를 빠르게 습득할 수 있는 능력은 로봇 학습을 혁신할 잠재력을 지니고 있습니다. 비전 및 언어 분야의 기초 모델(foundation model) 최근 발전에 영감을 받아, 우리는 로봇 조작을 위한 다중 구현체, 다중 작업 범용 에이전트를 제안합니다. 이 에이전트는 RoboCat이라 명명되었으며, 시각적 목표 조건부 결정 트랜스포머(visual goal-conditioned decision transformer)로서 행동 레이블이 지정된 시각적 경험을 소비할 수 있습니다. 이 데이터는 다양한 관찰 및 행동 세트를 가진 시뮬레이션 및 실제 로봇 팔의 광범위한 모터 제어 기술을 포괄합니다. RoboCat을 통해 우리는 새로운 작업과 로봇에 대해 제로샷(zero-shot)뿐만 아니라 대상 작업에 대해 100~1000개의 예제만 사용한 적응을 통해 일반화할 수 있는 능력을 입증합니다. 또한 훈련된 모델 자체를 후속 훈련 반복을 위한 데이터 생성에 사용할 수 있어, 자율적 개선 루프의 기본 구성 요소를 제공함을 보여줍니다. 우리는 시뮬레이션과 세 가지 다른 실제 로봇 구현체에서의 대규모 평가를 통해 에이전트의 능력을 조사합니다. 훈련 데이터를 확장하고 다양화함에 따라 RoboCat이 교차 작업 전이(cross-task transfer)의 징후를 보일 뿐만 아니라 새로운 작업에 적응하는 데 더 효율적이 된다는 것을 발견했습니다.

## 핵심 내용
다양한 로봇과 작업에서 얻은 이질적 로봇 경험을 활용하여 새로운 기술과 구현체를 빠르게 습득할 수 있는 능력은 로봇 학습을 혁신할 잠재력을 지니고 있습니다. 비전 및 언어 분야의 기초 모델 최근 발전에 영감을 받아, 우리는 로봇 조작을 위한 다중 구현체, 다중 작업 범용 에이전트를 제안합니다. 이 에이전트는 RoboCat이라 명명되었으며, 시각적 목표 조건부 결정 트랜스포머로서 행동 레이블이 지정된 시각적 경험을 소비할 수 있습니다. 이 데이터는 다양한 관찰 및 행동 세트를 가진 시뮬레이션 및 실제 로봇 팔의 광범위한 모터 제어 기술을 포괄합니다. RoboCat을 통해 우리는 새로운 작업과 로봇에 대해 제로샷뿐만 아니라 대상 작업에 대해 100~1000개의 예제만 사용한 적응을 통해 일반화할 수 있는 능력을 입증합니다. 또한 훈련된 모델 자체를 후속 훈련 반복을 위한 데이터 생성에 사용할 수 있어, 자율적 개선 루프의 기본 구성 요소를 제공함을 보여줍니다. 우리는 시뮬레이션과 세 가지 다른 실제 로봇 구현체에서의 대규모 평가를 통해 에이전트의 능력을 조사합니다. 훈련 데이터를 확장하고 다양화함에 따라 RoboCat이 교차 작업 전이의 징후를 보일 뿐만 아니라 새로운 작업에 적응하는 데 더 효율적이 된다는 것을 발견했습니다.

## 参考
- http://arxiv.org/abs/2306.11706v2
