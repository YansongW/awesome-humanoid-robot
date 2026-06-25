---
$id: ent_newton_euler_equations
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: equation
names:
  en: Newton-Euler equations
  zh: 牛顿-欧拉方程
  ko: 뉴턴-오일러 방정식
summary:
  en: A set of coupled force and torque balance equations that describe the motion of a rigid body or articulated multibody system.
  zh: 描述刚体或铰接多体系统运动的一组耦合的力平衡与力矩平衡方程。
  ko: 강철 또는 관절 연결 다물체 시스템의 운전을 기술하는 결합된 힘 및 토크 평형 방정식 집합.
domains:
- 00_foundations
layers:
- foundations
functional_roles:
- knowledge
theoretical_depth:
- formalism
tags:
- dynamics
- rigid_body
- multibody
- newton_euler
- equations_of_motion
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: high
  notes: Standard foundational knowledge; reviewed against standard references.
sources:
- id: src_featherstone_2014
  type: other
  title: R. Featherstone, Rigid Body Dynamics Algorithms, Springer, 2014
  url: https://doi.org/10.1007/978-1-4899-7560-7
  date: '2014-01-01'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_lagrangian
  relationship: is_alternative_to
  description:
    en: The Newton-Euler and Lagrangian formalisms are equivalent for rigid-body systems; the former emphasizes force/torque balances, the latter emphasizes energy.
    zh: 牛顿-欧拉形式与拉格朗日形式对刚体系统等价；前者强调力/力矩平衡，后者强调能量。
    ko: 뉴턴-오일러 형식과 라그랑지안 형식은 강체 시스템에서 동치입니다. 전자는 힘/토크 균형에, 후자는 에너지에 초점을 맞춥니다.
---

# Newton-Euler equations / 牛顿-欧拉方程 / 뉴턴-오일러 방정식

## 生活实例 + 自然语言阐述逻辑

> **生活实例**：想象把沉重柜子推过房间：你既要克服滑动阻力（力平衡），又要避免倾倒（力矩平衡）。牛顿-欧拉方程同时刻画机器人每个刚体连杆的这两种效应。
>
> **自然语言逻辑**：每个刚体都有线动量与角动量。牛顿第二定律指出线动量的变化率等于合外力；欧拉扩展指出角动量的变化率等于合外力矩。递归地从一个连杆到下一个连杆应用这些平衡，即可得到机器人控制中使用的完整动力学模型。

## 形式化定义 / Formal Definition

For a single rigid body of mass $m$ with center of mass velocity $v$ and angular velocity $\omega$ expressed in a body-fixed frame with inertia tensor $I$:

**Newton's equation (linear momentum balance):**

$$m \dot{v} = \sum f^{\text{ext}}.$$

**Euler's equation (angular momentum balance):**

$$I \dot{\omega} + \omega \times (I \omega) = \sum \tau^{\text{ext}}.$$

For an articulated multibody system with $n$ links, these can be assembled into a recursive or closed-form equation

$$M(q)\ddot{q} + C(q, \dot{q})\dot{q} + g(q) = \tau,$$

where $q \in \mathbb{R}^n$ are generalized coordinates, $M(q)$ is the mass matrix, $C(q, \dot{q})$ captures Coriolis and centrifugal terms, $g(q)$ is gravity, and $\tau$ is the vector of generalized forces/torques.

## 关键符号与直觉对应

| 符号 | 名称 | 直觉含义 |
|------|------|----------|
| $m$ | 质量 | 刚体的总质量 |
| $v$ | 质心速度 | 刚体质心的平动速度 |
| $\omega$ | 角速度 | 刚体绕质心转动的角速度矢量 |
| $I$ | 惯性张量 | 描述质量绕各轴分布的矩阵 |
| $M(q)$ | 质量矩阵 | 广义坐标下的等效惯性矩阵 |
| $\tau$ | 广义力/力矩 | 驱动关节的力或力矩 |

## 与其他知识点的关系

- `is_alternative_to` → [ent_lagrangian]

## 参考文献

1. R. Featherstone, Rigid Body Dynamics Algorithms, Springer, 2014
