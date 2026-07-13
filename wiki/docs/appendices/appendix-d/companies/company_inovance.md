---
id: ent_company_inovance
schema_version: 1
type: company
title: Inovance Technology
domain: 02_components
theoretical_depth: system
names:
  zh: 汇川技术
  en: Inovance Technology
status: active
sources:
  - id: src_inovance_official
    type: website
    title: Inovance Technology Official Website
    url: https://www.inovance.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---

# 汇川技术 / Inovance Technology

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 汇川技术 |
| **英文名** | Inovance Technology |
| **总部** | 中国深圳 |
| **成立时间** | 2003 |
| **官网** | [https://www.inovance.com](https://www.inovance.com) |
| **供应链环节** | 伺服系统 / 电机 / 驱动器 / 变频器 |
| **企业属性** | 国产品牌、上市公司（300124.SZ） |
| **母公司/所属集团** | 无（独立上市） |
| **数据来源** | 官网、产品手册、公开研报、WAIC 2026 报道 |

## 公司简介

中国工业自动化龙头，提供伺服电机、驱动器、PLC 和机器人核心部件。

汇川技术的 MS1 系列伺服电机搭配 SV680 系列高性能伺服驱动，覆盖 50 W–7.5 kW 功率段，支持 23/26 位绝对值编码器，广泛应用于工业机器人、人形机器人和新能源装备。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| MS1 伺服电机 | 高响应伺服电机 | MS1H2 / MS1H3 / MS1H4 | 机器人、机床、锂电 |
| SV680 伺服驱动 | 高端单轴伺服驱动 | SV680P / SV680-INT | 半导体、机器人 |

## 代表产品

### MS1H4-40B30CB 伺服电机 / MS1H4-40B30CB Servo Motor

> MS1H4-40B30CB 伺服电机：请访问 [官方资料](https://www.inovance.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 机座号 | 40 mm | 汇川 SV630P 手册 |
| 额定功率 | 400 W | 汇川 SV630P 手册 |
| 额定转速 | 3000 rpm | 汇川手册 |
| 最高转速 | 6000 rpm | 汇川官网 |
| 额定扭矩 | 未公开 | - |
| 最大扭矩 | 约 3.5 倍额定扭矩 | 汇川手册（H4 机型） |
| 转子惯量 | 0.43 kg·cm² | 汇川手册 |
| 编码器 | 18 位多圈绝对值（T3） | 汇川手册 |
| 防护等级 | IP67 | 汇川手册 |

**技术亮点**：小惯量、小容量设计，高过载能力，适配机器人小关节和高速定位应用。

**应用场景**：SCARA、协作机器人关节、人形机器人手臂、3C 自动化。

### SV680P 伺服驱动器 / SV680P Servo Drive

> SV680P 伺服驱动器：请访问 [官方资料](https://www.inovance.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 功率范围 | 50 W – 7.5 kW | Inovance 官网 |
| 通信协议 | CANopen / EtherCAT / Pulse | Inovance 官网 |
| 速度环带宽 | 3.5 kHz | Inovance 欧洲官网 |
| 电流环频率 | 625 kHz | Inovance 欧洲官网 |
| 编码器支持 | 23/26 位绝对值、BiSS-C、EnDat 2.2 | Inovance 欧洲官网 |
| 安全功能 | STO / SS1 / SLS 等 SIL3/PL e | Inovance 欧洲官网 |
| 认证 | CE / UL / KC / UKCA / SEMI F47 | Inovance 官网 |

**技术亮点**：高响应、功能安全齐全，适合人形机器人对动态性能和安全性的要求。

**应用场景**：工业机器人、半导体设备、人形机器人关节驱动。

## 供应链位置

- **上游关键零部件/材料**：稀土磁材、IGBT、PCB、铜线、铝壳、编码器芯片
- **下游客户/应用场景**：工业机器人、人形机器人、新能源汽车、光伏/锂电设备厂商
- **主要竞争对手/对标**：禾川科技、雷赛智能、安川、三菱

## 知识图谱节点与关系

- 公司实体：`ent_company_inovance`
- 产品实体：`ent_component_inovance_ms1h4_40b`、`ent_component_inovance_sv680p`
- 关键关系：
  - `ent_company_inovance` -- `manufactures` --> `ent_component_inovance_ms1h4_40b`
  - `ent_company_inovance` -- `manufactures` --> `ent_component_inovance_sv680p`

## 参考资料

1. [官网](https://www.inovance.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.inovance.com)（请按实际产品型号核对）