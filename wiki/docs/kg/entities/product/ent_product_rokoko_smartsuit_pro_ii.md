---
id: ent_product_rokoko_smartsuit_pro_ii
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: Rokoko Smartsuit Pro II
  en: Rokoko Smartsuit Pro II
status: active
sources:
- id: src_ent_product_rokoko_smartsuit_pro_ii
  type: website
  url: ''
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# Rokoko Smartsuit Pro II

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [Rokoko](../../../appendices/appendix-d/companies/company_rokoko.md) |
| **产品类别** | 惯性动作捕捉套装 |
| **发布时间** | 2021 年 10 月发布 |
| **状态** | 商用 |
| **官网/来源** | [Rokoko 官网](https://rokoko.com) |

## 产品概述

Rokoko Smartsuit Pro II 是 Rokoko 推出的第二代全身惯性动作捕捉套装，面向独立创作者、游戏工作室、影视制作、体育科学与机器人研究领域。套装通过 Wi-Fi 与免费 Rokoko Studio 软件连接，可实时录制、清理、编辑并将动作数据流式传输到 Unreal Engine、Unity、Blender、Maya、MotionBuilder 等主流 3D 工具。

相较于第一代，Smartsuit Pro II 在漂移抑制、高冲击运动稳定性、多层追踪（楼梯/梯子/垂直移动）以及与 Smartgloves 手部追踪的集成方面有显著提升。其 17–19 颗 9-DOF IMU 传感器、200 fps 流传输和约 6 小时续航，使其成为高性价比专业动捕方案的代表。

在机器人领域，Smartsuit Pro II 可用于采集人类自然运动数据，为人形机器人、数字人和具身智能模型提供动作参考与训练数据。

## 产品图片

> Rokoko Smartsuit Pro II：请访问 [官方资料](https://rokoko.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 传感器数量 | 17× 或 19× 9-DOF IMU | Rokoko 官网 |
| 3D 方向精度 | ±1° | Rokoko 公开规格 |
| 采样/流传输 | 200 fps | Rokoko 公开规格 |
| 加速度计量程 | 16 g | Rokoko 公开规格 |
| 无线连接 | Wi-Fi（最大约 100 m） | Rokoko 公开规格 |
| 续航 | 约 6 小时 | Rokoko 公开规格 |
| 套装尺寸 | S / M / L / XL | Rokoko 官网 |
| 面料 | 可水洗尼龙/弹性面料 | Rokoko 公开规格 |
| 价格 | 约 2,745 USD 起 | 公开报价 |

## 供应链位置

- **制造商**：[Rokoko](../../../appendices/appendix-d/companies/company_rokoko.md)
- **核心零部件/技术来源**：MEMS IMU 传感器、Wi-Fi 模块、可穿戴纺织品、锂电池、传感器融合算法芯片、Rokoko Studio 软件。
- **下游应用/客户**：独立动画师、游戏工作室（Ubisoft、EA 等）、影视 VFX、体育科研机构、机器人/人形机器人公司。

## 知识图谱节点与关系

- 产品实体：`ent_product_rokoko_smartsuit_pro_ii`
- 制造商实体：`ent_company_rokoko`
- 关键关系：
  - `rel_ent_company_rokoko_manufactures_ent_product_rokoko_smartsuit_pro_ii`（`ent_company_rokoko` → `manufactures` → `ent_product_rokoko_smartsuit_pro_ii`）

## 应用场景

- **影视与游戏动画**：实时驱动角色，快速生成高质量动画。
- **虚拟直播 / VTubing**：低延迟驱动虚拟形象。
- **体育生物力学**：分析运动员动作、姿态与发力模式。
- **机器人动作参考**：为人形机器人采集自然运动数据，用于模仿学习与运动规划。

## 竞争对比

| 对比项 | Rokoko Smartsuit Pro II | Xsens MVN Link | Noitom Perception Neuron |
|--------|------------------------|----------------|--------------------------|
| 定位 | 高性价比专业惯性动捕 | 高端专业惯性动捕 | 入门级惯性动捕 |
| 传感器 | 17–19× 9-DOF IMU | 17× 有线 IMU | 较少 IMU |
| 更新率 | 200 fps | 最高 240 Hz | 较低 |
| 价格 | 约 2,745 USD 起 | 企业询价 | 约 1,500 USD 起 |
| 软件生态 | Rokoko Studio（免费基础版） | MVN Analyze/Animate | 自有软件 |

## 选购与部署建议

- 适合预算有限但需要专业级全身动捕的团队，尤其是独立创作者与中小型工作室。
- 若需高冲击运动或垂直移动捕捉，建议确认固件为支持多层追踪的最新版本。
- 用于机器人数据采集时，需额外标定骨架比例，并导出为 BVH/FBX/CSV 等通用格式。

## 参考资料

1. [Rokoko 官网](https://rokoko.com)
2. [CGW – Rokoko Smartsuit Pro II 发布](https://www.cgw.com/Press-Center/News/2021/Rokoko-Launches-the-Next-Gen-Smartsuit-Pro-II.aspx)
3. [Animation Xpress – Rokoko Smartsuit Pro II](https://www.animationxpress.com/latest-news/motion-capture-company-rokoko-launches-smartsuit-pro-ii/)
4. [Rokoko Studio 下载页](https://rokoko.com/studio)