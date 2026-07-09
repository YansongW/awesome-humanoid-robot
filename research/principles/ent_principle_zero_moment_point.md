---
$id: ent_principle_zero_moment_point
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: principle
names:
  en: Zero Moment Point (ZMP)
  zh: 零力矩点（ZMP）
  ko: 영모멘트 점(ZMP)
summary:
  en: A point on the ground where the horizontal moment of the ground reaction force about it is zero; widely used as a dynamic
    stability criterion for bipedal walking.
  zh: 地面反作用力水平分力矩为零的地面点，常用于判断双足机器人动态行走的稳定性。
  ko: 지면 반력의 수평 모멘트가 0이 되는 지면 점으로, 이족 보행의 동적 안정성 판단에 널리 사용됨.
domains:
- 06_design_engineering
- 07_ai_models_algorithms
layers:
- midstream
functional_roles:
- knowledge
theoretical_depth:
- principle
tags:
- balance
- locomotion
- biped
- dynamics
- stability
- wiki_gap
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-09'
  confidence: high
  notes: Curated names and summary from data/gap-entity-polish.yaml; placeholder body rewritten. Pending domain-expert final
    review.
sources:
- id: src_vukobratovic_2004_zmp
  type: paper
  title: M. Vukobratović and B. Borovac, Zero-Moment Point — Thirty Five Years of Its Life, IJHR, 2004
  url: https://doi.org/10.1142/S0219843604000083
  date: '2004-03-01'
  accessed_at: '2026-07-09'
- id: src_sardain_bessonnet_2004_zmp
  type: paper
  title: P. Sardain and G. Bessonnet, Forces Acting on a Biped Robot. Center of Pressure—Zero Moment Point, IEEE Trans. SMC-A,
    2004
  url: https://doi.org/10.1109/TSMCA.2004.832811
  date: '2004-09-01'
  accessed_at: '2026-07-09'
related_entities:
- id: ent_formalism_euler_lagrange_equations
  relationship: is_based_on
  description:
    en: The ZMP condition is derived from the moment balance of the robot's equations of motion, commonly expressed via Euler-Lagrange
      or Newton-Euler dynamics.
    zh: ZMP 条件来源于机器人运动方程的力矩平衡，通常由欧拉-拉格朗日方程或牛顿-欧拉动力学表达。
---

# Zero Moment Point / 零力矩点 / 영점

## 抽象

> **生活实例**：人走路时若身体前倾，脚尖会自然踩下去“撑住”身体；ZMP 就是这个“支撑点”在地面上的投影，保证身体不会绕它翻倒。
>
> **自然语言逻辑**：把机器人全身看成一个整体，地面给脚底一个反作用力。如果地面反作用力的合力矩在水平方向上为零，机器人就不会因为水平力矩而倾倒；这个特殊点就叫零力矩点。

## 形式化说明

对于行走机器人，设地面反作用力 $\mathbf{F} = (F_x, F_y, F_z)$ 作用于点 $P$，若关于 $P$ 的力矩水平分量为零：

$$\tau_x = 0, \quad \tau_y = 0,$$

则 $P$ 为 ZMP。当 ZMP 位于支撑多边形（support polygon）内时，机器人具备动态行走的可行性（非翻倒的充分条件之一）。

## 与其他知识点的关系

- `based_on` → [ent_formalism_euler_lagrange_equations]
- `applies_to` → 双足步行 / locomotion
