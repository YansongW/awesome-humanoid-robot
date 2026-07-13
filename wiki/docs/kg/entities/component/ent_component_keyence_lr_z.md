---
id: ent_component_keyence_lr_z
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 基恩士 LR-Z 系列 CMOS 激光传感器
  en: Keyence LR-Z Series CMOS Laser Sensor
status: active
sources:
- id: src_keyence_lr_z
  type: website
  url: https://www.keyence.com/products/sensors/laser/lr-z/
- id: src_nexinstrument_lr_zh500cp
  type: website
  url: https://www.nexinstrument.com/lr-zh500p
- id: src_directindustry_lr_z
  type: website
  url: https://www.directindustry.com/prod/keyence/product-64178-828299.html
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 基恩士 LR-Z 系列 CMOS 激光传感器 / Keyence LR-Z Series CMOS Laser Sensor

## 概述

基恩士 LR-Z 系列是放大器内置型 CMOS 激光传感器，将 CMOS 成像元件与激光光源集成于 SUS316L 不锈钢壳体内。该系列支持基于距离、对比度及透明体的检测，具备 U.C.D.（Universal Change Detection）功能和 DATUM 背景抑制能力，对目标颜色、角度及表面光泽变化不敏感，适用于严苛工业环境。

## 工作原理 / 技术架构

LR-Z 通过激光二极管发射 660 nm 红色可见激光，CMOS 接收器采集反射光图像。控制单元利用光功率控制自动调节激光强度，并结合 DATUM 校准实现背景抑制，从而稳定检测不同颜色、材质和角度的目标。检测原理以距离检测为主，部分型号采用时间飞行或三角测距方式。输出为 PNP/NPN 集电极开路，可通过 M8/M12 连接器与 PLC 或机器人 I/O 连接。

## 关键参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品类型 | 放大器内置型 CMOS 激光传感器 | Keyence |
| 代表型号 | LR-ZB100 / LR-ZB250 / LR-ZH500 等 | Keyence |
| 检测距离 | 35–100 mm / 35–250 mm / 35–500 mm | NexInstrument |
| 光源 | 红色激光 660 nm，Class 2 | NexInstrument |
| 光斑直径 | 约 Φ3 mm | NexInstrument |
| 响应时间 | 1.5 / 10 / 50 ms 可选 | NexInstrument |
| 供电电压 | 10–30 VDC | NexInstrument |
| 功耗 | ≤450 mW | NexInstrument |
| 输出方式 | PNP / NPN 集电极开路 | NexInstrument |
| 防护等级 | IP68 / IP69K | DirectIndustry |
| 壳体材料 | SUS316L 不锈钢 | DirectIndustry |
| 显示 | 3 位 7 段 LED | Keyence |

## 应用场景

- 机器人目标检测与定位
- 产线工件有无检测
- 透明/黑色/高反光工件检测
- 包装与物流分拣

## 供应链关系

基恩士（`ent_company_keyence`）设计并制造 LR-Z 系列传感器。上游包括 CMOS 图像传感器、激光二极管、光学镜头、FPGA/ASIC 及不锈钢结构件；下游客户为工厂自动化产线、机器人 OEM 与物流系统集成商。在知识图谱中，`ent_company_keyence` 通过 `manufactures` 关系指向 `ent_component_keyence_lr_z`，该传感器可作为机器人视觉/感知子系统的前端检测单元。

## 来源与验证

- [KEYENCE LR-Z Series Product Page](https://www.keyence.com/products/sensors/laser/lr-z/)
- [Keyence LR-ZH500CP Specifications](https://www.nexinstrument.com/lr-zh500p)
- [DirectIndustry LR-Z Series Overview](https://www.directindustry.com/prod/keyence/product-64178-828299.html)