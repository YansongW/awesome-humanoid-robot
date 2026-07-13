---
id: ent_component_inspire_micro_linear_actuator
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: 因时机器人微型伺服电缸
  en: Inspire Micro Linear Actuator
sources:
- id: src_inspire_official
  type: website
- title: '"因时机器人官网"'
  url: https://www.inspire-robots.com
- id: src_inspire_manual
  type: website
- title: '"因时机器人微型伺服电缸选型手册"'
  url: https://www.inspire-robots.com/d/file/p/2026/01-14/%E5%BE%AE%E5%9E%8B%E4%BC%BA%E6%9C%8D%E7%94%B5%E7%BC%B8%E9%80%89%E5%9E%8B%E6%89%8B%E5%86%8C%EF%BC%88V18.1%EF%BC%89.pdf
- id: src_inspire_waic_pdf
  type: website
- title: '"因时机器人 WAIC 产品资料"'
  url: https://www.worldrobotconference.com/uploads/exfile/video/yz7f8y.pdf
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from official datasheets, product manuals and verified
    distributors; missing values marked as 未公开.
---


# 因时机器人微型伺服电缸 / Inspire Micro Linear Actuator

## 概述

因时机器人微型伺服电缸是一体化直线伺服执行器，内部集成空心杯无刷电机、精密行星减速器、微型丝杠传动机构、位置/力传感器与闭环伺服驱动器。产品以体积小、精度高、功率密度大、可力控为特点，是仿人五指灵巧手、机器人线性关节、医疗器械与精密夹持的核心驱动部件。

## 工作原理 / 技术架构

电机经减速器驱动丝杠旋转，螺母沿轴向直线运动，实现旋转到直线的转换。导程 $p$ 与电机转速 $n$ 决定推杆线速度：

$$v = \frac{p \cdot n}{60}$$

输出推力 $F$ 与电机扭矩 $T$、减速比 $i$、效率 $\eta$ 的关系为：

$$F = \frac{2\pi \eta T i}{p}$$

内置绝对位置传感器使断电后位置不丢失，LAF/LASF 系列集成力传感器实现推拉力闭环控制。

## 关键参数表

| 参数 | 数值 | 备注 |
|---|---|---|
| 产品系列 | LA / LAF / LAS / LASF / BLA | 因时产品手册 |
| 典型型号 | LA10 | 因时产品手册 |
| 行程 | 10–50 mm（视型号） | 因时产品手册 |
| 重量 | 21–50 g（LA 系列） | 因时产品手册 |
| 工作电压 | DC 8–24 V（视型号） | 因时产品手册 |
| 最大推拉力 | 50–250 N（BLA 系列可达 250 N） | 因时产品手册 |
| 最大速度 | 13–70 mm/s | 因时产品手册 |
| 重复定位精度 | ±0.02–±0.1 mm（BLA 系列 ±2 µm） | 因时产品手册 |
| 通信接口 | PWM / CAN / RS232 / RS485 | 因时产品手册 |
| 防护等级 | IP40（部分型号） | 因时产品手册 |
| 价格 | 未公开 | - |

## 应用场景

仿人五指灵巧手手指驱动、机器人线性关节、医疗精密器械、自适应夹爪、半导体设备、3C 自动化。

## 供应链关系

因时机器人（`ent_company_inspire_robots`）自研微型电机、减速器、丝杠与驱动控制；微型伺服电缸作为其灵巧手 RH56DFX 的核心驱动单元，下游客户覆盖人形机器人整机厂、假肢厂商、医疗器械与科研机构。

## 来源与验证

- 因时机器人官网：https://www.inspire-robots.com
- 微型伺服电缸选型手册：https://www.inspire-robots.com/d/file/p/2026/01-14/%E5%BE%AE%E5%9E%8B%E4%BC%BA%E6%9C%8D%E7%94%B5%E7%BC%B8%E9%80%89%E5%9E%8B%E6%89%8B%E5%86%8C%EF%BC%88V18.1%EF%BC%89.pdf
- WAIC 产品资料：https://www.worldrobotconference.com/uploads/exfile/video/yz7f8y.pdf