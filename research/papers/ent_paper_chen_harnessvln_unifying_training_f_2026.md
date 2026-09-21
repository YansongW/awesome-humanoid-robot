---
$id: ent_paper_chen_harnessvln_unifying_training_f_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HarnessVLN: Unifying Training-Free Embodied Navigation through an Agent Harness'
  zh: 'HarnessVLN: Unifying Training-Free Embodied Navigation through an Agent Harness'
  ko: 'HarnessVLN: Unifying Training-Free Embodied Navigation through an Agent Harness'
summary:
  en: Embodied navigation requires agents to ground instructions or object goals in spatial observations and translate plans
    into successful execution. As multimodal large language models (MLLMs) become increasingly capable, they offer stronger
    support for navigation without task-specific training; however, improved semantic reasoning alone does not ensure that
    proposed actions remain consistent with ...
  zh: HarnessVLN 是一个零样本、免训练的统一具身导航框架，通过共享的 Agent Harness 将指令跟随导航与物体目标导航统一起来。该工作由 Yang Chen、Lirong Che、Zhenyu Huang 等人完成。其核心在于由
    Harness 协调感知、记忆与执行工具，并在动作下发前对规划器提案进行证据支持、几何可行性与子目标一致性校验，在 R2R、RxR、HM3D-v2 与 HM3D-OVON 上分别取得 60.8%、53.9%、76.0% 与 59.3%
    的成功率。
  ko: Embodied navigation requires agents to ground instructions or object goals in spatial observations and translate plans
    into successful execution. As multimodal large language models (MLLMs) become increasingly capable, they offer stronger
    support for navigation without task-specific training; however, improved semantic reasoning alone does not ensure that
    proposed actions remain consistent with ...
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
- embodied_navigation
- training_free
- zero_shot
- multimodal_large_language_models
- spatiotemporal_graph
- humanoid_robot
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-21'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-21). Bibliographic metadata from arXiv API (2609.15195);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.15195 HarnessVLN: Unifying Training-Free Embodied Navigation through an Agent Harness'
  url: https://arxiv.org/abs/2609.15195
  date: '2026-09-14'
  accessed_at: '2026-09-21'
---

## 概述

具身导航要求智能体把指令或物体目标落地到空间观测中，并将规划转化为可成功执行的行动。随着多模态大语言模型能力增强，无需任务特定训练即可为导航提供更强支持，但语义推理的改善并不能保证所提出的动作与空间证据、任务进度及执行结果保持一致。为此，作者提出 HarnessVLN，一个零样本、免训练框架，通过共享的 Agent Harness 统一指令跟随与物体目标两类导航任务。该 Harness 以统一接口协调感知、记忆与执行工具，在动作派发前对规划器提案进行证据支持、几何可行性与子目标一致性校验，并联合管理分层事件记忆与持久化的 Spatiotemporal Graph，以跟踪任务进度、保留空间证据并为失败提供上下文。结构化执行反馈会更新这一共享状态，从而引导后续规划、恢复与终止。在 R2R、RxR、HM3D-v2 与 HM3D-OVON 上，HarnessVLN 的成功率分别为 60.8%、53.9%、76.0% 与 59.3%，优于此前的免训练最先进方法；人形机器人部署进一步表明其可应用于真实环境中的两类导航任务。

## 核心内容

### 问题背景
具身导航需要智能体将指令或物体目标与空间观测对齐，并把规划落实为成功执行。多模态大语言模型（MLLMs）能力提升后，为免任务特定训练的导航提供了更强支撑，但语义推理的增强本身并不能保证所提出的动作始终与空间证据、任务进度和执行结果保持一致。

### 方法
- 提出 HarnessVLN，一个零样本、免训练的框架，通过共享的 Agent Harness 统一指令跟随导航与物体目标导航。
- Harness 以统一接口协调感知、记忆与执行工具。
- 在动作派发之前，Harness 会对规划器提案进行三重校验：证据支持、几何可行性、子目标一致性。
- Harness 联合管理分层事件记忆与持久化的 Spatiotemporal Graph，用于跟踪任务进度、保留空间证据，并为失败提供上下文。
- 结构化执行反馈会更新这一共享状态，进而引导后续的规划、恢复与终止。

### 实验设置与关键结果
- 在 R2R、RxR、HM3D-v2 与 HM3D-OVON 四个基准上进行评估。
- 成功率分别为 60.8%、53.9%、76.0% 与 59.3%。
- 在上述基准上均优于此前的免训练最先进方法。
- 通过人形机器人部署，进一步展示了该方法在真实环境中对两类导航任务的适用性。
- 项目页面：https://agibot-harnessvln.netlify.app/

### 结论
HarnessVLN 表明，借助统一的 Agent Harness 对规划提案进行校验并维护共享的时空状态，可以在完全免训练、零样本的条件下统一两类具身导航任务，并取得优于既有免训练方法的成功率，同时具备向真实人形机器人环境迁移的可行性。

## Overview

Embodied navigation requires agents to ground instructions or object goals in spatial observations and translate plans into successful execution. As multimodal large language models (MLLMs) become increasingly capable, they offer stronger support for navigation without task-specific training; however, improved semantic reasoning alone does not ensure that proposed actions remain consistent with spatial evidence, task progress, and execution outcomes. We introduce HarnessVLN, a zero-shot, training-free framework that unifies instruction-following and object-goal navigation through a shared Agent Harness. The Harness coordinates perception, memory, and execution tools through a unified interface, validating planner proposals for evidential support, geometric feasibility, and subgoal consistency before dispatch. It jointly manages hierarchical event memory and a persistent Spatiotemporal Graph to track task progress, preserve spatial evidence, and contextualize failures. Structured execution feedback updates this shared state, guiding subsequent planning, recovery, and termination. Across R2R, RxR, HM3D-v2, and HM3D-OVON, HarnessVLN achieves success rates of 60.8%, 53.9%, 76.0%, and 59.3%, respectively, outperforming prior training-free state-of-the-art methods. Humanoid robot deployment further demonstrates its applicability to both navigation tasks in real-world environments. The project page is available at https://agibot-harnessvln.netlify.app/.

## 参考
- https://arxiv.org/abs/2609.15195
