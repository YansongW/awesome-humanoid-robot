---
$id: ent_foundation_linear_algebra
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: foundation
names:
  en: Linear Algebra
  zh: 线性代数
  ko: 선형대수학
summary:
  en: The branch of mathematics concerning vector spaces, linear transformations, matrices, and systems of linear equations.
  zh: 研究向量空间、线性变换、矩阵和线性方程组的数学分支。
  ko: 벡터 공간, 선형 변환, 행렬, 선형 방정식 체계를 다루는 수학 분야이다.
domains:
- 00_foundations
layers:
- foundations
functional_roles:
- knowledge
tags:
- linear_algebra
- matrices
- vector_spaces
- jacobian
- humanoid_robot
theoretical_depth:
- foundation
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Foundational for robotics and machine learning.
sources:
- id: src_001
  type: paper
  title: 'Strang, Introduction to Linear Algebra'
  url: https://math.mit.edu/~gs/linearalgebra/
  date: '2016'
  accessed_at: '2026-06-26'
---

## 抽象

> **生活实例**：解一组线性方程就像调配几种原料的配方。线性代数告诉你如何把“每种原料有多少”写成表格（矩阵），把“想要的效果”写成向量，然后通过行变换或求逆快速算出配方。
>
> **自然语言逻辑**：向量表示物理量（力、速度），矩阵表示线性映射（如 Jacobian、旋转矩阵）；线性方程组 `Ax = b` 的解给出未知量；特征值和奇异值分解揭示系统的内在结构。

## Overview

Linear algebra is the language of modern robotics and machine learning. It provides the tools to represent transformations, solve systems, and analyze stability. In humanoid robotics, it appears in kinematics, dynamics, optimization, and learning.

## Relevance to Humanoid Robotics

Jacobians, inertia matrices, QP KKT systems, and neural-network weight matrices are all linear-algebra objects. A solid grasp of linear algebra is necessary to read and implement humanoid control and learning algorithms.
