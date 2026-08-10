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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1811.09656v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (703 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/1811.09656v2

## 개요
이 연구는 지각, 운동 제어 및 기억을 통합한 복잡한 휴머노이드 에이전트 구축을 목표로 합니다. 문제를 두 계층으로 분해하여, 저수준 운동 제어는 고유수용감각 신호에 기반하고, 고수준 조정은 시각 정보에 의해 구동됩니다. 연구자들은 저수준 운동 제어기를 사전 학습하고, 고수준 작업 지향 제어기가 다양한 하위 전략 간 전환을 수행하는 아키텍처를 개발하여, 고자유도 휴머노이드 로봇 신체의 유연한 작업 지향 제어를 구현했습니다. 최종 시스템은 물리 시뮬레이션 휴머노이드 로봇을 제어하며, 환경 내 이동 중 안정화되지 않은 일인칭 RGB 카메라를 활용하여 시각적 지각을 수행하고 해당 작업을 완료합니다.

## 핵심 내용
### 방법 아키텍처
- 계층적 제어 아키텍처를 채택하여 문제를 두 계층으로 분해:
  - **저수준 운동 제어**: 고유수용감각(proprioception) 신호에 기반하며, 사전 학습을 통해 기본 운동 기술 획득
  - **고수준 조정 제어**: 시각 정보에 의해 구동되며, 다양한 저수준 하위 전략 간 전환을 담당하여 작업 지향 제어 구현
- 고수준 제어기는 작업 목표에 초점을 맞추며, 적절한 저수준 하위 전략을 선택하여 전체 행동을 조정

### 실험 설정
- 물리 시뮬레이션 환경의 고자유도(high-DoF) 휴머노이드 로봇 사용
- 시각 입력은 안정화되지 않은 일인칭 RGB 카메라(egocentric RGB camera)에서 제공되며, 로봇 이동 중 실시간으로 수집
- 시스템은 동적 환경에서 시각적 지각과 결합된 작업을 완료해야 함

### 주요 결과
- 이 아키텍처는 고자유도 휴머노이드 로봇의 유연한 작업 지향 운동 제어를 성공적으로 구현
- 시스템은 이동 중 안정화되지 않은 시각 입력을 효과적으로 활용하여 지각 및 의사 결정 수행
- 복잡한 휴머노이드 로봇 제어에서 계층적 접근 방식의 효과성을 입증

### 결론
이 연구는 계층적 분해 방법을 통해 시각적 지각과 운동 제어를 효과적으로 결합하여, 더 복잡한 휴머노이드 에이전트 구축을 위한 실행 가능한 프레임워크를 제공합니다. 추가 비디오는 https://youtu.be/7GISvfbykLE 에서 확인할 수 있습니다.
