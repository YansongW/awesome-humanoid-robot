# 施耐德电气 / Schneider Electric SE

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 施耐德电气 |
| **英文名** | Schneider Electric SE |
| **总部** | 法国吕埃-玛尔梅松（Rueil-Malmaison） |
| **成立时间** | 1836 年 |
| **官网** | [https://www.se.com](https://www.se.com) |
| **供应链环节** | 工业自动化、能源管理、运动控制、数字化配电 |
| **企业属性** | 上市公司（EPA：SU） |
| **母公司/所属集团** | 无（独立上市） |
| **数据来源** | 施耐德电气官网、年报、产品资料 |

## 公司简介

施耐德电气是全球能源管理与工业自动化领域的领导者之一。

施耐德电气为楼宇、数据中心、基础设施和工业客户提供从低压配电、中压电网到自动化控制、工业软件的全栈解决方案。其工业自动化业务以 Modicon PLC、Altivar 变频器、Lexium 伺服和 EcoStruxure 工业互联网平台为核心，广泛应用于离散制造、混合工业与过程工业。其开放以太网架构、网络安全能力及能效管理技术，可为人形机器人制造端的产线配电、运动控制与能源优化提供成熟方案。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| PLC / ePAC | 过程与离散控制中枢 | Modicon M580 / M340 / M241 | 能源、水处理、智能制造 |
| 变频器与伺服 | 电机控制与运动控制 | Altivar Process / Lexium 32 | 泵、风机、传送、机器人 |
| 工业软件与能源管理 | 数字孪生与能效优化 | EcoStruxure / AVEVA | 工厂运维、数据中心 |

## 代表产品

### Schneider Electric Modicon M580 ePAC

> Schneider Electric Modicon M580 ePAC：请访问 [官方资料](https://www.se.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品类型 | ePAC（以太网可编程自动化控制器） | 官方资料 |
| 程序/数据内存 | 最大 64 MB | 官方资料（依 CPU 型号） |
| 最大 I/O 容量 | 未公开 | 未公开 |
| 通信接口 | EtherNet/IP、Modbus TCP、OPC UA | 官方资料 |
| 安全认证 | Achilles Level 2 | 官方资料 |
| 供电电压 | 24 VDC | 官方资料 |
| 工作温度 | 0 °C ~ 60 °C | 官方资料 |
| 价格 | 未公开 | 未公开 |

**技术亮点**：原生以太网、内置网络安全、过程与离散控制融合、支持 DCS/PLC 混合架构。

**应用场景**：电力与能源、水处理、石油化工、食品饮料、人形机器人整机装配线的控制与配电。

## 与人形机器人的关联

人形机器人量产需要稳定的配电、能效管理与产线控制，施耐德的 ePAC、变频与伺服系统可在装配、测试、物流环节提供成熟的自动化与能源管理基础设施。

## 供应链位置

- **上游关键零部件/材料**：半导体、功率器件、PCB、连接器、结构件、传感器
- **下游客户/应用场景**：能源基础设施、工业制造、数据中心、楼宇自动化
- **主要竞争对手/对标**：Siemens, Rockwell Automation, ABB, Mitsubishi Electric

## 知识图谱节点与关系

- 公司实体：`ent_company_schneider_electric`
- 产品实体：`ent_product_schneider_modicon_m580`
- 关键关系：
  - `ent_company_schneider_electric` -- `manufactures` --> `ent_product_schneider_modicon_m580`

## 参考资料

1. [施耐德电气 官网](https://www.se.com)
2. [Schneider Electric Modicon M580 ePAC 产品页](https://www.se.com/us/en/product-range/1469-modicon-m580/)
3. Schneider Electric Annual Report / EcoStruxure platform pages