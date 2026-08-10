---
$id: ent_paper_team_gemini_robotics_15_pushing_the_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion
    Transfer'
  zh: Gemini Robotics 1.5：以高级具身推理、思考和动作迁移推动通才机器人前沿
  ko: 'Gemini Robotics 1.5: 고급 구체화 추론, 사고 및 동작 전이를 통한 범용 로봇의 최전선 확장'
summary:
  en: Gemini Robotics 1.5 introduces a multi-embodiment Vision-Language-Action model with Motion Transfer and a Thinking VLA
    that interleaves actions with natural-language reasoning, alongside Gemini Robotics-ER 1.5, an embodied reasoning model
    for spatial understanding and task planning.
  zh: Gemini Robotics 1.5 是 Google DeepMind 推出的新一代通用机器人模型家族，包含多形态视觉-语言-动作模型与运动转移机制，以及先进的具身推理模型 Gemini Robotics-ER 1.5。核心贡献在于通过动作与自然语言推理的交错执行实现“先思考后行动”，并在空间理解与任务规划上达到新高度。
  ko: Gemini Robotics 1.5는 동작 전이를 갖춘 다중 구체화 비전-언어-행동 모델과 자연어 추론과 행동을 교차하는 Thinking VLA를 소개하며, 공간 이해와 작업 계획을 위한 Gemini Robotics-ER
    1.5 구체화 추론 모델을 함께 제시한다.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
