---
id: ent_company_vastai
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 瀚博半导体
  en: Vastai Technologies
status: active
sources:
- id: src_vastai_official
  type: website
  url: https://www.vastai.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 瀚博半导体 / Vastai Technologies

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 瀚博半导体 |
| **英文名** | Vastai Technologies |
| **总部** | 中国上海市浦东新区 |
| **成立时间** | 2018 年 |
| **官网** | [https://www.vastai.com](https://www.vastai.com) |
| **供应链环节** | AI 推理/视频芯片、云端/边缘 AI 计算、国产算力 |
| **企业属性** | 独角兽、国产 AI 芯片企业 |
| **母公司/所属集团** | 无（独立主体） |
| **数据来源** | 瀚博半导体官网、产品发布会、公开新闻稿、行业研报 |

## 公司简介

瀚博半导体是中国专注于人工智能与视频处理芯片设计的企业，提供云端 AI 推理与视频加速解决方案。

瀚博半导体推出 SV100 系列云端 AI 推理加速卡及 VA1 系列视频加速卡，采用自研 VPU/AI 架构，强调高吞吐、低延迟、低功耗与视频场景优化。其产品广泛应用于云计算、视频直播、智慧城市、内容审核及大模型推理等场景。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| SV100 系列 | 云端 AI 推理加速卡 | SV100 / SV200 系列 | 大模型推理、CV、视频分析 |
| VA1 系列 | 视频处理加速卡 | VA1 | 视频转码、直播、云游戏 |
| 边缘方案 | 边缘 AI 计算 | 边缘定制方案 | 边缘盒子、机器人 |
| 软件栈 | 芯片使能与开发工具 | VastStream / SDK | 全系列加速卡 |

## 代表产品

### 瀚博半导体 SV100

> 瀚博半导体 SV100：请访问 [官方资料](https://www.vastai.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 架构 | 自研 AI 推理架构 | 瀚博半导体公开资料 |
| 制程 | 7 nm（公开报道） | 公开报道 |
| 算力 | INT8 约 200 TOPS 级 | 瀚博半导体公开资料 |
| 显存 | 32 GB LPDDR4X / HBM（视型号） | 公开报道 |
| 视频能力 | 支持多路视频编解码 | 瀚博半导体公开资料 |
| 接口 | PCIe Gen4 | 公开报道 |
| 功耗 | 约 75–150 W | 公开报道 |
| 价格 | 未公开 | - |

**技术亮点**：视频+AI 融合加速、高并发视频处理、低延迟推理、支持大模型与多模态应用。

**应用场景**：云端视频分析、内容审核、直播转码、大模型推理、具身智能感知。

### 瀚博半导体 VA1

> 瀚博半导体 VA1：请访问 [官方资料](https://www.vastai.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 定位 | 视频处理加速卡 | 瀚博半导体公开资料 |
| 视频性能 | 多路 4K/8K 视频编解码 | 瀚博半导体公开资料 |
| 接口 | PCIe Gen3/Gen4 | 公开报道 |
| 功耗 | 约 25–75 W | 公开报道 |
| 应用场景 | 视频云、直播、云游戏、安防 | 瀚博半导体公开资料 |
| 软件栈 | VastStream | 瀚博半导体公开资料 |
| 价格 | 未公开 | - |

**技术亮点**：高密度视频转码、低功耗、与 AI 卡协同构建视频理解方案。

**应用场景**：视频云、直播平台、云游戏、智慧安防、机器人视觉回传。

## 供应链位置

- **上游关键零部件/材料**：晶圆代工、存储器、封测、EDA/IP、PCB、散热。
- **下游客户/应用场景**：互联网视频平台、云计算厂商、电信运营商、智慧城市、机器人公司。
- **主要竞争对手/对标**：NVIDIA T4/L4、寒武纪、燧原科技、地平线、Intel Flex。

## 知识图谱节点与关系

- 公司实体：`ent_company_vastai`
- 产品实体：`ent_product_vastai_sv100`
- 零部件实体：`ent_component_vastai_sv100_accelerator`
- 关键关系：
  - `ent_company_vastai` -- `manufactures` --> `ent_product_vastai_sv100`
  - `ent_company_vastai` -- `manufactures` --> `ent_component_vastai_sv100_accelerator`
  - `ent_product_vastai_sv100` -- `uses` --> `ent_component_vastai_sv100_accelerator`

## 参考资料

1. [瀚博半导体官网](https://www.vastai.com)
2. [瀚博半导体产品页](https://www.vastai.com/products.html)
3. 瀚博半导体产品发布会资料