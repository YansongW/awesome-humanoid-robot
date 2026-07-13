---
id: ent_product_ti_tda4vm
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: TI TDA4VM
  en: TI TDA4VM
status: active
sources:
- id: src_ent_product_ti_tda4vm_official
  type: website
  url: https://www.ti.com/product/TDA4VM
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01 00:00:00+00:00
---





# TI TDA4VM / TI TDA4VM

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [德州仪器 / Texas Instruments](../../../appendices/appendix-d/companies/company_texas_instruments.md) |
| **产品类别** | ADAS / 工业边缘 AI SoC / 功能安全处理器 |
| **发布时间** | 2020 年发布，2021 年量产 |
| **状态** | 量产/商用 |
| **官网/来源** | [TI TDA4VM Product Page](https://www.ti.com/product/TDA4VM) |

## 产品概述

TI TDA4VM 是基于 Jacinto 7 架构的异构 SoC，面向 ADAS 与工业边缘 AI。芯片集成 8 TOPS INT8 的 Matrix Multiply Accelerator、C7x 向量 DSP、双核 Cortex-A72 与六核实时 Cortex-R5F，并配备 ISP、视觉加速器、8 端口千兆以太网交换机和 PCIe hub。其 ASIL-D 功能安全支持使其成为高可靠机器人、自动驾驶感知与工业视觉的理想选择。

## 产品图片

> TI TDA4VM Jacinto 处理器：请访问 [官方资料](https://www.ti.com/product/TDA4VM) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制程 | 16 nm FinFET（公开报道） | TI 公开资料 |
| CPU | 双核 64-bit Arm Cortex-A72 @ 最高 2.0 GHz + 六核 Cortex-R5F @ 1.0 GHz | TI 公开资料 |
| AI 加速器 | C7x DSP + Matrix Multiply Accelerator（MMA） | TI 公开资料 |
| AI 算力 | 最高 8 TOPS INT8（MMA） | TI 公开资料 |
| DSP | 2× C7x + 2× C66x | TI 公开资料 |
| GPU | PowerVR Rogue 8XE GE8430（约 100 GFLOPS） | TI 公开资料 |
| ISP/视觉 | 集成第 7 代 ISP、VPAC、DMPAC | TI 公开资料 |
| 内存 | 支持 LPDDR4 | TI 公开资料 |
| 接口 | PCIe hub、8-port GbE switch、CSI-2、CAN-FD、USB 3.1、MCASP | TI 公开资料 |
| 功耗 | 典型约 5–20 W（依配置） | TI 公开资料 |
| 安全 | ASIL-D / SIL-3 目标功能安全 | TI 公开资料 |
| 价格 | SK-TDA4VM 开发套件约 199 USD | TI 公开资料 |

## 供应链位置

- **制造商**：[德州仪器 / Texas Instruments](../../../appendices/appendix-d/companies/company_texas_instruments.md)
- **核心零部件/技术来源**：TI 自研 C7x/MMA/ISP、ARM CPU/GPU IP、16 nm 代工、LPDDR4、PMIC、载板
- **下游应用/客户**：汽车 Tier1/OEM、工业 AMR/AGV 厂商、机器视觉集成商、机器人整机厂

## 知识图谱节点与关系

- 产品实体：`ent_product_ti_tda4vm`
- 零部件实体：`ent_component_ti_tda4vm_soc`
- 制造商实体：`ent_company_texas_instruments`
- 关键关系：
  - `rel_ent_company_texas_instruments_manufactures_ent_product_ti_tda4vm`（`ent_company_texas_instruments` → `manufactures` --> `ent_product_ti_tda4vm`）
  - `rel_ent_company_texas_instruments_manufactures_ent_component_ti_tda4vm_soc`（`ent_company_texas_instruments` → `manufactures` --> `ent_component_ti_tda4vm_soc`）
  - `ent_product_ti_tda4vm` -- `uses` --> `ent_component_ti_tda4vm_soc`

## 应用场景

- **工业 AMR/AGV**：多传感器融合、安全认证、实时路径规划与避障
- **机器视觉检测**：ISP + MMA 实现高速缺陷检测与目标识别
- **ADAS 感知 ECU**：前视/环视、雷达/激光雷达融合，支持 ASIL-D

## 竞争对比

| 对比项 | TI TDA4VM | NXP S32G / i.MX 8M Plus | NVIDIA Jetson Orin NX |
|---|---|---|---|
| AI 算力 | 8 TOPS | 2.3 TOPS / S32G 无 NPU | 最高 100 TOPS |
| 功能安全 | ASIL-D 目标 | ASIL-B/D 依版本 | 工业级 |
| CPU | 双核 A72 + 六核 R5F | 四核 A53 + M7 | 八核 / 十二核 ARM |

## 选购与部署建议

使用 TI Processor SDK（Linux/RTOS）评估 MMA 与 C7x 性能；确认功能安全等级需求；工业部署时选择合适的散热与载板设计。

## 相关词条

- [制造商：德州仪器 / Texas Instruments](../../../appendices/appendix-d/companies/company_texas_instruments.md)
- [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)

## 参考资料

1. [TI TDA4VM 产品页](https://www.ti.com/product/TDA4VM)
2. [TI Jacinto 7 页面](https://www.ti.com/processors/automotive-processors/jacino-7-family.html)
3. [SK-TDA4VM 开发套件](https://www.ti.com/tool/SK-TDA4VM)