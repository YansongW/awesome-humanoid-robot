---
$id: ent_paper_zero_moment_point_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Zero Moment Point
  zh: 零力矩点
  ko: Zero Moment Point
summary:
  en: Foundational stability criterion for bipedal walking and balance control.
  zh: 双足行走和平衡控制的基础稳定性判据。
  ko: 이족 보행 및 균형 제어의 기초적 안정성 기준.
domains:
- 07_ai_models_algorithms
- 06_design_engineering
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- bipedal
- control
- method
- stability
- zmp
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body populated from chapter-08.md section "8.4.4 零力矩点（ZMP）与动态平衡" by scripts/backfill_method_bodies_from_wiki.py.
sources:
- id: src_001
  type: website
  title: Zero Moment Point
  url: https://en.wikipedia.org/wiki/Zero_moment_point
  date: '2024'
  accessed_at: '2026-07-02'
---
## 概述
8.4.4 零力矩点（ZMP）与动态平衡相关内容如下。

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

## 参考
- 详见 chapter-08.md。

