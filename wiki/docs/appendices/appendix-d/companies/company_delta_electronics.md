---
id: ent_company_delta_electronics
schema_version: 1
type: company
title: Delta Electronics
domain: 02_components
theoretical_depth: system
names:
  zh: 台达电子
  en: Delta Electronics
status: active
sources:
  - id: src_delta_official
    type: website
    title: Delta Electronics Official Website
    url: https://www.deltaww.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---

# 台达电子 / Delta Electronics

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 台达电子 |
| **英文名** | Delta Electronics |
| **总部** | 中国台湾台北 |
| **成立时间** | 1971 |
| **官网** | [https://www.deltaww.com](https://www.deltaww.com) |
| **供应链环节** | 伺服系统 / 变频器 / PLC / 运动控制器 / 电源 |
| **企业属性** | 台资品牌、上市公司（2308.TW） |
| **母公司/所属集团** | 无（独立上市） |
| **数据来源** | 台达官网、产品手册、公开研报、WAIC 2026 报道 |

## 公司简介

台达电子是全球领先的电源管理与散热解决方案厂商，工业自动化领域覆盖伺服、变频器、PLC 与运动控制。

台达工业自动化事业部提供从核心零部件到行业解决方案的完整产品线，ASDA 系列伺服系统、变频器与运动控制器广泛应用于机器人、机床、电子制造与新能源装备。其伺服产品以高响应、高可靠性与节能设计见长，是亚太地区机器人核心零部件的重要供应商。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| ASDA 交流伺服系统 | 高性能伺服电机+驱动 | ASDA-B3 / ASDA-A3 | 工业机器人、电子制造 |
| 变频器与 PLC | 工厂自动化控制 | MS300 / AH500 系列 | 风机水泵、产线控制 |
| 运动控制器 | 多轴同步控制 | DMCNET / AX 系列 | CNC、机器人 |

## 代表产品

### ASDA-B3 系列伺服驱动器 / ASDA-B3 Series Servo Drive

> ASDA-B3 系列伺服驱动器：请访问 [官方资料](https://www.deltaww.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品形态 | 单轴交流伺服驱动器 | 台达官网 |
| 功率范围 | 100 W – 15 kW | 产品手册 |
| 输入电压 | 单相/三相 220 VAC / 380 VAC | 产品手册 |
| 控制模式 | 位置/速度/转矩 | 产品手册 |
| 通信协议 | CANopen / EtherCAT / DMCNET | 产品手册 |
| 速度环带宽 | 3.1 kHz（参考） | 产品手册 |
| 编码器支持 | 17/20/23 位绝对值 | 产品手册 |
| 安全功能 | STO（部分型号） | 产品手册 |
| 价格 | 未公开 | 需询价 |

**技术亮点**：高响应控制、内置多种抑振与摩擦力补偿算法，适配机器人高动态关节与精密定位。

**应用场景**：工业机器人、协作机器人、人形机器人关节、半导体设备、3C 自动化。

### ECMA 系列伺服电机 / ECMA Series Servo Motor

> ECMA 系列伺服电机：请访问 [官方资料](https://www.deltaww.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品形态 | 交流伺服电机 | 台达官网 |
| 机座号 | 40–180 mm | 产品手册 |
| 额定功率 | 50 W – 15 kW | 产品手册 |
| 额定转速 | 1000–6000 rpm | 产品手册 |
| 编码器 | 17/20/23 位绝对值 | 产品手册 |
| 防护等级 | IP65（部分型号） | 产品手册 |
| 价格 | 未公开 | 需询价 |

**技术亮点**：低齿槽转矩、高过载能力，与 ASDA 系列驱动器深度匹配，支持机器人高精度运动。

**应用场景**：工业机器人、人形机器人、数控机床、自动化产线。

## 供应链位置

- **上游关键零部件/材料**：IGBT、MOS 管、PCB、铜线、铝壳、编码器芯片、磁材、DSP/ARM 控制芯片。
- **下游客户/应用场景**：工业机器人厂商、人形机器人整机厂、3C 电子、半导体设备、机床、物流自动化。
- **主要竞争对手/对标**：汇川技术、安川、三菱、松下、西门子。

## 知识图谱节点与关系

- 公司实体：`ent_company_delta_electronics`
- 产品实体：`ent_component_delta_asda_b3`、`ent_component_delta_ecma`
- 关键关系：
  - `ent_company_delta_electronics` -- `manufactures` --> `ent_component_delta_asda_b3`
  - `ent_company_delta_electronics` -- `manufactures` --> `ent_component_delta_ecma`
  - `ent_component_delta_asda_b3` -- `uses` --> `ent_component_delta_ecma`

## 参考资料

1. [台达官网](https://www.deltaww.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. 台达工业自动化产品手册与年报