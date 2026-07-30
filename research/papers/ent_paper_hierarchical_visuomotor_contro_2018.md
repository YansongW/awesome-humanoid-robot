---
$id: ent_paper_hierarchical_visuomotor_contro_2018
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Hierarchical visuomotor control of humanoids
  zh: Hierarchical visuomotor control of humanoids
  ko: Hierarchical visuomotor control of humanoids
summary:
  en: Hierarchical visuomotor control of humanoids is a 2018 work on physics-based character animation for humanoid robots.
  zh: Hierarchical visuomotor control of humanoids 是2018年关于物理仿真人形机器人角色动画的研究。该工作通过将问题分解为基于本体感觉的低层运动控制和基于视觉的高层技能协调，实现了灵活的任务导向控制。核心贡献在于结合预训练的低层控制器与高层任务控制器，使高自由度人形机器人能够完成需要视觉感知的复杂任务。
  ko: Hierarchical visuomotor control of humanoids is a 2018 work on physics-based character animation for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- hierarchical_visuomotor_contro
- humanoid
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1811.09656v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Hierarchical visuomotor control of humanoids (arXiv)
  url: https://arxiv.org/abs/1811.09656
  date: '2018'
  accessed_at: '2026-07-01'
---
## 概述
该研究旨在构建集感知、运动控制和记忆于一体的复杂人形智能体。通过将问题分解为两个层次：低层运动控制基于本体感觉信号，高层协调则由视觉信息驱动。研究者开发了一种架构，通过预训练低层运动控制器，并结合高层任务导向控制器在不同子策略间切换，实现了对高自由度人形机器人身体的灵活任务导向控制。最终系统能够控制物理仿真人形机器人，在环境中移动时利用未稳定的第一人称RGB摄像头进行视觉感知，并完成相应任务。

## 核心内容
### 方法架构
- 采用层次化控制架构，将问题分解为两个层次：
  - **低层运动控制**：基于本体感觉（proprioception）信号，通过预训练获得基础运动技能
  - **高层协调控制**：由视觉信息驱动，负责在不同低层子策略间切换，实现任务导向控制
- 高层控制器聚焦于任务目标，通过选择适当的低层子策略来协调整体行为

### 实验设置
- 使用物理仿真环境中的高自由度（high-DoF）人形机器人
- 视觉输入来自未稳定的第一人称RGB摄像头（egocentric RGB camera），在机器人移动过程中实时采集
- 系统需在动态环境中完成需要视觉感知耦合的任务

### 关键结果
- 该架构成功实现了对高自由度人形机器人的灵活任务导向运动控制
- 系统能够在移动过程中有效利用未稳定的视觉输入进行感知和决策
- 展示了层次化方法在复杂人形机器人控制中的有效性

### 结论
该研究通过层次化分解方法，将视觉感知与运动控制有效结合，为构建更复杂的人形智能体提供了可行框架。补充视频可参见 https://youtu.be/7GISvfbykLE 。

## Overview
We aim to build complex humanoid agents that integrate perception, motor control, and memory. In this work, we partly factor this problem into low-level motor control from proprioception and high-level coordination of the low-level skills informed by vision. We develop an architecture capable of surprisingly flexible, task-directed motor control of a relatively high-DoF humanoid body by combining pre-training of low-level motor controllers with a high-level, task-focused controller that switches among low-level sub-policies. The resulting system is able to control a physically-simulated humanoid body to solve tasks that require coupling visual perception from an unstabilized egocentric RGB camera during locomotion in the environment. For a supplementary video link, see https://youtu.be/7GISvfbykLE .

## 개요
우리는 지각, 운동 제어 및 기억을 통합하는 복잡한 휴머노이드 에이전트를 구축하는 것을 목표로 합니다. 본 연구에서는 이 문제를 부분적으로 고유 감각에 기반한 저수준 운동 제어와 시각 정보를 활용한 저수준 기술의 고수준 조정으로 분해합니다. 우리는 저수준 운동 제어기의 사전 훈련과 저수준 하위 정책 간 전환을 수행하는 고수준 작업 중심 제어기를 결합하여 비교적 높은 자유도를 가진 휴머노이드 신체의 놀라울 정도로 유연하고 작업 지향적인 운동 제어가 가능한 아키텍처를 개발합니다. 결과 시스템은 물리적으로 시뮬레이션된 휴머노이드 신체를 제어하여 환경 내 이동 중 비안정화된 자기 중심적 RGB 카메라의 시각적 인식을 결합해야 하는 작업을 해결할 수 있습니다. 보충 비디오 링크는 https://youtu.be/7GISvfbykLE 에서 확인할 수 있습니다.

## 핵심 내용
우리는 지각, 운동 제어 및 기억을 통합하는 복잡한 휴머노이드 에이전트를 구축하는 것을 목표로 합니다. 본 연구에서는 이 문제를 부분적으로 고유 감각에 기반한 저수준 운동 제어와 시각 정보를 활용한 저수준 기술의 고수준 조정으로 분해합니다. 우리는 저수준 운동 제어기의 사전 훈련과 저수준 하위 정책 간 전환을 수행하는 고수준 작업 중심 제어기를 결합하여 비교적 높은 자유도를 가진 휴머노이드 신체의 놀라울 정도로 유연하고 작업 지향적인 운동 제어가 가능한 아키텍처를 개발합니다. 결과 시스템은 물리적으로 시뮬레이션된 휴머노이드 신체를 제어하여 환경 내 이동 중 비안정화된 자기 중심적 RGB 카메라의 시각적 인식을 결합해야 하는 작업을 해결할 수 있습니다. 보충 비디오 링크는 https://youtu.be/7GISvfbykLE 에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/1811.09656v2
