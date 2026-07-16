---
$id: ent_paper_dreamdojo_a_generalist_robot_w_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos'
  zh: 世界模型开始变成机器人策略的试验场
  ko: 'DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos'
summary:
  en: 'DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos is a knowledge node related to paper in the
    humanoid robot value chain.'
  zh: Being able to simulate the outcomes of actions in varied environments will revolutionize the development of generalist
    agents at scale. However, modeling these world dynamics, especially for dexterous robotics tasks, poses significant challenges
    due to limited data coverage and scarce action labels. As an endeavor towards this end, we introduce DreamDojo, a foundation
    world model that learns diverse interactions and dexterous controls from 44k hours of egocentric human videos. Our data
    mixture represents the largest video dataset to date for world model pretraining, spanning a wide range of daily scenarios
    with diverse objects and skills. To address the scarcity of action labels, we introduce continuous latent actions as unified
    proxy actions, enhancing interaction knowledge transfer from
  ko: 'DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos is a knowledge node related to paper in the
    humanoid robot value chain.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- compliance
- contact_rich
- fall_recovery
- load_carrying
- safety
- whole_body_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.06949v1.
sources:
- id: src_001
  type: paper
  title: 'DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos (arXiv)'
  url: https://arxiv.org/abs/2602.06949
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 世界模型开始变成机器人策略的试验场 project page
  url: https://dreamdojo-world.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
Being able to simulate the outcomes of actions in varied environments will revolutionize the development of generalist agents at scale. However, modeling these world dynamics, especially for dexterous robotics tasks, poses significant challenges due to limited data coverage and scarce action labels. As an endeavor towards this end, we introduce DreamDojo, a foundation world model that learns diverse interactions and dexterous controls from 44k hours of egocentric human videos. Our data mixture represents the largest video dataset to date for world model pretraining, spanning a wide range of daily scenarios with diverse objects and skills. To address the scarcity of action labels, we introduce continuous latent actions as unified proxy actions, enhancing interaction knowledge transfer from unlabeled videos. After post-training on small-scale target robot data, DreamDojo demonstrates a strong understanding of physics and precise action controllability. We also devise a distillation pipeline that accelerates DreamDojo to a real-time speed of 10.81 FPS and further improves context consistency. Our work enables several important applications based on generative world models, including live teleoperation, policy evaluation, and model-based planning. Systematic evaluation on multiple challenging out-of-distribution (OOD) benchmarks verifies the significance of our method for simulating open-world, contact-rich tasks, paving the way for general-purpose robot world models.

## 核心内容
Being able to simulate the outcomes of actions in varied environments will revolutionize the development of generalist agents at scale. However, modeling these world dynamics, especially for dexterous robotics tasks, poses significant challenges due to limited data coverage and scarce action labels. As an endeavor towards this end, we introduce DreamDojo, a foundation world model that learns diverse interactions and dexterous controls from 44k hours of egocentric human videos. Our data mixture represents the largest video dataset to date for world model pretraining, spanning a wide range of daily scenarios with diverse objects and skills. To address the scarcity of action labels, we introduce continuous latent actions as unified proxy actions, enhancing interaction knowledge transfer from unlabeled videos. After post-training on small-scale target robot data, DreamDojo demonstrates a strong understanding of physics and precise action controllability. We also devise a distillation pipeline that accelerates DreamDojo to a real-time speed of 10.81 FPS and further improves context consistency. Our work enables several important applications based on generative world models, including live teleoperation, policy evaluation, and model-based planning. Systematic evaluation on multiple challenging out-of-distribution (OOD) benchmarks verifies the significance of our method for simulating open-world, contact-rich tasks, paving the way for general-purpose robot world models.

## 参考
- http://arxiv.org/abs/2602.06949v1

## Overview
Being able to simulate the outcomes of actions in varied environments will revolutionize the development of generalist agents at scale. However, modeling these world dynamics, especially for dexterous robotics tasks, poses significant challenges due to limited data coverage and scarce action labels. As an endeavor towards this end, we introduce DreamDojo, a foundation world model that learns diverse interactions and dexterous controls from 44k hours of egocentric human videos. Our data mixture represents the largest video dataset to date for world model pretraining, spanning a wide range of daily scenarios with diverse objects and skills. To address the scarcity of action labels, we introduce continuous latent actions as unified proxy actions, enhancing interaction knowledge transfer from unlabeled videos. After post-training on small-scale target robot data, DreamDojo demonstrates a strong understanding of physics and precise action controllability. We also devise a distillation pipeline that accelerates DreamDojo to a real-time speed of 10.81 FPS and further improves context consistency. Our work enables several important applications based on generative world models, including live teleoperation, policy evaluation, and model-based planning. Systematic evaluation on multiple challenging out-of-distribution (OOD) benchmarks verifies the significance of our method for simulating open-world, contact-rich tasks, paving the way for general-purpose robot world models.

