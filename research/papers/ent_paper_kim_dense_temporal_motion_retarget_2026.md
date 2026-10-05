---
$id: ent_paper_kim_dense_temporal_motion_retarget_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Dense Temporal Motion Retargeting for Legged Robots
  zh: Dense Temporal Motion Retargeting for Legged Robots
  ko: Dense Temporal Motion Retargeting for Legged Robots
summary:
  en: Legged robots can learn expressive whole-body skills from the motions of humans and animals. Due to the morphology gap
    between the source and the robot, however, the motion must be tailored to the dynamic properties of the robot. In particular,
    dynamic motions such as a jump require careful adjustment, since their timing and control are interdependent. We propose
    dense temporal motion retargeting ...
  zh: 本文提出稠密时间运动重定向方法 DTMR（dense temporal motion retargeting），由 Jaeryeong Kim、Taerim Yoon、Jin Cheng、Sungjoon Choi、Stelian
    Coros 完成。该方法在单一优化中联合优化时序与控制，且时序在每个控制步上都被调整，从而只对确实需要改变时序的运动片段进行形变。求解采用 GPU 上并行运行的采样型模型预测控制（MPC）。
  ko: Legged robots can learn expressive whole-body skills from the motions of humans and animals. Due to the morphology gap
    between the source and the robot, however, the motion must be tailored to the dynamic properties of the robot. In particular,
    dynamic motions such as a jump require careful adjustment, since their timing and control are interdependent. We propose
    dense temporal motion retargeting ...
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
- motion_retargeting
- humanoid_robots
- model_predictive_control
- whole_body_control
- temporal_optimization
- sim_to_real
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-05'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-05). Bibliographic metadata from arXiv API (2609.38617);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2609.38617 Dense Temporal Motion Retargeting for Legged Robots
  url: https://arxiv.org/abs/2609.38617
  date: '2026-09-29'
  accessed_at: '2026-10-05'
- id: src_002
  type: website
  title: Project page
  url: https://jaeryeongnicolekim.com/Dense-Temporal-Motion-Retargeting-For-Legged-Robots/
  accessed_at: '2026-10-05'
---

## 概述

足式机器人可以从人类与动物的运动中学习富有表现力的全身技能，但源运动与机器人之间存在形态差异，运动必须针对机器人的动力学特性进行调整，跳跃等动态运动尤其需要精细处理，因为其时序与控制相互耦合。为此作者提出 DTMR，在同一个优化中联合求解时序与控制，其中“稠密”指时序在每个控制步上都被调整，使方法只形变那些真正需要改变时序的运动部分。该问题通过 GPU 上并行执行的采样型模型预测控制（MPC）求解。作者在两小时人类运动数据、四款人形机器人上与基线方法对比，结果显示 DTMR 整体更优，在动态运动上优势尤为明显；允许更大的时间形变会带来更精确的重定向；与同样优化时间维度的基线相比，DTMR 在相同形变预算下重定向更精确，且约快 19 倍。最后，基于该方法生成参考轨迹训练的策略可迁移到真实人形机器人上。

## 核心内容

### 问题背景
足式机器人能够从人类和动物的运动中习得富有表现力的全身技能。然而源运动与机器人之间存在形态差异，运动必须被改造以匹配机器人的动力学特性。跳跃等动态运动对时序与控制之间的相互依赖尤为敏感，因此需要谨慎调整。

### 方法
作者提出稠密时间运动重定向（dense temporal motion retargeting, DTMR）：
- 在单一优化中联合优化时序与控制；
- “稠密”意味着时序在每个控制步上都被调整，因此 DTMR 只形变那些需要改变时序的运动部分；
- 该问题使用采样型模型预测控制（MPC）在 GPU 上并行求解。

### 实验设置
- 数据：两小时人类运动；
- 平台：四款人形机器人；
- 对比：与基线方法进行比较，其中包括一个同样优化时间维度的基线。

### 关键结果
- DTMR 优于基线方法，在动态运动上表现尤为突出；
- 允许更多时间形变会带来更精确的重定向；
- 在与优化时间维度的基线对比中，DTMR 在相同形变预算下重定向更精确，同时约快 19 倍；
- 在 DTMR 生成的参考轨迹上训练的策略可迁移到真实人形机器人。

### 结论
DTMR 通过在单一优化中稠密地联合调整时序与控制，实现了对动态运动更精确的重定向，并在效率上显著优于优化时间维度的基线，且其参考轨迹可支撑策略向真实人形机器人的迁移。

## Overview

Legged robots can learn expressive whole-body skills from the motions of humans and animals. Due to the morphology gap between the source and the robot, however, the motion must be tailored to the dynamic properties of the robot. In particular, dynamic motions such as a jump require careful adjustment, since their timing and control are interdependent. We propose dense temporal motion retargeting (DTMR), which jointly optimizes timing and control within a single optimization, where dense means that the timing is adjusted for every control step. This dense formulation enables DTMR to deform only the parts of the motion that need a change in timing. The problem is solved with sampling-based model predictive control (MPC) in parallel on a GPU. We evaluate DTMR against baselines on two hours of human motion with four humanoid robots, where the results show that DTMR outperforms baseline methods, particularly on dynamic motions. We also show that allowing more temporal deformation yields more precise retargeting. We further compare DTMR with a baseline that optimizes the temporal dimension, where the result shows that DTMR retargets more precisely under the same deformation budget while being ~19x faster. Lastly, policies trained on our references transfer to a real humanoid robot.

## 参考
- https://arxiv.org/abs/2609.38617
- https://jaeryeongnicolekim.com/Dense-Temporal-Motion-Retargeting-For-Legged-Robots/
