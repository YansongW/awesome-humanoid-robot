---
$id: ent_paper_ase_large_scale_reusable_adver_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters'
  zh: 'ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters'
  ko: 'ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters'
summary:
  en: 'ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters is a 2022 work on physics-based
    character animation for humanoid robots, with open-source code available.'
  zh: 'ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters is a 2022 work on physics-based
    character animation for humanoid robots, with open-source code available.'
  ko: 'ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters is a 2022 work on physics-based
    character animation for humanoid robots, with open-source code available.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- ase
- character_animation
- humanoid
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2205.01906v2.
sources:
- id: src_001
  type: paper
  title: 'ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters (arXiv)'
  url: https://arxiv.org/abs/2205.01906
  date: '2022'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters project page'
  url: https://xbpeng.github.io/projects/ASE/index.html
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
The incredible feats of athleticism demonstrated by humans are made possible in part by a vast repertoire of general-purpose motor skills, acquired through years of practice and experience. These skills not only enable humans to perform complex tasks, but also provide powerful priors for guiding their behaviors when learning new tasks. This is in stark contrast to what is common practice in physics-based character animation, where control policies are most typically trained from scratch for each task. In this work, we present a large-scale data-driven framework for learning versatile and reusable skill embeddings for physically simulated characters. Our approach combines techniques from adversarial imitation learning and unsupervised reinforcement learning to develop skill embeddings that produce life-like behaviors, while also providing an easy to control representation for use on new downstream tasks. Our models can be trained using large datasets of unstructured motion clips, without requiring any task-specific annotation or segmentation of the motion data. By leveraging a massively parallel GPU-based simulator, we are able to train skill embeddings using over a decade of simulated experiences, enabling our model to learn a rich and versatile repertoire of skills. We show that a single pre-trained model can be effectively applied to perform a diverse set of new tasks. Our system also allows users to specify tasks through simple reward functions, and the skill embedding then enables the character to automatically synthesize complex and naturalistic strategies in order to achieve the task objectives.

## 核心内容
The incredible feats of athleticism demonstrated by humans are made possible in part by a vast repertoire of general-purpose motor skills, acquired through years of practice and experience. These skills not only enable humans to perform complex tasks, but also provide powerful priors for guiding their behaviors when learning new tasks. This is in stark contrast to what is common practice in physics-based character animation, where control policies are most typically trained from scratch for each task. In this work, we present a large-scale data-driven framework for learning versatile and reusable skill embeddings for physically simulated characters. Our approach combines techniques from adversarial imitation learning and unsupervised reinforcement learning to develop skill embeddings that produce life-like behaviors, while also providing an easy to control representation for use on new downstream tasks. Our models can be trained using large datasets of unstructured motion clips, without requiring any task-specific annotation or segmentation of the motion data. By leveraging a massively parallel GPU-based simulator, we are able to train skill embeddings using over a decade of simulated experiences, enabling our model to learn a rich and versatile repertoire of skills. We show that a single pre-trained model can be effectively applied to perform a diverse set of new tasks. Our system also allows users to specify tasks through simple reward functions, and the skill embedding then enables the character to automatically synthesize complex and naturalistic strategies in order to achieve the task objectives.

## 参考
- http://arxiv.org/abs/2205.01906v2

## Overview
The incredible feats of athleticism demonstrated by humans are made possible in part by a vast repertoire of general-purpose motor skills, acquired through years of practice and experience. These skills not only enable humans to perform complex tasks, but also provide powerful priors for guiding their behaviors when learning new tasks. This is in stark contrast to what is common practice in physics-based character animation, where control policies are most typically trained from scratch for each task. In this work, we present a large-scale data-driven framework for learning versatile and reusable skill embeddings for physically simulated characters. Our approach combines techniques from adversarial imitation learning and unsupervised reinforcement learning to develop skill embeddings that produce life-like behaviors, while also providing an easy to control representation for use on new downstream tasks. Our models can be trained using large datasets of unstructured motion clips, without requiring any task-specific annotation or segmentation of the motion data. By leveraging a massively parallel GPU-based simulator, we are able to train skill embeddings using over a decade of simulated experiences, enabling our model to learn a rich and versatile repertoire of skills. We show that a single pre-trained model can be effectively applied to perform a diverse set of new tasks. Our system also allows users to specify tasks through simple reward functions, and the skill embedding then enables the character to automatically synthesize complex and naturalistic strategies in order to achieve the task objectives.

