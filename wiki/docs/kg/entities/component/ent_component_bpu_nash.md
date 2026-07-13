---
id: ent_component_bpu_nash
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 地平线 BPU Nash 架构
  en: Horizon Robotics BPU Nash Architecture
status: active
sources:
- id: src_horizon_journey6
  type: website
  url: https://www.horizon.auto/en/solutions/horizon-journey/horizon-journey6
- id: src_horizon_journey
  type: website
  url: https://www.horizon.auto/en/solutions/horizon-journey
- id: src_baike_journey6m
  type: website
  url: https://baike.baidu.com/en/item/Journey%206M/1756692
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 地平线 BPU Nash 架构 / Horizon Robotics BPU Nash Architecture

## 概述

BPU Nash 是地平线（Horizon Robotics）推出的第四代智能驾驶加速架构，名称中的“Nash”体现了算法与硬件协同优化的设计思想。该架构搭载于征程 6（Journey 6）系列车载智能计算平台，覆盖从主动安全到城区 NOA 的全阶辅助驾驶需求，并原生支持大参数量 Transformer 模型、端到端算法及交互式博弈决策。

## 工作原理 / 技术架构

BPU Nash 采用统一的可扩展架构，在征程 6 系列各型号之间保持软件兼容，支持跨代迁移。其设计强调高带宽-算力比，以满足多路高清摄像头、激光雷达与毫米波雷达等多模态传感器融合的数据吞吐需求。硬件层面集成 BPU、CPU、GPU 与 MCU，形成“四芯合一”的 SoC 方案；软件层面通过地平线工具链实现模型量化、编译与部署优化。

有效算力通常以稀疏加速后的 TOPS 表示。征程 6 旗舰型号标称有效算力为 560 TOPS（1/2 稀疏，TPP<4800），算力利用率与模型特征强相关。

## 关键参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 架构代际 | BPU Nash（第 4 代） | Horizon |
| 搭载平台 | 征程 6 系列（6B/6E/6M/6H/6P 等） | Horizon |
| 算力范围 | 10+ – 560 TOPS（effective，1/2 sparsity） | Horizon |
| CPU DMIPS | 20K – 410K | Horizon |
| 支持摄像头 | 最高 24 路车载高清摄像头 | Horizon |
| 视频流 | 多路 4K | Horizon |
| 网络接口 | 10 Gigabit Ethernet 等高速接口 | Horizon |
| 功能安全 | AEC-Q100 Grade 2；ASIL-B(D) 计算 & ASIL-D MCU | Horizon |
| 算法支持 | Transformer、端到端、交互式博弈决策 | Horizon |

## 应用场景

- 乘用车 ADAS/NOA 域控制器
- 高阶自动驾驶感知与规划
- 机器人边缘 AI 计算平台
- 多传感器融合智能系统

## 供应链关系

地平线（`ent_company_horizon`）为 BPU Nash 的知识产权持有者与芯片设计者，晶圆制造、封装测试由外部半导体供应链完成。下游客户包括理想、比亚迪、奇瑞、广汽、大众 CARIAD、博世等车企与 Tier-1。在知识图谱中，BPU Nash 作为 `ent_component_bpu_nash` 内嵌于 `ent_product_horizon_journey6` 等征程 6 系列产品。

## 来源与验证

- [Horizon Robotics Journey 6 Series Official](https://www.horizon.auto/en/solutions/horizon-journey/horizon-journey6)
- [Horizon Robotics Journey Series Overview](https://www.horizon.auto/en/solutions/horizon-journey)
- [Journey 6M Baidu Baike](https://baike.baidu.com/en/item/Journey%206M/1756692)