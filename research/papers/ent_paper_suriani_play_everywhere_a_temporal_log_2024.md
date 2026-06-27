---
$id: ent_paper_suriani_play_everywhere_a_temporal_log_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Play Everywhere: A Temporal Logic based Game Environment Independent Approach
    for Playing Soccer with Robots'
  zh: 随处可玩：一种基于时序逻辑的游戏环境无关机器人足球方法
  ko: '어디서나 플레이: 시계열 논리 기반 게임 환경 독립적인 로봇 축구 접근법'
summary:
  en: Proposes a temporal-logic-based hierarchical representation that lets NAO humanoid
    robots adapt soccer behaviors and goals to perceived semantic characteristics
    of unstructured environments, compiled into FOND planning.
  zh: 提出一种基于时序逻辑的分层表示方法，使NAO人形机器人能够根据对非结构化环境的语义感知动态调整足球行为与目标，并编译为FOND规划。
  ko: 시계열 논리 기반 계층적 표현을 제안하여 NAO 휴머노이드 로봇이 비구조화 환경의 의미적 특성을 인식하여 축구 행동과 목표를 동적으로 조정하고
    FOND 계획으로 컴파일할 수 있게 한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- temporal_logic
- fond_planning
- behavior_planning
- adaptive_behavior
- nao_robot
- robocup_spl
- robot_soccer
- pltl
- semantic_perception
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; full-text independent verification
    not performed.
sources:
- id: src_001
  type: paper
  title: 'Play Everywhere: A Temporal Logic based Game Environment Independent Approach
    for Playing Soccer with Robots'
  url: https://arxiv.org/abs/2405.12628
  date: '2024'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---

## Overview

Robots playing soccer traditionally depend on hard-coded behaviors that break down when the environment changes, such as moving from an official field to a street. This paper introduces a temporal-logic-based approach in which a robot dynamically selects its level of operation according to the perceived semantic characteristics of the environment. By changing the active level, the robot modifies the rules and goals it pursues, enabling play in unstructured settings.

The core of the proposal is a hierarchical representation of soccer coupled with Pure-Past Linear Temporal Logic (PLTLf) rules over finite traces. These non-Markovian temporal goals are compiled into Fully Observable Non-Deterministic (FOND) planning problems. An intermediate conceptual layer abstracts ordinary sensed objects into semantically equivalent entities, decoupling high-level reasoning from the underlying perception pipeline.

The authors instantiate the approach on the B-Human SPL framework running on NAO humanoid robots and report three use cases of increasing complexity to show how the same architecture adapts to different environmental semantics.

## Key Contributions

- A hierarchical representation of goals that adapts to the complexity level of the operational environment based on perceived semantics.
- An SPL-related conceptual layer that generalizes ordinary objects to semantically equivalent entities, decoupled from the sensory level.
- An approach to FOND planning for temporal goals that encodes non-Markovian properties as mixed sets of predicates and PLTLf rules.
- A deployed architecture built on the B-Human SPL framework demonstrating three use cases of increasing complexity.

## Relevance to Humanoid Robotics

The approach is implemented on NAO humanoid robots competing in the RoboCup Standard Platform League (SPL), so it directly concerns adaptive behavior generation for humanoid platforms. Rather than relying on hand-tuned, environment-specific behaviors, it provides a principled method for replanning goals from perceived semantic context, which is relevant to deploying humanoids in unstructured or partially known environments.

From an industry-chain perspective, the paper sits at the algorithm and software-middleware layers: it improves how a humanoid robot reasons about tasks and selects actions. While the soccer domain is narrow, the underlying pattern of environment-independent temporal-goal adaptation could transfer to other humanoid applications such as service tasks, search-and-rescue, or logistics.
