# 天数智芯天垓 200 / Iluvatar BI-V200

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [天数智芯 / Iluvatar CoreX](../companies/company_iluvatar.md) |
| **产品类别** | 通用 GPU / AI 训练推理加速卡 |
| **发布时间** | 天垓 100 后迭代至天垓 200 |
| **状态** | 量产/商用 |
| **官网/来源** | 天数智芯官网、产品手册 |

## 产品概述

天数智芯天垓 200（BI-V200）是天数智芯推出的新一代通用 GPU 加速卡，基于自研通用 GPU 架构，面向 AI 训练、推理及高性能计算提供国产算力。

天垓 200 支持 FP32/FP16/BF16/INT8 等多精度计算，配备 HBM2e 高带宽显存与 PCIe Gen4 接口，兼容主流 CUDA 应用生态。其通用 GPU 架构不仅适用于深度学习，也可支撑科学计算、图形渲染与机器人仿真训练等任务。

## 产品图片

> 天数智芯天垓 200：请访问 [官方资料](https://www.iluvatar.com.cn) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| GPU | 天垓 200（BI-V200） | 天数智芯官网 |
| 架构 | 自研通用 GPU 架构 | 天数智芯公开资料 |
| 制程 | 7 nm | 公开报道 |
| AI 算力 | FP16 / BF16 / FP32 数百 TFLOPS 级 | 天数智芯公开资料 |
| 显存 | 32 GB HBM2e（部分型号） | 公开报道 |
| 显存带宽 | 未公开 | - |
| 互联 | 支持多卡互联 | 天数智芯公开资料 |
| 接口 | PCIe Gen4 / OAM | 公开报道 |
| 功耗 | 约 300–350 W | 公开报道 |
| 软件栈 | CUDA 兼容运行时、天数智芯 SDK | 天数智芯公开资料 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[天数智芯 / Iluvatar CoreX](../companies/company_iluvatar.md)
- **核心零部件/技术来源**：自研通用 GPU 架构、晶圆代工、HBM2e 显存、封测、PCB、散热。
- **下游应用/客户**：互联网企业、云计算厂商、智算中心、AI 公司、科研院所、机器人公司。

## 知识图谱节点与关系

- 产品实体：`ent_product_iluvatar_biv200`
- 零部件实体：`ent_component_iluvatar_biv200_gpu`
- 制造商实体：`ent_company_iluvatar`
- 关键关系：
  - `rel_ent_company_iluvatar_manufactures_ent_product_iluvatar_biv200`（`ent_company_iluvatar` → `manufactures` --> `ent_product_iluvatar_biv200`）
  - `rel_ent_company_iluvatar_manufactures_ent_component_iluvatar_biv200_gpu`（`ent_company_iluvatar` → `manufactures` --> `ent_component_iluvatar_biv200_gpu`）
  - `ent_product_iluvatar_biv200` -- `uses` --> `ent_component_iluvatar_biv200_gpu`

## 应用场景

- **大模型训练与微调**：支撑百亿至千亿参数模型的分布式训练。
- **AIGC 与科学计算**：用于生成式 AI、分子模拟、CFD 等高性能计算任务。
- **机器人仿真与训练**：结合 Isaac Sim/Gazebo 等仿真平台，加速策略学习与 Sim2Real。

## 竞争对比

| 对比项 | 天垓 200 | NVIDIA A100 | 华为昇腾 910B |
|--------|------|------|------|
| 架构 | 通用 GPU | NVIDIA Ampere | 达芬奇 |
| 生态 | CUDA 兼容 | CUDA | CANN + MindSpore |
| 显存 | 32 GB HBM2e | 40/80 GB HBM | HBM2e |
| 国产化 | 自主可控 | 受出口管制影响 | 自主可控 |

## 选购与部署建议

- 迁移 CUDA 应用前需验证天数智芯兼容层的完整性与性能表现。
- 多卡训练场景需确认互联带宽、NCCL 兼容性与集群拓扑。
- 建议通过天数智芯官方渠道获取最新驱动、SDK 与技术支持。

## 相关词条

- [制造商：天数智芯 / Iluvatar CoreX](../companies/company_iluvatar.md)
- [附录 D.4 重点产品 Wiki](../index-products.md)

## 参考资料

1. [天数智芯官网](https://www.iluvatar.com.cn)
2. [天数智芯产品页](https://www.iluvatar.com.cn/product/)
3. 天数智芯产品发布会资料