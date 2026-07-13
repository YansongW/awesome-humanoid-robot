---
id: ent_company_infineon
type: company
'title:': Infineon Technologies / 英飞凌
domain: 02_components
theoretical_depth: system
aliases:
- 英飞凌
- Infineon
status: active
created_at: 2026-07-01 00:00:00+00:00
updated_at: 2026-07-09 00:00:00+00:00
sources:
- id: infineon_official
  type: website
  url: https://www.infineon.com
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-09 00:00:00+00:00
---





# infineon

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 英飞凌科技股份公司 |
| **英文名** | Infineon Technologies AG |
| **总部** | 德国纽必堡（Neubiberg） |
| **成立时间** | 1999 年（从西门子半导体部门拆分） |
| **官网** | [https://www.infineon.com](https://www.infineon.com) |
| **供应链环节** | 功率半导体、传感器、微控制器、安全芯片 |
| **企业属性** | 上市公司（法兰克福证交所：IFX） |
| **母公司/所属集团** | 无（独立上市） |
| **数据来源** | Infineon 官网新闻稿、CoolSiC 产品页 |

## 公司简介

英飞凌是全球领先的半导体解决方案供应商，汽车电子和功率半导体市场份额位居前列。

其 CoolSiC™ 碳化硅 MOSFET 与 IGBT 模块广泛应用于电动汽车电驱、光伏逆变器、储能变流器及工业驱动。对于人形机器人，高效率的电机驱动逆变器与电源管理芯片是提升续航和动态响应的核心部件。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 功率 MOSFET | 高效碳化硅功率器件 | CoolSiC™ MOSFET | 电驱逆变器、DC/DC、充电桩 |
| IGBT 模块 | 中高功率电机驱动 | HybridPACK / EconoDUAL | 新能源汽车、工业驱动 |
| 栅极驱动器 | 功率器件驱动 | EiceDRIVER | 逆变器、电源 |

## 代表产品

### CoolSiC™ MOSFET 1200 V / 62 mm 模块

![CoolSiC](https://www.infineon.com/cms/en/product/power/wide-band-gap-semiconductors/sic/sic-mosfets/)


| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 封装 | 62 mm 半桥模块 | Infineon 新闻稿 |
| 电压等级 | 1200 V / 2000 V | Infineon 新闻稿 |
| 导通电阻 | 1 mΩ / 2 mΩ / 5 mΩ 等 | Infineon 新闻稿 |
| 额定电流 | 180 A / 420 A / 560 A | Infineon 新闻稿 |
| 工作结温 | 150 °C（连续） | Infineon 新闻稿 |
| 拓扑 | 半桥 | Infineon 新闻稿 |
| 价格 | 未公开 | 未公开 |

**技术亮点**：基于 M1H 沟槽栅 SiC MOSFET 技术，具有宽栅压窗口、低开关损耗和高功率密度，适用于 250 kW 以上中功率场景。

**应用场景**：电驱逆变器、储能变流器、工业伺服驱动、人形机器人关节电机驱动。

## 与人形机器人的关联

- 电池、功率半导体与先进材料是人形机器人实现长续航、高动态与轻量化的共性基础。
- 工业机器人与自动化产线为人形机器人整机装配、测试与量产提供可复用的制造能力。

## 供应链位置

- **上游关键零部件/材料**：SiC 衬底（SICC、Wolfspeed）、外延片、封装材料、硅晶圆。
- **下游客户/应用场景**：汽车 OEM、光伏/储能逆变器厂商、工业自动化厂商。
- **主要竞争对手/对标**：STMicroelectronics、Wolfspeed、ROHM、Onsemi、Mitsubishi Electric。

## 知识图谱节点与关系

- 公司实体：`ent_company_infineon`
- 产品实体：`ent_component_infineon_coolsic_mosfet`
- 关键关系：
  - `ent_company_infineon` -- `manufactures` --> `ent_component_infineon_coolsic_mosfet`

## 参考资料

1. [Infineon 官网](https://www.infineon.com)
2. [Infineon CoolSiC MOSFET 产品页](https://www.infineon.com/cms/en/product/power/wide-band-gap-semiconductors/sic/sic-mosfets/)
3. [CoolSiC 62mm 模块新闻稿](https://www.infineon.com/cms/en/about-infineon/press/market-news/2023/INFGIP202311-024.html)