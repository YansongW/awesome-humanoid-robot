---
$id: "ent_paper_aljalbout_reality_gap_2025"
$schema: "../../../../../data/schema/v1/entry_schema.json"
$version: 1

type: "paper"

names:
  en: "The Reality Gap in Robotics: Challenges, Solutions, and Best Practices"
  zh: "机器人中的现实鸿沟：挑战、解决方案与最佳实践"
  ko: "로보틱스의 현실 격차: 과제, 해결책 및 모범 사례"

summary:
  en: "A 2025 survey that maps the sim-to-real reality gap into perception and action-dynamics discrepancies, and reviews mitigation strategies including domain randomization, system identification, and sim-real co-training."
  zh: "2025 年综述，将仿真到现实的现实鸿沟划分为感知差异与动作动力学差异，并综述了域随机化、系统辨识和仿真-现实协同训练等缓解策略。"
  ko: "2025년 서베이로, 시뮬레이션-현실 간 현실 격차를 지각 및 동작 역학 불일치로 분류하고 도메인 랜덤화, 시스템 식별, 시뮬-현실 공동 학습 등 완화 전략을 검토함."

domains:
  - "07_ai_models_algorithms"
  - "02_components"
  - "08_software_middleware"

layers:
  - "intelligence"
  - "midstream"

functional_roles:
  - "knowledge"
  - "intelligence"

tags:
  - "sim_to_real"
  - "reality_gap"
  - "survey"
  - "domain_randomization"
  - "system_identification"
  - "physics_simulation"

verification:
  status: "partially_verified"
  reviewed_by: "ai"
  reviewed_at: "2026-06-25"
  confidence: "medium"
  notes: "AI-extracted from arXiv abstract and HTML preview; full-paper review pending."

sources:
  - id: "src_paper_aljalbout_reality_gap_2025"
    type: "paper"
    title: "The Reality Gap in Robotics: Challenges, Solutions, and Best Practices"
    url: "https://arxiv.org/abs/2510.20808"
    date: "2025-10-23"
    accessed_at: "2026-06-25"
---

# The Reality Gap in Robotics: Challenges, Solutions, and Best Practices

## 生活实例 + 自然语言阐述逻辑

> **生活实例**：它就像飞行模拟器与真实驾驶之间的差距——模拟里你能完美降落，但真机上风切变、仪表延迟、轮胎摩擦都会让同样操作出问题。

> **自然语言逻辑**：这篇 2025 年综述系统梳理了机器人从仿真到现实部署之间的“现实鸿沟”，将其分为感知差异和动作动力学差异；它回顾了域随机化、系统辨识、仿真-现实协同训练等缓解方法，帮助人形机器人开发者理解为什么仿真里好用的策略到了真机上可能失效。

## Overview

This survey (Aljalbout et al., 2025) provides a structured taxonomy of the "reality gap" between physics simulators and real-world robot deployment. It groups discrepancies into **perception gaps** (sensor noise, lighting, rendering, calibration) and **action-dynamics gaps** (contact friction, actuator latency, deformable objects, controller timing), then reviews mitigation approaches and evaluation metrics.

## Key Themes

- **Causes**: abstractions and approximations in physics engines, simplified sensor models, and unmodeled hardware dynamics.
- **Solutions**: calibration and explicit modeling, domain randomization, domain adaptation, residual learning, real-to-sim transfer, and sim-real co-training.
- **Evaluation**: metrics that correlate simulated and real-world performance, increasingly using learned world models and physics-aware digital cousins.

## Relevance to Humanoid Robotics

Humanoids amplify the reality gap because whole-body control involves high-DoF contact dynamics, balance, and morphological diversity. The survey's framing is directly relevant to co-designing simulators, actuators, and learning algorithms for humanoid platforms.
