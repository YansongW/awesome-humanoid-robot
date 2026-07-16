---
$id: ent_paper_closd_closing_the_loop_between_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CLoSD: Closing the Loop between Simulation and Diffusion for multi-task character control'
  zh: 'CLoSD: Closing the Loop between Simulation and Diffusion for multi-task character control'
  ko: 'CLoSD: Closing the Loop between Simulation and Diffusion for multi-task character control'
summary:
  en: 'CLoSD: Closing the Loop between Simulation and Diffusion for multi-task character control is a 2024 work on physics-based
    character animation for humanoid robots.'
  zh: 'CLoSD: Closing the Loop between Simulation and Diffusion for multi-task character control is a 2024 work on physics-based
    character animation for humanoid robots.'
  ko: 'CLoSD: Closing the Loop between Simulation and Diffusion for multi-task character control is a 2024 work on physics-based
    character animation for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- closd
- humanoid
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.03441v1.
sources:
- id: src_001
  type: paper
  title: 'CLoSD: Closing the Loop between Simulation and Diffusion for multi-task character control (arXiv)'
  url: https://arxiv.org/abs/2410.03441
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'CLoSD: Closing the Loop between Simulation and Diffusion for multi-task character control project page'
  url: https://guytevet.github.io/CLoSD-page/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Motion diffusion models and Reinforcement Learning (RL) based control for physics-based simulations have complementary strengths for human motion generation. The former is capable of generating a wide variety of motions, adhering to intuitive control such as text, while the latter offers physically plausible motion and direct interaction with the environment. In this work, we present a method that combines their respective strengths. CLoSD is a text-driven RL physics-based controller, guided by diffusion generation for various tasks. Our key insight is that motion diffusion can serve as an on-the-fly universal planner for a robust RL controller. To this end, CLoSD maintains a closed-loop interaction between two modules -- a Diffusion Planner (DiP), and a tracking controller. DiP is a fast-responding autoregressive diffusion model, controlled by textual prompts and target locations, and the controller is a simple and robust motion imitator that continuously receives motion plans from DiP and provides feedback from the environment. CLoSD is capable of seamlessly performing a sequence of different tasks, including navigation to a goal location, striking an object with a hand or foot as specified in a text prompt, sitting down, and getting up. https://guytevet.github.io/CLoSD-page/

## 核心内容
Motion diffusion models and Reinforcement Learning (RL) based control for physics-based simulations have complementary strengths for human motion generation. The former is capable of generating a wide variety of motions, adhering to intuitive control such as text, while the latter offers physically plausible motion and direct interaction with the environment. In this work, we present a method that combines their respective strengths. CLoSD is a text-driven RL physics-based controller, guided by diffusion generation for various tasks. Our key insight is that motion diffusion can serve as an on-the-fly universal planner for a robust RL controller. To this end, CLoSD maintains a closed-loop interaction between two modules -- a Diffusion Planner (DiP), and a tracking controller. DiP is a fast-responding autoregressive diffusion model, controlled by textual prompts and target locations, and the controller is a simple and robust motion imitator that continuously receives motion plans from DiP and provides feedback from the environment. CLoSD is capable of seamlessly performing a sequence of different tasks, including navigation to a goal location, striking an object with a hand or foot as specified in a text prompt, sitting down, and getting up. https://guytevet.github.io/CLoSD-page/

## 参考
- http://arxiv.org/abs/2410.03441v1

## Overview
Motion diffusion models and Reinforcement Learning (RL) based control for physics-based simulations have complementary strengths for human motion generation. The former is capable of generating a wide variety of motions, adhering to intuitive control such as text, while the latter offers physically plausible motion and direct interaction with the environment. In this work, we present a method that combines their respective strengths. CLoSD is a text-driven RL physics-based controller, guided by diffusion generation for various tasks. Our key insight is that motion diffusion can serve as an on-the-fly universal planner for a robust RL controller. To this end, CLoSD maintains a closed-loop interaction between two modules -- a Diffusion Planner (DiP), and a tracking controller. DiP is a fast-responding autoregressive diffusion model, controlled by textual prompts and target locations, and the controller is a simple and robust motion imitator that continuously receives motion plans from DiP and provides feedback from the environment. CLoSD is capable of seamlessly performing a sequence of different tasks, including navigation to a goal location, striking an object with a hand or foot as specified in a text prompt, sitting down, and getting up. https://guytevet.github.io/CLoSD-page/

