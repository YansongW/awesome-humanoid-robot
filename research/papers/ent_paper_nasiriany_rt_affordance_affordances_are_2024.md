---
$id: ent_paper_nasiriany_rt_affordance_affordances_are_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation'
  zh: RT-A
  ko: 'RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation'
summary:
  en: 'RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation (RT-A), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Google DeepMind, The University of Austin at Texas,
    and published at ICRA25.'
  zh: 'RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation (RT-A), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Google DeepMind, The University of Austin at Texas,
    and published at ICRA25.'
  ko: 'RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation (RT-A), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Google DeepMind, The University of Austin at Texas,
    and published at ICRA25.'
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
- rt_a
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2411.02704v1.
sources:
- id: src_001
  type: website
  title: RT-A source
  url: https://doi.org/10.1109/ICRA55743.2025.11127525
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
We explore how intermediate policy representations can facilitate generalization by providing guidance on how to perform manipulation tasks. Existing representations such as language, goal images, and trajectory sketches have been shown to be helpful, but these representations either do not provide enough context or provide over-specified context that yields less robust policies. We propose conditioning policies on affordances, which capture the pose of the robot at key stages of the task. Affordances offer expressive yet lightweight abstractions, are easy for users to specify, and facilitate efficient learning by transferring knowledge from large internet datasets. Our method, RT-Affordance, is a hierarchical model that first proposes an affordance plan given the task language, and then conditions the policy on this affordance plan to perform manipulation. Our model can flexibly bridge heterogeneous sources of supervision including large web datasets and robot trajectories. We additionally train our model on cheap-to-collect in-domain affordance images, allowing us to learn new tasks without collecting any additional costly robot trajectories. We show on a diverse set of novel tasks how RT-Affordance exceeds the performance of existing methods by over 50%, and we empirically demonstrate that affordances are robust to novel settings. Videos available at https://snasiriany.me/rt-affordance

## 核心内容
We explore how intermediate policy representations can facilitate generalization by providing guidance on how to perform manipulation tasks. Existing representations such as language, goal images, and trajectory sketches have been shown to be helpful, but these representations either do not provide enough context or provide over-specified context that yields less robust policies. We propose conditioning policies on affordances, which capture the pose of the robot at key stages of the task. Affordances offer expressive yet lightweight abstractions, are easy for users to specify, and facilitate efficient learning by transferring knowledge from large internet datasets. Our method, RT-Affordance, is a hierarchical model that first proposes an affordance plan given the task language, and then conditions the policy on this affordance plan to perform manipulation. Our model can flexibly bridge heterogeneous sources of supervision including large web datasets and robot trajectories. We additionally train our model on cheap-to-collect in-domain affordance images, allowing us to learn new tasks without collecting any additional costly robot trajectories. We show on a diverse set of novel tasks how RT-Affordance exceeds the performance of existing methods by over 50%, and we empirically demonstrate that affordances are robust to novel settings. Videos available at https://snasiriany.me/rt-affordance

## 参考
- http://arxiv.org/abs/2411.02704v1

## Overview
We explore how intermediate policy representations can facilitate generalization by providing guidance on how to perform manipulation tasks. Existing representations such as language, goal images, and trajectory sketches have been shown to be helpful, but these representations either do not provide enough context or provide over-specified context that yields less robust policies. We propose conditioning policies on affordances, which capture the pose of the robot at key stages of the task. Affordances offer expressive yet lightweight abstractions, are easy for users to specify, and facilitate efficient learning by transferring knowledge from large internet datasets. Our method, RT-Affordance, is a hierarchical model that first proposes an affordance plan given the task language, and then conditions the policy on this affordance plan to perform manipulation. Our model can flexibly bridge heterogeneous sources of supervision including large web datasets and robot trajectories. We additionally train our model on cheap-to-collect in-domain affordance images, allowing us to learn new tasks without collecting any additional costly robot trajectories. We show on a diverse set of novel tasks how RT-Affordance exceeds the performance of existing methods by over 50%, and we empirically demonstrate that affordances are robust to novel settings. Videos available at https://snasiriany.me/rt-affordance

