---
$id: ent_paper_kalaria_vicar_video_imitation_with_con_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VICAR: Video Imitation with Contact-Aware Retargeting for Humanoid Interactive Skills'
  zh: 'VICAR: Video Imitation with Contact-Aware Retargeting for Humanoid Interactive Skills'
  ko: 'VICAR: Video Imitation with Contact-Aware Retargeting for Humanoid Interactive Skills'
summary:
  en: Third-person human videos offer a scalable alternative to task-specific reward engineering, teleoperation, and manually
    scripted demonstrations for humanoid loco-manipulation. Recent video-to-humanoid systems have shown that noisy human motion,
    object trajectories, and contacts can be extracted from unstructured videos and refined into deployable skills. However,
    a key gap remains for ...
  zh: VICAR（Video Imitation with Contact-Aware Retargeting）是一个从第三人称人类视频中学习人形机器人交互技能的流程，由 Dvij Kalaria、Bike Zhang 与 S. Shankar
    Sastry 提出。该方法从单目视频中恢复人体运动并重建任务相关障碍物，在重定向到人形机器人时以高优先级拉格朗日惩罚项保留全局接触位姿、运动速度与碰撞间隙。作者在十项第三人称视频技能上验证了框架，并将学到的技能部署到硬件上。
  ko: Third-person human videos offer a scalable alternative to task-specific reward engineering, teleoperation, and manually
    scripted demonstrations for humanoid loco-manipulation. Recent video-to-humanoid systems have shown that noisy human motion,
    object trajectories, and contacts can be extracted from unstructured videos and refined into deployable skills. However,
    a key gap remains for ...
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
- humanoid_loco_manipulation
- video_imitation
- contact_aware_retargeting
- motion_retargeting
- contact_conditioned_generation
- sim_to_real
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-12'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-12). Bibliographic metadata from arXiv API (2610.13079);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.13079 VICAR: Video Imitation with Contact-Aware Retargeting for Humanoid Interactive Skills'
  url: https://arxiv.org/abs/2610.13079
  date: '2026-10-09'
  accessed_at: '2026-10-12'
---

## 概述

VICAR 面向接触丰富的人形机器人模仿任务，试图解决世界坐标系下接触的位姿、时序与速度在跨本体迁移和运行时场景变化中难以保持的问题。系统先从第三人称单目视频中恢复人体运动并重建任务相关障碍物，再将运动重定向到人形机器人，同时保留全局接触位姿、运动速度与碰撞间隙。与仅消除穿透或仅保留局部交互几何的重定向方法不同，VICAR 将用户指定的接触位姿与碰撞间隙表示为高优先级的拉格朗日惩罚项，并对整段运动进行优化，使其在接触丰富的过渡过程中保持平滑。由此得到的运动被用于训练一个接触条件化的运动生成器，其输入包含可移动接触点，从而支持在运行时适应新的接触位置。作者在十项多样化的第三人称视频技能上展示了该框架，并将学到的技能部署到硬件上。

## 核心内容

### 问题背景
第三人称人类视频为 humanoid loco-manipulation 提供了一种可扩展的替代方案，可避免针对具体任务的奖励工程、遥操作与人工脚本演示。已有的 video-to-humanoid 系统能够从非结构化视频中提取带噪声的人体运动、物体轨迹与接触，并精炼为可部署技能。但在接触丰富的模仿场景中仍存在关键缺口：任务往往由世界坐标系下的接触定义，其位姿、时序与速度必须在跨本体不匹配以及运行时场景变化下依然保持。

### 方法
VICAR（Video Imitation with Contact-Aware Retargeting）是一个从第三人称人类视频中学习人形机器人交互技能的流程，包含以下环节：
- 从视频中恢复人体运动；
- 从单目视频中重建任务相关障碍物；
- 将运动重定向到 humanoid，同时保留全局接触位姿、运动速度与碰撞间隙。

与仅消除穿透或仅保留局部交互几何的重定向方法不同，VICAR 将用户指定的接触位姿与碰撞间隙表示为高优先级的 Lagrangian penalty terms，并对完整运动进行优化，使其在接触丰富的过渡过程中保持平滑。

重定向得到的运动被用于训练一个 contact-conditioned motion generator，其输入包含 movable contact points，从而支持在运行时适应新的接触位置。

### 实验设置
作者在十项多样化的第三人称视频技能上演示了该框架，包括：
- 六项 table-tennis serves；
- 三项 object-pickup 任务；
- ladder climbing。

随后将学到的技能部署到硬件上。

### 结论
结果表明，保留接触的重定向是迈向"通过观察人类来学习有用交互行为的人形机器人"的一个实用步骤。

## Overview

Third-person human videos offer a scalable alternative to task-specific reward engineering, teleoperation, and manually scripted demonstrations for humanoid loco-manipulation. Recent video-to-humanoid systems have shown that noisy human motion, object trajectories, and contacts can be extracted from unstructured videos and refined into deployable skills. However, a key gap remains for contact-rich imitation: the task is often defined by world-frame contacts whose poses, timing, and speed must survive embodiment mismatch and runtime scene changes. Towards this, we present VICAR (Video Imitation with Contact-Aware Retargeting), a pipeline for learning humanoid interactive skills from third-person human videos. The system first recovers human motion, reconstructs task-relevant obstacles from monocular video, and then retargets the motion to a humanoid while preserving global contact poses, motion speed, and collision clearance. Unlike retargeting methods that only remove penetration or preserve local interaction geometry, our formulation represents user-specified contact poses and collision clearance as high-priority Lagrangian penalty terms and optimizes the full motion to remain smooth through contact-rich transitions. The resulting motions are used to train a contact-conditioned motion generator whose inputs include movable contact points enabling runtime adaptation to new contact positions. We demonstrate the framework on ten diverse third-person video skills, including six table-tennis serves, three object-pickup tasks, and ladder climbing, and deploy the learned skills on hardware. These results suggest that contact-preserving retargeting is a practical step toward humanoids that learn useful interactive behavior by watching humans.

## 参考
- https://arxiv.org/abs/2610.13079
