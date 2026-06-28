---
$id: ent_paper_colledanchise_act_perceive_and_plan_in_belie_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Act, Perceive, and Plan in Belief Space for Robot Localization
  zh: 在信念空间中行动、感知与规划以实现机器人定位
  ko: 로봇 위치 추정을 위한 신념 공간에서의 행동, 인식 및 계획
summary:
  en: This paper proposes an interleaved acting-and-planning framework that reduces
    robot pose uncertainty by planning sequences of actuation and perception actions
    in belief space, using a best-first search guided by an entropy-based heuristic.
    The method was validated in simulation and on the IIT-R1 humanoid robot, showing
    that active semantic perception can complement feature-based localization in ambiguous
    environments.
  zh: 本文提出了一种交错执行与规划的框架，通过在信念空间中使用基于熵启发式的最佳优先搜索来规划驱动与感知动作序列，从而降低机器人位姿不确定性。该方法在仿真和IIT-R1人形机器人上进行了验证，表明主动语义感知可以在模糊环境中补充基于特征的定。
  ko: 본 논문은 엔트로피 기반 휴리스틱을 사용하는 최우선 탐색을 통해 신념 공간에서 구동 및 인식 동작 시퀀스를 계획함으로써 로봇 자세 불확실성을
    줄이는 행동-계획 상호 교차 프레임워크를 제안한다. 이 방법은 시뮬레이션과 IIT-R1 휴머노이드 로봇에서 검증되었으며, 모호한 환경에서 능동적
    의미 인식이 특징 기반 위치 추정을 보완할 수 있음을 보여준다.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- intelligence
- knowledge
tags:
- active_perception
- belief_space_planning
- robot_localization
- semantic_localization
- entropy_based_search
- iit_r1
- humanoid_localization
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full-text review is needed
    to confirm exact section citations and experimental details.
sources:
- id: src_001
  type: paper
  title: Act, Perceive, and Plan in Belief Space for Robot Localization
  url: https://arxiv.org/abs/2002.08124
  date: '2020'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

The paper addresses feature-based robot localization in ambiguous or semantically rich environments where standard approaches may converge slowly or fail when initialized incorrectly. It formulates localization as an active information-gathering problem: a task planner operates in belief space over the robot's pose and selects sequences of actuation actions and perception actions (e.g., recognizing objects or asking directions) that most reduce uncertainty. Planning is performed with a best-first search and an entropy-based heuristic, and the framework reuses previously explored belief states during replanning to improve efficiency.

## Key Contributions

- Interleaved acting and planning framework for rapid robot localization in semantically-annotated maps.
- Best-first search in belief space using an entropy-based heuristic.
- Theoretical proofs of soundness and probabilistic completeness for the proposed algorithm.
- Simulated scalability experiments and real-robot experiments on the IIT-R1 humanoid.

## Relevance to Humanoid Robotics

The method was validated on the IIT-R1 humanoid robot, demonstrating that active semantic perception and belief-space planning can localize a full-size humanoid in real-world, ambiguous environments such as a kitchen and hallway. By complementing feature-based localization with semantic information gathering, the work is directly relevant to humanoid navigation and autonomy.
