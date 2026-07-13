# 莫仕 / Molex

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 莫仕 |
| **英文名** | Molex |
| **总部** | 美国伊利诺伊州利斯尔（Lisle） |
| **成立时间** | 1938 |
| **官网** | [https://www.molex.com](https://www.molex.com) |
| **供应链环节** | 连接器、线缆组件、天线、传感器 |
| **企业属性** | 私有公司（Koch Industries 子公司） |
| **母公司/所属集团** | Koch Industries |
| **数据来源** | 官网、产品 datasheet、行业报道 |

## 公司简介

Molex 是全球领先的电子连接器与互连解决方案供应商，产品覆盖消费电子、汽车、工业与医疗。其 Micro-Fit、Mini-Fit 与 Brad 工业圆形连接器广泛用于机器人电源、信号与通信连接。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| Micro-Fit 3.0 | 3.0 mm 电源/信号连接 | Micro-Fit 3.0 | 伺服驱动、机器人关节 |
| Brad M12 / M8 | 工业圆形连接器 | Brad M12 8 位 | 工业以太网、传感器 |
| Custom cable assemblies | 定制线束 | 机器人线束 | 整机 OEM、Tier 1 |

## 代表产品

### Molex Micro-Fit 3.0 连接器系统

> Molex Micro-Fit 3.0 连接器系统：请访问 [官方资料](https://www.molex.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 引脚数 | 2 – 24（可选） | 官方 catalog |
| 额定电流 | 未公开 | 官方 datasheet |
| 额定电压 | 未公开 | 官方 datasheet |
| 防护等级 | IP20 | 产品资料 |
| 间距 | 3.00 mm | 官方 catalog |
| 应用场景 | 机器人电源分配、伺服驱动、控制器 I/O | 产品资料 |
| 价格 | 未公开 | 未公开 |

**技术亮点**：3.0 mm 间距兼顾电流承载与空间，提供正向锁扣与极化防呆，适合中功率电源与信号。

**应用场景**：人形机器人关节供电、伺服驱动、电池包、工业控制器。

### Molex Brad M12 工业圆形连接器

> Molex Brad M12 工业圆形连接器：请访问 [官方资料](https://www.molex.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 引脚数 | 4 / 8（可选） | 官方 catalog |
| 额定电流 | 未公开 | 官方 datasheet |
| 额定电压 | 未公开 | 官方 datasheet |
| 防护等级 | IP67 | 产品资料 |
| 接口类型 | M12 D-Code / X-Code | 产品资料 |
| 应用场景 | 工业以太网、传感器、执行器 | 产品资料 |
| 价格 | 未公开 | 未公开 |

**技术亮点**：Brad 系列为工业环境设计，耐腐蚀、抗振动、即插即用，支持 Profinet/EtherNet/IP。

**应用场景**：协作机器人末端工具、工业相机、力传感器、AGV/AMR。

## 供应链位置

- **上游关键零部件/材料**：铜合金、LCP/PBT 塑料、电镀材料、线缆、磁材
- **下游客户/应用场景**：汽车、消费电子、工业自动化、机器人、医疗
- **主要竞争对手/对标**：TE Connectivity、Amphenol、Hirose、JAE、J.S.T.

## 知识图谱节点与关系

- 公司实体：`ent_company_molex`
- 产品实体：`ent_product_molex_micro_fit_3`
- 零部件实体：`ent_component_molex_micro_fit_3`
- 关键关系：
  - `rel_ent_company_molex_manufactures_ent_product_molex_micro_fit_3`（`ent_company_molex` → `manufactures` → `ent_product_molex_micro_fit_3`）
  - `rel_ent_company_molex_manufactures_ent_component_molex_micro_fit_3`（`ent_company_molex` → `manufactures` → `ent_component_molex_micro_fit_3`）

## 参考资料

1. [官网](https://www.molex.com)
2. 产品 datasheet 与公开技术报道
3. [附录 D 产品目录](../index-products.md)