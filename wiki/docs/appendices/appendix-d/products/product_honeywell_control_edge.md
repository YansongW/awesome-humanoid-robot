# Honeywell ControlEdge PLC / ControlEdge PLC

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [霍尼韦尔 / Honeywell](../companies/company_honeywell.md) |
| **产品类别** | 可编程逻辑控制器（PLC） |
| **发布时间** | 2016 年 |
| **状态** | 量产/商用 |
| **官网/来源** | [霍尼韦尔 官网](https://www.honeywell.com) |

## 产品概述

ControlEdge PLC 是霍尼韦尔面向过程与离散混合应用推出的新一代 PLC，支持 IEC 61131-3 编程与多种工业以太网协议。

该产品可直接接入 Experion PKS 分布式控制系统，并通过 OPC UA 与 MQTT 实现 IIoT 数据上云，适用于需要高可靠性与网络安全认证的关键基础设施。

## 产品图片

> Honeywell ControlEdge PLC：请访问 [官方资料](https://www.honeywell.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品类型 | 可编程逻辑控制器（PLC） | 官方资料 |
| 通信协议 | Modbus/TCP、EtherNet/IP、OPC UA、MQTT | 官方资料 |
| 冗余支持 | 支持（依配置） | 官方资料 |
| 编程标准 | IEC 61131-3 | 官方资料 |
| 工作温度 | -20 °C ~ 60 °C | 官方资料 |
| 安全认证 | 未公开 | 未公开 |
| 供电电压 | 24 VDC | 官方资料 |
| 价格 | 未公开 | 未公开 |

## 供应链位置

- **制造商**：[霍尼韦尔 / Honeywell](../companies/company_honeywell.md)
- **核心零部件/技术来源**：自研控制固件与 Experion 集成软件；处理器、通信芯片、I/O 模块、电源外购。
- **下游应用/客户**：过程工业、电力、水处理、制药、智能制造、机器人测试平台。

## 知识图谱节点与关系

- 产品实体：`ent_product_honeywell_control_edge`
- 制造商实体：`ent_company_honeywell`
- 关键关系：
  - `ent_company_honeywell` → `manufactures` → `ent_product_honeywell_control_edge`（关系文件：`rel_ent_company_honeywell_manufactures_ent_product_honeywell_control_edge.md`）

## 应用场景

- **油气化工**：储运、反应釜、压缩机控制。
- **电力水处理**：辅控系统与远程监控。
- **制药食品**：批次控制与追溯。
- **机器人测试**：为人形机器人实验室提供过程监控。

## 竞争对比

| 对比项 | Honeywell ControlEdge PLC | Emerson PACSystems | Siemens S7-1500 |
|--------|---------------|--------|--------|
| 目标市场 | 过程/混合工业 | 离散/过程工业 | 离散/通用 |
| DCS 集成 | Experion PKS | DeltaV | SIMATIC PCS 7 |
| IIoT 协议 | OPC UA / MQTT | OPC UA / MQTT | OPC UA / PROFINET |
| 价格 | 未公开 | 未公开 | 未公开 |

## 选购与部署建议

适合已有霍尼韦尔 DCS 体系的过程工厂扩展离散控制；或需要 IIoT 连接与高环境适应性的场景。

## 参考资料

1. [霍尼韦尔 官网](https://www.honeywell.com)
2. [Honeywell ControlEdge PLC 产品页](https://process.honeywell.com/us/en/products/control-edge-plc)
3. Honeywell Process Solutions ControlEdge PLC datasheet