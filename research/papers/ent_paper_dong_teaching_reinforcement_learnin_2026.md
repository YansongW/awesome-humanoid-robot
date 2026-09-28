---
$id: ent_paper_dong_teaching_reinforcement_learnin_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Teaching Reinforcement Learning and Humanoid Robotics to High-School Students: An Expert-Validated Curriculum Design
    on a Low-Cost Open Platform'
  zh: 'Teaching Reinforcement Learning and Humanoid Robotics to High-School Students: An Expert-Validated Curriculum Design
    on a Low-Cost Open Platform'
  ko: 'Teaching Reinforcement Learning and Humanoid Robotics to High-School Students: An Expert-Validated Curriculum Design
    on a Low-Cost Open Platform'
summary:
  en: Lower cost open source robots and reinforcement learning (RL) simulation tools create new opportunities for precollege
    students to engage with contemporary robotics. However, translating a complete research workflow, spanning mechanical
    assembly, electrical setup, simulation, policy learning, system identification, and physical deployment, into a coherent
    course for novice learners remains ...
  zh: 本文提出了一套面向高中生的机器人课程框架，围绕一个共享的机器人实体，将机械装配、电路搭建、仿真、策略学习、系统辨识与实物部署等完整科研流程整合为连贯的教学内容。该框架由 Yuanzhe Dong、Jie Cao、Shuman Wang
    设计，并经五位来自机器人研究、工程、中学 STEM 教育与课程设计领域的专家形成性评审。课程以低成本开源人形机器人为载体，学生两人一组完成装配、在仿真中训练行走策略并部署到实物平台。
  ko: Lower cost open source robots and reinforcement learning (RL) simulation tools create new opportunities for precollege
    students to engage with contemporary robotics. However, translating a complete research workflow, spanning mechanical
    assembly, electrical setup, simulation, policy learning, system identification, and physical deployment, into a coherent
    course for novice learners remains ...
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
- humanoid_robotics
- reinforcement_learning
- curriculum_design
- precollege_stem_education
- open_source_robot
- simulation_to_reality
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-28'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-28). Bibliographic metadata from arXiv API (2609.25674);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.25674 Teaching Reinforcement Learning and Humanoid Robotics to High-School Students: An Expert-Validated
    Curriculum Design on a Low-Cost Open Platform'
  url: https://arxiv.org/abs/2609.25674
  date: '2026-09-22'
  accessed_at: '2026-09-28'
---

## 概述

针对低成本开源机器人与强化学习仿真工具为大学前学生带来的新机会，本文尝试解决如何将完整科研工作流转化为适合初学者的课程这一难题。作者提出一个整合式课程框架，围绕同一机器人实体组织教学活动，采用并行学科主线、基于技术依赖关系的排序、仿真与硬件的渐进式整合、分层性能检查点，以及兼顾协作与个人责任的机制。该框架通过迭代设计流程开发，并经过五位专家的形成性评审，专家反馈指出了三组核心设计张力：真实性与认知负荷、系统集成与及时可见的进展、团队构建与个人责任。这些张力最终塑造了论文所呈现的框架。作者指出，未来仍需开展课堂研究以考察实际实施与学生学情。

## 核心内容

### 问题背景
低成本开源机器人与强化学习（RL）仿真工具的出现，为大学前学生接触当代机器人技术创造了新机会。但将一条完整的研究工作流——涵盖机械装配、电路搭建、仿真、策略学习、系统辨识与实物部署——转化为面向初学者的连贯课程，仍然具有挑战性。

### 方法
作者提出一个整合式机器人课程框架，其核心思路是围绕一个共享的机器人实体来组织各项活动。框架包含以下设计要素：
- 并行学科主线
- 基于技术依赖关系的教学排序
- 仿真与硬件的渐进式整合
- 分层性能检查点
- 用于平衡协作工作与个人责任的机制

### 课程实例
作者以一套高中课程为例说明该框架。课程围绕一个机器人项目展开：学生两人一组装配一台开源人形机器人，在仿真中训练行走策略，并将其部署到实物平台上。

### 开发与专家评审
该框架通过迭代设计流程开发，其中包括五位专家的形成性评审，专家分别来自机器人研究、工程、中学 STEM 教育与课程设计领域。专家反馈凸显了三组核心设计张力：
- 真实性与认知负荷
- 系统集成与及时可见的进展
- 团队构建与个人责任

这些张力影响了论文最终呈现的框架。

### 结论
本工作为将机器人研究工作流改造为跨学科大学前课程提供了一种结构化方法。作者强调，未来仍需开展课堂研究，以考察课程的实施情况与学生的学习效果。

## Overview

Lower cost open source robots and reinforcement learning (RL) simulation tools create new opportunities for precollege students to engage with contemporary robotics. However, translating a complete research workflow, spanning mechanical assembly, electrical setup, simulation, policy learning, system identification, and physical deployment, into a coherent course for novice learners remains challenging. We present an integrated robotics course framework that organizes these activities around a shared robotic artifact. The framework combines parallel disciplinary tracks, sequencing based on technical dependencies, progressive integration of simulation and hardware, layered performance checkpoints, and structures for balancing collaborative work with individual accountability. We illustrate the framework through a high school curriculum organized around a robot project in which pairs of students assemble an open source humanoid robot, train a walking policy in simulation, and deploy it on the physical platform. The framework was developed through an iterative design process that included formative review by five experts in robotics research, engineering, secondary STEM education, and curriculum design. Expert feedback highlighted three central design tensions: authenticity versus cognitive load, system integration versus timely visible progress, and team construction versus individual accountability. These tensions informed the final framework presented in this paper. This work offers a structured approach for adapting robotics research workflows into interdisciplinary precollege courses; future classroom studies are needed to examine implementation and student learning.

## 参考
- https://arxiv.org/abs/2609.25674
