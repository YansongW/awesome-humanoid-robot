---
$id: ent_nernst_planck_equation
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: equation
names:
  en: Nernst-Planck equation
  zh: 能斯特-普朗克方程
  ko: 넬스트-플랑크 방정식
summary:
  en: A transport equation describing the flux of charged species under combined concentration gradients and electric fields, combining diffusion and electromigration.
  zh: 描述带电粒子在浓度梯度与电场共同作用下的通量，融合扩散与电迁移的输运方程。
  ko: 농도 기울기와 전기장이 함께 작용할 때 대전 입자의 선속을 기술하며 확산과 전기 이동을 결합한 수송 방정식.
domains:
- 00_foundations
layers:
- foundations
functional_roles:
- knowledge
theoretical_depth:
- formalism
tags:
- electrochemistry
- ion_transport
- nernst_planck
- diffusion
- migration
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: high
  notes: Standard foundational knowledge; reviewed against standard references.
sources:
- id: src_bard_faulkner_2001
  type: other
  title: 'A. J. Bard and L. R. Faulkner, Electrochemical Methods: Fundamentals and Applications, 2nd ed., Wiley, 2001'
  url: https://doi.org/10.1021/ac0351306
  date: '2001-01-01'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_ficks_law
  relationship: builds_on
  description:
    en: The Nernst-Planck flux extends Fick's law by including an electromigration term.
    zh: 能斯特-普朗克通量在菲克定律基础上增加了电迁移项。
    ko: 넬스트-플랑크 선속은 픽의 법칙에 전기 이동 항을 추가하여 확장합니다.
- id: ent_continuity_equation
  relationship: builds_on
  description:
    en: Together with the continuity equation, the Nernst-Planck flux yields a time-dependent transport equation for ion concentrations.
    zh: 与连续性方程结合，能斯特-普朗克通量给出离子浓度随时间演化的输运方程。
    ko: 연속 방정식과 함께 넬스트-플랑크 선속은 이온 농도의 시간 의존 수송 방정식을 제공합니다.
---

# Nernst-Planck equation / 能斯特-普朗克方程 / 넬스트-플랑크 방정식

## 生活实例 + 自然语言阐述逻辑

> **生活实例**：想象河里的鱼：有些因鱼群密度不均而散开（扩散），有些被水流冲向下游（迁移）。能斯特-普朗克方程把这两种贡献相加得到总鱼流。
>
> **自然语言逻辑**：离子物种的运动有两个原因：热运动平滑浓度梯度（菲克扩散），库仑力驱使带电粒子沿电场线运动（电迁移）。能斯特-普朗克通量将这两种矢量贡献相加。结合电势的泊松方程，它构成用于模拟电池、膜和电解质的泊松-能斯特-普朗克系统。

## 形式化定义 / Formal Definition

For ionic species $i$ with concentration $c_i$, charge number $z_i$, and diffusion coefficient $D_i$, the Nernst-Planck flux is

$$\mathbf{J}_i = -D_i \nabla c_i - \frac{z_i F}{RT} D_i c_i \nabla \phi,$$

where $F$ is Faraday's constant, $R$ the gas constant, $T$ temperature, and $\phi$ the electric potential. The first term is Fickian diffusion; the second is electromigration.

Combined with the continuity equation,

$$\frac{\partial c_i}{\partial t} + \nabla \cdot \mathbf{J}_i = 0,$$

and Poisson's equation for the electrostatic potential,

$$-\nabla \cdot (\varepsilon \nabla \phi) = F \sum_i z_i c_i,$$

we obtain the Poisson-Nernst-Planck (PNP) system.

## 关键符号与直觉对应

| 符号 | 名称 | 直觉含义 |
|------|------|----------|
| $c_i$ | 离子浓度 | 第 i 种离子的摩尔浓度 |
| $z_i$ | 电荷数 | 离子所带基本电荷的倍数 |
| $D_i$ | 扩散系数 | 第 i 种离子的扩散能力 |
| $F$ | 法拉第常数 | 每摩尔电子所带电荷 |
| $\phi$ | 电势 | 空间中的静电势 |
| $\varepsilon$ | 介电常数 | 介质的电容率 |

## 与其他知识点的关系

- `builds_on` → [ent_ficks_law]
- `builds_on` → [ent_continuity_equation]

## 参考文献

1. A. J. Bard and L. R. Faulkner, Electrochemical Methods: Fundamentals and Applications, 2nd ed., Wiley, 2001