## Content
Motion diffusion models and Reinforcement Learning (RL) based control for physics-based simulations have complementary strengths for human motion generation. The former is capable of generating a wide variety of motions, adhering to intuitive control such as text, while the latter offers physically plausible motion and direct interaction with the environment. In this work, we present a method that combines their respective strengths. CLoSD is a text-driven RL physics-based controller, guided by diffusion generation for various tasks. Our key insight is that motion diffusion can serve as an on-the-fly universal planner for a robust RL controller. To this end, CLoSD maintains a closed-loop interaction between two modules -- a Diffusion Planner (DiP), and a tracking controller. DiP is a fast-responding autoregressive diffusion model, controlled by textual prompts and target locations, and the controller is a simple and robust motion imitator that continuously receives motion plans from DiP and provides feedback from the environment. CLoSD is capable of seamlessly performing a sequence of different tasks, including navigation to a goal location, striking an object with a hand or foot as specified in a text prompt, sitting down, and getting up. https://guytevet.github.io/CLoSD-page/

## 개요
모션 확산 모델과 물리 기반 시뮬레이션을 위한 강화 학습(RL) 기반 제어는 인간 동작 생성에 있어 상호 보완적인 강점을 지닙니다. 전자는 텍스트와 같은 직관적인 제어를 따르며 다양한 동작을 생성할 수 있는 반면, 후자는 물리적으로 타당한 동작과 환경과의 직접적인 상호작용을 제공합니다. 본 연구에서는 각각의 강점을 결합한 방법을 제시합니다. CLoSD는 다양한 작업을 위해 확산 생성을 통해 안내되는 텍스트 기반 RL 물리 제어기입니다. 우리의 핵심 통찰은 동작 확산이 강력한 RL 제어기를 위한 즉석 범용 계획자 역할을 할 수 있다는 것입니다. 이를 위해 CLoSD는 확산 계획자(DiP)와 추적 제어기라는 두 모듈 간의 폐쇄 루프 상호작용을 유지합니다. DiP는 텍스트 프롬프트와 목표 위치에 의해 제어되는 빠르게 응답하는 자기회귀 확산 모델이며, 제어기는 DiP로부터 지속적으로 동작 계획을 수신하고 환경으로부터 피드백을 제공하는 간단하고 강력한 동작 모방기입니다. CLoSD는 목표 위치로의 이동, 텍스트 프롬프트에 지정된 손이나 발로 물체 치기, 앉기, 일어서기 등 일련의 다양한 작업을 원활하게 수행할 수 있습니다. https://guytevet.github.io/CLoSD-page/

## 핵심 내용
모션 확산 모델과 물리 기반 시뮬레이션을 위한 강화 학습(RL) 기반 제어는 인간 동작 생성에 있어 상호 보완적인 강점을 지닙니다. 전자는 텍스트와 같은 직관적인 제어를 따르며 다양한 동작을 생성할 수 있는 반면, 후자는 물리적으로 타당한 동작과 환경과의 직접적인 상호작용을 제공합니다. 본 연구에서는 각각의 강점을 결합한 방법을 제시합니다. CLoSD는 다양한 작업을 위해 확산 생성을 통해 안내되는 텍스트 기반 RL 물리 제어기입니다. 우리의 핵심 통찰은 동작 확산이 강력한 RL 제어기를 위한 즉석 범용 계획자 역할을 할 수 있다는 것입니다. 이를 위해 CLoSD는 확산 계획자(DiP)와 추적 제어기라는 두 모듈 간의 폐쇄 루프 상호작용을 유지합니다. DiP는 텍스트 프롬프트와 목표 위치에 의해 제어되는 빠르게 응답하는 자기회귀 확산 모델이며, 제어기는 DiP로부터 지속적으로 동작 계획을 수신하고 환경으로부터 피드백을 제공하는 간단하고 강력한 동작 모방기입니다. CLoSD는 목표 위치로의 이동, 텍스트 프롬프트에 지정된 손이나 발로 물체 치기, 앉기, 일어서기 등 일련의 다양한 작업을 원활하게 수행할 수 있습니다. https://guytevet.github.io/CLoSD-page/
