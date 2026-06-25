---
$id: "ent_tech_robogen"
$schema: "../../data/schema/v1/entry_schema.json"
$version: 1

type: "technology"

names:
  en: "RoboGen"
  zh: "RoboGen"
  ko: "RoboGen"

summary:
  en: "An LLM-driven automatic task-generation framework for robotics that proposes tasks and generates simulation code to expand synthetic training data diversity."
  zh: "一种由大语言模型驱动的机器人自动任务生成框架，提出任务并生成仿真代码以扩展合成训练数据的多样性。"
  ko: "작업을 제안하고 시뮬레이션 코드를 생성하여 합성 학습 데이터 다양성을 확장하는 LLM 기반 로봇 자동 작업 생성 프레임워크."

domains:
  - "07_ai_models_algorithms"
  - "08_software_middleware"
  - "09_data_datasets"

layers:
  - "intelligence"

functional_roles:
  - "intelligence"
  - "tool_equipment"

tags:
  - "data_engine"
  - "llm"
  - "automatic_task_generation"
  - "simulation"
  - "synthetic_data"
  - "vla"

verification:
  status: "verified"
  reviewed_by: "human_and_ai"
  reviewed_at: "2026-06-22"
  confidence: "high"
  notes: "Scope confirmed by original NeurIPS 2023 paper and Wang et al. 2026 VLA survey."

sources:
  - id: "src_robogen_paper"
    type: "paper"
    title: "RoboGen: Towards Universal Humanoid Control via Diffusion Transformer"
    url: "https://arxiv.org/abs/2311.01455"
    date: "2023-11-02"
    accessed_at: "2026-06-22"
  - id: "src_robogen_code"
    type: "website"
    title: "RoboGen Project Page"
    url: "https://robogen-ai.github.io/"
    date: "2023-11-02"
    accessed_at: "2026-06-22"

related_entities:
  - id: "ent_paper_wang_vla_survey_2026"
    relationship: "cites"
    description:
      en: "Wang et al. 2026 survey discusses RoboGen as an LLM-driven automatic task-generation framework for simulation."
      zh: "Wang 等人 2026 综述将 RoboGen 作为由 LLM 驱动的仿真自动任务生成框架进行讨论。"
      ko: "Wang et al. 2026 서베이는 RoboGen을 LLM 기반 시뮬레이션 자동 작업 생성 프레임워크로 논의함."
---

# RoboGen

## 生活实例 + 自然语言阐述逻辑

> **生活实例**：它就像一位自动出题的 AI 教练——不再需要人类一题一题地设计训练任务，而是自己为机器人编写“作业”和对应的虚拟训练场景。

> **自然语言逻辑**：RoboGen 是一个由大语言模型驱动的机器人任务自动生成框架，能够提出任务描述、奖励函数和仿真环境代码；它旨在用低成本方式快速扩展合成训练数据的多样性，帮助机器人学习更多样的操作技能。

## Overview

RoboGen uses large language models to automatically generate diverse robotics tasks and the corresponding simulation environments. It aims to reduce the manual engineering required to create large-scale synthetic training data.

## Key Characteristics

- **LLM-driven task proposal**: generates task descriptions and reward functions.
- **Automatic scene generation**: produces simulation code and asset layouts.
- **Diversity expansion**: can create large numbers of novel tasks without human authoring.
- **Validation and filtering**: includes mechanisms to remove physically implausible or noisy generations.

## Limitations

- Generated tasks may not be physically realistic or semantically meaningful without strong filtering.
- Current demonstrations focus on arm manipulation; whole-body humanoid task generation remains under-explored.
- Sim-to-real transfer requires additional engineering.

## Relevance to Humanoid Robotics

RoboGen's automatic generation paradigm is promising for scaling humanoid task diversity, but significant work is needed to generate tasks that include bipedal locomotion, balance recovery, and contact-rich whole-body manipulation.
