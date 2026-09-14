---
$id: ent_paper_xu_thrive_therapeutic_humanoid_ro_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'THRIVE: Therapeutic Humanoid Robot In Virtual Environment'
  zh: 'THRIVE: Therapeutic Humanoid Robot In Virtual Environment'
  ko: 'THRIVE: Therapeutic Humanoid Robot In Virtual Environment'
summary:
  en: This paper presents THRIVE (Therapeutic Humanoid Robot In Virtual Environment), an at-home rehabilitation platform that
    integrates a suite of virtual-reality upper-body rehabilitation games, a real-time camera-based motion-tracking system,
    and a socially interactive robot therapist. The system is designed for therapy and intervention in children with upper-limb
    motor impairments, which can be ...
  zh: THRIVE（虚拟环境中的治疗性人形机器人）是一个面向家庭的上肢康复平台，由Jin Xu、Yu-Ping Chen和Ayanna Howard提出，整合了虚拟现实康复游戏、基于摄像头的实时运动追踪系统以及社交互动型机器人治疗师。其核心贡献在于通过可定制的游戏任务和机器人无关的模块化设计，为儿童上肢运动障碍提供持续、有趣且可扩展的居家治疗途径。
  ko: This paper presents THRIVE (Therapeutic Humanoid Robot In Virtual Environment), an at-home rehabilitation platform that
    integrates a suite of virtual-reality upper-body rehabilitation games, a real-time camera-based motion-tracking system,
    and a socially interactive robot therapist. The system is designed for therapy and intervention in children with upper-limb
    motor impairments, which can be ...
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- humanoid_rehabilitation
- virtual_reality_therapy
- upper_limb_motor_impairment
- robot_therapist
- home_rehabilitation
- modular_robotics
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-17'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-08-17). Bibliographic metadata from arXiv API (2608.14462);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2608.14462 THRIVE: Therapeutic Humanoid Robot In Virtual Environment'
  url: https://arxiv.org/abs/2608.14462
  date: '2026-08-14'
  accessed_at: '2026-08-17'
---

## 概述

THRIVE系统专为儿童上肢运动障碍设计，利用虚拟现实游戏（如击打、抓取等任务）结合摄像头运动追踪，实时捕捉儿童的运动学表现。系统配备的机器人治疗师（可物理或虚拟形式部署）提供自适应动态反馈，以激励儿童并引导其动作朝向治疗目标。通过将治疗游戏与机器人实体解耦，THRIVE支持多种机器人形态，使其经济实惠、可扩展，并易于在家庭环境中长期使用。

## 核心内容

### 问题背景
上肢运动障碍儿童需要持续、任务导向的练习以改善功能，但传统康复常受限于医院环境、缺乏趣味性和依从性。THRIVE旨在通过家庭化、游戏化的方式解决这一挑战。

### 方法
THRIVE包含三个核心组件：
- **虚拟现实游戏套件**：新设计的游戏针对功能性伸展、抓握和物体操作，通过可定制的击打、弹跳、接住和抓取任务实现。
- **摄像头运动追踪系统**：实时捕捉儿童在游戏中的运动学数据，无需穿戴设备。
- **机器人治疗师**：可作为物理机器人教练或远程临场虚拟代理部署，提供自适应动态反馈，激励儿童并指导动作。

系统设计的关键创新在于将治疗游戏与机器人实体解耦，使平台能够在一个模块化系统中支持不同机器人形态，实现机器人无关（robot-agnostic）的架构。

### 实验设置与关键结果
摘要未提供具体实验数据或量化结果，但强调系统设计旨在实现经济性、可扩展性和家庭适应性。其模块化架构为长期持续使用提供了实际路径，有望提升儿童上肢治疗的参与度和一致性。

### 结论
THRIVE通过整合游戏化康复、实时追踪和社交机器人反馈，为儿童上肢运动障碍提供了一种可负担、可扩展的居家治疗解决方案。其机器人无关设计增强了平台的通用性和未来适配性，为更持续、更吸引人的康复干预奠定了基础。

## Overview

This paper presents THRIVE (Therapeutic Humanoid Robot In Virtual Environment), an at-home rehabilitation platform that integrates a suite of virtual-reality upper-body rehabilitation games, a real-time camera-based motion-tracking system, and a socially interactive robot therapist. The system is designed for therapy and intervention in children with upper-limb motor impairments, which can be improved through consistent, task-specific practice. THRIVE features a set of newly designed, engaging games that target functional reaching, grasping, and object-manipulation movements through customizable popping, hitting, catching, and grabbing tasks, while the camera-based tracking system captures the child's kinematic performance during play. A robot therapist - deployable either as a physical robotic coach or as a remote-presence virtual agent - delivers adaptive, dynamic feedback to motivate the child and guide their movements toward therapeutic goals. THRIVE decouples the therapeutic games from the robot embodiment, extending the platform to support various embodiments and different robots within one modular system. This robot-agnostic design makes THRIVE affordable, scalable, and readily adaptable for sustained use in the home, offering a practical pathway to more consistent and engaging upper-limb therapy for children with motor function impairments.

## 参考
- https://arxiv.org/abs/2608.14462
