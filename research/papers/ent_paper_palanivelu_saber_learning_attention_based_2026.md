---
$id: ent_paper_palanivelu_saber_learning_attention_based_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SABER: Learning Attention-based Semantic Affordance for Legged Locomotion'
  zh: 'SABER: Learning Attention-based Semantic Affordance for Legged Locomotion'
  ko: 'SABER: Learning Attention-based Semantic Affordance for Legged Locomotion'
summary:
  en: 'Perceptive legged locomotion has advanced rapidly by integrating terrain geometry into learned policies, yet the integration
    of terrain meaning remains sparse: a pipe, a patch of grass, or a fragile box may be geometrically traversable while being
    inappropriate for contact. In industrial environments, where legged robots increasingly operate, a single misplaced step
    can damage fragile equipment, ...'
  zh: SABER 是一种无规划器的强化学习策略，由 Hari Prasanth Palanivelu 等人提出，可同时推理地形几何与语义接触许可。它使用统一的地形可供性地图，并通过带符号语义偏置的交叉注意力机制，让危险区域在仍能影响下一步落脚点时重塑注意力。在
    Unitree B2 上的实验表明，仅移除语义偏置就会使违禁接触增加 55%，而速度跟踪性能不变。
  ko: 'Perceptive legged locomotion has advanced rapidly by integrating terrain geometry into learned policies, yet the integration
    of terrain meaning remains sparse: a pipe, a patch of grass, or a fragile box may be geometrically traversable while being
    inappropriate for contact. In industrial environments, where legged robots increasingly operate, a single misplaced step
    can damage fragile equipment, ...'
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
- legged_locomotion
- semantic_affordance
- cross_attention
- sim_to_real
- reinforcement_learning
- terrain_awareness
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-21'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-21). Bibliographic metadata from arXiv API (2609.21572);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.21572 SABER: Learning Attention-based Semantic Affordance for Legged Locomotion'
  url: https://arxiv.org/abs/2609.21572
  date: '2026-09-18'
  accessed_at: '2026-09-21'
---

## 概述

在工业场景中，管道、草地或易碎箱子等区域虽然几何上可通行，却未必适合落脚，而现有感知式足式运动研究大多只关注地形几何，忽略了地形的语义含义。SABER 通过一张统一的地形可供性地图，将局部三维几何与语义接触代价编码到每个栅格中，从而让策略同时考虑几何与语义接触许可。其核心是在交叉注意力上引入一个可学习的带符号语义偏置，该偏置作为注意力 logits 上的加性项，由接触代价门控，并按栅格到最近足端的距离重新加权。这样，危险区域只会在仍能影响下一次落脚点的位置改变注意力，其影响在无法影响落脚点处自然衰减。策略最终在允许支撑面上选择落脚点，并在整个摆动阶段让腿部避开禁区。

## 核心内容

### 问题背景
感知式足式运动通过将地形几何融入学习策略取得了快速进展，但地形语义的整合仍然稀少。管道、草地或易碎箱子在几何上可能可通行，却不适合接触。在足式机器人日益应用的工业环境中，一次错误的落脚就可能损坏易碎设备、使机器人失稳或危及现场安全。

### 方法
- 提出 SABER，一种无规划器的强化学习策略，联合推理地形几何与语义接触许可。
- 策略输入为统一的地形可供性地图，每个栅格编码局部三维几何与一个语义接触代价。
- 在交叉注意力中引入可学习的带符号语义偏置：该偏置是注意力 logits 上的加性项，由接触代价门控，并按栅格到最近足端的距离重新加权。
- 由此，危险区域会在仍能影响下一次落脚点的位置重塑注意力，而在无法影响落脚点处其影响逐渐消退。
- 最终策略在允许的支撑面上选择落脚点，并在整个摆动阶段让腿部避开禁区。

### 实验设置
- 在 Unitree B2 机器人上验证策略。
- 覆盖室内与室外环境，以及四类语义障碍。
- 进行了系统性消融，以分离各架构组件的贡献。

### 关键结果
- 仅移除语义偏置，违禁接触增加 55%，而速度跟踪保持不变。
- 展示了跨室内外环境与四类语义障碍的 sim-to-real 语义接触选择能力。

### 结论
SABER 表明，将语义接触许可与地形几何联合建模，可让足式机器人在保持速度跟踪的同时显著减少违禁接触，并成功实现从仿真到真实机器人的语义接触选择。

## Overview

Perceptive legged locomotion has advanced rapidly by integrating terrain geometry into learned policies, yet the integration of terrain meaning remains sparse: a pipe, a patch of grass, or a fragile box may be geometrically traversable while being inappropriate for contact. In industrial environments, where legged robots increasingly operate, a single misplaced step can damage fragile equipment, destabilize the robot, or endanger the site. To address this, we introduce SABER, a planner-free reinforcement-learning policy that jointly reasons about terrain geometry and semantic contact permission. The policy consumes a unified terrain-affordance map, where each cell encodes local 3D geometry and a semantic contact cost. We augment cross-attention with a learned, signed semantic bias: an additive term on the attention logits, gated by the contact cost, that reweights flagged cells by their distance from the nearest foot. A hazard therefore reshapes attention where it can still affect the next foothold, and its influence fades where it cannot. The resulting policy selects footholds on permitted support and keeps the leg clear of forbidden regions throughout the swing phase. We perform a systematic ablation that isolates the contribution of each architectural component; removing the semantic bias alone increases forbidden contacts by 55% while velocity tracking is unchanged. We validate the policy on a Unitree B2, demonstrating sim-to-real semantic contact selection across indoor and outdoor environments and four semantic obstacle classes.

## 参考
- https://arxiv.org/abs/2609.21572
