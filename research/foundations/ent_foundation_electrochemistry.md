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

## Overview
Electrochemistry is a fundamental discipline in the field of humanoid robotics. The following content is compiled from the project Wiki for in-depth reference.

## Content
The energy storage mechanism of lithium-ion batteries is essentially the reversible intercalation/deintercalation of lithium within the crystal lattices of the positive and negative electrode active materials. To understand nominal voltage, rate capability, low-temperature degradation, and aging, one must return to electrochemical thermodynamics and kinetics.

!!! note "Terminology Explanation: Intercalation Reaction, Deintercalation Reaction, Active Material, Electrolyte, Lithium Ion"
    - **Intercalation**: The reversible insertion of lithium ions into a host lattice without destroying its structure.
    - **Deintercalation**: The removal of lithium ions from the host lattice.
    - **Active Material**: The host material in a battery that participates in electrochemical reactions and stores lithium ions.
    - **Electrolyte**: The ionic conductor that conducts lithium ions between the positive and negative electrodes.
    - **Lithium Ion (Li⁺)**: The charge carrier responsible for charge transport in lithium-ion batteries.

**Electrode Potential and the Nernst Equation**. The electrode potential is determined by the chemical potential of lithium in the active material. For intercalation electrodes, the Nernst equation can be written as:

$$
E(x) = E^\circ - \frac{RT}{F} \ln\left( \frac{a_{\mathrm{Li}^+,\mathrm{host}}}{a_{\mathrm{Li}^+}} \right)
$$

where \(E^\circ\) is the standard electrode potential, \(R\) is the gas constant (8.314 J/(mol·K)), \(T\) is the absolute temperature, \(F\) is the Faraday constant (96485 C/mol), and \(a\) is the activity. Under the dilute solution approximation, the electrode potential varies with the lithiation degree \(x\) (i.e., SOC). The open-circuit voltage \(OCV(x)\) is the difference between the positive and negative electrode potentials:

$$
OCV(x) = E_\mathrm{cathode}(x) - E_\mathrm{anode}(x)
$$

For a graphite negative electrode, its potential is very close to that of metallic lithium (approximately 0.05–0.2 V vs Li/Li⁺), so the full cell voltage is primarily determined by the positive electrode material. The plateau potential of LiFePO₄ is about 3.45 V vs Li/Li⁺, while that of NCM (LiNi₀.₈Co₀.₁Mn₀.₁O₂) is about 3.7–3.8 V.

!!! note "Terminology Explanation: Nernst Equation, Electrode Potential, Activity, Open-Circuit Voltage, Potential vs Li/Li⁺"
    - **Nernst Equation**: An equation describing the relationship between electrode potential and the activity of reactants.
    - **Electrode Potential**: The potential of an electrode relative to a reference electrode.
    - **Activity**: The effective concentration, reflecting the chemical potential of ions or atoms in a material.
    - **Open-Circuit Voltage (OCV)**: The terminal voltage of a battery when no external current flows.
    - **Potential vs Li/Li⁺**: The potential relative to a lithium metal reference electrode.

**Butler-Volmer Equation and Polarization**. When a battery discharges, the electrode reaction deviates from equilibrium, generating an overpotential \(\eta\). The Butler-Volmer equation describes the relationship between the charge transfer current density \(j\) and the overpotential:

$$
j = j_0 \left[ \exp\left( \frac{\alpha_a F \eta}{RT} \right) - \exp\left( -\frac{\alpha_c F \eta}{RT} \right) \right]
$$

where \(j_0\) is the exchange current density, and \(\alpha_a, \alpha_c\) are the anodic and cathodic transfer coefficients (typically approximated as \(\alpha_a \approx \alpha_c \approx 0.5\)). In the low overpotential region, it can be linearized as \(j \approx j_0 F \eta / RT\), defining the charge transfer resistance \(R_{ct} = RT / (F j_0)\). During high-rate discharge, both charge transfer polarization and concentration polarization cause a significant drop in terminal voltage and generate Joule heat.

