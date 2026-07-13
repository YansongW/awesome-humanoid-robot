---
id: ent_component_ati_mini45
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: ATI Mini45 六维力/力矩传感器
  en: ATI Mini45 Force/Torque Sensor
sources:
- id: src_ati_official
  type: website
- title: '"ATI Mini45 产品页"'
  url: https://ati.novanta.com/product/mini45-force-torque-sensor/
- id: src_ati_manual
  type: website
- title: '"ATI F/T Sensor DAQ Manual"'
  url: https://www.ati-ia.com/app_content/documents/9610-05-1017%20DAQ.pdf
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from official datasheets, product manuals and verified
    distributors; missing values marked as 未公开.
---


# ATI Mini45 六维力/力矩传感器 / ATI Mini45 Force/Torque Sensor

## 概述

ATI Mini45 是 ATI Industrial Automation 推出的微型六维力/力矩传感器，可同时测量三个正交力分量（Fx、Fy、Fz）和三个正交力矩分量（Tx、Ty、Tz）。传感器采用高屈服强度不锈钢电火花线切割本体与硅应变计，具有高信噪比、高刚度与超高过载能力，广泛用于机器人装配、打磨、抛光、医疗手术机器人与人机交互研究。

## 工作原理 / 技术架构

传感器弹性体在受力时产生微小形变，贴附其上的硅应变计电阻变化经惠斯通电桥转换为电压信号。ATI 通过出厂标定建立 6×6 解耦矩阵 $C$，将六路原始电压 $V$ 映射为六维力/力矩 $W$：

$$W = C \cdot V$$

硅应变计输出信号约为传统箔式应变计的 75 倍，经放大后噪声极低。Mini45 提供模拟 ±10 V、EtherCAT、CAN 等多种输出接口，支持 IP65/IP68 版本可选。

## 关键参数表

| 参数 | 数值 | 备注 |
|---|---|---|
| 测量轴数 | 6（Fx/Fy/Fz/Tx/Ty/Tz） | 官方 datasheet |
| 直径 | 45 mm | 官方 datasheet |
| 高度 | 15.7 mm | 官方 datasheet |
| 重量 | 约 91.7 g | 官方 datasheet |
| Fx/Fy 力量程 | ±580 N | SI-580-20 标定 |
| Fz 力量程 | ±1160 N | SI-580-20 标定 |
| Tx/Ty/Tz 力矩量程 | ±20 Nm | SI-580-20 标定 |
| Fx/Fy 分辨率 | 0.25 N | 官方 datasheet |
| Fz 分辨率 | 0.25 N | 官方 datasheet |
| 扭矩分辨率 | 0.003–0.005 Nm | 官方 datasheet |
| 单轴过载 | 5.7–25.3 倍额定量程 | 官方 datasheet |
| 共振频率 | 5400–5600 Hz | 官方 datasheet |
| 精度 | 0.75–1.25% FS | 官方 datasheet |
| 防护等级 | IP20（标准）；IP65/IP68 可选 | 官方 datasheet |

## 应用场景

协作机器人装配、机器人打磨/抛光、质量检测、医疗手术机器人、人形机器人手腕/脚踝力控、力反馈研究。

## 供应链关系

ATI Industrial Automation（`ent_company_ati`，Novanta 子公司）制造 Mini45；上游包括高强度不锈钢、硅应变计与信号调理电路；下游客户包括 FANUC、协作机器人与人形机器人 OEM，与 OnRobot、Robotiq、宇立仪器、坤维科技等竞争。

## 来源与验证

- ATI Mini45 产品页：https://ati.novanta.com/product/mini45-force-torque-sensor/
- ATI F/T DAQ 手册：https://www.ati-ia.com/app_content/documents/9610-05-1017%20DAQ.pdf