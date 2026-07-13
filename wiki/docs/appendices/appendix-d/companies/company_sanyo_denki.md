---
id: ent_company_sanyo_denki
schema_version: 1
type: company
title: Sanyo Denki
domain: 02_components
theoretical_depth: system
names:
  zh: 山洋电气
  en: Sanyo Denki
status: active
sources:
  - id: src_sanyo_denki_official
    type: website
    title: Sanyo Denki Official Website
    url: https://www.sanyodenki.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---

# 山洋电气 / Sanyo Denki

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 山洋电气 |
| **英文名** | Sanyo Denki |
| **总部** | 日本东京 |
| **成立时间** | 1927 |
| **官网** | [https://www.sanyodenki.com](https://www.sanyodenki.com) |
| **供应链环节** | 伺服系统 / 冷却风扇 / 电源 / 运动控制 |
| **企业属性** | 外资品牌、上市公司（TSE 6516） |
| **母公司/所属集团** | 无（独立上市） |
| **数据来源** | 山洋官网、产品手册、公开研报、WAIC 2026 报道 |

## 公司简介

山洋电气是日本老牌伺服系统与冷却设备制造商，以高可靠性、小型化与低噪音设计著称。

其 SANMOTION 系列伺服电机与驱动器广泛应用于半导体设备、医疗设备、机器人与精密自动化。山洋电气在小型高响应伺服、无刷电机与冷却风扇领域技术领先，是高端人形机器人与精密设备零部件的重要供应商。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| SANMOTION R 伺服 | 高性能交流伺服 | SANMOTION R | 半导体、医疗、机器人 |
| SANMOTION G 伺服 | 通用型伺服 | SANMOTION G | 自动化、机床 |
| 冷却风扇/电源 | 散热与供电 | 9S 系列风扇 | 服务器、工业设备 |

## 代表产品

### SANMOTION R 系列伺服电机 / SANMOTION R Series Servo Motor

> SANMOTION R 系列：请访问 [官方资料](https://www.sanyodenki.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品形态 | 交流伺服电机 | 山洋官网 |
| 机座号 | 20–130 mm（视型号） | 产品手册 |
| 额定功率 | 10 W – 5 kW | 产品手册 |
| 额定转速 | 1000–6000 rpm | 产品手册 |
| 编码器 | 20 位绝对值（参考） | 产品手册 |
| 防护等级 | IP65（部分型号） | 产品手册 |
| 价格 | 未公开 | 需询价 |

**技术亮点**：体积小、响应快、低速平稳，适合机器人手指、腕部等空间受限关节。

**应用场景**：半导体设备、医疗机器人、协作机器人、人形机器人手指/腕部。

### SANMOTION R ADVANCED 伺服驱动器 / SANMOTION R ADVANCED Servo Drive

> SANMOTION R ADVANCED：请访问 [官方资料](https://www.sanyodenki.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品形态 | 单轴交流伺服驱动器 | 山洋官网 |
| 功率范围 | 10 W – 5 kW | 产品手册 |
| 通信协议 | EtherCAT / MECHATROLINK / CANopen | 产品手册 |
| 控制模式 | 位置/速度/转矩 | 产品手册 |
| 编码器支持 | 20/23 位绝对值 | 产品手册 |
| 安全功能 | STO（部分型号） | 产品手册 |
| 价格 | 未公开 | 需询价 |

**技术亮点**：高响应、高分辨率反馈、支持多种工业总线，适配精密运动与力控应用。

**应用场景**：半导体设备、医疗机器人、人形机器人关节、精密定位平台。

## 供应链位置

- **上游关键零部件/材料**：稀土磁材、IGBT、PCB、铜线、铝壳、编码器芯片、轴承、DSP/ARM 控制芯片。
- **下游客户/应用场景**：半导体设备商、医疗机器人厂商、人形机器人整机厂、精密自动化设备商。
- **主要竞争对手/对标**：安川、松下、三菱、汇川技术、禾川科技。

## 知识图谱节点与关系

- 公司实体：`ent_company_sanyo_denki`
- 产品实体：`ent_component_sanyo_sanmotion_r_motor`、`ent_component_sanyo_sanmotion_r_drive`
- 关键关系：
  - `ent_company_sanyo_denki` -- `manufactures` --> `ent_component_sanyo_sanmotion_r_motor`
  - `ent_company_sanyo_denki` -- `manufactures` --> `ent_component_sanyo_sanmotion_r_drive`
  - `ent_component_sanyo_sanmotion_r_drive` -- `uses` --> `ent_component_sanyo_sanmotion_r_motor`

## 参考资料

1. [山洋电气官网](https://www.sanyodenki.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. 山洋电气产品手册与年报