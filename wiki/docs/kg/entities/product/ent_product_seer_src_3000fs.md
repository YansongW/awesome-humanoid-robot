---
id: ent_product_seer_src_3000fs
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: component
names:
  zh: 仙工 SRC-3000FS
  en: SEER SRC-3000FS
status: active
sources:
- id: src_seer_src3000fs_datasheet
  type: report
  url: http://uploadfile.gongkong.com/Upload/gongkong/technicalDataAttachment/202207/08/f8110c68d8514e1e95f20a26a5e26e5e.pdf
- title: SRC-3000FS 参数表 - 仙工智能
- id: src_seer_src3000fs_media
  type: website
  url: https://seer-robotics.ai/zh/media/11.0
- title: 新品推介 | 想做 AMR 的整机安全认证，就选 SRC-3000FS - 仙工智能
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 仙工 SRC-3000FS / SEER SRC-3000FS

## 概述

仙工 SRC-3000FS 是上海仙工智能科技有限公司（SEER）自主研发的安全型 AMR（自主移动机器人）控制器，是全球首款通过 SGS TÜV SAAR 功能安全认证、集激光 SLAM 导航与功能安全于一体的移动机器人控制器。该控制器可替代传统“安全 PLC + 导航控制器”的分立方案，帮助集成商以更紧凑的结构、更低的成本打造符合 ISO 3691-4 标准的安全型 AMR。

## 工作原理 / 技术架构

SRC-3000FS 集成多核异构计算平台：Cortex-A72×2 负责 SLAM 导航与上层应用，Cortex-A73 负责 AI/视觉处理，Cortex-M4×2 负责实时安全控制。控制器内置安全急停、安全速度监控、安全转向检测、安全停障与安全限位五大安全功能。

激光 SLAM 导航通过 2D/3D 激光雷达扫描环境，构建占据栅格地图并实时定位。机器人位姿估计可表示为：

$$
\mathbf{x}_t = f(\mathbf{x}_{t-1}, \mathbf{u}_t) + \mathbf{w}_t
$$

其中 $\mathbf{x}$ 为机器人位姿，$\mathbf{u}$ 为里程计输入，$\mathbf{w}$ 为过程噪声。通过激光观测进行卡尔曼滤波或粒子滤波更新，实现 ±2 mm 的定位精度。

## 关键参数表

| 参数 | 数值 |
|------|------|
| 计算平台 | Cortex-A72×2 + Cortex-A73 + Cortex-M4×2 |
| 内存 | 4 GB LPDDR4 |
| 存储 | 16 GB eMMC |
| 无线通信 | 802.11ac 2×2 Wi-Fi |
| 工业以太网 | 5 路千兆以太网，支持 IEEE 1588 PTP |
| 供电输入 | 24 V / 48 V 蓄电池 |
| 防护等级 | IP65 |
| 工作温度 | 30°C–55°C |
| 存储温度 | -40°C–70°C |
| 功能安全认证 | SGS TÜV SAAR |
| 安全等级 | IEC 61508 SIL2 / ISO 13849-1 Cat.3 PLd |
| 适用标准 | ISO 3691-4 |
| 支持车型 | 安全型双轮差速 AMR、单舵轮 AMR |

## 应用场景

- 工厂内部物流搬运与产线对接
- 仓储自动化分拣与盘点
- 3C、汽车、新能源、半导体等行业的 AMR 底盘
- 需要整机安全认证的出口型 AMR

## 供应链关系

仙工智能位于移动机器人控制器产业链中游，上游采购计算芯片、工业以太网芯片、安全继电器与结构件；中游为控制器硬件、Robokit 软件系统与造车方案；下游面向 AMR 集成商与终端工厂。SRC-3000FS 是 SRC 系列中的高端安全型号，与 SRC-2000 等通用型控制器形成产品梯度。

## 来源与验证

参数来源于仙工智能官方参数表 PDF（http://uploadfile.gongkong.com/Upload/gongkong/technicalDataAttachment/202207/08/f8110c68d8514e1e95f20a26a5e26e5e.pdf）及仙工智能官网媒体文章（https://seer-robotics.ai/zh/media/11.0）。具体接口数量与扩展能力以最新产品手册为准。