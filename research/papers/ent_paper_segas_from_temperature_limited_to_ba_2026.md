---
$id: ent_paper_segas_from_temperature_limited_to_ba_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: From Temperature-Limited to Battery-Limited Legged Locomotion
  zh: From Temperature-Limited to Battery-Limited Legged Locomotion
  ko: From Temperature-Limited to Battery-Limited Legged Locomotion
summary:
  en: 'On legged robots, sustained locomotion often ends in thermal shutdown rather than battery depletion: the heat of walking
    concentrates in a few joint motors, which overheat long before the battery is empty. We train thermally aware locomotion
    policies by reinforcement learning without ever observing temperature, and demonstrate this on a Unitree Go2 quadruped.
    We first identify a coupled 13-node ...'
  zh: 该研究针对腿足机器人持续行走常因少数关节电机过热而被迫停机、而非电池耗尽的问题，提出一种热感知强化学习策略。作者在 Unitree Go2 四足机器人上训练策略，训练过程中完全不输入温度信息，核心是设计奖励函数压低预测的最热稳态温度。实测中该策略将持续运动从受温度限制转为受电池限制：5
    kg 负载、1 m/s 下基线 19 分钟（1.1 km）即热停机，而该策略运行 174 分钟（10.0 km）直至电池耗尽。
  ko: 'On legged robots, sustained locomotion often ends in thermal shutdown rather than battery depletion: the heat of walking
    concentrates in a few joint motors, which overheat long before the battery is empty. We train thermally aware locomotion
    policies by reinforcement learning without ever observing temperature, and demonstrate this on a Unitree Go2 quadruped.
    We first identify a coupled 13-node ...'
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
- thermally_aware_locomotion
- legged_robots
- reinforcement_learning
- thermal_modeling
- unitree_go2
- energy_efficiency
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-23'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-23). Bibliographic metadata from arXiv API (2611.22231);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2611.22231 From Temperature-Limited to Battery-Limited Legged Locomotion
  url: https://arxiv.org/abs/2611.22231
  date: '2026-11-17'
  accessed_at: '2026-11-23'
- id: src_002
  type: website
  title: Project page
  url: https://doi.org/10.5281/zenodo.24274994
  accessed_at: '2026-11-23'
---

## 概述

腿足机器人持续运动时，热量集中在少数关节电机上，往往在电池耗尽前就触发过热保护。作者首先构建并标定了一个 13 节点集总 RC 热网络模型，可预测全部十二个电机的温度，在不同机器人个体、步态、负载与速度下平均 RMSE 低于 1 °C。研究发现，持续步态下电机的稳态温度可由步态平均的力矩平方与关节转速直接推得。由于热时间常数远超强化学习的信用分配视野，作者转而用预测稳态温度构造奖励，使其在单个步态周期内即可响应力矩与转速变化，从而在无温度输入的情况下学会降低并分散发热。最终在真实机器人上，该策略把持续运动从温度受限变为电池受限。

## 核心内容

### 问题背景
腿足机器人的持续运动常常以热停机告终，而不是电池耗尽：行走产生的热量集中在少数关节电机上，这些电机远早于电池耗尽就已过热。这使机器人的实际续航由最热电机的温升决定，而非能量储备。

### 热模型
- 作者辨识出一个耦合的 13 节点集总 RC 热网络。
- 该模型在单台机器人的两次运行数据上拟合，并依据实测电功率进行校准。
- 模型能够预测全部十二个电机温度，在不同机器人个体、步态、负载与速度下平均 RMSE 低于 1 °C。
- 在持续步态下，电机最终将达到的温度可由步态平均的力矩平方与关节转速直接推出。

### 方法
核心贡献是一个奖励函数，用于压低预测的最热稳态温度（渐近温度）。难点在于热时间常数比强化学习的信用分配视野大出数个数量级；但预测的渐近温度会在单个步态周期内响应力矩与关节转速，因此策略无需任何温度输入即可学会降低并分散发热。策略通过强化学习训练，训练中从不观测温度。

### 实验设置与关键结果
实验在 Unitree Go2 四足机器人上进行。
- 5 kg 负载、1 m/s：学习得到的基线策略在 19 分钟后热停机（1.1 km）；所提策略运行 174 分钟（10.0 km）直至电池耗尽，在 26 °C 室温下最热电机比停机阈值低 14 °C。
- 无负载的工厂环路（含楼梯与坡道）：基线在 25 圈（6.2 km）后过热；所提策略用一块电池完成 47 圈（11.2 km），余量 22 °C。

### 结论
通过预测稳态温度而非直接观测温度来构造奖励，可在不输入温度的情况下学到热感知运动策略，使真实机器人上的持续运动由温度受限转变为电池受限。

## Overview

On legged robots, sustained locomotion often ends in thermal shutdown rather than battery depletion: the heat of walking concentrates in a few joint motors, which overheat long before the battery is empty. We train thermally aware locomotion policies by reinforcement learning without ever observing temperature, and demonstrate this on a Unitree Go2 quadruped. We first identify a coupled 13-node lumped RC thermal network, fitted on two runs of a single robot and calibrated against the measured electrical power, that predicts all twelve motor temperatures with a mean RMSE below 1 $^\circ$C across different robot instances, gaits, payloads, and speeds. Under a sustained gait, the temperatures the motors will settle at follow directly from the gait-averaged squared torques and joint speeds. Our core contribution is a reward that drives down the hottest predicted asymptotes: thermal time constants exceed the credit-assignment horizon of reinforcement learning by orders of magnitude, but predicted asymptotes respond to torque and joint speed within a single gait cycle, so the policy learns to lower and spread heat with no temperature input. On the robot, the policy turns sustained locomotion from temperature-limited to battery-limited: with a 5 kg payload at 1 m/s, a learned baseline reaches thermal shutdown after 19 minutes (1.1 km), whereas our policy runs the battery down after 174 minutes (10.0 km) with its hottest motor 14 $^\circ$C below the shutdown threshold in a 26 $^\circ$C room; on an unloaded factory circuit with stairs and ramps, the baseline overheats after 25 laps (6.2 km), while our policy completes 47 (11.2 km) on one battery with 22 $^\circ$C of margin.

## 参考
- https://arxiv.org/abs/2611.22231
- https://doi.org/10.5281/zenodo.24274994
