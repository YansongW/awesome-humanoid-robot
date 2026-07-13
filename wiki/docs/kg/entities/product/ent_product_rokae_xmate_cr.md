---
id: ent_product_rokae_xmate_cr
schema_version: 1
type: product
'title:': 珞石 xMate CR 系列协作机器人
domain: 04_assembly_integration_testing
theoretical_depth: system
names:
  zh: 珞石 xMate CR 系列协作机器人
  en: ROKAE xMate CR Series Collaborative Robot
status: active
sources:
- id: src_rokae_xmate_cr_official
  type: website
  url: https://www.rokae.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 珞石 xMate CR 系列协作机器人 / ROKAE xMate CR Series Collaborative Robot

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [珞石机器人 / ROKAE](../../../appendices/appendix-d/companies/company_rokae.md) |
| **产品类别** | 工业级协作机器人 |
| **发布时间** | 2019 年起持续迭代 |
| **状态** | 量产/商用 |
| **官网/来源** | [https://www.rokae.com](https://www.rokae.com) |

## 产品概述

xMate CR 系列是珞石机器人推出的工业级协作机器人，以自研 xCore 控制系统、高轨迹精度和力控能力见长。

产品覆盖 3–12 kg 负载与 6/7 自由度，强调高速、高精、高刚性，适合复杂工艺与人机协作柔性产线。

## 产品图片

> xMate CR：请访问 [官方资料](https://www.rokae.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品形态 | 6/7-DOF 工业级协作机器人 | 珞石官网 |
| 自重 | 未公开 | - |
| 负载 | 3–12 kg（视型号） | 产品手册 |
| 臂展 | 717–1304 mm（视型号） | 产品手册 |
| 自由度 | 6/7 DOF（视型号） | 公开规格 |
| 重复定位精度 | ±0.02–±0.03 mm | 产品手册 |
| 最大末端速度 | 未公开 | - |
| 最大关节速度 | 未公开 | - |
| 防护等级 | IP54 | 产品手册 |
| 通信接口 | Ethernet / EtherCAT / ROS | 产品手册 |
| 价格 | 未公开 | 需询价 |

## 供应链位置

- **制造商**：[珞石机器人 / ROKAE](../../../appendices/appendix-d/companies/company_rokae.md)
- **核心零部件/技术来源**：自研 xCore 控制系统、谐波减速器、伺服电机、控制器、编码器、结构件。
- **下游应用/客户**：汽车、3C、新能源、金属加工、医疗、人形机器人整机厂。

## 知识图谱节点与关系

- 产品实体：`ent_product_rokae_xmate_cr`
- 制造商实体：`ent_company_rokae`
- 关键关系：
  - `rel_ent_company_rokae_manufactures_ent_product_rokae_xmate_cr`（`ent_company_rokae` → `manufactures` → `ent_product_rokae_xmate_cr`）

## 应用场景

- **3C 精密装配**：高精度插件、贴合、检测。
- **汽车零部件打磨**：力控抛光、去毛刺。
- **医疗器械上下料**：无菌环境下的柔性取放。
- **科研教育**：运动规划、力控交互、人机协作研究。

## 竞争对比

| 对比项 | xMate CR | 主要竞品 |
|--------|----------|----------|
| 定位 | 工业级高精度协作机器人 | 埃斯顿、节卡、遨博、KUKA iiwa |
| 核心优势 | 自研 xCore、高轨迹精度、力控 | 视具体型号而定 |
| 价格 | 未公开 | 未公开 |

## 选购与部署建议

- 根据负载、臂展与自由度需求选择具体型号。
- 力控打磨场景需确认力传感器与控制算法的配套方案。
- 建议通过珞石官方渠道获取最新控制软件与工艺包。

## 相关词条

- [制造商：珞石机器人 / ROKAE](../../../appendices/appendix-d/companies/company_rokae.md)
- [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)

## 参考资料

1. [珞石机器人官网](https://www.rokae.com)
2. 珞石 xMate CR 系列产品手册
3. [WAIC 2026 参展报道](https://www.worldrobotconference.com)