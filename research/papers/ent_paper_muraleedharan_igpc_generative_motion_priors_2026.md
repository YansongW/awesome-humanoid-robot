---
$id: ent_paper_muraleedharan_igpc_generative_motion_priors_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'iGPC: Generative Motion Priors for Object-Aware Humanoid Interaction'
  zh: 'iGPC: Generative Motion Priors for Object-Aware Humanoid Interaction'
  ko: 'iGPC: Generative Motion Priors for Object-Aware Humanoid Interaction'
summary:
  en: Humanoid robots operating in unstructured environments must combine robust whole-body control with the ability to perceive
    and physically interact with surrounding objects. While large-scale human motion data provides powerful priors for natural
    and versatile humanoid control, effectively transferring such priors to perception-driven object interaction remains challenging.
    To address this ...
  zh: 本文提出 iGPC 框架，将近期提出的 Generative Pretrained Controller (GPC) 从通用人体运动扩展到全身人形机器人与环境的交互。作者先以场景可供性线索与特权状态信息为条件，把 GPC 改造为交互专家，再通过感知驱动的学生策略在机载传感器观测下蒸馏专家技能。实验表明，大规模生成式人体运动先验可为接触丰富的真实环境中的人形交互策略学习提供有效基础。
  ko: Humanoid robots operating in unstructured environments must combine robust whole-body control with the ability to perceive
    and physically interact with surrounding objects. While large-scale human motion data provides powerful priors for natural
    and versatile humanoid control, effectively transferring such priors to perception-driven object interaction remains challenging.
    To address this ...
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
- humanoid_interaction
- motion_prior
- whole_body_control
- policy_distillation
- generative_controller
- object_interaction
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-12'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-12). Bibliographic metadata from arXiv API (2610.08120);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.08120 iGPC: Generative Motion Priors for Object-Aware Humanoid Interaction'
  url: https://arxiv.org/abs/2610.08120
  date: '2026-10-06'
  accessed_at: '2026-10-12'
---

## 概述

人形机器人在非结构化环境中工作，既需要稳健的全身控制，也需要感知并与周围物体发生物理交互的能力。大规模人体运动数据虽能为自然多样的人形控制提供强先验，但把这类先验有效迁移到感知驱动的物体交互上仍很困难。为此，作者提出 iGPC 框架，把 Generative Pretrained Controller (GPC) 从通用人体运动拓展到全身人形—环境交互。方法上先将 GPC 适配为以场景可供性线索和特权状态信息为条件的交互专家，使其在学习任务特定接触行为的同时利用预训练运动先验；随后引入保留预训练 GPC 策略的感知驱动学生模型，借助机载感官观测蒸馏专家技能，并用两个互补训练目标弥合特权观测与感官输入之间的差距。多项全身交互任务的实验显示，大规模生成式人体运动先验是学习可部署人形交互策略的有效基础。

## 核心内容

### 问题背景
在非结构化环境中运行的人形机器人，需要同时具备稳健的全身控制能力，以及感知并物理交互周围物体的能力。大规模人体运动数据为自然、多样的人形控制提供了强先验，但如何把这类先验有效迁移到由感知驱动的物体交互任务上，仍是一个瓶颈。

### 方法
作者提出的框架把近期提出的 Generative Pretrained Controller (GPC) 从通用人体运动扩展到全身人形—环境交互，主要包含两个阶段：

- **交互专家**：将 GPC 适配为以场景可供性线索（scene affordance cues）和特权状态信息（privileged state information）为条件的交互专家。这些专家在利用预训练人体运动先验的同时，学习任务特定的接触行为，包括伸向物体、抓握环境支撑以保持稳定，以及推动可移动物体。
- **感知驱动学生**：引入一个感知驱动的学生策略，它保留预训练的 GPC 策略，并利用机载感官观测（onboard sensory observations）从专家处蒸馏交互技能。为弥合特权专家观测与感官输入之间的差距，作者提出两个互补的训练目标，使预训练运动先验在蒸馏过程中得到有效适配。

### 实验与结果
实验覆盖多个全身交互任务。结果表明，大规模生成式人体运动先验为学习可部署的人形交互策略提供了有效基础，适用于接触丰富的真实世界环境。

### 结论
将大规模生成式人体运动先验与交互专家、感知驱动蒸馏相结合，是把人体运动先验迁移到感知驱动的人形物体交互上的一条可行路径。

## Overview

Humanoid robots operating in unstructured environments must combine robust whole-body control with the ability to perceive and physically interact with surrounding objects. While large-scale human motion data provides powerful priors for natural and versatile humanoid control, effectively transferring such priors to perception-driven object interaction remains challenging. To address this bottleneck, we propose a framework that extends the recently proposed Generative Pretrained Controller (GPC) from general human motion to full-body humanoid-environment interaction. First, we adapt GPC into interaction experts conditioned on scene affordance cues and privileged state information. These experts leverage the pretrained human motion prior while learning task-specific contact behaviors, including reaching toward objects, grasping environmental supports for stabilization, and pushing movable objects. Second, we introduce a perception-driven student that retains the pretrained GPC policy and distills interaction skills from the experts using onboard sensory observations. To bridge the gap between privileged expert observations and sensory inputs, we propose two complementary training objectives that enable effective adaptation of the pretrained motion prior during distillation. Notably, our experiments across multiple whole-body interaction tasks demonstrate that large-scale generative human motion priors provide an effective foundation for learning deployable policies for humanoid interactions in contact-rich real-world environments.

## 参考
- https://arxiv.org/abs/2610.08120
