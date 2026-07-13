---
id: ent_component_magnetic_steel
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 磁钢（电工钢/硅钢）
  en: Magnetic Steel (Electrical Steel / Silicon Steel)
status: active
sources:
- id: src_ent_component_magnetic_steel_1
  type: website
  url: https://www.ruixinmould.com/news/industry-news/magnetic-steel-motor-how-lamination-drives-efficiency.html
- id: src_ent_component_magnetic_steel_2
  type: website
  url: https://www.gneesiliconsteel.com/blog/silicon-steel-lamination-properties.html
- id: src_ent_component_magnetic_steel_3
  type: website
  url: https://library.wolfram.com/infocenter/technotes/5142/magneticabook_letter.pdf
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 磁钢（电工钢/硅钢）

## 概述

磁钢，工业上通常指电工钢（electrical steel）或硅钢（silicon steel），是以铁为基体、加入适量硅及其他微量元素的软磁合金。其突出特征为高的磁导率、低的矫顽力与可控的铁损，广泛用于电机定子/转子铁心、变压器铁心及电感磁路。在人形机器人产业链中，磁钢是伺服电机、无框力矩电机与空心杯电机铁心的核心材料，直接决定电机效率、转矩密度与热损耗水平。

## 工作原理 / 技术架构

磁钢在交变磁场中的性能可用磁化曲线与损耗模型描述。其高磁导率 $\mu$ 使磁通易于集中通过定转子铁心，从而提高气隙磁密 $B_g$，电机电磁转矩可近似表示为

$$
T \propto B_g \cdot A_{gap} \cdot r \cdot I
$$

其中 $A_{gap}$ 为气隙有效面积，$r$ 为转子半径，$I$ 为电枢电流。

为降低交变磁通感应的涡流损耗，电机铁心采用薄板叠片结构。单片硅钢厚度 $t$ 通常为 0.35 mm 或 0.50 mm，叠片间涂覆绝缘层以切断涡流通路。涡流损耗近似与频率 $f$、磁密幅值 $B_m$ 及片厚平方成正比：

$$
P_e \propto \frac{(B_m f t)^2}{\rho}
$$

硅的加入使电阻率 $\rho$ 从纯铁的约 10 µΩ·cm 提高到 20–60 µΩ·cm，从而显著降低涡流损耗。总铁心损耗可分解为磁滞损耗与涡流损耗：

$$
P_{core} = P_h + P_e = k_h f B_m^n + k_e (f B_m t)^2 / \rho
$$

其中 $k_h$、$k_e$ 为材料常数，$n$ 通常为 1.6–2.0。非取向硅钢（non-oriented）用于旋转电机，因其磁性能各向同性；取向硅钢（grain-oriented）用于变压器，沿轧制方向具有更低铁损与更高磁导率。

## 关键参数表

| 参数项 | 典型值 | 备注/来源 |
|--------|--------|-----------|
| 材料类型 | 非取向硅钢 / 取向硅钢 | 电机多用非取向型 |
| 硅含量 | 1.5–3.5 wt%（商用电机钢）；最高 6.5 wt%（高频低噪声专用） | Ruixin Mould / Magnetica |
| 饱和磁感应强度 $B_s$ | 1.9–2.0 T（普通硅钢）；>2.3 T（钴铁合金） | Magnetica SiSteel3 数据 |
| 电阻率 $\rho$ | 10–60 µΩ·cm | 随硅含量增加而提高 |
| 相对磁导率 $\mu_r$ | 峰值可达 5,000–9,000 | Magnetica 典型曲线 |
| 叠片厚度 | 0.35 mm / 0.50 mm / 0.65 mm | IEC 标准牌号 |
| 铁损等级（IEC） | M270-35A：≤2.70 W/kg @1.5T/50Hz；M400-50A：≤4.00 W/kg | Ruixin Mould |
| 矫顽力 $H_c$ | 低（软磁特性，典型 <100 A/m） | 未公开具体批次值 |
| 价格 | 未公开 | 随牌号、厚度与采购量波动 |

## 应用场景

- **人形机器人伺服电机**：作为无框力矩电机、谐波减速一体化关节的铁心材料，影响峰值扭矩密度与连续运行温升。
- **无人机云台与精密电机**：高转速场景下低铁损硅钢可降低涡流发热。
- **变压器与电感**：取向硅钢用于功率变换器磁心，提高能量转换效率。
- **新能源汽车驱动电机**：高牌号非取向硅钢（如 35W300、20WTG1500）是提升电机效率的关键。

## 供应链关系

在“公司—产品—零部件”网络中，磁钢位于原材料层级。上游为宝武、JFE、新日铁、Posco 等钢铁企业；中游为电机铁心冲压/激光切割与电机制造商（如汇川、安川、MinebeaMitsumi、灵宝 CASBOT 自研关节团队）；下游进入机器人整机（如 CASBOT 01、LimX Oli 等）的驱动系统。磁钢的性能参数通常由电机制造商在定制叠片时指定，最终通过电机产品进入机器人整机供应链。

## 来源与验证

- 磁钢牌号与铁损数据参考 Ruixin Mould《Magnetic Steel Motor: How Lamination Drives Efficiency》及 Gnee Silicon Steel 技术资料。
- 典型磁性能（饱和磁化强度、磁导率峰值）取自 Wolfram Magnetica User Book 中 SiSteel3 示例。
- 硅含量与电阻率关系为材料科学公开数据；具体机器人电机所用磁钢牌号多由厂商保密，未公开项已标注。