!!! note "Terminology Explanation: Butler-Volmer Equation, Exchange Current Density, Overpotential, Polarization, Charge Transfer Resistance"
    - **Butler-Volmer Equation**: An equation describing the relationship between electrochemical reaction rate and overpotential.
    - **Exchange Current Density**: The magnitude of the forward and reverse reaction current densities at equilibrium, reflecting reaction activity.
    - **Overpotential**: The deviation of the actual electrode potential from the equilibrium potential.
    - **Polarization**: The phenomenon where the electrode potential deviates from the equilibrium value when current flows.
    - **Charge-Transfer Resistance**: The resistance to current flow during the charge transfer step.

**Solid-State Diffusion**. The diffusion of lithium ions inside the active material particles of the positive electrode follows Fick's second law. For a spherical particle with radius \(R_p\), the diffusion time constant can be approximated as:

$$
\tau_D = \frac{R_p^2}{D_{\mathrm{Li}^+}}
$$

where \(D_{\mathrm{Li}^+}\) is the solid-state diffusion coefficient (approximately \(10^{-16}–10^{-14}\ \mathrm{m^2/s}\) for LFP, and \(10^{-13}–10^{-12}\ \mathrm{m^2/s}\) for NCM). If the discharge rate is too fast, the lithium ion concentration on the particle surface becomes depleted while the interior remains lithium-rich, creating concentration polarization and limiting capacity utilization. Reducing particle size, increasing operating temperature, or using materials with high diffusion coefficients can improve rate capability.

!!! note "Terminology Explanation: Fick's Law, Diffusion Coefficient, Diffusion Time Constant, Concentration Polarization"
    - **Fick's Law**: A law describing the diffusion of substances from regions of high concentration to low concentration.
    - **Diffusion Coefficient**: A material parameter characterizing the rate of diffusion.
    - **Diffusion Time Constant**: The characteristic time for a diffusion process to reach equilibrium.
    - **Concentration Polarization**: Polarization caused by a concentration gradient of reactants.

**Formation and Growth of the SEI Film**. During the first charge, the electrolyte is reductively decomposed on the surface of the graphite negative electrode, forming a solid electrolyte interphase (SEI) film. Its main components include Li₂CO₃, LiF, ROCO₂Li, alkyl lithium, etc. The SEI film is an ionic conductor but an electronic insulator, preventing further decomposition of the electrolyte. However, during cycling, the SEI film continuously breaks and reforms, consuming cyclable lithium and thickening, leading to capacity fade and impedance rise. High temperature, high voltage, and fast charging accelerate SEI growth.

!!! note "Terminology Explanation: SEI Film, LiF, Li₂CO₃, Cyclable Lithium, Impedance Growth"
    - **SEI Film (Solid Electrolyte Interphase)**: A protective film formed on the negative electrode surface from the decomposition products of the electrolyte.
    - **LiF / Li₂CO₃**: Common inorganic lithium salt components in the SEI.
    - **Cyclable Lithium**: The total amount of lithium ions available to participate in charge-discharge cycles.
    - **Impedance Growth**: The increase in battery internal resistance with cycling or storage.

**Python Example: Approximating OCV-SOC Curves with the Nernst Equation**. The following code compares the open-circuit voltage variation with SOC for LFP and NCM. Actual OCV-SOC curves also need to consider phase transition plateaus (LFP has a very flat voltage plateau between approximately 20–80% SOC), so an empirical Redlich-Kister expansion is used here for fitting, primarily to demonstrate the potential differences between different positive electrodes.

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

## 개요
전기화학은 휴머노이드 로봇 분야의 중요한 기초 학문입니다. 아래 내용은 프로젝트 Wiki에서 정리한 것으로, 심층적인 참고를 위해 제공됩니다.

## 핵심 내용
리튬이온 배터리의 에너지 저장은 본질적으로 리튬이 양극 및 음극 활물질 격자 내에서 가역적으로 삽입/탈리되는 반응입니다. 공칭 전압, 출력 성능, 저온 열화 및 노화를 이해하려면 전기화학 열역학과 동역학으로 돌아가야 합니다.

