---
$id: ent_paper_yi_swap_test_time_steerable_human_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SWAP: Test-Time Steerable Humanoid Whole-Body Collision Avoidance'
  zh: 'SWAP: Test-Time Steerable Humanoid Whole-Body Collision Avoidance'
  ko: 'SWAP: Test-Time Steerable Humanoid Whole-Body Collision Avoidance'
summary:
  en: 'Humanoid robots operating in human-centric environments must coordinate the entire body to traverse tight, cluttered
    spaces while maintaining balance. Existing methods often struggle to jointly consider dynamic stability and collision
    avoidance from high-dimensional perceptual inputs. Moreover, for humanoids, safe behavior is inherently multimodal: the
    same obstacle may admit multiple valid ...'
  zh: SWAP（Steerable Whole-body Avoidance Policy）是一个面向人形机器人全身避障的分层框架，由 Zeji Yi、Guanqi He、Xiaofeng Guo、Guannan Qu、Pieter Abbeel、Yan
    Duan、Karen Liu、Guanya Shi 提出。该框架将碰撞感知决策与稳定控制解耦：高层基于感知条件的扩散策略生成多模态避障运动提案，低层全身 RL 控制器负责跟踪并维持动态平衡。作者通过 hindsight labeling
    构造可扩展监督，并在部署时用 Monte Carlo 采样与简单代价信号实现测试时引导，在仿真与真实 Unitree G1 上验证了静态与动态障碍物避障能力，目标奖励平均提升 34%。
  ko: 'Humanoid robots operating in human-centric environments must coordinate the entire body to traverse tight, cluttered
    spaces while maintaining balance. Existing methods often struggle to jointly consider dynamic stability and collision
    avoidance from high-dimensional perceptual inputs. Moreover, for humanoids, safe behavior is inherently multimodal: the
    same obstacle may admit multiple valid ...'
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
- humanoid_collision_avoidance
- whole_body_control
- diffusion_policy
- hierarchical_control
- test_time_steering
- hindsight_labeling
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-26'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-26). Bibliographic metadata from arXiv API (2610.25711);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.25711 SWAP: Test-Time Steerable Humanoid Whole-Body Collision Avoidance'
  url: https://arxiv.org/abs/2610.25711
  date: '2026-10-19'
  accessed_at: '2026-10-26'
- id: src_002
  type: website
  title: Project page
  url: https://iscoyizj.github.io/SWAP-steerable-humanoid-oa-website/
  accessed_at: '2026-10-26'
---

## 概述

人形机器人在以人为中心的环境中需要协调全身穿越狭窄杂乱空间并保持平衡，但现有方法难以从高维感知输入中同时兼顾动态稳定性与避障，且安全行为本身具有多模态性——同一障碍物可能存在多种可行穿越方式，单一确定性策略难以表达。为此，作者提出 SWAP 分层框架，把碰撞感知决策交给高层、把稳定控制交给低层：高层是感知条件扩散策略，输出多模态且碰撞感知的运动提案；低层是全身 RL 控制器，负责跟踪提案并维持动态平衡。为高效训练高层策略，作者采用 hindsight labeling 获得可扩展监督：在随机指令下滚动低层策略，仅在已执行运动未扫过的空间放置障碍物，使运动在构造上无碰撞，并重新渲染机器人本应看到的感知。部署阶段，Monte Carlo 采样配合简单代价信号即可将扩散模型引导向安全且符合任务的行为，无需繁重的奖励调参。仿真与真实 Unitree G1 实验显示该方法对静态和动态障碍物均能可靠避障，测试时引导还带来可定制性，使速度、朝向或姿态等目标奖励平均提升 34%，同时保持较高的避障成功率。

## 核心内容

### 问题背景

人形机器人在人类环境中作业时，必须协调全身穿越狭窄、杂乱的区域，同时维持动态平衡。现有方法存在两方面不足：一是难以从高维感知输入中联合考虑动态稳定性与碰撞避免；二是人形机器人的安全行为本质上是多模态的——同一障碍物可能允许多种有效穿越方式，单一确定性策略难以表达这种多样性。

### 方法

作者提出 SWAP（Steerable Whole-body Avoidance Policy），一个分层框架，将碰撞感知决策与稳定控制分离：

- **高层策略**：感知条件扩散策略，生成多模态、碰撞感知的运动提案。
- **低层控制器**：全身 RL 控制器，跟踪高层提案并维持动态平衡。

为高效训练高层策略，作者设计了基于 hindsight labeling 的可扩展监督流程：

- 在随机指令下滚动低层策略；
- 仅在已执行运动未扫过的空间放置障碍物，使该运动在构造上即为无碰撞；
- 重新渲染机器人本应看到的感知输入。

部署阶段，采用 Monte Carlo 采样配合简单代价信号，将扩散模型引导向安全且符合任务的行为，无需繁重的奖励调参。

### 实验设置

实验在仿真环境与真实 Unitree G1 人形机器人上进行，测试场景包含静态障碍物与动态障碍物。

### 关键结果

- 在仿真与真实 Unitree G1 上均实现可靠避障，覆盖静态与动态障碍物。
- 测试时引导支持行为定制：针对速度、朝向或姿态等目标奖励，平均提升 34%，同时保持较高的避障成功率。

### 结论

结果表明，SWAP 为人形机器人全身避障提供了一种具备测试时可引导性的实用方案。项目网站：https://iscoyizj.github.io/SWAP-steerable-humanoid-oa-website/

## Overview

Humanoid robots operating in human-centric environments must coordinate the entire body to traverse tight, cluttered spaces while maintaining balance. Existing methods often struggle to jointly consider dynamic stability and collision avoidance from high-dimensional perceptual inputs. Moreover, for humanoids, safe behavior is inherently multimodal: the same obstacle may admit multiple valid traversals, which is difficult to represent with a single deterministic policy. To address these challenges, we propose SWAP (Steerable Whole-body Avoidance Policy), a hierarchical framework that separates collision-aware decision making from stabilization. A high-level, perception-conditioned diffusion policy generates multimodal, collision-aware motion proposals, while a low-level whole-body RL controller tracks these proposals and maintains dynamic balance. To efficiently train the high-level policy, we obtain scalable supervision via hindsight labeling: we roll out the low-level policy under randomized commands, place obstacles only in the space that each executed motion did not sweep, so the motion is collision-free by construction, and re-render the perception the robot would have seen. At deployment, Monte Carlo sampling with simple cost signals steers the diffusion model toward safe, task-aligned behaviors without heavy reward tuning. Experiments in simulation and on a real Unitree G1 humanoid show reliable avoidance with static and dynamic obstacles. Test-time steering further enables customization, improving targeted rewards (e.g., speed, orientation, or posture) by 34% on average while maintaining a high collision avoidance rate. Together, these results support a practical solution to humanoid whole-body collision avoidance with test-time steerability. Project website: https://iscoyizj.github.io/SWAP-steerable-humanoid-oa-website/

## 参考
- https://arxiv.org/abs/2610.25711
- https://iscoyizj.github.io/SWAP-steerable-humanoid-oa-website/
