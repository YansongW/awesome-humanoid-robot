---
$id: ent_paper_yang_robot_policy_evaluation_for_si_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective'
  zh: 面向模拟到现实迁移的机器人策略评估：基准测试视角
  ko: '시뮬레이션-현실 전이를 위한 로봇 정책 평가: 벤치마킹 관점'
summary:
  en: This paper identifies challenges and desiderata for benchmarking generalist
    robot manipulation policies, proposing a high-fidelity simulation-based evaluation
    framework that scales task complexity, applies systematic scene perturbations,
    and quantifies sim-to-real alignment through discrete and continuous metrics.
  zh: 本文识别了通用机器人操作策略基准测试中的挑战与需求，提出了一种基于高保真仿真的评估框架，通过逐步增加任务复杂度、施加系统化场景扰动，并以离散与连续指标量化模拟到现实的对齐程度。
  ko: 본 논문은 범용 로봇 조작 정책 벤치마킹의 과제와 요구사항을 도출하고, 작업 복잡도를 단계적으로 높이고 체계적인 장면 교란을 적용하며 이산/연속
    지표로 시뮬레이션-현실 정렬을 정량화하는 고충실도 시뮬레이션 기반 평가 프레임워크를 제안한다.
domains:
- 10_evaluation_benchmarks
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- sim_to_real
- benchmarking
- visual_fidelity
- policy_evaluation
- manipulation
- isaaclab
- task_taxonomy
- robustness
- simulation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the arXiv full text; requires human review before final
    verification.
sources:
- id: src_001
  type: paper
  title: 'Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective'
  url: https://arxiv.org/abs/2508.11117
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
related_entities:
- id: ent_benchmark_libero
  relationship: cites
  description:
    en: Cited as a benchmark with limited testing tasks for lifelong robot learning.
    zh: 作为有限测试任务的终身机器人学习基准被引用。
    ko: 제한된 테스트 작업을 다루는 평생 로봇 학습 벤치마크로 인용됨.
---

## Overview

Current vision-based robotics simulation benchmarks have advanced manipulation research, yet evaluation that targets real-world deployment of generalist policies remains underdeveloped. The paper argues that robotics is fundamentally a real-world problem and that the absence of standardized, scalable sim-to-real benchmarks is a critical bottleneck for visual robotic policies. It reviews four challenge areas: the sim-to-real gap (contact physics, visual appearance, dynamics), the need for language-annotated tasks, the lack of a unified platform with consistent task definitions and action spaces, and the difficulty of achieving relevant scale and scope in data and tasks.

To address these gaps, the authors propose a benchmarking framework built on high visual-fidelity simulation. The framework defines a four-level task taxonomy, a suite of systematic environment perturbations, and a granular set of discrete and continuous metrics. It also introduces sim-to-real transfer metrics designed to quantify how well simulation performance predicts real-world performance. The intended workflow procedurally generates tasks and perturbations, evaluates policies across the taxonomy, and compares sim and real results to identify failure modes and domain gaps.

The paper outlines an initial implementation using IsaacLab as the simulation backbone and positions the framework as a scalable reference pipeline for the research community. Real-world experiments are planned to complement simulation evaluations, but are not yet reported.

## Key Contributions

- Identify key challenges and desiderata for sim-to-real robot manipulation benchmarking.
- Introduce a four-level task taxonomy for systematic complexity scaling (single-motion, continuous-motion, multi-step, and long-horizon tasks with memory).
- Define environment perturbation categories (object placement, number of objects, texture, lighting, camera pose) and granular discrete/continuous evaluation metrics.
- Propose sim-to-real transfer metrics to quantify simulation-to-real-world alignment, including success matching, trajectory divergence, and expected real-world success rate.
- Outline an IsaacLab-based scalable benchmarking pipeline intended as a community reference.

## Relevance to Humanoid Robotics

Humanoid robots are expected to operate as generalist manipulators in unstructured, real-world industrial and service environments, where reliable sim-to-real transfer is essential. The paper's emphasis on standardized task definitions, robustness to visual and scene perturbations, failure-mode diagnosis, and sim-to-real alignment directly addresses the validation gap that slows deployment of humanoid manipulation policies.

Because real-world data collection on full humanoids is expensive and hard to scale, a high-fidelity simulation benchmark that can proxy real-world evaluation offers a practical path toward reproducible, community-wide progress. The framework's metrics and taxonomy can be adapted to humanoid embodiments as action-space heterogeneity is resolved, making it a relevant methodological reference for humanoid-robot evaluation.
