---
id: ent_company_moore_threads
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 摩尔线程
  en: 摩尔线程
status: active
sources:
- id: src_moore_threads_official
  type: website
  url: https://www.moorethreads.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 摩尔线程 / 摩尔线程

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 摩尔线程 |
| **英文名** | Moore Threads |
| **总部** | 中国北京市 |
| **成立时间** | 2020 年 |
| **官网** | [https://www.moorethreads.com](https://www.moorethreads.com) |
| **供应链环节** | 全功能 GPU、AI 计算、图形渲染、国产算力、元宇宙 |
| **企业属性** | 独角兽、国产全功能 GPU 企业 |
| **母公司/所属集团** | 无（独立主体） |
| **数据来源** | 摩尔线程官网、产品发布会、公开新闻稿、行业研报 |

## 公司简介

摩尔线程致力于全功能 GPU 研发，提供图形渲染、AI 计算与视频编解码能力，构建国产 GPU 软硬件生态。

摩尔线程是中国全功能 GPU 代表企业，推出 MTT S 系列桌面与数据中心 GPU，支持 DirectX、Vulkan、OpenGL、CUDA 兼容及 AI 框架。公司强调图形与计算一体化，面向云游戏、AI 推理、数字孪生与元宇宙提供算力支持。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 桌面 GPU | 消费级/工作站图形 | MTT S80 / S70 | 游戏、设计、办公 |
| 数据中心 GPU | AI 推理与云渲染 | MTT S3000 / S4000 | 智算中心、云游戏、AIGC |
| 软件生态 | 驱动与开发工具 | MUSA / MTTensor | AI 框架、图形应用 |

## 代表产品

### 摩尔线程 MTT S80

> 摩尔线程 MTT S80：请访问 [官方资料](https://www.moorethreads.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 架构 | MUSA（Moore Threads Unified System Architecture） | 摩尔线程官网 |
| 制程 | 未公开 | - |
| 显存 | 16 GB GDDR6 | 摩尔线程官网 |
| 接口 | PCIe Gen5 | 摩尔线程官网 |
| 图形 API | DirectX、Vulkan、OpenGL | 摩尔线程官网 |
| AI 算力 | 未公开 | - |
| 视频编解码 | 支持 AV1、H.265、H.264 | 摩尔线程官网 |
| 价格 | 约 2999 RMB（参考价） | 公开报道 |

**技术亮点**：国产游戏/图形 GPU、PCIe Gen5、支持主流图形 API 与视频编解码、MUSA 软件生态。

**应用场景**：桌面游戏、图形设计、视频编辑、轻量 AI 推理。

### 摩尔线程 MTT S4000

> 摩尔线程 MTT S4000：请访问 [官方资料](https://www.moorethreads.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 架构 | MUSA | 摩尔线程官网 |
| 定位 | 数据中心全功能 GPU | 摩尔线程官网 |
| 显存 | 48 GB（公开报道） | 公开报道 |
| AI 算力 | FP32/TF32/INT8 多精度 | 摩尔线程公开资料 |
| 图形渲染 | 支持云游戏、数字孪生 | 摩尔线程官网 |
| 视频 | 多路视频编解码 | 摩尔线程公开资料 |
| 接口 | PCIe | 公开报道 |
| 价格 | 未公开 | - |

**技术亮点**：数据中心级国产 GPU、图形/AI/视频一体化、适配云游戏与 AIGC 推理场景。

**应用场景**：智算中心、云游戏、AIGC 推理、数字孪生、元宇宙。

## 供应链位置

- **上游关键零部件/材料**：晶圆代工、GDDR/HBM 存储、封测、EDA、图形/计算 IP、服务器厂商。
- **下游客户/应用场景**：游戏玩家、设计工作室、云服务商、智算中心、AIGC 企业。
- **主要竞争对手/对标**：NVIDIA GeForce/RTX、AMD Radeon、Intel Arc；国产对标壁仞、沐曦。

## 知识图谱节点与关系

- 公司实体：`ent_company_moore_threads`
- 产品实体：`ent_product_moore_threads_s80`、`ent_product_moore_threads_s4000`
- 关键关系：
  - `ent_company_moore_threads` -- `manufactures` --> `ent_product_moore_threads_s80`
  - `ent_company_moore_threads` -- `manufactures` --> `ent_product_moore_threads_s4000`
  - `ent_product_moore_threads_s80` -- `uses` --> `ent_component_gddr6_memory`
  - `ent_product_moore_threads_s4000` -- `uses` --> `ent_component_pcie_interface`

## 参考资料

1. [官网](https://www.moorethreads.com)
2. [摩尔线程官网](https://www.moorethreads.com)
3. 摩尔线程产品发布会资料