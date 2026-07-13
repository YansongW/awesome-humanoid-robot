# 艾默生电气 / Emerson Electric Co.

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 艾默生电气 |
| **英文名** | Emerson Electric Co. |
| **总部** | 美国密苏里州圣路易斯 |
| **成立时间** | 1890 年 |
| **官网** | [https://www.emerson.com](https://www.emerson.com) |
| **供应链环节** | 过程控制、工业自动化、流体控制、电气设备、工业软件 |
| **企业属性** | 上市公司（NYSE：EMR） |
| **母公司/所属集团** | 无（独立上市） |
| **数据来源** | Emerson 官网、产品目录、年报 |

## 公司简介

艾默生电气是全球过程工业自动化与流体控制技术的领导者。

艾默生通过 DeltaV DCS、PACSystems PLC、Ovation 控制系统、ASCO 流体控制、Rosemount 仪表及 AspenTech 工业软件，为能源、化工、电力、生命科学等行业提供自动化解决方案。其 PACSystems RSTi-EP 系列将紧凑型控制器与分布式 I/O 结合，强调模块化、可扩展性与信息安全。其传感器、阀门与运动控制产品亦可服务于机器人与智能装备。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 过程控制 / DCS | 连续过程自动化 | DeltaV / Ovation | 油气、化工、电力 |
| PLC / PAC | 离散与混合控制 | PACSystems RX3i / RSTi-EP | 制造、水处理、能源 |
| 流体控制与仪表 | 阀门、执行机构、传感器 | ASCO / Rosemount / AVENTICS | 过程工厂、机器人气动 |

## 代表产品

### Emerson PACSystems RSTi-EP PLC

> Emerson PACSystems RSTi-EP PLC：请访问 [官方资料](https://www.emerson.com) 查看。

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

**技术亮点**：紧凑型模块化 PAC、分布式 I/O 扩展、内置信息安全功能、多协议通信与冗余能力。

**应用场景**：水处理、食品饮料、离散制造、能源、生命科学、机器人单元控制与测试系统。

## 与人形机器人的关联

人形机器人原型开发与测试需要采集大量传感器数据并控制外围设备，PACSystems 的模块化 I/O 与快速扫描能力适合作为实验室测试台与产线控制节点。

## 供应链位置

- **上游关键零部件/材料**：处理器、功率模块、I/O 模块、传感器、气动元件、PCB
- **下游客户/应用场景**：石油天然气、化工、电力、水处理、离散制造、机器人集成
- **主要竞争对手/对标**：Honeywell, Siemens, Schneider Electric, Rockwell Automation

## 知识图谱节点与关系

- 公司实体：`ent_company_emerson`
- 产品实体：`ent_product_emerson_pacsystems_rsti_ep`
- 关键关系：
  - `ent_company_emerson` -- `manufactures` --> `ent_product_emerson_pacsystems_rsti_ep`

## 参考资料

1. [艾默生电气 官网](https://www.emerson.com)
2. [Emerson PACSystems RSTi-EP PLC 产品页](https://www.emerson.com/en-us/catalog/controllers/pacsystems-rsti-ep)
3. Emerson PACSystems RSTi-EP product catalog