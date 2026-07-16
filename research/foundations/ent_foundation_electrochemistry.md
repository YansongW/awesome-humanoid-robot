---
$id: ent_foundation_electrochemistry
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: foundation
names:
  en: Electrochemistry
  zh: 电化学
  ko: 전기화학
summary:
  en: The foundational science of electron and ion transport across interfaces, governing reactions, potentials, and mass
    transfer in batteries, fuel cells, and corrosion.
  zh: 锂离子电池的能量存储本质上是锂在正负极活性材料晶格中的可逆嵌入/脱嵌反应。要理解标称电压、倍率性能、低温衰减和老化，需要回到电化学热力学与动力学。
  ko: 전지, 연료 전지 및 부식에서 반응, 전위 및 물질 이동을 지배하는 계면을 통한 전자와 이온 전송의 기초 과학이다.
domains:
- 00_foundations
layers:
- foundations
functional_roles:
- knowledge
tags:
- electrochemistry
- ion_transport
- electrode_kinetics
- battery
- humanoid_robot
theoretical_depth:
- foundation
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-06.md#电池电化学基础：电极电位、动力学与扩散 by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_bard_faulkner_2001
  type: other
  title: 'A. J. Bard and L. R. Faulkner, Electrochemical Methods: Fundamentals and Applications, 2nd ed.'
  url: https://www.wiley.com/en-us/Electrochemical+Methods%3A+Fundamentals+and+Applications%2C+2nd+Edition-p-9780471043720
  date: '2001-01-01'
  accessed_at: '2026-06-26'
---

## 概述
电化学是人形机器人领域的重要基础学科。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
锂离子电池的能量存储本质上是锂在正负极活性材料晶格中的可逆嵌入/脱嵌反应。要理解标称电压、倍率性能、低温衰减和老化，需要回到电化学热力学与动力学。

!!! note "术语解释：嵌入反应、脱嵌反应、活性材料、电解液、锂离子"
    - **嵌入反应（intercalation）**：锂离子可逆地插入宿主晶格而不破坏其结构的反应。
    - **脱嵌反应（deintercalation）**：锂离子从宿主晶格中脱出的反应。
    - **活性材料（active material）**：电池中参与电化学反应、存储锂离子的主体材料。
    - **电解液（electrolyte）**：在正负极之间传导锂离子的离子导体。
    - **锂离子（Li⁺）**：锂离子电池中承担电荷传输的载流子。

**电极电位与能斯特方程**。电极电位由活性材料中锂的化学势决定。对于插层电极，能斯特方程可写为：

$$
E(x) = E^\circ - \frac{RT}{F} \ln\left( \frac{a_{\mathrm{Li}^+,\mathrm{host}}}{a_{\mathrm{Li}^+}} \right)
$$

其中 \(E^\circ\) 为标准电极电位，\(R\) 为气体常数（8.314 J/(mol·K)），\(T\) 为绝对温度，\(F\) 为法拉第常数（96485 C/mol），\(a\) 为活度。在稀溶液近似下，电极电位随锂化程度 \(x\)（即 SOC）变化。开路电压 \(OCV(x)\) 就是正负极电位之差：

$$
OCV(x) = E_\mathrm{cathode}(x) - E_\mathrm{anode}(x)
$$

对于石墨负极，其电位非常接近金属锂（约 0.05–0.2 V vs Li/Li⁺），因此全电池电压主要由正极材料决定。LiFePO₄ 的平台电位约为 3.45 V vs Li/Li⁺，NCM（LiNi₀.₈Co₀.₁Mn₀.₁O₂）约为 3.7–3.8 V。

!!! note "术语解释：能斯特方程、电极电位、活度、开路电压、对锂电位"
    - **能斯特方程（Nernst equation）**：描述电极电位与反应物活度之间关系的方程。
    - **电极电位（electrode potential）**：电极相对于参考电极的电势。
    - **活度（activity）**：有效浓度，反映离子或原子在材料中的化学势。
    - **开路电压（open-circuit voltage, OCV）**：电池无外部电流时的端电压。
    - **对锂电位（potential vs Li/Li⁺）**：相对于锂金属参比电极的电位。

**巴特勒-沃尔默方程与极化**。当电池放电时，电极反应偏离平衡，产生过电位 \(\eta\)。巴特勒-沃尔默（Butler-Volmer）方程描述电荷转移电流密度 \(j\) 与过电位的关系：

$$
j = j_0 \left[ \exp\left( \frac{\alpha_a F \eta}{RT} \right) - \exp\left( -\frac{\alpha_c F \eta}{RT} \right) \right]
$$

