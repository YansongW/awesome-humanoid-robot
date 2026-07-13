# Bosch Rexroth ctrlX CORE / ctrlX CORE

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [博世力士乐 / Bosch Rexroth](../companies/company_bosch_rexroth.md) |
| **产品类别** | 工业自动化控制器 |
| **发布时间** | 2020 年 |
| **状态** | 量产/商用 |
| **官网/来源** | [博世力士乐 官网](https://www.boschrexroth.com) |

## 产品概述

ctrlX CORE 是 Bosch Rexroth ctrlX AUTOMATION 平台的核心控制器，采用基于 Linux 的实时操作系统，支持以 app 方式扩展 PLC、运动、机器人和物联网功能。

控制器内置多协议通信能力，可作为边缘计算节点与上层云平台对接，适用于需要高灵活性与软件定义的自动化系统。

## 产品图片

> Bosch Rexroth ctrlX CORE：请访问 [官方资料](https://www.boschrexroth.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品类型 | 工业自动化控制器 / IPC | 官方资料 |
| 操作系统 | ctrlX OS（基于 Linux 实时内核） | 官方资料 |
| 处理器 | 未公开 | 未公开 |
| 控制轴数 | 最多 99 轴 | 官方资料 |
| 通信接口 | EtherCAT、Sercos III、PROFINET、OPC UA、MQTT | 官方资料 |
| 供电电压 | 24 VDC | 官方资料 |
| 工作温度 | 0 °C ~ 50 °C | 官方资料 |
| 价格 | 未公开 | 未公开 |

## 供应链位置

- **制造商**：[博世力士乐 / Bosch Rexroth](../companies/company_bosch_rexroth.md)
- **核心零部件/技术来源**：自研 ctrlX OS 与控制软件；处理器、通信模块、功率器件、存储外购。
- **下游应用/客户**：智能机床、包装、物流、移动机械、人形机器人控制平台。

## 知识图谱节点与关系

- 产品实体：`ent_product_bosch_rexroth_ctrlx_core`
- 制造商实体：`ent_company_bosch_rexroth`
- 关键关系：
  - `ent_company_bosch_rexroth` → `manufactures` → `ent_product_bosch_rexroth_ctrlx_core`（关系文件：`rel_ent_company_bosch_rexroth_manufactures_ent_product_bosch_rexroth_ctrlx_core.md`）

## 应用场景

- **智能机床**：多轴联动与工艺优化。
- **包装机械**：飞剪、追剪与电子凸轮。
- **移动机器人**：AGV/AMR 运动控制与调度。
- **人形机器人**：作为本体控制器或关节驱动网关。

## 竞争对比

| 对比项 | Bosch Rexroth ctrlX CORE | Siemens SIMATIC S7-1500 | Beckhoff CX2030 |
|--------|---------------|--------|--------|
| 操作系统 | Linux RT（ctrlX OS） | 实时 Windows / Linux | TwinCAT/BSD |
| 软件形态 | app-based | 传统 PLC 项目 | TwinCAT runtime |
| 控制轴数 | 最多 99 轴 | 依型号 | 依型号 |
| 价格 | 未公开 | 未公开 | 未公开 |

## 选购与部署建议

适合希望以软件定义自动化、快速集成第三方算法与云边协同的项目；需评估 app 生态成熟度与实时性需求。

## 参考资料

1. [博世力士乐 官网](https://www.boschrexroth.com)
2. [Bosch Rexroth ctrlX CORE 产品页](https://www.boschrexroth.com/en/us/products/product-groups/controls/ctrlx-automation/ctrlx-core)
3. Bosch Rexroth ctrlX AUTOMATION product pages