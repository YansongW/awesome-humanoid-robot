---
id: ent_company_hcfa
schema_version: 1
type: company
title: HCFA
domain: 02_components
theoretical_depth: system
names:
  zh: 禾川科技
  en: HCFA
status: active
sources:
  - id: src_hcfa_official
    type: website
    title: HCFA Official Website
    url: https://www.hcfa.cn
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---

# 禾川科技 / HCFA

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 禾川科技 |
| **英文名** | HCFA |
| **总部** | 中国浙江龙游 |
| **成立时间** | 2011 |
| **官网** | [https://www.hcfa.cn](https://www.hcfa.cn) |
| **供应链环节** | 伺服系统 / 电机 / 驱动器 / 控制器 |
| **企业属性** | 国产品牌、上市公司（688320.SH） |
| **母公司/所属集团** | 无（独立上市） |
| **数据来源** | 官网、产品手册、公开研报、WAIC 2026 报道 |

## 公司简介

国内通用伺服和机器人核心零部件供应商，提供伺服电机、驱动器、PLC 和一体化关节模组。

禾川科技 X3E/X5E 系列伺服系统覆盖 100 W–7.5 kW，支持 EtherCAT、PROFINET、CANopen 等总线，编码器最高 20 位，产品广泛应用于机器人、光伏、锂电和物流自动化。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| X3E 伺服系统 | 经济型通用伺服 | SV-X3E + X3E 电机 | 机器人、3C、光伏 |
| X5E 伺服系统 | 高性能总线伺服 | SV-X5E | 锂电、半导体、人形机器人 |

## 代表产品

### X3E 系列伺服电机 / X3E Series Servo Motor

> X3E 系列伺服电机：请访问 [官方资料](https://www.hcfa.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 功率范围 | 50 W – 2 kW | HCFA X3E 手册 |
| 额定转速 | 3000 rpm | HCFA X3E 手册 |
| 编码器 | 17 位绝对值磁编 / 增量式 | HCFA X3E 手册 |
| 防护等级 | IP65 | HCFA 企业公告 |
| 额定扭矩 | 未公开 | - |
| 过载能力 | 未公开 | - |
| 电压等级 | AC 200–230 V | HCFA X3E 手册 |

**技术亮点**：经济型高可靠伺服电机，适配通用自动化和机器人关节。

**应用场景**：3C 自动化、包装机械、AGV、协作机器人。

### SV-X5E 伺服驱动器 / SV-X5E Servo Drive

> SV-X5E 伺服驱动器：请访问 [官方资料](https://www.hcfa.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 功率范围 | 100 W – 7.5 kW | HCFA 2024 年报 |
| 电压等级 | 220 V / 380 V | HCFA 2024 年报 |
| 通信协议 | EtherCAT / PROFINET / CANopen / Modbus | HCFA 2024 年报 |
| 控制方式 | 脉冲 / 总线 / 全闭环 | HCFA 2024 年报 |
| 安全功能 | STO、动态刹车、堵转保护 | HCFA 2024 年报 |
| 防护 | 独立风道、三防漆 | HCFA 2024 年报 |

**技术亮点**：高性能总线型伺服驱动，支持多轴协同与机器人高速响应。

**应用场景**：工业机器人、人形机器人、锂电/光伏产线、高端数控。

## 供应链位置

- **上游关键零部件/材料**：稀土磁材、IGBT、PCB、芯片、结构件
- **下游客户/应用场景**：工业机器人、人形机器人、光伏、锂电、物流设备厂商
- **主要竞争对手/对标**：汇川技术、雷赛智能、安川、松下

## 知识图谱节点与关系

- 公司实体：`ent_company_hcfa`
- 产品实体：`ent_component_hcfa_x3e_motor`、`ent_component_hcfa_x5e_drive`
- 关键关系：
  - `ent_company_hcfa` -- `manufactures` --> `ent_component_hcfa_x3e_motor`
  - `ent_company_hcfa` -- `manufactures` --> `ent_component_hcfa_x5e_drive`

## 参考资料

1. [官网](https://www.hcfa.cn)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.inovance.com)（请按实际产品型号核对）