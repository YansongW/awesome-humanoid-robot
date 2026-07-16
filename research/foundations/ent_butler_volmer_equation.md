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

## Overview
# Butler-Volmer Equation

## Content
## Abstract

> **Life Example**: Charging a battery is like many people squeezing through a revolving door at the same time. If the door is very narrow (large activation overpotential), everyone crowds together and the flow of people slows down; if the door is relatively wide (small overpotential), the flow is approximately proportional to the "looseness" of the door. The Butler-Volmer equation precisely describes the nonlinear relationship between the "door width" (overpotential) and the "flow of people" (current density).
>
> **Natural Language Logic**: On the electrode surface, oxidation (lithium ions leaving the electrode) and reduction (lithium ions embedding into the electrode) occur simultaneously. The rates of both reactions vary exponentially with the potential difference, but in opposite directions. The net current density is the difference between the forward and reverse currents; when the overpotential is zero, they cancel out, resulting in zero net current. In the equation, $j_0$ represents the "passage capacity of the door at ideal width," and $\alpha$ represents the sensitivity of the reaction to potential changes.

## Formal Definition

For a single-electron transfer reaction ($n=1$), the Butler-Volmer equation is written as:

$$
j = j_0 \left[ \exp\!\left( \frac{\alpha_a n F \eta}{RT} \right) - \exp\!\left( -\frac{\alpha_c n F \eta}{RT} \right) \right].
$$

Where:

- $j$: Net current density (A/m²)
- $j_0$: Exchange current density
- $\alpha_a, \alpha_c$: Anodic and cathodic charge transfer coefficients, typically satisfying $\alpha_a + \alpha_c = 1$
- $n$: Number of electrons involved in the reaction
- $F$: Faraday constant
- $R$: Ideal gas constant
- $T$: Absolute temperature
- $\eta$: Activation overpotential

The exchange current density can be further written as:

$$
j_0 = n F k^0 c_R^{\alpha_c} c_O^{\alpha_a},
$$

where $k^0$ is the standard rate constant, and $c_R, c_O$ are the concentrations of the reduced and oxidized species, respectively.

## Key Symbols and Intuitive Correspondence

| Symbol | Name | Intuitive Meaning |
|--------|------|-------------------|
| $j$ | Net current density | Net flow of people through the "revolving door" |
| $j_0$ | Exchange current density | Bidirectional passage capacity of the door at ideal width |
| $\eta$ | Activation overpotential | "Tightness" of the door |
| $\alpha_a, \alpha_c$ | Charge transfer coefficients | Sensitivity of the door to pushing/pulling |
| $F$ | Faraday constant | Size of the "charge packet" carried by one electron |
| $RT/nF$ | Thermal voltage | Natural voltage scale determined by temperature |

## Relationships with Other Knowledge Points

- `derived_from` → Transition state theory
- `has_prerequisite` → Electrochemical kinetics
- `has_prerequisite` → Thermodynamics / Nernst equation
- `approximates` → Tafel equation (Tafel approximation at high overpotential)
- `uses` → Faraday constant, gas constant, charge transfer coefficients

## 개요
# Butler-Volmer 방정식

## 핵심 내용
## 추상

> **생활 예시**: 배터리 충전은 마치 많은 사람들이 동시에 회전문을 통과하는 것과 같습니다. 문이 매우 좁으면(활성화 과전압이 크면) 사람들이 뭉쳐서 인파 증가가 느려집니다. 문이 상대적으로 넓으면(과전압이 매우 작으면) 인파와 문의 "여유 정도"가 거의 비례합니다. Butler-Volmer 방정식은 "문의 너비"(과전압)와 "인파"(전류 밀도) 사이의 비선형 관계를 정밀하게 설명하는 공식입니다.
>
> **자연어 논리**: 전극 표면에서는 산화 반응(리튬 이온이 전극을 떠남)과 환원 반응(리튬 이온이 전극에 삽입됨)이 동시에 발생합니다. 두 반응의 속도는 전위차에 따라 지수적으로 변하지만 방향은 반대입니다. 순 전류 밀도는 정방향 전류와 역방향 전류의 차이입니다. 과전압이 0일 때, 두 전류는 상쇄되어 순 전류는 0이 됩니다. 방정식의 $j_0$는 "이상적인 문 너비에서의 통행 능력"을 나타내고, $\alpha$는 전위 변화에 대한 반응의 민감도를 나타냅니다.

## 형식적 정의

단일 전자 전이 반응($n=1$)의 경우, Butler-Volmer 방정식은 다음과 같이 작성됩니다:

$$
j = j_0 \left[ \exp\!\left( \frac{\alpha_a n F \eta}{RT} \right) - \exp\!\left( -\frac{\alpha_c n F \eta}{RT} \right) \right].
$$

여기서:

- $j$: 순 전류 밀도 (A/m²)
- $j_0$: 교환 전류 밀도
- $\alpha_a, \alpha_c$: 양극, 음극 전하 이동 계수, 일반적으로 $\alpha_a + \alpha_c = 1$을 만족
- $n$: 반응에 참여하는 전자 수
- $F$: 패러데이 상수
- $R$: 이상 기체 상수
- $T$: 절대 온도
- $\eta$: 활성화 과전압

교환 전류 밀도는 다음과 같이 더 쓸 수 있습니다:

$$
j_0 = n F k^0 c_R^{\alpha_c} c_O^{\alpha_a},
$$

여기서 $k^0$는 표준 속도 상수, $c_R, c_O$는 각각 환원 상태와 산화 상태 물질의 농도입니다.

## 주요 기호와 직관적 대응

| 기호 | 이름 | 직관적 의미 |
|------|------|----------|
| $j$ | 순 전류 밀도 | "회전문"을 통과하는 순 인파 |
| $j_0$ | 교환 전류 밀도 | 이상적인 문 너비에서의 양방향 통행 능력 |
| $\eta$ | 활성화 과전압 | 문의 "조임 정도" |
| $\alpha_a, \alpha_c$ | 전하 이동 계수 | 문이 밀기/당기기에 대한 민감도 |
| $F$ | 패러데이 상수 | 하나의 전자가 가진 "전하 패키지" 크기 |
| $RT/nF$ | 열 전압 | 온도에 의해 결정되는 자연 전압 척도 |

## 다른 지식 포인트와의 관계

- `derived_from` → 전이 상태 이론 (Transition state theory)
- `has_prerequisite` → 전기화학 동역학 (Electrochemical kinetics)
- `has_prerequisite` → 열역학 / Nernst 방정식 (Thermodynamics / Nernst equation)
- `approximates` → Tafel 방정식 (고과전압에서의 Tafel 근사)
- `uses` → 패러데이 상수, 기체 상수, 전하 이동 계수
