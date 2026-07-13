# 登临科技 Goldwasser X / Denglai Goldwasser X

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [登临科技 / Denglai Technology](../companies/company_denglai.md) |
| **产品类别** | 通用 GPU+ AI 训练/推理加速卡 |
| **发布时间** | Goldwasser 系列持续迭代 |
| **状态** | 量产/商用 |
| **官网/来源** | 登临科技官网、产品手册 |

## 产品概述

登临科技 Goldwasser X 是基于自研 GPU+ 创新架构的云端 AI 加速卡，融合 GPGPU 通用计算与 AI 专用加速能力，面向大模型推理、训练及通用计算提供高能效国产算力。

Goldwasser X 采用登临科技 GPU+ 架构，在统一芯片上集成通用计算单元与张量加速单元，兼顾 CUDA 兼容性与 AI 任务效率。产品支持多精度推理、多卡互联与主流框架适配，适用于智算中心、互联网及 AI 企业等场景。

## 产品图片

> 登临科技 Goldwasser X：请访问 [官方资料](https://www.denglai.com.cn) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 加速器 | Goldwasser X 系列 | 登临科技官网 |
| 架构 | GPU+（GPGPU + AI 加速） | 登临科技公开资料 |
| 制程 | 7 nm | 公开报道 |
| AI 算力 | INT8 / FP16 数百 TOPS 级 | 登临科技公开资料 |
| 显存 | 32 GB HBM2e（部分型号） | 公开报道 |
| 显存带宽 | 未公开 | - |
| 互联 | 支持多卡互联 | 登临科技公开资料 |
| 接口 | PCIe Gen4 / OAM | 公开报道 |
| 功耗 | 约 150–300 W（视型号） | 公开报道 |
| 软件栈 | CUDA 兼容运行时、登临 SDK | 登临科技公开资料 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[登临科技 / Denglai Technology](../companies/company_denglai.md)
- **核心零部件/技术来源**：自研 GPU+ 架构、晶圆代工、HBM2e 显存、封测、PCB、散热。
- **下游应用/客户**：互联网企业、云计算厂商、智算中心、AI 公司、机器人公司、科研院所。

## 知识图谱节点与关系

- 产品实体：`ent_product_denglai_goldwasser_x`
- 零部件实体：`ent_component_denglai_goldwasser_x_accelerator`
- 制造商实体：`ent_company_denglai`
- 关键关系：
  - `rel_ent_company_denglai_manufactures_ent_product_denglai_goldwasser_x`（`ent_company_denglai` → `manufactures` --> `ent_product_denglai_goldwasser_x`）
  - `rel_ent_company_denglai_manufactures_ent_component_denglai_goldwasser_x_accelerator`（`ent_company_denglai` → `manufactures` --> `ent_component_denglai_goldwasser_x_accelerator`）
  - `ent_product_denglai_goldwasser_x` -- `uses` --> `ent_component_denglai_goldwasser_x_accelerator`

## 应用场景

- **大模型推理与部署**：支持 LLM、VLM 等生成式模型的高吞吐推理。
- **云端 AI 训练**：用于中小规模模型训练与微调任务。
- **机器人云端大脑**：为人形机器人提供远程感知、规划与模型服务算力。

## 竞争对比

| 对比项 | Goldwasser X | 寒武纪 MLU370 | NVIDIA T4/L4 |
|--------|------|------|------|
| 架构 | GPU+ 融合 | 自研 MLU | NVIDIA Tensor Core |
| 生态 | CUDA 兼容 | Neuware | CUDA |
| 定位 | 训练/推理兼顾 | 推理/训练 | 推理为主 |
| 国产化 | 自主可控 | 自主可控 | 受出口管制影响 |

## 选购与部署建议

- 根据工作负载选择 X/L/S 等子型号，关注 CUDA 兼容层对目标算子的支持。
- 多卡部署时确认互联方案、驱动版本与集群调度工具。
- 建议通过登临科技官方渠道获取最新固件、SDK 与技术支持。

## 相关词条

- [制造商：登临科技 / Denglai Technology](../companies/company_denglai.md)
- [附录 D.4 重点产品 Wiki](../index-products.md)

## 参考资料

1. [登临科技官网](https://www.denglai.com.cn)
2. [登临科技产品页](https://www.denglai.com.cn/product/)
3. 登临科技产品发布会资料