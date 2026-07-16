---
$id: ent_paper_zhang_unicod_enhancing_robot_policy_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'UniCoD: Enhancing Robot Policy via Unified Continuous and Discrete Representation Learning'
  zh: UniCoD
  ko: 'UniCoD: Enhancing Robot Policy via Unified Continuous and Discrete Representation Learning'
summary:
  en: 'UniCoD: Enhancing Robot Policy via Unified Continuous and Discrete Representation Learning (UniCoD), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute for Interdisciplinary Information Sciences,
    Tsinghua University, Shanghai Qizhi Institute, Peking University, Shanghai AI Lab.'
  zh: 'UniCoD: Enhancing Robot Policy via Unified Continuous and Discrete Representation Learning (UniCoD), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute for Interdisciplinary Information Sciences,
    Tsinghua University, Shanghai Qizhi Institute, Peking University, Shanghai AI Lab.'
  ko: 'UniCoD: Enhancing Robot Policy via Unified Continuous and Discrete Representation Learning (UniCoD), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute for Interdisciplinary Information Sciences,
    Tsinghua University, Shanghai Qizhi Institute, Peking University, Shanghai AI Lab.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- unicod
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.10642v3.
sources:
- id: src_001
  type: paper
  title: 'UniCoD: Enhancing Robot Policy via Unified Continuous and Discrete Representation Learning (arXiv)'
  url: https://arxiv.org/abs/2510.10642
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: UniCoD source
  url: https://doi.org/10.48550/arXiv.2510.10642
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Building generalist robot policies that can handle diverse tasks in open-ended environments is a central challenge in robotics. To leverage knowledge from large-scale pretraining, prior work (VLA) has typically built generalist policies either on top of vision-language understanding models (VLMs) or generative models. However, both semantic understanding from vision-language pretraining and visual dynamics modeling from visual-generation pretraining are crucial for embodied robots. Recent unified models of generation and understanding have demonstrated strong capabilities in both comprehension and generation through large-scale pretraining. We posit that robotic policy learning can likewise benefit from the combined strengths of understanding, planning, and continuous future representation learning. Building on this insight, we introduce UniJEPA, which acquires the ability to dynamically model high-dimensional visual features through pretraining on over 1M internet-scale instructional manipulation videos. Subsequently, UniJEPA is fine-tuned on data collected from the robot embodiment, enabling the learning of mappings from predictive representations to action tokens. Extensive experiments show our approach consistently outperforms baseline methods in terms of 9\% and 12\% across simulation environments and real-world out-of-distribution tasks.

## 核心内容
Building generalist robot policies that can handle diverse tasks in open-ended environments is a central challenge in robotics. To leverage knowledge from large-scale pretraining, prior work (VLA) has typically built generalist policies either on top of vision-language understanding models (VLMs) or generative models. However, both semantic understanding from vision-language pretraining and visual dynamics modeling from visual-generation pretraining are crucial for embodied robots. Recent unified models of generation and understanding have demonstrated strong capabilities in both comprehension and generation through large-scale pretraining. We posit that robotic policy learning can likewise benefit from the combined strengths of understanding, planning, and continuous future representation learning. Building on this insight, we introduce UniJEPA, which acquires the ability to dynamically model high-dimensional visual features through pretraining on over 1M internet-scale instructional manipulation videos. Subsequently, UniJEPA is fine-tuned on data collected from the robot embodiment, enabling the learning of mappings from predictive representations to action tokens. Extensive experiments show our approach consistently outperforms baseline methods in terms of 9\% and 12\% across simulation environments and real-world out-of-distribution tasks.

## 参考
- http://arxiv.org/abs/2510.10642v3

## Overview
Building generalist robot policies that can handle diverse tasks in open-ended environments is a central challenge in robotics. To leverage knowledge from large-scale pretraining, prior work (VLA) has typically built generalist policies either on top of vision-language understanding models (VLMs) or generative models. However, both semantic understanding from vision-language pretraining and visual dynamics modeling from visual-generation pretraining are crucial for embodied robots. Recent unified models of generation and understanding have demonstrated strong capabilities in both comprehension and generation through large-scale pretraining. We posit that robotic policy learning can likewise benefit from the combined strengths of understanding, planning, and continuous future representation learning. Building on this insight, we introduce UniJEPA, which acquires the ability to dynamically model high-dimensional visual features through pretraining on over 1M internet-scale instructional manipulation videos. Subsequently, UniJEPA is fine-tuned on data collected from the robot embodiment, enabling the learning of mappings from predictive representations to action tokens. Extensive experiments show our approach consistently outperforms baseline methods in terms of 9\% and 12\% across simulation environments and real-world out-of-distribution tasks.

