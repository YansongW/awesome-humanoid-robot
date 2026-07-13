# 瑞萨电子 / Renesas Electronics

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 瑞萨电子 |
| **英文名** | Renesas Electronics |
| **总部** | 日本东京 |
| **成立时间** | 2010 年（NEC 电子与日立/三菱半导体业务合并） |
| **官网** | [https://www.renesas.com](https://www.renesas.com) |
| **供应链环节** | MCU/MPU、边缘 AI、汽车电子、工业控制、机器人视觉 |
| **企业属性** | 上市公司（TSE: 6723） |
| **母公司/所属集团** | 无（Renesas Electronics 为上市主体） |
| **数据来源** | Renesas 官网、RZ/V 产品手册、公开新闻稿、行业研报 |

## 公司简介

Renesas Electronics（瑞萨电子）是全球领先的 MCU/MPU 与模拟半导体供应商，产品广泛应用于汽车、工业与基础设施。其 RZ/V 系列 AI MPU 集成自研 DRP-AI 加速器，以极低功耗实现高 TOPS 视觉推理；RA/RX/RL 系列 MCU 则覆盖从传感器节点到实时控制的广泛场景。瑞萨还提供完整的 AI 工具链与参考设计，支持机器人、智能相机与工业视觉快速落地。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| RZ/V 系列 | 视觉 AI MPU / DRP-AI 加速器 | RZ/V2H / RZ/V2N | 机器人、智能相机、工业视觉、ADAS |
| RA / RX / RL MCU | 实时控制与安全 MCU | RA8 / RX700 | 电机控制、传感器节点、功能安全 |

## 代表产品

### Renesas RZ/V2H

> Renesas RZ/V2H：请访问 [官方资料](https://www.renesas.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制程 | 未公开 | Renesas 公开资料 |
| CPU | 四核 Arm Cortex-A55 @ 1.8 GHz + 双核 Cortex-R8 @ 800 MHz + Cortex-M33 @ 200 MHz | Renesas 公开资料 |
| AI 加速器 | DRP-AI3（动态可重配置处理器 + AI-MAC） | Renesas 公开资料 |
| AI 算力 | 8 TOPS（稠密模型）/ 最高 80 TOPS（稀疏模型） | Renesas 公开资料 |
| ISP | 可选 Arm Mali-C55 ISP | Renesas 公开资料 |
| GPU | GE3D 3D GPU | Renesas 公开资料 |
| 内存 | LPDDR4 / LPDDR4X 接口 | Renesas 公开资料 |
| 接口 | PCIe Gen3 x4、USB 3.2 Gen2 x2、GbE x2、MIPI CSI-2 x4、CAN-FD x6 | Renesas 公开资料 |
| 功耗 | 未公开（典型低于 10 W） | Renesas 公开资料 |
| 封装 | BGA 19 mm × 19 mm，1368 pin | Renesas 公开资料 |
| 价格 | 未公开 | Renesas 公开资料 |

**技术亮点**：DRP-AI3 高算力低功耗、支持 INT8 量化与剪枝、四路 MIPI CSI、PCIe/USB 3.2 高速接口、无需风扇即可运行高负载 AI。

**应用场景**：**自主移动机器人**：多路视觉感知、SLAM、动态避障与路径规划；**智能工业相机**：高速缺陷检测、目标识别与测量，无需外部加速器；**视觉引导机器人**：实时姿态估计与抓取定位，支持 Transformer/CNN 混合网络

### Renesas RZ/V2N

> Renesas RZ/V2N：请访问 [官方资料](https://www.renesas.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| CPU | 四核 Cortex-A55 + Cortex-M33 | Renesas 公开资料 |
| AI 加速器 | DRP-AI3 | Renesas 公开资料 |
| AI 算力 | 最高 15 TOPS（稀疏） | Renesas 公开资料 |
| 功耗 | 低功耗无风扇设计 | Renesas 公开资料 |
| 接口 | MIPI CSI、PCIe、USB、GbE、CAN-FD | Renesas 公开资料 |
| 封装 | 15 mm × 15 mm | Renesas 公开资料 |
| 价格 | 未公开 | Renesas 公开资料 |

**技术亮点**：更小封装、更低功耗、继承 RZ/V2H 的 DRP-AI3 架构，适合高量产视觉 AI 设备。

**应用场景**：智能安防相机、交通监控、工业视觉、服务机器人。

## 供应链位置

- **上游关键零部件/材料**：瑞萨自研 DRP-AI IP、ARM CPU/ISP IP、台积电代工、LPDDR4x、封测、PMIC
- **下游客户/应用场景**：汽车 OEM/Tier1、工业自动化厂商、机器人公司、智能相机与安防客户
- **主要竞争对手/对标**：NXP i.MX、Texas Instruments Jacinto、NVIDIA Jetson、地平线征程、Ambarella

## 知识图谱节点与关系

- 公司实体：`ent_company_renesas`
- 产品实体：`ent_product_renesas_rz_v2h`、`ent_product_renesas_rz_v2n`
- 零部件实体：`ent_component_renesas_rz_v2h_soc`、`ent_component_renesas_rz_v2n_soc`
- 关键关系：
  - `ent_company_renesas` -- `manufactures` --> `ent_product_renesas_rz_v2h`
  - `ent_company_renesas` -- `manufactures` --> `ent_product_renesas_rz_v2n`
  - `ent_company_renesas` -- `manufactures` --> `ent_component_renesas_rz_v2h_soc`
  - `ent_company_renesas` -- `manufactures` --> `ent_component_renesas_rz_v2n_soc`
  - `ent_product_renesas_rz_v2h` -- `uses` --> `ent_component_renesas_rz_v2h_soc`
  - `ent_product_renesas_rz_v2n` -- `uses` --> `ent_component_renesas_rz_v2n_soc`

## 参考资料

1. [Renesas 官网](https://www.renesas.com)
2. [RZ/V2H 产品页](https://www.renesas.com/en/products/rz-v2h)
3. [Renesas RZ/V 系列](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rz-v-ai-accelerator)