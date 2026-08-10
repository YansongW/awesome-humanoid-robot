---
$id: ent_paper_emergent_active_perception_and_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Emergent Active Perception and Dexterity of Simulated Humanoids from Visual Reinforcement Learning
  zh: Emergent Active Perception and Dexterity of Simulated Humanoids from Visual Reinforcement Learning
  ko: Emergent Active Perception and Dexterity of Simulated Humanoids from Visual Reinforcement Learning
summary:
  en: Emergent Active Perception and Dexterity of Simulated Humanoids from Visual Reinforcement Learning is a 2025 work on
    physics-based character animation for humanoid robots.
  zh: Perceptive Dexterous Control (PDC) 是2025年提出的一种基于视觉强化学习的模拟人形机器人框架。它仅依靠第一人称视觉输入实现物体搜索、抓取与放置等灵巧操作，无需3D位置等特权状态信息，并展现出主动感知等涌现行为。
  ko: Emergent Active Perception and Dexterity of Simulated Humanoids from Visual Reinforcement Learning is a 2025 work on
    physics-based character animation for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- emergent_active_perception_and
- humanoid
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.12278v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (534 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Emergent Active Perception and Dexterity of Simulated Humanoids from Visual Reinforcement Learning (arXiv)
  url: https://arxiv.org/abs/2505.12278
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Emergent Active Perception and Dexterity of Simulated Humanoids from Visual Reinforcement Learning project page
  url: https://www.zhengyiluo.com/PDC-Site/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
受人类视觉感知驱动行为的启发，PDC框架将第一人称视觉作为任务接口，使模拟人形机器人能够执行多种家务操作。该框架摒弃了传统的3D物体位置与几何信息，仅通过视觉线索完成物体搜索、目标定位与技能选择。实验表明，从零开始的强化学习训练即可涌现出主动搜索等类人行为，证明了视觉驱动控制与复杂任务之间的闭环关系。

## 核心内容
### 核心方法
- **感知即接口**：PDC将第一人称视觉作为唯一任务规范输入，替代传统方法中依赖的3D物体位置与几何等特权状态信息。
- **灵巧全身控制**：框架支持物体搜索、目标放置与技能选择，通过视觉线索驱动整个控制流程。

### 实验设置
- **训练方式**：从零开始进行强化学习训练，不依赖任何预训练或特权信息。
- **任务范围**：涵盖多种家务操作，包括伸手、抓取、放置以及铰接物体操作。

### 关键发现
- **涌现行为**：训练过程中自然产生了主动搜索等类人行为，验证了视觉驱动控制的有效性。
- **单一策略**：单个策略即可完成多种任务，无需为不同任务分别训练模型。

### 结论
PDC框架展示了视觉驱动控制如何通过感知-动作闭环实现类人行为，为动画、机器人学与具身AI领域提供了关键设计思路。

## Overview
Human behavior is fundamentally shaped by visual perception -- our ability to interact with the world depends on actively gathering relevant information and adapting our movements accordingly. Behaviors like searching for objects, reaching, and hand-eye coordination naturally emerge from the structure of our sensory system. Inspired by these principles, we introduce Perceptive Dexterous Control (PDC), a framework for vision-driven dexterous whole-body control with simulated humanoids. PDC operates solely on egocentric vision for task specification, enabling object search, target placement, and skill selection through visual cues, without relying on privileged state information (e.g., 3D object positions and geometries). This perception-as-interface paradigm enables learning a single policy to perform multiple household tasks, including reaching, grasping, placing, and articulated object manipulation. We also show that training from scratch with reinforcement learning can produce emergent behaviors such as active search. These results demonstrate how vision-driven control and complex tasks induce human-like behaviors and can serve as the key ingredients in closing the perception-action loop for animation, robotics, and embodied AI.

## 参考
- http://arxiv.org/abs/2505.12278v1

## 개요
인간의 시각적 지각이 행동을 유도하는 방식에서 영감을 받은 PDC 프레임워크는 1인칭 시각을 작업 인터페이스로 사용하여 시뮬레이션 휴머노이드 로봇이 다양한 가사 작업을 수행할 수 있게 합니다. 이 프레임워크는 기존의 3D 객체 위치 및 기하학적 정보를 배제하고, 오직 시각적 단서만으로 객체 탐색, 목표 위치 파악, 기술 선택을 완료합니다. 실험 결과, 처음부터 강화 학습 훈련만으로도 능동적 탐색과 같은 인간형 행동이 자연스럽게 나타나며, 시각 기반 제어와 복잡한 작업 간의 폐쇄 루프 관계를 입증했습니다.

## 핵심 내용
### 핵심 방법
- **지각이 곧 인터페이스**: PDC는 1인칭 시각을 유일한 작업 사양 입력으로 사용하며, 기존 방법에서 의존하던 3D 객체 위치 및 기하학과 같은 특권 상태 정보를 대체합니다.
- **민첩한 전신 제어**: 프레임워크는 객체 탐색, 목표 배치, 기술 선택을 지원하며, 시각적 단서를 통해 전체 제어 흐름을 구동합니다.

### 실험 설정
- **훈련 방식**: 사전 훈련이나 특권 정보 없이 처음부터 강화 학습 훈련을 수행합니다.
- **작업 범위**: 손 뻗기, 잡기, 배치, 관절 객체 조작을 포함한 다양한 가사 작업을 다룹니다.

### 주요 발견
- **창발적 행동**: 훈련 과정에서 능동적 탐색과 같은 인간형 행동이 자연스럽게 생성되어 시각 기반 제어의 효과성을 검증했습니다.
- **단일 정책**: 단일 정책만으로도 다양한 작업을 완료할 수 있으며, 작업별로 별도의 모델을 훈련할 필요가 없습니다.

### 결론
PDC 프레임워크는 시각 기반 제어가 지각-행동 폐쇄 루프를 통해 인간형 행동을 어떻게 구현하는지 보여주며, 애니메이션, 로봇공학, 구현 AI 분야에 핵심 설계 통찰을 제공합니다.
