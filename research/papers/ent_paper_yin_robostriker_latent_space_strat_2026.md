---
$id: ent_paper_yin_robostriker_latent_space_strat_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboStriker: Latent-Space Strategic Games for Autonomous Humanoid Boxing'
  zh: 'RoboStriker: Latent-Space Strategic Games for Autonomous Humanoid Boxing'
  ko: 'RoboStriker: Latent-Space Strategic Games for Autonomous Humanoid Boxing'
summary:
  en: Achieving human-level competitive intelligence and physical agility in humanoid robots remains a profound challenge,
    particularly in contact-rich and highly dynamic tasks such as boxing. While Multi-Agent Reinforcement Learning offers
    a principled framework for strategic interaction, its direct application to unstructured raw motor spaces inevitably leads
    to joint-level physical collapse, ...
  zh: RoboStriker 是一个面向人形机器人自主拳击的层级式框架，由 Kangning Yin 等研究者提出。它将拳击任务建模为潜空间中的二人零和马尔可夫博弈，通过预训练的运动解码器约束策略探索，在真实人形机器人上验证了战术性能与物理可行性。
  ko: Achieving human-level competitive intelligence and physical agility in humanoid robots remains a profound challenge,
    particularly in contact-rich and highly dynamic tasks such as boxing. While Multi-Agent Reinforcement Learning offers
    a principled framework for strategic interaction, its direct application to unstructured raw motor spaces inevitably leads
    to joint-level physical collapse, ...
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
- humanoid_robotics
- latent_space_games
- multi_agent_rl
- self_play
- contact_rich_manipulation
- real_world_deployment
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-24'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-08-24). Bibliographic metadata from arXiv API (2608.16195);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2608.16195 RoboStriker: Latent-Space Strategic Games for Autonomous Humanoid Boxing'
  url: https://arxiv.org/abs/2608.16195
  date: '2026-08-17'
  accessed_at: '2026-08-24'
---

## 概述

RoboStriker 的核心创新在于将高层的战略推理与低层的运动执行解耦，利用预训练的拳击动作解码器构建一个拓扑有界的潜空间，从而避免直接在原始动作空间中探索导致的关节级物理崩溃。该框架在理论上证明了潜空间博弈与解码器可达动作流形上的博弈等价，并提供了近似纳什解释。实验表明，在结构化潜空间中进行博弈显著优于直接探索，大幅减少了平衡失败，并在胜率和打击效率上取得优势，最终成功部署到真实人形机器人上。

## 核心内容

### 问题背景
人形机器人在接触丰富且高度动态的任务（如拳击）中，实现人类级别的竞争智能与身体敏捷性仍是巨大挑战。多智能体强化学习虽为策略交互提供了理论框架，但直接应用于非结构化的原始运动空间会导致关节级物理崩溃，无法产生可行的战斗策略。

### 方法
- **潜空间零和博弈**：将人形机器人拳击任务形式化为一个双人潜空间零和马尔可夫博弈。在标准正则性与近似最优响应假设下，证明该潜空间公式在解码器可达动作流形上诱导出一个等价博弈，从而为自对弈动力学提供近似纳什解释。
- **RoboStriker 层级框架**：将高层推理与低层执行解耦。首先，将预定义的拳击动作的跟踪技能蒸馏到一个拓扑有界的潜流形中；随后，通过潜空间神经虚构自对弈（Latent-Space Neural Fictitious Self-Play）驱动多智能体协同进化。

### 实验设置与关键结果
- 实验对比了在结构化潜空间中进行博弈与直接在原始动作空间中探索的效果。
- 结果表明，通过预训练运动解码器约束战略探索，RoboStriker 显著减少了原始动作空间方法中观察到的灾难性平衡失败。
- 在竞争胜率与打击效率方面，RoboStriker 取得了更优的战术性能。
- 学习到的战斗策略已成功部署并在真实人形机器人上得到验证。

### 结论
RoboStriker 通过将战略探索限制在预训练运动解码器定义的潜空间内，有效解决了战略探索与物理可行性之间的根本冲突，为接触丰富的人形机器人对抗任务提供了一种可行的解决方案。代码、视频及补充材料已公开。

## Overview

Achieving human-level competitive intelligence and physical agility in humanoid robots remains a profound challenge, particularly in contact-rich and highly dynamic tasks such as boxing. While Multi-Agent Reinforcement Learning offers a principled framework for strategic interaction, its direct application to unstructured raw motor spaces inevitably leads to joint-level physical collapse, preventing the emergence of any viable combat tactics. To resolve this fundamental conflict between strategic exploration and physical feasibility, we formulate the humanoid combat task as a novel two-player latent-space zero-sum Markov game. Under standard regularity and approximate best-response assumptions, we show that the latent formulation induces an equivalent game over the decoder-reachable action manifold, providing an approximate-Nash interpretation of the resulting self-play dynamics. To instantiate this theoretical formulation, we propose RoboStriker, a hierarchical framework that decouples high-level reasoning from low-level execution. It first distills the tracking expertise of predefined boxing motions into a topologically bounded latent manifold. This structured latent foundation subsequently drives multi-agent co-evolution via Latent-Space Neural Fictitious Self-Play. Extensive experimental results demonstrate that gaming within this structured latent space substantially outperforms direct exploration. By constraining strategic exploration through a pretrained motion decoder, RoboStriker substantially reduces the catastrophic balance failures observed in raw action-space methods and achieves superior tactical performance in both competitive win rates and striking efficiency. Finally, we successfully deploy and validate our learned combat policies on real-world humanoid robots. Our code and video and supplementary materials are available at RoboStriker.

## 参考
- https://arxiv.org/abs/2608.16195
