---
id: ent_product_sensetime_sensecore
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 商汤 SenseCore AI 大装置
  en: SenseTime SenseCore AI Infrastructure
status: active
sources:
- id: src_ent_product_sensetime_sensecore_1
  type: website
  url: https://www.sensetime.com/hk/technology-detail?categoryId=41144&gioNav=1
- id: src_ent_product_sensetime_sensecore_2
  type: website
  url: https://www.sensetime.com/en/news-detail/51170532?categoryId=1072
- id: src_ent_product_sensetime_sensecore_3
  type: website
  url: https://www.aibase.com/news/www.aibase.com/news/16902
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 商汤 SenseCore AI 大装置 / SenseTime SenseCore AI Infrastructure

## 概述

SenseCore 是商汤科技打造的 AI 原生基础设施（AI Native Cloud），覆盖 AI IaaS、AI PaaS 与算法模型层，旨在为大模型训练、推理及行业 AI 应用提供端到端算力、算法与数据闭环。SenseCore 以商汤上海临港 AIDC 为核心节点，并接入深圳、广州、福州、济南、重庆等多地算力资源。截至 2024 年 7 月，SenseCore 总算力达到 20,000 petaFLOPS，部署 GPU 超过 54,000 张，是中国市场份额领先的 AI 原生云平台之一。SenseCore 支撑商汤“日日新”大模型体系，并面向具身智能、AIGC、自动驾驶、科学计算等场景提供服务。

## 工作原理 / 技术架构

SenseCore 由三层架构组成：

1. **AI IaaS（计算基础设施层）**：提供异构 GPU/AI 芯片集群、存储与网络资源，支持 1 至 10,000 GPU 弹性扩展，可兼容 NVIDIA 及多款国产芯片，并完成与昇腾 384 超节点的适配。
2. **AI PaaS（深度学习平台层）**：包括 SenseParrots 训练框架、OpenMMLab 开源算法库、OpenDILab 决策智能平台、数据管理与标注工具，实现模型训练、微调、评估、压缩与部署的全链路工具支持。
3. **算法/模型层（模型工厂）**：已开发超过 49,000 个商用 AI 模型，日日新（SenseNova）大模型系列覆盖自然语言、视觉、多模态、代码与 3D 生成。

在大规模训练任务中，有效训练时长比率可衡量集群稳定性。公开测试显示，SenseCore 在 8 副本 × 8 卡异构训练任务中有效训练时长比率达到 99.46%，并具备断点续训、自动容错、拓扑感知调度等能力。

## 关键参数表

| 参数项 | 典型值/范围 | 备注/来源 |
|--------|-------------|-----------|
| 产品形态 | AI 原生云平台 / AI 大装置 | 商汤官网 |
| 核心节点 | 上海临港 AIDC | 商汤官网 |
| 扩展节点 | 深圳、广州、福州、济南、重庆等 | 公开报道 |
| 总算力 | 20,000 petaFLOPS（截至 2024 年 7 月） | 商汤公开资料 |
| GPU 数量 | 超过 54,000 张（截至 2024 年 7 月） | 商汤公开资料 |
| 临港 AIDC 峰值算力 | 3,740 petaFLOPS | 商汤 2022 公开资料 |
| 架构分层 | AI IaaS / AI PaaS / 算法模型层 | 商汤官网 |
| 训练框架 | SenseParrots、OpenMMLab、OpenDILab | 商汤官网 |
| 商用模型数量 | 超过 49,000 个 | 商汤官网 |
| 异构兼容性 | 支持 NVIDIA 及多款国产芯片；适配昇腾 384 超节点 | 公开报道 |
| 有效训练时长比 | 99.46%（8×8 异构训练测试） | 商汤新闻稿 |
| 服务形态 | 公有云 / 私有化 / 混合云 / MaaS | 商汤官网 |
| 行业认证 | 中国信通院 CAICT 5A 级原生 AI 云平台认证 | 商汤新闻稿 |
| 价格 | 按算力/服务计费 | 商汤官网 |

## 应用场景

- **具身智能与人形机器人大脑**：训练视觉-语言-动作（VLA）大模型，为机器人提供感知、理解与任务规划能力。
- **AIGC 内容生成**：文生图、文生视频、数字人、3D 内容生成。
- **自动驾驶**：感知模型训练、BEV/Occupancy 算法迭代、数据闭环。
- **科学计算（AI4S）**：蛋白质结构预测、气象预报、材料发现等。
- **智慧城市与企业服务**：城市治理、工业质检、金融风控、医疗影像。

## 供应链关系

- **开发商/运营商**：商汤科技 / SenseTime（`ent_company_sensetime`）。
- **上游关键零部件/材料**：NVIDIA/国产 AI 芯片、服务器、数据中心、高速网络、存储系统、数据标注服务。
- **下游客户/应用场景**：车企、机器人厂商、互联网平台、政企客户、金融机构、科研机构。
- **竞争/对标**：华为昇腾/盘古、阿里云通义、百度文心、科大讯飞星火、智谱 AI。
- **知识图谱关系**：`ent_company_sensetime` — `manufactures` → `ent_product_sensetime_sensecore`；`ent_product_sensetime_ruyi` — `runs_on` → `ent_product_sensetime_sensecore`。

## 来源与验证

1. [商汤 SenseCore AI 大装置官方页面](https://www.sensetime.com/hk/technology-detail?categoryId=41144&gioNav=1)
2. [SenseCore 获 CAICT 5A 级原生 AI 云平台认证](https://www.sensetime.com/en/news-detail/51170532?categoryId=1072)
3. [SenseCore 算力规模与市场份额报道](https://www.aibase.com/news/www.aibase.com/news/16902)
4. [附录 D 企业 Wiki：商汤科技](../../../appendices/appendix-d/companies/company_sensetime.md)