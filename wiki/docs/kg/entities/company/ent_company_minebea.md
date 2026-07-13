---
id: ent_company_minebea
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 美蓓亚三美
  en: 美蓓亚三美
status: active
sources:
- id: src_minebea_official
  type: website
  url: https://www.minebeamitsumi.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 美蓓亚三美 / 美蓓亚三美

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 美蓓亚三美 |
| **英文名** | MinebeaMitsumi Inc. |
| **总部** | 日本长野县 |
| **成立时间** | 1951 |
| **官网** | [https://www.minebeamitsumi.com](https://www.minebeamitsumi.com) |
| **供应链环节** | 微型电机 / 轴承 / 传感器 |
| **企业属性** | 上市公司（TYO.6479）、国际品牌 |
| **母公司/所属集团** | MinebeaMitsumi Inc. |
| **数据来源** | 官网、年报、产品手册、WAIC 2026 报道 |

## 公司简介

全球精密微型电机与轴承综合制造商，产品以高精度、低噪音著称。

美蓓亚三美由美蓓亚（Minebea）与三美电机（Mitsumi）合并而来，业务覆盖微型球轴承、小型电机、LED 背光、传感器与半导体封装。其微型电机广泛应用于硬盘、光驱、无人机、机器人关节等领域，高精度轴承与电机一体化能力为人形机器人提供了关键运动部件。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 微型电机 | 有刷/无刷直流电机、步进电机 | PM 系列、BLDC 系列 | 机器人、汽车、消费电子 |
| 精密轴承 | 微型滚珠轴承 | DDL 系列 | 电机、机器人关节、无人机 |
| 传感器与模组 | 角度/力传感器、触觉模组 | 未公开 | 机器人、汽车、IoT |

## 代表产品

### 微型无刷直流电机 / MinebeaMitsumi Micro BLDC Motor

> 微型无刷直流电机：请访问 [官方资料](https://www.minebeamitsumi.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | Ø10–Ø40 mm（系列范围） | 产品手册 |
| 重量 | 5–120 g（依型号） | 产品手册 |
| 额定电压 | 6–36 VDC | 产品手册 |
| 额定转速 | 3,000–15,000 rpm | 产品手册 |
| 额定扭矩 | 0.3–40 mNm | 产品手册 |
| 效率 | ≥80% | 产品手册 |
| 轴承类型 | 微型滚珠轴承 | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：内置高精度滚珠轴承、低振动、低噪音、长寿命，适合高速精密传动场景。

**应用场景**：人形机器人关节、无人机云台、硬盘驱动器、医疗设备、精密仪器。

### 微型滚珠轴承 / MinebeaMitsumi Miniature Ball Bearing

> 微型滚珠轴承：请访问 [官方资料](https://www.minebeamitsumi.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 内径 | 1–50 mm（系列范围） | 产品手册 |
| 外径 | 3–80 mm | 产品手册 |
| 精度等级 | ABEC-1 至 ABEC-7 | 产品手册 |
| 材质 | 轴承钢 / 不锈钢可选 | 产品手册 |
| 润滑方式 | 油脂 / 油润滑 | 产品手册 |
| 额定载荷 | 依型号 | 产品手册 |
| 密封形式 | 开式 / 防尘盖 / 橡胶密封 | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：全球市占率领先的微型轴承，尺寸精度高、摩擦低，是机器人关节与电机的关键配套件。

**应用场景**：电机转子支撑、机器人关节减速器、精密轴系、无人机旋翼。

## 供应链位置

- **上游关键零部件/材料**：特种钢材、润滑油脂、磁材、铜线、树脂材料
- **下游客户/应用场景**：电机厂商、机器人整机厂、汽车电子、消费电子、航空航天
- **主要竞争对手/对标**：NSK、NTN、Nidec、Faulhaber、环驰轴承

## 知识图谱节点与关系

- 公司实体：`ent_company_minebea`
- 产品/零部件实体：`ent_component_minebea_micro_bldc`, `ent_component_minebea_ball_bearing`
- 关键关系：
  - `ent_company_minebea` -- `manufactures` --> `ent_component_minebea_micro_bldc`
  - `ent_company_minebea` -- `manufactures` --> `ent_component_minebea_ball_bearing`

## 参考资料

1. [官网](https://www.minebeamitsumi.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.minebeamitsumi.com/products/)（请按实际产品型号核对）