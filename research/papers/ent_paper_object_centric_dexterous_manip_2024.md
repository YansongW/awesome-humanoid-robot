---
$id: ent_paper_object_centric_dexterous_manip_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Object-Centric Dexterous Manipulation from Human Motion Data
  zh: Object-Centric Dexterous Manipulation from Human Motion Data
  ko: Object-Centric Dexterous Manipulation from Human Motion Data
summary:
  en: Object-Centric Dexterous Manipulation from Human Motion Data is a 2024 work on manipulation for humanoid robots.
  zh: Object-Centric Dexterous Manipulation from Human Motion Data is a 2024 work on manipulation for humanoid robots.
  ko: Object-Centric Dexterous Manipulation from Human Motion Data is a 2024 work on manipulation for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- manipulation
- object_centric_dexterous_manip
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2411.04005v1.
sources:
- id: src_001
  type: paper
  title: Object-Centric Dexterous Manipulation from Human Motion Data (arXiv)
  url: https://arxiv.org/abs/2411.04005
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Object-Centric Dexterous Manipulation from Human Motion Data project page
  url: https://cypypccpy.github.io/obj-dex.github.io/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Manipulating objects to achieve desired goal states is a basic but important skill for dexterous manipulation. Human hand motions demonstrate proficient manipulation capability, providing valuable data for training robots with multi-finger hands. Despite this potential, substantial challenges arise due to the embodiment gap between human and robot hands. In this work, we introduce a hierarchical policy learning framework that uses human hand motion data for training object-centric dexterous robot manipulation. At the core of our method is a high-level trajectory generative model, learned with a large-scale human hand motion capture dataset, to synthesize human-like wrist motions conditioned on the desired object goal states. Guided by the generated wrist motions, deep reinforcement learning is further used to train a low-level finger controller that is grounded in the robot's embodiment to physically interact with the object to achieve the goal. Through extensive evaluation across 10 household objects, our approach not only demonstrates superior performance but also showcases generalization capability to novel object geometries and goal states. Furthermore, we transfer the learned policies from simulation to a real-world bimanual dexterous robot system, further demonstrating its applicability in real-world scenarios. Project website: https://cypypccpy.github.io/obj-dex.github.io/.

## 核心内容
Manipulating objects to achieve desired goal states is a basic but important skill for dexterous manipulation. Human hand motions demonstrate proficient manipulation capability, providing valuable data for training robots with multi-finger hands. Despite this potential, substantial challenges arise due to the embodiment gap between human and robot hands. In this work, we introduce a hierarchical policy learning framework that uses human hand motion data for training object-centric dexterous robot manipulation. At the core of our method is a high-level trajectory generative model, learned with a large-scale human hand motion capture dataset, to synthesize human-like wrist motions conditioned on the desired object goal states. Guided by the generated wrist motions, deep reinforcement learning is further used to train a low-level finger controller that is grounded in the robot's embodiment to physically interact with the object to achieve the goal. Through extensive evaluation across 10 household objects, our approach not only demonstrates superior performance but also showcases generalization capability to novel object geometries and goal states. Furthermore, we transfer the learned policies from simulation to a real-world bimanual dexterous robot system, further demonstrating its applicability in real-world scenarios. Project website: https://cypypccpy.github.io/obj-dex.github.io/.

## 参考
- http://arxiv.org/abs/2411.04005v1

## Overview
Manipulating objects to achieve desired goal states is a basic but important skill for dexterous manipulation. Human hand motions demonstrate proficient manipulation capability, providing valuable data for training robots with multi-finger hands. Despite this potential, substantial challenges arise due to the embodiment gap between human and robot hands. In this work, we introduce a hierarchical policy learning framework that uses human hand motion data for training object-centric dexterous robot manipulation. At the core of our method is a high-level trajectory generative model, learned with a large-scale human hand motion capture dataset, to synthesize human-like wrist motions conditioned on the desired object goal states. Guided by the generated wrist motions, deep reinforcement learning is further used to train a low-level finger controller that is grounded in the robot's embodiment to physically interact with the object to achieve the goal. Through extensive evaluation across 10 household objects, our approach not only demonstrates superior performance but also showcases generalization capability to novel object geometries and goal states. Furthermore, we transfer the learned policies from simulation to a real-world bimanual dexterous robot system, further demonstrating its applicability in real-world scenarios. Project website: https://cypypccpy.github.io/obj-dex.github.io/.