## Content
The incredible feats of athleticism demonstrated by humans are made possible in part by a vast repertoire of general-purpose motor skills, acquired through years of practice and experience. These skills not only enable humans to perform complex tasks, but also provide powerful priors for guiding their behaviors when learning new tasks. This is in stark contrast to what is common practice in physics-based character animation, where control policies are most typically trained from scratch for each task. In this work, we present a large-scale data-driven framework for learning versatile and reusable skill embeddings for physically simulated characters. Our approach combines techniques from adversarial imitation learning and unsupervised reinforcement learning to develop skill embeddings that produce life-like behaviors, while also providing an easy to control representation for use on new downstream tasks. Our models can be trained using large datasets of unstructured motion clips, without requiring any task-specific annotation or segmentation of the motion data. By leveraging a massively parallel GPU-based simulator, we are able to train skill embeddings using over a decade of simulated experiences, enabling our model to learn a rich and versatile repertoire of skills. We show that a single pre-trained model can be effectively applied to perform a diverse set of new tasks. Our system also allows users to specify tasks through simple reward functions, and the skill embedding then enables the character to automatically synthesize complex and naturalistic strategies in order to achieve the task objectives.

## 개요
인간이 보여주는 놀라운 운동 능력은 수년간의 연습과 경험을 통해 습득된 방대한 범용 운동 기술 덕분에 가능합니다. 이러한 기술은 인간이 복잡한 작업을 수행할 수 있게 할 뿐만 아니라, 새로운 작업을 학습할 때 행동을 안내하는 강력한 사전 지식을 제공합니다. 이는 물리 기반 캐릭터 애니메이션에서 일반적으로 각 작업마다 제어 정책을 처음부터 학습하는 관행과는 대조적입니다. 본 연구에서는 물리적으로 시뮬레이션된 캐릭터를 위해 다재다능하고 재사용 가능한 기술 임베딩을 학습하는 대규모 데이터 기반 프레임워크를 제시합니다. 우리의 접근 방식은 적대적 모방 학습과 비지도 강화 학습의 기술을 결합하여 생생한 행동을 생성하는 동시에 새로운 하위 작업에 사용하기 쉬운 제어 표현을 제공하는 기술 임베딩을 개발합니다. 우리의 모델은 작업별 주석이나 모션 데이터 분할 없이 구조화되지 않은 대규모 모션 클립 데이터셋을 사용하여 학습할 수 있습니다. 대규모 병렬 GPU 기반 시뮬레이터를 활용하여 10년 이상의 시뮬레이션 경험을 통해 기술 임베딩을 학습할 수 있으며, 이를 통해 모델이 풍부하고 다재다능한 기술 레퍼토리를 습득할 수 있습니다. 단일 사전 학습 모델이 다양한 새로운 작업을 효과적으로 수행할 수 있음을 보여줍니다. 또한 우리 시스템은 사용자가 간단한 보상 함수를 통해 작업을 지정할 수 있도록 하며, 기술 임베딩은 캐릭터가 작업 목표를 달성하기 위해 복잡하고 자연스러운 전략을 자동으로 합성할 수 있게 합니다.

## 핵심 내용
인간이 보여주는 놀라운 운동 능력은 수년간의 연습과 경험을 통해 습득된 방대한 범용 운동 기술 덕분에 가능합니다. 이러한 기술은 인간이 복잡한 작업을 수행할 수 있게 할 뿐만 아니라, 새로운 작업을 학습할 때 행동을 안내하는 강력한 사전 지식을 제공합니다. 이는 물리 기반 캐릭터 애니메이션에서 일반적으로 각 작업마다 제어 정책을 처음부터 학습하는 관행과는 대조적입니다. 본 연구에서는 물리적으로 시뮬레이션된 캐릭터를 위해 다재다능하고 재사용 가능한 기술 임베딩을 학습하는 대규모 데이터 기반 프레임워크를 제시합니다. 우리의 접근 방식은 적대적 모방 학습과 비지도 강화 학습의 기술을 결합하여 생생한 행동을 생성하는 동시에 새로운 하위 작업에 사용하기 쉬운 제어 표현을 제공하는 기술 임베딩을 개발합니다. 우리의 모델은 작업별 주석이나 모션 데이터 분할 없이 구조화되지 않은 대규모 모션 클립 데이터셋을 사용하여 학습할 수 있습니다. 대규모 병렬 GPU 기반 시뮬레이터를 활용하여 10년 이상의 시뮬레이션 경험을 통해 기술 임베딩을 학습할 수 있으며, 이를 통해 모델이 풍부하고 다재다능한 기술 레퍼토리를 습득할 수 있습니다. 단일 사전 학습 모델이 다양한 새로운 작업을 효과적으로 수행할 수 있음을 보여줍니다. 또한 우리 시스템은 사용자가 간단한 보상 함수를 통해 작업을 지정할 수 있도록 하며, 기술 임베딩은 캐릭터가 작업 목표를 달성하기 위해 복잡하고 자연스러운 전략을 자동으로 합성할 수 있게 합니다.
