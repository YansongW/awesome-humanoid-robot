---
$id: ent_butler_volmer_equation
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: equation
names:
  en: Butler-Volmer Equation
  zh: Butler-Volmer 方程
  ko: Butler-Volmer 방정식
summary:
  en: Relates the electrochemical reaction current density at an electrode to the activation overpotential and kinetic parameters.
  zh: '> 生活实例：电池充电就像很多人同时挤过一扇旋转门。如果门很窄（活化过电位很大），大家就会挤成一团，人流增长变慢；如果门相对较宽（过电位很小），人流和门的“宽松程度”近似成正比。Butler-Volmer 方程就是精确描述“门宽”（过电位）与“人流”（电流密度）之间非线性关系的公式。
    > > 自然语言逻辑：电极表面同时发生着氧化反应（锂离子离开电极）和还原反应（锂离子嵌入电极）。两种反应的速率都随电势差呈指数变化，但方向相反。净电流密度就是正向电流与反向电流之差；当过电位为零时，两者抵消，净电流为零。方程中的 $j_0$
    表示“门在理想宽度下的通行能力”，$\alpha$ 表示反应对电势变化的敏感程度。'
  ko: 전극 표면의 전류 밀도와 활성화 과전위 및 동역학 매개변수 간의 관계를 기술하는 방정식.
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
- battery
- kinetics
- butler_volmer
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body restructured into standard sections by scripts/restructure_entry_bodies.py.
sources:
- id: src_bard_faulkner_2001
  type: other
  title: 'A. J. Bard and L. R. Faulkner, Electrochemical Methods: Fundamentals and Applications, 2nd ed., Wiley, 2001'
  url: https://www.wiley.com/en-us/Electrochemical+Methods%3A+Fundamentals+and+Applications%2C+2nd+Edition-p-9780471043720
  date: '2001-01-01'
  accessed_at: '2026-06-25'
---

## 概述
# Butler-Volmer 方程

## 核心内容
## 抽象

> **生活实例**：电池充电就像很多人同时挤过一扇旋转门。如果门很窄（活化过电位很大），大家就会挤成一团，人流增长变慢；如果门相对较宽（过电位很小），人流和门的“宽松程度”近似成正比。Butler-Volmer 方程就是精确描述“门宽”（过电位）与“人流”（电流密度）之间非线性关系的公式。
>
> **自然语言逻辑**：电极表面同时发生着氧化反应（锂离子离开电极）和还原反应（锂离子嵌入电极）。两种反应的速率都随电势差呈指数变化，但方向相反。净电流密度就是正向电流与反向电流之差；当过电位为零时，两者抵消，净电流为零。方程中的 $j_0$ 表示“门在理想宽度下的通行能力”，$\alpha$ 表示反应对电势变化的敏感程度。

## 形式化定义

对于单电子转移反应（$n=1$），Butler-Volmer 方程写作：

$$
j = j_0 \left[ \exp\!\left( \frac{\alpha_a n F \eta}{RT} \right) - \exp\!\left( -\frac{\alpha_c n F \eta}{RT} \right) \right].
$$

其中：

- $j$：净电流密度（A/m²）
- $j_0$：交换电流密度
- $\alpha_a, \alpha_c$：阳极、阴极电荷转移系数，通常满足 $\alpha_a + \alpha_c = 1$
- $n$：参与反应的电子数
- $F$：Faraday 常数
- $R$：理想气体常数
- $T$：绝对温度
- $\eta$：活化过电位

交换电流密度可进一步写成：

$$
j_0 = n F k^0 c_R^{\alpha_c} c_O^{\alpha_a},
$$

其中 $k^0$ 为标准速率常数，$c_R, c_O$ 分别为还原态和氧化态物质的浓度。

## 关键符号与直觉对应

| 符号 | 名称 | 直觉含义 |
|------|------|----------|
| $j$ | 净电流密度 | 通过“旋转门”的净人流 |
| $j_0$ | 交换电流密度 | 门在理想宽度下的双向通行能力 |
| $\eta$ | 活化过电位 | 门的“松紧程度” |
| $\alpha_a, \alpha_c$ | 电荷转移系数 | 门对推/拉的敏感程度 |
| $F$ | Faraday 常数 | 一个电子所带的“电荷包”大小 |
| $RT/nF$ | 热电压 | 温度决定的自然电压尺度 |

## 与其他知识点的关系

- `derived_from` → Transition state theory（过渡态理论）
- `has_prerequisite` → Electrochemical kinetics（电化学动力学）
- `has_prerequisite` → Thermodynamics / Nernst equation（热力学 / Nernst 方程）
- `approximates` → Tafel equation（高过电位下的 Tafel 近似）
- `uses` → Faraday constant, gas constant, charge transfer coefficients

## 参考
- [A. J. Bard and L. R. Faulkner, Electrochemical Methods: Fundamentals and Applications, 2nd ed., Wiley, 2001](https://www.wiley.com/en-us/Electrochemical+Methods%3A+Fundamentals+and+Applications%2C+2nd+Edition-p-9780471043720)


