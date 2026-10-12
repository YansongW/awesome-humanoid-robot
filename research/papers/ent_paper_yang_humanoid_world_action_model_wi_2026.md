---
$id: ent_paper_yang_humanoid_world_action_model_wi_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Humanoid World Action Model With Joint State--Action Generation
  zh: Humanoid World Action Model With Joint State--Action Generation
  ko: Humanoid World Action Model With Joint State--Action Generation
summary:
  en: Humanoid robots are a promising platform for general-purpose manipulation. Recent Vision-Language-Action (VLA) policies
    learn actions directly from multimodal observations, while World Action Models (WAMs) further incorporate future visual
    prediction to improve action generation. However, in hierarchical humanoid systems, VLA and WAM policies output reference
    actions that are subsequently ...
  zh: HWAM 是一种面向人形机器人的世界动作模型，由 Yan Yang、Jikun Rong、Minzhao Zhu 等人提出，核心思路是将机器人执行后的本体感知状态作为显式预测目标，与参考动作联合生成。该方法通过 Policy、Forward
    Dynamics Modeling（FDM）与 Inverse Dynamics Modeling（IDM）三条条件路径训练，在 LimX OLI 人形机器人的三项真实任务上取得最高成功率，其中 Candy Picking 任务成功率达
    70.6%，高于 Fast-WAM 的 43.3%。
  ko: Humanoid robots are a promising platform for general-purpose manipulation. Recent Vision-Language-Action (VLA) policies
    learn actions directly from multimodal observations, while World Action Models (WAMs) further incorporate future visual
    prediction to improve action generation. However, in hierarchical humanoid systems, VLA and WAM policies output reference
    actions that are subsequently ...
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
- humanoid_robots
- world_action_model
- vision_language_action
- whole_body_control
- state_action_generation
- forward_inverse_dynamics
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-12'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-12). Bibliographic metadata from arXiv API (2610.12026);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2610.12026 Humanoid World Action Model With Joint State--Action Generation
  url: https://arxiv.org/abs/2610.12026
  date: '2026-10-08'
  accessed_at: '2026-10-12'
---

## 概述

人形机器人是通用操作的重要平台，但分层系统中策略输出的参考动作需经全身控制、动力学、平衡与接触才能实现，由此产生动作—执行鸿沟。现有 Vision-Language-Action（VLA）策略直接从多模态观测学习动作，World Action Models（WAMs）进一步引入未来视觉预测，但若不明建模实际执行的身体状态，未来视觉预测就需同时解释场景演化与参考动作和执行动作之间的偏差。为此作者提出 HWAM，将执行后的本体感知状态作为显式预测目标，与参考动作联合生成，从而把执行动作的监督直接纳入动作学习。HWAM 通过 Policy、FDM、IDM 三条互补条件路径训练，将策略参考、实际身体运动与视觉结果联系起来。在 LimX OLI 人形机器人的三项真实任务上，HWAM 在评估基线中取得最高成功率。

## 核心内容

### 问题背景
人形机器人被视为通用操作的有前景平台。近期 Vision-Language-Action（VLA）策略直接从多模态观测中学习动作，而 World Action Models（WAMs）进一步引入未来视觉预测以改进动作生成。然而在分层人形系统中，VLA 与 WAM 策略输出的是参考动作，这些参考动作随后需经由全身控制、机器人动力学、平衡与接触才能实现。这种分层结构带来了动作—执行鸿沟：策略产生的参考动作可能与机器人实际实现的运动不一致。若不明建模实际实现的身体状态，未来视觉预测就必须同时解释场景演化以及参考动作与执行动作之间的差异，导致难以将某个动作与其物理结果关联起来。

### 方法
作者提出 HWAM（Humanoid World Action Model），一种带联合状态—动作生成的人形世界动作模型，将机器人执行后的本体感知状态设为显式预测目标。通过联合生成参考动作及其实际实现的身体状态，HWAM 将执行运动的监督直接纳入动作学习。

HWAM 通过三条互补的条件路径进行训练：
- **Policy 路径**：仅以当前观测为条件，对状态—动作轨迹进行联合去噪，与部署条件相匹配。
- **Forward Dynamics Modeling（FDM）**：以动作与执行后状态为条件，预测未来视觉观测。
- **Inverse Dynamics Modeling（IDM）**：从视觉转换中重建关节轨迹。

这三条路径共同将策略参考、实际身体运动与视觉结果连接起来。

### 实验设置与关键结果
评估在 LimX OLI 人形机器人的三项真实机器人任务上进行。HWAM 在评估基线中取得最高成功率。在 Candy Picking 任务上，HWAM 成功率为 70.6%，而 Fast-WAM 为 43.3%。

### 结论
通过将执行后的本体感知状态作为显式预测目标并与参考动作联合生成，HWAM 缓解了分层人形系统中的动作—执行鸿沟，在真实机器人任务上优于所评估的基线方法。

## Overview

Humanoid robots are a promising platform for general-purpose manipulation. Recent Vision-Language-Action (VLA) policies learn actions directly from multimodal observations, while World Action Models (WAMs) further incorporate future visual prediction to improve action generation. However, in hierarchical humanoid systems, VLA and WAM policies output reference actions that are subsequently realized through whole-body control, robot dynamics, balance, and contact. This hierarchy creates an action--execution gap: the reference produced by the policy can differ from the motion realized by the robot. Without explicitly modeling the realized body state, future visual prediction must jointly explain scene evolution and discrepancies between reference actions and executed motion, making it difficult to associate an action with its physical outcome. We propose HWAM, a Humanoid World Action Model with joint state--action generation, which makes the robot's post-execution proprioceptive state an explicit prediction target. By jointly generating reference actions and their realized body states, HWAM directly incorporates supervision of executed motion into action learning. HWAM is trained through three complementary conditional paths. The Policy path jointly denoises state--action trajectories conditioned only on current observations, matching deployment conditions. Forward Dynamics Modeling (FDM) predicts future visual observations conditioned on actions and post-execution states, while Inverse Dynamics Modeling (IDM) reconstructs the joint trajectory from visual transitions. Together, these paths connect policy references, realized body motion, and visual outcomes. HWAM achieves the highest success rate among evaluated baselines on three real-robot tasks on the LimX OLI humanoid. On Candy Picking, HWAM achieves a 70.6% success rate, compared with 43.3% for Fast-WAM.

## 参考
- https://arxiv.org/abs/2610.12026
