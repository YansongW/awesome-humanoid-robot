---
id: ent_company_csb
schema_version: 1
type: company
'title:': Zhejiang Changsheng Bearing Co., Ltd. (CSB)
domain: 02_components
theoretical_depth: system
names:
  zh: 长盛轴承
  en: Zhejiang Changsheng Bearing Co., Ltd. (CSB)
status: active
sources:
- id: src_csb_official
  type: website
  url: https://www.csb.com.cn
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 长盛轴承 / Zhejiang Changsheng Bearing Co., Ltd. (CSB)

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 长盛轴承 |
| **英文名** | Zhejiang Changsheng Bearing Co., Ltd. (CSB) |
| **总部** | 中国浙江嘉兴 |
| **成立时间** | 1995 |
| **官网** | [https://www.csb.com.cn](https://www.csb.com.cn) |
| **供应链环节** | 自润滑轴承 / 滑动轴承 / 复合材料轴承 |
| **企业属性** | 上市公司（SZ.300718）、国内品牌 |
| **母公司/所属集团** | 浙江长盛滑动轴承股份有限公司 |
| **数据来源** | 官网、年报、产品手册、WAIC 2026 报道 |

## 公司简介

国内自润滑轴承领域龙头，专注于金属-聚合物复合材料滑动轴承的研发与制造。

长盛轴承主营自润滑轴承、滑动轴承轴套、复合材料轴承及关节轴承，产品广泛应用于汽车、工程机械、液压系统、自动化设备及机器人。公司具备材料配方、烧结复合、精密成型等核心工艺能力，可提供免维护、低摩擦、耐磨损的轴承解决方案。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 金属塑料复合轴承 | 自润滑、免维护 | CSB-50 / CSB-40 系列 | 汽车、工程机械 |
| 双金属轴承 | 高承载、耐疲劳 | CSB-800 / CSB-850 系列 | 液压系统、重载设备 |
| 单金属轴承 | 经济型滑动轴承 | CSB-10 / CSB-20 系列 | 通用机械 |
| 纤维缠绕轴承 | 水润滑、耐腐蚀 | CSB-CR 系列 | 船舶、化工、机器人 |

## 代表产品

### 自润滑轴承 / Self-Lubricating Bearing

> 自润滑轴承：请访问 [官方资料](https://www.csb.com.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 内径范围 | 2–300 mm | 产品手册 |
| 外径范围 | 4–340 mm | 产品手册 |
| 宽度范围 | 3–100 mm | 产品手册 |
| 最大载荷 | 140 MPa（静载） | 产品手册 |
| 摩擦系数 | 0.03–0.25 | 产品手册 |
| 工作温度 | -200 °C – +280 °C | 产品手册 |
| 材质 | 钢背 + PTFE / 铜粉 + 聚合物 | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：自润滑免维护、低摩擦、耐粉尘与冲击，适合机器人关节与摆动部位。

**应用场景**：人形机器人关节、谐波减速器、汽车转向系统、液压油缸、工程机械。

### 金属塑料复合轴套 / Metal-Polymer Composite Bushing

> 金属塑料复合轴套：请访问 [官方资料](https://www.csb.com.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 壁厚 | 0.5–2.5 mm | 产品手册 |
| 内径范围 | 2–200 mm | 产品手册 |
| 最大 PV 值 | 2.5 MPa·m/s | 产品手册 |
| 摩擦系数 | 0.05–0.20 | 产品手册 |
| 工作温度 | -40 °C – +130 °C | 产品手册 |
| 材质 | 钢背 + 青铜粉 + PTFE | 产品手册 |
| 精度等级 | 依型号 | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：三层复合结构，兼具钢背强度与 PTFE 自润滑性能，可直接压装使用。

**应用场景**：自动化设备导向套、机器人关节衬套、汽车悬挂、液压阀。

## 供应链位置

- **上游关键零部件/材料**：冷轧钢板、铜粉、PTFE、聚甲醛、烧结炉、精密冲压模具
- **下游客户/应用场景**：汽车 OEM、工程机械、液压件厂商、机器人整机厂、自动化设备
- **主要竞争对手/对标**：GGB、Daido Metal、Oiles、双飞股份、中达精密

## 知识图谱节点与关系

- 公司实体：`ent_company_csb`
- 产品/零部件实体：`ent_component_csb_self_lubricating_bearing`, `ent_component_csb_composite_bushing`
- 关键关系：
  - `ent_company_csb` -- `manufactures` --> `ent_component_csb_self_lubricating_bearing`
  - `ent_company_csb` -- `manufactures` --> `ent_component_csb_composite_bushing`

## 参考资料

1. [长盛轴承官网](https://www.csb.com.cn)
2. [长盛轴承投资者关系](https://www.csb.com.cn/investor/)
3. [WAIC 2026 参展报道](https://www.worldrobotconference.com)