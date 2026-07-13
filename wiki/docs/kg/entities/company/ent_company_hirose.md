---
id: ent_company_hirose
schema_version: 1
type: company
'title:': 广濑电机 / Hirose Electric
domain: 02_components
theoretical_depth: system
names:
  zh: 广濑电机
  en: Hirose Electric
status: active
sources:
- id: src_hirose_official
  type: website
  url: https://www.hirose.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 广濑电机 / Hirose Electric

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 广濑电机 |
| **英文名** | Hirose Electric |
| **总部** | 日本东京都品川区 |
| **成立时间** | 1937 |
| **官网** | [https://www.hirose.com](https://www.hirose.com) |
| **供应链环节** | 连接器、接插件、FPC/FFC 连接器 |
| **企业属性** | 上市公司（东证 Prime: 6806） |
| **母公司/所属集团** | 独立上市 |
| **数据来源** | 官网、产品 datasheet、年报 |

## 公司简介

Hirose Electric 是日本高端连接器制造商，以高密度、高可靠、小型化连接器著称。其 DF、GT、ZE 系列广泛用于无人机、服务机器人、工业相机、伺服编码器与电池管理系统。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| DF13 系列 | 1.25 mm 线对板 | DF13 | 小型伺服、编码器、相机 |
| GT 系列 | 0.8 mm 超小型 | GT8E | 电池、传感器、穿戴设备 |
| ZE05 / ZE064W | 防水连接器 | ZE05 | 户外机器人、电池包 |

## 代表产品

### Hirose DF13 1.25 mm 线对板连接器

> Hirose DF13 1.25 mm 线对板连接器：请访问 [官方资料](https://www.hirose.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 引脚数 | 2 – 40（可选） | 官方 catalog |
| 额定电流 | 未公开 | 官方 datasheet |
| 额定电压 | 未公开 | 官方 datasheet |
| 防护等级 | IP20 | 产品资料 |
| 间距 | 1.25 mm | 官方 catalog |
| 应用场景 | 小型伺服、编码器、工业相机、无人机 | 产品资料 |
| 价格 | 未公开 | 未公开 |

**技术亮点**：小巧可靠、插拔手感好、种类丰富，是小型机器人信号连接的主流选择。

**应用场景**：机器人关节编码器、摄像头模组、IMU、电池 BMS、小型执行器。

### Hirose GT8E 0.8 mm 超小型连接器

> Hirose GT8E 0.8 mm 超小型连接器：请访问 [官方资料](https://www.hirose.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 引脚数 | 2 – 40（可选） | 官方 catalog |
| 额定电流 | 未公开 | 官方 datasheet |
| 额定电压 | 未公开 | 官方 datasheet |
| 防护等级 | IP20 | 产品资料 |
| 间距 | 0.8 mm | 官方 catalog |
| 应用场景 | 电池包、传感器、穿戴式设备 | 产品资料 |
| 价格 | 未公开 | 未公开 |

**技术亮点**：0.8 mm 超小间距，适合空间极受限的机器人末端与传感器。

**应用场景**：人形机器人手指传感器、电池连接、微型摄像头、AR/VR 设备。

## 供应链位置

- **上游关键零部件/材料**：磷青铜、高性能塑料、镀金/镀锡、线缆
- **下游客户/应用场景**：消费电子、汽车电子、工业机器人、无人机、医疗设备
- **主要竞争对手/对标**：J.S.T.、JAE、Molex、Amphenol、TE Connectivity

## 知识图谱节点与关系

- 公司实体：`ent_company_hirose`
- 产品实体：`ent_product_hirose_df13`
- 零部件实体：`ent_component_hirose_df13`
- 关键关系：
  - `rel_ent_company_hirose_manufactures_ent_product_hirose_df13`（`ent_company_hirose` → `manufactures` → `ent_product_hirose_df13`）
  - `rel_ent_company_hirose_manufactures_ent_component_hirose_df13`（`ent_company_hirose` → `manufactures` → `ent_component_hirose_df13`）

## 参考资料

1. [官网](https://www.hirose.com)
2. 产品 datasheet 与公开技术报道
3. [附录 D 产品目录](../../../appendices/appendix-d/index-products.md)