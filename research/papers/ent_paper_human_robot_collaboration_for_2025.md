---
$id: ent_paper_human_robot_collaboration_for_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Human-Robot Collaboration for the Remote Control of Mobile Humanoid Robots
  zh: Human-Robot Collaboration for the Remote Control of Mobile Humanoid Robots
  ko: Human-Robot Collaboration for the Remote Control of Mobile Humanoid Robots
summary:
  en: Human-Robot Collaboration for the Remote Control of Mobile Humanoid Robots is a 2025 work on teleoperation for humanoid
    robots.
  zh: 这是一篇2025年关于移动人形机器人远程操控中的人机协作研究。作者提出了多种协调机器人躯干与手臂运动的方法，包括人类主导和机器人自主两种模式。通过17人用户实验，评估了不同方法在任务表现、可操作性和能效方面的优劣。
  ko: Human-Robot Collaboration for the Remote Control of Mobile Humanoid Robots is a 2025 work on teleoperation for humanoid
    robots.
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
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.05773v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Human-Robot Collaboration for the Remote Control of Mobile Humanoid Robots (arXiv)
  url: https://arxiv.org/abs/2505.05773
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
移动人形机器人因其运动冗余性，在复杂环境中具有更强的可达性和可操作性，但也带来了躯干与手臂协调控制的挑战。为此，本文提出了多种人机协作方法，包括由人类手动控制躯干运动的人类主导方式，以及基于可达性、任务目标或推断的人类意图来自主协调躯干与手臂的机器人主导方式。研究通过17名参与者的用户实验，对比了这些方法在任务表现、可操作性和能效方面的表现，并分析了参与者的偏好。

## 核心内容
### 研究背景与挑战
- 人形机器人正被部署于医院、辅助生活设施等场景，常需远程操控。
- 运动冗余性虽提升了可达性与可操作性，但增加了躯干与手臂（宏观-微观结构）协调控制的难度。

### 提出的方法
- **人类主导方法**：用户手动控制躯干运动，保留完全控制权。
- **机器人主导方法**：机器人根据可达性、任务目标或推断的人类意图，自主协调躯干与手臂运动。

### 实验设置
- 用户研究：N=17名参与者。
- 评估指标：任务表现、可操作性、能效。
- 分析目标：确定参与者偏好的方法。

### 结论
- 不同方法在任务表现、可操作性和能效上存在差异，参与者偏好因场景而异。

## Overview
Recently, many humanoid robots have been increasingly deployed in various facilities, including hospitals and assisted living environments, where they are often remotely controlled by human operators. Their kinematic redundancy enhances reachability and manipulability, enabling them to navigate complex, cluttered environments and perform a wide range of tasks. However, this redundancy also presents significant control challenges, particularly in coordinating the movements of the robot's macro-micro structure (torso and arms). Therefore, we propose various human-robot collaborative (HRC) methods for coordinating the torso and arm of remotely controlled mobile humanoid robots, aiming to balance autonomy and human input to enhance system efficiency and task execution. The proposed methods include human-initiated approaches, where users manually control torso movements, and robot-initiated approaches, which autonomously coordinate torso and arm based on factors such as reachability, task goal, or inferred human intent. We conducted a user study with N=17 participants to compare the proposed approaches in terms of task performance, manipulability, and energy efficiency, and analyzed which methods were preferred by participants.

## 개요
최근 많은 휴머노이드 로봇이 병원 및 요양 시설을 포함한 다양한 시설에 점점 더 많이 배치되고 있으며, 종종 인간 운영자가 원격으로 제어합니다. 이들의 운동학적 중복성은 도달성과 조작성을 향상시켜 복잡하고 혼잡한 환경을 탐색하고 다양한 작업을 수행할 수 있게 합니다. 그러나 이러한 중복성은 특히 로봇의 매크로-마이크로 구조(몸통과 팔)의 움직임을 조정하는 데 있어 상당한 제어 문제를 야기합니다. 따라서 우리는 원격 제어 모바일 휴머노이드 로봇의 몸통과 팔을 조정하기 위한 다양한 인간-로봇 협업(HRC) 방법을 제안하며, 자율성과 인간 입력의 균형을 맞춰 시스템 효율성과 작업 실행을 향상시키는 것을 목표로 합니다. 제안된 방법에는 사용자가 수동으로 몸통 움직임을 제어하는 인간 주도 접근 방식과 도달성, 작업 목표 또는 추론된 인간 의도와 같은 요소에 기반하여 몸통과 팔을 자율적으로 조정하는 로봇 주도 접근 방식이 포함됩니다. 우리는 N=17명의 참가자로 사용자 연구를 수행하여 제안된 접근 방식을 작업 성능, 조작성 및 에너지 효율성 측면에서 비교하고 참가자가 선호하는 방법을 분석했습니다.

## 핵심 내용
최근 많은 휴머노이드 로봇이 병원 및 요양 시설을 포함한 다양한 시설에 점점 더 많이 배치되고 있으며, 종종 인간 운영자가 원격으로 제어합니다. 이들의 운동학적 중복성은 도달성과 조작성을 향상시켜 복잡하고 혼잡한 환경을 탐색하고 다양한 작업을 수행할 수 있게 합니다. 그러나 이러한 중복성은 특히 로봇의 매크로-마이크로 구조(몸통과 팔)의 움직임을 조정하는 데 있어 상당한 제어 문제를 야기합니다. 따라서 우리는 원격 제어 모바일 휴머노이드 로봇의 몸통과 팔을 조정하기 위한 다양한 인간-로봇 협업(HRC) 방법을 제안하며, 자율성과 인간 입력의 균형을 맞춰 시스템 효율성과 작업 실행을 향상시키는 것을 목표로 합니다. 제안된 방법에는 사용자가 수동으로 몸통 움직임을 제어하는 인간 주도 접근 방식과 도달성, 작업 목표 또는 추론된 인간 의도와 같은 요소에 기반하여 몸통과 팔을 자율적으로 조정하는 로봇 주도 접근 방식이 포함됩니다. 우리는 N=17명의 참가자로 사용자 연구를 수행하여 제안된 접근 방식을 작업 성능, 조작성 및 에너지 효율성 측면에서 비교하고 참가자가 선호하는 방법을 분석했습니다.

## 参考
- http://arxiv.org/abs/2505.05773v1
