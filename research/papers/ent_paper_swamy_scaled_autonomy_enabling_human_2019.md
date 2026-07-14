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
  en: This paper formalizes operator attention allocation as learning an internal scoring function under the Luce choice model,
    and uses the learned model to automatically select which robot in a large fleet most needs teleoperated intervention.
  zh: 本文将操作员注意力分配形式化为在Luce选择模型下学习内部评分函数，并利用所学模型自动选择大型机器人群中最需要遥操作干预的机器人。
  ko: 본 논문은 운영자의 주의력 배분을 Luce 선택 모델 하에서 내부 점수 함수를 학습하는 문제로 형식화하고, 학습된 모델을 사용하여 대규모 로봇 함대에서 가장 원격 조작 개입이 필요한 로봇을 자동으로 선택한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1910.02910v2.
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
## 概述
Autonomous robots often encounter challenging situations where their control policies fail and an expert human operator must briefly intervene, e.g., through teleoperation. In settings where multiple robots act in separate environments, a single human operator can manage a fleet of robots by identifying and teleoperating one robot at any given time. The key challenge is that users have limited attention: as the number of robots increases, users lose the ability to decide which robot requires teleoperation the most. Our goal is to automate this decision, thereby enabling users to supervise more robots than their attention would normally allow for. Our insight is that we can model the user's choice of which robot to control as an approximately optimal decision that maximizes the user's utility function. We learn a model of the user's preferences from observations of the user's choices in easy settings with a few robots, and use it in challenging settings with more robots to automatically identify which robot the user would most likely choose to control, if they were able to evaluate the states of all robots at all times. We run simulation experiments and a user study with twelve participants that show our method can be used to assist users in performing a simulated navigation task. We also run a hardware demonstration that illustrates how our method can be applied to a real-world mobile robot navigation task.

## 核心内容
Autonomous robots often encounter challenging situations where their control policies fail and an expert human operator must briefly intervene, e.g., through teleoperation. In settings where multiple robots act in separate environments, a single human operator can manage a fleet of robots by identifying and teleoperating one robot at any given time. The key challenge is that users have limited attention: as the number of robots increases, users lose the ability to decide which robot requires teleoperation the most. Our goal is to automate this decision, thereby enabling users to supervise more robots than their attention would normally allow for. Our insight is that we can model the user's choice of which robot to control as an approximately optimal decision that maximizes the user's utility function. We learn a model of the user's preferences from observations of the user's choices in easy settings with a few robots, and use it in challenging settings with more robots to automatically identify which robot the user would most likely choose to control, if they were able to evaluate the states of all robots at all times. We run simulation experiments and a user study with twelve participants that show our method can be used to assist users in performing a simulated navigation task. We also run a hardware demonstration that illustrates how our method can be applied to a real-world mobile robot navigation task.

## 参考
- http://arxiv.org/abs/1910.02910v2

