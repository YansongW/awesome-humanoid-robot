---
$id: ent_paper_luan_forgetmimic_motion_unlearning_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ForgetMimic: Motion Unlearning for Reinforcement Learning Humanoid Control'
  zh: 'ForgetMimic: Motion Unlearning for Reinforcement Learning Humanoid Control'
  ko: 'ForgetMimic: Motion Unlearning for Reinforcement Learning Humanoid Control'
summary:
  en: 'Humanoid control, leveraging human demonstrations, has achieved diverse, agile, and natural locomotion behaviors through
    reinforcement learning (RL). While this paradigm has yielded remarkable performance in physical humanoid control, how
    to eliminate specific motions from learned policies remains insufficiently explored. Addressing this issue is motivated
    by pressing safety and privacy concerns: ...'
  zh: ForgetMimic 是首个面向物理世界人形机器人控制的运动级遗忘方法，由 Xukun Luan、Zhongxiang Lei、Chen Gong、Shaowei Li、Yuanguo Bi、Jinyan Liu 提出。该方法在给定于
    N 个运动上训练的策略 π_θ 时，能够削弱目标 K 个运动的性能，同时保留其余 N-K 个运动的能力。作者还识别并解决了机器人控制中导致遗忘失败的两个关键训练机制，并在 Unitree G1 与 H2 上针对 12 个运动进行了验证。
  ko: 'Humanoid control, leveraging human demonstrations, has achieved diverse, agile, and natural locomotion behaviors through
    reinforcement learning (RL). While this paradigm has yielded remarkable performance in physical humanoid control, how
    to eliminate specific motions from learned policies remains insufficiently explored. Addressing this issue is motivated
    by pressing safety and privacy concerns: ...'
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
- machine_unlearning
- humanoid_control
- reinforcement_learning
- motion_learning
- unitree_g1
- right_to_be_forgotten
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-28'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-28). Bibliographic metadata from arXiv API (2609.28378);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.28378 ForgetMimic: Motion Unlearning for Reinforcement Learning Humanoid Control'
  url: https://arxiv.org/abs/2609.28378
  date: '2026-09-23'
  accessed_at: '2026-09-28'
- id: src_002
  type: website
  title: Project page
  url: https://github.com/Zili1000/ForgetMimic
  accessed_at: '2026-09-28'
---

## 概述

人形机器人控制借助人类演示与强化学习，已能实现多样、敏捷且自然的运动行为，但如何从已学策略中消除特定运动仍缺乏探索。这一需求源于安全与隐私方面的现实压力：需要移除恶意、被投毒或次优的运动，以及受版权保护、在 GDPR 等法规下适用被遗忘权的运动。为此，作者提出 ForgetMimic，这是首个专为物理世界人形机器人控制设计的运动级遗忘方法。其核心设定是：给定在 N 个运动上训练的策略 π_θ，在削弱目标 K 个运动表现的同时保持其余 N-K 个运动有效。作者进一步指出并解决了机器人控制中导致遗忘失败的两个关键训练机制，并在 Unitree G1 和 H2 两款人形机器人上、覆盖 Dance、Fight、Flip 等 12 个运动开展了实验，结果显示该方法能有效消除指定运动的记忆，同时维持其他运动的正常运行。

## 核心内容

### 问题背景
基于人类演示的人形机器人控制通过强化学习已实现多样、敏捷、自然的运动行为，在物理人形控制中表现突出。然而，如何从已学策略中消除特定运动，此前研究尚不充分。该问题的动机来自安全与隐私的双重压力：一方面需要移除恶意、被投毒或次优的运动；另一方面，受版权保护的运动在 GDPR 等法规下可能涉及被遗忘权，因此删除特定运动能力具有关键意义。

### 方法
作者提出 ForgetMimic，这是首个面向物理世界人形机器人控制的运动级遗忘方法。其核心思想是：给定一个在 N 个运动上训练得到的策略 π_θ，方法的目标是降低该策略在目标子集 K 个运动上的性能，同时保持其余 N-K 个运动的效果不受影响。此外，作者识别出机器人控制中会导致遗忘失败的两个关键训练机制，并针对性地加以解决。

### 实验设置
实验在 Unitree G1 与 H2 两款人形机器人上进行，覆盖 12 个运动，其中包括 Dance、Fight、Flip 等。

### 关键结果
实验结果表明，ForgetMimic 能够有效消除对指定运动的记忆，同时保持所有其他运动的正常运行。

### 结论
ForgetMimic 将机器遗忘从传统的数据或模型层面拓展到物理人形控制的运动层面，在满足安全与隐私删除需求的同时，维持了策略在非目标运动上的可用性。

## Overview

Humanoid control, leveraging human demonstrations, has achieved diverse, agile, and natural locomotion behaviors through reinforcement learning (RL). While this paradigm has yielded remarkable performance in physical humanoid control, how to eliminate specific motions from learned policies remains insufficiently explored. Addressing this issue is motivated by pressing safety and privacy concerns: the removal of malicious, poisoned, or suboptimal motions, as well as copyright-protected motions subject to the right to be forgotten under regulations such as the GDPR, is of critical importance. To this end, we propose {ForgetMimic}, the first motion-level unlearning method designed specifically for physical-world humanoid control. The core idea of ForgetMimic is as follows: given a policy $π_θ$ trained on $N$ motions, our method degrades performance on a target subset of $K$ motions while preserving the effectiveness of the remaining $N-K$ motions. Furthermore, we identify and resolve two key training mechanisms in robot control that lead to unlearning failure. We conduct extensive experiments on the Unitree G1 and H2 humanoid robots across 12 motions, including Dance, Fight, Flip, and others. Experimental results demonstrate that ForgetMimic effectively eliminates memory of designated motions while maintaining the normal operation of all other motions.

## 参考
- https://arxiv.org/abs/2609.28378
- https://github.com/Zili1000/ForgetMimic
