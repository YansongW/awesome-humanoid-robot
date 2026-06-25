---
$id: ent_ficks_law
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: principle
names:
  en: Fick's law
  zh: 菲克定律
  ko: 픽의 법칙
summary:
  en: A constitutive principle stating that the diffusive flux of a species is proportional to the negative gradient of its concentration.
  zh: 一种本构原理，指出物质的扩散通量与其浓度梯度的负值成正比。
  ko: 종의 확산 선속이 농도 기울기의 음수에 비례한다는 구성 원리.
domains:
- 00_foundations
layers:
- foundations
functional_roles:
- knowledge
theoretical_depth:
- principle
tags:
- diffusion
- mass_transport
- ficks_law
- concentration
- flux
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: high
  notes: Standard foundational knowledge; reviewed against standard references.
sources:
- id: src_crank_1975
  type: other
  title: J. Crank, The Mathematics of Diffusion, 2nd ed., Oxford University Press, 1975
  url: https://doi.org/10.1093/oso/9780198534112.001.0001
  date: '1975-01-01'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_nernst_planck_equation
  relationship: is_prerequisite_for
  description:
    en: The Nernst-Planck equation generalizes Fick's law by adding migration flux due to an electric field.
    zh: 能斯特-普朗克方程在菲克定律基础上增加了电场引起的迁移通量，是其推广。
    ko: 넬스트-플랑크 방정식은 전기장에 의한 이동 선속을 추가하여 픽의 법칙을 일반화합니다.
---

# Fick's law / 菲克定律 / 픽의 법칙

## 抽象

> **生活实例**：想象一列拥挤车厢和旁边的空车厢：人们自然从拥挤侧流向空侧，直到密度平衡。菲克定律指出人流与各地拥挤程度变化的快慢成正比。
>
> **自然语言逻辑**：菲克定律本身不是守恒律，而是驱动力（浓度梯度）与产生的通量之间的唯象关系。将其与连续性方程结合，可得到扩散方程，预测浓度如何随时间平滑化。

## 形式化定义 / Formal Definition

For species concentration $c(\mathbf{x}, t)$, Fick's first law states that the diffusive mass flux $\mathbf{J}$ is

$$\mathbf{J} = -D \nabla c,$$

where $D$ is the diffusion coefficient (tensor in anisotropic media). Fick's second law follows from combining this with the continuity equation $\partial_t c + \nabla \cdot \mathbf{J} = 0$:

$$\frac{\partial c}{\partial t} = \nabla \cdot (D \nabla c).$$

For constant $D$ this simplifies to the standard heat/diffusion equation

$$\frac{\partial c}{\partial t} = D \nabla^2 c.$$

## 关键符号与直觉对应

| 符号 | 名称 | 直觉含义 |
|------|------|----------|
| $c$ | 浓度 | 单位体积内物质的量 |
| $\mathbf{J}$ | 扩散通量 | 单位时间通过单位面积的物质量 |
| $D$ | 扩散系数 | 物质在介质中扩散快慢的度量 |
| $\nabla c$ | 浓度梯度 | 浓度在空间中的变化率 |
| $\nabla \cdot \mathbf{J}$ | 通量散度 | 净流入/流出某区域的物质量 |
| $\nabla^2$ | 拉普拉斯算子 | 空间二阶导数，刻画曲率/扩散 |

## 与其他知识点的关系

- `is_prerequisite_for` → [ent_nernst_planck_equation]

## 参考文献

1. J. Crank, The Mathematics of Diffusion, 2nd ed., Oxford University Press, 1975
