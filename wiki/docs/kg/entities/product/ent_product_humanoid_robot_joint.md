---
id: ent_product_humanoid_robot_joint
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 人形机器人关节模组
  en: Humanoid Robot Joint Module
status: active
sources:
- id: src_makon_integrated_joint
  type: website
  url: https://www.makongear.com/integrated-joint-actuator-for-humanoid-robots/
- id: src_makon_harmonic_actuators_table
  type: website
  url: https://www.makongear.com/product/harmonic-drive-servo-actuators/
- id: src_honpine_robot_joint
  type: website
  url: https://www.honpine.com/Robot-Joint-Motor.html
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 人形机器人关节模组 / Humanoid Robot Joint Module

## 概述

人形机器人关节模组（Humanoid Robot Joint Module）是将无框力矩电机、谐波/行星减速器、双编码器、制动器与伺服驱动器集成于一体的机电执行单元，是人形机器人实现关节运动、力控与动态平衡的核心部件。作为通用产品类别节点，以下以 Makon 谐波伺服关节模组系列为代表，说明该类产品的关键参数范围与集成方式。

## 工作原理 / 技术架构

关节模组通常采用“电机 + 减速器 + 传感器 + 驱动器”一体化设计。无框力矩电机直接驱动谐波减速器波发生器，经柔轮/刚轮减速后由输出端带动连杆；输出端与电机端各装一只编码器，实现负载侧与电机侧的位置/速度双闭环，并通过电流环估算关节输出力矩。

关节输出力矩由电机电磁转矩经减速器放大：

$$
\tau_{\text{joint}} = \eta \, N \, \tau_{\text{motor}}
$$

其中 $N$ 为减速比，$\eta$ 为传动效率。谐波减速器常见减速比为 51:1、81:1、101:1、121:1、161:1。

关节扭矩密度定义为：

$$
\rho_{\tau} = \frac{\tau_{\text{peak}}}{m_{\text{joint}}}
$$

先进谐波关节模组的扭矩密度可达 100 N·m/kg 以上。

电机输出功率与关节转速的关系为：

$$
P = \tau_{\text{rated}} \cdot \omega_{\text{joint}} = \tau_{\text{rated}} \cdot \frac{2\pi n_{\text{motor}}}{60 \, N}
$$

## 关键参数表

| 参数 | Makon MA-M60-80（上肢/小腿代表） | Makon MA-M110-170（髋/腰重载代表） |
|------|----------------------------------|-----------------------------------|
| 外径 | 60 mm | 110 mm |
| 长度 | 72.5 mm | 121.7 mm |
| 重量 | 0.73 ~ 1.04 kg | 6.84 ~ 6.87 kg |
| 减速比 | 121:1 | 161:1 |
| 峰值扭矩 | 66 N·m | 800 N·m |
| 额定扭矩 | 30 N·m | 363 N·m |
| 中空孔径 | 18 mm | 40 mm |
| 通信总线 | CAN | CAN |
| 编码器 | 单/双编码器可选 | 单/双编码器可选 |
| 扭矩密度 | 约 90 N·m/kg（按 1.04 kg 计算） | 约 116.5 N·m/kg（按 6.87 kg 计算） |
| 重复定位精度 | < 30 arcsec（谐波减速器典型值） | < 30 arcsec（谐波减速器典型值） |

## 应用场景

- 人形机器人肩、肘、腕、腰、髋、膝、踝等全身关节；
- 协作机器人与工业机械臂关节；
- 四足/双足机器人腿部高动态驱动；
- 外骨骼与康复机器人动力关节；
- 高精密伺服转台与定位平台。

## 供应链关系

`ent_product_humanoid_robot_joint` 是集成级产品节点，位于人形机器人产业链中游。其上游依赖 `ent_component_delta_ecma` 等伺服电机、`ent_component_heidenhain_eqi_1131` 等编码器、谐波/行星减速器、力矩传感器、制动器、轴承与壳体；向下装配于人形机器人整机平台，如 `ent_product_unitree_h1`、`ent_product_unitree_g1` 及 `ent_product_tesla_optimus` 等。整机厂商通过运动控制算法与关节模组协同实现机器人动态运动。

## 来源与验证

- Makon Gear 官网“Integrated Joint Actuator for Humanoid Robots”页面详细介绍了 M60、M80、M100、M110 系列关节模组的扭矩密度、重量、中空孔径等参数，并给出 M110-170 峰值扭矩 800 N·m、重量 6.87 kg、扭矩密度约 116.5 N·m/kg 的指标。
- Makon Gear 谐波伺服执行器技术数据页提供了 MA-M60-80、MA-M110-170 等型号的具体尺寸、减速比、扭矩、转速与重量表格。
- HONPINE 官网机器人关节电机页面说明了关节模组集成谐波减速器、无框力矩电机、制动器与编码器的典型架构，并给出谐波减速器常用减速比范围。
- 本条目以 Makon 系列产品为代表值；不同厂商、不同型号的关节模组参数以各自 datasheet 为准。