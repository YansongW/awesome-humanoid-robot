---
$id: ent_paper_aktas_correspondence_learning_betwee_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Correspondence learning between morphologically different robots via task demonstrations
  zh: 基于任务演示的形态不同机器人之间的对应关系学习
  ko: 작업 시연을 통한 형태학적으로 다른 로봇 간 대응 관계 학습
summary:
  en: Proposes a correspondence-learning framework that trains separate Conditional Neural Movement Primitives for each robot
    and blends their latent codes through a learned convex combination, enabling zero-shot trajectory generation across morphologically
    different robots from a single task demonstration.
  zh: 本文提出一种跨形态机器人对应学习框架，通过为每个机器人训练独立的Conditional Neural Movement Primitives，并利用学习到的凸组合融合其潜在编码，实现从单一任务演示到形态不同机器人的零样本轨迹生成。该工作由研究团队完成，核心贡献在于无需重新训练即可将技能迁移至不同形态机器人。
  ko: 각 로봇에 대해 개별적인 조건적 신경 운동 기본형을 학습하고 학습된 볼록 조합을 통해 잠재 코드를 혼합하여, 단일 작업 시연으로 형태학적으로 다른 로봇 간 제로샷 궤적 생성을 가능하게 하는 대응 관계 학습 프레임워크를
    제안한다.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- skill_transfer
