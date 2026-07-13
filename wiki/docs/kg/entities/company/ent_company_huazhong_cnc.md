---
id: ent_company_huazhong_cnc
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 华中数控
  en: 华中数控
status: active
sources:
- id: src_huazhong_cnc_official
  type: website
  url: https://www.huazhongcnc.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---





# 华中数控 / 华中数控

# 华中数控 / Huazhong CNC

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 华中数控 |
| **英文名** | Huazhong CNC |
| **总部** | 中国湖北武汉 |
| **成立时间** | 1994 |
| **官网** | [https://www.huazhongcnc.com](https://www.huazhongcnc.com) |
| **供应链环节** | CNC 数控系统 / 伺服驱动 / 工业机器人 |
| **企业属性** | 国产品牌、上市公司（300161.SZ） |
| **母公司/所属集团** | 武汉华中科技大产业集团（早期背景） |
| **数据来源** | 华中数控官网、产品手册、年报、WAIC 2026 报道 |

## 公司简介

华中数控是中国数控系统与工业机器人的核心供应商，依托华中科技大学技术背景，长期深耕高端数控系统、伺服驱动与机器人控制。

公司以 HNC 系列数控系统为代表，在国产高端数控系统市场占据重要地位，同时布局工业机器人与伺服电机。其自主可控的数控平台与伺服驱动技术在航空航天、汽车制造、3C 加工与人形机器人核心零部件领域均有应用。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| HNC 数控系统 | 中高端 CNC 系统 | HNC-818D / HNC-848D | 机床、航空航天 |
| 伺服驱动/电机 | 进给轴/主轴驱动 | HSJ 系列 | 机床、机器人 |
| 工业机器人 | 六轴/协作机器人 | 未公开 | 焊接、搬运 |

## 代表产品

### HNC-818D 数控系统 / HNC-818D CNC System

> HNC-818D 数控系统：请访问 [官方资料](https://www.huazhongcnc.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品形态 | 全功能数控系统 | 华中数控官网 |
| 控制轴数 | 最多 9 轴（视配置） | 产品手册 |
| 联动轴数 | 5 轴联动 | 产品手册 |
| 插补周期 | 1 ms / 0.5 ms（参考） | 产品手册 |
| 通信接口 | Ethernet / RS232 / USB | 产品手册 |
| 编程语言 | G 代码 / 宏程序 / 对话式 | 产品手册 |
| 适配电机 | 交流伺服电机 / 主轴电机 | 产品手册 |
| 价格 | 未公开 | 需询价 |

**技术亮点**：自主可控数控内核、五轴联动、高速高精插补，适配高端机床与复杂曲面加工。

**应用场景**：航空航天零件加工、汽车模具、精密零部件制造、复杂曲面加工。

### HSJ 系列伺服驱动器 / HSJ Series Servo Drive

> HSJ 系列伺服驱动器：请访问 [官方资料](https://www.huazhongcnc.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品形态 | 交流伺服驱动器 | 华中数控官网 |
| 功率范围 | 100 W – 7.5 kW | 产品手册 |
| 控制模式 | 位置/速度/转矩 | 产品手册 |
| 通信协议 | Modbus / CANopen | 产品手册 |
| 编码器支持 | 17/23 位绝对值 | 产品手册 |
| 价格 | 未公开 | 需询价 |

**技术亮点**：与 HNC 数控系统深度集成，支持高刚性进给与高速主轴控制。

**应用场景**：数控机床、工业机器人、人形机器人关节驱动。

## 供应链位置

- **上游关键零部件/材料**：工业计算机、显示面板、IGBT、PCB、编码器芯片、伺服电机、轴承、磁材。
- **下游客户/应用场景**：机床厂、航空航天制造、汽车零部件、3C 加工、人形机器人整机厂。
- **主要竞争对手/对标**：发那科、西门子、广州数控、科德数控、海德汉。

## 知识图谱节点与关系

- 公司实体：`ent_company_huazhong_cnc`
- 产品实体：`ent_component_huazhong_hnc_818d`、`ent_component_huazhong_hsj`
- 关键关系：
  - `ent_company_huazhong_cnc` -- `manufactures` --> `ent_component_huazhong_hnc_818d`
  - `ent_company_huazhong_cnc` -- `manufactures` --> `ent_component_huazhong_hsj`

## 参考资料

1. [华中数控官网](https://www.huazhongcnc.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. 华中数控年报与产品手册