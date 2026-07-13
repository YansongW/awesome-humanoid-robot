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
  reviewed_at: '2026-07-13'
  confidence: high
  notes: Body populated from Wiki chapter section by scripts/fill_gap_bodies_from_wiki.py; pending human review and translation
    to en/ko.
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
### 8.4.4 零力矩点（ZMP）与动态平衡

**零力矩点（Zero Moment Point, ZMP）**是地面上的一个点，在该点处地面反作用力产生的水平力矩分量为零[43][44]。ZMP 是人形机器人动态平衡的核心判据：若 ZMP 位于支撑多边形（support polygon）内，则机器人理论上不会绕地面边缘倾倒。

!!! note "术语解释：零力矩点（ZMP）、支撑多边形、地面反作用力、动态平衡"
    - **零力矩点（ZMP）**：地面反作用力等效作用点，水平力矩分量为零。
    - **支撑多边形（support polygon）**：脚底与地面接触点构成的凸包。
    - **地面反作用力（GRF）**：地面作用于脚的力。
    - **动态平衡（dynamic balance）**：在运动过程中保持不倾倒的能力。

在简化模型中，假设质心高度 $z_c$ 恒定，ZMP 坐标为：

$$
x_{\text{ZMP}} = x_{\text{CoM}} - \frac{z_c}{g} \ddot{x}_{\text{CoM}}
$$

$$
y_{\text{ZMP}} = y_{\text{CoM}} - \frac{z_c}{g} \ddot{y}_{\text{CoM}}
$$

其中 $g$ 为重力加速度，$\ddot{x}_{\text{CoM}}$、$\ddot{y}_{\text{CoM}}$ 为质心水平加速度。

!!! note "术语解释：质心高度、水平加速度、重力加速度、凸包"
    - **质心高度（CoM height）**：质心到地面的垂直距离。
    - **水平加速度（horizontal acceleration）**：质心在水平面内的加速度分量。
    - **重力加速度（gravitational acceleration）**：$g \approx 9.81\ \text{m/s}^2$。
    - **凸包（convex hull）**：包含一组点的最小凸集。
