---
id: ent_product_rockchip_rk3576
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: Rockchip RK3576
  en: Rockchip RK3576
status: active
sources:
- id: src_rockchip_rk3576_yibeiic
  type: website
  url: https://www.yibeiic.com/cms/Article/get/article_id/16910
- title: 瑞芯微 RK 系列芯片深度解析：RK3588/RK3576 参数对比 | 亿配芯城
- id: src_rockchip_rk3576_industio
  type: website
  url: https://blog.csdn.net/Industio_CSDN/article/details/153988108
- title: 瑞芯微 RK3576 核心板详细参数配置 | 触觉智能
- id: src_rockchip_rk3576_iotdt
  type: website
  url: http://iotdt.com/news/xingyezixun/841.html
- title: 瑞芯微 RK3576 芯片参数：高性能低功耗的 SoC 处理器 | 万物纵横
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# Rockchip RK3576

## 概述

RK3576 是瑞芯微（Rockchip）推出的高性能、低功耗边缘 AI SoC，采用 8 nm 制程，集成 4 核 Cortex-A72 + 4 核 Cortex-A53 CPU、ARM Mali-G52 MC3 GPU 与双核 NPU，INT8 算力 6 TOPS。该芯片支持 LPDDR4/LPDDR4X/LPDDR5 内存、UFS 2.0 存储、PCIe 2.1、USB 3.0、HDMI 2.1 与多路 MIPI CSI/DSI，主要面向工业平板、边缘 AI 网关、智能机器人、智能相机与中高端 AIoT 设备。

## 工作原理 / 技术架构

RK3576 采用大小核异构 CPU 架构，4 颗 Cortex-A72 负责高性能计算，主频最高 2.2–2.3 GHz；4 颗 Cortex-A53 负责能效敏感任务。CPU 综合算力约 58K DMIPS，满足多任务并发需求。

NPU 为瑞芯微自研双核架构，INT8 峰值算力 6 TOPS，支持 INT4/INT8/INT16/FP16/BF16/TF32 混合精度，可通过 RKNN-Toolkit2 将 TensorFlow、PyTorch、ONNX 等模型量化部署。NPU 利用率受模型结构、内存带宽与量化方式影响，有效推理吞吐可近似表示为

$$
T_{\text{eff}} = \frac{\text{TOPS} \times \eta}{\text{OPs per sample}} \times \text{batch}
$$

其中 $\eta$ 为实际利用率，典型值 30%–70%。

视频处理单元支持 8K@30 fps 或 4K@120 fps 解码、4K@60 fps 编码；ISP V3.9 支持 16 MP 传感器与 120 dB HDR，适用于机器人视觉、智能门铃与工业相机。

## 关键参数表

| 参数 | 数值/说明 | 备注 |
|------|-----------|------|
| 制程 | 8 nm | 行业资料 |
| CPU | 4×Cortex-A72 + 4×Cortex-A53 | 异构八核 |
| A72 主频 | 最高 2.2–2.3 GHz | 不同来源 |
| A53 主频 | 最高 2.2 GHz | 不同来源 |
| GPU | ARM Mali-G52 MC3 @ 950 MHz | 官方/方案商 |
| NPU | 双核 6 TOPS @ INT8 | 官方/方案商 |
| 支持数据类型 | INT4/INT8/INT16/FP16/BF16/TF32 | 方案商资料 |
| 内存 | LPDDR4/LPDDR4X/LPDDR5，最大 16 GB | 方案商资料 |
| 内存带宽 | 25.6 GB/s（LPDDR5 32 bit）| 方案商资料 |
| 存储 | eMMC 5.1、UFS 2.0 | 方案商资料 |
| PCIe | PCIe 2.1 | 方案商资料 |
| USB | USB 3.0 / USB 2.0 | 方案商资料 |
| 显示 | HDMI 2.1（4K@120 fps）、DP 1.4、MIPI-DSI | 方案商资料 |
| 视频输入 | MIPI CSI、DVP | 方案商资料 |
| 视频解码 | 8K@30 fps / 4K@120 fps | 方案商资料 |
| 视频编码 | 4K@60 fps | 方案商资料 |
| ISP | 16 MP，HDR up to 120 dB | 方案商资料 |
| 网络 | 双千兆以太网、Wi-Fi 5 / 蓝牙 5.2 | 方案商资料 |
| 安兔兔跑分 | 约 34.2 万 | 行业评测 |

## 应用场景

- **智能机器人**：作为中端人形/轮式机器人的主控，负责视觉感知、SLAM、路径规划与 AI 推理。
- **边缘 AI 网关**：在工业现场完成图像识别、缺陷检测与协议转换，降低云端依赖。
- **工业平板与 HMI**：多核 CPU + GPU 支持复杂人机界面与实时控制显示。
- **智能相机与门禁**：集成 ISP 与 NPU，实现人脸识别、行为分析与事件告警。
- **AIoT 设备**：家居中控、智能音箱、广告机等对成本与功耗敏感的智能终端。

## 供应链关系

RK3576 属于 **边缘 AI 芯片/SoC 层**，上游依赖 ARM CPU/GPU IP 授权、晶圆代工（如台积电、中芯国际）、封测与存储颗粒；中游由瑞芯微完成 SoC 设计、参考方案与工具链（RKNN）提供；下游包括核心板/开发板厂商（如触觉智能、正点原子）、整机厂商与系统集成商。在机器人产业链中，RK3576 常作为感知-决策主控芯片，连接摄像头、激光雷达、电机驱动与通信模块。

## 来源与验证

- 亿配芯城 RK3588/RK3576 对比分析：https://www.yibeiic.com/cms/Article/get/article_id/16910
- 触觉智能 RK3576 核心板规格书：https://blog.csdn.net/Industio_CSDN/article/details/153988108
- 万物纵横 RK3576 芯片参数解析：http://iotdt.com/news/xingyezixun/841.html

瑞芯微官网未公开 RK3576 完整 datasheet，表中主频、GPU 频率、接口细节等主要来自核心板厂商与行业评测；具体参数以芯片原厂规格书为准。