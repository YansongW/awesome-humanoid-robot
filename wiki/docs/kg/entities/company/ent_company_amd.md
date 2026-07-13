---
id: ent_company_amd
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: AMD
  en: Advanced Micro Devices
status: active
sources:
- id: src_amd_official
  type: website
  url: https://www.amd.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# AMD / Advanced Micro Devices

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | AMD（超威半导体） |
| **英文名** | Advanced Micro Devices |
| **总部** | 美国加利福尼亚州圣克拉拉 |
| **成立时间** | 1969 年 |
| **官网** | [https://www.amd.com](https://www.amd.com) |
| **供应链环节** | CPU/GPU/FPGA/AI 加速、数据中心、边缘 AI 计算 |
| **企业属性** | 上市公司（NASDAQ: AMD） |
| **母公司/所属集团** | 无（AMD 为上市主体） |
| **数据来源** | AMD 官网、Xilinx 官网、产品手册、公开新闻稿 |

## 公司简介

AMD 是全球领先的半导体设计与计算平台企业，产品覆盖 CPU、GPU、FPGA 及自适应计算，并通过收购 Xilinx 进入 AI 加速与边缘计算市场。

AMD 为机器人与具身智能提供多元算力：EPYC 服务器 CPU 用于训练与仿真；Instinct GPU 用于大模型训练/推理；Ryzen AI 处理器集成 NPU，面向端侧 AI；Xilinx Kria 与 Versal 自适应计算平台提供低延迟、可编程的 AI 推理与传感器融合能力。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| EPYC | 数据中心服务器 CPU | EPYC 9004 / 9005 系列 | 云计算、训练/推理服务器 |
| Instinct | 数据中心 AI GPU | MI300X / MI325X | 大模型训练/推理、HPC |
| Ryzen AI | 端侧 AI PC/嵌入式处理器 | Ryzen AI 300 系列 | 边缘 AI、机器人主控 |
| Xilinx Kria | 自适应边缘 AI 平台 | Kria K26 / KR260 | 机器人视觉、工业控制 |
| Xilinx Versal | 自适应计算加速平台 | Versal AI Edge 系列 | 自动驾驶、机器人感知 |

## 代表产品

### AMD Ryzen AI（NPU 集成处理器）

> AMD Ryzen AI：请访问 [官方资料](https://www.amd.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 架构 | Zen CPU + RDNA GPU + XDNA NPU | AMD 公开资料 |
| NPU 算力 | 最高约 55 TOPS INT8（Ryzen AI 300 系列） | AMD 公开资料 |
| CPU 核心 | 最高 12 核 Zen 5 | AMD 公开资料 |
| 制程 | 4 nm（公开报道） | 公开报道 |
| 内存 | 支持 LPDDR5X / DDR5 | AMD 公开资料 |
| 接口 | USB4、PCIe、显示输出等 | AMD 公开资料 |
| 功耗 | 约 15–54 W | 公开报道 |
| 价格 | 视 OEM 整机而定 | - |

**技术亮点**：CPU+GPU+NPU 三合一、XDNA 架构 NPU 高能效、支持 Windows AI 与 ONNX Runtime。

**应用场景**：AI PC、边缘 AI 盒子、机器人端侧感知与决策、工业 HMI。

### AMD Xilinx Kria K26

> AMD Xilinx Kria K26：请访问 [官方资料](https://www.amd.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 架构 | Zynq UltraScale+ MPSoC | AMD/Xilinx 公开资料 |
| AI 算力 | 约 1.4 TOPS INT8 | AMD/Xilinx 公开资料 |
| CPU | 四核 ARM Cortex-A53 + 双核 Cortex-R5 | AMD/Xilinx 公开资料 |
| 接口 | 多路 MIPI、USB、千兆以太网、GPIO | AMD/Xilinx 公开资料 |
| 功耗 | 约 5–15 W | 公开报道 |
| 形态 | SOM 模组 + 载板 | AMD/Xilinx 公开资料 |
| 价格 | 约 199 USD 起（1k） | AMD 公开报价 |

**技术亮点**：FPGA+ARM 异构、可编程逻辑、低延迟传感器接口、工业级可靠性。

**应用场景**：机器人视觉、工业检测、医疗影像、智能零售、边缘 AI。

## 供应链位置

- **上游关键零部件/材料**：台积电代工、存储器合作伙伴、封测、EDA/IP、PCB/被动元件。
- **下游客户/应用场景**：数据中心、云计算厂商、OEM/ODM、工业自动化、汽车电子、机器人整机厂、科研院所。
- **主要竞争对手/对标**：NVIDIA GPU/平台、Intel Xeon/AI PC、Qualcomm 边缘 AI、华为昇腾、地平线。

## 知识图谱节点与关系

- 公司实体：`ent_company_amd`
- 产品实体：`ent_product_amd_ryzen_ai`
- 零部件实体：`ent_component_amd_ryzen_ai_npu`
- 关键关系：
  - `ent_company_amd` -- `manufactures` --> `ent_product_amd_ryzen_ai`
  - `ent_company_amd` -- `manufactures` --> `ent_component_amd_ryzen_ai_npu`
  - `ent_product_amd_ryzen_ai` -- `uses` --> `ent_component_amd_ryzen_ai_npu`

## 参考资料

1. [AMD 官网](https://www.amd.com)
2. [AMD Ryzen AI 产品页](https://www.amd.com/en/processors/ryzen-ai)
3. [AMD Xilinx Kria 产品页](https://www.amd.com/en/products/system-on-modules/kria.html)