## Content
Manipulating objects to achieve desired goal states is a basic but important skill for dexterous manipulation. Human hand motions demonstrate proficient manipulation capability, providing valuable data for training robots with multi-finger hands. Despite this potential, substantial challenges arise due to the embodiment gap between human and robot hands. In this work, we introduce a hierarchical policy learning framework that uses human hand motion data for training object-centric dexterous robot manipulation. At the core of our method is a high-level trajectory generative model, learned with a large-scale human hand motion capture dataset, to synthesize human-like wrist motions conditioned on the desired object goal states. Guided by the generated wrist motions, deep reinforcement learning is further used to train a low-level finger controller that is grounded in the robot's embodiment to physically interact with the object to achieve the goal. Through extensive evaluation across 10 household objects, our approach not only demonstrates superior performance but also showcases generalization capability to novel object geometries and goal states. Furthermore, we transfer the learned policies from simulation to a real-world bimanual dexterous robot system, further demonstrating its applicability in real-world scenarios. Project website: https://cypypccpy.github.io/obj-dex.github.io/.

## 개요
목표 상태를 달성하기 위해 물체를 조작하는 것은 정교한 조작을 위한 기본적이면서도 중요한 기술입니다. 인간의 손 동작은 능숙한 조작 능력을 보여주며, 다중 손가락 로봇을 훈련시키는 데 귀중한 데이터를 제공합니다. 이러한 잠재력에도 불구하고, 인간과 로봇 손 사이의 구현 격차로 인해 상당한 어려움이 발생합니다. 본 연구에서는 인간의 손 동작 데이터를 사용하여 물체 중심의 정교한 로봇 조작을 훈련하는 계층적 정책 학습 프레임워크를 소개합니다. 우리 방법의 핵심은 대규모 인간 손 동작 캡처 데이터셋으로 학습된 고수준 궤적 생성 모델로, 원하는 물체 목표 상태에 따라 인간과 유사한 손목 움직임을 합성합니다. 생성된 손목 움직임에 따라, 심층 강화 학습을 사용하여 로봇의 구현에 기반한 저수준 손가락 제어기를 추가로 훈련시켜 물체와 물리적으로 상호작용하며 목표를 달성합니다. 10가지 가정용 물체에 대한 광범위한 평가를 통해, 우리의 접근 방식은 뛰어난 성능을 보여줄 뿐만 아니라 새로운 물체 형상과 목표 상태에 대한 일반화 능력도 입증합니다. 또한, 학습된 정책을 시뮬레이션에서 실제 양손 정교 로봇 시스템으로 전이하여 실제 시나리오에서의 적용 가능성을 추가로 입증합니다. 프로젝트 웹사이트: https://cypypccpy.github.io/obj-dex.github.io/.

## 핵심 내용
목표 상태를 달성하기 위해 물체를 조작하는 것은 정교한 조작을 위한 기본적이면서도 중요한 기술입니다. 인간의 손 동작은 능숙한 조작 능력을 보여주며, 다중 손가락 로봇을 훈련시키는 데 귀중한 데이터를 제공합니다. 이러한 잠재력에도 불구하고, 인간과 로봇 손 사이의 구현 격차로 인해 상당한 어려움이 발생합니다. 본 연구에서는 인간의 손 동작 데이터를 사용하여 물체 중심의 정교한 로봇 조작을 훈련하는 계층적 정책 학습 프레임워크를 소개합니다. 우리 방법의 핵심은 대규모 인간 손 동작 캡처 데이터셋으로 학습된 고수준 궤적 생성 모델로, 원하는 물체 목표 상태에 따라 인간과 유사한 손목 움직임을 합성합니다. 생성된 손목 움직임에 따라, 심층 강화 학습을 사용하여 로봇의 구현에 기반한 저수준 손가락 제어기를 추가로 훈련시켜 물체와 물리적으로 상호작용하며 목표를 달성합니다. 10가지 가정용 물체에 대한 광범위한 평가를 통해, 우리의 접근 방식은 뛰어난 성능을 보여줄 뿐만 아니라 새로운 물체 형상과 목표 상태에 대한 일반화 능력도 입증합니다. 또한, 학습된 정책을 시뮬레이션에서 실제 양손 정교 로봇 시스템으로 전이하여 실제 시나리오에서의 적용 가능성을 추가로 입증합니다. 프로젝트 웹사이트: https://cypypccpy.github.io/obj-dex.github.io/.