## Content
Being able to simulate the outcomes of actions in varied environments will revolutionize the development of generalist agents at scale. However, modeling these world dynamics, especially for dexterous robotics tasks, poses significant challenges due to limited data coverage and scarce action labels. As an endeavor towards this end, we introduce DreamDojo, a foundation world model that learns diverse interactions and dexterous controls from 44k hours of egocentric human videos. Our data mixture represents the largest video dataset to date for world model pretraining, spanning a wide range of daily scenarios with diverse objects and skills. To address the scarcity of action labels, we introduce continuous latent actions as unified proxy actions, enhancing interaction knowledge transfer from unlabeled videos. After post-training on small-scale target robot data, DreamDojo demonstrates a strong understanding of physics and precise action controllability. We also devise a distillation pipeline that accelerates DreamDojo to a real-time speed of 10.81 FPS and further improves context consistency. Our work enables several important applications based on generative world models, including live teleoperation, policy evaluation, and model-based planning. Systematic evaluation on multiple challenging out-of-distribution (OOD) benchmarks verifies the significance of our method for simulating open-world, contact-rich tasks, paving the way for general-purpose robot world models.

## 개요
다양한 환경에서 행동의 결과를 시뮬레이션할 수 있다면, 대규모 범용 에이전트 개발에 혁신을 가져올 것입니다. 그러나 특히 정교한 로봇 작업을 위한 이러한 세계 역학 모델링은 제한된 데이터 범위와 부족한 행동 레이블로 인해 상당한 어려움을 겪습니다. 이러한 목표를 향한 노력의 일환으로, 우리는 44,000시간의 자기중심적 인간 비디오로부터 다양한 상호작용과 정교한 제어를 학습하는 기초 세계 모델인 DreamDojo를 소개합니다. 우리의 데이터 혼합은 세계 모델 사전 학습을 위한 현재까지 가장 큰 비디오 데이터셋을 대표하며, 다양한 객체와 기술을 포함한 광범위한 일상 시나리오를 포괄합니다. 행동 레이블 부족 문제를 해결하기 위해, 우리는 연속 잠재 행동을 통합 프록시 행동으로 도입하여 레이블이 없는 비디오로부터의 상호작용 지식 전이를 향상시킵니다. 소규모 대상 로봇 데이터에 대한 사후 학습 후, DreamDojo는 물리학에 대한 강력한 이해와 정밀한 행동 제어 능력을 보여줍니다. 또한, 우리는 DreamDojo를 실시간 속도인 10.81 FPS로 가속화하고 맥락 일관성을 더욱 개선하는 증류 파이프라인을 고안했습니다. 우리의 연구는 실시간 원격 조작, 정책 평가, 모델 기반 계획을 포함한 생성적 세계 모델 기반의 여러 중요한 응용을 가능하게 합니다. 여러 도전적인 분포 외(OOD) 벤치마크에 대한 체계적인 평가는 개방형 접촉이 많은 작업을 시뮬레이션하는 우리 방법의 중요성을 검증하며, 범용 로봇 세계 모델을 위한 길을 열어줍니다.

## 핵심 내용
다양한 환경에서 행동의 결과를 시뮬레이션할 수 있다면, 대규모 범용 에이전트 개발에 혁신을 가져올 것입니다. 그러나 특히 정교한 로봇 작업을 위한 이러한 세계 역학 모델링은 제한된 데이터 범위와 부족한 행동 레이블로 인해 상당한 어려움을 겪습니다. 이러한 목표를 향한 노력의 일환으로, 우리는 44,000시간의 자기중심적 인간 비디오로부터 다양한 상호작용과 정교한 제어를 학습하는 기초 세계 모델인 DreamDojo를 소개합니다. 우리의 데이터 혼합은 세계 모델 사전 학습을 위한 현재까지 가장 큰 비디오 데이터셋을 대표하며, 다양한 객체와 기술을 포함한 광범위한 일상 시나리오를 포괄합니다. 행동 레이블 부족 문제를 해결하기 위해, 우리는 연속 잠재 행동을 통합 프록시 행동으로 도입하여 레이블이 없는 비디오로부터의 상호작용 지식 전이를 향상시킵니다. 소규모 대상 로봇 데이터에 대한 사후 학습 후, DreamDojo는 물리학에 대한 강력한 이해와 정밀한 행동 제어 능력을 보여줍니다. 또한, 우리는 DreamDojo를 실시간 속도인 10.81 FPS로 가속화하고 맥락 일관성을 더욱 개선하는 증류 파이프라인을 고안했습니다. 우리의 연구는 실시간 원격 조작, 정책 평가, 모델 기반 계획을 포함한 생성적 세계 모델 기반의 여러 중요한 응용을 가능하게 합니다. 여러 도전적인 분포 외(OOD) 벤치마크에 대한 체계적인 평가는 개방형 접촉이 많은 작업을 시뮬레이션하는 우리 방법의 중요성을 검증하며, 범용 로봇 세계 모델을 위한 길을 열어줍니다.
