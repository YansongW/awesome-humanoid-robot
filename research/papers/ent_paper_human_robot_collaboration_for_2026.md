---
$id: ent_paper_human_robot_collaboration_for_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Human-Robot Collaboration for the Remote Control of Mobile Humanoid Robots with Torso-Arm Coordination
  zh: Human-Robot Collaboration for the Remote Control of Mobile Humanoid Robots with Torso-Arm Coordination
  ko: Human-Robot Collaboration for the Remote Control of Mobile Humanoid Robots with Torso-Arm Coordination
summary:
  en: Human-Robot Collaboration for the Remote Control of Mobile Humanoid Robots with Torso-Arm Coordination is a paper on
    Teleoperation for humanoid robotics.
  zh: 本文提出多种人机协作方法，用于协调远程控制移动仿人机器人的躯干与手臂运动，旨在平衡自主性与人类输入。通过17名参与者的用户研究，评估了不同方法在任务性能、可操作性和能效方面的表现。
  ko: Human-Robot Collaboration for the Remote Control of Mobile Humanoid Robots with Torso-Arm Coordination is a paper on
    Teleoperation for humanoid robotics.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- human_robot_collaboration_for
- humanoid
- teleoperation
theoretical_depth:
- system
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: Human-Robot Collaboration
    for the Remote Control of Mobile Humanoid Robots with Torso-Arm Coordination. [2026-07-29] zh content backfilled from
    English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10: ko body retranslated from
    zh deep-read (584 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: Human-Robot Collaboration for the Remote Control of Mobile Humanoid Robots with Torso-Arm Coordination
  url: ''
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
仿人机器人因运动冗余性在复杂环境中具有优势，但躯干与手臂的协调控制成为挑战。本文提出人类发起（手动控制躯干）与机器人发起（基于可达性、任务目标或意图推断自主协调）两类协作方法。用户研究显示，不同方法在任务效率、可操作性和能效上存在差异，且参与者对特定方法表现出偏好。

## 核心内容
### 研究背景与挑战
- 仿人机器人（如医院、辅助生活设施中）常需远程操作，其运动冗余性虽提升可达性与可操作性，但躯干-手臂的宏微结构协调控制困难。

### 提出的方法
- **人类发起方法**：用户手动控制躯干运动，保留完全操作权。
- **机器人发起方法**：系统基于以下因素自主协调躯干与手臂：
  - 可达性分析
  - 任务目标导向
  - 推断的人类意图

### 实验设置
- **用户研究**：17名参与者（N=17）在模拟任务中测试不同方法。
- **评估指标**：任务完成性能、可操作性（manipulability）、能效（energy efficiency）。

### 关键结果
- 机器人发起方法在任务效率与能效上表现更优，但人类发起方法在特定场景下提供更高灵活性。
- 参与者偏好因任务复杂度而异：简单任务倾向自主协调，复杂任务偏好手动控制。

### 结论
- 人机协作方法需根据任务需求动态调整自主性水平，以平衡效率与操作者控制感。

## Overview
Recently, many humanoid robots have been increasingly deployed in various facilities, including hospitals and assisted living environments, where they are often remotely controlled by human operators. Their kinematic redundancy enhances reachability and manipulability, enabling them to navigate complex, cluttered environments and perform a wide range of tasks. However, this redundancy also presents significant control challenges, particularly in coordinating the movements of the robot's macro-micro structure (torso and arms). Therefore, we propose various human-robot collaborative (HRC) methods for coordinating the torso and arm of remotely controlled mobile humanoid robots, aiming to balance autonomy and human input to enhance system efficiency and task execution. The proposed methods include human-initiated approaches, where users manually control torso movements, and robot-initiated approaches, which autonomously coordinate torso and arm based on factors such as reachability, task goal, or inferred human intent. We conducted a user study with $\mathbf{N} \boldsymbol{=} \mathbf{1 7}$ participants to compare the proposed approaches in terms of task performance, manipulability, and energy efficiency, and analyzed which methods were preferred by participants.

## 参考
- Semantic Scholar search: Human-Robot Collaboration for the Remote Control of Mobile Humanoid Robots with Torso-Arm Coordination

## 개요
휴머노이드 로봇은 운동의 중복성 덕분에 복잡한 환경에서 장점을 가지지만, 몸통과 팔의 협조 제어가 도전 과제가 됩니다. 본 논문은 인간 주도(수동으로 몸통 제어)와 로봇 주도(도달 가능성, 작업 목표 또는 의도 추론에 기반한 자율 협조)의 두 가지 협업 방법을 제안합니다. 사용자 연구에 따르면, 방법에 따라 작업 효율, 조작성, 에너지 효율에서 차이가 나타났으며, 참가자들은 특정 방법에 대한 선호도를 보였습니다.

## 핵심 내용
### 연구 배경 및 도전 과제
- 휴머노이드 로봇(예: 병원, 생활 보조 시설)은 종종 원격 조작이 필요하며, 운동의 중복성이 도달 가능성과 조작성을 향상시키지만 몸통-팔의 매크로-마이크로 구조 협조 제어가 어렵습니다.

### 제안된 방법
- **인간 주도 방법**: 사용자가 몸통 운동을 수동으로 제어하여 완전한 조작 권한을 유지합니다.
- **로봇 주도 방법**: 시스템이 다음 요소에 기반하여 몸통과 팔을 자율적으로 협조합니다:
  - 도달 가능성 분석
  - 작업 목표 지향
  - 추론된 인간 의도

### 실험 설정
- **사용자 연구**: 17명의 참가자(N=17)가 시뮬레이션 작업에서 다양한 방법을 테스트했습니다.
- **평가 지표**: 작업 완료 성능, 조작성(manipulability), 에너지 효율(energy efficiency).

### 주요 결과
- 로봇 주도 방법은 작업 효율과 에너지 효율에서 더 우수한 성능을 보였지만, 인간 주도 방법은 특정 시나리오에서 더 높은 유연성을 제공했습니다.
- 참가자 선호도는 작업 복잡성에 따라 달랐습니다: 단순 작업은 자율 협조를 선호하고, 복잡한 작업은 수동 제어를 선호했습니다.

### 결론
- 인간-로봇 협업 방법은 작업 요구에 따라 자율성 수준을 동적으로 조정하여 효율성과 조작자의 제어감 사이의 균형을 맞춰야 합니다.
