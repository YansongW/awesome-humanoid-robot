---
id: ent_company_zhongda
schema_version: 1
type: company
'title:': Zhongda Smart Transmission
domain: 02_components
theoretical_depth: system
names:
  zh: 中大力德
  en: Zhongda Smart Transmission
status: active
sources:
- id: src_zhongda_official
  type: website
  url: https://www.zd-drivers.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 中大力德 / Zhongda Smart Transmission

# 中大力德 / Zhongda Smart Transmission

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 中大力德 |
| **英文名** | Zhongda Smart Transmission |
| **总部** | 中国浙江慈溪 |
| **成立时间** | 1998 |
| **官网** | [https://www.zd-drivers.com](https://www.zd-drivers.com) |
| **供应链环节** | 行星减速器 / RV 减速器 / 谐波减速器 / 电机驱动 |
| **企业属性** | 国产品牌、上市公司（002896.SZ） |
| **母公司/所属集团** | 无（独立上市） |
| **数据来源** | 官网、产品手册、公开研报、WAIC 2026 报道 |

## 公司简介

国内少数同时量产行星/RV/谐波减速器及一体化智能执行单元的企业。

中大力德构建了“减速器 + 电机 + 驱动”一体化产品架构，产品包括精密行星减速器、RV 减速器、谐波减速器和伺服电机，已为宇树科技等机器人企业提供核心传动部件。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| ZDE/ZDF 精密行星减速器 | 经济型精密行星 | 40ZDE / 60ZDE / 80ZDE | 自动化、机器人关节 |
| RV/谐波减速器 | 重载/轻载机器人关节 | RVE / RVC / 谐波系列 | 工业机器人、人形机器人 |

## 代表产品

### 40ZDE-10 精密行星减速器 / 40ZDE-10 Precision Planetary Gearbox

> 40ZDE-10 精密行星减速器：请访问 [官方资料](https://www.zd-drivers.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 机座号 | 40 | 中大力德行星减速器手册 |
| 减速比 | 10:1（单级） | 中大力德行星减速器手册 |
| 输出扭矩 | 4–6 N·m | 五矿证券研报（引用中大力德官网） |
| 回程间隙 | < 12 arcmin | 中大力德手册 |
| 满载效率 | 96% | 中大力德手册 |
| 重量 | 0.4 kg | 中大力德手册 |
| 箱体长度 | 39 mm | 中大力德手册 |
| 防护等级 | IP54 | 中大力德手册 |
| 设计寿命 | 20,000 h | 中大力德手册 |

**技术亮点**：结构紧凑、传动效率高、成本低，适合小负载机器人关节和自动化模组。

**应用场景**：AGV 轮毂、协作机器人关节、人形机器人手指/腕部、3C 自动化。

### RVE/RVC 系列 RV 减速器 / RVE/RVC Series RV Reducer

> RVE/RVC 系列 RV 减速器：请访问 [官方资料](https://www.zd-drivers.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 系列 | RVE / RVC | 环动科技招股书对比 |
| 传动比范围 | 26–192.4:1 | 环动科技招股书 |
| 额定扭矩范围 | 58.8–4900 N·m | 环动科技招股书 |
| 背隙 | < 1.5 arcmin | 环动科技招股书 |
| 传动误差 | < 90 arcsec | 环动科技招股书 |
| 额定效率 | > 78% | 环动科技招股书 |
| 应用 | 工业机器人、工作母机、医疗设备 | 中大力德年报 |

**技术亮点**：高刚性、大扭矩，适配工业机器人基座和大臂等重载关节。

**应用场景**：工业机器人 J1–J3、人形机器人腰/髋部、重型自动化设备。

## 供应链位置

- **上游关键零部件/材料**：合金钢、铝材、轴承、磁材、铜线、驱动芯片
- **下游客户/应用场景**：宇树科技、智元机器人、工业机器人 OEM
- **主要竞争对手/对标**：双环传动、Nabtesco、绿的谐波

## 知识图谱节点与关系

- 公司实体：`ent_company_zhongda`
- 产品实体：`ent_component_zhongda_40zde_10`、`ent_component_zhongda_rv_series`
- 关键关系：
  - `ent_company_zhongda` -- `manufactures` --> `ent_component_zhongda_40zde_10`
  - `ent_company_zhongda` -- `manufactures` --> `ent_component_zhongda_rv_series`
  - `ent_company_zhongda` -- `supplies` --> `ent_company_unitree`

## 参考资料

1. [官网](https://www.zd-drivers.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.inovance.com)（请按实际产品型号核对）