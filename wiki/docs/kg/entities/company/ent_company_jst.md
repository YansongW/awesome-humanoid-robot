---
id: ent_company_jst
schema_version: 1
type: company
'title:': 日本压着端子制造 / J.S.T.
domain: 02_components
theoretical_depth: system
names:
  zh: 日本压着端子制造
  en: J.S.T.
status: active
sources:
- id: src_jst_official
  type: website
  url: https://www.jst-mfg.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 日本压着端子制造 / J.S.T.

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 日本压着端子制造 |
| **英文名** | J.S.T. |
| **总部** | 日本大阪府堺市 |
| **成立时间** | 1957 |
| **官网** | [https://www.jst-mfg.com](https://www.jst-mfg.com) |
| **供应链环节** | 压着端子、连接器、线束 |
| **企业属性** | 上市公司（东证 Standard: 7701） |
| **母公司/所属集团** | 独立上市 |
| **数据来源** | 官网、产品 datasheet、公开资料 |

## 公司简介

J.S.T.（日本压着端子制造株式会社）是全球最大的压着端子与连接器制造商之一，PH、XH、SM、ZH 等标准系列在消费与工业电子中应用极广，亦大量用于机器人内部信号与电源连接。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| PH 系列 | 2.0 mm 通用连接 | JST PH | 小型电机、传感器、控制器 |
| XH 系列 | 2.5 mm 通用连接 | JST XH | 家电、机器人电源 |
| SM / VH 系列 | 线对线/大电流 | SM / VH | 电池、功率分配 |

## 代表产品

### JST PH 系列 2.0 mm 线对板连接器

> JST PH 系列 2.0 mm 线对板连接器：请访问 [官方资料](https://www.jst-mfg.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 引脚数 | 2 – 16（可选） | 官方 catalog |
| 额定电流 | 未公开 | 官方 datasheet |
| 额定电压 | 未公开 | 官方 datasheet |
| 防护等级 | IP20 | 产品资料 |
| 间距 | 2.0 mm | 官方 catalog |
| 应用场景 | 小型电机、传感器、控制器、无人机 | 产品资料 |
| 价格 | 未公开 | 未公开 |

**技术亮点**：成本低廉、规格齐全、兼容广泛，是机器人和航模中最常用的信号连接器之一。

**应用场景**：机器人舵机、编码器、LED/指示灯、小功率风扇、传感器。

### JST XH 系列 2.5 mm 线对板连接器

> JST XH 系列 2.5 mm 线对板连接器：请访问 [官方资料](https://www.jst-mfg.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 引脚数 | 2 – 20（可选） | 官方 catalog |
| 额定电流 | 未公开 | 官方 datasheet |
| 额定电压 | 未公开 | 官方 datasheet |
| 防护等级 | IP20 | 产品资料 |
| 间距 | 2.5 mm | 官方 catalog |
| 应用场景 | 机器人电源、电池包、工业控制器 | 产品资料 |
| 价格 | 未公开 | 未公开 |

**技术亮点**：2.5 mm 间距承载更大电流，结构简单，适合电源与低速信号。

**应用场景**：机器人电池连接、电源分配板、低功率电机、工业控制器。

## 供应链位置

- **上游关键零部件/材料**：磷青铜、黄铜、PBT/尼龙、电镀材料、线缆
- **下游客户/应用场景**：消费电子、家电、汽车、工业机器人、无人机
- **主要竞争对手/对标**：Hirose、Molex、TE Connectivity、Amphenol、JAE

## 知识图谱节点与关系

- 公司实体：`ent_company_jst`
- 产品实体：`ent_product_jst_ph`
- 零部件实体：`ent_component_jst_ph`
- 关键关系：
  - `rel_ent_company_jst_manufactures_ent_product_jst_ph`（`ent_company_jst` → `manufactures` → `ent_product_jst_ph`）
  - `rel_ent_company_jst_manufactures_ent_component_jst_ph`（`ent_company_jst` → `manufactures` → `ent_component_jst_ph`）

## 参考资料

1. [官网](https://www.jst-mfg.com)
2. 产品 datasheet 与公开技术报道
3. [附录 D 产品目录](../../../appendices/appendix-d/index-products.md)