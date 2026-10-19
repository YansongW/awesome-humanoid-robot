---
$id: ent_paper_aurand_walk_like_this_stylized_locomo_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Walk Like This: Stylized Locomotion for Physics-Based Characters through Example-Driven Diffusion'
  zh: 'Walk Like This: Stylized Locomotion for Physics-Based Characters through Example-Driven Diffusion'
  ko: 'Walk Like This: Stylized Locomotion for Physics-Based Characters through Example-Driven Diffusion'
summary:
  en: We present a real-time framework for expressive legged locomotion that enables independent control over velocity and
    style. Unlike existing data-driven controllers, which typically require explicit style labels for training, our method
    efficiently leverages large-scale unstructured motion data and generalizes to unseen styles. We disentangle style from
    functional locomotion through a tailored ...
  zh: 本文提出一个面向物理仿真角色的实时风格化腿部运动框架，可独立控制移动速度与运动风格。作者来自 Joshua Aurand、Agon Serifi、Sammy Christen、Ruben Grandia、Espen Knoop、Marco
    Hutter、Moritz Bächer 团队，核心做法是用定制采样策略训练风格编码器，将其输出作为自回归扩散模型的条件，从而把风格与功能性运动解耦，并利用大规模无结构运动数据泛化到未见风格。推理时用户只需提供风格参考片段与摇杆速度指令，扩散模型生成的运动学参考由强化学习控制器跟踪。
  ko: We present a real-time framework for expressive legged locomotion that enables independent control over velocity and
    style. Unlike existing data-driven controllers, which typically require explicit style labels for training, our method
    efficiently leverages large-scale unstructured motion data and generalizes to unseen styles. We disentangle style from
    functional locomotion through a tailored ...
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
- stylized_locomotion
- diffusion_model
- style_encoder
- reinforcement_learning
- humanoid_robot
- real_time_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-19'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-19). Bibliographic metadata from arXiv API (2610.18147);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.18147 Walk Like This: Stylized Locomotion for Physics-Based Characters through Example-Driven Diffusion'
  url: https://arxiv.org/abs/2610.18147
  date: '2026-10-13'
  accessed_at: '2026-10-19'
---

## 概述

该工作针对现有数据驱动控制器通常依赖显式风格标签训练、难以泛化到新风格的问题，提出一种将风格与功能性运动分离的实时腿部运动框架。方法上，作者设计定制采样策略训练风格编码器，使其输出条件化一个自回归扩散模型，从而能够高效利用大规模无结构运动数据。推理阶段，用户给出风格参考片段和摇杆速度指令，扩散模型生成运动学参考，再由强化学习控制器在物理仿真中跟踪执行。为提升用户可控性与风格化强度，作者还引入注意力偏置机制与速度指令修正策略。实验在仿真中的物理人形角色与真实机器人上验证了鲁棒实时控制与连续风格调制能力。

## 核心内容

### 问题背景
现有数据驱动的腿部运动控制器通常需要显式的风格标签才能训练，这限制了其对大规模无结构运动数据的利用，也使其难以泛化到训练中未见的风格。作者希望实现速度与风格的独立控制，并让系统能够从无标注数据中学习风格。

### 方法
- **风格与功能解耦**：通过一种定制采样策略训练风格编码器，将风格信息从功能性运动中分离出来。
- **扩散模型条件化**：风格编码器的输出作为自回归扩散模型的条件，用于生成运动学参考。
- **推理接口**：用户提供一段风格参考片段与摇杆速度指令，扩散模型据此生成参考运动，再由强化学习控制器跟踪。
- **可控性增强**：提出注意力偏置机制与速度指令修正策略，以改善用户可控性与风格化强度。

### 实验设置
方法在仿真中的物理人形角色以及一台真实机器人上进行验证。摘要未披露具体训练数据规模、硬件型号或对比基线等细节。

### 关键结果
实验展示了鲁棒的实时控制能力与连续的风格调制效果，并能够泛化到未见风格。作者指出结果最好通过补充视频查看（https://www.youtube.com/watch?v=roFnS6N7nJ4）。

### 结论
该框架无需显式风格标签即可利用大规模无结构运动数据，实现速度与风格的独立实时控制，并在仿真人形角色与真实机器人上得到验证。

## Overview

We present a real-time framework for expressive legged locomotion that enables independent control over velocity and style. Unlike existing data-driven controllers, which typically require explicit style labels for training, our method efficiently leverages large-scale unstructured motion data and generalizes to unseen styles. We disentangle style from functional locomotion through a tailored sampling strategy used to train a style encoder whose output conditions an autoregressive diffusion model. During inference, the user provides a style reference clip and a joystick velocity command. The diffusion model then generates a kinematic reference tracked by a reinforcement learning controller. To improve user controllability and stylization strength, we propose an attention biasing mechanism and a velocity command correction strategy. We demonstrate our method on a physics-based humanoid character in simulation and on a physical robot, showcasing robust real-time control and continuous style modulation. The results can be best seen in our supplemental video (https://www.youtube.com/watch?v=roFnS6N7nJ4).

## 参考
- https://arxiv.org/abs/2610.18147
