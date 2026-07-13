---
id: ent_product_nxp_imx8m_plus
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: NXP i.MX 8M Plus
  en: NXP i.MX 8M Plus
status: active
sources:
- id: src_ent_product_nxp_imx8m_plus_official
  type: website
  url: https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-8-applications-processors/i-mx-8m-plus-arm-cortex-a53-machine-learning-vision-multimedia-and-industrial-iot:IMX8MPLUS
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01 00:00:00+00:00
---





# NXP i.MX 8M Plus / NXP i.MX 8M Plus

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [恩智浦 / NXP Semiconductors](../../../appendices/appendix-d/companies/company_nxp.md) |
| **产品类别** | 集成 NPU 的工业级应用处理器 / 边缘 AI SoC |
| **发布时间** | 2020 年发布，2021 年量产 |
| **状态** | 量产/商用 |
| **官网/来源** | [NXP i.MX 8M Plus Product Page](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-8-applications-processors/i-mx-8m-plus-arm-cortex-a53-machine-learning-vision-multimedia-and-industrial-iot:IMX8MPLUS) |

## 产品概述

NXP i.MX 8M Plus 是面向工业与 AIoT 的 14 nm 异构应用处理器，集成 2.3 TOPS NPU、双 ISP、四核 Cortex-A53 与实时 Cortex-M7。该芯片支持 TSN 千兆以太网、CAN-FD、PCIe 3.0 与多路显示输出，可在本地完成缺陷检测、目标识别等视觉 AI 任务，同时具备工业级温度范围与长供货周期，广泛应用于机器人、AGV 与工业网关。

## 产品图片

> NXP i.MX 8M Plus 应用处理器：请访问 [官方资料](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-8-applications-processors/i-mx-8m-plus-arm-cortex-a53-machine-learning-vision-multimedia-and-industrial-iot:IMX8MPLUS) 查看。

## 规格参数表

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

## 供应链位置

- **制造商**：[恩智浦 / NXP Semiconductors](../../../appendices/appendix-d/companies/company_nxp.md)
- **核心零部件/技术来源**：NXP 自研 NPU 与系统 IP、ARM CPU/GPU IP、台积电/格芯 14 nm 代工、LPDDR4/DDR4、PMIC、封测
- **下游应用/客户**：工业自动化设备商、AGV/AMR 厂商、机器人整机厂、医疗与智能网关客户

## 知识图谱节点与关系

- 产品实体：`ent_product_nxp_imx8m_plus`
- 零部件实体：`ent_component_nxp_imx8m_plus_soc`
- 制造商实体：`ent_company_nxp`
- 关键关系：
  - `rel_ent_company_nxp_manufactures_ent_product_nxp_imx8m_plus`（`ent_company_nxp` → `manufactures` --> `ent_product_nxp_imx8m_plus`）
  - `rel_ent_company_nxp_manufactures_ent_component_nxp_imx8m_plus_soc`（`ent_company_nxp` → `manufactures` --> `ent_component_nxp_imx8m_plus_soc`）
  - `ent_product_nxp_imx8m_plus` -- `uses` --> `ent_component_nxp_imx8m_plus_soc`

## 应用场景

- **工业视觉检测**：NPU 加速缺陷分类与 OCR，双 ISP 支持 HDR 与高动态场景
- **AGV/AMR 主控**：TSN/CAN-FD 支持实时通信，低功耗运行 SLAM 与导航
- **智能网关与 HMI**：多屏异显、丰富接口与工业级可靠性

## 竞争对比

| 对比项 | i.MX 8M Plus | TI TDA4VM | Renesas RZ/V2H |
|---|---|---|---|
| AI 算力 | 2.3 TOPS | 8 TOPS | 8 TOPS（稠密） |
| CPU | 四核 A53 + M7 | 双核 A72 + 六核 R5F | 四核 A55 + 双核 R8 |
| 工业接口 | TSN、CAN-FD、PCIe 3.0 | TSN、CAN-FD、PCIe | CAN-FD、PCIe、USB 3.2 |

## 选购与部署建议

使用 NXP eIQ 工具链评估模型在 NPU 上的性能；注意不同版本（Quad/Lite）是否集成 NPU；工业场景确认温度等级与 ECC 内存配置。

## 相关词条

- [制造商：恩智浦 / NXP Semiconductors](../../../appendices/appendix-d/companies/company_nxp.md)
- [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)

## 参考资料

1. [NXP i.MX 8M Plus 产品页](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-8-applications-processors/i-mx-8m-plus-arm-cortex-a53-machine-learning-vision-multimedia-and-industrial-iot:IMX8MPLUS)
2. [NXP i.MX 8M Plus 数据手册](https://www.nxp.com/docs/en/data-sheet/IMX8MPLUSIEC.pdf)
3. [NXP eIQ 机器学习软件](https://www.nxp.com/design/software/development-software/eiq-ml-software-development-environment:EIQ)