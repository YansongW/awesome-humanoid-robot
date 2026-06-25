---
$id: ent_continuity_equation
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: equation
names:
  en: Continuity equation
  zh: 连续性方程
  ko: 연속 방정식
summary:
  en: A partial differential equation expressing local conservation of a quantity by equating its rate of change to the negative divergence of its flux.
  zh: 一种偏微分方程，通过将某物理量的变化率等于其通量散度的负值来表达局部守恒。
  ko: 어떤 물리량의 변화율을 그 선속의 발산의 음수와 같게 하여 국소 보존을 표현하는 편미분 방정식.
domains:
- 00_foundations
layers:
- foundations
functional_roles:
- knowledge
theoretical_depth:
- principle
tags:
- conservation
- pde
- continuity_equation
- mass_transport
- probability
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: high
  notes: Standard foundational knowledge; reviewed against standard references.
sources:
- id: src_evans_2010
  type: other
  title: L. C. Evans, Partial Differential Equations, 2nd ed., American Mathematical Society, 2010
  url: https://doi.org/10.1090/gsm/019
  date: '2010-01-01'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_ficks_law
  relationship: builds_on
  description:
    en: Substituting Fick's flux into the continuity equation gives the diffusion equation.
    zh: 将菲克通量代入连续性方程可得到扩散方程。
    ko: 픽의 선속을 연속 방정식에 대입하면 확산 방정식을 얻습니다.
- id: ent_flow_matching
  relationship: is_prerequisite_for
  description:
    en: Flow matching constructs probability paths that satisfy the continuity equation by design.
    zh: 流匹配按设计构造满足连续性方程的概率路径。
    ko: 흐름 매칭은 설계상 연속 방정식을 만족하는 확률 경로를 구성합니다.
- id: ent_ddpm_reverse_process
  relationship: is_prerequisite_for
  description:
    en: The continuous-time probability flow of diffusion models satisfies a Fokker-Planck continuity equation.
    zh: 扩散模型的连续时间概率流满足 Fokker-Planck 连续性方程。
    ko: 확산 모델의 연속 시간 확률 흐름은 포커-플랑크 연속 방정식을 만족합니다.
---

# Continuity equation / 连续性方程 / 연속 방정식

## 抽象

> **生活实例**：想象水流过管道：如果流入某一小段的水多于流出的，该段水位必然上升。连续性方程把这种常识性平衡写成精确的微分表述。
>
> **自然语言逻辑**：连续性方程是守恒律的局部形式。它指出任意微小区域内的物质量变化仅因物质穿过边界流动。若流动具有正散度，物质离开该区域，局部密度减小；反之亦然。

## 形式化定义 / Formal Definition

Let $\rho(\mathbf{x}, t)$ be the density of a conserved scalar quantity and $\mathbf{J}(\mathbf{x}, t)$ its flux. The continuity equation is

$$\frac{\partial \rho}{\partial t} + \nabla \cdot \mathbf{J} = 0.$$

If the quantity is transported with a velocity field $\mathbf{v}$ so that $\mathbf{J} = \rho \mathbf{v}$, the equation becomes

$$\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{v}) = 0,$$

or, using the material derivative,

$$\frac{D\rho}{Dt} + \rho \nabla \cdot \mathbf{v} = 0.$$

In probability form, with $p_t$ a time-dependent probability density and velocity field $u_t$,

$$\frac{\partial p_t}{\partial t} + \nabla \cdot (p_t u_t) = 0.$$

## 关键符号与直觉对应

| 符号 | 名称 | 直觉含义 |
|------|------|----------|
| $\rho$ | 密度 | 单位体积内某物理量的量 |
| $\mathbf{J}$ | 通量 | 单位时间通过单位面积的该物理量 |
| $\nabla \cdot \mathbf{J}$ | 通量散度 | 净流出某点的量 |
| $\mathbf{v}$ | 速度场 | 携带该物理量的介质速度 |
| $\frac{D\rho}{Dt}$ | 物质导数 | 随流体运动的观察者看到的密度变化率 |
| $p_t$ | 概率密度 | 连续时间概率分布的密度函数 |

## 与其他知识点的关系

- `builds_on` → [ent_ficks_law]
- `is_prerequisite_for` → [ent_flow_matching]
- `is_prerequisite_for` → [ent_ddpm_reverse_process]

## 参考文献

1. L. C. Evans, Partial Differential Equations, 2nd ed., American Mathematical Society, 2010
