---
$id: ent_paper_team_gemini_robotics_15_pushing_the_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced
    Embodied Reasoning, Thinking, and Motion Transfer'
  zh: Gemini Robotics 1.5：以高级具身推理、思考和动作迁移推动通才机器人前沿
  ko: 'Gemini Robotics 1.5: 고급 구체화 추론, 사고 및 동작 전이를 통한 범용 로봇의 최전선 확장'
summary:
  en: Gemini Robotics 1.5 introduces a multi-embodiment Vision-Language-Action model
    with Motion Transfer and a Thinking VLA that interleaves actions with natural-language
    reasoning, alongside Gemini Robotics-ER 1.5, an embodied reasoning model for spatial
    understanding and task planning.
  zh: Gemini Robotics 1.5 提出了一个具备动作迁移能力的多本体视觉-语言-动作模型，以及将动作与自然语言推理交织的 Thinking VLA，并配套
    Gemini Robotics-ER 1.5 具身推理模型用于空间理解与任务规划。
  ko: Gemini Robotics 1.5는 동작 전이를 갖춘 다중 구체화 비전-언어-행동 모델과 자연어 추론과 행동을 교차하는 Thinking
    VLA를 소개하며, 공간 이해와 작업 계획을 위한 Gemini Robotics-ER 1.5 구체화 추론 모델을 함께 제시한다.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
- 08_software_middleware
layers:
- intelligence
functional_roles:
- intelligence
- knowledge
tags:
- vla
- vision_language_action
- embodied_reasoning
- motion_transfer
- multi_embodiment
- humanoid_robot
- apptronik_apollo
- thinking_vla
- foundation_model
- robot_learning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review against
    the full arXiv paper before final verification.
sources:
- id: src_001
  type: paper
  title: 'Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced
    Embodied Reasoning, Thinking, and Motion Transfer'
  url: https://arxiv.org/abs/2510.03342
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Gemini Robotics 1.5 is the latest generation of the Gemini Robotics model family developed by Google DeepMind. It consists of two complementary models: Gemini Robotics 1.5, a multi-embodiment Vision-Language-Action (VLA) model, and Gemini Robotics-ER 1.5, an embodied reasoning (ER) model. The VLA introduces Motion Transfer (MT), a mechanism that enables pre-training on heterogeneous, multi-embodiment robot data and supports zero-shot skill transfer across robot platforms, including the Apptronik Apollo humanoid. The model also incorporates a "Thinking VLA" design that interleaves low-level actions with multi-level internal natural-language reasoning, allowing the robot to "think before acting" and improving interpretability and multi-step task execution.

Gemini Robotics-ER 1.5 advances embodied reasoning capabilities such as visual and spatial understanding, task planning, and progress estimation, achieving state-of-the-art results on multiple benchmarks. The two models are integrated into an agentic framework that combines perception, reasoning, and action for long-horizon tasks, tool use, planning, and safety reasoning. The report also presents safety and alignment contributions, including the ASIMOV-2.0 benchmark and an Auto-Red-Teaming framework.

## Key Contributions

- Novel VLA architecture with Motion Transfer enabling multi-embodiment pre-training and zero-shot skill transfer across robots.
- Thinking VLA that interleaves actions with multi-level natural-language reasoning to improve multi-step task decomposition and interpretability.
- Gemini Robotics-ER 1.5 sets a new state-of-the-art across embodied reasoning benchmarks.
- Agentic framework combining ER and VLA for long-horizon tasks with tool use, planning, and safety reasoning.
- Safety and alignment advances including the ASIMOV-2.0 benchmark and Auto-Red-Teaming framework.

## Relevance to Humanoid Robotics

Gemini Robotics 1.5 is directly relevant to humanoid robotics because it demonstrates zero-shot control of the Apptronik Apollo humanoid and cross-embodiment skill transfer into humanoid platforms. The Motion Transfer mechanism addresses a central challenge in scalable humanoid deployment: the ability to learn from diverse robot datasets and transfer skills across embodiments without per-robot retraining. By combining low-level action generation with high-level embodied reasoning in an agentic system, the work advances generalist robot foundation models that can support scalable humanoid mass production and deployment in unstructured environments.
