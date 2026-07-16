---
$id: ent_paper_shridhar_perceiver_actor_a_multi_task_t_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation'
  zh: PerAct
  ko: 'Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation'
summary:
  en: 'Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation (PerAct), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by University of Washington, NVIDIA, and published at CoRL 2022.'
  zh: 'Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation (PerAct), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by University of Washington, NVIDIA, and published at CoRL 2022.'
  ko: 'Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation (PerAct), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by University of Washington, NVIDIA, and published at CoRL 2022.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- peract
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2209.05451v2.
sources:
- id: src_001
  type: paper
  title: PerAct source
  url: https://proceedings.mlr.press/v205/shridhar23a.html
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
Transformers have revolutionized vision and natural language processing with their ability to scale with large datasets. But in robotic manipulation, data is both limited and expensive. Can manipulation still benefit from Transformers with the right problem formulation? We investigate this question with PerAct, a language-conditioned behavior-cloning agent for multi-task 6-DoF manipulation. PerAct encodes language goals and RGB-D voxel observations with a Perceiver Transformer, and outputs discretized actions by ``detecting the next best voxel action''. Unlike frameworks that operate on 2D images, the voxelized 3D observation and action space provides a strong structural prior for efficiently learning 6-DoF actions. With this formulation, we train a single multi-task Transformer for 18 RLBench tasks (with 249 variations) and 7 real-world tasks (with 18 variations) from just a few demonstrations per task. Our results show that PerAct significantly outperforms unstructured image-to-action agents and 3D ConvNet baselines for a wide range of tabletop tasks.

## 核心内容
Transformers have revolutionized vision and natural language processing with their ability to scale with large datasets. But in robotic manipulation, data is both limited and expensive. Can manipulation still benefit from Transformers with the right problem formulation? We investigate this question with PerAct, a language-conditioned behavior-cloning agent for multi-task 6-DoF manipulation. PerAct encodes language goals and RGB-D voxel observations with a Perceiver Transformer, and outputs discretized actions by ``detecting the next best voxel action''. Unlike frameworks that operate on 2D images, the voxelized 3D observation and action space provides a strong structural prior for efficiently learning 6-DoF actions. With this formulation, we train a single multi-task Transformer for 18 RLBench tasks (with 249 variations) and 7 real-world tasks (with 18 variations) from just a few demonstrations per task. Our results show that PerAct significantly outperforms unstructured image-to-action agents and 3D ConvNet baselines for a wide range of tabletop tasks.

## 参考
- http://arxiv.org/abs/2209.05451v2

## Overview
Transformers have revolutionized vision and natural language processing with their ability to scale with large datasets. But in robotic manipulation, data is both limited and expensive. Can manipulation still benefit from Transformers with the right problem formulation? We investigate this question with PerAct, a language-conditioned behavior-cloning agent for multi-task 6-DoF manipulation. PerAct encodes language goals and RGB-D voxel observations with a Perceiver Transformer, and outputs discretized actions by "detecting the next best voxel action". Unlike frameworks that operate on 2D images, the voxelized 3D observation and action space provides a strong structural prior for efficiently learning 6-DoF actions. With this formulation, we train a single multi-task Transformer for 18 RLBench tasks (with 249 variations) and 7 real-world tasks (with 18 variations) from just a few demonstrations per task. Our results show that PerAct significantly outperforms unstructured image-to-action agents and 3D ConvNet baselines for a wide range of tabletop tasks.

## Content
Transformers have revolutionized vision and natural language processing with their ability to scale with large datasets. But in robotic manipulation, data is both limited and expensive. Can manipulation still benefit from Transformers with the right problem formulation? We investigate this question with PerAct, a language-conditioned behavior-cloning agent for multi-task 6-DoF manipulation. PerAct encodes language goals and RGB-D voxel observations with a Perceiver Transformer, and outputs discretized actions by "detecting the next best voxel action". Unlike frameworks that operate on 2D images, the voxelized 3D observation and action space provides a strong structural prior for efficiently learning 6-DoF actions. With this formulation, we train a single multi-task Transformer for 18 RLBench tasks (with 249 variations) and 7 real-world tasks (with 18 variations) from just a few demonstrations per task. Our results show that PerAct significantly outperforms unstructured image-to-action agents and 3D ConvNet baselines for a wide range of tabletop tasks.

## 개요
Transformer는 대규모 데이터셋으로 확장 가능한 능력을 통해 비전 및 자연어 처리 분야에 혁신을 가져왔습니다. 하지만 로봇 조작 분야에서는 데이터가 제한적이고 비용이 많이 듭니다. 올바른 문제 공식화를 통해 조작 분야도 Transformer의 이점을 얻을 수 있을까요? 우리는 이 질문을 다중 작업 6-DoF 조작을 위한 언어 조건화 행동 복제 에이전트인 PerAct를 통해 조사합니다. PerAct는 Perceiver Transformer를 사용하여 언어 목표와 RGB-D 복셀 관측값을 인코딩하고, "다음 최적 복셀 행동 감지"를 통해 이산화된 행동을 출력합니다. 2D 이미지에서 작동하는 프레임워크와 달리, 복셀화된 3D 관측 및 행동 공간은 6-DoF 행동을 효율적으로 학습하기 위한 강력한 구조적 사전 지식을 제공합니다. 이 공식화를 통해 우리는 작업당 몇 개의 시연만으로 18개의 RLBench 작업(249개 변형)과 7개의 실제 세계 작업(18개 변형)에 대해 단일 다중 작업 Transformer를 훈련합니다. 결과는 PerAct가 다양한 탁상 작업에서 비구조적 이미지-행동 에이전트 및 3D ConvNet 기준선을 크게 능가함을 보여줍니다.

## 핵심 내용
Transformer는 대규모 데이터셋으로 확장 가능한 능력을 통해 비전 및 자연어 처리 분야에 혁신을 가져왔습니다. 하지만 로봇 조작 분야에서는 데이터가 제한적이고 비용이 많이 듭니다. 올바른 문제 공식화를 통해 조작 분야도 Transformer의 이점을 얻을 수 있을까요? 우리는 이 질문을 다중 작업 6-DoF 조작을 위한 언어 조건화 행동 복제 에이전트인 PerAct를 통해 조사합니다. PerAct는 Perceiver Transformer를 사용하여 언어 목표와 RGB-D 복셀 관측값을 인코딩하고, "다음 최적 복셀 행동 감지"를 통해 이산화된 행동을 출력합니다. 2D 이미지에서 작동하는 프레임워크와 달리, 복셀화된 3D 관측 및 행동 공간은 6-DoF 행동을 효율적으로 학습하기 위한 강력한 구조적 사전 지식을 제공합니다. 이 공식화를 통해 우리는 작업당 몇 개의 시연만으로 18개의 RLBench 작업(249개 변형)과 7개의 실제 세계 작업(18개 변형)에 대해 단일 다중 작업 Transformer를 훈련합니다. 결과는 PerAct가 다양한 탁상 작업에서 비구조적 이미지-행동 에이전트 및 3D ConvNet 기준선을 크게 능가함을 보여줍니다.
