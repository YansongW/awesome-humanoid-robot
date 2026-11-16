---
$id: ent_paper_ding_from_a_single_rgb_image_to_rob_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'From a Single RGB Image to Robot Execution: Metric Scene Alignment and Contact-Guided Retargeting'
  zh: 'From a Single RGB Image to Robot Execution: Metric Scene Alignment and Contact-Guided Retargeting'
  ko: 'From a Single RGB Image to Robot Execution: Metric Scene Alignment and Contact-Guided Retargeting'
summary:
  en: Extending humanoid interaction generation to new environments remains limited by the need for prebuilt 3D scene assets.
    Reconstructing scenes directly from single RGB images offers a way to overcome this limitation, but introduces a key challenge
    in maintaining geometric consistency throughout motion generation and transfer. Visually plausible human motions may be
    misaligned with the ...
  zh: 该工作提出一条统一流水线，将单张 RGB 图像转换为可供人形机器人执行的运动参考：先从图像重建场景几何，再在重建场景条件下生成人体交互动作，最后重定向到人形机器人。为保持全过程的几何一致性，作者在重定向前后分别引入 Joint Metric
    Interaction Refinement (JMIR) 与 Contact Guided Residual Retargeting (CGRR) 两个互补的细化阶段。相比 GRAIL，细化时间从 480 s 降至 87 s（5.5
    倍加速），在仿真中成功率达 89%，并在 Unitree G1 上完成 50 次实物试验、成功率 70%。
  ko: Extending humanoid interaction generation to new environments remains limited by the need for prebuilt 3D scene assets.
    Reconstructing scenes directly from single RGB images offers a way to overcome this limitation, but introduces a key challenge
    in maintaining geometric consistency throughout motion generation and transfer. Visually plausible human motions may be
    misaligned with the ...
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
- humanoid_motion_retargeting
- single_rgb_scene_reconstruction
- metric_scene_alignment
- contact_guided_retargeting
- humanoid_interaction_generation
- sim_to_real
- end
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-16'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-16). Bibliographic metadata from arXiv API (2611.14981);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.14981 From a Single RGB Image to Robot Execution: Metric Scene Alignment and Contact-Guided Retargeting'
  url: https://arxiv.org/abs/2611.14981
  date: '2026-11-11'
  accessed_at: '2026-11-16'
---

## 概述

将人形机器人交互动作生成扩展到新环境，通常受限于需要预先构建三维场景资产；从单张 RGB 图像直接重建场景可以绕开这一限制，但随之带来运动生成与迁移过程中的几何一致性难题——视觉上合理的人体动作可能与重建场景错位，而人机形态差异又会在重定向时引入额外的支撑误差。为此，作者构建了一条统一流水线，依次完成场景几何重建、以重建场景为条件的人体交互动作生成以及向人形机器人的运动重定向。为维持几何一致性，流水线在形态迁移前后各设置一个细化阶段：重定向前由 Joint Metric Interaction Refinement (JMIR) 在保留生成交互结构的前提下改善人体动作与已配准度量场景的对齐，重定向后由 Contact Guided Residual Retargeting (CGRR) 修正机器人特有的支撑误差、恢复预期支撑关系。经这两个阶段处理得到的运动参考与重建场景一致，可被多个预训练人形跟踪器直接跟随，无需针对具体场景微调策略。实验显示该方法将细化时间从 GRAIL 的 480 s 缩短至 87 s，仿真成功率 89%，并在 Unitree G1 的 50 次实物试验中取得 70% 的成功率。

## 核心内容

### 问题背景

将人形机器人的交互动作生成推广到新环境，主要障碍在于依赖预先构建的三维场景资产。利用单张 RGB 图像直接重建场景是规避该依赖的可行途径，但由此产生一个核心挑战：在动作生成与迁移的整个流程中保持几何一致性。具体而言，视觉上看似合理的人体动作可能与重建场景在度量尺度上并不对齐；而由于人体与机器人形态存在差异，重定向过程还会引入额外的支撑误差。

### 方法

作者提出一条统一流水线，把单张 RGB 图像转换为人体运动参考，包含三个环节：

- 从输入图像重建场景几何；
- 以重建场景为条件生成人体交互动作；
- 将动作重定向到人形机器人。

为在流程中维持几何一致性，流水线在形态迁移前后各加入一个互补的细化阶段：

- **Joint Metric Interaction Refinement (JMIR)**：位于重定向之前，用于改善人体动作与已配准度量场景之间的对齐，同时保留已生成的交互结构。
- **Contact Guided Residual Retargeting (CGRR)**：位于重定向之后，针对机器人形态修正其特有的支撑误差，恢复原本意图中的支撑关系。

经过这两个阶段，输出的运动参考与重建场景保持一致，并可被多个预训练人形跟踪器跟随，无需针对具体场景进行策略微调。

### 实验设置与关键结果

- 与 GRAIL 相比，本方法将细化时间从 480 s 缩短至 87 s，实现 5.5 倍加速。
- 完整流水线在仿真中达到 89% 的成功率。
- 在 Unitree G1 上开展 50 次实物试验，成功率为 70%。

### 结论

实验结果表明，该流水线能够从单张 RGB 图像生成可执行的人形运动参考，验证了其在真实机器人上从图像输入到动作执行的有效性。

## Overview

Extending humanoid interaction generation to new environments remains limited by the need for prebuilt 3D scene assets. Reconstructing scenes directly from single RGB images offers a way to overcome this limitation, but introduces a key challenge in maintaining geometric consistency throughout motion generation and transfer. Visually plausible human motions may be misaligned with the reconstructed scene, while retargeting can introduce additional support errors due to differences between human and robot embodiments. We present a unified pipeline that transforms a single RGB image into a humanoid motion reference. It reconstructs scene geometry from the input image, generates a human interaction conditioned on the reconstructed scene, and retargets the motion to a humanoid robot. To maintain geometric consistency throughout this process, we incorporate two complementary refinement stages before and after embodiment transfer. Before retargeting, Joint Metric Interaction Refinement (JMIR) refines human motion alignment with the registered metric scene while preserving the generated interaction structure. Following retargeting, Contact Guided Residual Retargeting (CGRR) corrects robot specific support errors to restore the intended support relationships. Together, these stages produce motion references that are consistent with the reconstructed scene and can be followed by multiple pretrained humanoid trackers without scene specific policy fine tuning. Compared with GRAIL, our method reduces refinement time from 480 s to 87 s, yielding a speedup of 5.5 times. The complete pipeline achieves a success rate of 89% in simulation and 70% across 50 physical trials on the Unitree G1, demonstrating its effectiveness in generating executable humanoid motion references from single RGB images.

## 参考
- https://arxiv.org/abs/2611.14981
