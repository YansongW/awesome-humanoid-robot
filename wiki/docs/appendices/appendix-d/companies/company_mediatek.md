# 联发科 / MediaTek

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 联发科 |
| **英文名** | MediaTek |
| **总部** | 中国台湾新竹 |
| **成立时间** | 1997 年 |
| **官网** | [https://www.mediatek.com](https://www.mediatek.com) |
| **供应链环节** | 边缘 AI SoC、AIoT、移动/计算平台、机器人主控 |
| **企业属性** | 上市公司（TWSE: 2454） |
| **母公司/所属集团** | 无（MediaTek 为上市主体） |
| **数据来源** | MediaTek 官网、Genio 产品资料、公开新闻稿、行业研报 |

## 公司简介

MediaTek（联发科）是全球领先的半导体设计公司，产品覆盖智能手机、平板电脑、电视、可穿戴设备、汽车与 AIoT。其 Genio 系列边缘 AI 平台面向工业 IoT、机器人与智能设备，集成多核 CPU、GPU、APU（AI 处理器）与丰富多媒体接口，以先进 6 nm 工艺实现高性能与低功耗平衡，并提供 NeuroPilot SDK 与 Yocto/Ubuntu 支持。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| Genio 系列 | AIoT 边缘 AI 平台 | Genio 1200 / 700 / 510 | 工业 IoT、机器人、智能零售、数字标牌、边缘网关 |
| Filogic / Pentonic | 连接与显示平台 | Filogic 880 | Wi-Fi 7 路由、智能电视、AIoT 网关 |

## 代表产品

### MediaTek Genio 1200

> MediaTek Genio 1200：请访问 [官方资料](https://www.mediatek.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制程 | 6 nm | MediaTek 公开资料 |
| CPU | 八核（4× Cortex-A78 @ 最高 2.2 GHz + 4× Cortex-A55） | MediaTek 公开资料 |
| GPU | Arm Mali-G57 MC5 | MediaTek 公开资料 |
| AI 加速器 | MediaTek 多核 APU | MediaTek 公开资料 |
| AI 算力 | 最高 4.8 TOPS INT8 | MediaTek 公开资料 |
| 视觉 | 双 ISP，最高 48 MP 单摄 / 16 MP+16 MP 双摄，4K90 解码 | MediaTek 公开资料 |
| DSP | 双 Cadence Tensilica VP6 + HiFi 4 Audio DSP | MediaTek 公开资料 |
| 内存 | 支持 LPDDR4X，最高 16 GB | MediaTek 公开资料 |
| 接口 | PCIe 3.0、USB 3.2 Gen1、GbE（TSN）、MIPI CSI/DSI、HDMI、UART/I2C/SPI | MediaTek 公开资料 |
| 功耗 | 典型约 6–10 W（整板/模组） | MediaTek 公开资料 |
| 价格 | 开发套件约 200–400 USD（参考价） | MediaTek 公开资料 |

**技术亮点**：6 nm 旗舰 AIoT SoC、4.8 TOPS APU、三屏 4K、双 ISP、丰富高速接口、支持 Android/Yocto/Ubuntu 与 ROS。

**应用场景**：**工业机器人与 AMR**：多路视觉感知、SLAM、路径规划与机械臂控制；**智能相机与安防**：4K 实时目标检测、人脸识别与行为分析；**边缘 AI 网关与 HMI**：多屏显示、设备互联与本地 AI 推理

### MediaTek Genio 700

> MediaTek Genio 700：请访问 [官方资料](https://www.mediatek.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制程 | 6 nm | MediaTek 公开资料 |
| CPU | 八核（4× Cortex-A78 + 4× Cortex-A55） | MediaTek 公开资料 |
| GPU | Arm Mali-G57 MC3 | MediaTek 公开资料 |
| AI 算力 | 约 4 TOPS | MediaTek 公开资料 |
| 视频 | 4K60 编解码 | MediaTek 公开资料 |
| 接口 | PCIe、USB 3.0、GbE、MIPI CSI/DSI | MediaTek 公开资料 |
| 功耗 | 约 4–8 W | MediaTek 公开资料 |
| 价格 | 未公开 | MediaTek 公开资料 |

**技术亮点**：中高端 AIoT 平台，6 nm 能效比、丰富多媒体与连接能力。

**应用场景**：智能零售、工业 HMI、智能相机、边缘网关。

## 供应链位置

- **上游关键零部件/材料**：台积电 6 nm 代工、ARM CPU/GPU IP、自研 APU、LPDDR5、UFS、封测、载板
- **下游客户/应用场景**：AIoT 设备商、机器人整机厂、智能零售与数字标牌厂商、工业网关客户
- **主要竞争对手/对标**：Qualcomm QCS、NVIDIA Jetson、Rockchip RK3588、Allwinner T527、Amlogic

## 知识图谱节点与关系

- 公司实体：`ent_company_mediatek`
- 产品实体：`ent_product_mediatek_genio_1200`、`ent_product_mediatek_genio_700`
- 零部件实体：`ent_component_mediatek_genio_1200_soc`、`ent_component_mediatek_genio_700_soc`
- 关键关系：
  - `ent_company_mediatek` -- `manufactures` --> `ent_product_mediatek_genio_1200`
  - `ent_company_mediatek` -- `manufactures` --> `ent_product_mediatek_genio_700`
  - `ent_company_mediatek` -- `manufactures` --> `ent_component_mediatek_genio_1200_soc`
  - `ent_company_mediatek` -- `manufactures` --> `ent_component_mediatek_genio_700_soc`
  - `ent_product_mediatek_genio_1200` -- `uses` --> `ent_component_mediatek_genio_1200_soc`
  - `ent_product_mediatek_genio_700` -- `uses` --> `ent_component_mediatek_genio_700_soc`

## 参考资料

1. [MediaTek 官网](https://www.mediatek.com)
2. [MediaTek Genio 1200](https://genio.mediatek.com/genio-1200)
3. [MediaTek Genio 平台](https://www.mediatek.com/products/iot/genio)