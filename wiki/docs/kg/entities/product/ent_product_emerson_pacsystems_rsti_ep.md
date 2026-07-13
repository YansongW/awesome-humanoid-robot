---
id: ent_product_emerson_pacsystems_rsti_ep
schema_version: 1
type: product
'title:': Emerson PACSystems RSTi-EP PLC
domain: 02_components
theoretical_depth: system
aliases:
- RSTi-EP
status: active
sources:
- id: ent_product_emerson_pacsystems_rsti_ep_official
  type: website
  url: https://www.emerson.com/en-us/catalog/controllers/pacsystems-rsti-ep
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13 00:00:00+00:00
---





# emerson_pacsystems_rsti_ep

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [艾默生电气 / Emerson Electric](../../../appendices/appendix-d/companies/company_emerson.md) |
| **产品类别** | 可编程自动化控制器（PAC） |
| **发布时间** | 现役（RSTi-EP 系列持续更新） |
| **状态** | 量产/商用 |
| **官网/来源** | [艾默生电气 官网](https://www.emerson.com) |

## 产品概述

PACSystems RSTi-EP 是艾默生面向紧凑、高密度应用推出的 PAC 平台，集成了控制器与可扩展的分布式 I/O。

该平台支持 PROFINET、EtherNet/IP、Modbus/TCP 与 OPC UA，具备信息安全与冗余选项，适用于需要高灵活性与可靠性的离散和混合过程应用。

## 产品图片

> Emerson PACSystems RSTi-EP PLC：请访问 [官方资料](https://www.emerson.com/en-us/catalog/controllers/pacsystems-rsti-ep) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品类型 | 可编程自动化控制器（PAC） | 官方资料 |
| I/O 容量 | 最多 2,048 点（依配置） | 官方资料 |
| 扫描速度 | 1 ms / 1K 布尔指令 | 官方资料 |
| 通信接口 | PROFINET、EtherNet/IP、Modbus/TCP、OPC UA | 官方资料 |
| 编程软件 | PAC Machine Edition | 官方资料 |
| 冗余支持 | 支持 | 官方资料 |
| 工作温度 | -20 °C ~ 60 °C | 官方资料 |
| 价格 | 未公开 | 未公开 |

## 供应链位置

- **制造商**：[艾默生电气 / Emerson Electric](../../../appendices/appendix-d/companies/company_emerson.md)
- **核心零部件/技术来源**：自研 PAC 固件与 Machine Edition 软件；处理器、通信模块、I/O 模块、电源外购。
- **下游应用/客户**：水处理、食品饮料、生命科学、能源、机器人测试与集成系统。

## 知识图谱节点与关系

- 产品实体：`ent_product_emerson_pacsystems_rsti_ep`
- 制造商实体：`ent_company_emerson`
- 关键关系：
  - `ent_company_emerson` → `manufactures` → `ent_product_emerson_pacsystems_rsti_ep`（关系文件：`rel_ent_company_emerson_manufactures_ent_product_emerson_pacsystems_rsti_ep.md`）

## 应用场景

- **水处理**：泵站、曝气、过滤控制。
- **食品饮料**：灌装、包装、输送线。
- **生命科学**：批次控制与设备集成。
- **机器人测试**：为人形机器人实验室提供高速 I/O 与运动协调。

## 竞争对比

| 对比项 | Emerson PACSystems RSTi-EP PLC | Honeywell ControlEdge | Siemens S7-1500 |
|--------|---------------|--------|--------|
| 产品形态 | 紧凑型 PAC + 分布式 I/O | 模块化 PLC | 模块化 PLC |
| 扫描速度 | 1 ms / 1K 布尔 | 未公开 | 未公开 |
| 主要通信 | PROFINET / EtherNet/IP | EtherNet/IP / Modbus | PROFINET / EtherNet/IP |
| 价格 | 未公开 | 未公开 | 未公开 |

## 选购与部署建议

在 I/O 点分散、对空间与扫描速度有要求的场景优先考虑 RSTi-EP；选型时确认 I/O 模块类型与网络安全功能授权。

## 参考资料

1. [艾默生电气 官网](https://www.emerson.com)
2. [Emerson PACSystems RSTi-EP PLC 产品页](https://www.emerson.com/en-us/catalog/controllers/pacsystems-rsti-ep)
3. Emerson PACSystems RSTi-EP product catalog