# AMD Ryzen AI（集成 XDNA NPU）

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [AMD / Advanced Micro Devices](../companies/company_amd.md) |
| **产品类别** | 端侧 AI PC / 嵌入式 AI 处理器 |
| **发布时间** | Ryzen AI 系列随锐龙处理器迭代发布 |
| **状态** | 量产/商用 |
| **官网/来源** | AMD 官网、Ryzen AI 产品页 |

## 产品概述

AMD Ryzen AI 是 AMD 在锐龙处理器中集成的专用 AI 计算引擎，基于 XDNA 架构 NPU，为 AI PC、边缘设备与机器人端侧提供高能效 AI 推理能力。

Ryzen AI 将 Zen CPU、RDNA GPU 与 XDNA NPU 整合于单一 SoC，支持 Windows AI、ONNX Runtime 及多种端侧 AI 框架。其 15–54 W 功耗区间覆盖笔记本、迷你主机、边缘盒子及机器人控制器，适合运行 VLM、语音识别、实时视觉等端侧 AI 任务。

## 产品图片

> AMD Ryzen AI：请访问 [官方资料](https://www.amd.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 处理器 | AMD Ryzen AI 300 系列 | AMD 官网 |
| 架构 | Zen 5 CPU + RDNA GPU + XDNA NPU | AMD 公开资料 |
| 制程 | 4 nm | 公开报道 |
| NPU 算力 | 最高约 55 TOPS INT8 | AMD 公开资料 |
| CPU 核心 | 最高 12 核 Zen 5 | AMD 公开资料 |
| GPU | RDNA 3.5 集成显卡 | AMD 公开资料 |
| 内存 | 支持 LPDDR5X / DDR5 | AMD 公开资料 |
| 接口 | USB4、PCIe、DP/HDMI 等 | AMD 公开资料 |
| 功耗 | 约 15–54 W | 公开报道 |
| 价格 | 视 OEM 整机而定 | - |

## 供应链位置

- **制造商**：[AMD / Advanced Micro Devices](../companies/company_amd.md)
- **核心零部件/技术来源**：台积电代工、自研 XDNA NPU、LPDDR5X/DDR5 内存、主板/PCB、散热。
- **下游应用/客户**：OEM PC 厂商、边缘设备商、工业自动化、机器人整机厂、开发者。

## 知识图谱节点与关系

- 产品实体：`ent_product_amd_ryzen_ai`
- 零部件实体：`ent_component_amd_ryzen_ai_npu`
- 制造商实体：`ent_company_amd`
- 关键关系：
  - `rel_ent_company_amd_manufactures_ent_product_amd_ryzen_ai`（`ent_company_amd` → `manufactures` --> `ent_product_amd_ryzen_ai`）
  - `rel_ent_company_amd_manufactures_ent_component_amd_ryzen_ai_npu`（`ent_company_amd` → `manufactures` --> `ent_component_amd_ryzen_ai_npu`）
  - `ent_product_amd_ryzen_ai` -- `uses` --> `ent_component_amd_ryzen_ai_npu`

## 应用场景

- **AI PC 与边缘盒子**：运行本地大模型、语音识别、实时翻译与视觉应用。
- **机器人端侧主控**：作为机器人小脑/端侧大脑，处理感知、导航与人机交互。
- **工业 HMI 与边缘网关**：提供图形渲染、AI 推理与多设备连接能力。

## 竞争对比

| 对比项 | AMD Ryzen AI | Intel Core Ultra | Qualcomm Snapdragon X |
|--------|------|------|------|
| NPU 架构 | XDNA | NPU（Meteor/Lunar Lake） | Hexagon NPU |
| 算力 | 最高 55 TOPS | 最高约 48 TOPS | 最高约 45 TOPS |
| 生态 | Windows AI / ONNX | Windows AI / ONNX | Windows on ARM |
| 集成度 | CPU+GPU+NPU | CPU+GPU+NPU | CPU+GPU+NPU |

## 选购与部署建议

- 根据功耗与形态选择 H/HS/U 系列型号，确认目标框架对 XDNA NPU 的驱动支持。
- 部署机器人方案时评估 I/O 接口、实时性与散热设计。
- 建议通过 AMD 官方渠道或 OEM 获取最新驱动、Ryzen AI SDK 与技术支持。

## 相关词条

- [制造商：AMD / Advanced Micro Devices](../companies/company_amd.md)
- [附录 D.4 重点产品 Wiki](../index-products.md)

## 参考资料

1. [AMD 官网](https://www.amd.com)
2. [AMD Ryzen AI 产品页](https://www.amd.com/en/processors/ryzen-ai)
3. AMD Ryzen AI 开发者指南