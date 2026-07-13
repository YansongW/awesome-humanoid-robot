---
id: ent_product_robotiq_hand
schema_version: 1
type: product
'title:': 2F-85 自适应二指夹爪
domain: 02_components
theoretical_depth: system
names:
  zh: 2F-85 自适应二指夹爪
  en: Robotiq 2F-85 Adaptive Gripper
status: active
sources:
- id: src_robotiq_hand_official
  type: website
  url: https://robotiq.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 2F-85 自适应二指夹爪 / Robotiq 2F-85 Adaptive Gripper

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [Robotiq / Robotiq](../../../appendices/appendix-d/companies/company_robotiq.md) |
| **产品类别** | 电动夹爪 / 末端执行器 |
| **发布时间** | 现役主力型号 |
| **状态** | 量产/商用 |
| **官网/来源** | [Robotiq官网](https://robotiq.com) |

## 产品概述

Robotiq 2F-85 是一款专为协作机器人设计的自适应二指电动夹爪，支持平行、包络与内撑三种抓取模式，具备力/位置闭环控制、掉落检测与 UR+ 即插即用能力，是全球协作机器人领域应用最广泛的夹爪之一。

## 产品图片

> 2F-85 自适应二指夹爪：请访问 [官方资料](https://robotiq.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 未公开（需参阅尺寸图） | - |
| 重量 | 0.9 kg | 产品手册 |
| 自由度 | 1（二指平动） | 产品手册 |
| 行程 | 0–85 mm | 产品手册 |
| 夹持力 | 20–235 N | 产品手册 |
| 建议负载 | 5 kg | 产品手册 |
| 闭合速度 | 20–150 mm/s | 产品手册 |
| 位置分辨率 | 0.4 mm | 产品手册 |
| 通信接口 | Modbus RTU (RS-485/RS-232) | 产品手册 |
| 防护等级 | IP40 | 产品手册 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[Robotiq / Robotiq](../../../appendices/appendix-d/companies/company_robotiq.md)
- **核心零部件/技术来源**：伺服电机、丝杠/齿轮、力传感器、铝合金、密封件。
- **下游应用/客户**：协作机器人集成商、汽车、3C、食品、物流。

## 知识图谱节点与关系

- 零部件实体：`ent_product_robotiq_hand`
- 制造商实体：`ent_company_robotiq`
- 关键关系：
  - `rel_ent_company_robotiq_manufactures_ent_product_robotiq_hand`（`ent_company_robotiq` --> `manufactures` --> `ent_product_robotiq_hand`）

## 应用场景

- **装配**：插件、压装、精密零件装配
- **搬运**：机床上下料、包装分拣
- **检测**：视觉引导质检、漏装检测
- **协作机器人**：与 UR 等协作臂即插即用

## 竞争对比

| 对比项 | 本产品 | 国际品牌 | 国内对标 |
|--------|--------|----------|----------|
| 核心优势 | 即插即用、自适应抓取、力位闭环、生态成熟 | 高端精度与可靠性 | 同区间性能竞争 |
| 交付周期 | 较短/按配置 | 较长 | 较短 |
| 服务响应 | 快速 | 中等 | 快速 |
| 价格水平 | 中高端 | 高端 | 中低端 |

## 选购与部署建议

- 选型时应根据负载、行程、速度与精度要求匹配合适型号，必要时联系厂商获取定制方案。
- 部署前建议进行负载惯量辨识、刚性匹配与振动抑制调试，确保与整机系统兼容。

## 参考资料

1. [Robotiq官网](https://robotiq.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://robotiq.com)（请按实际产品型号核对）