- correspondence_learning
- conditional_neural_movement_primitives
- zero_shot_learning
- morphological_differences
- latent_representation
- imitation_learning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2310.13458v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (996 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Correspondence learning between morphologically different robots via task demonstrations
  url: https://arxiv.org/abs/2310.13458
  date: '2023'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
针对机器人形态多样导致技能重复训练效率低下的问题，本文提出一种基于任务演示的对应学习方法。该方法首先让不同形态机器人执行相同基准任务，然后为每个机器人独立训练条件神经运动基元，并通过学习凸组合将它们的潜在编码融合。训练完成后，仅需观察一个机器人执行新任务，即可自动生成其他机器人完成相同任务的轨迹。实验验证了该方法在三种场景下的有效性：机器人需遵循相同路径、不同路径以及不同复杂度轨迹完成任务。此外，还实现了真实机械臂与仿真移动机器人之间的对应学习概念验证。

## 核心内容
### 方法架构
- **核心框架**：为每个机器人训练独立的Conditional Neural Movement Primitives（cNMP），通过可学习的凸组合（convex combination）融合各机器人的潜在编码（latent codes），实现跨形态零样本轨迹生成。
- **训练流程**：
  1. 让所有机器人执行同一基准任务（如到达目标点），收集演示数据。
  2. 联合学习一个共享潜在空间（common latent representation）和每个机器人的独立策略。
  3. 训练完成后，输入一个机器人的新任务演示，通过潜在空间映射自动生成其他机器人的对应轨迹。

### 实验设置
- **机器人类型**：固定基座关节控制机械臂（fixed-based manipulator）与差速驱动移动机器人（differential drive mobile robot），验证了不同形态（不同自由度、不同控制方式）的对应学习。
- **三种实验场景**：
  1. **相同路径**：所有机器人需沿相同几何路径完成任务。
  2. **不同路径**：机器人需采用不同轨迹但达成相同任务目标。
  3. **不同复杂度**：各机器人所需传感器-运动轨迹的复杂度不同。
- **真实-仿真验证**：在真实机械臂与仿真移动机器人之间实现了对应学习的概念验证（proof-of-concept）。

### 关键结论
- 该方法成功实现了从单一任务演示到不同形态机器人的零样本轨迹生成，无需重新训练。
- 在三种实验场景下均有效，尤其适用于形态差异较大的机器人（如机械臂与移动机器人）。
- 潜在空间融合策略（凸组合）能够有效捕捉不同机器人运动模式的共性，同时保留个体差异。

## Overview
We observe a large variety of robots in terms of their bodies, sensors, and actuators. Given the commonalities in the skill sets, teaching each skill to each different robot independently is inefficient and not scalable when the large variety in the robotic landscape is considered. If we can learn the correspondences between the sensorimotor spaces of different robots, we can expect a skill that is learned in one robot can be more directly and easily transferred to other robots. In this paper, we propose a method to learn correspondences among two or more robots that may have different morphologies. To be specific, besides robots with similar morphologies with different degrees of freedom, we show that a fixed-based manipulator robot with joint control and a differential drive mobile robot can be addressed within the proposed framework. To set up the correspondence among the robots considered, an initial base task is demonstrated to the robots to achieve the same goal. Then, a common latent representation is learned along with the individual robot policies for achieving the goal. After the initial learning stage, the observation of a new task execution by one robot becomes sufficient to generate a latent space representation pertaining to the other robots to achieve the same task. We verified our system in a set of experiments where the correspondence between robots is learned (1) when the robots need to follow the same paths to achieve the same task, (2) when the robots need to follow different trajectories to achieve the same task, and (3) when complexities of the required sensorimotor trajectories are different for the robots. We also provide a proof-of-the-concept realization of correspondence learning between a real manipulator robot and a simulated mobile robot.

## 参考
- http://arxiv.org/abs/2310.13458v3

## 개요
로봇 형태가 다양하여 스킬 반복 훈련의 효율성이 낮은 문제를 해결하기 위해, 본 논문은 작업 시연 기반 대응 학습 방법을 제안한다. 이 방법은 먼저 서로 다른 형태의 로봇이 동일한 기준 작업을 수행하도록 한 다음, 각 로봇에 대해 조건부 신경 운동 프리미티브를 독립적으로 훈련하고, 볼록 결합을 학습하여 이들의 잠재 인코딩을 융합한다. 훈련이 완료된 후, 하나의 로봇이 새로운 작업을 수행하는 것을 관찰하기만 하면 다른 로봇이 동일한 작업을 완료하는 궤적을 자동으로 생성할 수 있다. 실험은 세 가지 시나리오에서 이 방법의 유효성을 검증했다: 로봇이 동일한 경로를 따라야 하는 경우, 서로 다른 경로를 따라야 하는 경우, 그리고 서로 다른 복잡도의 궤적으로 작업을 완료해야 하는 경우. 또한 실제 로봇 팔과 시뮬레이션 이동 로봇 간의 대응 학습 개념 검증도 구현되었다.

## 핵심 내용
### 방법 아키텍처
- **핵심 프레임워크**: 각 로봇에 대해 독립적인 Conditional Neural Movement Primitives(cNMP)를 훈련하고, 학습 가능한 볼록 결합(convex combination)을 통해 각 로봇의 잠재 인코딩(latent codes)을 융합하여 형태 간 제로샷 궤적 생성을 구현한다.
- **훈련 프로세스**:
  1. 모든 로봇이 동일한 기준 작업(예: 목표 지점 도달)을 수행하도록 하고, 시연 데이터를 수집한다.
  2. 공통 잠재 표현(common latent representation)과 각 로봇의 독립적인 정책을 공동으로 학습한다.
  3. 훈련이 완료된 후, 하나의 로봇의 새로운 작업 시연을 입력하면 잠재 공간 매핑을 통해 다른 로봇의 대응 궤적을 자동으로 생성한다.

### 실험 설정
- **로봇 유형**: 고정 베이스 관절 제어 로봇 팔(fixed-based manipulator)과 차동 구동 이동 로봇(differential drive mobile robot)을 사용하여 서로 다른 형태(서로 다른 자유도, 서로 다른 제어 방식)의 대응 학습을 검증했다.
- **세 가지 실험 시나리오**:
  1. **동일 경로**: 모든 로봇이 동일한 기하학적 경로를 따라 작업을 완료해야 한다.
  2. **서로 다른 경로**: 로봇이 서로 다른 궤적을 사용하지만 동일한 작업 목표를 달성해야 한다.
  3. **서로 다른 복잡도**: 각 로봇이 요구하는 센서-운동 궤적의 복잡도가 다르다.
- **실제-시뮬레이션 검증**: 실제 로봇 팔과 시뮬레이션 이동 로봇 간의 대응 학습 개념 검증(proof-of-concept)을 구현했다.

### 핵심 결론
- 이 방법은 단일 작업 시연에서 서로 다른 형태의 로봇으로의 제로샷 궤적 생성을 성공적으로 구현했으며, 재훈련이 필요 없다.
- 세 가지 실험 시나리오에서 모두 유효하며, 특히 형태 차이가 큰 로봇(예: 로봇 팔과 이동 로봇)에 적합하다.
- 잠재 공간 융합 전략(볼록 결합)은 서로 다른 로봇의 운동 패턴 간 공통점을 효과적으로 포착하면서 개별 차이를 보존할 수 있다.
