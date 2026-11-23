---
$id: ent_paper_zhang_body_schema_policy_body_as_the_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Body Schema Policy: Body as the Vision-Action Interface for Efficient Robot Loco-Manipulation'
  zh: 'Body Schema Policy: Body as the Vision-Action Interface for Efficient Robot Loco-Manipulation'
  ko: 'Body Schema Policy: Body as the Vision-Action Interface for Efficient Robot Loco-Manipulation'
summary:
  en: 'Currently, robots can learn whole-body loco-manipulation through scale: the strongest policies have billions of parameters
    and still need task-specific fine-tuning. Humans have limited processing capacity, yet learn and act efficiently through
    a body schema that organizes what they see and how they move. We introduce Body Schema Policy (BSP), an imitation learning
    policy that builds such a schema ...'
  zh: Body Schema Policy（BSP）是一种将“身体图式”嵌入视觉-动作接口的模仿学习策略，由 Lechen Zhang、Chenyuan Chen、Muxin Zhou、Zewen He 与 Yoshihiko Nakamura
    提出。其潜在身体图式把关节与连杆 token 放置在机器人运动学树上，并通过学习到的螺旋运动在连杆间传递特征。在九个 Unitree G1 仿真全身任务上，BSP 以少 75 倍的参数量匹配 Ψ_0 人形基础模型，并将 Diffusion
    Policy 的成功率提升近一倍。
  ko: 'Currently, robots can learn whole-body loco-manipulation through scale: the strongest policies have billions of parameters
    and still need task-specific fine-tuning. Humans have limited processing capacity, yet learn and act efficiently through
    a body schema that organizes what they see and how they move. We introduce Body Schema Policy (BSP), an imitation learning
    policy that builds such a schema ...'
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
- imitation_learning
- body_schema
- loco_manipulation
- humanoid_robot
- vision_action_interface
- unitree_g1
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-23'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-23). Bibliographic metadata from arXiv API (2611.22713);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.22713 Body Schema Policy: Body as the Vision-Action Interface for Efficient Robot Loco-Manipulation'
  url: https://arxiv.org/abs/2611.22713
  date: '2026-11-17'
  accessed_at: '2026-11-23'
---

## 概述

当前全身移动操作策略依赖规模扩张，最强策略拥有数十亿参数且仍需任务特定微调；而人类处理能力有限，却借助身体图式高效地组织视觉与动作。BSP 将这一思想作为归纳偏置引入模仿学习：在潜在空间中把关节与连杆 token 组织到机器人运动学树上，用学习到的螺旋运动在连杆之间传递特征，并让每个身体部位通过“身体查询视觉”取回自身的视觉证据，用以条件化其动作去噪。该设计使 BSP 生成动作块的速度快于所比较的所有策略，并在无空间监督的情况下自发形成紧凑的、部位特异的视觉读出：操作指令强烈依赖任务物体，而移动指令对场景的响应更为宽泛。在九个 Unitree G1 仿真全身任务上，BSP 以少 75 倍的参数量达到 Ψ_0 人形基础模型的水平，成功率接近 Diffusion Policy 的两倍，并在真实 G1 与 Fetch 移动操作平台上得到同样验证。

## 核心内容

### 问题背景
现有机器人全身移动操作能力主要靠规模堆叠获得：最强策略参数量达数十亿，且仍需针对具体任务做微调。相比之下，人类处理能力有限，却能通过身体图式（body schema）高效地组织所见与所动。作者据此提出将身体图式作为视觉-动作接口中的归纳偏置。

### 方法
- **Body Schema Policy（BSP）**：一种模仿学习策略，把身体图式构建进视觉-动作接口。
- **潜在身体图式**：将关节 token 与连杆 token 放置在机器人的运动学树上，连杆之间的特征传递由学习到的螺旋运动（screw motions）承载。
- **身体查询视觉**：每个身体部位检索属于自己的视觉证据，并用该证据条件化其动作的去噪过程。
- 借助上述归纳偏置，BSP 返回动作块的速度快于论文所比较的所有策略。
- 无需空间监督，即可自发出现紧凑的、身体部位特异的视觉读出：操作类指令强烈依赖任务物体，移动类指令则对场景作出更宽泛的响应。

### 实验设置
- 仿真：九个 Unitree G1 全身任务。
- 真实平台：一台真实 G1，以及一台 Fetch 移动操作机器人。

### 关键结果
- 在九个仿真 Unitree G1 全身任务上，BSP 以少 75 倍的参数量匹配 Ψ_0 人形基础模型的表现。
- 在同一批任务上，BSP 的成功率接近 Diffusion Policy 的两倍。
- 上述结论在真实 G1 与 Fetch 移动操作平台上同样成立。

### 结论
将身体图式作为视觉-动作接口的结构性先验，可以在远小得多的参数规模下取得与大型人形基础模型相当的性能，并显著优于 Diffusion Policy，且在真实机器人上可复现。

## Overview

Currently, robots can learn whole-body loco-manipulation through scale: the strongest policies have billions of parameters and still need task-specific fine-tuning. Humans have limited processing capacity, yet learn and act efficiently through a body schema that organizes what they see and how they move. We introduce Body Schema Policy (BSP), an imitation learning policy that builds such a schema into the vision-action interface. Its latent body schema places joint and link tokens on the robot's kinematic tree, where learned screw motions carry features between links. Through body-queried vision, each body part retrieves its own visual evidence, which conditions the denoising of its actions. With this inductive bias, BSP returns an action chunk faster than any policy we compare. Compact, body-specific visual readouts also emerge without spatial supervision: manipulation commands depend strongly on task objects, while locomotion commands respond more broadly to the scene. On nine simulated Unitree G1 whole-body tasks, BSP matches the $Ψ_0$ humanoid foundation model with $75\times$ fewer parameters and nearly doubles Diffusion Policy's success. The same holds on a real G1 and a Fetch mobile manipulator.

## 参考
- https://arxiv.org/abs/2611.22713
