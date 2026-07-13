---
id: ent_company_metax
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 沐曦
  en: 沐曦
status: active
sources:
- id: src_metax_official
  type: website
  url: https://www.metax-tech.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 沐曦 / 沐曦

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 沐曦 |
| **英文名** | MetaX |
| **总部** | 中国上海市 |
| **成立时间** | 2020 年 |
| **官网** | [https://www.metax-tech.com](https://www.metax-tech.com) |
| **供应链环节** | 高性能 GPU、AI 推理/训练、数据中心、国产算力 |
| **企业属性** | 独角兽、国产高性能 GPU 企业 |
| **母公司/所属集团** | 无（独立主体） |
| **数据来源** | 沐曦官网、产品发布会、公开新闻稿、行业研报 |

## 公司简介

沐曦专注于高性能 GPU 研发，提供 AI 推理与训练、图形渲染及科学计算芯片，构建国产自主 GPU 算力生态。

沐曦是中国高性能 GPU 创新企业，产品覆盖 AI 推理、AI 训练与图形渲染三大方向。公司自研 GPU 架构与软件栈，推出曦思（推理）、曦云（训练/通用）系列产品，并面向数据中心、智算中心与边缘场景提供解决方案。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 曦思推理 GPU | AI 推理加速 | MXN 系列 | 大模型推理、推荐、CV |
| 曦云通用 GPU | AI 训练与通用计算 | MXC 系列 | 大模型训练、HPC、云游戏 |
| 软件生态 | 编译器与开发工具 | MXMACA | AI 框架适配、迁移优化 |

## 代表产品

### 沐曦高性能 GPU / 曦云 MXC 系列

> 沐曦高性能 GPU / 曦云 MXC 系列：请访问 [官方资料](https://www.metax-tech.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 架构 | 沐曦自研高性能 GPU 架构 | 沐曦公开资料 |
| 制程 | 7 nm | 公开报道 |
| 算力 | FP16/BF16 数百至千 TFLOPS 级 | 沐曦公开资料 |
| 显存 | HBM2e / GDDR6（视型号） | 公开报道 |
| 互联 | xGMI / PCIe（视型号） | 沐曦公开资料 |
| 功耗 | 未公开 | - |
| 形态 | PCIe 加速卡 / OAM 模组 | 沐曦公开资料 |
| 价格 | 未公开 | - |

**技术亮点**：国产高性能通用 GPU、统一软件栈、支持训练推理与图形渲染、适配国产服务器生态。

**应用场景**：大模型训练与推理、智算中心、云游戏、科学计算。

### 沐曦曦思 MXN 推理 GPU

> 沐曦曦思 MXN 推理 GPU：请访问 [官方资料](https://www.metax-tech.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 定位 | 数据中心 AI 推理 | 沐曦公开资料 |
| 算力 | INT8/FP16 高吞吐推理 | 沐曦公开资料 |
| 显存 | 数十 GB（视型号） | 公开报道 |
| 接口 | PCIe Gen4 | 公开报道 |
| 能效 | 未公开 | - |
| 支持模型 | CV、NLP、推荐、大模型 | 沐曦公开资料 |
| 部署 | 数据中心服务器 | 未公开 |
| 价格 | 未公开 | - |

**技术亮点**：高推理吞吐、低延迟、与训练卡统一软件生态、适配国产算力场景。

**应用场景**：大模型推理、推荐系统、视频分析、智能客服。

## 供应链位置

- **上游关键零部件/材料**：晶圆代工、HBM/GDDR 存储、封测、EDA、IP 核、服务器厂商。
- **下游客户/应用场景**：互联网与云计算大厂、智算中心、AI 企业、科研院所。
- **主要竞争对手/对标**：NVIDIA、AMD、壁仞科技、摩尔线程、海光信息、寒武纪。

## 知识图谱节点与关系

- 公司实体：`ent_company_metax`
- 产品实体：`ent_product_metax_mxc`、`ent_product_metax_mxn`
- 关键关系：
  - `ent_company_metax` -- `manufactures` --> `ent_product_metax_mxc`
  - `ent_company_metax` -- `manufactures` --> `ent_product_metax_mxn`
  - `ent_product_metax_mxc` -- `uses` --> `ent_component_hbm_memory`
  - `ent_product_metax_mxn` -- `uses` --> `ent_component_pcie_interface`

## 参考资料

1. [官网](https://www.metax-tech.com)
2. [沐曦官网](https://www.metax-tech.com)
3. 沐曦产品发布会资料