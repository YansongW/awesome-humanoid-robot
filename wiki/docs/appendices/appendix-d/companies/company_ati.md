# ATI Industrial Automation / ATI Industrial Automation

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | ATI Industrial Automation |
| **英文名** | ATI Industrial Automation |
| **总部** | 美国北卡罗来纳州 Apex（罗利附近） |
| **成立时间** | 1989 |
| **官网** | [https://www.ati-ia.com](https://www.ati-ia.com) |
| **供应链环节** | 六维力/力矩传感器、机器人末端执行器、碰撞传感器 |
| **企业属性** | 私有公司、Novanta 子公司（2021 年收购） |
| **母公司/所属集团** | Novanta Inc.（NASDAQ: NOVT） |
| **数据来源** | 官网、Novanta 收购公告、产品 datasheet |

## 公司简介

ATI 是全球领先的六维力/力矩传感器与机器人末端执行器供应商，产品广泛用于工业、协作与医疗机器人。

ATI 提供 Nano、Mini、Gamma、Delta 等系列的六维力/力矩传感器，以及工具快换、碰撞传感器等末端执行器。其硅应变计技术具有高信噪比、高过载能力，可用于机器人精密装配、打磨、医疗手术与力控操作。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| Nano 系列 | 微型六维力传感器 | Nano17 / Nano25 / Nano43 | 协作机器人、医疗机器人、指端力研究 |
| Mini 系列 | 小型六维力传感器 | Mini40 / Mini45 / Mini58 | 机器人装配、打磨、测试 |
| 工具快换与碰撞传感器 | 末端执行器 | QC 系列 / Collision Sensor | 自动化产线、协作机器人 |

## 代表产品

### ATI Nano25

> ATI Nano25：请访问 [官方资料](https://www.ati-ia.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 直径 | 25 mm | 官方 datasheet |
| 高度 | 21.6 mm | 官方 datasheet |
| 重量 | 63.4 g | 官方 datasheet |
| 力测量范围（Fx/Fy） | ±250 N | 官方 datasheet |
| 力测量范围（Fz） | ±1000 N | 官方 datasheet |
| 力矩测量范围（Tx/Ty/Tz） | ±6 Nm / ±3.4 Nm | 官方 datasheet |
| 单轴过载能力 | 额定量程的 7.1 – 15.1 倍 | 官方 datasheet |
| 共振频率 | Fx,Fy,Tz: 3600 Hz；Fz,Tx,Ty: 3800 Hz | 经销商 datasheet |
| 防护等级 | 可选 IP65 / IP68 | 官方 datasheet |
| 输出接口 | 模拟 / DAQ / EtherCAT / Net / TWE / WNet / Controller | 官方 datasheet |
| 价格 | 未公开 | 未公开 |

**技术亮点**：极小尺寸、高刚度、高信噪比硅应变计、超高过载保护，适合人形机器人手腕/脚踝力控。

**应用场景**：协作机器人力控、医疗手术机器人、机器人精密装配、手指力研究、人形机器人关节。

### ATI Mini45

> ATI Mini45：请访问 [官方资料](https://www.ati-ia.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 直径 | 45 mm | 官方 datasheet |
| 高度 | 15.7 mm | 官方 datasheet |
| 重量 | 约 91 g | 官方 datasheet |
| 力测量范围（Fx/Fy） | ±240 N | 官方 datasheet |
| 力测量范围（Fz） | ±660 N | 官方 datasheet |
| 力矩测量范围 | ±12 Nm | 官方 datasheet |
| 接口 | 多种采集系统可选 | 官方 datasheet |
| 价格 | 未公开 | 未公开 |

**技术亮点**：中等尺寸、高动态响应、多种安装方式，是工业机器人手臂末端力控的常用选择。

**应用场景**：机器人打磨、抛光、装配、测试、协作机器人操作。

## 供应链位置

- **上游关键零部件/材料**：高强度不锈钢、硅应变计、信号调理电路、精密机械加工、数据采集系统
- **下游客户/应用场景**：工业机器人、协作机器人、医疗手术机器人、人形机器人、FANUC 等机器人 OEM
- **主要竞争对手/对标**：OnRobot、Robotiq、宇立仪器、坤维科技、海伯森

## 知识图谱节点与关系

- 公司实体：`ent_company_ati`
- 产品实体：`ent_component_ati_nano25`
- 产品实体：`ent_component_ati_mini45`
- 关键关系：
  - `ent_company_ati` -- `manufactures` --> `ent_component_ati_nano25`
  - `ent_company_ati` -- `manufactures` --> `ent_component_ati_mini45`
  - `ent_company_ati` -- `supplies` --> `ent_company_fanuc` (ATI 为 FANUC CRX 协作机器人提供末端执行器套件)

## 参考资料

1. [官网](https://www.ati-ia.com)
2. [产品资料与公开报道](https://www.ati-ia.com)
3. [附录 D 产品目录](../index-products.md)