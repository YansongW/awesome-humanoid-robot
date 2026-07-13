---
id: ent_company_googoltech
schema_version: 1
type: company
title: Googol Technology
domain: 02_components
theoretical_depth: system
names:
  zh: 固高科技
  en: Googol Technology
status: active
sources:
  - id: src_googoltech_official
    type: website
    title: Googol Technology Official Website
    url: https://www.googoltech.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---

# 固高科技 / Googol Technology

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 固高科技 |
| **英文名** | Googol Technology |
| **总部** | 中国广东深圳 |
| **成立时间** | 1999 |
| **官网** | [https://www.googoltech.com](https://www.googoltech.com) |
| **供应链环节** | 运动控制器 / 伺服驱动 / 工业软件 |
| **企业属性** | 国产品牌、上市公司（301510.SZ）、运动控制龙头 |
| **母公司/所属集团** | 无（独立上市） |
| **数据来源** | 固高科技官网、产品手册、招股说明书、WAIC 2026 报道 |

## 公司简介

固高科技是中国运动控制技术领域的领军企业，专注于高性能运动控制器、伺服驱动器与工业控制软件。

公司由李泽湘教授等创办，长期深耕运动控制核心算法与软硬件平台，产品覆盖从运动控制卡、控制器到伺服驱动器的完整链条，广泛应用于工业机器人、半导体装备、激光加工、数控机床与人形机器人领域。其开放式控制架构与多轴协同能力在国内高端装备领域具有较强的替代能力。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 运动控制卡/器 | 多轴运动控制 | GT-400 / GUC 系列 | 机器人、CNC、激光 |
| 伺服驱动器 | 高性能伺服驱动 | GSHD 系列 | 工业机器人、人形机器人 |
| 驱控一体机 | 集成电机+驱动 | 未公开 | 协作机器人 |

## 代表产品

### GSHD 系列伺服驱动器 / GSHD Series Servo Drive

> GSHD 系列伺服驱动器：请访问 [官方资料](https://www.googoltech.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品形态 | 单轴/多轴交流伺服驱动器 | 固高科技官网 |
| 功率范围 | 100 W – 7.5 kW | 产品手册 |
| 输入电压 | 单相/三相 220 VAC / 380 VAC | 产品手册 |
| 控制模式 | 位置/速度/转矩 | 产品手册 |
| 通信协议 | EtherCAT / CANopen | 产品手册 |
| 速度环带宽 | 未公开 | - |
| 编码器支持 | 17/23 位绝对值、BiSS-C | 产品手册 |
| 安全功能 | STO（部分型号） | 产品手册 |
| 价格 | 未公开 | 需询价 |

**技术亮点**：高集成度、多轴协同能力强，适配机器人高动态力控与复杂轨迹规划。

**应用场景**：工业机器人、人形机器人关节、半导体设备、激光加工、数控机床。

### GT-400 运动控制卡 / GT-400 Motion Control Card

> GT-400 运动控制卡：请访问 [官方资料](https://www.googoltech.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品形态 | 多轴运动控制卡 | 固高科技官网 |
| 控制轴数 | 2/4 轴（视型号） | 产品手册 |
| 控制方式 | 点位 / 连续轨迹 / 电子齿轮 | 产品手册 |
| 接口 | PCI / 端子板 | 产品手册 |
| 编码器输入 | 4 路 ABZ 增量式 | 产品手册 |
| 价格 | 未公开 | 需询价 |

**技术亮点**：开放式架构、丰富的运动控制函数库，广泛用于高校研究与工业设备原型开发。

**应用场景**：机器人控制平台、数控机床、激光切割机、半导体设备。

## 供应链位置

- **上游关键零部件/材料**：DSP/ARM 控制芯片、FPGA、IGBT、PCB、编码器芯片、电容、磁材。
- **下游客户/应用场景**：工业机器人厂商、人形机器人整机厂、半导体设备、激光设备、数控机床。
- **主要竞争对手/对标**：汇川技术、雷赛智能、柏楚电子、PMAC、固高自研生态。

## 知识图谱节点与关系

- 公司实体：`ent_company_googoltech`
- 产品实体：`ent_component_googoltech_gshd`、`ent_component_googoltech_gt400`
- 关键关系：
  - `ent_company_googoltech` -- `manufactures` --> `ent_component_googoltech_gshd`
  - `ent_company_googoltech` -- `manufactures` --> `ent_component_googoltech_gt400`

## 参考资料

1. [固高科技官网](https://www.googoltech.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. 固高科技招股说明书与产品手册