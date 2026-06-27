---
$id: ent_principle_newton_euler_equations
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: principle
names:
  en: Newton-Euler Equations of Motion
  zh: 牛顿-欧拉运动方程
  ko: 뉴턴-오일러 운동 방정식
summary:
  en: The coupled translational and rotational equations that describe how forces and torques produce linear and angular accelerations of a rigid body.
  zh: 描述力和力矩如何产生刚体平动和转动加速度的耦合平移与旋转方程。
  ko: 힘과 토크가 강체의 직선 및 각 가속도를 어떻게 생성하는지 기술하는 결합된 평행이동 및 회전 방정식이다.
domains:
- 00_foundations
- 06_design_engineering
layers:
- foundations
- midstream
functional_roles:
- knowledge
tags:
- newton_euler
- rigid_body_dynamics
- equations_of_motion
- classical_mechanics
- humanoid_control
theoretical_depth:
- principle
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Standard classical-mechanics principle.
sources:
- id: src_001
  type: paper
  title: 'Featherstone, Rigid Body Dynamics Algorithms'
  url: https://www.springer.com/gp/book/9780387743141
  date: '2014'
  accessed_at: '2026-06-26'
related_entities:
- id: ent_foundation_classical_mechanics
  relationship: has_prerequisite
  description:
    en: Newton-Euler equations are derived from Newton's second law and Euler's rotation equations.
    zh: 牛顿-欧拉方程由牛顿第二定律和欧拉旋转方程推导而来。
    ko: 뉴턴-오일러 방정식은 뉴턴의 제2법칙과 오일러 회전 방정식에서 유도된다.
---

## 抽象

> **生活实例**：推一个箱子，箱子会沿推力方向加速；拧一个陀螺，陀螺会绕轴旋转。牛顿-欧拉方程就是把这两种现象写成一个公式：平动部分说“力产生加速度”，转动部分说“力矩产生角加速度”。
>
> **自然语言逻辑**：牛顿第二定律给出平动方程，欧拉方程给出转动方程；两者联立，就能完整描述刚体在力和力矩作用下的运动。

## Overview

The Newton-Euler equations combine Newton's second law for translation and Euler's equation for rotation. For a single rigid body:

```
F = m a
M = I α + ω × I ω
```

where `F` is force, `m` is mass, `a` is linear acceleration, `M` is torque, `I` is the inertia tensor, `α` is angular acceleration, and `ω` is angular velocity.

## Relevance to Humanoid Robotics

These equations are the foundation of floating-base dynamics. Every whole-body controller that respects physics ultimately encodes Newton-Euler principles in its equality constraints.
