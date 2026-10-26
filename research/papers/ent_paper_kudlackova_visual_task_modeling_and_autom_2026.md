---
$id: ent_paper_kudlackova_visual_task_modeling_and_autom_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Visual Task Modeling and Automated Planning for Humanoid Robots in Education of Individuals with Autism Spectrum Disorder
  zh: Visual Task Modeling and Automated Planning for Humanoid Robots in Education of Individuals with Autism Spectrum Disorder
  ko: Visual Task Modeling and Automated Planning for Humanoid Robots in Education of Individuals with Autism Spectrum Disorder
summary:
  en: In robot-assisted education, a robot must understand how to complete a task in order to effectively guide a student
    through it. We present a novel method that enables a semi-autonomous, camera-equipped robot to recognise the task goal
    and plan actions to achieve it. Our work focuses on Shoebox Tasks, an activity commonly used in the education of individuals
    with Autism Spectrum Disorder (ASD). ...
  zh: 本文提出一种面向自闭症谱系障碍（ASD）教育场景的方法，使配备摄像头的半自主机器人能够识别 Shoebox Tasks 的任务目标并自动规划动作。作者开发了一个求解器，利用基于视觉的 Large Language Model 将任务照片转换为
    PDDL 表示并生成行动计划，同时在 Nao 机器人上实现了可执行多种 Shoebox Tasks 的交互接口。该系统仅以拍摄图像为输入，教师无需编程知识，且经适配后可集成到多种教育机器人中。
  ko: In robot-assisted education, a robot must understand how to complete a task in order to effectively guide a student
    through it. We present a novel method that enables a semi-autonomous, camera-equipped robot to recognise the task goal
    and plan actions to achieve it. Our work focuses on Shoebox Tasks, an activity commonly used in the education of individuals
    with Autism Spectrum Disorder (ASD). ...
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
- humanoid_robot
- autism_spectrum_disorder
- task_planning
- pddl
- vision_language_model
- robot_assisted_education
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-26'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-26). Bibliographic metadata from arXiv API (2610.27162);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2610.27162 Visual Task Modeling and Automated Planning for Humanoid Robots in Education of Individuals with
    Autism Spectrum Disorder
  url: https://arxiv.org/abs/2610.27162
  date: '2026-10-19'
  accessed_at: '2026-10-26'
---

## 概述

在机器人辅助教育中，机器人需要先理解任务如何完成，才能有效引导学生。本文聚焦常用于 ASD 个体教育的 Shoebox Tasks，这类活动的目标可直接从其视觉结构中推断。作者构建了一个求解器，借助基于视觉的 Large Language Model 把 Shoebox Task 的照片转化为 PDDL 表示，并据此生成求解动作计划。研究还实现了机器人接口，使 Nao 机器人能够自主执行多种 Shoebox Tasks，并通过动作演示、语音指令或手势提示下一步或报告检测到的失败。该系统仅依赖拍摄图像作为输入，教师无需编程专业知识，适配后的接口可集成到多种教育机器人中，旨在强化 ASD 学生的学习机会并激发其对机器人技术的兴趣。

## 核心内容

### 问题背景

在机器人辅助教育中，机器人必须理解任务的完成方式，才能有效引导学生。本文针对自闭症谱系障碍（ASD）个体教育中常用的 Shoebox Tasks 展开研究：这类任务的设计使目标可以直接从其视觉结构中推断出来，因此适合由视觉系统自动识别。

### 方法

- **任务目标识别与规划**：作者开发了一个求解器，使用基于视觉的 Large Language Model 将 Shoebox Task 的照片转换为 Planning Domain Definition Language（PDDL）表示，并生成用于求解该任务的动作计划。
- **机器人接口**：实现了使 Nao 机器人能够自主执行多种 Shoebox Tasks 的接口，机器人可通过动作演示、语音指令或手势来建议下一步，或对检测到的失败发出信号。
- **输入与使用门槛**：求解器仅以拍摄的图像作为输入，教师无需具备编程专业知识。
- **可移植性**：经过适配的机器人接口使该求解器能够集成到多种教育机器人中。

### 实验设置与关键结果

摘要未提供具体实验设置、数据集规模或定量结果。

### 结论

特殊教育需求领域的研究表明，ASD 学生可从机器人辅助教学中显著受益。该系统旨在强化这些学习机会，同时培养 ASD 个体对机器人技术的兴趣。

## Overview

In robot-assisted education, a robot must understand how to complete a task in order to effectively guide a student through it. We present a novel method that enables a semi-autonomous, camera-equipped robot to recognise the task goal and plan actions to achieve it. Our work focuses on Shoebox Tasks, an activity commonly used in the education of individuals with Autism Spectrum Disorder (ASD). These tasks are designed so that the goal can be inferred directly from their visual structure. We have developed a solver that uses a vision-based Large Language Model to convert photos of a Shoebox Task into a Planning Domain Definition Language (PDDL) representation and generate action plans for solving it. We have also implemented a robotic interface that enables a Nao robot to autonomously execute various Shoebox Tasks and assist a student by suggesting next steps or signalling detected failures through action demonstrations, voice commands, or gestures. With an adapted robotic interface, the solver can be integrated into a variety of educational robots. No programming expertise is required from teachers, and the solver operates exclusively on captured images as input. Research in special educational needs indicates that students with ASD can benefit substantially from robot-assisted teaching, and our system aims to strengthen these learning opportunities while also fostering interest in robotics among individuals with ASD.

## 参考
- https://arxiv.org/abs/2610.27162
