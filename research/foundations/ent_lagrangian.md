---
$id: ent_lagrangian
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: formalism
names:
  en: Lagrangian
  zh: 拉格朗日量
  ko: 라그랑지안
summary:
  en: A scalar function that encodes the dynamics of a system through the difference (or generalized combination) of kinetic and potential energy, from which equations of motion follow via a variational principle.
  zh: 通过动能与势能之差（或更一般组合）刻画系统动力学，并由变分原理导出运动方程的标量函数。
  ko: 울성 및 위치 에너지의 차이(또는 일반화된 조합)로 시스템 역학을 기술하고 변분 원리로부터 운 동 방정식을 유도하는 스칼라 함수.
domains:
- 00_foundations
layers:
- foundations
functional_roles:
- knowledge
theoretical_depth:
- formalism
tags:
- mechanics
- classical_mechanics
- variational_principle
- lagrangian
- energy
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: high
  notes: Standard foundational knowledge; reviewed against standard references.
sources:
- id: src_goldstein_poole_safko_2002
  type: other
  title: H. Goldstein, C. Poole, and J. Safko, Classical Mechanics, 3rd ed., Addison-Wesley, 2002
  url: https://doi.org/10.2307/2522307
  date: '2002-01-01'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_newton_euler_equations
  relationship: is_alternative_to
  description:
    en: Newton-Euler equations give the same dynamics as the Lagrangian formalism for rigid-body systems, but via force and torque balances.
    zh: 牛顿-欧拉方程与拉格朗日形式对刚体系统给出相同动力学，但直接通过力与力矩平衡列写。
    ko: 뉴턴-오일러 방정식은 강체 시스템에 대해 라그랑지안 형식과 동일한 역학을 주지만 힘과 토크 균형을 통해 직접 유도합니다.
---

# Lagrangian / 拉格朗日量 / 라그랑지안

## 抽象

> **生活实例**：想象滑雪者选择下山最快路线：每个位置下滑速度（动能）与重力势能的取舍决定路线好坏。拉格朗日量就是这种取舍的“记分卡”，真实运动路径是让总得分最小的那条。
>
> **自然语言逻辑**：拉格朗日形式不直接列写力的平衡，而是定义一个标量 L，并追问：在所有想象路径中，哪一条让 L 对时间的积分取驻值？回答这个变分问题即可得到欧拉-拉格朗日方程，它们与牛顿定律等价，但在复杂坐标系中更易推导。

## 形式化定义 / Formal Definition

For a mechanical system with generalized coordinates $q(t)$ and velocities $\dot{q}(t)$, define the Lagrangian

$$\mathcal{L}(q, \dot{q}, t) = T(q, \dot{q}) - V(q, t),$$

where $T$ is kinetic energy and $V$ is potential energy. The equations of motion are the Euler–Lagrange equations:

$$\frac{d}{dt}\frac{\partial \mathcal{L}}{\partial \dot{q}_i} - \frac{\partial \mathcal{L}}{\partial q_i} = 0 \quad (i = 1, \dots, n).$$

For a system with non-conservative generalized forces $Q_i$, the forced form is

$$\frac{d}{dt}\frac{\partial \mathcal{L}}{\partial \dot{q}_i} - \frac{\partial \mathcal{L}}{\partial q_i} = Q_i.$$

## 关键符号与直觉对应

| 符号 | 名称 | 直觉含义 |
|------|------|----------|
| $q_i$ | 广义坐标 | 描述系统位形的独立参数 |
| $\dot{q}_i$ | 广义速度 | 广义坐标对时间的变化率 |
| $T$ | 动能 | 系统由于运动而具有的能量 |
| $V$ | 势能 | 系统由于位形而具有的能量 |
| $\mathcal{L}$ | 拉格朗日量 | 能量差的标量函数，变分核心 |
| $Q_i$ | 广义非保守力 | 不能由势函数导出的力 |

## 与其他知识点的关系

- `is_alternative_to` → [ent_newton_euler_equations]

## 参考文献

1. H. Goldstein, C. Poole, and J. Safko, Classical Mechanics, 3rd ed., Addison-Wesley, 2002