- 08_software_middleware
layers:
- intelligence
functional_roles:
- intelligence
- knowledge
tags:
- vla
- vision_language_action
- embodied_reasoning
- motion_transfer
- multi_embodiment
- humanoid_robot
- apptronik_apollo
- thinking_vla
- foundation_model
- robot_learning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.03342v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (559 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion
    Transfer'
  url: https://arxiv.org/abs/2510.03342
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Gemini Robotics 1.5 家族由两个核心模型组成：多形态视觉-语言-动作模型与具身推理模型 Gemini Robotics-ER 1.5。前者通过创新的运动转移机制，能够从异构的多形态机器人数据中学习，提升通用性；后者则在视觉空间理解、任务规划与进度估计等关键具身推理能力上达到当前最优水平。该家族模型通过将动作与多级自然语言推理过程交错执行，使机器人能够分解并完成复杂多步任务，同时提升行为可解释性。

## 核心内容
### 模型架构与创新
- **多形态视觉-语言-动作模型**：采用新型架构，支持从不同形态的机器人数据中学习，通过**运动转移机制**实现跨形态技能迁移，增强模型的通用性。
- **思考型 VLA**：在动作生成过程中交错插入多级自然语言推理，使机器人能够“先思考后行动”，显著提升复杂多步任务的分解与执行能力，同时让用户更易理解机器人的行为逻辑。

### 具身推理模型
- **Gemini Robotics-ER 1.5**：在具身推理领域达到新最优水平，核心能力包括：
  - 视觉与空间理解
  - 任务规划
  - 进度估计

### 实验与结论
- 该模型家族使机器人能够感知、思考并行动，从而解决复杂的多步任务，标志着向通用物理智能体时代迈出重要一步。

## Overview
General-purpose robots need a deep understanding of the physical world, advanced reasoning, and general and dexterous control. This report introduces the latest generation of the Gemini Robotics model family: Gemini Robotics 1.5, a multi-embodiment Vision-Language-Action (VLA) model, and Gemini Robotics-ER 1.5, a state-of-the-art Embodied Reasoning (ER) model. We are bringing together three major innovations. First, Gemini Robotics 1.5 features a novel architecture and a Motion Transfer (MT) mechanism, which enables it to learn from heterogeneous, multi-embodiment robot data and makes the VLA more general. Second, Gemini Robotics 1.5 interleaves actions with a multi-level internal reasoning process in natural language. This enables the robot to "think before acting" and notably improves its ability to decompose and execute complex, multi-step tasks, and also makes the robot's behavior more interpretable to the user. Third, Gemini Robotics-ER 1.5 establishes a new state-of-the-art for embodied reasoning, i.e., for reasoning capabilities that are critical for robots, such as visual and spatial understanding, task planning, and progress estimation. Together, this family of models takes us a step towards an era of physical agents-enabling robots to perceive, think and then act so they can solve complex multi-step tasks.

## Overview
General-purpose robots require a profound understanding of the physical world, advanced reasoning capabilities, and general, dexterous control. This report introduces the latest generation of the Gemini Robotics model family: Gemini Robotics 1.5, a multi-embodiment Vision-Language-Action (VLA) model, and Gemini Robotics-ER 1.5, a state-of-the-art Embodied Reasoning (ER) model. We bring together three major innovations. First, Gemini Robotics 1.5 features a novel architecture and a Motion Transfer (MT) mechanism, enabling it to learn from heterogeneous, multi-embodiment robot data and making the VLA more general. Second, Gemini Robotics 1.5 interleaves actions with a multi-level internal reasoning process in natural language. This allows the robot to "think before acting," significantly improving its ability to decompose and execute complex, multi-step tasks, while also making its behavior more interpretable to users. Third, Gemini Robotics-ER 1.5 establishes a new state-of-the-art for embodied reasoning—i.e., reasoning capabilities critical for robots, such as visual and spatial understanding, task planning, and progress estimation. Together, this family of models takes us a step closer to an era of physical agents, enabling robots to perceive, think, and then act to solve complex multi-step tasks.

## Content
General-purpose robots require a profound understanding of the physical world, advanced reasoning capabilities, and general, dexterous control. This report introduces the latest generation of the Gemini Robotics model family: Gemini Robotics 1.5, a multi-embodiment Vision-Language-Action (VLA) model, and Gemini Robotics-ER 1.5, a state-of-the-art Embodied Reasoning (ER) model. We bring together three major innovations. First, Gemini Robotics 1.5 features a novel architecture and a Motion Transfer (MT) mechanism, enabling it to learn from heterogeneous, multi-embodiment robot data and making the VLA more general. Second, Gemini Robotics 1.5 interleaves actions with a multi-level internal reasoning process in natural language. This allows the robot to "think before acting," significantly improving its ability to decompose and execute complex, multi-step tasks, while also making its behavior more interpretable to users. Third, Gemini Robotics-ER 1.5 establishes a new state-of-the-art for embodied reasoning—i.e., reasoning capabilities critical for robots, such as visual and spatial understanding, task planning, and progress estimation. Together, this family of models takes us a step closer to an era of physical agents, enabling robots to perceive, think, and then act to solve complex multi-step tasks.

## 参考
- http://arxiv.org/abs/2510.03342v3

## 개요
Gemini Robotics 1.5 제품군은 두 가지 핵심 모델로 구성됩니다: 다형태 비전-언어-행동 모델과 구현 추론 모델 Gemini Robotics-ER 1.5입니다. 전자는 혁신적인 운동 전이 메커니즘을 통해 이기종 다형태 로봇 데이터에서 학습하여 범용성을 향상시킵니다. 후자는 시각적 공간 이해, 작업 계획, 진행 상황 추정과 같은 핵심 구현 추론 능력에서 현재 최고 수준에 도달했습니다. 이 제품군 모델은 행동과 다단계 자연어 추론 과정을 교차 실행함으로써 로봇이 복잡한 다단계 작업을 분해하고 완료할 수 있게 하며, 동시에 행동의 해석 가능성을 향상시킵니다.

## 핵심 내용
### 모델 아키텍처 및 혁신
- **다형태 비전-언어-행동 모델**: 새로운 아키텍처를 채택하여 다양한 형태의 로봇 데이터에서 학습을 지원하며, **운동 전이 메커니즘**을 통해 형태 간 기술 전이를 구현하여 모델의 범용성을 강화합니다.
- **사고형 VLA**: 행동 생성 과정에서 다단계 자연어 추론을 교차 삽입하여 로봇이 "먼저 생각한 후 행동"할 수 있게 하며, 복잡한 다단계 작업의 분해 및 실행 능력을 크게 향상시키고, 사용자가 로봇의 행동 논리를 더 쉽게 이해할 수 있게 합니다.

### 구현 추론 모델
- **Gemini Robotics-ER 1.5**: 구현 추론 분야에서 새로운 최고 수준에 도달했으며, 핵심 능력은 다음과 같습니다:
  - 시각 및 공간 이해
  - 작업 계획
  - 진행 상황 추정

### 실험 및 결론
- 이 모델 제품군은 로봇이 인식하고, 생각하고, 행동하여 복잡한 다단계 작업을 해결할 수 있게 하며, 범용 물리 지능 에이전트 시대로 나아가는 중요한 한 걸음을 의미합니다.
