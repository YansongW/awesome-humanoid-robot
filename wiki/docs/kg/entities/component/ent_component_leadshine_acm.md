---
id: ent_component_leadshine_acm
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: 雷赛 ACM 系列伺服电机
  en: Leadshine ACM Series Servo Motor
sources:
- id: src_leadshine_official
  type: website
- title: '"雷赛智能官网"'
  url: https://www.leadshine.com
- id: src_leadshine_acm_pdf
  type: website
- title: '"Leadshine ACM Series AC Servo Motors Datasheet"'
  url: https://www.leadshine.com/upfiles/downloads/006a40c553d0c6fc60a1221d6a764222_1675822261873.pdf
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from official datasheets, product manuals and verified
    distributors; missing values marked as 未公开.
---


# 雷赛 ACM 系列伺服电机 / Leadshine ACM Series Servo Motor

## 概述

雷赛 ACM 系列是雷赛智能推出的低压/中压交流伺服电机，额定功率覆盖 50–400 W，机座号 60 mm，适配 ACS/EL 系列伺服驱动器。电机采用稀土永磁转子，具有低齿槽转矩、高过载能力与 3000 rpm 额定转速，广泛应用于工业机器人、人形机器人、数控机床与自动化产线。

## 工作原理 / 技术架构

ACM 系列为三相永磁同步伺服电机，定子电流产生旋转磁场，拖动永磁转子同步旋转。额定扭矩与功率关系为：

$$T_{\text{rated}} = \frac{9.55 P_{\text{rated}}}{n_{\text{rated}}}$$

以 400 W/3000 rpm 为例，$T_{\text{rated}} \approx 1.27\,\text{N·m}$，峰值扭矩可达约 3.8 N·m。标准配置为 1000/2500 线增量编码器（部分型号可选），与雷赛驱动器配套使用。

## 关键参数表

| 参数 | 数值 | 备注 |
|---|---|---|
| 系列 | ACM | 雷赛 |
| 额定功率 | 50–400 W | 产品手册 |
| 额定电压 | 36 / 60 VDC（ACM 低压系列） | 产品手册 |
| 额定转速 | 3000 rpm | 产品手册 |
| 最高转速 | 4000 rpm | 产品手册 |
| 额定扭矩 | 0.318–1.27 N·m | 产品手册 |
| 峰值扭矩 | 0.95–3.82 N·m | 产品手册 |
| 机座号 | 60 mm | 产品手册 |
| 编码器 | 1000/2500 线增量式（可选） | 产品手册 |
| 防护等级 | IP65（部分型号） | 雷赛官网 |
| 绝缘等级 | Class F | 产品手册 |

## 应用场景

工业机器人关节、人形机器人、数控机床、3C 自动化、锂电设备、纺织机械。

## 供应链关系

雷赛智能（`ent_company_leadshine`）制造 ACM 系列电机，并与同厂 L8/L7 伺服驱动器配套销售；上游包括 IGBT、磁材、编码器芯片与 PCB，下游客户覆盖机器人 OEM 与自动化设备商。

## 来源与验证

- 雷赛智能官网：https://www.leadshine.com
- ACM 系列 datasheet：https://www.leadshine.com/upfiles/downloads/006a40c553d0c6fc60a1221d6a764222_1675822261873.pdf