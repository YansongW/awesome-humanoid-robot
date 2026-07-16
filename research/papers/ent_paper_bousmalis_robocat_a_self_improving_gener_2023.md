---
$id: ent_paper_bousmalis_robocat_a_self_improving_gener_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation'
  zh: RoboCat
  ko: 'RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation'
summary:
  en: 'RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation (RoboCat), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Google DeepMind, and published at Trans. Mach. Learn. Res. 2024.'
  zh: 'RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation (RoboCat), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Google DeepMind, and published at Trans. Mach. Learn. Res. 2024.'
  ko: 'RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation (RoboCat), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Google DeepMind, and published at Trans. Mach. Learn. Res. 2024.'
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
- robocat
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2306.11706v2.
sources:
- id: src_001
  type: paper
  title: RoboCat source
  url: https://openreview.net/forum?id=vsCpILiWHu
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
The ability to leverage heterogeneous robotic experience from different robots and tasks to quickly master novel skills and embodiments has the potential to transform robot learning. Inspired by recent advances in foundation models for vision and language, we propose a multi-embodiment, multi-task generalist agent for robotic manipulation. This agent, named RoboCat, is a visual goal-conditioned decision transformer capable of consuming action-labelled visual experience. This data spans a large repertoire of motor control skills from simulated and real robotic arms with varying sets of observations and actions. With RoboCat, we demonstrate the ability to generalise to new tasks and robots, both zero-shot as well as through adaptation using only 100-1000 examples for the target task. We also show how a trained model itself can be used to generate data for subsequent training iterations, thus providing a basic building block for an autonomous improvement loop. We investigate the agent's capabilities, with large-scale evaluations both in simulation and on three different real robot embodiments. We find that as we grow and diversify its training data, RoboCat not only shows signs of cross-task transfer, but also becomes more efficient at adapting to new tasks.

## 核心内容
The ability to leverage heterogeneous robotic experience from different robots and tasks to quickly master novel skills and embodiments has the potential to transform robot learning. Inspired by recent advances in foundation models for vision and language, we propose a multi-embodiment, multi-task generalist agent for robotic manipulation. This agent, named RoboCat, is a visual goal-conditioned decision transformer capable of consuming action-labelled visual experience. This data spans a large repertoire of motor control skills from simulated and real robotic arms with varying sets of observations and actions. With RoboCat, we demonstrate the ability to generalise to new tasks and robots, both zero-shot as well as through adaptation using only 100-1000 examples for the target task. We also show how a trained model itself can be used to generate data for subsequent training iterations, thus providing a basic building block for an autonomous improvement loop. We investigate the agent's capabilities, with large-scale evaluations both in simulation and on three different real robot embodiments. We find that as we grow and diversify its training data, RoboCat not only shows signs of cross-task transfer, but also becomes more efficient at adapting to new tasks.

## 参考
- http://arxiv.org/abs/2306.11706v2

## Overview
The ability to leverage heterogeneous robotic experience from different robots and tasks to quickly master novel skills and embodiments has the potential to transform robot learning. Inspired by recent advances in foundation models for vision and language, we propose a multi-embodiment, multi-task generalist agent for robotic manipulation. This agent, named RoboCat, is a visual goal-conditioned decision transformer capable of consuming action-labelled visual experience. This data spans a large repertoire of motor control skills from simulated and real robotic arms with varying sets of observations and actions. With RoboCat, we demonstrate the ability to generalise to new tasks and robots, both zero-shot as well as through adaptation using only 100-1000 examples for the target task. We also show how a trained model itself can be used to generate data for subsequent training iterations, thus providing a basic building block for an autonomous improvement loop. We investigate the agent's capabilities, with large-scale evaluations both in simulation and on three different real robot embodiments. We find that as we grow and diversify its training data, RoboCat not only shows signs of cross-task transfer, but also becomes more efficient at adapting to new tasks.

