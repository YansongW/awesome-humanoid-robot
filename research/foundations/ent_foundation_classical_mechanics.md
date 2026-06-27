---
$id: ent_foundation_classical_mechanics
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: foundation
names:
  en: Classical Mechanics
  zh: 经典力学
  ko: 고전역학
summary:
  en: The branch of physics describing the motion of macroscopic bodies under forces, including Newton's laws, conservation principles, and rigid-body dynamics.
  zh: 描述宏观物体在力作用下运动的物理学分支，包括牛顿定律、守恒原理和刚体动力学。
  ko: 힘을 받는 거시적 물체의 운동을 기술하는 물리학 분야로, 뉴턴의 법칙, 보존 원리, 강체 동역학을 포함한다.
domains:
- 00_foundations
layers:
- foundations
functional_roles:
- knowledge
tags:
- classical_mechanics
- newton_laws
- rigid_body_dynamics
- physics
- humanoid_robot
theoretical_depth:
- foundation
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Foundational domain for robotics.
sources:
- id: src_001
  type: paper
  title: 'Classical Mechanics, Goldstein'
  url: https://www.pearson.com/en-us/subject-catalog/p/classical-mechanics/P200000005792
  date: '2001'
  accessed_at: '2026-06-26'
---

## 抽象

> **生活实例**：扔出去的球会沿抛物线落地，转动的陀螺会保持直立。经典力学就是解释这些日常现象的学问：它用位置、速度、力、能量等概念，预测宏观物体如何运动。
>
> **自然语言逻辑**：牛顿三大定律给出力与加速度的关系；动量和能量守恒给出更宽泛的约束；刚体动力学把这些推广到不能变形的物体（如机器人的连杆）。

## Overview

Classical mechanics provides the physical laws that govern humanoid robot motion. It encompasses kinematics, dynamics, statics, and variational principles. For humanoids, the most relevant subfields are rigid-body dynamics and multi-body dynamics.

## Relevance to Humanoid Robotics

Every controller, simulator, and mechanical design for humanoid robots is built on classical mechanics. It is the deepest foundation of the knowledge graph's engineering branch.
