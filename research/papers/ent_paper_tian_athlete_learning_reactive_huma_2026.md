---
$id: ent_paper_tian_athlete_learning_reactive_huma_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ATHLETE: Learning Reactive Humanoid Tennis via Trajectory-Guided Motion Matching'
  zh: 'ATHLETE: Learning Reactive Humanoid Tennis via Trajectory-Guided Motion Matching'
  ko: 'ATHLETE: Learning Reactive Humanoid Tennis via Trajectory-Guided Motion Matching'
summary:
  en: Humanoid tennis requires reactive whole-body coordination under rapidly changing ball dynamics, yet collecting task-specific
    motion-capture demonstrations that cover diverse approach states, contact locations, and timing conditions is costly.
    Inspired by how humans acquire new skills by combining reusable motor experience with task-specific demonstrations, we
    present ATHLETE, a framework for ...
  zh: ATHLETE 是一个从通用运动数据与普通网球视频中学习反应式人形机器人网球技能的框架，由 Zhihao Tian、Zifan Wang、Enzheng Zhu、Xun Yang、Jialong Qin、Mengbo Wang、Junwei
    Liang 提出。它结合 LAFAN1 运动数据与视频提取的击球动作，通过 Trajectory-Guided Motion Matching (TGMM) 构建任务条件下的全身参考动作，并借助基于物理的教师—学生学习与在线 DAgger
    蒸馏转化为反应式策略，再经 PPO 微调。在真实人形机器人上，正手与反手击球成功率分别达到 90.00% 与 86.67%，并能与人类选手进行多拍对打。
  ko: Humanoid tennis requires reactive whole-body coordination under rapidly changing ball dynamics, yet collecting task-specific
    motion-capture demonstrations that cover diverse approach states, contact locations, and timing conditions is costly.
    Inspired by how humans acquire new skills by combining reusable motor experience with task-specific demonstrations, we
    present ATHLETE, a framework for ...
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
- humanoid_tennis
- motion_matching
- teacher_student_learning
- dagger
- ppo
- reactive_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-12'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-12). Bibliographic metadata from arXiv API (2610.13572);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.13572 ATHLETE: Learning Reactive Humanoid Tennis via Trajectory-Guided Motion Matching'
  url: https://arxiv.org/abs/2610.13572
  date: '2026-10-09'
  accessed_at: '2026-10-12'
- id: src_002
  type: website
  title: Project page
  url: https://hazintihoa.github.io/athlete.github.io/#overview
  accessed_at: '2026-10-12'
---

## 概述

人形机器人打网球需要在快速变化的球体动力学下进行反应式全身协调，而采集覆盖多种接近状态、击球位置与时机条件的任务专用动作捕捉示范成本高昂。受人类通过组合可复用运动经验与任务专用示范来习得新技能的启发，作者提出 ATHLETE 框架，从通用运动数据与普通网球视频中学习反应式人形网球。该框架将 LAFAN1 运动数据与视频导出的击球动作结合，利用 Trajectory-Guided Motion Matching (TGMM) 构建多样化的任务条件全身参考动作。这些参考动作通过基于物理的教师—学生学习与在线 DAgger 蒸馏被转化为反应式策略，随后针对网球任务进行 PPO 微调。最终策略在部署时直接响应机器人与球的观测，无需参考动作输入。在真实人形机器人上，ATHLETE 的正手与反手击球成功率分别为 90.00% 与 86.67%，并实现了与人类选手的多拍对打。

## 核心内容

### 问题背景
人形机器人网球要求机器人在球体动力学快速变化的条件下完成反应式全身协调。然而，采集覆盖多种接近状态、击球位置与时机条件的任务专用动作捕捉示范代价高昂，这构成了学习此类技能的主要障碍。

### 方法
受人类通过组合可复用运动经验与任务专用示范来获取新技能的方式启发，作者提出 ATHLETE 框架，其核心思路是从通用运动数据与普通网球视频中学习反应式人形网球：

- **数据来源**：将 LAFAN1 运动数据与从视频中导出的击球动作相结合。
- **参考动作构建**：使用 Trajectory-Guided Motion Matching (TGMM) 构建多样化的、以任务为条件的全身参考动作。
- **策略学习**：通过基于物理的教师—学生学习与在线 DAgger 蒸馏，将上述参考动作转化为反应式策略。
- **任务微调**：在网球任务上使用 PPO 进行微调。
- **部署特性**：所得策略在部署时直接响应机器人与球的观测，不需要参考动作作为输入。

### 关键结果
在真实人形机器人上，ATHLETE 取得以下表现：

- 正手击球成功率：90.00%
- 反手击球成功率：86.67%
- 能够与人类选手进行多拍对打（multi-shot rallies）

### 结论
结果表明，ATHLETE 能够从可复用的运动数据与视频示范中学习动态的人形机器人网球技能。相关结果视频与代码发布于 https://anonymous.4open.science/w/ATHLETE2027/。

## Overview

Humanoid tennis requires reactive whole-body coordination under rapidly changing ball dynamics, yet collecting task-specific motion-capture demonstrations that cover diverse approach states, contact locations, and timing conditions is costly. Inspired by how humans acquire new skills by combining reusable motor experience with task-specific demonstrations, we present ATHLETE, a framework for learning reactive humanoid tennis from generic locomotion data and ordinary tennis videos. ATHLETE combines LAFAN1 locomotion with video-derived striking motions and uses Trajectory-Guided Motion Matching (TGMM) to construct diverse task-conditioned whole-body references. These references are transformed into a reactive policy through physics-based teacher--student learning with online DAgger distillation, followed by PPO fine-tuning for the tennis task. The resulting policy responds directly to robot and ball observations without requiring reference-motion inputs at deployment. On a real humanoid robot, ATHLETE achieves forehand and backhand hit rates of $90.00\%$ and $86.67\%$, respectively, and enables multi-shot rallies with human players. These results demonstrate that ATHLETE can learn dynamic humanoid tennis skills from reusable locomotion data and video demonstrations. Result videos and code can be found at https://anonymous.4open.science/w/ATHLETE2027/.

## 参考
- https://arxiv.org/abs/2610.13572
- https://hazintihoa.github.io/athlete.github.io/#overview
