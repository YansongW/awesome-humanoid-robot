---
id: ent_product_black_sesame_a1000
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 黑芝麻智能华山 A1000
  en: Black Sesame A1000
aliases:
- 华山 A1000
- A1000
status: active
sources:
- id: src_ent_product_black_sesame_a1000_official
  type: website
  url: https://www.blacksesame.com.cn/products/1.html
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01 00:00:00+00:00
---





# 黑芝麻智能华山 A1000 / Black Sesame A1000

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [黑芝麻智能 / Black Sesame](../../../appendices/appendix-d/companies/company_black_sesame.md) |
| **产品类别** | 自动驾驶/机器人 AI 计算芯片 |
| **发布时间** | 2020 年发布华山 A1000 |
| **状态** | 量产/商用 |
| **官网/来源** | 黑芝麻智能官网、港股招股书 |

## 产品概述

黑芝麻智能华山 A1000 是面向高级别自动驾驶与智能机器人设计的高算力 AI 芯片，集成自研 ISP、神经网络处理引擎与多传感器融合能力。

华山 A1000 采用黑芝麻自研 NeuralIQ ISP 与 DynamAI NN 引擎，支持多路高清摄像头、激光雷达与毫米波雷达接入，具备 ASIL-B 至 ASIL-D 功能安全目标。单芯片算力可满足 L2+ 至 L3 级自动驾驶需求，也可扩展用于机器人的多模态感知与实时决策。

## 产品图片

> 黑芝麻智能华山 A1000：请访问 [官方资料](https://www.blacksesame.com.cn/products/1.html) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| AI 处理器 | 华山 A1000 | 黑芝麻智能官网 |
| 架构 | NeuralIQ ISP + DynamAI NN | 黑芝麻公开资料 |
| 制程 | 16 nm | 公开报道 |
| AI 算力 | INT8 约 58 TOPS | 黑芝麻公开资料 |
| CPU | ARM Cortex-A55 多核 | 公开报道 |
| ISP | 自研 NeuralIQ，支持多路高动态范围图像 | 黑芝麻公开资料 |
| 传感器接口 | 多路摄像头、激光雷达、毫米波雷达 | 黑芝麻公开资料 |
| 功能安全 | ASIL-B / ASIL-D（部分模块目标） | 黑芝麻公开资料 |
| 功耗 | 约 15–25 W | 公开报道 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[黑芝麻智能 / Black Sesame](../../../appendices/appendix-d/companies/company_black_sesame.md)
- **核心零部件/技术来源**：自研 ISP/NN 架构、晶圆代工、车规级存储、车载以太网 PHY、封测、PCB。
- **下游应用/客户**：主机厂、Tier1、自动驾驶方案商、机器人整机厂、传感器厂商。

## 知识图谱节点与关系

- 产品实体：`ent_product_black_sesame_a1000`
- 零部件实体：`ent_component_black_sesame_a1000_chip`
- 制造商实体：`ent_company_black_sesame`
- 关键关系：
  - `rel_ent_company_black_sesame_manufactures_ent_product_black_sesame_a1000`（`ent_company_black_sesame` → `manufactures` → `ent_product_black_sesame_a1000`）
  - `rel_ent_company_black_sesame_manufactures_ent_component_black_sesame_a1000_chip`（`ent_company_black_sesame` → `manufactures` → `ent_component_black_sesame_a1000_chip`）
  - `ent_product_black_sesame_a1000` -- `uses` --> `ent_component_black_sesame_a1000_chip`

## 应用场景

- **自动驾驶域控制器**：作为主芯片实现环境感知、融合定位与路径规划。
- **机器人感知大脑**：融合相机与激光雷达数据，支撑 SLAM、避障与操作。
- **多传感器融合平台**：用于无人车、无人配送、人形机器人等复杂场景。

## 竞争对比

| 对比项 | 华山 A1000 | 地平线 Journey 5 | NVIDIA Orin |
|--------|------|------|------|
| 算力 | ~58 TOPS | ~128 TOPS | ~200–254 TOPS |
| 功能安全 | ASIL-D 目标 | ASIL-B/D | ASIL-D |
| 生态 | 黑芝麻工具链 | 地平线天工开物 | NVIDIA DRIVE |

## 选购与部署建议

- 优先评估摄像头、雷达接口数量与 A1000 的匹配度，以及工具链对目标算法的支持。
- 部署前完成功能安全与热设计验证，确保满足车规/工业级可靠性要求。
- 建议通过黑芝麻官方渠道获取最新 BSP、SDK 与参考设计。

## 相关词条

- [制造商：黑芝麻智能 / Black Sesame](../../../appendices/appendix-d/companies/company_black_sesame.md)
- [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)

## 参考资料

1. [黑芝麻智能官网](https://www.blacksesame.com.cn)
2. [黑芝麻智能华山系列](https://www.blacksesame.com.cn/products/1.html)
3. 黑芝麻智能港股招股书