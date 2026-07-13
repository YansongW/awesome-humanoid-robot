# 德州仪器 / Texas Instruments

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 德州仪器 |
| **英文名** | Texas Instruments |
| **总部** | 美国德克萨斯州达拉斯 |
| **成立时间** | 1930 年 |
| **官网** | [https://www.ti.com](https://www.ti.com) |
| **供应链环节** | 工业 MCU、Jacinto ADAS/边缘 AI、模拟与电源管理 |
| **企业属性** | 上市公司（NASDAQ: TXN） |
| **母公司/所属集团** | 无（Texas Instruments 为上市主体） |
| **数据来源** | TI 官网、Jacinto 产品手册、公开新闻稿、行业研报 |

## 公司简介

Texas Instruments（德州仪器）是全球最大的模拟与嵌入式半导体公司之一，产品覆盖处理器、MCU、传感器、电源管理与模拟器件。其 Jacinto 7 系列 SoC（如 TDA4VM）专为 ADAS 与边缘 AI 设计，集成深度学习加速器（MMA）、DSP、ISP、功能安全硬件与丰富工业接口，广泛应用于汽车、工业机器人和机器视觉。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| Jacinto 7 / TDA4x | ADAS 与边缘 AI 处理器 | TDA4VM | 自动驾驶感知、工业 AMR、机器视觉、边缘 AI Box |
| Sitara / AM6x | 工业级 Arm 处理器 | AM68A / AM69A | 工业网关、机器人控制、HMI、实时通信 |

## 代表产品

### TI TDA4VM

> TI TDA4VM：请访问 [官方资料](https://www.ti.com) 查看。

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

**技术亮点**：Jacinto 7 异构架构、8 TOPS MMA、C7x 向量 DSP、集成 ISP 与 VPAC/DMPAC、ASIL-D 功能安全、丰富车载/工业接口。

**应用场景**：**工业 AMR/AGV**：多传感器融合、安全认证、实时路径规划与避障；**机器视觉检测**：ISP + MMA 实现高速缺陷检测与目标识别；**ADAS 感知 ECU**：前视/环视、雷达/激光雷达融合，支持 ASIL-D

### TI AM68A

> TI AM68A：请访问 [官方资料](https://www.ti.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| CPU | 双核 Cortex-A72 + 六核 Cortex-R5F | TI 公开资料 |
| AI 加速器 | MMA + C7x DSP | TI 公开资料 |
| AI 算力 | 最高 8 TOPS | TI 公开资料 |
| 接口 | PCIe、GbE、USB、CSI-2、CAN-FD | TI 公开资料 |
| 功耗 | 约 5–15 W | TI 公开资料 |
| 安全 | 工业级安全特性 | TI 公开资料 |
| 价格 | 未公开 | TI 公开资料 |

**技术亮点**：面向工业与边缘 AI 的 Jacinto 7 衍生平台，平衡算力、功耗与工业接口。

**应用场景**：工业网关、边缘 AI Box、机器人主控、智能零售。

## 供应链位置

- **上游关键零部件/材料**：台积电/自己晶圆厂、ARM IP、自研 C7x DSP/MMA、存储、PMIC、封测、PCB
- **下游客户/应用场景**：汽车 Tier1/OEM、工业自动化厂商、机器人公司、机器视觉集成商、能源与基础设施
- **主要竞争对手/对标**：NXP i.MX / S32、NVIDIA Jetson、Renesas RZ/V、Qualcomm Ride、地平线征程

## 知识图谱节点与关系

- 公司实体：`ent_company_texas_instruments`
- 产品实体：`ent_product_ti_tda4vm`、`ent_product_ti_am68a`
- 零部件实体：`ent_component_ti_tda4vm_soc`、`ent_component_ti_am68a_soc`
- 关键关系：
  - `ent_company_texas_instruments` -- `manufactures` --> `ent_product_ti_tda4vm`
  - `ent_company_texas_instruments` -- `manufactures` --> `ent_product_ti_am68a`
  - `ent_company_texas_instruments` -- `manufactures` --> `ent_component_ti_tda4vm_soc`
  - `ent_company_texas_instruments` -- `manufactures` --> `ent_component_ti_am68a_soc`
  - `ent_product_ti_tda4vm` -- `uses` --> `ent_component_ti_tda4vm_soc`
  - `ent_product_ti_am68a` -- `uses` --> `ent_component_ti_am68a_soc`

## 参考资料

1. [TI 官网](https://www.ti.com)
2. [TDA4VM 产品页](https://www.ti.com/product/TDA4VM)
3. [Jacinto 7 处理器](https://www.ti.com/processors/automotive-processors/jacino-7-family.html)