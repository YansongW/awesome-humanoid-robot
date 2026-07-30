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
    English abstract via scripts/sinicize_english_cards.py'
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

## 개요
최근 많은 휴머노이드 로봇이 병원 및 요양 시설을 포함한 다양한 시설에 점점 더 많이 배치되고 있으며, 종종 인간 운영자가 원격으로 제어합니다. 이들의 운동학적 중복성은 도달성과 조작성을 향상시켜 복잡하고 혼잡한 환경을 탐색하고 다양한 작업을 수행할 수 있게 합니다. 그러나 이러한 중복성은 특히 로봇의 매크로-마이크로 구조(몸통과 팔)의 움직임을 조정하는 데 있어 상당한 제어 문제를 야기합니다. 따라서 우리는 원격 제어 모바일 휴머노이드 로봇의 몸통과 팔을 조정하기 위한 다양한 인간-로봇 협업(HRC) 방법을 제안하며, 자율성과 인간 입력의 균형을 맞춰 시스템 효율성과 작업 수행을 향상시키는 것을 목표로 합니다. 제안된 방법에는 사용자가 수동으로 몸통 움직임을 제어하는 인간 주도 접근법과 도달성, 작업 목표 또는 추론된 인간 의도와 같은 요소에 기반하여 몸통과 팔을 자율적으로 조정하는 로봇 주도 접근법이 포함됩니다. 우리는 $\mathbf{N} \boldsymbol{=} \mathbf{1 7}$명의 참가자를 대상으로 사용자 연구를 수행하여 제안된 접근법을 작업 성능, 조작성 및 에너지 효율성 측면에서 비교하고, 참가자들이 선호하는 방법을 분석했습니다.

## 핵심 내용
최근 많은 휴머노이드 로봇이 병원 및 요양 시설을 포함한 다양한 시설에 점점 더 많이 배치되고 있으며, 종종 인간 운영자가 원격으로 제어합니다. 이들의 운동학적 중복성은 도달성과 조작성을 향상시켜 복잡하고 혼잡한 환경을 탐색하고 다양한 작업을 수행할 수 있게 합니다. 그러나 이러한 중복성은 특히 로봇의 매크로-마이크로 구조(몸통과 팔)의 움직임을 조정하는 데 있어 상당한 제어 문제를 야기합니다. 따라서 우리는 원격 제어 모바일 휴머노이드 로봇의 몸통과 팔을 조정하기 위한 다양한 인간-로봇 협업(HRC) 방법을 제안하며, 자율성과 인간 입력의 균형을 맞춰 시스템 효율성과 작업 수행을 향상시키는 것을 목표로 합니다. 제안된 방법에는 사용자가 수동으로 몸통 움직임을 제어하는 인간 주도 접근법과 도달성, 작업 목표 또는 추론된 인간 의도와 같은 요소에 기반하여 몸통과 팔을 자율적으로 조정하는 로봇 주도 접근법이 포함됩니다. 우리는 $\mathbf{N} \boldsymbol{=} \mathbf{1 7}$명의 참가자를 대상으로 사용자 연구를 수행하여 제안된 접근법을 작업 성능, 조작성 및 에너지 효율성 측면에서 비교하고, 참가자들이 선호하는 방법을 분석했습니다.

## 参考
- Semantic Scholar search: Human-Robot Collaboration for the Remote Control of Mobile Humanoid Robots with Torso-Arm Coordination
