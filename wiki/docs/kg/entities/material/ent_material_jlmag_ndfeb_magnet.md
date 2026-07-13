---
id: ent_material_jlmag_ndfeb_magnet
type: material
domain: 01_raw_materials
theoretical_depth: system
names:
  zh: 金力永磁 高性能烧结钕铁硼磁钢
  en: JL MAG High-Performance Sintered NdFeB Magnet
aliases:
- NdFeB magnet
- 钕铁硼磁钢
- 烧结钕铁硼
status: active
sources:
- id: src_jlmag_official
  type: website
  url: https://www.jlmag.com.cn/
- title: 江西金力永磁科技股份有限公司官网
- id: src_bjmt_ndfeb
  type: website
  url: https://www.bjmt.com.cn/index.php?m=content&c=index&a=lists&catid=13
- title: 烧结钕铁硼磁性能表 - 北京中科三环
- id: src_arnold_neo_catalog
  type: website
  url: https://www.arnoldmagnetics.com/wp-content/uploads/2019/06/Arnold-Neo-Catalog.pdf
- title: Arnold Neodymium Iron Boron Magnet Catalog
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 金力永磁 高性能烧结钕铁硼磁钢 / JL MAG High-Performance Sintered NdFeB Magnet

## 概述

金力永磁高性能烧结钕铁硼磁钢是江西金力永磁科技股份有限公司（JL MAG Rare-Earth Co., Ltd.）生产的第三代稀土永磁材料，以 Nd₂Fe₁₄B 金属间化合物为磁性主相。该材料具有高剩磁、高矫顽力与高最大磁能积，广泛应用于新能源汽车驱动电机、风力发电机、工业伺服电机、节能家电及机器人关节电机等领域。

## 物理化学基础

### 晶体结构与磁性能来源
烧结钕铁硼的磁性主相为四方晶系 Nd₂Fe₁₄B，其高磁性能来源于：

- **高磁晶各向异性**：Nd 原子 3d-4f 电子交换作用产生强磁晶各向异性场；
- **高饱和磁化强度**：Fe 基晶格提供高磁矩；
- **高居里温度**：主相居里温度约 310–370 °C。

关键磁性能参数：

| 参数 | 典型范围（商用 N52 牌号） |
|------|--------------------------|
| 剩磁 $B_r$ | 1.42–1.48 T |
| 磁感矫顽力 $H_{cB}$ | 836–960 kA/m |
| 内禀矫顽力 $H_{cJ}$ | ≥960 kA/m |
| 最大磁能积 $(BH)_{\max}$ | 390–422 kJ/m³（49–53 MGOe） |
| 密度 | 7.3–7.7 g/cm³ |
| 居里温度 $T_c$ | 310–370 °C |
| 剩磁温度系数 $\alpha_{B_r}$ | −0.10% ~ −0.13%/°C |
| 内禀矫顽力温度系数 $\beta_{H_{cJ}}$ | −0.4% ~ −0.7%/°C |

### 本构关系
钕铁硼磁钢的磁化状态可用退磁曲线描述。在第二象限，磁感应强度 $B$ 与磁场强度 $H$ 满足：

$$
B = \mu_0 (H + M)
$$

其中 $M$ 为磁化强度，$\mu_0$ 为真空磁导率。最大磁能积对应于退磁曲线上 $B \cdot H$ 的最大值：

$$
(BH)_{\max} = \max\{B \cdot H\}
$$

### 制备工艺
烧结钕铁硼采用粉末冶金工艺：

1. 合金熔炼与速凝铸片（Strip Casting）；
2. 氢破碎（Hydrogen Decrepitation）；
3. 气流磨制粉（Jet Milling）至 3–5 μm；
4. 磁场取向成型（Transverse Field Pressing）；
5. 冷等静压；
6. 烧结（约 1,080 °C）与回火；
7. 表面处理（电镀镍、环氧涂层等）；
8. 充磁。

### 温度稳定性与重稀土掺杂
通过 Dy、Tb 等重稀土元素掺杂可提高矫顽力与工作温度：

- N 系列：最高工作温度约 80 °C；
- H 系列：约 120 °C；
- SH 系列：约 150 °C；
- UH/EH/TH 系列：可达 180–220 °C。

## 在机器人系统中的作用

- **关节电机磁钢**：为人形机器人、协作机器人、四足机器人的伺服电机提供高扭矩密度永磁励磁；
- **电驱系统**：新能源汽车与机器人关节的 PMSM/BLDC 电机核心材料；
- **传感器与执行器**：磁性编码器、电磁制动器、夹爪驱动；
- **系统影响**：高磁能积直接提升电机转矩密度，降低关节质量与惯量，从而提高机器人动态响应与能效。

电机输出转矩与磁钢性能的关系可近似表示为：

$$
T \propto k_t \cdot \Phi \cdot I
$$

其中 $\Phi$ 为永磁体产生的气隙磁通，$I$ 为电枢电流，$k_t$ 为转矩常数。高 $B_r$ 与高 $(BH)_{\max}$ 可在相同体积下提供更高 $\Phi$，从而提升转矩密度。

## 供应链关系

金力永磁烧结钕铁硼磁钢位于“稀土矿—稀土氧化物—稀土金属—磁材—电机—机器人”链条的中游磁材层：

- **上游**：稀土矿采选、稀土冶炼分离（北方稀土、中国稀土集团等）；
- **中游**：钕铁硼速凝薄带合金、磁粉、烧结磁钢（金力永磁、中科三环、宁波韵升、正海磁材等）；
- **下游**：永磁电机制造商、机器人整机厂商、新能源汽车主机厂、风电整机厂商；
- **应用场景**：机器人关节电机、新能源汽车驱动电机、风力发电机、工业伺服电机。

## 来源与验证

- 金力永磁官网（https://www.jlmag.com.cn/）
- 北京中科三环烧结钕铁硼磁性能表
- Arnold Magnetics Neodymium Iron Boron Catalog

> 注：表中磁性能为 N52 等商用牌号典型值，金力永磁具体产品的完整牌号与实测数据需以其官方 datasheet 为准；表中“典型范围”综合多家头部磁材供应商公开数据。