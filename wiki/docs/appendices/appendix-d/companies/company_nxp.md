# 恩智浦 / NXP Semiconductors

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 恩智浦 |
| **英文名** | NXP Semiconductors |
| **总部** | 荷兰埃因霍温 |
| **成立时间** | 2006 年（Philips 半导体部门独立） |
| **官网** | [https://www.nxp.com](https://www.nxp.com) |
| **供应链环节** | MCU/MPU、边缘 AI、工业控制、汽车电子、机器人主控 |
| **企业属性** | 上市公司（NASDAQ: NXPI） |
| **母公司/所属集团** | 无（NXP Semiconductors 为上市主体） |
| **数据来源** | NXP 官网、i.MX 产品手册、公开新闻稿、行业研报 |

## 公司简介

NXP Semiconductors（恩智浦）是全球领先的嵌入式半导体供应商，产品覆盖 MCU、MPU、安全识别、汽车电子与模拟器件。其 i.MX 系列应用处理器面向工业、汽车与物联网边缘计算，i.MX 8M Plus 等型号集成 NPU，可为机器人、工业视觉与 AIoT 提供本地 AI 推理能力，同时具备高可靠性与长供货周期。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| i.MX 8 系列 | 高性能多媒体与 AI 应用处理器 | i.MX 8M Plus | 工业 HMI、机器人主控、边缘 AI、智能网关 |
| i.MX 9 / i.MX 93 系列 | 集成 NPU 的下一代边缘 AI 处理器 | i.MX 93 | AIoT、工业自动化、智能家居、机器人 |

## 代表产品

### NXP i.MX 8M Plus

> NXP i.MX 8M Plus：请访问 [官方资料](https://www.nxp.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制程 | 14 nm FinFET | NXP 公开资料 |
| CPU | 四核 Arm Cortex-A53 @ 最高 1.8 GHz + Cortex-M7 @ 800 MHz | NXP 公开资料 |
| NPU | 集成 Neural Processing Unit | NXP 公开资料 |
| AI 算力 | 最高 2.3 TOPS INT8 | NXP 公开资料 |
| ISP | 双 ISP，支持 12MP、HDR、鱼眼矫正 | NXP 公开资料 |
| GPU | Vivante GC7000UL 3D GPU + GC520L 2D GPU | NXP 公开资料 |
| 内存 | 支持 LPDDR4/DDR4，最高 6 GB（模组常见 2–4 GB） | NXP 公开资料 |
| 接口 | USB 3.0、PCIe 3.0、2× GbE（含 TSN）、2× CAN-FD、MIPI CSI/DSI、HDMI、LVDS | NXP 公开资料 |
| 功耗 | 未公开（典型整板 2–5 W） | NXP 公开资料 |
| 封装 | FCBGA 15 mm × 15 mm | NXP 公开资料 |
| 价格 | 未公开 | NXP 公开资料 |

**技术亮点**：集成 NPU 的工业级异构 SoC、双 ISP、TSN 以太网、CAN-FD、ECC 内存、15 年供货周期，适合功能安全与实时控制场景。

**应用场景**：**工业视觉检测**：NPU 加速缺陷分类与 OCR，双 ISP 支持 HDR 与高动态场景；**AGV/AMR 主控**：TSN/CAN-FD 支持实时通信，低功耗运行 SLAM 与导航；**智能网关与 HMI**：多屏异显、丰富接口与工业级可靠性

### NXP i.MX 93

> NXP i.MX 93：请访问 [官方资料](https://www.nxp.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| CPU | 双核 Cortex-A55 + Cortex-M33 | NXP 公开资料 |
| NPU | 集成 Arm Ethos U65 | NXP 公开资料 |
| AI 算力 | 约 0.5 TOPS | NXP 公开资料 |
| 制程 | 未公开 | NXP 公开资料 |
| 接口 | GbE、CAN-FD、USB、MIPI CSI/DSI | NXP 公开资料 |
| 功耗 | 极低功耗设计 | NXP 公开资料 |
| 价格 | 未公开 | NXP 公开资料 |

**技术亮点**：低功耗、低成本、集成 Arm Ethos U65 NPU，适合轻量 AIoT 与语音/视觉唤醒。

**应用场景**：智能家居、工业传感器、语音助手、轻量机器人控制。

## 供应链位置

- **上游关键零部件/材料**：台积电/格芯代工、ARM IP、自研 NPU、LPDDR4/DDR4、eMMC、封测、PMIC
- **下游客户/应用场景**：工业自动化厂商、汽车 OEM/Tier1、机器人整机厂、AIoT 设备商、网关厂商
- **主要竞争对手/对标**：Texas Instruments Jacinto、Renesas RZ/V、NVIDIA Jetson、Qualcomm QCS、瑞芯微 RK3588

## 知识图谱节点与关系

- 公司实体：`ent_company_nxp`
- 产品实体：`ent_product_nxp_imx8m_plus`、`ent_product_nxp_imx93`
- 零部件实体：`ent_component_nxp_imx8m_plus_soc`、`ent_component_nxp_imx93_soc`
- 关键关系：
  - `ent_company_nxp` -- `manufactures` --> `ent_product_nxp_imx8m_plus`
  - `ent_company_nxp` -- `manufactures` --> `ent_product_nxp_imx93`
  - `ent_company_nxp` -- `manufactures` --> `ent_component_nxp_imx8m_plus_soc`
  - `ent_company_nxp` -- `manufactures` --> `ent_component_nxp_imx93_soc`
  - `ent_product_nxp_imx8m_plus` -- `uses` --> `ent_component_nxp_imx8m_plus_soc`
  - `ent_product_nxp_imx93` -- `uses` --> `ent_component_nxp_imx93_soc`

## 参考资料

1. [NXP 官网](https://www.nxp.com)
2. [i.MX 8M Plus 产品页](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-8-applications-processors/i-mx-8m-plus-arm-cortex-a53-machine-learning-vision-multimedia-and-industrial-iot:IMX8MPLUS)
3. [NXP i.MX 生态系统](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors:IMX_HOME)