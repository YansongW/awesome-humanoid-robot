---
id: ent_component_step_low_voltage_servo
schema_version: 1
type: component
'title:': 低压伺服系统
domain: 02_components
theoretical_depth: system
names:
  zh: 低压伺服系统
  en: Step Low-Voltage Servo System
status: active
sources:
- id: src_step_low_voltage_servo_official
  type: website
  url: https://www.kinco.cn
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 低压伺服系统 / Step Low-Voltage Servo System

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [步科股份 / Step Automation / Kinco](../../../appendices/appendix-d/companies/company_step.md) |
| **产品类别** | 伺服驱动 |
| **发布时间** | 现役主力型号 |
| **状态** | 量产/商用 |
| **官网/来源** | [步科股份官网](https://www.kinco.cn) |

## 产品概述

低压直流供电、高功率密度、支持多种总线，适配移动机器人和电池供电设备。该系列产品由步科股份推出，主要面向伺服驱动 / 低压伺服 / HMI市场，具有DC 24–72 V等核心参数，适用于机器人、自动化设备及精密传动场景。

作为步科股份的代表产品之一，低压伺服系统在AGV/AMR、服务机器人等领域具有广泛应用。产品采用成熟制造工艺，可根据客户需求提供定制化接口、出线方式与控制协议。

## 产品图片

> 低压伺服系统：请访问 [官方资料](https://www.kinco.cn) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 驱动器约 70×120×40 mm（参考） | 产品手册 |
| 重量 | 未公开 | 产品手册 |
| 供电电压 | DC 24–72 V | 产品手册 |
| 额定功率 | 50 W – 1 kW | 产品手册 |
| 额定转速 | 3,000 rpm | 产品手册 |
| 编码器 | 17/23 位多圈绝对值 | 产品手册 |
| 通信接口 | CANopen / EtherCAT / RS485 | 产品手册 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[步科股份 / Step Automation / Kinco](../../../appendices/appendix-d/companies/company_step.md)
- **核心零部件/技术来源**：IGBT/SiC 功率器件、MCU/FPGA 控制芯片、磁性材料、编码器芯片、电容电阻。
- **下游应用/客户**：AGV/AMR 厂商、协作机器人公司、人形机器人 OEM、医疗设备、物流自动化。

## 知识图谱节点与关系

- 零部件实体：`ent_component_step_low_voltage_servo`
- 制造商实体：`ent_company_step`
- 关键关系：
  - `rel_ent_company_step_manufactures_ent_component_step_low_voltage_servo`（`ent_company_step` --> `manufactures` --> `ent_component_step_low_voltage_servo`）

## 应用场景

- **机器人**：AGV/AMR 轮毂驱动、协作机器人关节、人形机器人下肢、外骨骼。
- **工业自动化**：精密定位、传动与控制执行机构。
- **医疗与消费电子**：便携式设备、医疗器械驱动单元。
- **新能源与汽车**：电动执行器、热管理与智能座舱部件。

## 竞争对比

| 对比项 | 本产品 | 国际品牌 | 国内对标 |
|--------|--------|----------|----------|
| 核心优势 | 本土化供应、性价比、定制化 | 高端精度与可靠性 | 同区间性能竞争 |
| 交付周期 | 较短 | 较长 | 较短 |
| 服务响应 | 快速 | 中等 | 快速 |
| 价格水平 | 中低端至中高端 | 高端 | 中低端 |

## 选购与部署建议

- 选型时应根据负载、行程、速度与精度要求匹配合适型号，必要时联系厂商获取定制方案。
- 部署前建议进行负载惯量辨识、刚性匹配与振动抑制调试，确保与整机系统兼容。

## 参考资料

1. [步科股份官网](https://www.kinco.cn)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.inovance.com)（请按实际产品型号核对）