## Content
The ability to leverage heterogeneous robotic experience from different robots and tasks to quickly master novel skills and embodiments has the potential to transform robot learning. Inspired by recent advances in foundation models for vision and language, we propose a multi-embodiment, multi-task generalist agent for robotic manipulation. This agent, named RoboCat, is a visual goal-conditioned decision transformer capable of consuming action-labelled visual experience. This data spans a large repertoire of motor control skills from simulated and real robotic arms with varying sets of observations and actions. With RoboCat, we demonstrate the ability to generalise to new tasks and robots, both zero-shot as well as through adaptation using only 100-1000 examples for the target task. We also show how a trained model itself can be used to generate data for subsequent training iterations, thus providing a basic building block for an autonomous improvement loop. We investigate the agent's capabilities, with large-scale evaluations both in simulation and on three different real robot embodiments. We find that as we grow and diversify its training data, RoboCat not only shows signs of cross-task transfer, but also becomes more efficient at adapting to new tasks.

## 개요
다양한 로봇과 작업에서 얻은 이질적 로봇 경험을 활용하여 새로운 기술과 구현체를 빠르게 습득할 수 있는 능력은 로봇 학습을 혁신할 잠재력을 지니고 있습니다. 비전 및 언어 분야의 기초 모델(foundation model) 최근 발전에 영감을 받아, 우리는 로봇 조작을 위한 다중 구현체, 다중 작업 범용 에이전트를 제안합니다. 이 에이전트는 RoboCat이라 명명되었으며, 시각적 목표 조건부 결정 트랜스포머(visual goal-conditioned decision transformer)로서 행동 레이블이 지정된 시각적 경험을 소비할 수 있습니다. 이 데이터는 다양한 관찰 및 행동 세트를 가진 시뮬레이션 및 실제 로봇 팔의 광범위한 모터 제어 기술을 포괄합니다. RoboCat을 통해 우리는 새로운 작업과 로봇에 대해 제로샷(zero-shot)뿐만 아니라 대상 작업에 대해 100~1000개의 예제만 사용한 적응을 통해 일반화할 수 있는 능력을 입증합니다. 또한 훈련된 모델 자체를 후속 훈련 반복을 위한 데이터 생성에 사용할 수 있어, 자율적 개선 루프의 기본 구성 요소를 제공함을 보여줍니다. 우리는 시뮬레이션과 세 가지 다른 실제 로봇 구현체에서의 대규모 평가를 통해 에이전트의 능력을 조사합니다. 훈련 데이터를 확장하고 다양화함에 따라 RoboCat이 교차 작업 전이(cross-task transfer)의 징후를 보일 뿐만 아니라 새로운 작업에 적응하는 데 더 효율적이 된다는 것을 발견했습니다.

## 핵심 내용
다양한 로봇과 작업에서 얻은 이질적 로봇 경험을 활용하여 새로운 기술과 구현체를 빠르게 습득할 수 있는 능력은 로봇 학습을 혁신할 잠재력을 지니고 있습니다. 비전 및 언어 분야의 기초 모델 최근 발전에 영감을 받아, 우리는 로봇 조작을 위한 다중 구현체, 다중 작업 범용 에이전트를 제안합니다. 이 에이전트는 RoboCat이라 명명되었으며, 시각적 목표 조건부 결정 트랜스포머로서 행동 레이블이 지정된 시각적 경험을 소비할 수 있습니다. 이 데이터는 다양한 관찰 및 행동 세트를 가진 시뮬레이션 및 실제 로봇 팔의 광범위한 모터 제어 기술을 포괄합니다. RoboCat을 통해 우리는 새로운 작업과 로봇에 대해 제로샷뿐만 아니라 대상 작업에 대해 100~1000개의 예제만 사용한 적응을 통해 일반화할 수 있는 능력을 입증합니다. 또한 훈련된 모델 자체를 후속 훈련 반복을 위한 데이터 생성에 사용할 수 있어, 자율적 개선 루프의 기본 구성 요소를 제공함을 보여줍니다. 우리는 시뮬레이션과 세 가지 다른 실제 로봇 구현체에서의 대규모 평가를 통해 에이전트의 능력을 조사합니다. 훈련 데이터를 확장하고 다양화함에 따라 RoboCat이 교차 작업 전이의 징후를 보일 뿐만 아니라 새로운 작업에 적응하는 데 더 효율적이 된다는 것을 발견했습니다.
