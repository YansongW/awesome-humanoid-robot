---
id: ent_component_qrb4210_soc
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 高通 QRB4210 机器人 SoC
  en: Qualcomm QRB4210 Robotics SoC
status: active
sources:
- id: src_ent_component_qrb4210_soc_1
  type: website
  url: https://www.96boards.org/product/qualcomm-robotics-rb2/
- id: src_ent_component_qrb4210_soc_2
  type: website
  url: https://docs.qualcomm.com/doc/87-61721-1/87-61721-1_REV_B_Qualcomm_Robotics_RB2_Platform__Qualcomm_QRB4210__Product_Brief.pdf
- id: src_ent_component_qrb4210_soc_3
  type: website
  url: https://www.macnica.co.jp/en/business/semiconductor/manufacturers/qualcomm/products/141118/
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 高通 QRB4210 机器人 SoC / Qualcomm QRB4210 Robotics SoC

## 概述

Qualcomm QRB4210 是高通面向机器人与工业物联网应用推出的中端系统级芯片（SoC），也是 Qualcomm Robotics RB2 开发平台的核心处理器。该芯片集成 Kryo 260 八核 CPU、Adreno 610 GPU、Hexagon 683 DSP 与第三代高通 AI 引擎，支持 Linux、ROS 及 Android 操作系统，适用于服务机器人、自主移动机器人（AMR）、工业手持终端、无人机、智能相机与人形机器人边缘计算节点。

## 工作原理 / 技术架构

QRB4210 采用异构计算架构：CPU 负责通用任务与 ROS 节点调度；Adreno 610 GPU 处理 OpenGL ES 3.2 / OpenCL 2.0 / Vulkan 1.1 图形与并行计算；Hexagon 683 DSP 搭载双 HVX（Hexagon Vector eXtensions）向量加速器，用于计算机视觉与 AI 推理卸载；Spectra 340T 三重 ISP 支持多路摄像头并发。内存子系统支持双通道 LPDDR4x @1866 MHz，双通道 16-bit 峰值带宽约为

$$
B_{\text{peak}} = 2 \times 1866\times10^6 \times 2 \times \frac{16}{8} \approx 14.9\ \text{GB/s}
$$

该 SoC 通过 MIPI CSI/DSI、USB 3.1、PCIe、I2C、UART、GPIO 等接口连接传感器、执行器与通信模组，构成机器人边缘感知-决策-控制链路。

## 关键参数表

| 参数项 | 典型值/范围 | 备注/来源 |
|--------|-------------|-----------|
| 制程工艺 | 11 nm（行业公开资料） | 公开报道 |
| CPU | Qualcomm Kryo 260 八核（4×Gold 2.0 GHz + 4×Silver 1.8 GHz） | 高通官方 |
| GPU | Qualcomm Adreno 610 @ 950 MHz | 高通官方 |
| DSP | Qualcomm Hexagon 683 with dual HVX @ 1.0 GHz | 高通官方 |
| AI 引擎 | 第 3 代高通 AI 引擎 | 高通官方 |
| AI 算力 | 未公开 | 高通未披露 |
| 内存 | 双通道 LPDDR4x 1866 MHz + LPDDR3 933 MHz | 高通官方 |
| 存储 | eMMC 5.1 / SD 3.0 / UFS（以具体设计为准） | 高通官方 |
| 显示 | 1080 × 2520 @ 60 fps（DSI） | 高通官方 |
| ISP | Qualcomm Spectra 340T 三重 ISP | 高通官方 |
| 摄像头 | 13+13 MP @ 30 fps；25+5 MP @ 30 fps；16+16 MP @ 24 fps | 高通官方 |
| 视频编解码 | 1080p60 H.264/H.265/VP9 编解码 | 高通官方 |
| 连接 | Wi-Fi 5 / 802.11ac（Wi-Fi 6 ready with WCN3988）、Bluetooth 5.0、GNSS | 高通官方 |
| 定位 | GPS、GLONASS、NavIC、BeiDou、Galileo、QZSS、SBAS | 高通官方 |
| 安全 | TEE、TrustZone、Secure Boot、Key Provisioning | 高通官方 |
| 封装 | 752 NSP，12.0 mm × 12.4 mm × 0.91 mm，0.4 mm pitch | Macnica |
| 操作系统 | Linux / Android（QRB4210 对应 Linux） | 高通官方 |
| 价格 | 未公开 | 需询价 |

## 应用场景

- **服务机器人与 AMR**：边缘 SLAM、避障、物体识别与路径规划。
- **工业物联网手持设备**：仓库盘点、质量检测、人机交互终端。
- **无人机**：航拍、巡检、物流无人机的视觉与飞控处理。
- **人形机器人边缘节点**：头部/躯干感知计算、多摄像头融合、语音交互。

## 供应链关系

- **设计者/品牌**：高通 / Qualcomm（`ent_company_qualcomm`）。
- **晶圆制造/封测**：台积电等（公开报道）。
- **上游关键 IP/材料**：ARM 兼容 CPU 核、Adreno/Hexagon 自研 IP、LPDDR 存储器、射频前端、基带、PMIC。
- **下游客户/应用场景**：机器人 OEM、无人机厂商、工业手持设备商、IoT 方案商、开发者社区。
- **竞争/对标**：NVIDIA Jetson Orin Nano / TX2、地平线 Journey 系列、瑞芯微 RK3588、全志 T527。
- **知识图谱关系**：`ent_company_qualcomm` — `manufactures` → `ent_component_qrb4210_soc`；该 SoC 用于 `ent_product_qualcomm_rb5` 等平台级产品。

## 来源与验证

1. [96Boards：Qualcomm Robotics RB2 Development Platform](https://www.96boards.org/product/qualcomm-robotics-rb2/)
2. [Qualcomm Robotics RB2 Platform Product Brief（PDF）](https://docs.qualcomm.com/doc/87-61721-1/87-61721-1_REV_B_Qualcomm_Robotics_RB2_Platform__Qualcomm_QRB4210__Product_Brief.pdf)
3. [Macnica：Qualcomm QCS4290/QRB4210 SoC 产品规格](https://www.macnica.co.jp/en/business/semiconductor/manufacturers/qualcomm/products/141118/)