---
$id: ent_paper_chen_llm_based_conversational_ai_kn_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: LLM-based Conversational AI Knowledge Assistant for MyBuddy Humanoid Robot
  zh: LLM-based Conversational AI Knowledge Assistant for MyBuddy Humanoid Robot
  ko: LLM-based Conversational AI Knowledge Assistant for MyBuddy Humanoid Robot
summary:
  en: Humanoid robots are increasingly being popular and developed for human-centered applications, yet their ability to provide
    intelligent conversations and natural interactive knowledge assistance remains constrained by traditional rule-based dialogue
    systems, pre-defined responses and limited knowledge repositories. Large language models (LLMs) have emerged as a powerful
    foundation for enabling ...
  zh: 本文由 Hanxiao Chen 提出并实现了一套基于 LLM 的对话式 AI 知识助手，部署在由 Raspberry Pi 驱动、具备 13 个自由度的 MyBuddy 人形机器人上。该系统将 LLM 驱动的语言理解与 AI 推理同实时语音识别、可扩展的互联网知识检索（如
    Wikipedia、arXiv）、灵活的对话管理以及自然语音合成相结合，旨在突破传统规则式对话系统、预设回复和有限知识库的局限，实现更智能的多轮连续对话与情感支持型人机交互。
  ko: Humanoid robots are increasingly being popular and developed for human-centered applications, yet their ability to provide
    intelligent conversations and natural interactive knowledge assistance remains constrained by traditional rule-based dialogue
    systems, pre-defined responses and limited knowledge repositories. Large language models (LLMs) have emerged as a powerful
    foundation for enabling ...
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
- human_robot_interaction
- large_language_models
- conversational_ai
- knowledge_retrieval
- speech_synthesis
- humanoid_robot
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-28'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-28). Bibliographic metadata from arXiv API (2609.24742);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2609.24742 LLM-based Conversational AI Knowledge Assistant for MyBuddy Humanoid Robot
  url: https://arxiv.org/abs/2609.24742
  date: '2026-09-21'
  accessed_at: '2026-09-28'
---

## 概述

人形机器人正越来越多地走向以人为中心的应用场景，但其智能对话与自然交互式知识辅助能力仍受制于传统规则式对话系统、预设回复和有限的知识库。大语言模型（LLM）为构建自然、自适应且具备上下文感知能力的人机交互（HRI）提供了强有力的基础，使机器人能够理解自然口语、对复杂查询进行推理、维持高质量的对话上下文并生成知识丰富的回复。本文面向由 Raspberry Pi 驱动、13 自由度的 MyBuddy 人形机器人，提出并实现了一套基于 LLM 的多功能对话式 AI 知识助手。该系统把 LLM 驱动的语言理解与 AI 推理，与实时语音识别、通过可扩展互联网引擎（如 Wikipedia、arXiv）进行的知识检索、灵活的对话管理以及自然语音合成整合在一起，从而支持更智能的多轮连续对话和进阶的情感支持型人机交互。

## 核心内容

### 问题背景
人形机器人日益普及并面向以人为中心的应用开发，但其提供智能对话与自然交互式知识辅助的能力，仍受限于传统规则式对话系统、预设回复以及知识库规模有限等问题。LLM 的出现为自然、自适应、上下文感知的人机交互（HRI）提供了新的基础，使机器人有机会理解自然口语、对复杂查询进行推理、保持高质量对话上下文并生成知识丰富的回复。

### 方法
作者提出并实现了一套基于 LLM 的多功能对话式 AI 知识助手，部署于 Raspberry Pi 驱动、13 自由度的 MyBuddy 人形机器人。系统整合了以下能力：
- LLM 驱动的语言理解与 AI 推理；
- 实时语音识别；
- 通过可扩展的互联网引擎（例如 Wikipedia、arXiv）进行知识检索；
- 灵活的对话管理；
- 自然语音合成。

### 目标能力
上述组件的结合使机器人能够支持更智能的多轮连续对话，以及进阶的情感支持型人机交互。

### 结论
该工作展示了以 LLM 为基础、结合实时语音与可扩展知识检索的对话式助手，可作为突破传统规则式对话与有限知识库限制的可行路径，并落地于 MyBuddy 这类资源受限的小型人形机器人平台。

## Overview

Humanoid robots are increasingly being popular and developed for human-centered applications, yet their ability to provide intelligent conversations and natural interactive knowledge assistance remains constrained by traditional rule-based dialogue systems, pre-defined responses and limited knowledge repositories. Large language models (LLMs) have emerged as a powerful foundation for enabling natural, adaptive, and context-aware Human-Robot Interaction (HRI), which provides a significant opportunity to address such limitations by enabling robots to understand natural speech language, reason over complicated queries, maintain high-quality conversational context, and generate knowledge-rich responses. In this work, we originally present and implement an LLM-based versatile Conversational AI Knowledge Assistant for the Raspberry-Pi-powered 13-Axis MyBuddy humanoid robot, which integrates LLM-driven language understanding and AI reasoning with real-time speech recognition, knowledge retrieval via extensible access of internet engines (e.g., Wikipedia, arXiv), flexible dialogue management, and natural speech synthesis to enable much more intelligent multi-turn continuous conversations and advanced emotional-support Human-Robot Interaction.

## 参考
- https://arxiv.org/abs/2609.24742
