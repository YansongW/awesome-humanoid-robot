---
$id: ent_paper_wang_proof_perceptive_robustness_vi_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PROOF: Perceptive Robustness via Out-of-Distribution Fallback for Legged Locomotion'
  zh: 'PROOF: Perceptive Robustness via Out-of-Distribution Fallback for Legged Locomotion'
  ko: 'PROOF: Perceptive Robustness via Out-of-Distribution Fallback for Legged Locomotion'
summary:
  en: Vision-based perceptive locomotion has enabled legged robots to achieve agile and terrain-aware locomotion across complex
    environments. However, the reliability of such systems heavily depends on visual observations, which are inherently susceptible
    to occlusion, reflective surfaces, and illumination variations, often resulting in catastrophic locomotion failures under
    degraded perception ...
  zh: PROOF 是一个面向腿足机器人感知式运动的鲁棒框架，由 Siyuan Wang、Dongjie Zhu、Jinxuan Lu、Wenjun Xu、Jiankun Wang 提出，采用两阶段教师—学生学习范式显式建模感知可靠性。教师同时学习感知驱动行为与本体感知回退行为，学生则预测外感知特征的不确定性并在分布外输入下抑制这些特征。作者在搭载
    RealSense D435 深度相机的 Unitree Go2 四足机器人上进行了真实环境验证，在正常视觉条件下完成大间隙跨越、高台与窄梁等高动态跑酷动作，在严重遮挡与强光照变化下仍保持稳定运动。
  ko: Vision-based perceptive locomotion has enabled legged robots to achieve agile and terrain-aware locomotion across complex
    environments. However, the reliability of such systems heavily depends on visual observations, which are inherently susceptible
    to occlusion, reflective surfaces, and illumination variations, often resulting in catastrophic locomotion failures under
    degraded perception ...
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
- legged_locomotion
- perceptive_locomotion
- teacher_student_learning
- out_of_distribution_detection
- proprioceptive_fallback
- sim_to_real
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-16'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-16). Bibliographic metadata from arXiv API (2611.18305);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.18305 PROOF: Perceptive Robustness via Out-of-Distribution Fallback for Legged Locomotion'
  url: https://arxiv.org/abs/2611.18305
  date: '2026-11-13'
  accessed_at: '2026-11-16'
---

## 概述

基于视觉的感知式运动让腿足机器人能够在复杂环境中实现敏捷且地形感知的行走，但这类系统高度依赖视觉观测，而视觉本身容易受到遮挡、反光表面与光照变化的影响，在感知退化时往往导致灾难性的运动失败。PROOF 针对这一问题提出了一种在严重视觉干扰下仍能保持鲁棒运动的感知式运动框架，其核心是两阶段教师—学生学习范式，将感知可靠性显式纳入学习过程。教师策略同时掌握感知驱动行为与本体感知回退行为，学生策略则对外感知特征给出不确定性预测，并在分布外输入出现时抑制这些特征，从而平滑地退回到不依赖视觉的行为。作者在配备 RealSense D435 深度相机的 Unitree Go2 四足机器人上开展真实世界评估，正常视觉条件下机器人可完成跨越较大间隙、登上高台、通过窄梁等高动态跑酷动作，而在严重遮挡与强烈光照变化等视觉退化情形下仍能维持稳定、鲁棒的运动表现。

## 核心内容

### 问题背景

基于视觉的感知式运动使腿足机器人能够在复杂地形上实现敏捷、地形感知的行走，但系统可靠性高度依赖视觉观测。视觉本身易受遮挡、反光表面和光照变化影响，在感知条件退化时常常引发灾难性的运动失败。因此，如何在视觉输入不可靠时仍保持稳定运动，是该领域的关键挑战。

### 方法

PROOF（Perceptive Robustness via Out-of-Distribution Fallback for Legged Locomotion）是一个面向严重视觉干扰的感知式运动框架，其核心是两阶段教师—学生学习范式，显式地对感知可靠性建模：

- **教师阶段**：教师策略同时学习两类行为，一类由感知驱动，另一类是基于本体感知的回退行为。
- **学生阶段**：学生策略预测外感知特征及其不确定性，并在遇到分布外输入时抑制这些外感知特征，从而触发回退到不依赖视觉的行为模式。

### 实验设置

作者在真实世界环境中进行评估，实验平台为搭载 RealSense D435 深度相机的 Unitree Go2 四足机器人。

### 关键结果

- 在正常视觉条件下，该方法使机器人成功完成高动态跑酷动作，包括跨越较大间隙、通过高台以及窄梁地形。
- 在严重视觉退化条件下，例如重度遮挡与强烈光照变化，机器人仍能保持稳定且鲁棒的运动性能。

### 结论

PROOF 通过显式建模感知可靠性并引入分布外回退机制，使腿足机器人在视觉感知严重退化时仍能维持稳定运动，同时在正常视觉条件下保持高动态地形通过能力。

## Overview

Vision-based perceptive locomotion has enabled legged robots to achieve agile and terrain-aware locomotion across complex environments. However, the reliability of such systems heavily depends on visual observations, which are inherently susceptible to occlusion, reflective surfaces, and illumination variations, often resulting in catastrophic locomotion failures under degraded perception conditions. In this paper, we present PROOF (Perceptive Robustness via Out-of-Distribution Fallback for Legged Locomotion), a perceptive locomotion framework that enables robust locomotion under severe visual disturbances. Our method adopts a two-stage teacher-student learning paradigm that explicitly models perception reliability: the teacher learns both perception-driven and proprioceptive fallback behaviors, while the student predicts exteroceptive features with uncertainty and suppresses them under out-of-distribution inputs. We evaluate our method on a Unitree Go2 quadruped equipped with a RealSense D435 depth camera in real-world settings. Under normal visual conditions, our method enables the robot to successfully perform high-dynamic parkour maneuvers, including traversing large gaps, elevated platforms, and narrow beam terrains. Under severe visual degradation, such as heavy occlusion and strong illumination changes, the robot continues to maintain stable and robust locomotion performance.

## 参考
- https://arxiv.org/abs/2611.18305
