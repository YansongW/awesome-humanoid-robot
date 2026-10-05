---
$id: ent_paper_lin_interevolve_test_time_evolutio_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'InterEvolve: Test-Time Evolution of Reward Programs for Humanoid Loco-Manipulation'
  zh: 'InterEvolve: Test-Time Evolution of Reward Programs for Humanoid Loco-Manipulation'
  ko: 'InterEvolve: Test-Time Evolution of Reward Programs for Humanoid Loco-Manipulation'
summary:
  en: 'We study test-time evolution for humanoid loco-manipulation: solving tasks that a controller was never trained for
    by repurposing its existing skills, improving from its own attempts, and retaining what it learns, without retraining.
    Our key insight is that a broad controller already holds much of the competence a new task needs, and that this competence
    becomes accessible through an interface ...'
  zh: InterEvolve 是一种面向人形机器人 loco-manipulation 的测试时演化方法，由 Zhuo Lin、Sirui Xu、Liuyu Bian、Yu-Xiong Wang、Liang-Yan Gui 提出。它通过一个物体感知的前向-后向（FB）行为基础模型与由
    LLM 智能体修改、数值优化器调参的奖励程序，让控制器在不重新训练的情况下复用已有技能解决新任务。实验表明该方法能释放 FB 模型未被人工奖励触及的 loco-manipulation 能力，并在仿真与 Unitree G1 实机上产生多样、长时序的行为。
  ko: 'We study test-time evolution for humanoid loco-manipulation: solving tasks that a controller was never trained for
    by repurposing its existing skills, improving from its own attempts, and retaining what it learns, without retraining.
    Our key insight is that a broad controller already holds much of the competence a new task needs, and that this competence
    becomes accessible through an interface ...'
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
- humanoid_loco_manipulation
- test_time_evolution
- reward_program
- behavioral_foundation_model
- llm_agent
- sim_to_real
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-05'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-05). Bibliographic metadata from arXiv API (2610.02196);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.02196 InterEvolve: Test-Time Evolution of Reward Programs for Humanoid Loco-Manipulation'
  url: https://arxiv.org/abs/2610.02196
  date: '2026-10-01'
  accessed_at: '2026-10-05'
- id: src_002
  type: website
  title: Project page
  url: https://sirui-xu.github.io/InterEvolve
  accessed_at: '2026-10-05'
---

## 概述

InterEvolve 关注的是人形机器人 loco-manipulation 的测试时演化问题：让控制器在不重新训练的前提下，通过复用已有技能、从自身尝试中改进并保留所学，来完成从未训练过的任务。其核心思路是，一个能力广泛的控制器本身已具备新任务所需的大部分能力，关键在于规划与控制之间需要一个既能表达接触丰富、多阶段交互，又可执行、可度量的接口。为此作者构建了物体感知的前向-后向（FB）行为基础模型，在冻结的身体先验上加入物体残差，从而在测试时把关于身体或物体的新奖励转化为 loco-manipulation 行为。任务被写成奖励程序，即带完成条件和可调常数的分阶段奖励，由 LLM 智能体依据执行反馈与已验证程序构成的技能库修改程序结构，数值优化器负责调常数。每个候选程序都在并行仿真场景中验证，使程序在迭代中不断探索如何诱导、复用与组合控制器已有的运动能力。

## 核心内容

### 问题背景
论文研究人形机器人 loco-manipulation 的测试时演化：控制器需要完成它从未被训练过的任务，且不能重新训练。作者的关键洞察是，一个能力广泛的控制器已经掌握了新任务所需的大部分能力，但这些能力能否被调用，取决于规划与控制之间的接口是否足够表达接触丰富、多阶段的交互，同时又足够可执行、可度量，以便执行反馈能反过来指导规划。

### 方法
InterEvolve 用两个组件实现这一接口：

- **物体感知的前向-后向（FB）行为基础模型**：在冻结的身体先验上引入物体残差，从而在测试时把关于身体或物体的新奖励转化为 loco-manipulation 行为。
- **奖励程序**：任务被表示为分阶段奖励，包含完成条件与可调常数。LLM 智能体在上下文中修改程序结构，依据的是执行反馈以及一个由已验证程序构成的技能库；数值优化器则负责调节程序中的常数。

每个候选程序都会在并行的仿真场景中接受验证，因此程序能够探索新的方式来诱导、复用和组合控制器已有的运动能力，并在迭代中不断改进。

### 实验与关键结果
- 实验显示，人工设计的奖励未能充分挖掘 FB 模型的 loco-manipulation 能力，而 InterEvolve 演化出的程序能够释放这些能力，有时还通过新颖策略实现。
- 该方法在仿真中为多样任务、复杂场景以及长时序组合生成了行为。
- 演化得到的技能能够在物理 Unitree G1 上，基于以自我为中心的车载感知自主运行。

### 结论
通过将规划与控制之间的接口形式化为可演化的奖励程序，并借助 LLM 智能体与数值优化器在测试时迭代改进，InterEvolve 无需重新训练即可释放控制器已有的 loco-manipulation 能力，并支持从仿真到 Unitree G1 实机的自主执行。

## Overview

We study test-time evolution for humanoid loco-manipulation: solving tasks that a controller was never trained for by repurposing its existing skills, improving from its own attempts, and retaining what it learns, without retraining. Our key insight is that a broad controller already holds much of the competence a new task needs, and that this competence becomes accessible through an interface between planning and control that is expressive enough to specify contact-rich, multi-stage interactions, yet executable and measurable enough that execution feedback can guide planning from experience. InterEvolve realizes this interface with two components. First, we develop an object-aware forward-backward (FB) behavioral foundation model, whose object residuals on a frozen body prior turn a new reward about the body or objects into loco-manipulation behavior at test time. Second, we specify tasks as reward programs: staged rewards with completion conditions and tunable constants. A large language model (LLM) agent revises the program structure in context, drawing on execution feedback and a skill library of verified programs, while a numerical optimizer tunes its constants. With every candidate verified across parallel simulation scenarios, the program explores new ways to induce, repurpose, and compose the controller's existing motor competence for the task at hand, and thus improves over iterations. Experiments show that human-designed rewards leave much of the FB model's loco-manipulation competence untapped, whereas the programs InterEvolve evolves release it, sometimes through novel strategies. It further produces behaviors for diverse tasks, complex scenes, and long-horizon compositions in simulation, and evolved skills run autonomously on a physical Unitree G1 from egocentric onboard perception.

## 参考
- https://arxiv.org/abs/2610.02196
- https://sirui-xu.github.io/InterEvolve
