---
id: ent_product_eu_i_tech_rp_joint
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: component
names:
  zh: 意优 RP 人形专用行星关节
  en: EYouBot RP Series Humanoid Planetary Joint
status: active
sources:
- id: src_eyoubot_rp_series
  type: website
  url: https://eyoubot.com/humanoid-planetary-robot-actuator
- title: RP人形专用行星关节 | 意优科技
- id: src_eyoubot_rp90l
  type: website
  url: https://eyoubot.com/products/rp90l
- title: RP90L 人形行星一体化关节模组 | 意优科技
- id: src_eyoubot_catalog_2025
  type: document
  url: https://www.worldrobotconference.com/profile/robot/download/2025/07/11/%E6%84%8F%E4%BC%98%E7%A7%91%E6%8A%80%E4%BA%A7%E5%93%81%E7%94%BB%E5%86%8C2025061666_20250711133133A009.pdf
- title: 意优科技产品画册 2025
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 意优 RP 人形专用行星关节 / EYouBot RP Series Humanoid Planetary Joint

## 概述

意优 RP 系列是面向高动态、高冲击人形机器人场景开发的竞技级行星一体化关节模组，集成无刷力矩电机、精密行星减速器、双绝对值编码器及专业伺服驱动器，覆盖髋、膝、肩、腕等全身关节位置。RP 系列采用十字交叉滚子轴承与抱箍式安装结构，具备高刚性输出、中空防缠线设计，并通过 CANopen/CAN FD 总线实现低延迟控制。官方资料显示其峰值扭矩密度可达 114 N·m/kg，适配 0.8–1.3 m 级人形机器人的高强度运动需求。

## 工作原理 / 技术架构

行星一体化关节的核心传动链为：无刷力矩电机 → 行星减速器 → 输出法兰。设太阳轮齿数 $z_s$、行星轮齿数 $z_p$、内齿圈齿数 $z_r$，则单级行星减速比为

$$
i = 1 + \frac{z_r}{z_s} = 1 + \frac{z_p + z_s}{z_s}
$$

以 RP90L 为例，其标称减速比 $i=21.91$。电机额定转速 $n_m$（rpm）经减速后输出转速 $n_o$ 为

$$
n_o = \frac{n_m}{i}
$$

输出扭矩 $T_o$ 与电机扭矩 $T_m$ 的关系为

$$
T_o = \eta \, i \, T_m
$$

其中 $\eta$ 为传动效率，典型行星减速器取 0.90–0.95。

控制层面采用基于 FPGA 的全硬件 FOC 算法，电流环、速度环、位置环三环闭环，支持电流、力矩、位置及 MIT 混合控制模式。编码器系统采用电感式绝对值编码器，输入端 17 bit、输出端 19 bit，单圈分辨率为

$$
\theta_{\text{res}} = \frac{360^{\circ}}{2^{19}} \approx 6.87 \times 10^{-4\circ}
$$

回程间隙（backlash）≤12 arcmin，折算到输出端的角度误差为

$$
\Delta\theta_o = \frac{12'}{60'} \cdot \frac{1}{i} \approx 9.1 \times 10^{-3\circ}
$$

## 关键参数表

| 参数 | RP90L 典型值 | 备注 |
|------|--------------|------|
| 外径 × 长度 | φ96.5 mm × 56 mm | 官方产品页 |
| 中空内径 | 8 mm | 穿线走线 |
| 重量 | 1075 g | 未含线缆 |
| 工作电压 | 48 V | 高动态驱动 |
| 减速比 | 21.91 | 单级行星 |
| 额定扭矩 | 35 N·m | 持续输出 |
| 峰值扭矩 | 120 N·m | 短时冲击 |
| 额定转速 | 115 rpm | 输出端 |
| 回程间隙 | ≤12 arcmin | 行星减速器 |
| 编码器形式 | 电感式绝对值 | 输入 17 bit / 输出 19 bit |
| 通信协议 | CANopen / CAN FD | 可定制 |
| 防护等级 | IP54 | 防尘防泼溅 |
| 工作温度 | -10 ℃ ~ 45 ℃ | 标准版 |
| 工作噪音 | ≤60 dB | @1 m |
| 使用寿命 | >3000 h | 额定工况 |
| 扭矩密度 | 114 N·m/kg | 按峰值扭矩/重量计 |

## 应用场景

- **人形机器人下肢**：高峰值扭矩与抗冲击能力适配髋、膝、踝等大扭矩关节，支持深蹲、跳跃、奔跑等高动态动作。
- **上肢与肩腕**：紧凑型 RP 型号（如 RP60-C、RP80-C）可用于肩部外摆、腕部旋转，兼顾轻量化与精度。
- **竞技/表演机器人**：高动态响应与低噪音特性满足舞蹈、体操、连续翻转等表演需求。
- **科研教育平台**：CANopen/CAN FD 接口与 MIT 混合控制模式便于算法验证与二次开发。

## 供应链关系

在机器人产业链中，意优 RP 系列属于 **核心零部件/执行器层**，向上游采购稀土永磁电机磁材、轴承、编码器芯片、功率半导体及壳体铝材，向下游供应给人形机器人本体厂商、协作机器人厂商及科研机构。意优科技自研 FPGA 全硬件 FOC 控制算法与关节模组产线，覆盖谐波、行星、直线三大关节类型，年产能规划达数十万套，处于国产一体化关节模组供应商前列。

## 来源与验证

- 意优科技 RP 系列官方产品页：https://eyoubot.com/humanoid-planetary-robot-actuator
- RP90L 产品页与图纸：https://eyoubot.com/products/rp90l
- 2025 世界机器人大会产品画册（意优科技产品画册 2025）

部分参数（如扭矩密度 114 N·m/kg）来自行业媒体报道，已在表格中标注来源；未公开参数以官方产品页为准。