---
$id: ent_paper_liang_end_user_programming_of_low_an_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: End-User Programming of Low- and High-Level Actions for Robotic Task Planning
  zh: 面向机器人任务规划的最终用户低层与高层动作编程
  ko: 로봇 작업 계획을 위한 최종 사용자의 저수준 및 고수준 동작 프로그래밍
summary:
  en: Introduces iRoPro, an interactive Programming-by-Demonstration framework that lets end-users teach robots reusable low-level
    manipulation actions and high-level PDDL-style conditions, then reuses them with a Fast-Forward task planner to solve
    unseen tasks.
  zh: iRoPro 是一个交互式编程通过演示框架，允许终端用户教机器人可复用的低级操作动作和高级PDDL风格条件，然后通过Fast-Forward任务规划器重用这些动作来解决未见过的任务。该框架在双臂Baxter机器人上实现，并通过用户研究（N=21）验证了其易用性和泛化能力。
  ko: 최종 사용자가 재사용 가능한 저수준 조작 동작과 PDDL 스타일의 고수준 조건을 로봇에 가르치고 Fast-Forward 작업 플래너를 활용해 보지 못한 작업을 해결하는 iRoPro 대화형 시연 프로그래밍 프레임워크를
    소개한다.
domains:
- 08_software_middleware
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- programming_by_demonstration
- task_planning
- pddl
- fast_forward_planner
- end_user_programming
- human_robot_interaction
- manipulation
- baxter
- iropro
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2103.14342v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (721 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: End-User Programming of Low- and High-Level Actions for Robotic Task Planning
  url: https://arxiv.org/abs/2103.14342
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
iRoPro 框架解决了终端用户编程机器人的挑战，特别是从零开始教授可重用动作的问题。它通过演示同时教授低级和高级动作，并包含一个带有条件推理和修改的用户界面。系统在六个基准任务上评估了泛化能力，并通过21名用户的用户研究证明了不同编程水平和教育背景的用户都能轻松学习和使用该系统。

## 核心内容
### 方法
iRoPro 是一个交互式机器人编程框架，允许终端用户通过演示教授机器人新动作，并利用任务规划器重用这些动作。框架在双臂Baxter机器人上实现，支持：
- 同时教授低级和高级动作
- 通过用户界面创建动作，包含条件推理和修改功能
- 使用任务规划器创建和解决未见过的任务，并实时执行

### 架构
iRoPro 的核心架构包括：
- **低级动作**：通过演示教授的可复用操作，如抓取、放置等
- **高级动作**：以PDDL风格定义的条件和效果，描述动作的上下文和结果
- **任务规划器**：使用Fast-Forward规划器，基于教授的动作和条件生成任务执行序列

### 实验设置
- **机器人平台**：双臂Baxter机器人
- **基准任务**：六个基准任务，用于评估系统的泛化能力
- **用户研究**：21名参与者，完成八项任务，教授机器人新动作并重用

### 关键数字
- 用户研究参与者：21人
- 基准任务数量：6个
- 用户完成任务数量：8项

### 结论
iRoPro 框架成功实现了终端用户从零开始教授机器人可重用动作，并通过任务规划器解决未见过的任务。用户研究结果表明，无论用户的编程水平或教育背景如何，都能轻松学习和使用该系统。这为机器人通用应用编程提供了可行的解决方案。

## Overview
Programming robots for general purpose applications is extremely challenging due to the great diversity of end-user tasks ranging from manufacturing environments to personal homes. Recent work has focused on enabling end-users to program robots using Programming by Demonstration. However, teaching robots new actions from scratch that can be reused for unseen tasks remains a difficult challenge and is generally left up to robotic experts. We propose iRoPro, an interactive Robot Programming framework that allows end-users to teach robots new actions from scratch and reuse them with a task planner. In this work we provide a system implementation on a two-armed Baxter robot that (i) allows simultaneous teaching of low- and high-level actions by demonstration, (ii) includes a user interface for action creation with condition inference and modification, and (iii) allows creating and solving previously unseen problems using a task planner for the robot to execute in real-time. We evaluate the generalisation power of the system on six benchmark tasks and show how taught actions can be easily reused for complex tasks. We further demonstrate its usability with a user study (N=21), where users completed eight tasks to teach the robot new actions that are reused with a task planner. The study demonstrates that users with any programming level and educational background can easily learn and use the system.

## 参考
- http://arxiv.org/abs/2103.14342v1

## 개요
iRoPro 프레임워크는 최종 사용자가 로봇을 프로그래밍할 때 겪는 과제, 특히 처음부터 재사용 가능한 동작을 가르치는 문제를 해결합니다. 이는 시연을 통해 저수준 및 고수준 동작을 동시에 가르치며, 조건부 추론과 수정 기능을 갖춘 사용자 인터페이스를 포함합니다. 시스템은 6개의 기준 작업에서 일반화 능력을 평가했으며, 21명의 사용자 연구를 통해 다양한 프로그래밍 수준과 교육 배경을 가진 사용자가 쉽게 배우고 사용할 수 있음을 입증했습니다.

## 핵심 내용
### 방법
iRoPro는 최종 사용자가 시연을 통해 로봇에 새 동작을 가르치고 작업 플래너를 통해 이러한 동작을 재사용할 수 있게 하는 대화형 로봇 프로그래밍 프레임워크입니다. 이 프레임워크는 양팔 Baxter 로봇에 구현되었으며, 다음을 지원합니다:
- 저수준 및 고수준 동작의 동시 교육
- 조건부 추론 및 수정 기능을 포함한 사용자 인터페이스를 통한 동작 생성
- 작업 플래너를 사용한 미해결 작업 생성 및 해결, 실시간 실행

### 아키텍처
iRoPro의 핵심 아키텍처는 다음을 포함합니다:
- **저수준 동작**: 시연을 통해 가르치는 재사용 가능한 작업(예: 잡기, 놓기 등)
- **고수준 동작**: PDDL 스타일로 정의된 조건과 효과로, 동작의 맥락과 결과를 설명
- **작업 플래너**: Fast-Forward 플래너를 사용하여 가르친 동작과 조건을 기반으로 작업 실행 시퀀스 생성

### 실험 설정
- **로봇 플랫폼**: 양팔 Baxter 로봇
- **기준 작업**: 시스템의 일반화 능력을 평가하기 위한 6개의 기준 작업
- **사용자 연구**: 21명의 참가자가 8개의 작업을 완료하며 로봇에 새 동작을 가르치고 재사용

### 주요 수치
- 사용자 연구 참가자: 21명
- 기준 작업 수: 6개
- 사용자 완료 작업 수: 8개

### 결론
iRoPro 프레임워크는 최종 사용자가 처음부터 로봇에 재사용 가능한 동작을 가르치고 작업 플래너를 통해 미해결 작업을 해결할 수 있도록 성공적으로 구현했습니다. 사용자 연구 결과는 사용자의 프로그래밍 수준이나 교육 배경에 관계없이 쉽게 배우고 사용할 수 있음을 보여줍니다. 이는 로봇의 일반 응용 프로그래밍에 실현 가능한 솔루션을 제공합니다.
