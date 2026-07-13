---
id: ent_company_optitrack
type: company
'title:': OptiTrack（自然点） / OptiTrack（NaturalPoint, Inc.）
domain: 02_components
theoretical_depth: system
aliases:
- OptiTrack（NaturalPoint, Inc.）
- OptiTrack（自然点）
status: active
created_at: 2024-01-15 00:00:00+00:00
updated_at: 2026-07-01 00:00:00+00:00
sources:
- id: ent_company_optitrack_official
  type: website
  url: https://optitrack.com
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-01 00:00:00+00:00
  review_notes: Data sourced from official website and public reports; missing specs
    marked as 未公开.
---





# optitrack

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | OptiTrack（自然点） |
| **英文名** | OptiTrack（NaturalPoint, Inc.） |
| **总部** | 美国俄勒冈州科瓦利斯 |
| **成立时间** | 1996 |
| **官网** | [https://optitrack.com](https://optitrack.com) |
| **供应链环节** | 光学动作捕捉、追踪相机、运动测量 |
| **企业属性** | 私有公司（NaturalPoint 旗下） |
| **母公司/所属集团** | NaturalPoint, Inc. |
| **数据来源** | OptiTrack 官网、产品页、公开报道 |

## 公司简介

OptiTrack 是全球领先的光学动作捕捉系统供应商，其产品以高精度、低延迟、大捕捉范围著称，广泛应用于影视动画、游戏、生物力学、体育科学、无人机/机器人定位及人形机器人运动验证。OptiTrack 的相机阵列与 Motive 软件配合，可实现亚毫米级 6DoF 位姿追踪。

OptiTrack 提供 PrimeX 系列高分辨率红外相机、Motive 跟踪软件及主动/被动标记点方案，是机器人研发中用于步态分析、全身运动捕捉、遥操作验证与算法标定的常用工具。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| PrimeX 相机系列 | 高性能红外动作捕捉相机 | [OptiTrack 运动捕捉系统](../../../appendices/appendix-d/products/product_optitrack_motive_system.md) | 影视、体育、机器人 |
| Motive 软件 | 数据采集与实时解算 | Motive 3 | 动作捕捉、分析 |
| 追踪配件 | 标记点、校准工具、同步设备 | Active/Passive Marker Sets | 研发、集成 |

## 代表产品

### OptiTrack 运动捕捉系统

> OptiTrack 运动捕捉系统：请访问 [官方资料](https://optitrack.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 系统类型 | 光学红外动作捕捉系统 | OptiTrack 官网 |
| 代表相机 | PrimeX 13 / PrimeX 41 等 | 产品页 |
| 追踪精度 | 亚毫米级（未公开精确值） | 公开资料 |
| 延迟 | 低至数毫秒级 | 产品页 |
| 分辨率 | 最高约 2048×2048（PrimeX 41） | 产品页 |
| 帧率 | 最高 240 fps 以上（依型号） | 产品页 |
| 软件 | Motive 3（实时解算、数据导出） | 官网 |
| 同步接口 | eSync / Ethernet | 产品页 |
| 价格 | 未公开 | 商务报价 |

**技术亮点**：高分辨率红外成像、亚毫米精度、低延迟实时解算、大规模多相机同步、丰富的 SDK 与数据接口。

**应用场景**：人形机器人步态与动作标定、遥操作训练、无人机/AGV 定位验证、影视动画、体育生物力学、康复医学。

## 供应链位置

- **上游关键零部件/材料**：红外图像传感器、光学镜头、FPGA/处理芯片、红外 LED、精密结构件、校准算法、网络同步模块
- **下游客户/应用场景**：影视制作公司、游戏开发商、机器人/无人机研发机构、高校实验室、体育/医疗机构
- **主要竞争对手/对标**：Vicon、Motion Analysis、Qualisys、Noitom（诺亦腾）、Xsens（惯性）

## 知识图谱节点与关系

- 公司实体：`ent_company_optitrack`
- 产品实体：`ent_product_optitrack_motive_system`
- 零部件实体：`ent_component_optitrack_motive_system_core`
- 关键关系：
  - `ent_company_optitrack` -- `manufactures` --> `ent_product_optitrack_motive_system`
  - `ent_company_optitrack` -- `manufactures` --> `ent_component_optitrack_motive_system_core`
  - `ent_product_optitrack_motive_system` -- `uses` --> `ent_component_optitrack_motive_system_core`

## 参考资料

1. [OptiTrack 官网](https://optitrack.com)
2. [OptiTrack 相机产品页](https://optitrack.com/cameras/)
3. [附录 D 企业目录](../../../appendices/appendix-d/index-companies.md)