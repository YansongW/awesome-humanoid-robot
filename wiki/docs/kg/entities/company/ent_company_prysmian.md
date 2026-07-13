---
id: ent_company_prysmian
schema_version: 1
type: company
'title:': 普睿司曼 / Prysmian Group
domain: 02_components
theoretical_depth: system
names:
  zh: 普睿司曼
  en: Prysmian Group
status: active
sources:
- id: src_prysmian_official
  type: website
  url: https://www.prysmiangroup.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 普睿司曼 / Prysmian Group

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 普睿司曼 |
| **英文名** | Prysmian Group |
| **总部** | 意大利米兰 |
| **成立时间** | 1879（前身 Pirelli Cavi） |
| **官网** | [https://www.prysmiangroup.com](https://www.prysmiangroup.com) |
| **供应链环节** | 电力电缆、通信电缆、工业特种电缆 |
| **企业属性** | 上市公司（BIT: PRY） |
| **母公司/所属集团** | 独立上市 |
| **数据来源** | 官网、年报、产品 catalog |

## 公司简介

Prysmian Group 是全球最大的电缆系统制造商之一，产品覆盖能源、通信、建筑与工业特种电缆。其机器人/拖链电缆与柔性电缆可满足高动态、耐扭转、耐油、耐化学腐蚀的机器人应用需求。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| Flexibot / 机器人电缆 | 高柔性动力/控制电缆 | Flexibot 系列 | 工业机器人、协作机器人 |
| Afumex 电缆 | 低烟无卤电缆 | Afumex Green Power | 建筑、新能源 |
| Sicon 电缆 | 工业通信/数据电缆 | Sicon 系列 | 工业网络、传感器 |

## 代表产品

### Prysmian Group Flexibot 机器人电缆

> Prysmian Group Flexibot 机器人电缆：请访问 [官方资料](https://www.prysmiangroup.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 芯线数 | 按定制（常见 4G1.5 mm²） | 官方 catalog |
| 额定电流 | 未公开 | 官方 datasheet |
| 额定电压 | 300/500 V | 产品资料 |
| 防护等级 | IP65（成品线缆组件） | 产品资料 |
| 耐扭转 | ±180°/m（典型） | 产品资料 |
| 护套材质 | PUR | 产品资料 |
| 应用场景 | 工业机器人、协作机器人、人形机器人关节 | 产品资料 |
| 价格 | 未公开 | 未公开 |

**技术亮点**：PUR 外护套耐油、耐磨、耐弯曲，支持扭转与拖链运动，适合机器人动力与信号传输。

**应用场景**：机器人关节、焊接机器人、搬运机器人、协作机器人、人形机器人整机布线。

### Prysmian Group Afumex Green Power 电缆

> Prysmian Group Afumex Green Power 电缆：请访问 [官方资料](https://www.prysmiangroup.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 芯线数 | 按定制 | 官方 catalog |
| 额定电流 | 未公开 | 官方 datasheet |
| 额定电压 | 0.6/1 kV | 产品资料 |
| 防护等级 | IP 未公开 | 产品资料 |
| 阻燃/烟密 | 低烟无卤 | 产品资料 |
| 应用场景 | 建筑、新能源、充电设施 | 产品资料 |
| 价格 | 未公开 | 未公开 |

**技术亮点**：低烟无卤、阻燃、环保，适合公共建筑与新能源基础设施。

**应用场景**：数据中心、充电站、建筑配电、新能源电站。

## 供应链位置

- **上游关键零部件/材料**：铜/铝导体、XLPE/PVC/PUR 绝缘料、屏蔽材料、铠装材料
- **下游客户/应用场景**：电力、通信、建筑、新能源、机器人、汽车
- **主要竞争对手/对标**：LEONI、Nexans、NKT、Lapp、Igus

## 知识图谱节点与关系

- 公司实体：`ent_company_prysmian`
- 产品实体：`ent_product_prysmian_flexibot`
- 零部件实体：`ent_component_prysmian_flexibot`
- 关键关系：
  - `rel_ent_company_prysmian_manufactures_ent_product_prysmian_flexibot`（`ent_company_prysmian` → `manufactures` → `ent_product_prysmian_flexibot`）
  - `rel_ent_company_prysmian_manufactures_ent_component_prysmian_flexibot`（`ent_company_prysmian` → `manufactures` → `ent_component_prysmian_flexibot`）

## 参考资料

1. [官网](https://www.prysmiangroup.com)
2. 产品 datasheet 与公开技术报道
3. [附录 D 产品目录](../../../appendices/appendix-d/index-products.md)