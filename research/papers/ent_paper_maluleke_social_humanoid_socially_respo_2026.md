---
$id: ent_paper_maluleke_social_humanoid_socially_respo_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Social Humanoid: Socially Responsive Human-Humanoid Interaction'
  zh: 'Social Humanoid: Socially Responsive Human-Humanoid Interaction'
  ko: 'Social Humanoid: Socially Responsive Human-Humanoid Interaction'
summary:
  en: Humanoid robots are typically trained as solitary agents, leaving them unable to coordinate physically with human partners
    who naturally anticipate and adjust to one another. To bridge this gap, we present Social Humanoid, a hierarchical system
    that generates and executes socially responsive whole-body motion on a 29-DoF Unitree G1 conditioned on a human partner's
    motion. Its high-level policy ...
  zh: Social Humanoid 是一个分层系统，能让 29-DoF Unitree G1 人形机器人根据人类伙伴的动作生成并执行具有社会响应性的全身运动。该系统由 Vongani H. Maluleke、James Ni、Kie Horiuchi、Lea
    Wilken、Jiahui Lei、Evonne Ng、Roei Herzig、Jitendra Malik 等人提出，高层策略通过共享 token 化表示对人类与人形运动进行灵活的序列建模，低层全身跟踪控制器负责在机器人上执行生成的动作。作者还提出两阶段自适应重定向流程，并基于五个动作捕捉数据集构建了包含
    260 小时人-人形交互的 HHI 基准。
  ko: Humanoid robots are typically trained as solitary agents, leaving them unable to coordinate physically with human partners
    who naturally anticipate and adjust to one another. To bridge this gap, we present Social Humanoid, a hierarchical system
    that generates and executes socially responsive whole-body motion on a 29-DoF Unitree G1 conditioned on a human partner's
    motion. Its high-level policy ...
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
- human_humanoid_interaction
- social_humanoid
- whole_body_control
- motion_retargeting
- humanoid_locomotion
- motion_capture
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-09'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-09). Bibliographic metadata from arXiv API (2611.08407);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.08407 Social Humanoid: Socially Responsive Human-Humanoid Interaction'
  url: https://arxiv.org/abs/2611.08407
  date: '2026-11-05'
  accessed_at: '2026-11-09'
- id: src_002
  type: website
  title: Project page
  url: https://von31.github.io/social-humanoid/
  accessed_at: '2026-11-09'
---

## 概述

人形机器人通常被训练为孤立个体，难以与会自然预判并调整自身动作的人类伙伴进行物理协作。Social Humanoid 针对这一问题，构建了一个以人类伙伴动作为条件、在 29-DoF Unitree G1 上生成并执行社会响应性全身运动的分层系统。其高层策略借助共享 token 化表示对人类与人形运动做灵活的序列建模，既能生成反应性人形动作，也能在伙伴被遮挡时预判其运动；低层全身跟踪控制器则负责把生成的动作落实到真实机器人上。为训练该系统，作者设计了两阶段自适应重定向流程，将一个交互伙伴重定向到机器人，同时对另一伙伴做形变以保留接触动力学、可达性与相对身体尺度。该流程应用于五个动作捕捉数据集，产出了 260 小时的人-人形交互 HHI 基准，实验显示系统在仿真与真实世界中均能产生协调且与人类对齐的行为。

## 核心内容

### 问题背景
现有人形机器人多以孤立智能体的方式训练，缺乏与人类伙伴进行物理协调的能力；而人类在交互中会自然预判并调整彼此动作，这一差距限制了人机协作的自然性。

### 方法
- **分层系统架构**：Social Humanoid 在 29-DoF Unitree G1 上运行，条件输入为人类伙伴的运动。
- **高层策略**：通过共享 token 化表示对人类与人形运动进行灵活的序列建模，生成反应性人形动作，并在伙伴被遮挡时对其运动进行预判。
- **低层控制器**：全身跟踪控制器负责在机器人上执行高层生成的动作。
- **两阶段自适应重定向**：训练时将一对交互伙伴中的一个重定向到机器人，另一个做形变处理，以保留接触动力学、可达性与相对身体尺度。

### 实验设置
- 将上述重定向流程应用于五个动作捕捉数据集。
- 构建新的 Human-Humanoid Interaction（HHI）基准，包含 260 小时的人-人形交互数据。
- 在仿真与真实世界中评估系统在多种交互类型下的表现。

### 关键结果
结果表明，Social Humanoid 在多样化的交互类型中均能产生协调、与人类对齐的行为，且在仿真和真实世界环境中均得到验证。

### 结论
通过分层生成与执行结合自适应重定向训练数据构建，Social Humanoid 使人形机器人具备了社会响应性的全身交互能力，并配套发布了 HHI 基准。项目页面：https://von31.github.io/social-humanoid/

## Overview

Humanoid robots are typically trained as solitary agents, leaving them unable to coordinate physically with human partners who naturally anticipate and adjust to one another. To bridge this gap, we present Social Humanoid, a hierarchical system that generates and executes socially responsive whole-body motion on a 29-DoF Unitree G1 conditioned on a human partner's motion. Its high-level policy performs flexible sequence modeling of human and humanoid motion through a shared tokenized representation, generating reactive humanoid motion and anticipating the partner's motion when they are occluded, while a low-level whole-body tracking controller executes the generated motion on the robot. To train the system, we introduce a two-phase adaptive retargeting procedure that retargets one interaction partner to the robot while morphing the other partner to preserve contact dynamics, reachability, and relative body scale. We apply this procedure across five motion-capture datasets to produce a new Human-Humanoid Interaction (HHI) benchmark of 260 hours of human-humanoid interactions. Our results demonstrate that Social Humanoid produces coordinated, human-aligned behavior across diverse interaction types in simulation and the real world. Project page: https://von31.github.io/social-humanoid/

## 参考
- https://arxiv.org/abs/2611.08407
- https://von31.github.io/social-humanoid/
