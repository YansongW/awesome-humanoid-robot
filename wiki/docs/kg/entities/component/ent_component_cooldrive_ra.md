---
id: ent_component_cooldrive_ra
schema_version: 1
type: component
'title:': CoolDrive RA Series Servo Drive
domain: 02_components
theoretical_depth: system
names:
  zh: 清能德创 CoolDrive RA 系列伺服驱动器
  en: CoolDrive RA Series Servo Drive
status: active
sources:
- id: src_cooldrive_ra_official
  type: website
  url: https://www.cooldrive.com.cn
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 清能德创 CoolDrive RA 系列伺服驱动器 / CoolDrive RA Series Servo Drive

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [清能德创 / CoolDrive](../../../appendices/appendix-d/companies/company_cooldrive.md) |
| **产品类别** | 伺服驱动器 / 人形机器人核心部件 |
| **发布时间** | 2015 年起持续迭代 |
| **状态** | 量产/商用 |
| **官网/来源** | [https://www.cooldrive.com.cn](https://www.cooldrive.com.cn) |

## 产品概述

CoolDrive RA 系列是清能德创推出的高端伺服驱动器，面向工业机器人、协作机器人与人形机器人关节驱动。

产品支持 EtherCAT、CANopen 等工业总线，兼容多种高精度编码器协议，具备高集成度多轴驱动能力与功能安全设计，是国内人形机器人核心零部件国产替代的重要方案。

## 产品图片

> CoolDrive RA：请访问 [官方资料](https://www.cooldrive.com.cn) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品形态 | 单轴/多轴伺服驱动器 | 清能德创官网 |
| 功率范围 | 100 W – 15 kW（视型号） | 产品手册 |
| 输入电压 | 三相 220 VAC / 380 VAC（视型号） | 产品手册 |
| 控制模式 | 位置/速度/转矩 | 产品手册 |
| 通信协议 | EtherCAT / CANopen | 产品手册 |
| 速度环带宽 | 未公开 | - |
| 电流环频率 | 未公开 | - |
| 编码器支持 | 17/23 位绝对值、BiSS-C、EnDat 2.2 | 产品手册 |
| 安全功能 | STO / SS1 等 | 产品手册 |
| 价格 | 未公开 | 需询价 |

## 供应链位置

- **制造商**：[清能德创 / CoolDrive](../../../appendices/appendix-d/companies/company_cooldrive.md)
- **核心零部件/技术来源**：IGBT、MOS 管、PCB、电容、电流传感器、编码器接口芯片、DSP/ARM 控制芯片、散热器。
- **下游应用/客户**：工业机器人厂商、人形机器人整机厂、协作机器人厂商、数控机床、半导体设备、激光设备。

## 知识图谱节点与关系

- 产品实体：`ent_component_cooldrive_ra`
- 制造商实体：`ent_company_cooldrive`
- 关键关系：
  - `rel_ent_company_cooldrive_manufactures_ent_component_cooldrive_ra`（`ent_company_cooldrive` → `manufactures` → `ent_component_cooldrive_ra`）

## 应用场景

- **工业机器人**：六轴、SCARA、协作机器人关节驱动。
- **人形机器人**：全身关节高动态响应与力控驱动。
- **数控机床**：高精度主轴与进给轴驱动。
- **半导体设备**：精密运动平台驱动。

## 竞争对比

| 对比项 | CoolDrive RA | 主要竞品 |
|--------|--------------|----------|
| 定位 | 高端伺服驱动/多轴驱动 | 汇川 SV680、雷赛 L8、安川 Σ 系列 |
| 核心优势 | 多轴集成、高编码器兼容性、功能安全 | 视具体型号而定 |
| 价格 | 未公开 | 未公开 |

## 选购与部署建议

- 根据功率、轴数、编码器类型与总线协议选择对应型号。
- 人形机器人应用建议评估多轴驱动的散热、同步性能与故障安全机制。
- 建议通过清能德创官方渠道获取最新固件、调试软件与认证信息。

## 相关词条

- [制造商：清能德创 / CoolDrive](../../../appendices/appendix-d/companies/company_cooldrive.md)
- [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)

## 参考资料

1. [清能德创官网](https://www.cooldrive.com.cn)
2. 清能德创 CoolDrive RA 系列产品手册
3. [WAIC 2026 参展报道](https://www.worldrobotconference.com)