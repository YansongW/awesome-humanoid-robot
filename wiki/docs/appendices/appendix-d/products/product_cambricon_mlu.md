# 寒武纪思元 370 / Cambricon MLU370

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [寒武纪 / Cambricon](../companies/company_cambricon.md) |
| **产品类别** | AI 推理/训练加速芯片与加速卡 |
| **发布时间** | 2021 年发布思元 370 系列 |
| **状态** | 量产/商用 |
| **官网/来源** | 寒武纪官网、产品手册 |

## 产品概述

寒武纪思元 370（MLU370）是寒武纪第三代云端 AI 芯片，基于自研 MLUarch03 架构，面向云端推理、训练及大模型部署提供国产算力支持。

思元 370 系列包括 MLU370-X8、MLU370-S4、MLU370-X4 等形态，覆盖 PCIe 加速卡、OAM 模组及整机方案。芯片支持 INT8/INT16/FP16/BF16 等多精度计算，集成高带宽存储与 MLU-Link 片间互联，配套 Neuware 软件栈，可运行 CV、NLP、推荐及生成式 AI 工作负载。

## 产品图片

> 寒武纪思元 370：请访问 [官方资料](https://www.cambricon.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| AI 处理器 | 思元 370（MLU370） | 寒武纪官网 |
| 架构 | 自研 MLUarch03 | 寒武纪公开资料 |
| 制程 | 7 nm | 公开报道 |
| AI 算力 | INT8 最高约 256 TOPS；FP16 约 128 TFLOPS | 寒武纪公开资料 |
| 内存 | 48 GB LPDDR4X / HBM2e（视型号） | 公开报道 |
| 内存带宽 | 未公开 | - |
| 片间互联 | MLU-Link | 寒武纪公开资料 |
| 接口 | PCIe Gen4 / OAM | 寒武纪公开资料 |
| 功耗 | 约 75–250 W（视形态） | 公开报道 |
| 软件栈 | Neuware、PyTorch/TensorFlow 适配 | 寒武纪公开资料 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[寒武纪 / Cambricon](../companies/company_cambricon.md)
- **核心零部件/技术来源**：自研 MLU 架构、晶圆代工、LPDDR/HBM 存储、封测、PCB、散热。
- **下游应用/客户**：云计算厂商、互联网企业、智算中心、AI 公司、科研院所、机器人整机厂。

## 知识图谱节点与关系

- 产品实体：`ent_product_cambricon_mlu370`
- 零部件实体：`ent_component_cambricon_mlu370_chip`
- 制造商实体：`ent_company_cambricon`
- 关键关系：
  - `rel_ent_company_cambricon_manufactures_ent_product_cambricon_mlu370`（`ent_company_cambricon` → `manufactures` → `ent_product_cambricon_mlu370`）
  - `rel_ent_company_cambricon_manufactures_ent_component_cambricon_mlu370_chip`（`ent_company_cambricon` → `manufactures` → `ent_component_cambricon_mlu370_chip`）
  - `ent_product_cambricon_mlu370` -- `uses` --> `ent_component_cambricon_mlu370_chip`

## 应用场景

- **云端大模型推理**：部署 LLM、VLM 等生成式模型，提供文本/多模态推理服务。
- **智算中心**：作为国产 AI 加速节点，支撑训练与推理混合负载。
- **机器人大脑**：为人形机器人提供云端/边缘端感知、规划与决策算力。

## 竞争对比

| 对比项 | 寒武纪思元 370 | NVIDIA A10/L4 | 华为昇腾 310/910 |
|--------|------|------|------|
| 架构 | 自研 MLU | NVIDIA Ampere/Ada | 达芬奇 |
| 生态 | Neuware + 国产框架 | CUDA + PyTorch | CANN + MindSpore |
| 国产化 | 自主可控 | 受出口管制影响 | 自主可控 |

## 选购与部署建议

- 根据模型类型与精度需求选择 X8/S4 等形态，优先确认 Neuware 对目标模型的支持。
- 部署前评估供电、散热与 PCIe 拓扑是否满足多卡互联需求。
- 建议通过寒武纪官方渠道或授权代理商获取最新固件与 SDK。

## 相关词条

- [制造商：寒武纪 / Cambricon](../companies/company_cambricon.md)
- [附录 D.4 重点产品 Wiki](../index-products.md)

## 参考资料

1. [寒武纪官网](https://www.cambricon.com)
2. [寒武纪思元 370 产品页](https://www.cambricon.com/index.php?m=content&c=index&a=lists&catid=75)
3. 寒武纪产品手册与白皮书