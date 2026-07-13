---
id: ent_component_allwinner_a523_soc
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: 全志 A523 系统级芯片
  en: Allwinner A523 SoC
sources:
- id: src_allwinner_official
  type: website
- title: '"全志科技官网"'
  url: https://www.allwinnertech.com
- id: src_linux_sunxi_a523
  type: website
- title: '"linux-sunxi A523"'
  url: https://linux-sunxi.org/A523
- id: src_datasheet4u_a523
  type: website
- title: '"Allwinner A523 Datasheet"'
  url: https://datasheet4u.com/datasheets/Allwinner/A523/1603223
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from official datasheets, product manuals and verified
    distributors; missing values marked as 未公开.
---


# 全志 A523 系统级芯片 / Allwinner A523 SoC

## 概述

全志 A523（sun55iw3）是全志科技面向平板、AIoT 与轻量机器人应用设计的 64 位应用处理器 SoC。芯片集成八核 Arm Cortex-A55、Arm Mali-G57 GPU、XuanTie E906 RISC-V 协处理器以及丰富的多媒体与工业接口，以高性价比、长供货周期满足机器人主控、边缘网关与智能终端需求。

## 工作原理 / 技术架构

A523 采用 22 nm HPC 工艺，CPU 由两个四核 Cortex-A55 簇组成（高性能簇最高 1.8 GHz、能效簇 1.42 GHz），共享 1 MB L3 Cache；RISC-V E906 核心最高 200 MHz，用于系统管理或实时控制。GPU 为 Mali-G57 MC1，支持 OpenGL ES 3.2/Vulkan 1.1/OpenCL 2.0。多媒体子系统支持 4K@60fps H.265/VP9 解码、4K@30fps H.264 解码与 4K@25fps H.264 编码，ISP 支持最高 8 MP@30fps 多路 MIPI CSI。

## 关键参数表

| 参数 | 数值 | 备注 |
|---|---|---|
| 制程 | 22 nm HPC | linux-sunxi |
| CPU | 八核 Cortex-A55（4×1.8 GHz + 4×1.42 GHz） | 官方/社区资料 |
| 协处理器 | XuanTie E906 RISC-V @ 200 MHz | 官方/社区资料 |
| GPU | Arm Mali-G57 MC1 | 官方/社区资料 |
| AI 算力 | 最高 2 TOPS INT8 | 第三方资料 |
| 内存 | 32-bit DDR3/DDR4/LPDDR3/LPDDR4/LPDDR4X，最大 4 GB | 官方/社区资料 |
| 视频解码 | H.265/VP9 4K@60fps；H.264 4K@30fps | 官方/社区资料 |
| 视频编码 | H.264 4K@25fps | 官方/社区资料 |
| 摄像头接口 | 4+4-lane MIPI CSI，最高 8 MP@30fps | 官方/社区资料 |
| 高速接口 | USB 3.1/PCIe 2.1 Combo、GbE | 官方/社区资料 |
| 封装 | FCCSP 522 balls，15 mm × 15 mm | 社区资料 |
| TDP | 约 5 W | 第三方资料 |

## 应用场景

平板电脑、教育平板、AIoT 终端、机器人低成本主控、工业网关、智能商显、边缘 AI 推理。

## 供应链关系

全志科技（`ent_company_allwinner`）设计 A523，由台积电/中芯国际等代工；下游客户包括 Orange Pi 等开发板厂商、平板/智能硬件 OEM 与机器人整机厂，与瑞芯微 RK3568/RK3588、联发科 Genio、晶晨半导体等形成竞争。

## 来源与验证

- 全志科技官网：https://www.allwinnertech.com
- linux-sunxi A523 页面：https://linux-sunxi.org/A523
- Allwinner A523 Datasheet（datasheet4u）：https://datasheet4u.com/datasheets/Allwinner/A523/1603223