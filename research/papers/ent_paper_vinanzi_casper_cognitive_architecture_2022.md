---
$id: ent_paper_vinanzi_casper_cognitive_architecture_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CASPER: Cognitive Architecture for Social Perception and Engagement in Robots'
  zh: CASPER：面向机器人社会感知与参与的认知架构
  ko: 'CASPER: 로봇의 사회적 지각 및 참여를 위한 인지 아키텍처'
summary:
  en: CASPER is a symbolic cognitive architecture that uses Qualitative Spatial Relations
    to recognize low-level movements, infer high-level goals, and generate collaborative
    assistive plans for social robots. The authors evaluate it in a Webots kitchen
    simulation with a TIAGo++ robot, showing that the robot can anticipate a human
    partner's goal and contribute to the task.
  zh: CASPER是一个符号化认知架构，利用定性空间关系识别低层动作、推断高层目标，并为社交机器人生成协作辅助计划。作者在Webots厨房仿真环境中使用TIAGo++机器人进行评估，结果表明机器人能够预测人类伙伴的目标并协助完成任务。
  ko: CASPER는 정성적 공간 관계(QSR)를 사용하여 저수준 동작을 인식하고, 고수준 목표를 추론하며, 사회적 로봇을 위한 협력 보조 계획을
    생성하는 기호적 인지 아키텍처이다. 저자들은 Webots 주방 시뮬레이션에서 TIAGo++ 로봇으로 이를 평가하여, 로봇이 인간 파트너의 목표를
    예측하고 작업에 기여할 수 있음을 보였다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- intelligence
- system
- knowledge
tags:
- casper
- cognitive_architecture
- intention_reading
- qualitative_spatial_reasoning
- qsr
- human_robot_collaboration
- social_perception
- symbolic_reasoning
- plan_recognition
- owl_ontology
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from full text of the arXiv preprint; requires human review
    before verification.
sources:
- id: src_001
  type: paper
  title: 'CASPER: Cognitive Architecture for Social Perception and Engagement in Robots'
  url: https://arxiv.org/abs/2209.01012
  date: '2022'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

CASPER is presented as a platform-independent, symbolic cognitive architecture for human-robot collaboration. It combines a perception module, a low-level action-recognition pipeline, a high-level goal-inference component, a knowledge-based verification module, and a supervisor that generates collaborative robot behavior. The perception module computes Qualitative Spatial Relations (QSRs) between an observed agent and Objects of Interest (OOIs) using QSRlib, producing descriptors such as Qualitative Distance Calculus, Qualitative Trajectory Calculus, Moving-or-Stationary, and Holding-Object. The low-level module recognizes movements via a decision tree and temporally sequences them into actions using Markov-chain finite-state machines. The high-level module matches observed actions against a hand-authored plan library to infer the partner's goal using a scoring function based on observed and missed nodes. An OWL2 ontology checked by a Pellet reasoner filters invalid predictions and supports collaborative decision-making.

The authors evaluate CASPER in a simulated kitchen containing seven OOIs and a TIAGo++ robot. Three goals—Breakfast, Drink, and Lunch—are encoded as hierarchical plans. The robot observes the simulated human, predicts the ongoing goal before task completion, and selects a sequence of remaining actions it can perform to help. Results show correct goal recognition and appropriate collaborative responses. The system currently relies on manually engineered symbolic knowledge, including OOIs, plans, and the ontology, and the evaluation is limited to this single simulated scenario.

## Key Contributions

- A new cognitive architecture integrating intention reading and collaborative behavior generation for human-robot interaction.
- Novel application of Qualitative Spatial Relations to intention reading in embodied robots.
- Collection of psychologically inspired algorithms for social perception and reasoning, including a focus estimator, decision-tree movement classifier, Markov-chain finite-state machine action predictor, and plan-library goal scorer.
- First case study demonstrating CASPER in a simulated collaborative kitchen task with a TIAGo++ robot.

## Relevance to Humanoid Robotics

CASPER addresses core cognitive capabilities—intention reading, goal prediction, and collaborative planning—that are essential for deploying humanoid robots as autonomous, assistive partners in everyday human environments. Although the reported experiment uses the wheeled TIAGo++ manipulator, the architecture is described as platform-independent and the ontology explicitly allows the robot agent class to be expanded with several kinds of robots, including humanoid and non-humanoid categories. The symbolic, QSR-based approach is intended to generalize across agent morphologies, supporting future heterogeneous multi-agent teams where humanoids and other robots collaborate with humans.
