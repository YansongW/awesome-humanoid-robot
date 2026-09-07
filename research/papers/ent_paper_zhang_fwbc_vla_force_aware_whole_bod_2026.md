---
$id: ent_paper_zhang_fwbc_vla_force_aware_whole_bod_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FWBC-VLA: Force-Aware Whole-Body Compensation for Contact-Rich Loco-Manipulation'
  zh: 'FWBC-VLA: Force-Aware Whole-Body Compensation for Contact-Rich Loco-Manipulation'
  ko: 'FWBC-VLA: Force-Aware Whole-Body Compensation for Contact-Rich Loco-Manipulation'
summary:
  en: Contact-rich loco-manipulation requires a bridge between semantic action generation and physical interaction control.
    Existing Vision-language-action (VLA) models generate task-level actions from visual and linguistic observations, but
    cannot interpret the physical interactions induced by those actions. While the whole-body control (WBC) policy can stabilize
    the robot, it cannot distinguish ...
  zh: FWBC-VLA 是一个面向轮腿机器人的力感知框架，旨在弥合任务级视觉-语言-动作（VLA）生成与底层全身控制（WBC）之间的鸿沟。该框架由张宇天等人提出，引入了无传感器的残差力矩估计器 HSR-Force，将接触状态编码为令牌注入
    VLA 动作专家，并联合本体感受与雅可比力估计生成补偿动作。在包含超过 5,000 条轨迹的 WL&Arm 数据集上微调预训练 VLA 骨干，并在黑板擦拭和带闭门器的开门等真实世界接触丰富任务中验证了有效性。
  ko: Contact-rich loco-manipulation requires a bridge between semantic action generation and physical interaction control.
    Existing Vision-language-action (VLA) models generate task-level actions from visual and linguistic observations, but
    cannot interpret the physical interactions induced by those actions. While the whole-body control (WBC) policy can stabilize
    the robot, it cannot distinguish ...
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
- force_aware_control
- vision_language_action
- whole_body_control
- loco_manipulation
- wheeled_legged_robot
- contact_estimation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-07'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-07). Bibliographic metadata from arXiv API (2609.03889);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.03889 FWBC-VLA: Force-Aware Whole-Body Compensation for Contact-Rich Loco-Manipulation'
  url: https://arxiv.org/abs/2609.03889
  date: '2026-09-03'
  accessed_at: '2026-09-07'
---

## 概述

FWBC-VLA 解决了接触丰富的移动操作中语义动作生成与物理交互控制脱节的问题。现有 VLA 模型无法解读动作引发的物理交互，而 WBC 策略难以区分任务相关接触力与外部扰动。该框架通过 HSR-Force 无传感器估计器推断接触强度及其时间变化，并将这些估计编码为令牌注入 VLA 动作解码过程，使策略能感知接触起始、持续加载与释放。同时，机器人本体感受状态、雅可比导出的机体坐标系力估计与接触状态被联合馈入补偿生成器，产生修正动作，与操作中心动作结合后交由 WBC 策略执行。真实世界实验表明，该方法在黑板擦拭和带闭门器的开门任务中表现有效。

## 核心内容

### 问题背景
接触丰富的移动操作（如擦拭、开门）要求系统同时具备高层语义理解与底层物理交互控制能力。然而，现有 VLA 模型仅从视觉和语言观测生成任务级动作，无法解释这些动作引发的物理交互；WBC 策略虽能稳定机器人，却无法区分任务相关接触力与外部扰动引起的力。力/力矩传感器虽能直接测量物理交互，但加装成本高且集成难度大，尤其对未预设计传感器集成的平台。

### 方法
FWBC-VLA 提出三层桥接架构：
- **HSR-Force 估计器**：一种无传感器的残差力矩估计方法，用于推断接触强度及其时间变化，无需额外硬件。
- **接触感知动作解码**：将接触估计编码为令牌，注入 VLA 动作专家，使策略在动作解码时感知接触起始、持续加载与释放三个阶段。
- **补偿生成器**：联合处理机器人本体感受状态、雅可比导出的机体坐标系力估计以及估计的接触状态，生成修正动作。

### 实验设置
- **数据集**：WL&Arm 数据集包含超过 5,000 条轨迹，用于微调预训练 VLA 骨干的全部参数。
- **任务**：真实世界实验包括黑板擦拭和带闭门器的开门，两者均为接触丰富的移动操作场景。

### 关键结果
- 黑板擦拭任务中，FWBC-VLA 能有效维持接触并完成擦拭动作。
- 带闭门器的开门任务中，框架能应对闭门器产生的持续阻力，实现稳定开门。
- 实验验证了无传感器接触估计与补偿机制在真实物理交互中的有效性。

### 结论
FWBC-VLA 通过力感知桥接 VLA 与 WBC，使轮腿机器人能在接触丰富任务中同时保持语义正确性与物理稳定性，且无需额外力传感器硬件，为低成本、高鲁棒性的移动操作提供了可行方案。

## Overview

Contact-rich loco-manipulation requires a bridge between semantic action generation and physical interaction control. Existing Vision-language-action (VLA) models generate task-level actions from visual and linguistic observations, but cannot interpret the physical interactions induced by those actions. While the whole-body control (WBC) policy can stabilize the robot, it cannot distinguish task-relevant interaction forces from forces induced by external disturbances during manipulation. Although force/torque sensors provide direct measurements of physical interactions, retrofitting them entails additional hardware costs and substantial integration effort, particularly for platforms not designed with sensor integration in mind. To address this problem, we propose FWBC-VLA, a force-aware framework that bridges task-level VLA action generation and low-level whole-body compensation control for wheeled-legged robots. First, we introduce HSR-Force, a sensorless residual-torque estimator for inferring contact strength and its temporal variation. These contact estimates are then encoded as tokens and injected into the VLA action expert during action decoding, enabling the policy to perceive contact onset, sustained loading, and release. For loco-manipulation tasks, all parameters of the pretrained VLA backbone are fine-tuned on our WL\&Arm Dataset, which comprises more than 5,000 episodes. Moreover, the robot's proprioceptive state, the Jacobian-derived body-frame force estimate, and the estimated contact state are jointly fed into a compensation generator to produce corrective actions. The manipulation-centric actions are subsequently combined with the corrective actions and passed to the WBC policy for execution. Real-world experiments on whiteboard wiping and door opening with a door closer demonstrate the effectiveness of our FWBC-VLA in contact-rich loco-manipulation.

## 参考
- https://arxiv.org/abs/2609.03889
