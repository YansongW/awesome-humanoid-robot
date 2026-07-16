---
$id: ent_paper_amp_adversarial_motion_priors_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control'
  zh: 'AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control'
  ko: 'AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control'
summary:
  en: 'AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control is a 2021 work on physics-based character
    animation for humanoid robots, with open-source code available.'
  zh: 'AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control is a 2021 work on physics-based character
    animation for humanoid robots, with open-source code available.'
  ko: 'AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control is a 2021 work on physics-based character
    animation for humanoid robots, with open-source code available.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- amp
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2104.02180v2.
sources:
- id: src_001
  type: paper
  title: 'AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control (arXiv)'
  url: https://arxiv.org/abs/2104.02180
  date: '2021'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control project page'
  url: https://xbpeng.github.io/projects/AMP/index.html
  date: '2021'
  accessed_at: '2026-07-01'
---
## 概述
Synthesizing graceful and life-like behaviors for physically simulated characters has been a fundamental challenge in computer animation. Data-driven methods that leverage motion tracking are a prominent class of techniques for producing high fidelity motions for a wide range of behaviors. However, the effectiveness of these tracking-based methods often hinges on carefully designed objective functions, and when applied to large and diverse motion datasets, these methods require significant additional machinery to select the appropriate motion for the character to track in a given scenario. In this work, we propose to obviate the need to manually design imitation objectives and mechanisms for motion selection by utilizing a fully automated approach based on adversarial imitation learning. High-level task objectives that the character should perform can be specified by relatively simple reward functions, while the low-level style of the character's behaviors can be specified by a dataset of unstructured motion clips, without any explicit clip selection or sequencing. These motion clips are used to train an adversarial motion prior, which specifies style-rewards for training the character through reinforcement learning (RL). The adversarial RL procedure automatically selects which motion to perform, dynamically interpolating and generalizing from the dataset. Our system produces high-quality motions that are comparable to those achieved by state-of-the-art tracking-based techniques, while also being able to easily accommodate large datasets of unstructured motion clips. Composition of disparate skills emerges automatically from the motion prior, without requiring a high-level motion planner or other task-specific annotations of the motion clips. We demonstrate the effectiveness of our framework on a diverse cast of complex simulated characters and a challenging suite of motor control tasks.

## 核心内容
Synthesizing graceful and life-like behaviors for physically simulated characters has been a fundamental challenge in computer animation. Data-driven methods that leverage motion tracking are a prominent class of techniques for producing high fidelity motions for a wide range of behaviors. However, the effectiveness of these tracking-based methods often hinges on carefully designed objective functions, and when applied to large and diverse motion datasets, these methods require significant additional machinery to select the appropriate motion for the character to track in a given scenario. In this work, we propose to obviate the need to manually design imitation objectives and mechanisms for motion selection by utilizing a fully automated approach based on adversarial imitation learning. High-level task objectives that the character should perform can be specified by relatively simple reward functions, while the low-level style of the character's behaviors can be specified by a dataset of unstructured motion clips, without any explicit clip selection or sequencing. These motion clips are used to train an adversarial motion prior, which specifies style-rewards for training the character through reinforcement learning (RL). The adversarial RL procedure automatically selects which motion to perform, dynamically interpolating and generalizing from the dataset. Our system produces high-quality motions that are comparable to those achieved by state-of-the-art tracking-based techniques, while also being able to easily accommodate large datasets of unstructured motion clips. Composition of disparate skills emerges automatically from the motion prior, without requiring a high-level motion planner or other task-specific annotations of the motion clips. We demonstrate the effectiveness of our framework on a diverse cast of complex simulated characters and a challenging suite of motor control tasks.

## 参考
- http://arxiv.org/abs/2104.02180v2

## Overview
Synthesizing graceful and life-like behaviors for physically simulated characters has been a fundamental challenge in computer animation. Data-driven methods that leverage motion tracking are a prominent class of techniques for producing high fidelity motions for a wide range of behaviors. However, the effectiveness of these tracking-based methods often hinges on carefully designed objective functions, and when applied to large and diverse motion datasets, these methods require significant additional machinery to select the appropriate motion for the character to track in a given scenario. In this work, we propose to obviate the need to manually design imitation objectives and mechanisms for motion selection by utilizing a fully automated approach based on adversarial imitation learning. High-level task objectives that the character should perform can be specified by relatively simple reward functions, while the low-level style of the character's behaviors can be specified by a dataset of unstructured motion clips, without any explicit clip selection or sequencing. These motion clips are used to train an adversarial motion prior, which specifies style-rewards for training the character through reinforcement learning (RL). The adversarial RL procedure automatically selects which motion to perform, dynamically interpolating and generalizing from the dataset. Our system produces high-quality motions that are comparable to those achieved by state-of-the-art tracking-based techniques, while also being able to easily accommodate large datasets of unstructured motion clips. Composition of disparate skills emerges automatically from the motion prior, without requiring a high-level motion planner or other task-specific annotations of the motion clips. We demonstrate the effectiveness of our framework on a diverse cast of complex simulated characters and a challenging suite of motor control tasks.