!!! note "용어 설명: 삽입 반응, 탈리 반응, 활물질, 전해질, 리튬 이온"
    - **삽입 반응(intercalation)** : 리튬 이온이 결정 구조를 파괴하지 않고 호스트 격자에 가역적으로 삽입되는 반응.
    - **탈리 반응(deintercalation)** : 리튬 이온이 호스트 격자에서 빠져나오는 반응.
    - **활물질(active material)** : 배터리 내에서 전기화학 반응에 참여하여 리튬 이온을 저장하는 주재료.
    - **전해질(electrolyte)** : 양극과 음극 사이에서 리튬 이온을 전도하는 이온 전도체.
    - **리튬 이온(Li⁺)** : 리튬이온 배터리에서 전하 전달을 담당하는 캐리어.

**전극 전위와 네른스트 방정식**. 전극 전위는 활물질 내 리튬의 화학 퍼텐셜에 의해 결정됩니다. 인터칼레이션 전극의 경우 네른스트 방정식은 다음과 같이 쓸 수 있습니다:

$$
E(x) = E^\circ - \frac{RT}{F} \ln\left( \frac{a_{\mathrm{Li}^+,\mathrm{host}}}{a_{\mathrm{Li}^+}} \right)
$$

여기서 \(E^\circ\)는 표준 전극 전위, \(R\)은 기체 상수(8.314 J/(mol·K)), \(T\)는 절대 온도, \(F\)는 패러데이 상수(96485 C/mol), \(a\)는 활성도입니다. 묽은 용액 근사에서 전극 전위는 리튬화 정도 \(x\)(즉 SOC)에 따라 변합니다. 개방 회로 전압 \(OCV(x)\)는 양극과 음극 전위의 차이입니다:

$$
OCV(x) = E_\mathrm{cathode}(x) - E_\mathrm{anode}(x)
$$

흑연 음극의 경우 전위가 금속 리튬에 매우 가깝기 때문에(약 0.05–0.2 V vs Li/Li⁺), 전체 배터리 전압은 주로 양극 재료에 의해 결정됩니다. LiFePO₄의 플랫폼 전위는 약 3.45 V vs Li/Li⁺이고, NCM(LiNi₀.₈Co₀.₁Mn₀.₁O₂)은 약 3.7–3.8 V입니다.

!!! note "용어 설명: 네른스트 방정식, 전극 전위, 활성도, 개방 회로 전압, 리튬 기준 전위"
    - **네른스트 방정식(Nernst equation)** : 전극 전위와 반응물 활성도 간의 관계를 설명하는 방정식.
    - **전극 전위(electrode potential)** : 기준 전극에 대한 전극의 전위.
    - **활성도(activity)** : 유효 농도로, 재료 내 이온 또는 원자의 화학 퍼텐셜을 반영합니다.
    - **개방 회로 전압(open-circuit voltage, OCV)** : 배터리에 외부 전류가 흐르지 않을 때의 단자 전압.
    - **리튬 기준 전위(potential vs Li/Li⁺)** : 리튬 금속 기준 전극에 대한 전위.

**버틀러-볼머 방정식과 분극**. 배터리가 방전될 때 전극 반응은 평형에서 벗어나 과전위 \(\eta\)가 발생합니다. 버틀러-볼머(Butler-Volmer) 방정식은 전하 이동 전류 밀도 \(j\)와 과전위의 관계를 설명합니다:

$$
j = j_0 \left[ \exp\left( \frac{\alpha_a F \eta}{RT} \right) - \exp\left( -\frac{\alpha_c F \eta}{RT} \right) \right]
$$

여기서 \(j_0\)는 교환 전류 밀도, \(\alpha_a, \alpha_c\)는 양극 및 음극 전달 계수(일반적으로 \(\alpha_a \approx \alpha_c \approx 0.5\)로 근사)입니다. 낮은 과전위 영역에서는 \(j \approx j_0 F \eta / RT\)로 선형화할 수 있으며, 전하 이동 저항 \(R_{ct} = RT / (F j_0)\)을 정의합니다. 고율 방전 시 전하 이동 분극과 농도 분극 모두 단자 전압을 크게 낮추고 줄 열을 발생시킵니다.

