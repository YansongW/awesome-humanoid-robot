# 霍尼韦尔 / Honeywell International Inc.

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 霍尼韦尔 |
| **英文名** | Honeywell International Inc. |
| **总部** | 美国北卡罗来纳州夏洛特 |
| **成立时间** | 1906 年 |
| **官网** | [https://www.honeywell.com](https://www.honeywell.com) |
| **供应链环节** | 工业自动化、过程控制、楼宇自动化、传感器、PLC |
| **企业属性** | 上市公司（NASDAQ：HON） |
| **母公司/所属集团** | 无（独立上市） |
| **数据来源** | Honeywell 官网、过程控制产品资料、公开财报 |

## 公司简介

霍尼韦尔是全球领先的工业自动化、航空航天与楼宇技术企业。

霍尼韦尔的工业自动化业务以过程控制（Experion PKS）、安全系统、现场仪表、PLC（ControlEdge）和工业软件为核心，覆盖石油天然气、化工、电力、制药等行业。ControlEdge PLC 强调与 Experion PKS 的无缝集成、IIoT 连接与网络安全，适用于混合工业与关键基础设施。其传感器与控制技术也可用于机器人环境感知与过程监控。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| DCS / 过程控制 | 大规模连续过程控制 | Experion PKS | 油气、化工、电力 |
| PLC / RTU | 离散与混合控制 | ControlEdge PLC / RTU | 过程工厂、远程站点 |
| 工业软件与安全 | 生产管理、网络安全 | Honeywell Forge / SMX | 智能工厂、能源 |

## 代表产品

### Honeywell ControlEdge PLC

> Honeywell ControlEdge PLC：请访问 [官方资料](https://www.honeywell.com) 查看。

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

**技术亮点**：与 Experion PKS 深度集成、内置 OPC UA/MQTT 支持、面向 IIoT 与过程工业设计、冗余与高可用性选项。

**应用场景**：油气储运、化工过程、电力辅控、水处理、制药、人形机器人测试环境的过程监控。

## 与人形机器人的关联

人形机器人制造涉及大量环境监控、能源与过程数据采集，霍尼韦尔的 PLC 与传感器网络可为实验室与产线提供稳定的过程控制与数据底座。

## 供应链位置

- **上游关键零部件/材料**：半导体、传感器元件、PCB、电源模块、连接器、外壳
- **下游客户/应用场景**：石油天然气、化工、电力、制药、楼宇与基础设施
- **主要竞争对手/对标**：Emerson, Siemens, ABB, Yokogawa

## 知识图谱节点与关系

- 公司实体：`ent_company_honeywell`
- 产品实体：`ent_product_honeywell_control_edge`
- 关键关系：
  - `ent_company_honeywell` -- `manufactures` --> `ent_product_honeywell_control_edge`

## 参考资料

1. [霍尼韦尔 官网](https://www.honeywell.com)
2. [Honeywell ControlEdge PLC 产品页](https://process.honeywell.com/us/en/products/control-edge-plc)
3. Honeywell Process Solutions ControlEdge PLC datasheet