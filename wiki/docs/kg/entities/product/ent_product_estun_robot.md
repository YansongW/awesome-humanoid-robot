---
id: ent_product_estun_robot
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 埃斯顿机器人
  en: 埃斯顿机器人
status: active
sources:
- id: src_ent_product_estun_robot
  type: website
  url: ''
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 埃斯顿机器人

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [埃斯顿自动化 / Estun Automation](../../../appendices/appendix-d/companies/company_estun.md) |
| **产品类别** | 工业机器人/协作机器人/人形零部件 |
| **发布时间** | 1993 年成立，机器人业务持续迭代 |
| **状态** | 量产/商用 |
| **官网/来源** | 见正文参考资料 |

## 产品概述

埃斯顿机器人覆盖六轴工业机器人、SCARA、协作机器人及人形机器人核心零部件。公司坚持自主可控，自研伺服系统、运动控制器与机器人本体，并通过海外并购提升焊接与运动控制技术，是中国工业机器人国产替代与智能化升级的核心力量。

## 产品图片

> 埃斯顿机器人：请访问 [官方资料](https://www.estun.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品形态 | 六轴机器人、SCARA、协作机器人、Delta | 埃斯顿官网 |
| 负载范围 | 3–600 kg | 产品手册 |
| 重复定位精度 | ±0.02–±0.05 mm | 产品手册 |
| 臂展 | 500–3200 mm | 产品手册 |
| 自由度 | 4–6 DOF | 公开规格 |
| 防护等级 | IP40–IP67（视型号） | 产品手册 |
| 控制器 | 自研 ESTUN 控制器 | 埃斯顿官网 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[埃斯顿自动化 / Estun Automation](../../../appendices/appendix-d/companies/company_estun.md)
- **核心零部件/技术来源**：伺服电机、减速器、控制器、铸件、线缆、传感器。
- **下游应用/客户**：汽车、3C、锂电、光伏、金属加工、物流、人形机器人整机厂。

## 知识图谱节点与关系

- 产品实体：`ent_product_estun_robot`
- 制造商实体：`ent_company_estun`
- 关键关系：
  - `rel_ent_company_estun_manufactures_ent_product_estun_robot`（`ent_company_estun` → `manufactures` → `ent_product_estun_robot`）
  - `ent_product_estun_robot` -- `uses` --> `ent_component_estun_servo`
  - `ent_product_estun_robot` -- `uses` --> `ent_component_harmonic_drive`

## 应用场景

- **焊接**：收购 Cloos 后具备高端焊接机器人与工艺。
- **搬运与装配**：六轴/SCARA 用于 3C、锂电、汽车零部件产线。
- **人形零部件**：谐波减速器、无框力矩电机、关节模组供应。

## 竞争对比

| 对比项 | 埃斯顿 | 汇川技术 | 发那科/ABB |
|--------|------|------|------|
| 定位 | 国产工业机器人龙头 | 工控+机器人协同 | 外资高端 |
| 核心优势 | 全系列+并购技术 | 伺服/PLC 协同 | 品牌与精度 |
| 价格 | 国产中端 | 国产中端 | 高端 |

## 选购与部署建议

- 根据算力/精度/场景需求选择对应型号，优先考虑官方支持的工具链与生态兼容性。
- 部署前确认供电、散热、机械接口与通信协议是否满足整机要求。
- 建议通过官方渠道或授权代理商获取最新固件、SDK 与技术支持。

## 相关词条

- [制造商：埃斯顿自动化 / Estun Automation](../../../appendices/appendix-d/companies/company_estun.md)
- [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)

## 参考资料

1. [埃斯顿自动化 / Estun Automation 官方产品/公司页面](https://www.estun.com)
2. 埃斯顿官网产品页
3. 埃斯顿 2024 年度报告