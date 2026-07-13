---
id: ent_component_csb_composite_bushing
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: 长盛 CSB 金属塑料复合轴套
  en: CSB Metal-Polymer Composite Bushing
sources:
- id: src_csb_composite_bushing_datasheet
  type: website
- title: CSB-50 Steel Bronze Powder with PTFE/Fibre Dry Bearings Datasheet
  url: http://www.csbslidingbearings.com/uploads/1/5/6/9/15694310/csb-50.pdf
- id: src_csb_composite_bushing_catalog
  type: website
- title: Metal-Polymer Composite Bearings Catalogue
  url: https://www.csb-bearings.fr/wp-content/uploads/catalogue/Metal-Polymer_Composite_Bearings.pdf
- id: src_csb_company_official
  type: website
- title: 长盛轴承官网
  url: https://www.csb.com.cn
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
  review_notes: Specifications from official product datasheets and catalogues; missing
    values marked as 未公开.
---


# 长盛 CSB 金属塑料复合轴套 / CSB Metal-Polymer Composite Bushing

## 概述

长盛 CSB 金属塑料复合轴套（CSB Metal-Polymer Composite Bushing）是浙江长盛滑动轴承股份有限公司（CSB）生产的自润滑滑动轴承核心产品，以钢背为承载基体、烧结青铜粉为中间层、PTFE/纤维混合物为摩擦表层，形成三层复合结构。该产品无需外部润滑即可在干摩擦或边界润滑条件下运行，广泛应用于汽车、工程机械、液压系统、自动化设备以及人形机器人关节摆动部位。

## 工作原理 / 技术架构

复合轴套的工作机理基于“转移膜润滑”与“多孔储油/储脂”双重效应：

1. **PTFE/纤维表层**：在初始运行阶段，聚四氟乙烯（PTFE）与增强纤维在对偶轴表面形成一层稳定的固体润滑转移膜，显著降低摩擦系数并保护轴颈。
2. **烧结青铜层**：厚度 0.20–0.35 mm 的青铜粉末烧结层一方面将摩擦热快速传导至钢背，另一方面作为 PTFE 混合物的储库，在长时间运行中持续补充润滑物质。
3. **低碳钢背**：提供极高的机械强度与承载能力，并通过过盈配合压装于轴承座孔内。

轴套的 PV 值（压力-速度乘积）是衡量其工作能力的关键指标：

$$
PV = p \cdot v
$$

其中 $p$ 为轴承投影面压（MPa），$v$ 为滑动线速度（m/s）。CSB-50 在连续干运行条件下的额定 PV 值约为 1.8 MPa·m/s，短期峰值可达 3.6 MPa·m/s。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制造商 | 长盛轴承 / CSB | 公司官网 |
| 代表材质 | CSB-50 / CSB-40（钢背 + 青铜粉 + PTFE/纤维） | 产品手册 |
| 结构 | 三层复合：钢背 + 烧结青铜粉 + PTFE/纤维层 | 官方 datasheet |
| PTFE/纤维层厚度 | 0.01–0.03 mm | 官方 datasheet |
| 青铜层厚度 | 0.20–0.35 mm | 官方 datasheet |
| 钢背镀层 | 铜/锡镀层 0.002 mm | 官方 datasheet |
| 最大静载荷 | 250 N/mm² | CSB-50 datasheet |
| 旋转/摆动最大载荷 | 60 N/mm² | CSB-50 datasheet |
| 最大 PV 值（连续干运行） | 1.8 MPa·m/s | 官方 datasheet |
| 最大 PV 值（短期干运行） | 3.6 MPa·m/s | 官方 datasheet |
| 摩擦系数 | 0.03–0.20 | 产品手册 |
| 最高速度 | 2 m/s | 产品手册 |
| 工作温度 | -195 °C – +280 °C | 官方 datasheet |
| 热导率 | 42 W/(m·K) | 官方 datasheet |
| 内径范围 | 2–200 mm | 产品手册 |
| 壁厚范围 | 0.5–2.5 mm | 产品手册 |
| 价格 | 未公开 | 需询价 |

## 应用场景

- **人形机器人关节衬套**：部署于旋转/摆动关节处，承受径向载荷并降低摩擦，减少维护需求。
- **谐波减速器与线性执行器**：作为导向套或支撑衬套，提供自润滑、低磨损的滑动界面。
- **汽车与工程机械**：用于转向系统、悬挂减震器、液压油缸、动力转向缸等需要干运行或油脂润滑的场合。
- **自动化设备**：适用于食品、包装、印刷机械中无法频繁加油的轴承位置。

## 供应链关系

在公司–产品网络中，长盛轴承（`ent_company_csb`）作为上游材料/零部件供应商，制造并销售 CSB 金属塑料复合轴套（`ent_component_csb_composite_bushing`）。其上游原材料包括冷轧钢板、铜粉、PTFE、聚甲醛及烧结炉等；下游客户涵盖汽车 OEM、工程机械厂商、液压件厂、机器人整机厂与自动化设备商。长盛轴承与 GGB、Daido Metal、Oiles、双飞股份等国内外厂商形成竞争关系。在知识图谱中，CSB 复合轴套与长盛自润滑轴承共同构成公司的轴承产品矩阵。

## 来源与验证

- 长盛轴承官方 CSB-50 datasheet 提供了三层结构厚度、载荷、PV 值、摩擦系数、温度范围等核心参数。
- CSB Bearings France 的金属-聚合物复合轴承目录对 CSB-50、CSB-40、CSB-10DH 等材质的参数进行了系统整理。
- 长盛公司年报与投资者关系材料确认了其在机器人轴承领域的布局，但未公开具体型号在人形机器人中的装机比例。