---
$id: ent_paper_swamy_scaled_autonomy_enabling_human_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Scaled Autonomy: Enabling Human Operators to Control Robot Fleets'
  zh: 可扩展自主：使人类操作员能够控制机器人群
  ko: '확장된 자율성: 인간 운영자가 로봇 함대를 제어할 수 있도록'
summary:
  en: This paper formalizes operator attention allocation as learning an internal
    scoring function under the Luce choice model, and uses the learned model to automatically
    select which robot in a large fleet most needs teleoperated intervention.
  zh: 本文将操作员注意力分配形式化为在Luce选择模型下学习内部评分函数，并利用所学模型自动选择大型机器人群中最需要遥操作干预的机器人。
  ko: 본 논문은 운영자의 주의력 배분을 Luce 선택 모델 하에서 내부 점수 함수를 학습하는 문제로 형식화하고, 학습된 모델을 사용하여 대규모
    로봇 함대에서 가장 원격 조작 개입이 필요한 로봇을 자동으로 선택한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
- 05_mass_production
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- fleet_supervision
- human_robot_interaction
- teleoperation
- preference_learning
- attention_allocation
- luce_choice_model
- shared_autonomy
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full paper not reviewed
    by human.
sources:
- id: src_001
  type: paper
  title: 'Scaled Autonomy: Enabling Human Operators to Control Robot Fleets'
  url: https://arxiv.org/abs/1910.02910
  date: '2019'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

The paper addresses the problem of scaling human supervisory attention across multiple autonomous robots. When robots act in separate environments, a single operator can teleoperate one robot at a time, but limited attention makes it hard to decide which robot most needs help as fleet size grows. The authors model the operator's choice of which robot to control as an approximately optimal decision under the Luce choice model, learning a parametric scoring function from easy, small-fleet settings. The learned scoring function is then used in larger fleets to automatically select the robot most likely to need intervention. The proposed pipeline consists of training a robot policy, learning the operator scoring model, assisting the operator's choice, and refining the robot policy with the resulting interventions.

The method is motivated by the observation that users lose the ability to evaluate all robot states as the number of robots increases. By inferring the operator's internal utility from pairwise or small-set choices, the system can rank robots by need without requiring the user to monitor every state. The paper connects this inference problem to the Luce choice model, which provides a probabilistic relationship between the utility of controlling a robot and the probability of selecting it. This formulation allows the system to generalize from small fleets, where the operator can reasonably choose, to large fleets, where the operator cannot.

## Key Contributions

- Formalizes operator attention allocation as learning an internal scoring function via the Luce choice model.
- Proposes a four-phase pipeline: train robot policy, learn scoring model, assist choice, and refine robot policy.
- Shows that modeling relative preferences between robots generalizes from small fleets to large fleets.
- Validates through simulation experiments, a 12-participant user study, and a real hardware demonstration.

## Relevance to Humanoid Robotics

The method directly supports mass-deployment scenarios in which one operator must oversee many humanoid robots acting in parallel. By automating the decision of which robot most needs human intervention, the approach can reduce operator cognitive load and increase the number of humanoids that a single supervisor can manage. Although demonstrated on mobile robots, the preference-learning framework and fleet-attention allocation principle apply to humanoid fleets in warehouses, service environments, or other large-scale deployments.

Humanoid robots are likely to face long-tail failures in unstructured environments, making teleoperation and human oversight essential. The ability to scale attention learned from small fleets to large fleets is especially relevant as humanoid platforms move from individual prototypes to deployed fleets, where one operator cannot manually watch every unit.
