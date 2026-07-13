---
id: ent_product_schunk_svh
schema_version: 1
type: product
'title:': SCHUNK SVH 五指灵巧手
domain: 02_components
theoretical_depth: system
names:
  zh: SCHUNK SVH 五指灵巧手
  en: SCHUNK SVH 5-Finger Hand
status: active
sources:
- id: src_schunk_svh_official
  type: website
  url: https://www.schunk.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# SCHUNK SVH 五指灵巧手 / SCHUNK SVH 5-Finger Hand

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [SCHUNK GmbH / SCHUNK GmbH](../../../appendices/appendix-d/companies/company_schunk.md) |
| **产品类别** | 灵巧手 / 末端执行器 |
| **发布时间** | 现役型号 |
| **状态** | 量产/商用 |
| **官网/来源** | [SCHUNK GmbH官网](https://www.schunk.com) |

## 产品概述

SCHUNK SVH 是 SCHUNK 推出的五指协作灵巧手，也是全球首款通过 DGUV 认证、可用于协作操作的五指机械手。其齿轮/连杆传动与防滑橡胶抓握面设计，兼顾安全性与抓取稳定性，适用于服务机器人与协作机器人。

## 产品图片

> SCHUNK SVH 五指灵巧手：请访问 [官方资料](https://www.schunk.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 总长 242 mm | 公开资料 |
| 重量 | 1.3 kg | 公开资料 |
| 手指数 | 5 | 公开资料 |
| 自由度 | 9（五指各 1 + 手腕 4） | 公开资料 |
| 关节数 | 20 | 公开资料 |
| 电机数 | 9 | 公开资料 |
| 供电电压 | DC 24 V | 公开资料 |
| 通信接口 | RS485 | 公开资料 |
| 建议负载 | 约 2.5 kg | 公开资料 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[SCHUNK GmbH / SCHUNK GmbH](../../../appendices/appendix-d/companies/company_schunk.md)
- **核心零部件/技术来源**：电机、减速器、传感器、铝合金/钢构件、密封件。
- **下游应用/客户**：汽车制造、电子装配、协作机器人、物流、医疗。

## 知识图谱节点与关系

- 零部件实体：`ent_product_schunk_svh`
- 制造商实体：`ent_company_schunk`
- 关键关系：
  - `rel_ent_company_schunk_manufactures_ent_product_schunk_svh`（`ent_company_schunk` --> `manufactures` --> `ent_product_schunk_svh`）

## 应用场景

- **服务机器人**：迎宾、递送、人机交互
- **协作机器人**：柔性装配、协作上下料
- **医疗康复**：辅助抓取、康复训练
- **科研**：多指抓取与协作安全研究

## 竞争对比

| 对比项 | 本产品 | 国际品牌 | 国内对标 |
|--------|--------|----------|----------|
| 核心优势 | DGUV 认证、协作安全、工业级可靠性 | 高端精度与可靠性 | 同区间性能竞争 |
| 交付周期 | 较短/按配置 | 较长 | 较短 |
| 服务响应 | 快速 | 中等 | 快速 |
| 价格水平 | 高端 | 高端 | 中低端 |

## 选购与部署建议

- 选型时应根据负载、行程、速度与精度要求匹配合适型号，必要时联系厂商获取定制方案。
- 部署前建议进行负载惯量辨识、刚性匹配与振动抑制调试，确保与整机系统兼容。

## 参考资料

1. [SCHUNK GmbH官网](https://www.schunk.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.schunk.com)（请按实际产品型号核对）