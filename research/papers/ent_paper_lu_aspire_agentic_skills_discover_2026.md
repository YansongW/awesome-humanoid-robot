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
  en: ASPIRE is a self-improving continual learning system for robotics that autonomously
    writes and refines code-as-policy robot control programs from execution feedback.
    It combines a closed-loop robot execution engine that exposes fine-grained multimodal
    traces, a continually expanding skill library of validated repairs, and an evolutionary
    search procedure that explores diverse programs beyond single-trajectory refinement.
    Across manipulation, bimanual handover, and long-horizon household benchmarks,
    ASPIRE outperforms prior VLA and coding-agent baselines by large margins and shows
    initial sim-to-real transfer across embodiments.
  zh: ASPIRE 是一个面向机器人的自改进持续学习系统，能够根据执行反馈自动编写并迭代优化 code-as-policy 机器人控制程序。它由三部分组成：暴露细粒度多模态追踪的闭环机器人执行引擎、不断积累可复用修复策略的技能库，以及超越单轨迹优化的进化搜索过程。在操作、双手交接和长程家庭任务基准上，ASPIRE
    显著优于现有 VLA 和 coding-agent 基线，并展现了跨本体的初步 sim-to-real 迁移能力。
  ko: ASPIRE is a self-improving continual learning system for robotics that autonomously
    writes and refines code-as-policy robot control programs from execution feedback.
    It combines a closed-loop robot execution engine that exposes fine-grained multimodal
    traces, a continually expanding skill library of validated repairs, and an evolutionary
    search procedure that explores diverse programs beyond single-trajectory refinement.
    Across manipulation, bimanual handover, and long-horizon household benchmarks,
    ASPIRE outperforms prior VLA and coding-agent baselines by large margins and shows
    initial sim-to-real transfer across embodiments.
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
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: Imported from NVIDIA GEAR project page; no arXiv ID available yet.
sources:
- id: src_001
  type: website
  title: 'ASPIRE: Agentic Skills Discovery for Robotics (NVIDIA GEAR)'
  url: https://research.nvidia.com/labs/gear/aspire/
  date: '2026'
  accessed_at: '2026-07-01'
---

## 概述
ASPIRE 是一个面向机器人的自改进持续学习系统，能够根据执行反馈自动编写并迭代优化 code-as-policy 机器人控制程序。它由三部分组成：暴露细粒度多模态追踪的闭环机器人执行引擎、不断积累可复用修复策略的技能库，以及超越单轨迹优化的进化搜索过程。在操作、双手交接和长程家庭任务基准上，ASPIRE 显著优于现有 VLA 和 coding-agent 基线，并展现了跨本体的初步 sim-to-real 迁移能力。

## Overview
ASPIRE is a self-improving continual learning system for robotics that autonomously writes and refines code-as-policy robot control programs from execution feedback. It combines a closed-loop robot execution engine that exposes fine-grained multimodal traces, a continually expanding skill library of validated repairs, and an evolutionary search procedure that explores diverse programs beyond single-trajectory refinement. Across manipulation, bimanual handover, and long-horizon household benchmarks, ASPIRE outperforms prior VLA and coding-agent baselines by large margins and shows initial sim-to-real transfer across embodiments.

## 개요
ASPIRE is a self-improving continual learning system for robotics that autonomously writes and refines code-as-policy robot control programs from execution feedback. It combines a closed-loop robot execution engine that exposes fine-grained multimodal traces, a continually expanding skill library of validated repairs, and an evolutionary search procedure that explores diverse programs beyond single-trajectory refinement. Across manipulation, bimanual handover, and long-horizon household benchmarks, ASPIRE outperforms prior VLA and coding-agent baselines by large margins and shows initial sim-to-real transfer across embodiments.
