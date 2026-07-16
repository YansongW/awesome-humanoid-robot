---
$id: ent_paper_suriani_play_everywhere_a_temporal_log_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Play Everywhere: A Temporal Logic based Game Environment Independent Approach for Playing Soccer with Robots'
  zh: 随处可玩：一种基于时序逻辑的游戏环境无关机器人足球方法
  ko: '어디서나 플레이: 시계열 논리 기반 게임 환경 독립적인 로봇 축구 접근법'
summary:
  en: Proposes a temporal-logic-based hierarchical representation that lets NAO humanoid robots adapt soccer behaviors and
    goals to perceived semantic characteristics of unstructured environments, compiled into FOND planning.
  zh: Robots playing soccer often rely on hard-coded behaviors that struggle to generalize when the game environment change.
    In this paper, we propose a temporal logic based approach that allows robots' behaviors and goals to adapt to the semantics
    of the environment. In particular, we present a hierarchical representation of soccer in which the robot selects the level
    of operation based on the perceived semantic characteristics of the environment, thus modifying dynamically the set of
    rules and goals to apply. The proposed approach enables the robot to operate in unstructured environments, just as
  ko: 시계열 논리 기반 계층적 표현을 제안하여 NAO 휴머노이드 로봇이 비구조화 환경의 의미적 특성을 인식하여 축구 행동과 목표를 동적으로 조정하고 FOND 계획으로 컴파일할 수 있게 한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2405.12628v1.
sources:
- id: src_001
  type: paper
  title: 'Play Everywhere: A Temporal Logic based Game Environment Independent Approach for Playing Soccer with Robots'
  url: https://arxiv.org/abs/2405.12628
  date: '2024'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---

## 概述
Robots playing soccer often rely on hard-coded behaviors that struggle to generalize when the game environment change. In this paper, we propose a temporal logic based approach that allows robots' behaviors and goals to adapt to the semantics of the environment. In particular, we present a hierarchical representation of soccer in which the robot selects the level of operation based on the perceived semantic characteristics of the environment, thus modifying dynamically the set of rules and goals to apply. The proposed approach enables the robot to operate in unstructured environments, just as it happens when humans go from soccer played on an official field to soccer played on a street. Three different use cases set in different scenarios are presented to demonstrate the effectiveness of the proposed approach.

## 核心内容
Robots playing soccer often rely on hard-coded behaviors that struggle to generalize when the game environment change. In this paper, we propose a temporal logic based approach that allows robots' behaviors and goals to adapt to the semantics of the environment. In particular, we present a hierarchical representation of soccer in which the robot selects the level of operation based on the perceived semantic characteristics of the environment, thus modifying dynamically the set of rules and goals to apply. The proposed approach enables the robot to operate in unstructured environments, just as it happens when humans go from soccer played on an official field to soccer played on a street. Three different use cases set in different scenarios are presented to demonstrate the effectiveness of the proposed approach.

## 参考
- http://arxiv.org/abs/2405.12628v1

## Overview
Robots playing soccer often rely on hard-coded behaviors that struggle to generalize when the game environment changes. In this paper, we propose a temporal logic based approach that allows robots' behaviors and goals to adapt to the semantics of the environment. In particular, we present a hierarchical representation of soccer in which the robot selects the level of operation based on the perceived semantic characteristics of the environment, thus dynamically modifying the set of rules and goals to apply. The proposed approach enables the robot to operate in unstructured environments, just as it happens when humans go from soccer played on an official field to soccer played on a street. Three different use cases set in different scenarios are presented to demonstrate the effectiveness of the proposed approach.

## Content
Robots playing soccer often rely on hard-coded behaviors that struggle to generalize when the game environment changes. In this paper, we propose a temporal logic based approach that allows robots' behaviors and goals to adapt to the semantics of the environment. In particular, we present a hierarchical representation of soccer in which the robot selects the level of operation based on the perceived semantic characteristics of the environment, thus dynamically modifying the set of rules and goals to apply. The proposed approach enables the robot to operate in unstructured environments, just as it happens when humans go from soccer played on an official field to soccer played on a street. Three different use cases set in different scenarios are presented to demonstrate the effectiveness of the proposed approach.

## 개요
축구를 하는 로봇은 종종 하드코딩된 행동에 의존하는데, 이는 게임 환경이 변할 때 일반화하기 어렵습니다. 본 논문에서는 로봇의 행동과 목표가 환경의 의미론에 적응할 수 있도록 하는 시간 논리 기반 접근법을 제안합니다. 특히, 로봇이 인지된 환경의 의미론적 특성에 따라 작동 수준을 선택하여 적용할 규칙과 목표 집합을 동적으로 수정하는 축구의 계층적 표현을 제시합니다. 제안된 접근법은 인간이 공식 경기장에서 축구를 하다가 거리에서 축구를 하는 것처럼, 로봇이 비구조화된 환경에서도 작동할 수 있게 합니다. 제안된 접근법의 효과를 입증하기 위해 다양한 시나리오에서 설정된 세 가지 사용 사례를 제시합니다.

## 핵심 내용
축구를 하는 로봇은 종종 하드코딩된 행동에 의존하는데, 이는 게임 환경이 변할 때 일반화하기 어렵습니다. 본 논문에서는 로봇의 행동과 목표가 환경의 의미론에 적응할 수 있도록 하는 시간 논리 기반 접근법을 제안합니다. 특히, 로봇이 인지된 환경의 의미론적 특성에 따라 작동 수준을 선택하여 적용할 규칙과 목표 집합을 동적으로 수정하는 축구의 계층적 표현을 제시합니다. 제안된 접근법은 인간이 공식 경기장에서 축구를 하다가 거리에서 축구를 하는 것처럼, 로봇이 비구조화된 환경에서도 작동할 수 있게 합니다. 제안된 접근법의 효과를 입증하기 위해 다양한 시나리오에서 설정된 세 가지 사용 사례를 제시합니다.
