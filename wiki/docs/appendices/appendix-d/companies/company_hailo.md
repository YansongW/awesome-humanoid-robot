# Hailo

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | Hailo（以色列边缘 AI 芯片公司） |
| **英文名** | Hailo Technologies |
| **总部** | 以色列特拉维夫 |
| **成立时间** | 2017 年 |
| **官网** | [https://hailo.ai](https://hailo.ai) |
| **供应链环节** | 边缘 AI 处理器、端侧 NPU、机器人/汽车视觉 |
| **企业属性** | 独角兽、私有企业 |
| **母公司/所属集团** | 无（独立主体） |
| **数据来源** | Hailo 官网、产品手册、公开新闻稿、行业研报 |

## 公司简介

Hailo 是以色列领先的边缘 AI 芯片公司，专注于为边缘设备提供高性能、低功耗的神经网络处理器。

Hailo 的 Hailo-8 AI 处理器采用创新的数据流架构（Dataflow Architecture），在典型功耗下提供高 TOPS 算力，广泛应用于汽车 ADAS、智能摄像头、工业检测、机器人和无人机。其 Hailo-15 进一步集成 ISP 与 AI，面向智能相机 SoC。Hailo 提供完整 SDK 与模型优化工具，支持主流深度学习框架。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| Hailo-8 | 边缘 AI 加速器 | Hailo-8 / Hailo-8L | 机器人、汽车、安防、工业 |
| Hailo-15 | 集成 ISP 的视觉处理器 | Hailo-15 | 智能相机、AIoT |
| 开发套件 | 评估与原型 | Hailo-8 M.2 / PCIe 开发套件 | 开发者、方案商 |
| 软件栈 | 模型优化与推理 | Hailo Dataflow Compiler / TAPPAS | 全系列芯片 |

## 代表产品

### Hailo-8 AI 处理器

> Hailo-8 AI 处理器：请访问 [官方资料](https://hailo.ai) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 架构 | 数据流架构（Dataflow Architecture） | Hailo 公开资料 |
| 算力 | 最高 26 TOPS INT8 | Hailo 公开资料 |
| 能效 | 约 3 TOPS/W 典型 | Hailo 公开资料 |
| 制程 | 16 nm（公开报道） | 公开报道 |
| 接口 | PCIe Gen3 / M.2 / BGA 封装 | Hailo 公开资料 |
| 尺寸 | 约 15 mm × 15 mm（BGA） | Hailo 公开资料 |
| 功耗 | 约 2.5 W 典型 | Hailo 公开资料 |
| 价格 | 未公开 | - |

**技术亮点**：数据流架构高利用率、低功耗高算力、支持多精度量化、小尺寸易集成。

**应用场景**：机器人端侧感知、ADAS、智能摄像头、工业质检、无人机、AIoT。

### Hailo-15 视觉处理器

> Hailo-15 视觉处理器：请访问 [官方资料](https://hailo.ai) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 定位 | 集成 ISP 与 AI 的视觉处理器 | Hailo 公开资料 |
| AI 算力 | 最高 20 TOPS INT8 | Hailo 公开资料 |
| ISP | 集成高性能 ISP | Hailo 公开资料 |
| 视频 | 支持多路高分辨率视频 | Hailo 公开资料 |
| 接口 | MIPI、以太网、USB 等 | Hailo 公开资料 |
| 功耗 | 未公开 | - |
| 应用场景 | 智能相机、机器人视觉、AIoT | Hailo 公开资料 |
| 价格 | 未公开 | - |

**技术亮点**：ISP+AI 单芯片、端到端视觉处理、降低系统成本与功耗。

**应用场景**：智能安防相机、机器人导航、人脸识别、工业视觉检测。

## 供应链位置

- **上游关键零部件/材料**：晶圆代工、封测、存储器、ISP IP、PCB/模组。
- **下游客户/应用场景**：汽车 Tier1/OEM、安防厂商、工业相机公司、机器人整机厂、AIoT 设备商。
- **主要竞争对手/对标**：Intel Movidius、Qualcomm QCS、地平线征程、Ambarella、瑞萨 R-Car。

## 知识图谱节点与关系

- 公司实体：`ent_company_hailo`
- 产品实体：`ent_product_hailo_8`
- 零部件实体：`ent_component_hailo_8_npu`
- 关键关系：
  - `ent_company_hailo` -- `manufactures` --> `ent_product_hailo_8`
  - `ent_company_hailo` -- `manufactures` --> `ent_component_hailo_8_npu`
  - `ent_product_hailo_8` -- `uses` --> `ent_component_hailo_8_npu`

## 参考资料

1. [Hailo 官网](https://hailo.ai)
2. [Hailo-8 产品页](https://hailo.ai/products/hailo-8/)
3. [Hailo-15 产品页](https://hailo.ai/products/hailo-15/)