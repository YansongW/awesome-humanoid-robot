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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2306.11706v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (911 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2306.11706v2

## 개요
RoboCat은 시각적 목표 조건부 결정 트랜스포머 모델로, 시뮬레이션부터 실제 로봇 팔까지 다양한 운동 제어 기술을 포괄하는 행동 레이블이 있는 시각적 경험 데이터를 처리할 수 있습니다. 이 에이전트는 대규모 훈련을 통해 작업 간 전이 능력을 보여주며, 훈련 데이터가 증가하고 다양해질수록 새로운 작업에 적응하는 효율성이 크게 향상됩니다. 연구팀은 시뮬레이션 환경과 세 가지 서로 다른 실제 로봇 플랫폼에서 광범위한 평가를 수행하여 RoboCat의 제로샷 및 소수 샘플 시나리오에서의 일반화 능력을 검증했습니다.

## 핵심 내용
### 방법 아키텍처
RoboCat은 시각적 목표 조건부 결정 트랜스포머 아키텍처를 채택하여 시각적 관찰과 목표 상태를 입력으로 받아 직접 행동 시퀀스를 출력합니다. 이 모델은 서로 다른 관찰 공간과 행동 공간을 포함하는 다양한 로봇 플랫폼(시뮬레이션 및 실제 로봇 팔 포함)의 이질적 데이터를 처리할 수 있습니다.

### 훈련 및 적응
- **초기 훈련**: 대규모 다중 작업 데이터 세트를 사용한 사전 훈련으로 다양한 조작 기술을 포괄합니다.
- **빠른 적응**: 새로운 작업이나 로봇에 대해 100-1000개의 목표 예제만으로 미세 조정이 가능합니다.
- **자기 개선 루프**: 훈련된 모델은 자율적으로 새 데이터를 생성하여 후속 훈련 반복에 사용함으로써 지속적인 최적화의 폐쇄 루프를 형성합니다.

### 실험 설정
- **시뮬레이션 환경**: 여러 표준 로봇 조작 벤치마크에서 평가를 수행합니다.
- **실제 로봇**: 서로 다른 자유도, 그리퍼 유형 및 센서 구성을 포함한 세 가지 형태의 실제 로봇 팔에서 테스트합니다.
- **평가 지표**: 작업 성공률, 적응 효율성(필요한 샘플 수) 및 작업 간 전이 효과.

### 주요 결과
- **제로샷 일반화**: RoboCat은 본 적 없는 작업과 로봇에서 제로샷 실행 능력을 보여줍니다.
- **소수 샘플 적응**: 100-1000개의 목표 예제만으로 높은 성공률에 도달하며, 적응 효율성은 훈련 데이터 증가에 따라 향상됩니다.
- **작업 간 전이**: 훈련 데이터 다양성이 증가함에 따라 모델은 관련 작업 간 긍정적 전이를 보여주며, 새로운 작업 학습 속도가 빨라집니다.
- **자기 개선 효과**: 자율적으로 데이터를 생성하고 재훈련함으로써 RoboCat의 성능은 반복 과정에서 지속적으로 향상됩니다.

### 결론
RoboCat은 이질적 로봇 경험을 활용하여 범용 조작 에이전트를 구축하는 가능성을 입증했으며, 자기 개선 메커니즘은 로봇 학습에 확장 가능한 패러다임을 제공합니다. 이 연구는 향후 새로운 환경과 작업에 지속적으로 적응할 수 있는 범용 로봇 에이전트 개발의 기초를 마련합니다.