## Content
Building generalist robot policies that can handle diverse tasks in open-ended environments is a central challenge in robotics. To leverage knowledge from large-scale pretraining, prior work (VLA) has typically built generalist policies either on top of vision-language understanding models (VLMs) or generative models. However, both semantic understanding from vision-language pretraining and visual dynamics modeling from visual-generation pretraining are crucial for embodied robots. Recent unified models of generation and understanding have demonstrated strong capabilities in both comprehension and generation through large-scale pretraining. We posit that robotic policy learning can likewise benefit from the combined strengths of understanding, planning, and continuous future representation learning. Building on this insight, we introduce UniJEPA, which acquires the ability to dynamically model high-dimensional visual features through pretraining on over 1M internet-scale instructional manipulation videos. Subsequently, UniJEPA is fine-tuned on data collected from the robot embodiment, enabling the learning of mappings from predictive representations to action tokens. Extensive experiments show our approach consistently outperforms baseline methods in terms of 9\% and 12\% across simulation environments and real-world out-of-distribution tasks.

## 개요
개방형 환경에서 다양한 작업을 처리할 수 있는 범용 로봇 정책을 구축하는 것은 로봇 공학의 핵심 과제입니다. 대규모 사전 학습의 지식을 활용하기 위해, 기존 연구(VLA)는 일반적으로 시각-언어 이해 모델(VLM) 또는 생성 모델 위에 범용 정책을 구축해 왔습니다. 그러나 시각-언어 사전 학습의 의미 이해와 시각 생성 사전 학습의 시각적 동역학 모델링은 모두 임베디드 로봇에 필수적입니다. 최근 생성과 이해의 통합 모델은 대규모 사전 학습을 통해 이해와 생성 모두에서 강력한 능력을 입증했습니다. 우리는 로봇 정책 학습도 이해, 계획, 연속적인 미래 표현 학습의 결합된 강점으로부터 이점을 얻을 수 있다고 가정합니다. 이 통찰력을 바탕으로, 우리는 UniJEPA를 소개합니다. 이는 100만 개 이상의 인터넷 규모 지시 조작 비디오에 대한 사전 학습을 통해 고차원 시각적 특징을 동적으로 모델링하는 능력을 획득합니다. 이후 UniJEPA는 로봇 임베디드에서 수집된 데이터로 미세 조정되어 예측 표현에서 행동 토큰으로의 매핑 학습을 가능하게 합니다. 광범위한 실험을 통해 우리의 접근 방식은 시뮬레이션 환경과 실제 분포 외 작업에서 기준 방법보다 각각 9% 및 12% 더 우수한 성능을 일관되게 보여줍니다.

## 핵심 내용
개방형 환경에서 다양한 작업을 처리할 수 있는 범용 로봇 정책을 구축하는 것은 로봇 공학의 핵심 과제입니다. 대규모 사전 학습의 지식을 활용하기 위해, 기존 연구(VLA)는 일반적으로 시각-언어 이해 모델(VLM) 또는 생성 모델 위에 범용 정책을 구축해 왔습니다. 그러나 시각-언어 사전 학습의 의미 이해와 시각 생성 사전 학습의 시각적 동역학 모델링은 모두 임베디드 로봇에 필수적입니다. 최근 생성과 이해의 통합 모델은 대규모 사전 학습을 통해 이해와 생성 모두에서 강력한 능력을 입증했습니다. 우리는 로봇 정책 학습도 이해, 계획, 연속적인 미래 표현 학습의 결합된 강점으로부터 이점을 얻을 수 있다고 가정합니다. 이 통찰력을 바탕으로, 우리는 UniJEPA를 소개합니다. 이는 100만 개 이상의 인터넷 규모 지시 조작 비디오에 대한 사전 학습을 통해 고차원 시각적 특징을 동적으로 모델링하는 능력을 획득합니다. 이후 UniJEPA는 로봇 임베디드에서 수집된 데이터로 미세 조정되어 예측 표현에서 행동 토큰으로의 매핑 학습을 가능하게 합니다. 광범위한 실험을 통해 우리의 접근 방식은 시뮬레이션 환경과 실제 분포 외 작업에서 기준 방법보다 각각 9% 및 12% 더 우수한 성능을 일관되게 보여줍니다.
