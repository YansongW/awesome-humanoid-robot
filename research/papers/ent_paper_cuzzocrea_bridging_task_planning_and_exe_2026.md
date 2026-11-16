---
$id: ent_paper_cuzzocrea_bridging_task_planning_and_exe_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Bridging Task Planning and Execution for Language-Conditioned Bimanual Manipulation
  zh: Bridging Task Planning and Execution for Language-Conditioned Bimanual Manipulation
  ko: Bridging Task Planning and Execution for Language-Conditioned Bimanual Manipulation
summary:
  en: Robots are increasingly expected to execute natural-language manipulation tasks in real-world environments. This is
    particularly relevant in household assistance and logistics, where clutter requires reasoning about both task objectives
    and execution feasibility. This challenge becomes even more pronounced for bimanual humanoid platforms, where coordinating
    two manipulators introduces additional ...
  zh: 该论文提出一个零样本视觉语言框架，用于语言条件下的双臂操作，将任务目标与物理可行性联合推理。作者为 Emanuele Cuzzocrea、Giuseppina Iannotti、Luca Rossini、Arturo Laurenzi
    与 Nikos Tsagarakis。核心贡献在于以结构化场景表示支撑规划、将兼容动作组织为带前后条件的并行双臂阶段，并用分层验证器在感知不确定性下支持局部恢复或定向重规划；在 CENTAURO 混合轮腿人形机器人上的九个语言条件场景中取得更高任务成功率。
  ko: Robots are increasingly expected to execute natural-language manipulation tasks in real-world environments. This is
    particularly relevant in household assistance and logistics, where clutter requires reasoning about both task objectives
    and execution feasibility. This challenge becomes even more pronounced for bimanual humanoid platforms, where coordinating
    two manipulators introduces additional ...
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
- bimanual_manipulation
- language_conditioned_manipulation
- task_planning
- vision_language_framework
- humanoid_robot
- execution_aware_planning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-16'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-16). Bibliographic metadata from arXiv API (2611.12409);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2611.12409 Bridging Task Planning and Execution for Language-Conditioned Bimanual Manipulation
  url: https://arxiv.org/abs/2611.12409
  date: '2026-11-09'
  accessed_at: '2026-11-16'
---

## 概述

论文关注机器人在杂乱真实环境中执行自然语言操作任务的需求，这一需求在家庭辅助与物流场景中尤为突出，而双臂人形平台还需应对两个操作臂协调带来的额外交互与运动学约束。作者提出一个零样本视觉语言框架，使规划同时考虑任务目标与执行可行性。规划建立在结构化场景表示之上，该表示把语义物体关系与执行约束结合起来，从而在保持任务语义的前提下选择障碍物搬移与执行方式。兼容动作被组织为并行的双臂阶段，并带有明确的前置与后置条件；分层验证器在感知不确定性下评估这些条件，并利用阶段级执行历史支持局部恢复或定向重规划。在 CENTAURO 混合轮腿人形机器人上的九个语言条件操作场景实验中，该方法任务成功率高于不具备执行感知的基线；在专门的失败场景中，分层验证以比始终重规划更少的模型查询次数从执行失败中恢复。

## 核心内容

### 问题背景
机器人被越来越多地期望在真实环境中执行自然语言描述的操作任务，家庭辅助与物流场景尤其如此：环境杂乱时，系统既要推理任务目标，也要判断执行是否可行。对双臂人形平台而言，两个操作臂的协调还会引入额外的交互与运动学约束，使问题更加突出。

### 方法
作者提出一个零样本视觉语言框架，用于具备执行感知的双臂操作，对任务目标与物理可行性进行联合推理。其要点包括：

- **结构化场景表示**：将语义物体关系与执行约束结合，规划建立在这一表示之上，从而在保持任务语义的同时选择障碍物搬移方案与执行方式。
- **并行双臂阶段**：把兼容动作组织为并行的双臂阶段，每个阶段带有明确的前置条件与后置条件。
- **分层验证器**：在感知不确定性下评估上述条件，并利用阶段级执行历史支持局部恢复或定向重规划。

### 实验设置
实验在 CENTAURO 混合轮腿人形机器人上进行，覆盖九个语言条件操作场景，并与一个不具备执行感知的基线方法比较。此外还设置了专门的失败场景，用于考察分层验证的恢复能力。

### 关键结果
- 在九个语言条件操作场景中，该方法任务成功率高于非执行感知基线。
- 在专门的失败场景中，分层验证能够从执行失败中恢复，且所需模型查询次数少于始终重规划的做法。

### 结论
结果说明，将执行推理直接纳入任务规划具有明显收益。论文的项目网页提供了视频与补充材料：https://advrhumanoids.github.io/bridging-planning-execution/。

## Overview

Robots are increasingly expected to execute natural-language manipulation tasks in real-world environments. This is particularly relevant in household assistance and logistics, where clutter requires reasoning about both task objectives and execution feasibility. This challenge becomes even more pronounced for bimanual humanoid platforms, where coordinating two manipulators introduces additional interaction and kinematic constraints. We present a zero-shot vision-language framework for execution-aware bimanual manipulation that jointly reasons about task objectives and physical feasibility. Planning is grounded in a structured scene representation that combines semantic object relations with execution constraints, enabling the selection of obstacle relocations and execution choices while preserving task semantics. Compatible actions are organised into parallel bimanual stages with explicit pre- and post-conditions. A hierarchical validator evaluates these conditions under perceptual uncertainty and uses stage-level execution history to support local recovery or targeted replanning. Experiments on the CENTAURO hybrid wheeled-legged humanoid robot across nine language-conditioned manipulation scenarios show higher task success than a non-execution-aware baseline. In dedicated failure scenarios, hierarchical validation recovers from execution failures with fewer model queries than always replanning. These results demonstrate the benefits of combining execution reasoning directly into task planning. Videos and additional material are available on the Project Webpage: https://advrhumanoids.github.io/bridging-planning-execution/.

## 参考
- https://arxiv.org/abs/2611.12409
