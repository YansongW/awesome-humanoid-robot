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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.05773v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (495 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2505.05773v1

## 개요
이동형 휴머노이드 로봇은 운동의 중복성 덕분에 복잡한 환경에서 더 높은 도달성과 조작성을 제공하지만, 동시에 몸통과 팔의 협조 제어에 대한 도전 과제를 야기합니다. 이를 위해 본 논문은 인간이 몸통 운동을 수동으로 제어하는 인간 주도 방식과, 도달성, 작업 목표 또는 추론된 인간 의도에 기반하여 로봇이 몸통과 팔을 자율적으로 조정하는 로봇 주도 방식을 포함한 다양한 인간-로봇 협업 방법을 제안합니다. 연구는 17명의 참가자를 대상으로 한 사용자 실험을 통해 이러한 방법들을 작업 성능, 조작성 및 에너지 효율 측면에서 비교하고, 참가자들의 선호도를 분석했습니다.

## 핵심 내용
### 연구 배경 및 도전 과제
- 휴머노이드 로봇은 병원, 보조 생활 시설 등에서 배치되고 있으며, 종종 원격 조종이 필요합니다.
- 운동의 중복성은 도달성과 조작성을 향상시키지만, 몸통과 팔(매크로-마이크로 구조)의 협조 제어 난이도를 증가시킵니다.

### 제안된 방법
- **인간 주도 방식**: 사용자가 몸통 운동을 수동으로 제어하여 완전한 제어권을 유지합니다.
- **로봇 주도 방식**: 로봇이 도달성, 작업 목표 또는 추론된 인간 의도에 기반하여 몸통과 팔의 운동을 자율적으로 조정합니다.

### 실험 설정
- 사용자 연구: N=17명의 참가자.
- 평가 지표: 작업 성능, 조작성, 에너지 효율.
- 분석 목표: 참가자들이 선호하는 방법을 결정합니다.

### 결론
- 다양한 방법 간에 작업 성능, 조작성 및 에너지 효율에서 차이가 나타났으며, 참가자 선호도는 상황에 따라 달라졌습니다.
