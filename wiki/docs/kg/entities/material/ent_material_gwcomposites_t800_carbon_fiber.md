---
id: ent_material_gwcomposites_t800_carbon_fiber
schema_version: 1
type: material
domain: 01_raw_materials
theoretical_depth: system
names:
  zh: 光威复材 T800 级碳纤维
  en: GW Composites T800 Carbon Fiber
status: active
aliases:
- T800 carbon fiber
- T800 碳纤维
sources:
- id: src_gwcfc_t800_specs
  type: website
  url: https://www.gwcfc.com/photo/list-56.aspx
- title: 光威复材碳纤维及织物产品参数
- id: src_gwcfc_annual_report
  type: document
  url: http://money.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid=300699&id=10834445
- title: 光威复材公司公告
- id: src_gwcfc_xueqiu_analysis
  type: article
  url: https://xueqiu.com/9885782062/365708909
- title: 光威复材 T800/T1000 产品竞争力分析
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 光威复材 T800 级碳纤维 / GW Composites T800 Carbon Fiber

## 概述

光威复材 T800 级碳纤维是威海光威复合材料股份有限公司生产的高强度高模量聚丙烯腈（PAN）基碳纤维系列，对应国家标准牌号 QZ5526。该系列包括 TZ800H、TZ800S、TZ800G 等多个牌号，丝束规格覆盖 6K、12K、24K，拉伸强度可达 5490–5880 MPa，拉伸弹性模量约 294 GPa，已应用于航空航天、商业航天、汽车轻量化及高端装备结构件。光威复材是国内少数实现 T800 级碳纤维规模化量产并通过中国商飞 PCD 认证的企业之一。

## 物理化学基础

T800 级碳纤维由 PAN 前驱体经氧化稳定、低温碳化、高温碳化及表面处理制成。其微观结构为高度取向的石墨微晶沿纤维轴排列，赋予材料极高的比强度与比模量。

关键性能关系：

1. **比强度**（specific strength）

$$
   \frac{\sigma}{\rho},
   $$

其中 $\sigma$ 为拉伸强度，$\rho$ 为密度（碳纤维约 1.80 g/cm³）。

2. **比模量**（specific modulus）

$$
   \frac{E}{\rho},
   $$

其中 $E$ 为拉伸弹性模量。

3. **断裂伸长率**

$$
   \varepsilon=\frac{\sigma}{E},
   $$

T800H 约为 1.9%，T800S/G 约为 2.0%。

4. **复合材料层合板**：单向预浸料沿纤维方向的弹性模量可由混合律近似

$$
   E_c=E_fV_f+E_m(1-V_f),
   $$

其中 $E_f$、$E_m$ 分别为纤维与基体模量，$V_f$ 为纤维体积分数。

## 关键参数表

| 参数 | TZ800H | TZ800S / TZ800G |
|---|---|---|
| 拉伸强度 | 5490 MPa | 5880 MPa |
| 拉伸弹性模量 | 294 GPa | 294 GPa |
| 断裂伸长率 | 1.9% | 2.0% |
| 对应国标 | QZ5526 | QZ5526 |
| 丝束规格 | 6K / 12K | 6K / 12K / 24K / 36K |
| 生产工艺 | 湿法 / 干湿法 | 湿法 / 干湿法 |
| 密度（典型） | 约 1.80 g/cm³ | 约 1.80 g/cm³ |

## 在机器人系统中的作用

T800 级碳纤维在人形机器人与高端机器人平台中主要用于：

- **结构减重**：用碳纤维复合材料替代铝合金/钢材制作手臂、腿部连杆与机身骨架，可显著降低整机重量、提高负载/自重比与动态响应。
- **高刚度部件**：利用其高比模量提高关键结构件的刚度与固有频率，减少振动。
- **耐疲劳与抗冲击**：适合需要反复运动的机器人肢体与外壳。
- **热管理与电磁兼容**：碳纤维复合材料可用于散热结构与电磁屏蔽设计。

## 供应链关系

- **上游**：PAN 原丝、上浆剂、树脂基体（环氧、双马等）、碳纤维生产设备供应商。
- **同层**：光威复材提供 T800 级碳纤维、织物、预浸料及复合材料制件；子公司拓展纤维负责碳纤维生产，复材科技负责复合材料制品开发。
- **下游**：航空航天主机厂、汽车制造商、风电叶片/碳梁厂商、压力容器制造商以及机器人结构件供应商。

## 来源与验证

- 光威复材碳纤维及织物参数页：https://www.gwcfc.com/photo/list-56.aspx
- 光威复材公司公告（含产品矩阵）：http://money.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid=300699&id=10834445
- 雪球分析报告：https://xueqiu.com/9885782062/365708909