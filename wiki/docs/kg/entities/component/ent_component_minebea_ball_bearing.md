---
id: ent_component_minebea_ball_bearing
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 美蓓亚三美微型滚珠轴承
  en: MinebeaMitsumi Miniature Ball Bearing
status: active
sources:
- id: src_ent_component_minebea_ball_bearing_1
  type: website
  url: https://product.minebeamitsumi.com/en/product/category/bearing/miniature_small/parts/DDL2112.html
- id: src_ent_component_minebea_ball_bearing_2
  type: website
  url: https://product.minebeamitsumi.com/en/product/category/bearing/miniature_small/parts/DDL840ZZ.html
- id: src_ent_component_minebea_ball_bearing_3
  type: website
  url: https://product.minebeamitsumi.com/en/download/catalog/category/bearing.html
- id: src_ent_component_minebea_ball_bearing_4
  type: website
  url: https://pibsales.com/bearings/miniature-bearings-for-robot-finger-and-wrist-joints-ensuring-smooth-precise-motion/
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 美蓓亚三美微型滚珠轴承

## 概述

美蓓亚三美（MinebeaMitsumi）微型滚珠轴承是全球市占率领先的精密小径轴承，广泛应用于硬盘驱动器、无人机云台、医疗仪器及机器人关节。其产品以 DDL 系列深沟球轴承为代表，具有尺寸精度高、摩擦低、寿命长、噪音小等特点，是机器人手指、腕部及小型电机转子支撑的关键配套件。

## 工作原理 / 技术架构

深沟球轴承通过内圈、外圈、滚珠与保持架将径向与轴向载荷转化为滚动接触。滚珠与滚道之间的接触应力可由赫兹接触理论描述；在额定动载荷 $C_r$ 与当量动载荷 $P$ 作用下，轴承基本额定寿命（$L_{10}$）为

$$
L_{10} = \left(\frac{C_r}{P}\right)^p \times 10^6\ \mathrm{rev}
$$

对于球轴承，寿命指数 $p=3$；$L_{10}$ 表示 90% 同批轴承在疲劳剥落前可达到的转数。当轴承同时承受径向载荷 $F_r$ 与轴向载荷 $F_a$ 时，当量动载荷 $P$ 可近似为

$$
P = X F_r + Y F_a
$$

其中 $X$、$Y$ 为深沟球轴承的载荷系数，取决于 $F_a/F_r$ 比值。

微型轴承的尺寸紧凑（内径可小至 0.5 mm），但需控制游隙、保持架形状及润滑脂量，以满足高速、低振动与长寿命要求。美蓓亚三美在其 Karuizawa 工厂生产目前吉尼斯认证的最小商用钢球轴承 DDL-004，外径仅 1.50 mm。

## 关键参数表

| 参数项 | 典型值 | 备注/来源 |
|--------|--------|-----------|
| 系列 | DDL 深沟球轴承（微型/小型） | MinebeaMitsumi 产品目录 |
| 内径范围 | 0.5–50 mm | 产品目录（部分型号示例） |
| 外径范围 | 1.5–80 mm | 产品目录 |
| 精度等级 | ABEC-1 至 ABEC-7 | 附录 D / 产品目录 |
| 材质 | 轴承钢 / 不锈钢可选 | 产品目录 |
| 密封形式 | 开式 / 防尘盖 / 橡胶密封（ZZ / 2RS） | 产品目录 |
| DDL-2112 动态载荷 $C_r$ | 1,917 N | MinebeaMitsumi 产品页 |
| DDL-2112 静态载荷 $C_{0r}$ | 1,042 N | MinebeaMitsumi 产品页 |
| DDL-840ZZ 动态载荷 $C_r$ | 391 N | MinebeaMitsumi 产品页 |
| DDL-840ZZ 静态载荷 $C_{0r}$ | 140 N | MinebeaMitsumi 产品页 |
| 润滑方式 | 油脂润滑 / 油润滑 | 未公开具体型号油脂牌号 |
| 价格 | 未公开 | 按型号与批量询价 |

## 应用场景

- **机器人手指关节**：DDL-620ZZ、DDL-730ZZ、DDL-840ZZ 等 2–8 mm 内径微型轴承可直接嵌入指节，提供低摩擦、高精度的弯曲与旋转。
- **电机转子支撑**：伺服电机、空心杯电机转子两端使用微型深沟球轴承，保证高转速下的同心度。
- **无人机云台与精密轴系**：利用低振动、低噪音特性实现稳定成像与定位。
- **医疗设备与光学仪器**：微型轴承用于小型旋转机构与定位平台。

## 供应链关系

美蓓亚三美轴承位于零部件层级。上游为特种钢材、润滑油脂、保持架材料与密封件供应商；中游由 MinebeaMitsumi 设计制造；下游供应给电机厂商、减速器厂商及机器人整机厂。在人形机器人知识图谱中，该实体与 `ent_company_minebea` 存在制造关系，并可被 `ent_product_casbot_01`、`ent_product_limx_oli` 等整机产品的关节模组或电机间接采用。

## 来源与验证

- DDL-2112、DDL-840ZZ 等具体型号的尺寸与载荷数据来自 MinebeaMitsumi 官方产品页。
- 微型轴承在机器人手指关节中的应用示例参考 PIB Sales 技术文章。
- 系列范围与精度等级参考 MinebeaMitsumi 轴承数字目录。