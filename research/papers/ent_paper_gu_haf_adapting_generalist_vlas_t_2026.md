---
$id: ent_paper_gu_haf_adapting_generalist_vlas_t_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HAF: Adapting Generalist VLAs to Humanoid Whole-Body Loco-manipulation via Hierarchical Action Flow and Spectral Latent
    RL'
  zh: 'HAF: Adapting Generalist VLAs to Humanoid Whole-Body Loco-manipulation via Hierarchical Action Flow and Spectral Latent
    RL'
  ko: 'HAF: Adapting Generalist VLAs to Humanoid Whole-Body Loco-manipulation via Hierarchical Action Flow and Spectral Latent
    RL'
summary:
  en: Humanoid robots hold great promise as general-purpose agents in human-centered environments, yet generalist vision-language-action
    (VLA) foundation models are not readily applicable to humanoid whole-body loco-manipulation. The high dimensionality and
    interdependence of humanoid motions make it challenging for conventional single-stage VLA architectures to coordinate
    locomotion, waist posture, ...
  zh: HAF（人形机器人适配框架）由 HAF-VLA 和 HAF-Steer 两部分组成，将通用视觉-语言-动作（VLA）基础模型迁移到人形机器人全身移动操作任务。HAF-VLA 采用分层动作流生成器，将全身动作去噪分解为三个顺序阶段；HAF-Steer
    利用流匹配可逆性和 DCT 降维，在冻结的 VLA 骨干上实现高效的离线到在线强化学习。在七个真实世界人形移动操作任务中，HAF 优于单阶段 VLA 基线，提升了全身协调性和任务性能。
  ko: Humanoid robots hold great promise as general-purpose agents in human-centered environments, yet generalist vision-language-action
    (VLA) foundation models are not readily applicable to humanoid whole-body loco-manipulation. The high dimensionality and
    interdependence of humanoid motions make it challenging for conventional single-stage VLA architectures to coordinate
    locomotion, waist posture, ...
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
- humanoid_locomotion
- whole_body_control
- vision_language_action
- reinforcement_learning
- flow_matching
- hierarchical_policy
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-24'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-08-24). Bibliographic metadata from arXiv API (2608.16837);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2608.16837 HAF: Adapting Generalist VLAs to Humanoid Whole-Body Loco-manipulation via Hierarchical Action
    Flow and Spectral Latent RL'
  url: https://arxiv.org/abs/2608.16837
  date: '2026-08-17'
  accessed_at: '2026-08-24'
- id: src_002
  type: website
  title: Project page
  url: https://grange007.github.io/HAF
  accessed_at: '2026-08-24'
---

## 概述

HAF 由来自多家机构的 Langzhe Gu、Chengkai Hou、Meng Li 等研究者提出，旨在解决通用 VLA 基础模型难以直接应用于人形机器人全身移动操作的问题。HAF-VLA 通过阶段嵌入和跨阶段 KV 缓存保留运动学依赖，避免一次性生成导致的不连贯全身动作；HAF-Steer 则在冻结的 HAF-VLA 之上，将强化学习限制在紧凑噪声子空间，训练正则化 SAC 策略，无需更新大型 VLA 骨干即可进行真实世界策略优化。实验在七个真实世界任务上验证了方法的有效性。

## 核心内容

### 问题背景
人形机器人有望成为人类中心环境中的通用智能体，但通用 VLA 基础模型难以直接用于全身移动操作。人形运动的高维性和关节间的强耦合性，使传统单阶段 VLA 架构难以有效协调腿部运动、腰部姿态和双臂操作。此外，离线行为克隆训练的策略在真实部署中可能次优，而在线强化学习虽能通过真实交互优化策略，但直接微调大型 VLA 骨干计算开销过大，且真实机器人探索存在安全风险。

### 方法
HAF 框架包含两个核心组件：
- **HAF-VLA**：基于预训练的流匹配 VLA 构建的分层动作流生成器。它将全身动作去噪拆分为三个顺序阶段，引入阶段嵌入和跨阶段 KV 缓存来保留运动学依赖，避免一次性生成导致的全身动作不连贯。
- **HAF-Steer**：在冻结的 HAF-VLA 之上运行的潜在空间离线到在线强化学习管线。利用流匹配的可逆性和基于 DCT 的降维，将强化学习优化限制在紧凑噪声子空间，并训练正则化 SAC 策略。该方法避免更新大型 VLA 骨干，支持高效的真实世界策略优化。

### 实验设置与结果
在七个真实世界人形移动操作任务上进行了评估。与普通单阶段 VLA 基线相比，HAF 在全身协调性和任务性能上均取得更优结果。具体实验细节（如任务类型、量化指标数值）在摘要中未详细披露。

### 结论
HAF 通过分层动作流生成和潜在空间强化学习，有效解决了通用 VLA 向人形全身移动操作迁移的瓶颈，为真实世界人形机器人策略优化提供了高效且安全的方案。项目网站：https://grange007.github.io/HAF

## Overview

Humanoid robots hold great promise as general-purpose agents in human-centered environments, yet generalist vision-language-action (VLA) foundation models are not readily applicable to humanoid whole-body loco-manipulation. The high dimensionality and interdependence of humanoid motions make it challenging for conventional single-stage VLA architectures to coordinate locomotion, waist posture, and dual-arm manipulation effectively. Moreover, policies trained through offline behavior cloning can remain suboptimal during real-world deployment. Although online reinforcement learning can refine policies through real-world interaction, directly tuning large VLA backbones demands excessive computation and may introduce safety risks during real-robot exploration. To address these bottlenecks, we introduce HAF (Humanoid Adaptation Framework), a two-part framework consisting of HAF-VLA and HAF-Steer that transfers off-the-shelf generalist VLA foundation models to humanoid whole-body loco-manipulation. HAF-VLA is a hierarchical action-flow generator built on a pretrained flow-matching VLA. It splits full-body action denoising into three sequential stages with stage embeddings and cross-stage KV caches that retain kinematic dependencies, avoiding incoherent whole-body actions from one-shot generation. On top of the frozen HAF-VLA, HAF-Steer is a latent offline-to-online RL pipeline that leverages flow-matching invertibility and DCT-based dimensionality reduction to restrict RL optimization to a compact noise subspace and train a regularized SAC policy. This avoids updating the large VLA backbone and enables efficient real-world policy refinement. Evaluated on seven real-world humanoid loco-manipulation tasks, HAF surpasses vanilla single-stage VLA baselines and improves whole-body coordination and task performance. Project website: https://grange007.github.io/HAF .

## 参考
- https://arxiv.org/abs/2608.16837
- https://grange007.github.io/HAF
