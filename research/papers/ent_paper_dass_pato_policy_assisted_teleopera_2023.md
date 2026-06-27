---
$id: ent_paper_dass_pato_policy_assisted_teleopera_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PATO: Policy Assisted TeleOperation for Scalable Robot Data Collection'
  zh: PATO：面向可扩展机器人数据采集的策略辅助遥操作
  ko: 'PATO: 확장 가능한 로봇 데이터 수집을 위한 정책 보조 원격 조작'
summary:
  en: PATO is a policy-assisted teleoperation system that uses a learned hierarchical
    assistive policy to autonomously execute repetitive subtasks during demonstration
    collection and request human input only when uncertain, enabling one operator
    to control multiple robots in parallel.
  zh: PATO是一种策略辅助遥操作系统，利用学得的分层辅助策略在示范数据采集过程中自主执行重复性子任务，并仅在不确定时请求人工输入，从而使一名操作员能够并行控制多个机器人。
  ko: PATO는 학습된 계층적 보조 정책을 사용하여 시연 수집 중 반복적인 하위 작업을 자율적으로 수행하고 불확실한 경우에만 사람의 입력을 요청하는
    정책 보조 원격 조작 시스템으로, 한 명의 운영자가 여러 로봇을 병렬로 제어할 수 있게 한다.
domains:
- 09_data_datasets
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- teleoperation
- policy_assistance
- data_collection
- imitation_learning
- human_in_the_loop
- multi_robot
- assistive_policy
- robot_demonstrations
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from arXiv abstract and metadata; full-text review needed for
    section-level citations and exact component details.
sources:
- id: src_001
  type: paper
  title: 'PATO: Policy Assisted TeleOperation for Scalable Robot Data Collection'
  url: https://arxiv.org/abs/2212.04708
  date: '2023'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Policy Assisted TeleOperation (PATO) addresses the high cost and low scalability of collecting large-scale robot demonstration data. In conventional teleoperation, a single human operator must provide every action for one robot at a time, which becomes a bottleneck as data-hungrous imitation-learning and foundation-model pipelines grow. PATO automates part of the demonstration collection process by training a hierarchical assistive policy from a pre-collected dataset of human demonstrations. The high-level module predicts the next subgoal, while an ensemble of low-level policies reaches each subgoal. When the estimated policy uncertainty or task uncertainty exceeds manually tuned thresholds, PATO requests human input; otherwise it executes the subtask autonomously.

The system is evaluated in two user studies: a real-robot study with a Kinova Jaco 2 arm and a simulated fleet study in which one operator supervises multiple robots in parallel. Results show that PATO reduces operators' mental load and increases data collection throughput compared to fully manual teleoperation. The simulated fleet experiment is presented as a first step toward scalable robotic data collection, demonstrating that a single operator can oversee several robots simultaneously.

## Key Contributions

- Proposes PATO, a policy-assisted teleoperation system that automates repetitive demonstration behaviors and asks for human input only under uncertainty.
- Introduces a hierarchical assistive policy architecture with a high-level subgoal predictor and an ensemble of low-level subgoal-reaching policies.
- Develops an uncertainty-based intervention mechanism that separately estimates policy uncertainty and task uncertainty to decide when to request human input.
- Reports real-robot and simulated multi-robot user studies showing reduced mental load and improved data collection efficiency.
- Demonstrates single-operator control of multiple robots in parallel as a first step toward scalable robotic data collection.

## Relevance to Humanoid Robotics

PATO is relevant to humanoid robotics because scalable, high-quality demonstration data is a prerequisite for training general-purpose humanoid manipulation and whole-body control policies. By reducing the human effort required per robot and enabling one operator to supervise multiple platforms, PATO directly targets the data-collection bottleneck that limits the mass production and deployment of humanoid robots. The hierarchical policy and uncertainty-based intervention ideas are also applicable to high-degree-of-freedom humanoid teleoperation, where repetitive subtasks and occasional human correction are common.
