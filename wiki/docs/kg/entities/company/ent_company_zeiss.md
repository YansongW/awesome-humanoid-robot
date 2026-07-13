---
id: ent_company_zeiss
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 卡尔·蔡司
  en: 卡尔·蔡司
status: active
sources:
- id: src_zeiss_official
  type: website
  url: https://www.zeiss.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 卡尔·蔡司 / 卡尔·蔡司

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 卡尔·蔡司 |
| **英文名** | Carl Zeiss |
| **总部** | 德国奥伯科亨（Oberkochen） |
| **成立时间** | 1846 年 |
| **官网** | [https://www.zeiss.com](https://www.zeiss.com) |
| **供应链环节** | 光学、精密测量、三坐标测量机、显微镜、工业质量解决方案 |
| **企业属性** | 基金会持有企业、全球光学与计量龙头 |
| **母公司/所属集团** | 卡尔·蔡司基金会（Carl-Zeiss-Stiftung） |
| **数据来源** | ZEISS 官网、产品手册、公开新闻稿、年报 |

## 公司简介

蔡司是全球光学与光电子领域的领导者，其工业质量解决方案为机器人零部件提供亚微米级几何、表面与材料检测。

卡尔·蔡司业务涵盖半导体制造技术、工业质量与研究、医疗技术与消费品光学。工业质量部门提供三坐标测量机、光学测量系统、显微镜、CT 与表面测量设备，是机器人减速器、轴承、齿轮、连杆等关键零部件高精度检测的核心供应商。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 三坐标测量机 | 接触式高精度几何量测 | PRISMO / ACCURA / CONTURA | 精密零部件、汽车、航空航天 |
| 光学与多测头测量 | 非接触/复合式测量 | O-INSPECT / COMET | 复杂曲面、小批量精密件 |
| 显微镜与表面分析 | 材料与表面微观检测 | Axio / SmarTact / SEM | 材料研发、失效分析 |

## 代表产品

### 蔡司三坐标测量机 / PRISMO 系列

> 蔡司三坐标测量机 / PRISMO 系列：请访问 [官方资料](https://www.zeiss.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 测量范围 | 700×1000×600 mm 起，多种规格 | ZEISS 产品手册 |
| 精度 | MPE_E 可达 0.5 + L/500 µm | ZEISS 产品手册 |
| 探测系统 | VAST gold / RDS 旋转测头座 | ZEISS 产品手册 |
| 软件 | CALYPSO | ZEISS 官网 |
| 结构 | 花岗石、气浮轴承、高刚性桥架 | ZEISS 产品手册 |
| 扫描技术 | 主动扫描测头，支持高速扫描 | ZEISS 产品手册 |
| 接口 | 以太网 | ZEISS 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：亚微米级精度、主动扫描技术、CALYPSO 图形化测量软件、适用于最高精度零部件检测。

**应用场景**：机器人减速器/齿轮/轴承检测、汽车动力总成、航空航天精密件、医疗器械。

### 蔡司 O-INSPECT 复合式测量机

> 蔡司 O-INSPECT 复合式测量机：请访问 [官方资料](https://www.zeiss.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 测量范围 | 300×200×200 mm 起 | ZEISS 产品手册 |
| 精度 | MPE_E 约 1.5 + L/300 µm | ZEISS 产品手册 |
| 传感器 | 接触式测头 + 光学传感器 | ZEISS 产品手册 |
| 光学放大 | 变焦镜头，高分辨率相机 | ZEISS 产品手册 |
| 软件 | CALYPSO | ZEISS 官网 |
| 结构 | 紧凑型桥式结构 | ZEISS 产品手册 |
| 应用 | 小零件复合检测 | ZEISS 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：接触式与光学测量一体化、适合复杂小型零件、高精度影像测量与三维触测结合。

**应用场景**：电子连接器、医疗器械、精密齿轮、机器人微型零部件检测。

## 供应链位置

- **上游关键零部件/材料**：高精度光学元件、光栅尺、气浮轴承、花岗石、测头、工业软件。
- **下游客户/应用场景**：汽车、航空航天、电子半导体、医疗、机器人核心零部件制造商。
- **主要竞争对手/对标**：海克斯康（Hexagon）、温泽、尼康、三丰（Mitutoyo）。

## 知识图谱节点与关系

- 公司实体：`ent_company_zeiss`
- 产品实体：`ent_product_zeiss_prismo`、`ent_product_zeiss_oinspect`
- 关键关系：
  - `ent_company_zeiss` -- `manufactures` --> `ent_product_zeiss_prismo`
  - `ent_company_zeiss` -- `manufactures` --> `ent_product_zeiss_oinspect`
  - `ent_product_zeiss_prismo` -- `uses` --> `ent_component_vast_probe`
  - `ent_product_zeiss_oinspect` -- `uses` --> `ent_component_optical_sensor`

## 参考资料

1. [官网](https://www.zeiss.com)
2. [ZEISS 官网](https://www.zeiss.com)
3. ZEISS PRISMO 与 O-INSPECT 产品手册