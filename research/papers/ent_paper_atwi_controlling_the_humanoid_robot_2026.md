---
$id: ent_paper_atwi_controlling_the_humanoid_robot_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Controlling the Humanoid Robot H1-2 With a Simulated Biologically Plausible Network
  zh: Controlling the Humanoid Robot H1-2 With a Simulated Biologically Plausible Network
  ko: Controlling the Humanoid Robot H1-2 With a Simulated Biologically Plausible Network
summary:
  en: Artificial Spiking Neural Networks have gained remarkable attention in the last few years due to their proven ability
    in simulating biological neural cultures and producing similar activity and trends. Nevertheless, whether they can be
    trained for humanoid locomotion while retaining biological plausibility and robust performance at once remains an open
    question. We study this problem by proposing ...
  zh: 该研究由 Fatima Atwi、Constant Roux、Christian Bergaud 与 Olivier Stasse 完成，提出一种受生物启发的脉冲神经网络，并在 Unitree H1-2 人形机器人上测试其运动控制能力。作者比较了三种训练循环权重的方案：冻结循环权重的固定储备池、经奖励调制
    STDP 与 eligibility propagation 训练的网络，以及作为非生物基线的 BPTT。结果显示 e-prop 达到 100% 存活率并与 BPTT 持平，而固定储备池与奖励调制 STDP 分别仅约 43.7% 与 11%。
  ko: Artificial Spiking Neural Networks have gained remarkable attention in the last few years due to their proven ability
    in simulating biological neural cultures and producing similar activity and trends. Nevertheless, whether they can be
    trained for humanoid locomotion while retaining biological plausibility and robust performance at once remains an open
    question. We study this problem by proposing ...
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
- spiking_neural_networks
- humanoid_locomotion
- eligibility_propagation
- knowledge_distillation
- unitree_h1_2
- biologically_plausible_learning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-23'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-23). Bibliographic metadata from arXiv API (2611.26074);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2611.26074 Controlling the Humanoid Robot H1-2 With a Simulated Biologically Plausible Network
  url: https://arxiv.org/abs/2611.26074
  date: '2026-11-19'
  accessed_at: '2026-11-23'
---

## 概述

论文关注脉冲神经网络能否在保持生物合理性的同时胜任人形机器人行走控制这一开放问题。作者构建了一个生物启发的脉冲网络，所有方案均通过数据集聚合从强化学习专家策略中蒸馏学习。三种方案按生物忠实度从高到低排列：模拟体外神经培养、循环权重冻结仅训练线性读出层的固定储备池；用奖励调制 STDP 与 eligibility propagation 训练突触的网络；以及作为非生物基线的 BPTT。实验在 Unitree H1-2 人形机器人上进行，e-prop 取得 100% 存活率，与 BPTT 相当，而固定储备池与奖励调制 STDP 分别停留在约 43.7% 与约 11%。作者进一步分析了真实神经培养目前能够与不能够产生的活动趋势，并展示了全尺寸 H1-2 上的短时双足迈步。

## 核心内容

### 问题背景
脉冲神经网络（Artificial Spiking Neural Networks）近年来因能模拟生物神经培养并产生相似的活动与趋势而受到关注，但其能否在保持生物合理性的同时被训练用于人形机器人行走，仍是一个未解问题。作者以此为切入点，在 Unitree H1-2 人形机器人上评估不同学习方案。

### 方法
作者提出一个生物启发的脉冲网络，各方案的区别在于循环权重如何训练，按生物忠实度从高到低为：
- 固定储备池：模拟体外神经培养，循环权重保持冻结，仅训练线性读出层。
- 奖励调制 STDP 与 eligibility propagation（e-prop）：在同一网络上训练突触。
- BPTT（backpropagation through time）：作为非生物基线用于比较。

所有方案均依赖对强化学习专家策略的蒸馏，并结合数据集聚合（dataset aggregation）。

### 实验设置与关键结果
实验在 Unitree H1-2 人形机器人上进行。结果如下：
- e-prop 达到 100% 存活率，与 BPTT 持平。
- 固定储备池与奖励调制 STDP 虽然最接近生物培养，但性能明显较低，分别约为 43.7% 与约 11% 存活率。

作者进一步探讨了真实神经培养迄今能够与不能够产生的活动趋势。

### 结论
研究表明，在保持较高生物合理性的方案中，e-prop 能在该任务上达到与 BPTT 相当的性能，而更贴近生物培养的固定储备池与奖励调制 STDP 表现受限。作者最终展示了全尺寸 H1-2 人形机器人上的短时双足迈步。

## Overview

Artificial Spiking Neural Networks have gained remarkable attention in the last few years due to their proven ability in simulating biological neural cultures and producing similar activity and trends. Nevertheless, whether they can be trained for humanoid locomotion while retaining biological plausibility and robust performance at once remains an open question. We study this problem by proposing a biologically inspired spiking network, trained by different learning schemes and tested on the H1-2 Unitree Humanoid. These schemes differ in how recurrent weights are trained. Ordered from most to least biologically faithful, they are: a fixed reservoir mimicking an in-vitro neural culture, where recurrent weights are kept frozen and only a linear readout is trained, the same network but with its synapses trained by reward-modulated spike timing dependent plasticity and eligibility propagation, and finally backpropagation through time as a non biological baseline for comparison. All schemes relied on distillation of a reinforcement learning expert policy with dataset aggregation. We show that e-prop reached 100% survival rate matching backpropagation through time, whereas both the fixed reservoir and the reward-modulated STDP, though the closest to biological cultures, plateaued at a much lower performance (~43.7% and ~11% survival). We explore in further detail which trends a real culture could and could not produce until now. Finally we demonstrate brief bipedal stepping on a full size humanoid H1-2.

## 参考
- https://arxiv.org/abs/2611.26074
