# Renesas RZ/V2H 视觉 AI MPU

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [瑞萨电子 / Renesas Electronics](../companies/company_renesas.md) |
| **产品类别** | 集成 DRP-AI3 的视觉 AI MPU / 机器人边缘计算平台 |
| **发布时间** | 2024 年 |
| **状态** | 量产/商用 |
| **官网/来源** | [Renesas RZ/V2H Product Page](https://www.renesas.com/en/products/rz-v2h) |

## 产品概述

Renesas RZ/V2H 是面向高性能视觉 AI 的 MPU，集成瑞萨第三代 DRP-AI3 加速器，提供 8 TOPS 稠密算力与高达 80 TOPS 稀疏算力。芯片采用四核 Cortex-A55、双核实时 Cortex-R8 与 Cortex-M33 的异构组合，支持四路 MIPI CSI、PCIe Gen3、USB 3.2 与多路 CAN-FD，适合需要低功耗、高算力的自主机器人、工业视觉与智能相机应用。

## 产品图片

> Renesas RZ/V2H 视觉 AI MPU：请访问 [官方资料](https://www.renesas.com/en/products/rz-v2h) 查看。

## 规格参数表

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

## 供应链位置

- **制造商**：[瑞萨电子 / Renesas Electronics](../companies/company_renesas.md)
- **核心零部件/技术来源**：瑞萨自研 DRP-AI3 IP、ARM CPU/ISP/GPU IP、LPDDR4x、封测、PMIC、载板
- **下游应用/客户**：机器人整机厂、工业相机与视觉方案商、AGV/AMR 厂商、无人机制造商

## 知识图谱节点与关系

- 产品实体：`ent_product_renesas_rz_v2h`
- 零部件实体：`ent_component_renesas_rz_v2h_soc`
- 制造商实体：`ent_company_renesas`
- 关键关系：
  - `rel_ent_company_renesas_manufactures_ent_product_renesas_rz_v2h`（`ent_company_renesas` → `manufactures` --> `ent_product_renesas_rz_v2h`）
  - `rel_ent_company_renesas_manufactures_ent_component_renesas_rz_v2h_soc`（`ent_company_renesas` → `manufactures` --> `ent_component_renesas_rz_v2h_soc`）
  - `ent_product_renesas_rz_v2h` -- `uses` --> `ent_component_renesas_rz_v2h_soc`

## 应用场景

- **自主移动机器人**：多路视觉感知、SLAM、动态避障与路径规划
- **智能工业相机**：高速缺陷检测、目标识别与测量，无需外部加速器
- **视觉引导机器人**：实时姿态估计与抓取定位，支持 Transformer/CNN 混合网络

## 竞争对比

| 对比项 | RZ/V2H | NXP i.MX 8M Plus | TI TDA4VM |
|---|---|---|---|
| AI 算力（稠密） | 8 TOPS | 2.3 TOPS | 8 TOPS |
| 稀疏算力 | 最高 80 TOPS | 未公开 | 未公开 |
| CPU | 四核 A55 + 双核 R8 | 四核 A53 + M7 | 双核 A72 + 六核 R5F |

## 选购与部署建议

使用 DRP-AI TVM / RUHMI 工具链编译量化模型；确认 DRP-AI 对目标算子的支持；根据相机数量与带宽选择 RZ/V2H EVK 或定制载板。

## 相关词条

- [制造商：瑞萨电子 / Renesas Electronics](../companies/company_renesas.md)
- [附录 D.4 重点产品 Wiki](../index-products.md)

## 参考资料

1. [Renesas RZ/V2H 产品页](https://www.renesas.com/en/products/rz-v2h)
2. [Renesas RZ/V 系列](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rz-v-ai-accelerator)
3. [DRP-AI TVM GitHub](https://renesas-rz.github.io/rzv_drp-ai_tvm/)