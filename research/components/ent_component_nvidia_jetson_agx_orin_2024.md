---
$id: ent_component_nvidia_jetson_agx_orin_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: NVIDIA Jetson AGX Orin
  zh: NVIDIA Jetson AGX Orin
  ko: NVIDIA Jetson AGX Orin
summary:
  en: Onboard GPU/ARM SoC widely used for VLA inference and perception in humanoid robots.
  zh: 广泛用于人形机器人VLA推理和感知的 onboard GPU/ARM SoC。
  ko: 휨로봇 VLA 추론 및 인식에 널리 사용되는 온보드 GPU/ARM SoC.
domains:
- 02_components
- 08_software_middleware
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- agx_orin
- component
- compute
- gpu
- jetson
- nvidia
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/products/product_jetson_agx_orin.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: NVIDIA Jetson AGX Orin
  url: https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-agx-orin/
  date: '2024'
  accessed_at: '2026-07-02'
---
## 概述
NVIDIA Jetson AGX Orin是人形机器人领域的重要component。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## NVIDIA Jetson AGX Orin

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [NVIDIA / 英伟达](../companies/company_nvidia.md) |
| **产品类别** | 边缘 AI 计算模组 |
| **发布时间** | 2022 年 |
| **状态** | 量产/商用 |
| **官网/来源** | [NVIDIA Jetson Orin 页面](https://www.nvidia.cn/autonomous-machines/embedded-systems/jetson-orin/) |

### 产品概述

NVIDIA Jetson AGX Orin 是面向自主机器、机器人与边缘 AI 的高性能计算模组，AI 算力最高可达 275 TOPS（64 GB 版本），是上代 Jetson AGX Xavier 的 8 倍以上。模组采用 NVIDIA Ampere 架构 GPU、Arm Cortex-A78AE CPU 与新一代深度学习/视觉加速器，支持多路高分辨率摄像头、激光雷达、IMU 等传感器的高速接口。

Jetson AGX Orin 有 64 GB、32 GB 与工业版三个版本，功耗可在 15 W 至 60 W 之间配置，满足从低功耗移动机器人到高负载工业设备的不同需求。其统一的 JetPack SDK、Isaac ROS 与 Isaac Sim 生态，使其成为人形机器人、AMR、无人机与自动驾驶原型开发的主流计算平台。

### 产品图片

> NVIDIA Jetson AGX Orin：请访问 [官方资料](https://www.nvidia.cn/autonomous-machines/embedded-systems/jetson-orin/) 查看。

### 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 100 mm × 87 mm（模组） | NVIDIA 官网 |
| AI 算力 | 最高 275 TOPS（64 GB） | NVIDIA 官网 |
| GPU | 2048 核 NVIDIA Ampere 架构 GPU，64 个 Tensor Core | NVIDIA 官网 |
| CPU | 12 核 Arm Cortex-A78AE v8.2 | NVIDIA 官网 |
| 内存 | 64 GB / 32 GB LPDDR5，204.8 GB/s | NVIDIA 官网 |
| DL 加速器 | 2× NVDLA v2 | NVIDIA 官网 |
| 视觉加速器 | 1× PVA v2 | NVIDIA 官网 |
| 摄像头接口 | 16 通道 MIPI CSI-2 | NVIDIA 官网 |
| 功耗 | 15 W – 60 W（可配置） | NVIDIA 官网 |
| 价格 | 未公开（开发者套件约 1,999 USD） | 第三方参考 |

### 供应链位置

- **制造商**：[NVIDIA / 英伟达](../companies/company_nvidia.md)
- **核心零部件/技术来源**：自研 Ampere GPU、Arm CPU、NVDLA、PVA；存储、PMIC、载板由合作伙伴提供。
- **下游应用/客户**：人形机器人、AMR/AGV、无人机、工业视觉、自动驾驶原型、科研教育。

### 知识图谱节点与关系

- 零部件实体：`ent_component_nvidia_jetson_agx_orin`
- 制造商实体：`ent_company_nvidia`
- 关键关系：
  - `rel_ent_company_nvidia_manufactures_ent_component_nvidia_jetson_agx_orin`（`ent_company_nvidia` → `manufactures` → `ent_component_nvidia_jetson_agx_orin`）

### 应用场景

- **人形机器人大脑**：运行 VLM/VLA 模型、SLAM、动态避障与灵巧手控制。
- **AMR/AGV**：多摄像头、激光雷达融合感知与路径规划。
- **工业视觉检测**：边缘端实时缺陷检测、目标识别与测量。
- **自动驾驶原型**：乘用车与无人车的感知与决策验证平台。

### 竞争对比

| 对比项 | Jetson AGX Orin | Jetson Orin NX | Jetson AGX Xavier |
|--------|-----------------|----------------|-------------------|
| AI 算力 | 最高 275 TOPS | 最高 157 TOPS | 32 TOPS |
| 功耗 | 15–60 W | 10–40 W | 10–30 W |
| 内存 | 64 GB LPDDR5 | 16 GB LPDDR5 | 16 GB LPDDR4 |
| 核心优势 | 最高性能、统一生态 | 尺寸小、性价比高 | 成熟稳定 |

### 参考资料

1. [NVIDIA Jetson Orin 官方页面](https://www.nvidia.cn/autonomous-machines/embedded-systems/jetson-orin/)
2. [NVIDIA Jetson AGX Orin Developer Kit](https://developer.nvidia.com/embedded/jetson-agx-orin-developer-kit)
3. [与非网 – 人形机器人主芯片对比](https://www.eefocus.com/article/1821462.html)
4. [CSDN – Jetson 系列算力对比](https://blog.csdn.net/qq_43298381/article/details/144167933)

## 参考
- [NVIDIA Jetson AGX Orin](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-agx-orin/)
- 项目 Wiki：appendix-d/products/product_jetson_agx_orin.md

