---
id: ent_component_cambricon_mlu370_chip
type: component
schema_version: 1
domain: 02_components
status: active
names:
  zh: 寒武纪思元 370 芯片
  en: Cambricon MLU370 Chip
sources:
- id: src_cambricon_mlu370_x8
  type: website
- title: 寒武纪开发者社区 – MLU370-X8
  url: https://developer.cambricon.com/
- id: src_cambricon_mlu370_x8_baike
  type: website
- title: 寒武纪 MLU370-X8 百度百科
  url: https://baike.baidu.com/item/%E5%AF%92%E6%AD%A6%E7%BA%AA%20MLU370-X8/60369997
- id: src_cambricon_mlu370_s4s8
  type: website
- title: 寒武纪 MLU370-S4/S8 智能加速卡技术文章
  url: https://www.ibmipc.com.cn/index.php?ac=article&at=read&did=714
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications correspond to MLU370-X8 accelerator card; single-die
    values for bare MLU370 chip are not fully disclosed by Cambricon.
---


# 寒武纪思元 370 芯片 / Cambricon MLU370 Chip

## 概述

寒武纪思元 370 芯片（Cambricon MLU370 Chip）是寒武纪科技股份有限公司推出的新一代云端/边缘 AI 处理器，基于自研 MLUarch03 架构，采用 7 nm 制程工艺。该芯片支持 FP32、FP16、BF16、INT16、INT8、INT4 等多种计算精度，可同时覆盖 AI 训练与推理任务，并通过 MLU-Link 多芯互联技术实现多卡/多芯片扩展，广泛应用于智算中心、大模型推理、视频分析与具身智能“大脑”算力平台。

## 工作原理 / 技术架构

思元 370 采用寒武纪 MLU（Machine Learning Unit）专用 AI 计算架构，核心设计包括：

1. **MLUarch03 架构**：针对神经网络计算优化的领域专用架构，支持大规模张量运算、稀疏加速与混合精度计算。
2. **片上高带宽存储**：集成 LPDDR5 内存控制器，提供高内存带宽以支撑大模型参数访问。
3. **MLU-Link 片间互联**：通过高速 SerDes 链路实现芯片间、卡间全互联，支持单机 8 卡全连接拓扑，聚合带宽达 200 GB/s（双向）。
4. **视频/图像编解码引擎**：支持 8K 视频编解码与 16384×16384 分辨率图像处理，满足多路视觉输入需求。

在训练任务中，芯片有效算力 $P_{eff}$ 与峰值算力 $P_{peak}$、内存带宽 $B$、运算强度 $I$（operations/byte）的关系可受 roofline 模型约束：

$$
P_{eff} = \min\left(P_{peak}, \; B \cdot I\right)
$$

思元 370 通过高带宽 LPDDR5 与片上缓存设计，提升内存受限型模型的实际吞吐。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制造商 | 寒武纪 / Cambricon | 官网 |
| 架构 | Cambricon MLUarch03 | 寒武纪公开资料 |
| 制程工艺 | 7 nm（TSMC） | 公开报道 |
| 峰值性能（INT8） | 256 TOPS（MLU370-X8 双芯片卡） | 寒武纪公开资料 |
| 峰值性能（INT16） | 128 TOPS（MLU370-X8） | 寒武纪公开资料 |
| 峰值性能（FP16/BF16） | 96 TFLOPS（MLU370-X8） | 寒武纪公开资料 |
| 峰值性能（FP32） | 24 TFLOPS（MLU370-X8） | 寒武纪公开资料 |
| 精度支持 | FP32 / FP16 / BF16 / INT16 / INT8 / INT4 | 寒武纪公开资料 |
| 内存类型 | LPDDR5 | 公开报道 |
| 内存容量 | 24 GB（单芯片/S4）/ 48 GB（双芯片 X8） | 公开报道 |
| 内存带宽 | 307.2 GB/s（S4）/ 614.4 GB/s（X8） | 公开报道 |
| 系统接口 | x16 PCIe Gen4 | 寒武纪公开资料 |
| MLU-Link 接口 | 4 ports，16 Lanes，50 Gbps/lane | 寒武纪公开资料 |
| MLU-Link 聚合带宽 | 200 GB/s 双向 | 寒武纪公开资料 |
| 最大热功耗 | 75 W（S4）/ 250 W（X8） | 公开报道 |
| 散热设计 | 被动散热 | 公开报道 |
| 价格 | 未公开 | - |

注：公开资料多以 MLU370-X8 加速卡（双芯片）形式给出参数。单颗裸芯片的精确 TOPS、晶体管数量、die size 等寒武纪未单独披露。

## 应用场景

- **云端大模型推理与训练**：MLU370-X8 用于智算中心与互联网数据中心的 Transformer、大语言模型推理任务。
- **具身智能“大脑”算力平台**：为人形机器人、自动驾驶车辆提供多模态感知、决策与规划的 AI 算力。
- **视频分析与智能安防**：依托高路数视频编解码能力，支持城市治理、交通监控等场景。
- **推荐系统与搜索广告**：在云计算场景中加速 CTR 预估、向量化检索等任务。

## 供应链关系

寒武纪（`ent_company_cambricon`）是中国领先的 AI 芯片设计公司，科创板上市（688256）。思元 370 芯片（`ent_component_cambricon_mlu370_chip`）是其云端智能芯片产品线的核心，通过产品实体 MLU370 加速卡（`ent_product_cambricon_mlu370`）进入市场。上游依赖晶圆代工（台积电/中芯国际）、封测、存储器、EDA/IP、PCB 与散热方案；下游客户包括互联网企业、云计算厂商、智算中心、AI 公司与机器人整机厂。寒武纪与 NVIDIA GPU、华为昇腾、百度昆仑芯、燧原科技、海光信息形成竞争。知识图谱中，寒武纪制造芯片并由 MLU370 产品使用之。

## 来源与验证

- 寒武纪开发者社区与官方产品页公开了 MLU370-S4/S8/X4/X8 等加速卡的架构、算力、内存与接口参数。
- 百度百科与行业技术文章整理了 MLU370-X8 的峰值性能、内存带宽、MLU-Link 拓扑与功耗数据。
- 寒武纪 2024 年度报告披露了其云端芯片业务收入与市场拓展情况，但未公开单芯片 die-level 细节。