!!! note "용어 설명: 버틀러-볼머 방정식, 교환 전류 밀도, 과전위, 분극, 전하 이동 저항"
    - **버틀러-볼머 방정식(Butler-Volmer equation)** : 전기화학 반응 속도와 과전위 간의 관계를 설명하는 방정식.
    - **교환 전류 밀도(exchange current density)** : 평형 상태에서 정방향과 역방향 반응 전류 밀도의 크기로, 반응 활성을 나타냅니다.
    - **과전위(overpotential)** : 실제 전극 전위와 평형 전위의 차이.
    - **분극(polarization)** : 전류가 흐를 때 전극 전위가 평형 값에서 벗어나는 현상.
    - **전하 이동 저항(charge-transfer resistance)** : 전하 이동 단계에서 전류에 대한 저항.

**고상 확산**. 리튬 이온이 양극 활물질 입자 내부에서 확산하는 것은 픽의 제2법칙을 따릅니다. 반경이 \(R_p\)인 구형 입자의 경우 확산 시상수는 다음과 같이 근사할 수 있습니다:

$$
\tau_D = \frac{R_p^2}{D_{\mathrm{Li}^+}}
$$

여기서 \(D_{\mathrm{Li}^+}\)는 고상 확산 계수(LFP는 약 \(10^{-16}–10^{-14}\ \mathrm{m^2/s}\), NCM은 약 \(10^{-13}–10^{-12}\ \mathrm{m^2/s}\))입니다. 방전 속도가 너무 빠르면 입자 표면의 리튬 이온 농도가 고갈되고 내부는 여전히 리튬이 풍부하여 농도 분극이 형성되고 용량 발현이 제한됩니다. 입자 크기를 줄이거나, 작동 온도를 높이거나, 확산 계수가 높은 재료를 사용하면 출력 성능을 개선할 수 있습니다.

