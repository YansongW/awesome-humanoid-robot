---
$id: ent_paper_adwani_phd_hand_a_printable_humanoid_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PHD-Hand: A Printable Humanoid Dexterous Hand with Linkage-Driven 3-DOA Digits'
  zh: 'PHD-Hand: A Printable Humanoid Dexterous Hand with Linkage-Driven 3-DOA Digits'
  ko: 'PHD-Hand: A Printable Humanoid Dexterous Hand with Linkage-Driven 3-DOA Digits'
summary:
  en: Currently, dexterous humanoid robot hands are widely considered the final hardware bottleneck that hampers generalist
    robots from physically assisting people at home and work. As conventional tendon-driven designs suffer from high cost,
    demanding maintenance, poor reliability, and short durability, alternative linkage-driven designs have increasingly gained
    attention. Despite their potential to ...
  zh: PHD-Hand 是一种可打印的人形灵巧手，由 Neel Adwani、Muhaiminul Islam Akash、Saffia Ouali、Ethan Liu、Cong Wang 提出，采用连杆驱动方案，每根手指具备 3 个驱动自由度（DOA）。其核心创新在于引入独特的柔性铰链（flexure
    hinge）与弹簧钢制成的弹性驱动杆，大幅简化了连杆传动链，使其无需大量微型运动部件即可用低成本 3D 打印机加工，并可将尺寸做得更接近真人手部。
  ko: Currently, dexterous humanoid robot hands are widely considered the final hardware bottleneck that hampers generalist
    robots from physically assisting people at home and work. As conventional tendon-driven designs suffer from high cost,
    demanding maintenance, poor reliability, and short durability, alternative linkage-driven designs have increasingly gained
    attention. Despite their potential to ...
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
- dexterous_hand
- linkage_driven
- flexure_hinge
- 3d_printing
- humanoid_robot
- grasp_manipulation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-26'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-26). Bibliographic metadata from arXiv API (2610.29030);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.29030 PHD-Hand: A Printable Humanoid Dexterous Hand with Linkage-Driven 3-DOA Digits'
  url: https://arxiv.org/abs/2610.29030
  date: '2026-10-21'
  accessed_at: '2026-10-26'
- id: src_002
  type: website
  title: Project page
  url: https://lnkd.in/p/er-NRfMn
  accessed_at: '2026-10-26'
---

## 概述

当前灵巧人形手被视为通用机器人进入家庭与工作场景的最后硬件瓶颈，传统腱驱动方案存在成本高、维护难、可靠性差和寿命短等问题，连杆驱动因此受到关注，但在单指内集成多个驱动自由度（DOA）在设计与制造上颇具挑战，能实现全连杆驱动且每指至少 3 个 DOA 的功能性人形手研究仍很少。PHD-Hand 通过独特的柔性铰链配合弹簧钢弹性驱动杆，显著简化了连杆传动结构，避免了同类灵巧度设计中对大量微型运动部件的依赖。这一简化使该手可用预算级 3D 打印机轻松制造，降低了使用与开发灵巧人形手功能的门槛，也让手部尺寸能更接近普通人类手。设计还具备有利的运动学优势，作者通过原型开展了抓取与物体操作评估，并报告了在手部运动学与控制方面的最新发现。

## 核心内容

### 问题背景
- 灵巧人形机器人手被广泛认为是阻碍通用机器人真正在家庭与工作环境中为人类提供物理协助的最终硬件瓶颈。
- 传统腱驱动设计存在成本高、维护要求高、可靠性差、耐久性短等弱点，连杆驱动设计因此日益受到关注。
- 但用连杆传动在单根手指中集成多个驱动自由度（DOA）在设计与制造上都是难题；仅有少数研究实现了完全连杆驱动、且每指至少 3 个 DOA 的功能性人形手，同时不牺牲执行器布置与其他设计偏好。

### 方法
- 提出一种新的连杆驱动手，采用独特的柔性铰链（flexure hinge）。
- 配合由弹簧钢制成的弹性驱动杆，使连杆传动链显著简化。
- 与灵巧度相近的其他连杆驱动设计不同，该方案不需要大量微型运动部件。
- 因此该手可用预算级 3D 打印机轻松制造，并可使尺寸更接近普通人类手部。
- 设计同时具备有利的运动学优势。

### 实验设置与结果
- 对原型进行了抓取与物体操作方面的评估。
- 论文还给出了关于该手运动学与控制的最新研究结果。
- 摘要未提供具体量化指标、对比基线或数值结果。

### 结论
- 该设计降低了使用与开发灵巧人形机器人手功能的门槛。
- 通过柔性铰链与弹性驱动杆的组合，在保持每指 3 个 DOA 的同时实现了易制造、低成本与接近人手的尺寸。

## Overview

Currently, dexterous humanoid robot hands are widely considered the final hardware bottleneck that hampers generalist robots from physically assisting people at home and work. As conventional tendon-driven designs suffer from high cost, demanding maintenance, poor reliability, and short durability, alternative linkage-driven designs have increasingly gained attention. Despite their potential to avoid the weaknesses of tendon-driven hands, integrating multiple degrees of actuation (DOA) in a single digit with linkage drivetrains is a challenge for design and fabrication. Only a few studies have managed to present functional humanoid hands that are completely linkage-driven and have at least three DOAs per digit without compromising actuator placement and other design preferences. Our work introduces a new linkage-driven hand featuring a unique flexure hinge. Together with elastic drive rods made of spring steel, the linkage drivetrains are significantly simplified. Unlike other linkage-driven designs of similar dexterity, our design does not require many miniature moving parts. As a result, the hand can be fabricated easily with a budget 3D printer. This not only significantly lowers the barrier to entry for using and developing dexterous humanoid robot hand functions, but also allows the hands to be sized much closer to regular human hands. The design offers desirable kinematic advantages as well. A prototype is evaluated for grasping and object manipulation. In addition, this paper presents our latest findings on kinematics and control of the hand.

## 参考
- https://arxiv.org/abs/2610.29030
- https://lnkd.in/p/er-NRfMn
