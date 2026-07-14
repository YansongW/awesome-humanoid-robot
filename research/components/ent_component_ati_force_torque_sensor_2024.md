---
$id: ent_component_ati_force_torque_sensor_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: ATI Force Torque Sensor
  zh: ATI 力/力矩传感器
  ko: ATI 힘/토크 센서
summary:
  en: Wrist and ankle force/torque sensor for contact control and interaction.
  zh: 用于腕部和踝部接触控制和交互的力/力矩传感器。
  ko: 접촉 제어 및 상호작용을 위한 손목 및 발목 힘/토크 센서.
domains:
- 02_components
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- ankle
- ati
- component
- force_torque
- sensor
- wrist
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/products/product_onrobot_hex_e.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: ATI Force Torque Sensor
  url: https://www.ati-ia.com/
  date: '2024'
  accessed_at: '2026-07-02'
---
## 概述
ATI 力/力矩传感器是人形机器人领域的重要component。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## OnRobot HEX-E QC 六维力/力矩传感器 / OnRobot HEX-E QC 6-Axis Force/Torque Sensor

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [OnRobot（昂乐） / OnRobot](../companies/company_onrobot.md) |
| **产品类别** | 协作机器人六维力/力矩传感器 |
| **发布时间** | 持续在售 |
| **状态** | 量产/商用 |
| **官网/来源** | [OnRobot HEX-E QC 六维力/力矩传感器 产品/资料页](https://www.onrobot.com/en/products/he-x) |

### 产品概述

HEX-E QC 是 OnRobot 为协作机器人末端设计的六维力/力矩传感器，集成 Quick Changer 快换接口，支持即插即用安装。它可实时测量六维力/力矩数据，帮助机器人完成精密装配、恒力抛光、表面处理和碰撞检测。

### 产品图片

> OnRobot HEX-E QC 六维力/力矩传感器：请访问 [官方资料](https://www.onrobot.com/en/products/he-x) 查看。

### 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 六维力/力矩传感器 | 官网 |
| 力测量范围（Fx/Fy/Fz） | ±100 N / ±100 N / ±200 N | 官网/datasheet |
| 力矩测量范围（Mx/My/Mz） | ±10 Nm / ±10 Nm / ±10 Nm | 官网/datasheet |
| 精度 | 未公开 | - |
| 分辨率 | 未公开 | - |
| 采样频率 | 未公开 | - |
| 过载能力 | 约 500% FS | 官网/datasheet |
| 防护等级 | IP67 | 官网/datasheet |
| 通信接口 | TCP/IP、USB、EtherNet/IP、PROFINET | 官网/datasheet |
| 集成接口 | Quick Changer / 机器人法兰 | 官网/datasheet |
| 供电 | 24 V DC | 官网/datasheet |
| 重量 | 约 350 g | 官网/datasheet |
| 工作温度 | 未公开 | - |
| 价格 | 未公开 | - |

### 供应链位置

- **制造商**：[OnRobot（昂乐） / OnRobot](../companies/company_onrobot.md)
- **核心零部件/技术来源**：自研力觉传感单元、信号处理与通信电路、Quick Changer 机械接口、工业级密封外壳。
- **下游应用/客户**：协作机器人 OEM、汽车与电子制造商、人形机器人整机厂、自动化系统集成商。

### 知识图谱节点与关系

- 产品实体：`ent_product_onrobot_hex_e`
- 零部件实体：`ent_component_onrobot_hex_e_sensor`
- 制造商实体：`ent_company_onrobot`
- 关键关系：
  - `rel_ent_company_onrobot_manufactures_ent_product_onrobot_hex_e`（`ent_company_onrobot` → `manufactures` → `ent_product_onrobot_hex_e`）
  - `rel_ent_company_onrobot_manufactures_ent_component_onrobot_hex_e_sensor`（`ent_company_onrobot` → `manufactures` → `ent_component_onrobot_hex_e_sensor`）
  - `rel_ent_product_onrobot_hex_e_uses_ent_component_onrobot_hex_e_sensor`（`ent_product_onrobot_hex_e` → `uses` → `ent_component_onrobot_hex_e_sensor`）

### 应用场景

- **力控装配**：精密插件、齿轮装配中的柔顺插入与定位。
- **恒力打磨/抛光**：保持恒定接触力，提高表面质量一致性。
- **插拔与测试**：连接器、开关等零部件的力-位移测试。
- **人形机器人手臂**：末端六维力觉用于抓取与交互。

### 竞争对比

| 对比项 | 本产品 | 主要竞品 A | 主要竞品 B |
|--------|--------|------------|------------|
| 类型 | 协作机器人六维力传感器 | ATI Nano25 | Bota Systems SensONE |
| 力范围 | ±100 N / ±200 N | ±250 N / ±1000 N | ±200 N / ±500 N |
| 通信 | TCP/IP/USB/EtherNet/IP | 模拟/DAQ/EtherCAT | EtherCAT/Ethernet/CAN |
| 核心优势 | 快换集成、生态成熟 | 极小尺寸、高过载 | 紧凑高性价比 |

### 选购与部署建议

- 根据目标应用的分辨率、量程、精度或算力需求选择具体型号。
- 部署前确认接口、供电、散热、机械安装与环境温度范围匹配。
- 建议通过官方渠道或授权代理商获取最新固件、SDK 与技术支持。

### 相关词条

- [制造商：OnRobot（昂乐） / OnRobot](../companies/company_onrobot.md)
- [附录 D.4 重点产品 Wiki](../index-products.md)

### 参考资料

1. [OnRobot 官网](https://www.onrobot.com)
2. [OnRobot HEX-E QC 六维力/力矩传感器 产品/资料页](https://www.onrobot.com/en/products/he-x)
3. 产品 datasheet 与公开技术报道
4. [附录 D 企业目录](../index-companies.md)

## 参考
- [ATI Force Torque Sensor](https://www.ati-ia.com/)
- 项目 Wiki：appendix-d/products/product_onrobot_hex_e.md