!!! note "용어 설명: 픽의 법칙, 확산 계수, 확산 시상수, 농도 분극"
    - **픽의 법칙(Fick's law)** : 물질이 고농도 영역에서 저농도 영역으로 확산하는 법칙을 설명합니다.
    - **확산 계수(diffusion coefficient)** : 확산 속도를 나타내는 재료 매개변수.
    - **확산 시상수(diffusion time constant)** : 확산 과정이 평형에 도달하는 특성 시간.
    - **농도 분극(concentration polarization)** : 반응물 농도 구배로 인해 발생하는 분극.

**SEI 막의 형성과 성장**. 첫 충전 시 전해질이 흑연 음극 표면에서 환원 분해되어 고체 전해질 계면막(SEI)을 형성합니다. 주요 성분으로는 Li₂CO₃, LiF, ROCO₂Li, 알킬 리튬 등이 있습니다. SEI 막은 이온 전도체이지만 전자 절연체로, 전해질의 지속적인 분해를 막습니다. 그러나 사이클 과정에서 SEI는 지속적으로 파괴-재구성되며, 활성 리튬을 소모하고 두꺼워져 용량 감소와 임피던스 상승을 초래합니다. 고온, 고전압 및 급속 충전은 SEI 성장을 가속화합니다.

!!! note "용어 설명: SEI 막, LiF, Li₂CO₃, 활성 리튬, 임피던스 증가"
    - **SEI 막(Solid Electrolyte Interphase)** : 음극 표면에 전해질 분해 생성물로 형성된 보호막.
    - **LiF / Li₂CO₃** : SEI에서 흔히 발견되는 무기 리튬 염 성분.
    - **활성 리튬(cyclable lithium)** : 충방전 사이클에 참여할 수 있는 총 리튬 이온 양.
    - **임피던스 증가(impedance growth)** : 사이클 또는 보관에 따라 배터리 내부 저항이 증가하는 현상.

**Python 예제: 네른스트 방정식을 사용한 OCV-SOC 곡선 근사**. 아래 코드는 LFP와 NCM의 개방 회로 전압이 SOC에 따라 어떻게 변하는지 비교합니다. 실제 OCV-SOC 곡선은 상전이 플랫폼(LFP의 경우 약 20–80% SOC에서 전압 플랫폼이 매우 평탄함)을 고려해야 하므로, 여기서는 경험적 Redlich-Kister 전개식을 사용하여 피팅하며, 서로 다른 양극의 전위 차이를 중점적으로 보여줍니다.

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

## Overview
Electrochemistry is a fundamental discipline in the field of humanoid robotics. The following content is compiled from the project Wiki for in-depth reference.

## Content
The energy storage mechanism of lithium-ion batteries essentially involves the reversible intercalation/deintercalation of lithium within the crystal lattices of the positive and negative electrode active materials. Understanding nominal voltage, rate capability, low-temperature degradation, and aging requires revisiting electrochemical thermodynamics and kinetics.

!!! note "Terminology Explanation: Intercalation Reaction, Deintercalation Reaction, Active Material, Electrolyte, Lithium Ion"
    - **Intercalation**: A reaction where lithium ions reversibly insert into a host lattice without destroying its structure.
    - **Deintercalation**: A reaction where lithium ions are extracted from the host lattice.
    - **Active Material**: The host material in a battery that participates in electrochemical reactions and stores lithium ions.
    - **Electrolyte**: An ionic conductor that conducts lithium ions between the positive and negative electrodes.
    - **Lithium Ion (Li⁺)**: The charge carrier responsible for charge transport in lithium-ion batteries.

**Electrode Potential and the Nernst Equation**. The electrode potential is determined by the chemical potential of lithium in the active material. For intercalation electrodes, the Nernst equation can be written as:

$$
E(x) = E^\circ - \frac{RT}{F} \ln\left( \frac{a_{\mathrm{Li}^+,\mathrm{host}}}{a_{\mathrm{Li}^+}} \right)
$$

where \(E^\circ\) is the standard electrode potential, \(R\) is the gas constant (8.314 J/(mol·K)), \(T\) is the absolute temperature, \(F\) is the Faraday constant (96485 C/mol), and \(a\) is the activity. Under the dilute solution approximation, the electrode potential varies with the lithiation degree \(x\) (i.e., SOC). The open-circuit voltage \(OCV(x)\) is the difference between the positive and negative electrode potentials:

$$
OCV(x) = E_\mathrm{cathode}(x) - E_\mathrm{anode}(x)
$$

For a graphite negative electrode, its potential is very close to that of metallic lithium (approximately 0.05–0.2 V vs Li/Li⁺), so the full cell voltage is primarily determined by the positive electrode material. The plateau potential of LiFePO₄ is about 3.45 V vs Li/Li⁺, while that of NCM (LiNi₀.₈Co₀.₁Mn₀.₁O₂) is about 3.7–3.8 V.

!!! note "Terminology Explanation: Nernst Equation, Electrode Potential, Activity, Open-Circuit Voltage, Potential vs Li/Li⁺"
    - **Nernst Equation**: An equation describing the relationship between electrode potential and the activity of reactants.
    - **Electrode Potential**: The electrical potential of an electrode relative to a reference electrode.
    - **Activity**: The effective concentration, reflecting the chemical potential of ions or atoms in a material.
    - **Open-Circuit Voltage (OCV)**: The terminal voltage of a battery when no external current flows.
    - **Potential vs Li/Li⁺**: The potential relative to a lithium metal reference electrode.

**Butler-Volmer Equation and Polarization**. When a battery discharges, the electrode reaction deviates from equilibrium, generating an overpotential \(\eta\). The Butler-Volmer equation describes the relationship between the charge transfer current density \(j\) and the overpotential:

$$
j = j_0 \left[ \exp\left( \frac{\alpha_a F \eta}{RT} \right) - \exp\left( -\frac{\alpha_c F \eta}{RT} \right) \right]
$$

where \(j_0\) is the exchange current density, and \(\alpha_a, \alpha_c\) are the anodic and cathodic transfer coefficients (typically approximated as \(\alpha_a \approx \alpha_c \approx 0.5\)). In the low overpotential region, it can be linearized as \(j \approx j_0 F \eta / RT\), defining the charge transfer resistance \(R_{ct} = RT / (F j_0)\). During high-rate discharge, both charge transfer polarization and concentration polarization cause a significant drop in terminal voltage and generate Joule heat.

!!! note "Terminology Explanation: Butler-Volmer Equation, Exchange Current Density, Overpotential, Polarization, Charge-Transfer Resistance"
    - **Butler-Volmer Equation**: An equation describing the relationship between the electrochemical reaction rate and overpotential.
    - **Exchange Current Density**: The magnitude of the forward and reverse reaction current densities at equilibrium, reflecting reaction activity.
    - **Overpotential**: The deviation of the actual electrode potential from the equilibrium potential.
    - **Polarization**: The phenomenon where the electrode potential deviates from the equilibrium value when current flows.
    - **Charge-Transfer Resistance**: The resistance to current flow from the charge transfer step.

**Solid-State Diffusion**. The diffusion of lithium ions inside the active material particles of the positive electrode follows Fick's second law. For a spherical particle with radius \(R_p\), the diffusion time constant can be approximated as:

$$
\tau_D = \frac{R_p^2}{D_{\mathrm{Li}^+}}
$$

where \(D_{\mathrm{Li}^+}\) is the solid-state diffusion coefficient (LFP approximately \(10^{-16}–10^{-14}\ \mathrm{m^2/s}\), NCM approximately \(10^{-13}–10^{-12}\ \mathrm{m^2/s}\)). If the discharge rate is too fast, the lithium ion concentration at the particle surface becomes depleted while the interior remains lithium-rich, creating concentration polarization and limiting capacity utilization. Reducing particle size, increasing operating temperature, or using materials with high diffusion coefficients can improve rate capability.

!!! note "Terminology Explanation: Fick's Law, Diffusion Coefficient, Diffusion Time Constant, Concentration Polarization"
    - **Fick's Law**: A law describing the diffusion of matter from regions of high concentration to low concentration.
    - **Diffusion Coefficient**: A material parameter characterizing the rate of diffusion.
    - **Diffusion Time Constant**: The characteristic time for a diffusion process to reach equilibrium.
    - **Concentration Polarization**: Polarization caused by a concentration gradient of reactants.

**SEI Film Formation and Growth**. During the first charge, the electrolyte undergoes reductive decomposition on the surface of the graphite negative electrode, forming a Solid Electrolyte Interphase (SEI) film. Its main components include Li₂CO₃, LiF, ROCO₂Li, alkyl lithium, etc. The SEI film is an ionic conductor but an electronic insulator, preventing further decomposition of the electrolyte. However, during cycling, the SEI continuously breaks and reforms, consuming cyclable lithium and thickening, leading to capacity fade and impedance rise. High temperature, high voltage, and fast charging accelerate SEI growth.

!!! note "Terminology Explanation: SEI Film, LiF, Li₂CO₃, Cyclable Lithium, Impedance Growth"
    - **SEI Film (Solid Electrolyte Interphase)**: A protective film formed on the negative electrode surface from the decomposition products of the electrolyte.
    - **LiF / Li₂CO₃**: Common inorganic lithium salt components in the SEI.
    - **Cyclable Lithium**: The total amount of lithium ions available to participate in charge-discharge cycles.
    - **Impedance Growth**: The increase in battery internal resistance with cycling or storage.

**Python Example: Approximating OCV-SOC Curves with the Nernst Equation**. The following code compares the open-circuit voltage variation with SOC for LFP and NCM. Actual OCV-SOC curves also need to consider phase transition plateaus (LFP has a very flat voltage plateau between approximately 20–80% SOC), so an empirical Redlich-Kister expansion is used here for fitting, primarily to demonstrate the potential differences between different positive electrodes.

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
