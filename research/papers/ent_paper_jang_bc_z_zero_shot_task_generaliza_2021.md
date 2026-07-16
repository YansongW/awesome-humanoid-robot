---
$id: ent_paper_jang_bc_z_zero_shot_task_generaliza_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning'
  zh: BC-Z
  ko: 'BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning'
summary:
  en: 'BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning (BC-Z), is a 2021 generalized vision-language-action
    model for robotic manipulation, introduced by UC Berkeley, Stanford University, and published at CoRL 2021.'
  zh: 'BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning (BC-Z), is a 2021 generalized vision-language-action
    model for robotic manipulation, introduced by UC Berkeley, Stanford University, and published at CoRL 2021.'
  ko: 'BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning (BC-Z), is a 2021 generalized vision-language-action
    model for robotic manipulation, introduced by UC Berkeley, Stanford University, and published at CoRL 2021.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- bc_z
- generalist_policy
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: BC-Z: Zero-Shot Task Generalization
    with Robotic Imitation Learning.'
sources:
- id: src_001
  type: paper
  title: BC-Z source
  url: https://proceedings.mlr.press/v164/jang22a.html
  date: '2021'
  accessed_at: '2026-07-01'
---
## 概述
In this paper, we study the problem of enabling a vision-based robotic manipulation system to generalize to novel tasks, a long-standing challenge in robot learning. We approach the challenge from an imitation learning perspective, aiming to study how scaling and broadening the data collected can facilitate such generalization. To that end, we develop an interactive and flexible imitation learning system that can learn from both demonstrations and interventions and can be conditioned on different forms of information that convey the task, including pre-trained embeddings of natural language or videos of humans performing the task. When scaling data collection on a real robot to more than 100 distinct tasks, we find that this system can perform 24 unseen manipulation tasks with an average success rate of 44%, without any robot demonstrations for those tasks.

## 核心内容
In this paper, we study the problem of enabling a vision-based robotic manipulation system to generalize to novel tasks, a long-standing challenge in robot learning. We approach the challenge from an imitation learning perspective, aiming to study how scaling and broadening the data collected can facilitate such generalization. To that end, we develop an interactive and flexible imitation learning system that can learn from both demonstrations and interventions and can be conditioned on different forms of information that convey the task, including pre-trained embeddings of natural language or videos of humans performing the task. When scaling data collection on a real robot to more than 100 distinct tasks, we find that this system can perform 24 unseen manipulation tasks with an average success rate of 44%, without any robot demonstrations for those tasks.

## 参考
- Semantic Scholar search: BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning

## Overview
In this paper, we study the problem of enabling a vision-based robotic manipulation system to generalize to novel tasks, a long-standing challenge in robot learning. We approach the challenge from an imitation learning perspective, aiming to study how scaling and broadening the data collected can facilitate such generalization. To that end, we develop an interactive and flexible imitation learning system that can learn from both demonstrations and interventions and can be conditioned on different forms of information that convey the task, including pre-trained embeddings of natural language or videos of humans performing the task. When scaling data collection on a real robot to more than 100 distinct tasks, we find that this system can perform 24 unseen manipulation tasks with an average success rate of 44%, without any robot demonstrations for those tasks.

## Content
In this paper, we study the problem of enabling a vision-based robotic manipulation system to generalize to novel tasks, a long-standing challenge in robot learning. We approach the challenge from an imitation learning perspective, aiming to study how scaling and broadening the data collected can facilitate such generalization. To that end, we develop an interactive and flexible imitation learning system that can learn from both demonstrations and interventions and can be conditioned on different forms of information that convey the task, including pre-trained embeddings of natural language or videos of humans performing the task. When scaling data collection on a real robot to more than 100 distinct tasks, we find that this system can perform 24 unseen manipulation tasks with an average success rate of 44%, without any robot demonstrations for those tasks.

## 개요
본 논문에서는 로봇 학습의 오랜 과제인 비전 기반 로봇 조작 시스템이 새로운 작업으로 일반화할 수 있도록 하는 문제를 연구합니다. 우리는 모방 학습 관점에서 이 과제에 접근하며, 수집된 데이터의 규모 확장과 다양화가 이러한 일반화를 어떻게 촉진할 수 있는지 연구하는 것을 목표로 합니다. 이를 위해 시연과 개입 모두로부터 학습할 수 있고, 사전 학습된 자연어 임베딩이나 인간이 작업을 수행하는 비디오 등 작업을 전달하는 다양한 형태의 정보에 조건화될 수 있는 대화형이면서 유연한 모방 학습 시스템을 개발합니다. 실제 로봇에서 100개 이상의 다양한 작업으로 데이터 수집을 확장했을 때, 이 시스템은 해당 작업에 대한 로봇 시연 없이도 24개의 보지 못한 조작 작업을 평균 성공률 44%로 수행할 수 있음을 발견했습니다.

## 핵심 내용
본 논문에서는 로봇 학습의 오랜 과제인 비전 기반 로봇 조작 시스템이 새로운 작업으로 일반화할 수 있도록 하는 문제를 연구합니다. 우리는 모방 학습 관점에서 이 과제에 접근하며, 수집된 데이터의 규모 확장과 다양화가 이러한 일반화를 어떻게 촉진할 수 있는지 연구하는 것을 목표로 합니다. 이를 위해 시연과 개입 모두로부터 학습할 수 있고, 사전 학습된 자연어 임베딩이나 인간이 작업을 수행하는 비디오 등 작업을 전달하는 다양한 형태의 정보에 조건화될 수 있는 대화형이면서 유연한 모방 학습 시스템을 개발합니다. 실제 로봇에서 100개 이상의 다양한 작업으로 데이터 수집을 확장했을 때, 이 시스템은 해당 작업에 대한 로봇 시연 없이도 24개의 보지 못한 조작 작업을 평균 성공률 44%로 수행할 수 있음을 발견했습니다.
