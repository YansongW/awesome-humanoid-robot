---
id: ent_product_deep_robotics_x30
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 云深处 绝影 X30
  en: DEEPRobotics Jueying X30
status: active
sources:
- id: src_deep_robotics_official
  type: website
  url: https://www.deeprobotics.cn
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 云深处 绝影 X30 / DEEPRobotics Jueying X30

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [云深处科技 / DEEP Robotics](../../../appendices/appendix-d/companies/company_deep_robotics.md) |
| **产品类别** | 行业级四足机器人 |
| **发布时间** | 2023 年 10 月 |
| **状态** | 量产/商用 |
| **官网/来源** | [云深处 X30 产品页](https://deeprobotics.cn/robot/index/x30.html) |

## 产品概述

绝影 X30 是云深处科技面向行业应用推出的旗舰级四足机器人，聚焦电力巡检、应急救援、消防侦察、管廊隧道与工业测绘等场景。X30 具备 IP67 工业级防护，可在 -20°C 至 55°C 温度范围内作业，并支持昏暗、强光、闪烁甚至无光环境下的融合感知自主导航。

X30 整机重量 56 kg，最大速度不低于 4 m/s，可跨越 20 cm 障碍物、攀爬 45° 楼梯与斜坡。其电池支持现场快速拆换，负载续航相比前代提升 25%，续航里程不低于 10 km。凭借高防护、强越障与长续航，X30 已在国内外电力、冶金、矿山与应急救援项目中落地。

## 产品图片

> DEEP Robotics Jueying X30：请访问 [官方资料](https://www.deeprobotics.cn) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 站立尺寸 1000×695×470 mm | 官方规格 |
| 重量 | 56 kg | 官方规格 |
| 自由度（整机） | 12 DOF（每条腿 3 DOF） | 四足结构 |
| 关键性能指标 | 最大速度 ≥4 m/s；爬坡 ≤45°；越障 ≥20 cm | 官方规格 |
| 负载能力 | 有效负载 ≥20 kg；极限负载可达 50 kg | 公开资料 |
| 续航 | 2.5–4 h；续航里程 ≥10 km | 官方规格 |
| 防护等级 | IP67 | 官方规格 |
| 工作温度 | -20°C 至 55°C | 官方规格 |
| 价格 | 未公开（行业级定制方案） | - |

## 供应链位置

- **制造商**：[云深处科技 / DEEP Robotics](../../../appendices/appendix-d/companies/company_deep_robotics.md)
- **核心零部件/技术来源**：自研高扭矩关节（J80/J100）、融合感知系统、运动控制算法；激光雷达、深度相机、电池外购。
- **下游应用/客户**：国家电网、南方电网、宝钢、福禄克、应急救援与消防单位。

## 知识图谱节点与关系

- 产品实体：`ent_product_deep_robotics_x30`
- 制造商实体：`ent_company_deep_robotics`
- 关键关系：
  - `rel_ent_company_deep_robotics_manufactures_ent_product_deep_robotics_x30`（`ent_company_deep_robotics` → `manufactures` → `ent_product_deep_robotics_x30`）

## 应用场景

- **电力巡检**：变电站、输电走廊与配电房的设备状态、红外测温与表计识别。
- **应急救援**：地震、燃爆与消防现场的侦察、搜救与环境监测。
- **工业巡检**：钢厂、化工厂、管廊与隧道的全天候自主巡逻与异常报警。

## 竞争对比

| 对比项 | 云深处 绝影 X30 | Unitree B2 | Boston Dynamics Spot |
|--------|-----------------|------------|----------------------|
| 定位 | 行业级四足机器人 | 行业级四足机器人 | 商用四足机器人 |
| 防护等级 | IP67 | IP66 | IP54 |
| 工作温度 | -20°C 至 55°C | 未公开 | -20°C 至 45°C |
| 核心优势 | 高防护、高负载、长续航 | 高动态运动、性价比 | 生态成熟、SDK 丰富 |

## 选购与部署建议

- 行业客户建议根据巡检/救援任务需求选配云台、气体传感器、红外热像仪等载荷。
- 部署前应完成现场地图构建、自主充电点设置以及极端环境下的电池续航验证。

## 参考资料

1. [云深处 X30 产品页](https://deeprobotics.cn/robot/index/x30.html)
2. [云深处官网](https://www.deeprobotics.cn/)
3. [AI 星踪岛 – 绝影 X30 评测](https://aixzd.com/robot/x30)
4. [NE 时代 – 云深处完成 C 轮融资](https://www.ne-time.cn/web/article/37321)