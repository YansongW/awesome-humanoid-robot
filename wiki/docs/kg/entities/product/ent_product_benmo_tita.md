---
id: ent_product_benmo_tita
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 本末 TITA
  en: 本末 TITA
status: active
sources:
- id: src_benmo_tita_official
  type: website
  url: https://directdrive.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 本末 TITA / 本末 TITA

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [本末科技 / Benmo Technology / Direct Drive Technology](../../../appendices/appendix-d/companies/company_benmo.md) |
| **产品类别** | 轮足机器人 |
| **发布时间** | 2023 年 |
| **状态** | 量产/开发平台 |
| **官网/来源** | [https://directdrive.com](https://directdrive.com) |

## 产品概述

智慧园区巡检、物流配送、地形测绘、农业、家用陪伴、移动拍摄。

本末 TITA 是 本末科技 的代表产品。准直驱 8 轴轮足、站立/跳跃/越障/自动恢复、顶部通用导轨模块化扩展、红外激光+超声+双目相机感知。主要规格包括：站立 510×590×490 mm；蹲下 510×590×300 mm（尺寸）、24.1 kg（不含电池）（重量）、8 DOF（自由度）。

## 产品图片

> 本末 TITA：请访问 [官方资料](https://directdrive.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 站立 510×590×490 mm；蹲下 510×590×300 mm | 本末公司介绍 PDF |
| 重量 | 24.1 kg（不含电池） | 本末公司介绍 PDF |
| 自由度 | 8 DOF | 本末公司介绍 PDF |
| 负载/扭矩 | 移动负载 10 kg | 本末公司介绍 PDF |
| 速度/转速 | 最快速度 3 m/s（5 m/s 需 API 解锁） | 本末公司介绍 PDF |
| 续航 | 双电池约 2 小时，支持热插拔 | 本末公司介绍 PDF |
| 接口/通信 | NVIDIA Jetson Orin NX 16G、RPC/机载编程、行为级与关节级接口 | 本末公司介绍 PDF |
| 价格 | 未公开 | 需询价 |

## 供应链位置

- **制造商**：[本末科技 / Benmo Technology / Direct Drive Technology](../../../appendices/appendix-d/companies/company_benmo.md)
- **核心零部件/技术来源**：自研直驱电机、M15/M07 系列关节模组、轮毂电机、控制器、电池与导航塔（激光雷达）。
- **下游应用/客户**：智慧园区巡检、物流配送、地形测绘、农业、家用陪伴、移动拍摄。

## 知识图谱节点与关系

- 产品实体：`ent_product_benmo_tita`
- 制造商实体：`ent_company_benmo`
- 关键关系：
  - `rel_ent_company_benmo_manufactures_ent_product_benmo_tita`（`ent_company_benmo` → `manufactures` → `ent_product_benmo_tita`）
  - `ent_product_benmo_tita` -- `uses` --> `ent_component_benmo_m1502d`

## 应用场景

- **智慧园区巡检、物流配送、地形测绘、农业、家用陪伴、移动拍摄。**
- **科研教育**：作为机器人控制、AI 训练与具身智能研究的硬件平台。

## 竞争对比

| 对比项 | 本产品 | 主要竞品 |
|--------|--------|----------|
| 定位 | 轮足机器人 | 同类产品视具体场景而定 |
| 核心优势 | 准直驱 8 轴轮足、站立/跳跃/越障/自动恢复、顶部通用导轨模块化扩展、红外激光+超声+双目相机感知 | 未公开 |
| 价格 | 未公开 | 未公开 |

## 选购与部署建议

- 建议通过官方渠道确认最新软件版本、SDK 支持与售后培训。
- 科研与教育用户应优先评估二次开发接口、仿真平台兼容性与社区活跃度。
- 工业用户需结合具体工序验证负载、精度、防护等级与集成接口。

## 参考资料

1. [本末科技官网](https://directdrive.com)
2. [本末科技公司介绍 PDF](https://www.worldrobotconference.com/profile/robot/download/2025/07/10/250110%20%E6%9C%AC%E6%9C%AB%E7%A7%91%E6%8A%80%E4%BB%8B%E7%BB%8D_20250710110734A073.pdf)
3. [硬氪 – 本末科技融资报道](http://mp.weixin.qq.com/s?__biz=MzkwMTI4MjU0Mw==&mid=2247520049&idx=2&sn=36133880658fdda8d838fcf5d975fbb0)