其中 \(j_0\) 为交换电流密度，\(\alpha_a, \alpha_c\) 为阳极和阴极传递系数（通常近似 \(\alpha_a \approx \alpha_c \approx 0.5\)）。在低过电位区可线性化为 \(j \approx j_0 F \eta / RT\)，定义电荷转移电阻 \(R_{ct} = RT / (F j_0)\)。高倍率放电时，电荷转移极化和浓差极化都会使端电压显著下降，并产生焦耳热。

!!! note "术语解释：巴特勒-沃尔默方程、交换电流密度、过电位、极化、电荷转移电阻"
    - **巴特勒-沃尔默方程（Butler-Volmer equation）**：描述电化学反应速率与过电位关系的方程。
    - **交换电流密度（exchange current density）**：平衡状态下正向与反向反应电流密度的大小，反映反应活性。
    - **过电位（overpotential）**：实际电极电位与平衡电位的偏差。
    - **极化（polarization）**：电流通过时电极电位偏离平衡值的现象。
    - **电荷转移电阻（charge-transfer resistance）**：电荷转移步骤对电流的阻碍。

**固相扩散**。锂离子在正极活性材料颗粒内部的扩散遵循菲克第二定律。对于半径为 \(R_p\) 的球形颗粒，扩散时间常数可近似为：

$$
\tau_D = \frac{R_p^2}{D_{\mathrm{Li}^+}}
$$

其中 \(D_{\mathrm{Li}^+}\) 为固相扩散系数（LFP 约 \(10^{-16}–10^{-14}\ \mathrm{m^2/s}\)，NCM 约 \(10^{-13}–10^{-12}\ \mathrm{m^2/s}\)）。若放电速率过快，颗粒表面锂离子浓度耗尽而内部仍富锂，形成浓差极化并限制容量发挥。减小颗粒尺寸、提高工作温度或采用高扩散系数的材料可改善倍率性能。

!!! note "术语解释：菲克定律、扩散系数、扩散时间常数、浓差极化"
    - **菲克定律（Fick's law）**：描述物质从高浓度区向低浓度区扩散的规律。
    - **扩散系数（diffusion coefficient）**：表征扩散速率的材料参数。
    - **扩散时间常数（diffusion time constant）**：扩散过程达到平衡的特征时间。
    - **浓差极化（concentration polarization）**：由于反应物浓度梯度引起的极化。

**SEI 膜的形成与生长**。首次充电时，电解液在石墨负极表面还原分解，形成固态电解质界面膜（SEI）。其主要成分包括 Li₂CO₃、LiF、ROCO₂Li、烷基锂等。SEI 膜是离子导体但电子绝缘体，能阻止电解液持续分解。然而，在循环过程中 SEI 会不断破裂-重构，消耗活性锂并增厚，导致容量衰减和阻抗上升。高温、高电压和快充会加速 SEI 生长。

!!! note "术语解释：SEI 膜、LiF、Li₂CO₃、活性锂、阻抗增长"
    - **SEI 膜（Solid Electrolyte Interphase）**：负极表面由电解液分解产物形成的保护膜。
    - **LiF / Li₂CO₃**：SEI 中常见的无机锂盐成分。
    - **活性锂（cyclable lithium）**：可参与充放电循环的锂离子总量。
    - **阻抗增长（impedance growth）**：电池内阻随循环或存储而增加的现象。

**Python 算例：用能斯特方程近似 OCV-SOC 曲线**。下面代码对比 LFP 和 NCM 的开路电压随 SOC 的变化。实际 OCV-SOC 曲线还需考虑相变平台（LFP 在约 20–80% SOC 处电压平台非常平坦），因此这里采用经验 Redlich-Kister 展开式拟合，重点展示不同正极的电位差异。

```python
"""
Approximate OCV-SOC curves for LFP and NCM positive electrodes
using a Redlich-Kister expansion. For illustration only.
"""
import numpy as np
import matplotlib.pyplot as plt

R = 8.314      # J/(mol K)
T = 298.15     # K
F = 96485      # C/mol

soc = np.linspace(0.05, 0.95, 200)

## 参考
- [A. J. Bard and L. R. Faulkner, Electrochemical Methods: Fundamentals and Applications, 2nd ed.](https://www.wiley.com/en-us/Electrochemical+Methods%3A+Fundamentals+and+Applications%2C+2nd+Edition-p-9780471043720)
- 项目 Wiki：chapter-06.md#电池电化学基础：电极电位、动力学与扩散