## Content
We explore how intermediate policy representations can facilitate generalization by providing guidance on how to perform manipulation tasks. Existing representations such as language, goal images, and trajectory sketches have been shown to be helpful, but these representations either do not provide enough context or provide over-specified context that yields less robust policies. We propose conditioning policies on affordances, which capture the pose of the robot at key stages of the task. Affordances offer expressive yet lightweight abstractions, are easy for users to specify, and facilitate efficient learning by transferring knowledge from large internet datasets. Our method, RT-Affordance, is a hierarchical model that first proposes an affordance plan given the task language, and then conditions the policy on this affordance plan to perform manipulation. Our model can flexibly bridge heterogeneous sources of supervision including large web datasets and robot trajectories. We additionally train our model on cheap-to-collect in-domain affordance images, allowing us to learn new tasks without collecting any additional costly robot trajectories. We show on a diverse set of novel tasks how RT-Affordance exceeds the performance of existing methods by over 50%, and we empirically demonstrate that affordances are robust to novel settings. Videos available at https://snasiriany.me/rt-affordance

## 개요
본 연구에서는 중간 정책 표현이 조작 작업 수행 방법에 대한 지침을 제공함으로써 일반화를 촉진할 수 있는 방법을 탐구합니다. 언어, 목표 이미지, 궤적 스케치와 같은 기존 표현은 유용한 것으로 입증되었지만, 이러한 표현은 충분한 맥락을 제공하지 못하거나 지나치게 구체적인 맥락을 제공하여 덜 강건한 정책을 초래합니다. 우리는 작업의 주요 단계에서 로봇의 자세를 포착하는 어포던스(affordances)에 정책을 조건화하는 것을 제안합니다. 어포던스는 표현력이 풍부하면서도 가벼운 추상화를 제공하고, 사용자가 쉽게 지정할 수 있으며, 대규모 인터넷 데이터셋에서 지식을 전이하여 효율적인 학습을 촉진합니다. 우리의 방법인 RT-Affordance는 계층적 모델로, 먼저 작업 언어가 주어지면 어포던스 계획을 제안한 다음, 이 어포던스 계획에 정책을 조건화하여 조작을 수행합니다. 우리의 모델은 대규모 웹 데이터셋과 로봇 궤적을 포함한 이질적인 감독 소스를 유연하게 연결할 수 있습니다. 또한 저렴하게 수집 가능한 도메인 내 어포던스 이미지로 모델을 훈련하여, 추가적인 고비용 로봇 궤적을 수집하지 않고도 새로운 작업을 학습할 수 있습니다. 우리는 다양한 새로운 작업 세트에서 RT-Affordance가 기존 방법보다 50% 이상 뛰어난 성능을 보이는 것을 입증하고, 어포던스가 새로운 환경에 강건함을 실증적으로 보여줍니다. 비디오는 https://snasiriany.me/rt-affordance 에서 확인할 수 있습니다.

## 핵심 내용
본 연구에서는 중간 정책 표현이 조작 작업 수행 방법에 대한 지침을 제공함으로써 일반화를 촉진할 수 있는 방법을 탐구합니다. 언어, 목표 이미지, 궤적 스케치와 같은 기존 표현은 유용한 것으로 입증되었지만, 이러한 표현은 충분한 맥락을 제공하지 못하거나 지나치게 구체적인 맥락을 제공하여 덜 강건한 정책을 초래합니다. 우리는 작업의 주요 단계에서 로봇의 자세를 포착하는 어포던스(affordances)에 정책을 조건화하는 것을 제안합니다. 어포던스는 표현력이 풍부하면서도 가벼운 추상화를 제공하고, 사용자가 쉽게 지정할 수 있으며, 대규모 인터넷 데이터셋에서 지식을 전이하여 효율적인 학습을 촉진합니다. 우리의 방법인 RT-Affordance는 계층적 모델로, 먼저 작업 언어가 주어지면 어포던스 계획을 제안한 다음, 이 어포던스 계획에 정책을 조건화하여 조작을 수행합니다. 우리의 모델은 대규모 웹 데이터셋과 로봇 궤적을 포함한 이질적인 감독 소스를 유연하게 연결할 수 있습니다. 또한 저렴하게 수집 가능한 도메인 내 어포던스 이미지로 모델을 훈련하여, 추가적인 고비용 로봇 궤적을 수집하지 않고도 새로운 작업을 학습할 수 있습니다. 우리는 다양한 새로운 작업 세트에서 RT-Affordance가 기존 방법보다 50% 이상 뛰어난 성능을 보이는 것을 입증하고, 어포던스가 새로운 환경에 강건함을 실증적으로 보여줍니다. 비디오는 https://snasiriany.me/rt-affordance 에서 확인할 수 있습니다.
