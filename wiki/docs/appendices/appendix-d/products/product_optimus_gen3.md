# Tesla Optimus Gen 3 / 特斯拉 Optimus Gen 3

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [特斯拉 / Tesla](../companies/company_tesla.md) |
| **产品类别** | 通用人形机器人 |
| **发布时间** | Gen 3 手部于 2024 年底公开；2026 年推进整机体量产 |
| **状态** | 内部量产/工厂部署 |
| **官网/来源** | [Tesla 官网](https://www.tesla.com) |

## 产品概述

Tesla Optimus Gen 3 是特斯拉人形机器人平台的最新迭代，重点升级了手部自由度与整机电驱集成度。Gen 3 在 Gen 2 的 173 cm 躯干基础上，将单手自由度从 11 DOF 提升至 22 DOF，单只手搭载 25 个执行器，双手共 50 个执行器，显著增强了精细抓取与工具操作能力。

Optimus Gen 3 依托特斯拉自研的 FSD 视觉神经网络、车载级电池包与执行器技术，目标场景覆盖特斯拉工厂内部的电池分拣、物料搬运，并长期面向消费级市场。马斯克在公开表态中提出目标零售价 20,000–30,000 美元，但截至 2026 年该价格仍属于目标规划，未正式对外销售。

## 产品图片

> Tesla Optimus Gen 3：请访问 [官方资料](https://www.tesla.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 173 cm（高） | Tesla AI Day 公开资料 |
| 重量 | 约 57 kg（Gen 2 躯干基准） | 公开资料；Gen 3 完整体重未公开 |
| 自由度（整机） | 躯干 28+；手部 22×2 | Gen 3 手部升级 |
| 关键性能指标 | 双手搬运约 20 kg；手部 50 执行器 | 公开演示/媒体汇编 |
| 行走速度 | 约 8 km/h（目标） | 第三方评测 |
| 续航 | 约 2–4 小时（视任务） | 未官方确认 |
| 功耗 | 未公开 | - |
| 价格 | 目标零售价 20,000–30,000 USD | Musk 公开表态 |

## 供应链位置

- **制造商**：[特斯拉 / Tesla](../companies/company_tesla.md)
- **核心零部件/技术来源**：自研线性/旋转执行器、FSD 视觉感知、电池包与电源管理、车载级计算平台；部分结构件外协。
- **下游应用/客户**：特斯拉自有工厂（电池分拣、物料搬运），未来面向企业级与消费级市场。

## 知识图谱节点与关系

- 产品实体：`ent_product_tesla_optimus_gen3`
- 制造商实体：`ent_company_tesla`
- 关键关系：
  - `rel_ent_company_tesla_manufactures_ent_product_tesla_optimus_gen3`（`ent_company_tesla` → `manufactures` → `ent_product_tesla_optimus_gen3`）

## 应用场景

- **汽车制造**：在特斯拉工厂执行电池单元分拣、物料搬运、箱体码垛与产线巡检。
- **通用工业**：替代重复性、高强度或存在安全隐患的人工作业，如搬运、装配辅助。
- **未来消费/服务**：家庭清洁、个人助理与照护服务（仍处于长期规划阶段）。

## 竞争对比

| 对比项 | Tesla Optimus Gen 3 | Figure 02 | Boston Dynamics Atlas |
|--------|---------------------|-----------|-----------------------|
| 定位 | 通用/工业人形 | 工业制造人形 | 重载工业人形 |
| 手部 DOF | 22×2 | 16（双手） | 未公开 |
| 价格方向 | 目标 20,000–30,000 USD | 未公开 | 未公开（预估高端） |
| 核心优势 | 规模化制造目标、FSD 视觉、自研执行器 | Helix VLA 模型、宝马部署 | 56 DOF、50 kg 负载、运动能力 |

## 选购与部署建议

- 目前 Optimus Gen 3 仅面向特斯拉内部及特定企业试点，消费级销售尚未开放。
- 企业客户若关注人形机器人替代方案，建议同步评估 Figure 02、Digit 等已部署平台。

## 参考资料

1. [Tesla 官网](https://www.tesla.com)
2. [Tesla AI Day 公开演示](https://www.tesla.com/AI)
3. [Robozaps – Tesla Optimus Gen 3 Specs](https://blog.robozaps.com/b/tesla-optimus-gen-3)
4. [Optimusk – Tesla Optimus Capabilities 2025-2026](https://optimusk.blog/blog/tesla-optimus-capabilities/)