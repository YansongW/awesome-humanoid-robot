---
id: ent_company_xinje
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 信捷电气
  en: 信捷电气
status: active
sources:
- id: src_xinje_official
  type: website
  url: https://www.xinje.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---





# 信捷电气 / 信捷电气

# 信捷电气 / Xinje Electric

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 信捷电气 |
| **英文名** | Xinje Electric |
| **总部** | 中国江苏无锡 |
| **成立时间** | 2008 |
| **官网** | [https://www.xinje.com](https://www.xinje.com) |
| **供应链环节** | PLC / 伺服系统 / HMI / 变频器 |
| **企业属性** | 国产品牌、上市公司（603416.SH） |
| **母公司/所属集团** | 无（独立上市） |
| **数据来源** | 信捷官网、产品手册、年报、WAIC 2026 报道 |

## 公司简介

信捷电气是中国小型 PLC 与伺服系统领域的重要厂商，产品以高性价比、易用性和快速交付见长。

公司核心产品包括 XD/XL 系列 PLC、DS 系列伺服驱动器、触摸屏与变频器，广泛应用于 3C、包装、纺织、机床与人形机器人关节驱动。信捷通过自主研发的 PLC 平台与伺服算法，持续向中高端运动控制市场渗透。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| DS 系列伺服系统 | 通用伺服驱动+电机 | DS5 / DS3 | 自动化、机器人 |
| XD/XL 系列 PLC | 小型/中型可编程控制器 | XD3 / XD5 / XL1 | 产线控制 |
| HMI/触摸屏 | 人机界面 | TGA62 / TG765 | 设备操作面板 |

## 代表产品

### DS5 系列伺服驱动器 / DS5 Series Servo Drive

> DS5 系列伺服驱动器：请访问 [官方资料](https://www.xinje.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品形态 | 单轴交流伺服驱动器 | 信捷官网 |
| 功率范围 | 100 W – 7.5 kW | 产品手册 |
| 输入电压 | 单相/三相 220 VAC / 380 VAC | 产品手册 |
| 控制模式 | 位置/速度/转矩 | 产品手册 |
| 通信协议 | Modbus / CANopen / EtherCAT | 产品手册 |
| 速度环带宽 | 2.5 kHz（参考） | 产品手册 |
| 编码器支持 | 17/23 位绝对值 | 产品手册 |
| 价格 | 未公开 | 需询价 |

**技术亮点**：调试简便、响应快、与信捷 PLC/HMI 生态深度集成，适合中小型自动化与机器人关节。

**应用场景**：工业机器人、人形机器人、包装机械、纺织机械、3C 自动化。

### MS6 系列伺服电机 / MS6 Series Servo Motor

> MS6 系列伺服电机：请访问 [官方资料](https://www.xinje.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品形态 | 交流伺服电机 | 信捷官网 |
| 机座号 | 40–180 mm | 产品手册 |
| 额定功率 | 50 W – 7.5 kW | 产品手册 |
| 额定转速 | 1000–6000 rpm | 产品手册 |
| 编码器 | 17/23 位绝对值 | 产品手册 |
| 价格 | 未公开 | 需询价 |

**技术亮点**：低惯量设计、高过载能力，与 DS5 系列驱动器配套使用。

**应用场景**：自动化产线、机器人关节、数控机床、输送设备。

## 供应链位置

- **上游关键零部件/材料**：IGBT、MOS 管、PCB、电容、铜线、铝壳、编码器芯片、磁材、DSP/ARM 控制芯片。
- **下游客户/应用场景**：自动化设备厂商、工业机器人厂商、人形机器人整机厂、3C 电子、包装纺织。
- **主要竞争对手/对标**：汇川技术、台达、三菱、欧姆龙、雷赛智能。

## 知识图谱节点与关系

- 公司实体：`ent_company_xinje`
- 产品实体：`ent_component_xinje_ds5`、`ent_component_xinje_ms6`
- 关键关系：
  - `ent_company_xinje` -- `manufactures` --> `ent_component_xinje_ds5`
  - `ent_company_xinje` -- `manufactures` --> `ent_component_xinje_ms6`
  - `ent_component_xinje_ds5` -- `uses` --> `ent_component_xinje_ms6`

## 参考资料

1. [信捷电气官网](https://www.xinje.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. 信捷电气年报与产品手册