## Content
Synthesizing graceful and life-like behaviors for physically simulated characters has been a fundamental challenge in computer animation. Data-driven methods that leverage motion tracking are a prominent class of techniques for producing high fidelity motions for a wide range of behaviors. However, the effectiveness of these tracking-based methods often hinges on carefully designed objective functions, and when applied to large and diverse motion datasets, these methods require significant additional machinery to select the appropriate motion for the character to track in a given scenario. In this work, we propose to obviate the need to manually design imitation objectives and mechanisms for motion selection by utilizing a fully automated approach based on adversarial imitation learning. High-level task objectives that the character should perform can be specified by relatively simple reward functions, while the low-level style of the character's behaviors can be specified by a dataset of unstructured motion clips, without any explicit clip selection or sequencing. These motion clips are used to train an adversarial motion prior, which specifies style-rewards for training the character through reinforcement learning (RL). The adversarial RL procedure automatically selects which motion to perform, dynamically interpolating and generalizing from the dataset. Our system produces high-quality motions that are comparable to those achieved by state-of-the-art tracking-based techniques, while also being able to easily accommodate large datasets of unstructured motion clips. Composition of disparate skills emerges automatically from the motion prior, without requiring a high-level motion planner or other task-specific annotations of the motion clips. We demonstrate the effectiveness of our framework on a diverse cast of complex simulated characters and a challenging suite of motor control tasks.

## 개요
물리적으로 시뮬레이션된 캐릭터를 위한 우아하고 생생한 행동을 합성하는 것은 컴퓨터 애니메이션의 근본적인 도전 과제였습니다. 모션 트래킹을 활용하는 데이터 기반 방법은 다양한 행동에 대해 높은 충실도의 모션을 생성하는 대표적인 기술 클래스입니다. 그러나 이러한 트래킹 기반 방법의 효과성은 종종 신중하게 설계된 목적 함수에 의존하며, 크고 다양한 모션 데이터셋에 적용될 때 주어진 시나리오에서 캐릭터가 추적할 적절한 모션을 선택하기 위해 상당한 추가 장치가 필요합니다. 본 연구에서는 적대적 모방 학습(adversarial imitation learning)에 기반한 완전 자동화된 접근 방식을 활용하여 모방 목적과 모션 선택 메커니즘을 수동으로 설계할 필요를 없애고자 합니다. 캐릭터가 수행해야 하는 높은 수준의 작업 목표는 비교적 간단한 보상 함수로 지정할 수 있으며, 캐릭터 행동의 낮은 수준 스타일은 명시적인 클립 선택이나 순서 지정 없이 비구조화된 모션 클립 데이터셋으로 지정할 수 있습니다. 이러한 모션 클립은 강화 학습(RL)을 통해 캐릭터를 훈련하기 위한 스타일 보상을 지정하는 적대적 모션 사전(adversarial motion prior)을 훈련하는 데 사용됩니다. 적대적 RL 절차는 데이터셋에서 동적으로 보간 및 일반화하여 수행할 모션을 자동으로 선택합니다. 우리 시스템은 최첨단 트래킹 기반 기술로 달성된 것과 견줄 만한 고품질 모션을 생성하면서도 비구조화된 모션 클립의 대규모 데이터셋을 쉽게 수용할 수 있습니다. 서로 다른 기술의 구성은 높은 수준의 모션 플래너나 모션 클립의 작업별 주석 없이 모션 사전에서 자동으로 나타납니다. 우리는 다양한 복잡한 시뮬레이션 캐릭터와 까다로운 모터 제어 작업 세트에서 프레임워크의 효과성을 입증합니다.

## 핵심 내용
물리적으로 시뮬레이션된 캐릭터를 위한 우아하고 생생한 행동을 합성하는 것은 컴퓨터 애니메이션의 근본적인 도전 과제였습니다. 모션 트래킹을 활용하는 데이터 기반 방법은 다양한 행동에 대해 높은 충실도의 모션을 생성하는 대표적인 기술 클래스입니다. 그러나 이러한 트래킹 기반 방법의 효과성은 종종 신중하게 설계된 목적 함수에 의존하며, 크고 다양한 모션 데이터셋에 적용될 때 주어진 시나리오에서 캐릭터가 추적할 적절한 모션을 선택하기 위해 상당한 추가 장치가 필요합니다. 본 연구에서는 적대적 모방 학습에 기반한 완전 자동화된 접근 방식을 활용하여 모방 목적과 모션 선택 메커니즘을 수동으로 설계할 필요를 없애고자 합니다. 캐릭터가 수행해야 하는 높은 수준의 작업 목표는 비교적 간단한 보상 함수로 지정할 수 있으며, 캐릭터 행동의 낮은 수준 스타일은 명시적인 클립 선택이나 순서 지정 없이 비구조화된 모션 클립 데이터셋으로 지정할 수 있습니다. 이러한 모션 클립은 강화 학습을 통해 캐릭터를 훈련하기 위한 스타일 보상을 지정하는 적대적 모션 사전을 훈련하는 데 사용됩니다. 적대적 RL 절차는 데이터셋에서 동적으로 보간 및 일반화하여 수행할 모션을 자동으로 선택합니다. 우리 시스템은 최첨단 트래킹 기반 기술로 달성된 것과 견줄 만한 고품질 모션을 생성하면서도 비구조화된 모션 클립의 대규모 데이터셋을 쉽게 수용할 수 있습니다. 서로 다른 기술의 구성은 높은 수준의 모션 플래너나 모션 클립의 작업별 주석 없이 모션 사전에서 자동으로 나타납니다. 우리는 다양한 복잡한 시뮬레이션 캐릭터와 까다로운 모터 제어 작업 세트에서 프레임워크의 효과성을 입증합니다.
