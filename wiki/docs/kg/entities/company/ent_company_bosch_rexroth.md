---
id: ent_company_bosch_rexroth
schema_version: 1
type: company
'title:': Bosch Rexroth AG
domain: 02_components
theoretical_depth: system
names:
  zh: 博世力士乐
  en: Bosch Rexroth AG
aliases:
- 博世力士乐
- Bosch Rexroth
status: active
sources:
- id: ent_company_bosch_rexroth_official
  type: website
  url: https://www.boschrexroth.com
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13 00:00:00+00:00
---





# 博世力士乐 / Bosch Rexroth AG

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 博世力士乐 |
| **英文名** | Bosch Rexroth AG |
| **总部** | 德国洛尔（Lohr am Main） |
| **成立时间** | 2001 年（Rexroth 起源可追溯至 1795 年） |
| **官网** | [https://www.boschrexroth.com](https://www.boschrexroth.com) |
| **供应链环节** | 传动与控制技术、液压、线性传动、伺服系统、工业自动化平台 |
| **企业属性** | 非上市（Robert Bosch GmbH 全资子公司） |
| **母公司/所属集团** | Robert Bosch GmbH |
| **数据来源** | Bosch Rexroth 官网、产品页、博世集团年报 |

## 公司简介

博世力士乐是全球传动与控制技术领域的系统供应商。

博世力士乐提供液压、电气驱动与控制、线性传动与组装技术、物联网与自动化平台等产品，服务于工厂自动化、行走机械与工业 4.0。其 ctrlX AUTOMATION 平台以“智能手机式”的 app 生态和开放 Linux 实时系统为特色，支持 PLC、运动、机器人、IoT 与机器视觉应用。其伺服与线性传动产品亦适用于人形机器人关节与执行机构。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 自动化平台 | 开放、app-based 控制 | ctrlX CORE / ctrlX OS | 机床、包装、移动机械 |
| 电气驱动 | 伺服驱动与电机 | IndraDrive / MS2N | 机器人、机床、物流 |
| 线性传动 | 导轨、丝杠、电缸 | 滚珠导轨 / 行星滚柱丝杠 | 装配、半导体、医疗 |

## 代表产品

### Bosch Rexroth ctrlX CORE

> Bosch Rexroth ctrlX CORE：请访问 [官方资料](https://www.boschrexroth.com) 查看。

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

**技术亮点**：app-based 架构、开放 Linux 实时系统、集成 PLC/运动/IoT/机器人功能、多协议通信。

**应用场景**：智能机床、包装机械、移动机器人、仓储物流、人形机器人控制系统与边缘计算。

## 与人形机器人的关联

人形机器人开发需要灵活的软件架构与多轴实时控制，ctrlX CORE 的 app 生态与开放接口可作为机器人本体控制器或关节驱动网关。

## 供应链位置

- **上游关键零部件/材料**：处理器、功率半导体、液压元件、轴承、铝材、PCB
- **下游客户/应用场景**：机床、包装、行走机械、汽车、物流自动化
- **主要竞争对手/对标**：Siemens, Beckhoff, B&R, Schneider Electric

## 知识图谱节点与关系

- 公司实体：`ent_company_bosch_rexroth`
- 产品实体：`ent_product_bosch_rexroth_ctrlx_core`
- 关键关系：
  - `ent_company_bosch_rexroth` -- `manufactures` --> `ent_product_bosch_rexroth_ctrlx_core`

## 参考资料

1. [博世力士乐 官网](https://www.boschrexroth.com)
2. [Bosch Rexroth ctrlX CORE 产品页](https://www.boschrexroth.com/en/us/products/product-groups/controls/ctrlx-automation/ctrlx-core)
3. Bosch Rexroth ctrlX AUTOMATION product pages