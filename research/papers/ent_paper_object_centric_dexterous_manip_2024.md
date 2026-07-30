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
  zh: 这是一项2024年的研究，由作者团队提出，核心贡献是构建了一个分层策略学习框架，利用人类手部运动数据训练灵巧机器人进行以物体为中心的操作。该方法通过高层轨迹生成模型合成类人手腕运动，并结合深度强化学习训练低层手指控制器，在10种日常物体上展现了优越性能和泛化能力。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2411.04005v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
该工作针对人形机器人的灵巧操作问题，提出了一种分层策略学习框架。框架的核心是一个基于大规模人类手部运动捕捉数据集训练的高层轨迹生成模型，该模型能根据目标物体状态生成类人手腕运动。随后，利用深度强化学习训练低层手指控制器，使机器人能基于自身实体与物体物理交互以实现目标。实验在10种日常物体上验证了方法的优越性能，并展示了其对新型物体几何形状和目标状态的泛化能力。此外，研究还将学习到的策略从仿真成功迁移到真实世界的双臂灵巧机器人系统，证明了其实用性。

## 核心内容
### 方法概述
- 提出分层策略学习框架，解决人机手部实体差异（embodiment gap）问题。
- 高层模块：基于大规模人类手部运动捕捉数据集训练轨迹生成模型，合成类人手腕运动，以目标物体状态为条件。
- 低层模块：利用深度强化学习训练手指控制器，使机器人能基于自身实体物理操作物体。

### 实验设置
- 评估对象：10种日常物体，涵盖不同几何形状和操作需求。
- 泛化测试：验证对新型物体几何形状和目标状态的适应能力。
- 真实世界迁移：将仿真中学习的策略部署到真实双臂灵巧机器人系统。

### 关键结果
- 在10种物体上，方法性能显著优于基线。
- 成功泛化到未见过的物体几何形状和目标状态。
- 仿真到真实世界的策略迁移成功，证明了实际应用潜力。

### 结论
该工作通过分层框架有效利用人类运动数据，克服了人机实体差异，为灵巧机器人操作提供了可泛化且实用的解决方案。项目网站提供更多细节：https://cypypccpy.github.io/obj-dex.github.io/。

## Overview
Manipulating objects to achieve desired goal states is a basic but important skill for dexterous manipulation. Human hand motions demonstrate proficient manipulation capability, providing valuable data for training robots with multi-finger hands. Despite this potential, substantial challenges arise due to the embodiment gap between human and robot hands. In this work, we introduce a hierarchical policy learning framework that uses human hand motion data for training object-centric dexterous robot manipulation. At the core of our method is a high-level trajectory generative model, learned with a large-scale human hand motion capture dataset, to synthesize human-like wrist motions conditioned on the desired object goal states. Guided by the generated wrist motions, deep reinforcement learning is further used to train a low-level finger controller that is grounded in the robot's embodiment to physically interact with the object to achieve the goal. Through extensive evaluation across 10 household objects, our approach not only demonstrates superior performance but also showcases generalization capability to novel object geometries and goal states. Furthermore, we transfer the learned policies from simulation to a real-world bimanual dexterous robot system, further demonstrating its applicability in real-world scenarios. Project website: https://cypypccpy.github.io/obj-dex.github.io/.

## 개요
목표 상태를 달성하기 위해 물체를 조작하는 것은 정교한 조작을 위한 기본적이면서도 중요한 기술입니다. 인간의 손 동작은 능숙한 조작 능력을 보여주며, 다중 손가락 로봇을 훈련시키는 데 귀중한 데이터를 제공합니다. 이러한 잠재력에도 불구하고, 인간과 로봇 손 사이의 구현 격차로 인해 상당한 어려움이 발생합니다. 본 연구에서는 인간의 손 동작 데이터를 사용하여 물체 중심의 정교한 로봇 조작을 훈련하는 계층적 정책 학습 프레임워크를 소개합니다. 우리 방법의 핵심은 대규모 인간 손 동작 캡처 데이터셋으로 학습된 고수준 궤적 생성 모델로, 원하는 물체 목표 상태에 따라 인간과 유사한 손목 움직임을 합성합니다. 생성된 손목 움직임에 따라, 심층 강화 학습을 사용하여 로봇의 구현에 기반한 저수준 손가락 제어기를 추가로 훈련시켜 물체와 물리적으로 상호작용하며 목표를 달성합니다. 10가지 가정용 물체에 대한 광범위한 평가를 통해, 우리의 접근 방식은 뛰어난 성능을 보여줄 뿐만 아니라 새로운 물체 형상과 목표 상태에 대한 일반화 능력도 입증합니다. 또한, 학습된 정책을 시뮬레이션에서 실제 양손 정교 로봇 시스템으로 전이하여 실제 시나리오에서의 적용 가능성을 추가로 입증합니다. 프로젝트 웹사이트: https://cypypccpy.github.io/obj-dex.github.io/.

## 핵심 내용
목표 상태를 달성하기 위해 물체를 조작하는 것은 정교한 조작을 위한 기본적이면서도 중요한 기술입니다. 인간의 손 동작은 능숙한 조작 능력을 보여주며, 다중 손가락 로봇을 훈련시키는 데 귀중한 데이터를 제공합니다. 이러한 잠재력에도 불구하고, 인간과 로봇 손 사이의 구현 격차로 인해 상당한 어려움이 발생합니다. 본 연구에서는 인간의 손 동작 데이터를 사용하여 물체 중심의 정교한 로봇 조작을 훈련하는 계층적 정책 학습 프레임워크를 소개합니다. 우리 방법의 핵심은 대규모 인간 손 동작 캡처 데이터셋으로 학습된 고수준 궤적 생성 모델로, 원하는 물체 목표 상태에 따라 인간과 유사한 손목 움직임을 합성합니다. 생성된 손목 움직임에 따라, 심층 강화 학습을 사용하여 로봇의 구현에 기반한 저수준 손가락 제어기를 추가로 훈련시켜 물체와 물리적으로 상호작용하며 목표를 달성합니다. 10가지 가정용 물체에 대한 광범위한 평가를 통해, 우리의 접근 방식은 뛰어난 성능을 보여줄 뿐만 아니라 새로운 물체 형상과 목표 상태에 대한 일반화 능력도 입증합니다. 또한, 학습된 정책을 시뮬레이션에서 실제 양손 정교 로봇 시스템으로 전이하여 실제 시나리오에서의 적용 가능성을 추가로 입증합니다. 프로젝트 웹사이트: https://cypypccpy.github.io/obj-dex.github.io/.

## 参考
- http://arxiv.org/abs/2411.04005v1
