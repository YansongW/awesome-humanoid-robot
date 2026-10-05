---
$id: ent_paper_shin_hoi_retarget_contact_centric_r_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HOI-Retarget: Contact-Centric Retargeting for Human-Object Interaction'
  zh: 'HOI-Retarget: Contact-Centric Retargeting for Human-Object Interaction'
  ko: 'HOI-Retarget: Contact-Centric Retargeting for Human-Object Interaction'
summary:
  en: Learning from demonstration (LfD) has enabled humanoid robots to acquire diverse whole-body skills, but extending this
    paradigm to human-object interaction (HOI) is limited by the availability of robot-compatible interaction references.
    We present HOI-Retarget, a contact-centric retargeting method that transfers HOI onto a humanoid robot for large-scale
    motion-data generation. Its windowed ...
  zh: HOI-Retarget 是一种以接触为中心的重定向方法，用于将人-物交互（HOI）迁移到人形机器人上，从而支持大规模运动数据生成。该方法由 Jihwan Shin、Adrià López Escoriza、Junzhe He、Matthias
    Heyrman 与 Marco Hutter 提出，其核心是基于窗口的轨迹优化，将每个标注接触作为物体坐标系下的目标，在机器人运动学约束下平衡身体跟踪、足部支撑与平滑性。作者公开了代码与重定向后的运动数据集。
  ko: Learning from demonstration (LfD) has enabled humanoid robots to acquire diverse whole-body skills, but extending this
    paradigm to human-object interaction (HOI) is limited by the availability of robot-compatible interaction references.
    We present HOI-Retarget, a contact-centric retargeting method that transfers HOI onto a humanoid robot for large-scale
    motion-data generation. Its windowed ...
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
- human_object_interaction
- motion_retargeting
- humanoid_robots
- trajectory_optimization
- learning_from_demonstration
- contact_centric
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-05'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-05). Bibliographic metadata from arXiv API (2609.34674);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.34674 HOI-Retarget: Contact-Centric Retargeting for Human-Object Interaction'
  url: https://arxiv.org/abs/2609.34674
  date: '2026-09-28'
  accessed_at: '2026-10-05'
- id: src_002
  type: website
  title: Project page
  url: http://shinben0327.github.io/hoi-retarget
  accessed_at: '2026-10-05'
---

## 概述

人形机器人通过示教学习（LfD）已能掌握多种全身技能，但该范式向人-物交互（HOI）扩展时受限于缺乏与机器人兼容的交互参考数据。为此，作者提出 HOI-Retarget，一种以接触为中心的重定向方法，可将 HOI 迁移到人形机器人上，用于大规模运动数据生成。该方法采用基于窗口的轨迹优化，把每一个标注接触都当作物体坐标系下的目标，并在机器人运动学限制下权衡身体跟踪、足部支撑与运动平滑性。它还能在保持单次示教的前提下跨物体尺寸进行增广，吸收从单目视频重建出的接触信息，并可扩展到多台机器人共同操作同一物体的场景。作者公开了代码以及重定向后的运动数据集。

## 核心内容

### 问题背景
示教学习（LfD）使人形机器人获得了多样化的全身技能，但要把这一范式推广到人-物交互（HOI），瓶颈在于缺少与机器人兼容的交互参考数据。现有的人类 HOI 数据难以直接用于人形机器人，因此需要一种能够把人类交互动作迁移到机器人上的重定向手段，以支撑大规模运动数据的生成。

### 方法
作者提出 HOI-Retarget，一种以接触为中心的重定向方法，将 HOI 迁移到人形机器人上。其核心是基于窗口的轨迹优化：把每一个被标注的接触都作为物体坐标系下的目标，并在机器人运动学限制的约束下，平衡身体跟踪、足部支撑与平滑性这三方面因素。

### 能力与扩展
- 可对单次示教进行增广，覆盖不同的物体尺寸。
- 可吸收从单目视频中重建出的接触信息。
- 可扩展到多台机器人共同操作同一个物体的情形。

### 结论与开源
作者公开了代码以及重定向后的运动数据集，以支持后续研究与大规模运动数据生成。

## Overview

Learning from demonstration (LfD) has enabled humanoid robots to acquire diverse whole-body skills, but extending this paradigm to human-object interaction (HOI) is limited by the availability of robot-compatible interaction references. We present HOI-Retarget, a contact-centric retargeting method that transfers HOI onto a humanoid robot for large-scale motion-data generation. Its windowed trajectory optimization uses every labeled contact as a target in the object frame, balancing body tracking, foot support and smoothness under the robot's kinematic limits. The method can augment a single demonstration across object sizes, absorb contacts reconstructed from monocular video, and extend to several robots manipulating one object. We publicly release the code and the retargeted motion dataset.

## 参考
- https://arxiv.org/abs/2609.34674
- http://shinben0327.github.io/hoi-retarget
