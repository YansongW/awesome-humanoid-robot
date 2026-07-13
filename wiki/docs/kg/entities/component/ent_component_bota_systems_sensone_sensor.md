---
id: ent_component_bota_systems_sensone_sensor
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: Bota Systems SensONE 六维力传感器 核心传感单元
  en: Bota Systems SensONE 6-Axis Force/Torque Sensor Core Sensing Unit
status: active
sources:
- id: src_ent_component_bota_systems_sensone_sensor_official
  type: website
  url: https://www.bota-systems.com/sensone
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01 00:00:00+00:00
---





# Bota Systems SensONE 六维力传感器 核心传感单元 / Bota Systems SensONE 6-Axis Force/Torque Sensor Core Sensing Unit

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [Bota Systems（博塔系统） / Bota Systems](../../../appendices/appendix-d/companies/company_bota_systems.md) |
| **产品类别** | 六维力/力矩传感器 |
| **发布时间** | 持续在售 |
| **状态** | 量产/商用 |
| **官网/来源** | [Bota Systems SensONE 六维力传感器 产品/资料页](https://www.bota-systems.com/sensone) |

## 产品概述

SensONE 是 Bota Systems 面向协作机器人和人形机器人设计的主流六维力/力矩传感器，支持拖动示教、力控装配、抛光与碰撞检测。其紧凑的圆盘式结构可直接安装于机器人末端法兰，提供多种量程与通信接口选项。

## 产品图片

> Bota Systems SensONE 六维力传感器：请访问 [官方资料](https://www.bota-systems.com/sensone) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 六维力/力矩传感器 | 官网 |
| 直径 | 约 80 mm | 官网/datasheet |
| 高度 | 约 21 mm | 官网/datasheet |
| 重量 | 约 290 g | 官网/datasheet |
| 力测量范围（Fx/Fy） | ±200 N | 官网/datasheet |
| 力测量范围（Fz） | ±500 N | 官网/datasheet |
| 力矩测量范围（Mx/My/Mz） | ±8 Nm | 官网/datasheet |
| 精度 | 未公开 | - |
| 过载能力 | 约 500% FS | 官网/datasheet |
| 采样频率 | 最高 1000 Hz | 官网/datasheet |
| 通信接口 | EtherCAT / Ethernet / USB / RS485 / CAN | 官网/datasheet |
| 防护等级 | IP67 | 官网/datasheet |
| 供电 | 未公开 | - |
| 工作温度 | 未公开 | - |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[Bota Systems（博塔系统） / Bota Systems](../../../appendices/appendix-d/companies/company_bota_systems.md)
- **核心零部件/技术来源**：自研六轴力觉弹性体与解耦算法、硅应变计、信号调理电路、工业级外壳与接插件。
- **下游应用/客户**：协作机器人 OEM、人形机器人整机厂、医疗康复设备、自动化集成商、科研院所。

## 知识图谱节点与关系

- 产品实体：`ent_product_bota_systems_sensone`
- 零部件实体：`ent_component_bota_systems_sensone_sensor`
- 制造商实体：`ent_company_bota_systems`
- 关键关系：
  - `rel_ent_company_bota_systems_manufactures_ent_product_bota_systems_sensone`（`ent_company_bota_systems` → `manufactures` → `ent_product_bota_systems_sensone`）
  - `rel_ent_company_bota_systems_manufactures_ent_component_bota_systems_sensone_sensor`（`ent_company_bota_systems` → `manufactures` → `ent_component_bota_systems_sensone_sensor`）
  - `rel_ent_product_bota_systems_sensone_uses_ent_component_bota_systems_sensone_sensor`（`ent_product_bota_systems_sensone` → `uses` → `ent_component_bota_systems_sensone_sensor`）

## 应用场景

- **协作机器人力控**：末端力反馈实现柔顺装配、抛光与打磨。
- **人形机器人手腕**：提供六维力觉，支撑抓取、平衡与碰撞检测。
- **拖动示教**：基于力反馈的快速轨迹示教与编程。
- **医疗康复机器人**：低延迟力觉反馈用于康复训练与手术辅助。

## 竞争对比

| 对比项 | 本产品 | 主要竞品 A | 主要竞品 B |
|--------|--------|------------|------------|
| 类型 | 协作机器人六维力传感器 | ATI Nano 系列 | OnRobot HEX-E |
| 量程 | Fx/Fy ±200 N / Fz ±500 N | 多型号 | ±100 N / ±10 Nm |
| 通信 | EtherCAT/Ethernet/USB/CAN | 模拟/DAQ/EtherCAT | TCP/IP/USB/EtherNet/IP |
| 核心优势 | 紧凑、高性价比 | 极小尺寸、高过载 | 即插即用生态 |

## 选购与部署建议

- 根据目标应用的分辨率、量程、精度或算力需求选择具体型号。
- 部署前确认接口、供电、散热、机械安装与环境温度范围匹配。
- 建议通过官方渠道或授权代理商获取最新固件、SDK 与技术支持。

## 相关词条

- [制造商：Bota Systems（博塔系统） / Bota Systems](../../../appendices/appendix-d/companies/company_bota_systems.md)
- [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)

## 参考资料

1. [Bota Systems 官网](https://www.bota-systems.com)
2. [Bota Systems SensONE 六维力传感器 产品/资料页](https://www.bota-systems.com/sensone)
3. 产品 datasheet 与公开技术报道
4. [附录 D 企业目录](../../../appendices/appendix-d/index-companies.md)