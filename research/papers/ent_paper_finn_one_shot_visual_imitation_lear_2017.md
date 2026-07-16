---
$id: ent_paper_finn_one_shot_visual_imitation_lear_2017
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: One-Shot Visual Imitation Learning via Meta-Learning
  zh: 基于元学习的一次视觉模仿学习
  ko: 메타러닝을 통한 원샷 시각 모방 학습
summary:
  en: Extends model-agnostic meta-learning (MAML) to imitation learning, enabling a robot to acquire new vision-based manipulation
    skills from a single demonstration via one or a few gradient updates.
  zh: In order for a robot to be a generalist that can perform a wide range of jobs, it must be able to acquire a wide variety
    of skills quickly and efficiently in complex unstructured environments. High-capacity models such as deep neural networks
    can enable a robot to represent complex skills, but learning each skill from scratch then becomes infeasible. In this
    work, we present a meta-imitation learning method that enables a robot to learn how to learn more efficiently, allowing
    it to acquire new skills from just a single demonstration. Unlike prior methods for one-shot imitation, our method can
  ko: 모델 무관 메타러닝(MAML)을 모방 학습으로 확장하여, 로봇이 단 하나의 시연을 통해 한 번 또는 소수의 그래디언트 업데이트로 새로운 비전 기반 조작 기술을 습득할 수 있게 함.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- one_shot_imitation
- meta_learning
- meta_imitation_learning
- visual_imitation
- imitation_learning
- convolutional_neural_network
- spatial_soft_argmax
- bias_transformation
- manipulation
- pr2
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1709.04905v1.
sources:
- id: src_001
  type: paper
  title: One-Shot Visual Imitation Learning via Meta-Learning
  url: https://arxiv.org/abs/1709.04905
  date: '2017'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## 概述
In order for a robot to be a generalist that can perform a wide range of jobs, it must be able to acquire a wide variety of skills quickly and efficiently in complex unstructured environments. High-capacity models such as deep neural networks can enable a robot to represent complex skills, but learning each skill from scratch then becomes infeasible. In this work, we present a meta-imitation learning method that enables a robot to learn how to learn more efficiently, allowing it to acquire new skills from just a single demonstration. Unlike prior methods for one-shot imitation, our method can scale to raw pixel inputs and requires data from significantly fewer prior tasks for effective learning of new skills. Our experiments on both simulated and real robot platforms demonstrate the ability to learn new tasks, end-to-end, from a single visual demonstration.

## 核心内容
In order for a robot to be a generalist that can perform a wide range of jobs, it must be able to acquire a wide variety of skills quickly and efficiently in complex unstructured environments. High-capacity models such as deep neural networks can enable a robot to represent complex skills, but learning each skill from scratch then becomes infeasible. In this work, we present a meta-imitation learning method that enables a robot to learn how to learn more efficiently, allowing it to acquire new skills from just a single demonstration. Unlike prior methods for one-shot imitation, our method can scale to raw pixel inputs and requires data from significantly fewer prior tasks for effective learning of new skills. Our experiments on both simulated and real robot platforms demonstrate the ability to learn new tasks, end-to-end, from a single visual demonstration.

## 参考
- http://arxiv.org/abs/1709.04905v1

## Overview
In order for a robot to be a generalist that can perform a wide range of jobs, it must be able to acquire a wide variety of skills quickly and efficiently in complex unstructured environments. High-capacity models such as deep neural networks can enable a robot to represent complex skills, but learning each skill from scratch then becomes infeasible. In this work, we present a meta-imitation learning method that enables a robot to learn how to learn more efficiently, allowing it to acquire new skills from just a single demonstration. Unlike prior methods for one-shot imitation, our method can scale to raw pixel inputs and requires data from significantly fewer prior tasks for effective learning of new skills. Our experiments on both simulated and real robot platforms demonstrate the ability to learn new tasks, end-to-end, from a single visual demonstration.

## Content
In order for a robot to be a generalist that can perform a wide range of jobs, it must be able to acquire a wide variety of skills quickly and efficiently in complex unstructured environments. High-capacity models such as deep neural networks can enable a robot to represent complex skills, but learning each skill from scratch then becomes infeasible. In this work, we present a meta-imitation learning method that enables a robot to learn how to learn more efficiently, allowing it to acquire new skills from just a single demonstration. Unlike prior methods for one-shot imitation, our method can scale to raw pixel inputs and requires data from significantly fewer prior tasks for effective learning of new skills. Our experiments on both simulated and real robot platforms demonstrate the ability to learn new tasks, end-to-end, from a single visual demonstration.

## 개요
로봇이 다양한 작업을 수행할 수 있는 제너럴리스트가 되기 위해서는 복잡한 비정형 환경에서 빠르고 효율적으로 다양한 기술을 습득할 수 있어야 합니다. 심층 신경망과 같은 고용량 모델은 로봇이 복잡한 기술을 표현할 수 있게 해주지만, 각 기술을 처음부터 학습하는 것은 비현실적입니다. 본 연구에서는 로봇이 더 효율적으로 학습하는 방법을 배울 수 있도록 하는 메타 모방 학습 방법을 제시하며, 단 한 번의 시연만으로 새로운 기술을 습득할 수 있게 합니다. 기존의 원샷 모방 방법과 달리, 본 방법은 원시 픽셀 입력으로 확장 가능하며, 새로운 기술을 효과적으로 학습하기 위해 훨씬 적은 수의 사전 작업 데이터만 필요로 합니다. 시뮬레이션 및 실제 로봇 플랫폼에서의 실험을 통해 단일 시각적 시연으로부터 종단간(end-to-end)으로 새로운 작업을 학습할 수 있는 능력을 입증했습니다.

## 핵심 내용
로봇이 다양한 작업을 수행할 수 있는 제너럴리스트가 되기 위해서는 복잡한 비정형 환경에서 빠르고 효율적으로 다양한 기술을 습득할 수 있어야 합니다. 심층 신경망과 같은 고용량 모델은 로봇이 복잡한 기술을 표현할 수 있게 해주지만, 각 기술을 처음부터 학습하는 것은 비현실적입니다. 본 연구에서는 로봇이 더 효율적으로 학습하는 방법을 배울 수 있도록 하는 메타 모방 학습 방법을 제시하며, 단 한 번의 시연만으로 새로운 기술을 습득할 수 있게 합니다. 기존의 원샷 모방 방법과 달리, 본 방법은 원시 픽셀 입력으로 확장 가능하며, 새로운 기술을 효과적으로 학습하기 위해 훨씬 적은 수의 사전 작업 데이터만 필요로 합니다. 시뮬레이션 및 실제 로봇 플랫폼에서의 실험을 통해 단일 시각적 시연으로부터 종단간(end-to-end)으로 새로운 작업을 학습할 수 있는 능력을 입증했습니다.
