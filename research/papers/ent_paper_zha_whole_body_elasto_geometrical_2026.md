---
$id: ent_paper_zha_whole_body_elasto_geometrical_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Whole-Body Elasto-Geometrical Calibration of Wheeled Humanoid Robots Using a Shared-Waist Dual-Chain Model
  zh: Whole-Body Elasto-Geometrical Calibration of Wheeled Humanoid Robots Using a Shared-Waist Dual-Chain Model
  ko: Whole-Body Elasto-Geometrical Calibration of Wheeled Humanoid Robots Using a Shared-Waist Dual-Chain Model
summary:
  en: Wheeled humanoid robots carry both arms on one actuated waist, usually without torque sensors, so the accuracy of both
    end-effectors depends on a single waist model. After a first stage that estimates the tracker and target extrinsics, we
    identify the waist and both arms in one problem from the target positions on both flanges, measured by an optical tracker.
    The kinematic model is complete, with ...
  zh: 该论文提出一种面向轮式人形机器人的全身弹性几何标定方法，将共享腰部的双臂视为一个整体进行联合辨识。作者来自 Pengxin Zha、Yi Lu 等人组成的研究团队。核心贡献是构建包含腰部-基座、平行轴与分支参数的完整运动学模型，并用高斯先验稳定估计，在留出位姿上把平均误差从
    11.3–31.1 mm 降至 0.50–1.11 mm。
  ko: Wheeled humanoid robots carry both arms on one actuated waist, usually without torque sensors, so the accuracy of both
    end-effectors depends on a single waist model. After a first stage that estimates the tracker and target extrinsics, we
    identify the waist and both arms in one problem from the target positions on both flanges, measured by an optical tracker.
    The kinematic model is complete, with ...
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
- whole_body_calibration
- wheeled_humanoid
- elasto_geometric_model
- shared_waist
- kinematic_calibration
- compliance_modeling
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-09'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-09). Bibliographic metadata from arXiv API (2611.07560);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2611.07560 Whole-Body Elasto-Geometrical Calibration of Wheeled Humanoid Robots Using a Shared-Waist Dual-Chain
    Model
  url: https://arxiv.org/abs/2611.07560
  date: '2026-11-05'
  accessed_at: '2026-11-09'
---

## 概述

轮式人形机器人的双臂安装在同一个带驱动的腰部上，且通常没有力矩传感器，因此两个末端执行器的精度都依赖同一个腰部模型。该工作在第一阶段估计跟踪器与目标的外参之后，利用光学跟踪器测得的两侧法兰目标位置，将腰部与双臂放在同一个问题中联合辨识。其运动学模型是完整的，涵盖腰部-基座、平行轴与分支参数；臂部柔顺由实测力矩驱动，腰部柔顺由机器人质量模型的重力力矩驱动，并采用尺度经证据最大化的高斯先验来稳定估计。作者指出，独立标定与顺序单链标定都是该问题的特例，且该问题所含的腰部信息等于各单链 Schur 补之和。在两台腰部结构不同的机器人上（各自分空载与带负载两种情形），标定把留出位姿的平均误差从 11.3–31.1 mm 降到 0.50–1.11 mm；在 20 个位姿到全量的各种训练集规模下，其平均误差比两种已发表全身标定方法的改编版本低 17–63%，改进主要来自腰部柔顺。

## 核心内容

### 问题背景
轮式人形机器人的双臂共用同一个带驱动的腰部，且一般未安装力矩传感器。这意味着两个末端执行器的定位精度共同受制于单一的腰部模型，若分别标定双臂，腰部误差会被重复计入或相互矛盾。

### 方法
- 采用两阶段流程：第一阶段估计光学跟踪器与目标的外参；第二阶段以光学跟踪器测得的两侧法兰目标位置为输入，将腰部与双臂作为一个整体问题联合辨识。
- 运动学模型为完整模型，包含腰部-基座参数、平行轴参数与分支参数。
- 弹性建模：臂部柔顺由实测力矩驱动，腰部柔顺由基于机器人质量模型计算的重力力矩驱动。
- 采用高斯先验稳定估计，先验尺度通过证据最大化确定。
- 理论分析表明：独立单链标定与顺序单链标定均为该联合问题的受限形式；联合问题中的腰部信息等于各单链 Schur 补之和。

### 实验设置
在两台腰部结构不同的轮式人形机器人上验证，每台机器人分别测试空载与带负载两种情形。评价指标为留出位姿上的平均误差，并考察训练集规模从 20 个位姿到全量的影响。

### 关键结果
- 标定后留出位姿平均误差由 11.3–31.1 mm 降至 0.50–1.11 mm。
- 在 20 个位姿至全量的各训练集规模下，该方法平均误差比两种已发表全身标定方法的改编版本低 17–63%，改进主要归因于腰部柔顺的建模。
- 若采用独立标定，会得到两个不同的腰部模型；用其中任一模型同时服务双臂，会使另一条臂的误差最高升至 3.21 mm。

### 结论
将共享腰部与双臂联合建模与标定，可显著提升轮式人形机器人双末端精度；腰部柔顺是精度提升的主要来源，分开标定双臂会引入不可忽略的交叉误差。

## Overview

Wheeled humanoid robots carry both arms on one actuated waist, usually without torque sensors, so the accuracy of both end-effectors depends on a single waist model. After a first stage that estimates the tracker and target extrinsics, we identify the waist and both arms in one problem from the target positions on both flanges, measured by an optical tracker. The kinematic model is complete, with waist-base, parallel-axis, and branch parameters; arm compliances are driven by measured torques and waist compliances by gravity torques of the robot's mass model; and Gaussian priors with evidence-maximizing scales stabilize the estimate. Independent and sequential single-chain calibration are restrictions of this problem, and its waist information is the sum of the single-chain Schur complements. On two robots with different waists, each without and with a payload, calibration reduces the mean errors on held-out poses from 11.3-31.1 mm to 0.50-1.11 mm. For every training-set size from 20 poses to all, the method has 17-63% lower mean errors than adaptations of two published whole-body calibration methods, mainly through the waist compliance. Independent calibration yields two waist models; using either for both arms raises the other arm's error to up to 3.21 mm.

## 参考
- https://arxiv.org/abs/2611.07560
