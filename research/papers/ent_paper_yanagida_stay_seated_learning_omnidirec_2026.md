---
$id: ent_paper_yanagida_stay_seated_learning_omnidirec_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Stay Seated: Learning Omnidirectional Humanoid Locomotion on a Passive Mobile Chair with Casters'
  zh: 'Stay Seated: Learning Omnidirectional Humanoid Locomotion on a Passive Mobile Chair with Casters'
  ko: 'Stay Seated: Learning Omnidirectional Humanoid Locomotion on a Passive Mobile Chair with Casters'
summary:
  en: Humanoid robots with quasi-direct-drive actuators continuously generate joint torque while standing, whereas seated
    humans delegate weight support to chairs during desk work. As a first step toward seated loco-manipulation, we study omnidirectional
    seated locomotion on a passive mobile chair, requiring unfixed pelvis-seat contact and intermittent foot-floor propulsion
    of the robot-chair system. ...
  zh: 本研究由 Kango Yanagida、Kazuki Miyazawa 和 Takato Horii 提出，首次探索人形机器人在被动移动椅子上实现全向坐姿运动，通过扩展站立速度跟踪环境并引入被动椅子模型与坐姿奖励，策略仅依赖本体感觉和速度指令即可学习。实验表明，最佳坐姿策略在速度跟踪上优于站立策略，并在
    Unitree G1 上实现零样本仿真到现实迁移。
  ko: Humanoid robots with quasi-direct-drive actuators continuously generate joint torque while standing, whereas seated
    humans delegate weight support to chairs during desk work. As a first step toward seated loco-manipulation, we study omnidirectional
    seated locomotion on a passive mobile chair, requiring unfixed pelvis-seat contact and intermittent foot-floor propulsion
    of the robot-chair system. ...
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
- seated_locomotion
- humanoid_robots
- passive_chair
- sim_to_real
- velocity_tracking
- reinforcement_learning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-31'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-08-31). Bibliographic metadata from arXiv API (2608.28090);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2608.28090 Stay Seated: Learning Omnidirectional Humanoid Locomotion on a Passive Mobile Chair with Casters'
  url: https://arxiv.org/abs/2608.28090
  date: '2026-08-28'
  accessed_at: '2026-08-31'
---

## 概述

该工作针对人形机器人坐姿操作的第一步，研究在带脚轮的被动移动椅子上的全向运动，涉及不固定的骨盆-椅子接触和间歇性足部推进。作者扩展了标准站立速度跟踪环境，加入被动椅子模型、坐姿状态奖励、仅评论家椅子观测和任务定制接触设置，策略无需运动模仿奖励即可学习。通过随机指令评估，策略在几乎全部 20 秒滚动中跟踪全向指令，且最佳坐姿策略在速度跟踪上超越站立策略。消融实验显示脚滑正则化（FS）降低运输成本（CoT）但增加跟踪误差，与对称正则化（SY）或指令课程（CC）结合可避免局部最优。最终策略在 Unitree G1 上实现零样本迁移。

## 核心内容

### 问题背景
人形机器人采用准直驱执行器时，站立状态需持续产生关节力矩以维持平衡，而人类在办公桌前工作时会将体重支撑委托给椅子。为迈向坐姿移动操作，本研究聚焦于被动移动椅子上的全向坐姿运动，该任务要求处理不固定的骨盆-椅子接触和机器人-椅子系统的间歇性足部地面推进。

### 方法
作者扩展了标准站立速度跟踪环境，具体修改包括：
- 引入被动椅子模型，模拟带脚轮椅子的动力学。
- 设计坐姿状态奖励，鼓励机器人保持坐姿并利用椅子支撑。
- 采用仅评论家椅子观测，使策略网络（演员）无需椅子状态信息。
- 定制接触设置，以适应坐姿下足部与地面的间歇性接触模式。

策略训练不使用运动模仿奖励，演员网络仅依赖本体感觉（如关节角度、速度）和速度指令，不接收接触传感或椅子状态输入。

### 实验设置
- 训练使用四种随机种子，进行 $2^3$ 全因子比较，因素包括对称正则化（SY）、脚滑正则化（FS）和指令课程（CC）。
- 评估采用随机指令，每次滚动持续 20 秒。
- 消融实验分析各正则化组合对运输成本（CoT）、跟踪误差和腿部对称性的影响。

### 关键结果
- 在随机指令评估中，策略在几乎所有 20 秒滚动中成功跟踪全向指令。
- 最佳坐姿策略在速度跟踪上优于站立策略（Standing policy）。
- FS 单独使用可降低 CoT，但增加跟踪误差，且部分 FS-only 策略收敛到静止局部最优。
- 将 FS 与 SY 或 CC 结合可避免上述失败，无需重新调整 FS 参数；SY 还改善了纵向运动中的双腿对称性。
- 方向分解分析显示 CoT 排序为：后退 < 侧向 << 前进；后退和侧向运动中植腿伸展，前进运动中脚跟接触后出现膝屈曲。
- 学习策略在 Unitree G1 上实现零样本仿真到现实迁移，成功生成全向坐姿运动。

### 结论
该研究首次证明人形机器人可在被动移动椅子上学习全向坐姿运动，且无需接触传感或椅子状态信息。正则化组合策略有效平衡了效率与稳定性，为未来坐姿移动操作奠定了基础。

## Overview

Humanoid robots with quasi-direct-drive actuators continuously generate joint torque while standing, whereas seated humans delegate weight support to chairs during desk work. As a first step toward seated loco-manipulation, we study omnidirectional seated locomotion on a passive mobile chair, requiring unfixed pelvis-seat contact and intermittent foot-floor propulsion of the robot-chair system. We extend a standard standing velocity-tracking environment with a passive-chair model, seated-state rewards, critic-only chair observations, and task-tailored contact settings. The policy is learned without motion-imitation rewards; its actor uses only proprioception and velocity commands, without contact sensing or chair states. In random-command evaluation, the policies tracked omnidirectional commands through nearly all 20-s rollouts, and the best seated policies could outperform the Standing policy in velocity tracking. Across four training seeds, a $2^3$ full-factorial comparison of symmetry regularization (SY), foot-slip regularization (FS), and command curriculum (CC) showed that FS reduced CoT but increased tracking error and that some FS-only policies converged to stationary local optima. Combining FS with either SY or CC avoided this failure without retuning FS, while SY improved bilateral leg symmetry during longitudinal motion. Direction-resolved analysis showed CoT ordered backward $<$ lateral $\ll$ forward, with planted-leg extension in backward and lateral motion and knee flexion following heel contact in forward motion. The learned policy achieved zero-shot sim-to-real transfer to a Unitree G1 and generated omnidirectional seated locomotion.

## 参考
- https://arxiv.org/abs/2608.28090
