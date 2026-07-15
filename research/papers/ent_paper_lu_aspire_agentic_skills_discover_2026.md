---
$id: ent_paper_lu_aspire_agentic_skills_discover_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ASPIRE: Agentic Skills Discovery for Robotics'
  zh: ASPIRE：面向机器人的自主技能发现
  ko: 'ASPIRE: Agentic Skills Discovery for Robotics'
summary:
  en: ASPIRE is a self-improving continual learning system for robotics that autonomously writes and refines code-as-policy
    robot control programs from execution feedback. It combines a closed-loop robot execution engine that exposes fine-grained
    multimodal traces, a continually expanding skill library of validated repairs, and an evolutionary search procedure that
    explores diverse programs beyond single-trajectory refinement. Across manipulation, bimanual handover, and long-horizon
    household benchmarks, ASPIRE outperforms prior VLA and coding-agent baselines by large margins and shows initial sim-to-real
    transfer across embodiments.
  zh: ASPIRE 是一个面向机器人的自改进持续学习系统，能够根据执行反馈自动编写并迭代优化 code-as-policy 机器人控制程序。它由三部分组成：暴露细粒度多模态追踪的闭环机器人执行引擎、不断积累可复用修复策略的技能库，以及超越单轨迹优化的进化搜索过程。在操作、双手交接和长程家庭任务基准上，ASPIRE
    显著优于现有 VLA 和 coding-agent 基线，并展现了跨本体的初步 sim-to-real 迁移能力。
  ko: ASPIRE is a self-improving continual learning system for robotics that autonomously writes and refines code-as-policy
    robot control programs from execution feedback. It combines a closed-loop robot execution engine that exposes fine-grained
    multimodal traces, a continually expanding skill library of validated repairs, and an evolutionary search procedure that
    explores diverse programs beyond single-trajectory refinement. Across manipulation, bimanual handover, and long-horizon
    household benchmarks, ASPIRE outperforms prior VLA and coding-agent baselines by large margins and shows initial sim-to-real
    transfer across embodiments.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- robotics
- agentic
- skill_discovery
- code_as_policy
- continual_learning
- sim_to_real
- nvidia
- gear
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.00272v1.
sources:
- id: src_001
  type: website
  title: 'ASPIRE: Agentic Skills Discovery for Robotics (NVIDIA GEAR)'
  url: https://research.nvidia.com/labs/gear/aspire/
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Traditional robot programming is challenging: it requires orchestrating multimodal perception, managing physical contact dynamics, and handling diverse configurations and execution failures. We introduce ASPIRE (Agentic Skill Programming through Iterative Robot Exploration), a continual learning system that autonomously writes and refines robot control programs in a code-as-policy paradigm while compounding experience into a reusable skill library. ASPIRE discovers skills that persist across tasks, simulation and real-world settings, and embodiments. It operates in an open-ended loop with three components: (1) a closed-loop robot execution engine that exposes fine-grained multimodal traces, enabling autonomous failure diagnosis, repair synthesis, and validation; (2) a continually expanding skill library that distills validated fixes into reusable, transferable knowledge; and (3) evolutionary search that generates diverse task sequences and control programs to explore beyond single-trajectory refinement. ASPIRE surpasses prior methods by up to 77% on LIBERO-Pro manipulation under perturbation, 72% on Robosuite bimanual handover, and 32% on BEHAVIOR-1K long-horizon household tasks. Its accumulated library also enables zero-shot generalization to unseen long-horizon tasks: on LIBERO-Pro Long, ASPIRE achieves 31% success versus 4% for prior methods despite their use of test-time reasoning and retries. Finally, simulation-discovered skills provide initial evidence of sim-to-real transfer, substantially reducing real-robot programming effort across different embodiments and robot APIs.

## 核心内容
Traditional robot programming is challenging: it requires orchestrating multimodal perception, managing physical contact dynamics, and handling diverse configurations and execution failures. We introduce ASPIRE (Agentic Skill Programming through Iterative Robot Exploration), a continual learning system that autonomously writes and refines robot control programs in a code-as-policy paradigm while compounding experience into a reusable skill library. ASPIRE discovers skills that persist across tasks, simulation and real-world settings, and embodiments. It operates in an open-ended loop with three components: (1) a closed-loop robot execution engine that exposes fine-grained multimodal traces, enabling autonomous failure diagnosis, repair synthesis, and validation; (2) a continually expanding skill library that distills validated fixes into reusable, transferable knowledge; and (3) evolutionary search that generates diverse task sequences and control programs to explore beyond single-trajectory refinement. ASPIRE surpasses prior methods by up to 77% on LIBERO-Pro manipulation under perturbation, 72% on Robosuite bimanual handover, and 32% on BEHAVIOR-1K long-horizon household tasks. Its accumulated library also enables zero-shot generalization to unseen long-horizon tasks: on LIBERO-Pro Long, ASPIRE achieves 31% success versus 4% for prior methods despite their use of test-time reasoning and retries. Finally, simulation-discovered skills provide initial evidence of sim-to-real transfer, substantially reducing real-robot programming effort across different embodiments and robot APIs.

## 参考
- http://arxiv.org/abs/2607.00272v1

