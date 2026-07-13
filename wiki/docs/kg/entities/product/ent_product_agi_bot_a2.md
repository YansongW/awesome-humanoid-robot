---
id: ent_product_agi_bot_a2
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 智元 远征 A2
  en: AgiBot Expedition A2
status: active
sources:
- id: src_agi_bot_official
  type: website
  url: https://www.zhiyuan-robot.com/products/A2_D
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 智元 远征 A2 / AgiBot Expedition A2

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [智元机器人 / AgiBot](../../../appendices/appendix-d/companies/company_agi_bot.md) |
| **产品类别** | 通用人形机器人 |
| **发布时间** | 2024 年 8 月 |
| **状态** | 量产/商用 |
| **官网/来源** | [智元机器人官网](https://www.zhiyuan-robot.com) |

## 产品概述

智元远征 A2 是智元机器人面向交互服务、汽车制造与 3C 电子场景推出的全尺寸人形机器人。A2 采用人因工程学设计，支持 40+ 全身自由度，配备 360° 激光雷达、6 颗高清摄像头与 PowerFlow 准直驱关节模组，单腿峰值扭矩超过 350 N·m。

远征 A2 强调“大脑-小脑-肢体”三级具身智能架构，自研 EI-Brain 框架与 SkillHand 灵巧手（12 主动 + 5 被动 DOF）支持精密装配与物料搬运。2025 年，A2 成为全球首个同时通过中国 CR、欧盟 CE-MD/CE-RED 与美国 FCC 认证的人形机器人，并完成了高温环境下长时间自主行走挑战。

## 产品图片

> AgiBot 远征 A2：请访问 [官方资料](https://www.zhiyuan-robot.com/products/A2_D) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 169–175 cm（高） | 旗舰版/官网参数差异 |
| 重量 | 约 55–69 kg | 旗舰版/青春版配置差异 |
| 自由度（整机） | 40+ DOF；官网标注 49+ | 公开规格 |
| 关键性能指标 | 单臂最大负载 5 kg；关节峰值扭矩 350 N·m | 官网参数 |
| 行走速度 | 约 7 km/h（约 1.94 m/s） | 官网参数 |
| 续航 | 约 2 小时（700 Wh 电池） | 公开规格 |
| AI 算力 | 200 TOPS | 官网参数 |
| 价格 | 未公开（国内已上架京东/智元商城） | 官方渠道 |

## 供应链位置

- **制造商**：[智元机器人 / AgiBot](../../../appendices/appendix-d/companies/company_agi_bot.md)
- **核心零部件/技术来源**：自研 PowerFlow 关节模组、SkillHand 灵巧手、具身智脑 EI-Brain、NVIDIA Jetson AGX Orin（部分配置）、激光雷达与视觉传感器。
- **下游应用/客户**：汽车主机厂、3C 电子、商超导览、展厅讲解、科研教育。

## 知识图谱节点与关系

- 产品实体：`ent_product_agi_bot_a2`
- 制造商实体：`ent_company_agi_bot`
- 关键关系：
  - `rel_ent_company_agi_bot_manufactures_ent_product_agi_bot_a2`（`ent_company_agi_bot` → `manufactures` → `ent_product_agi_bot_a2`）

## 应用场景

- **汽车制造**：汽车产线外观质检、内饰装配校验、安全带安装检测与螺丝拧紧。
- **3C 电子**：半导体上下料、精密组装与新能源电池 PACK 线辅助作业。
- **交互服务**：展厅讲解、商超导览、营销客服与车展销售顾问。

## 竞争对比

| 对比项 | 智元远征 A2 | 优必选 Walker S2 | Tesla Optimus Gen 3 |
|--------|-------------|------------------|---------------------|
| 定位 | 通用/服务人形 | 工业人形 | 通用/工业人形 |
| 整机 DOF | 40+（官网 49+） | 52 | 28+ 躯干 + 22×2 手 |
| 认证 | CR / CE-MD / CE-RED / FCC | 未公开 | 未公开 |
| 核心优势 | 全栈自研、多国认证、交互能力 | 工厂部署、热插拔电池 | 制造规模目标、FSD 视觉 |

## 选购与部署建议

- 建议通过智元官方商城或京东旗舰店了解现货配置、交付周期与售后政策。
- 工业场景部署前应完成 CR/CE 认证文件核对、现场安全评估及操作人员培训。

## 参考资料

1. [智元机器人官网](https://www.zhiyuan-robot.com)
2. [智元远征 A2 产品页](https://www.agibot.com/product/169/detail/4.html)
3. [IT之家 – 智元远征 A2 跨省行走](https://www.ithome.com/0/898/193.htm)
4. [与非网 – 智元远征 A2 运动控制](https://www.eefocus.com/article/1952915.html)