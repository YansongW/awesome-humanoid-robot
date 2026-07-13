---
id: ent_product_schneider_modicon_m580
schema_version: 1
type: product
'title:': Schneider Electric Modicon M580 ePAC
domain: 02_components
theoretical_depth: system
aliases:
- Modicon M580
status: active
sources:
- id: ent_product_schneider_modicon_m580_official
  type: website
  url: https://www.se.com/us/en/product-range/1469-modicon-m580/
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13 00:00:00+00:00
---





# schneider_modicon_m580

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [施耐德电气 / Schneider Electric](../../../appendices/appendix-d/companies/company_schneider_electric.md) |
| **产品类别** | 可编程自动化控制器（ePAC） |
| **发布时间** | 2012 年（现役系列持续更新） |
| **状态** | 量产/商用 |
| **官网/来源** | [施耐德电气 官网](https://www.se.com) |

## 产品概述

Modicon M580 是施耐德电气推出的基于原生以太网架构的 ePAC，融合了 PLC 的灵活性与 DCS 的过程控制能力，强调内置网络安全与开放连接。

该系列支持 Modbus TCP、EtherNet/IP 与 OPC UA 等协议，可与变频器、伺服、HMI 及上层 MES/SCADA 系统无缝集成，适用于需要高可用性与 IIoT 连接的智能制造场景。

## 产品图片

> Schneider Electric Modicon M580 ePAC：请访问 [官方资料](https://www.se.com/us/en/product-range/1469-modicon-m580/) 查看。

## 规格参数表

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

## 供应链位置

- **制造商**：[施耐德电气 / Schneider Electric](../../../appendices/appendix-d/companies/company_schneider_electric.md)
- **核心零部件/技术来源**：自研控制固件与软件；处理器、以太网芯片、功率器件、存储芯片外购。
- **下游应用/客户**：过程工业、能源与水处理、食品饮料、人形机器人产线控制中枢。

## 知识图谱节点与关系

- 产品实体：`ent_product_schneider_modicon_m580`
- 制造商实体：`ent_company_schneider_electric`
- 关键关系：
  - `ent_company_schneider_electric` → `manufactures` → `ent_product_schneider_modicon_m580`（关系文件：`rel_ent_company_schneider_electric_manufactures_ent_product_schneider_modicon_m580.md`）

## 应用场景

- **过程控制**：油气、化工、水处理等连续过程。
- **离散制造**：汽车、电子、食品饮料产线。
- **机器人单元**：为人形机器人装配与测试提供控制中枢。
- **能源管理**：产线能效监测与优化。

## 竞争对比

| 对比项 | Schneider Electric Modicon M580 ePAC | Siemens S7-1500 | Rockwell ControlLogix |
|--------|---------------|--------|--------|
| 产品类型 | ePAC | PLC | PLC |
| 原生以太网 | 是 | 是 | 是 |
| 典型安全认证 | Achilles Level 2 | 未公开 | 未公开 |
| 价格 | 未公开 | 未公开 | 未公开 |

## 选购与部署建议

在需要过程与离散控制融合、且对网络安全有合规要求的场景优先考虑 M580；选型时需确认 I/O 点数、通信协议及冗余需求。

## 参考资料

1. [施耐德电气 官网](https://www.se.com)
2. [Schneider Electric Modicon M580 ePAC 产品页](https://www.se.com/us/en/product-range/1469-modicon-m580/)
3. Schneider Electric Annual Report / EcoStruxure platform pages