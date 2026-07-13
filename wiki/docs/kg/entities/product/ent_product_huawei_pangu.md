---
id: ent_product_huawei_pangu
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 华为盘古大模型
  en: Huawei Pangu Large Models
status: active
sources:
- id: src_ent_product_huawei_pangu_1
  type: website
  url: https://support.huawei.com/enterprise/en/doc/EDOC1100404294/f6515733/what-is-pangu-large-models
- id: src_ent_product_huawei_pangu_2
  type: website
  url: https://handwiki.org/wiki/Software:Huawei_PanGu
- id: src_ent_product_huawei_pangu_3
  type: website
  url: https://www.serverscn.com/news/-huawei-cloud-pangu-big-model-leads-the-chinese-market
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 华为盘古大模型 / Huawei Pangu Large Models

## 概述

华为盘古大模型（Huawei Pangu Large Models）是华为云推出的行业级大模型体系，覆盖自然语言处理（NLP）、计算机视觉（CV）、多模态、预测分析与科学计算五大基础方向。盘古大模型采用“5+N+X”三层架构：L0 层提供五大基础模型能力，L1 层面向政府、金融、制造、矿山、气象等行业训练行业大模型，L2 层针对具体业务场景提供可落地的场景模型服务。盘古大模型 5.0 进一步在全系列、多模态、强推理三方面升级，参数规格从十亿级到万亿级，已在超过 30 个行业、400 余个场景落地，并广泛应用于具身智能、工业设计、自动驾驶、矿山、钢铁、气象等领域。

## 工作原理 / 技术架构

盘古大模型基于华为昇腾 AI 计算平台与 CANN、MindSpore 全栈软件生态训练。模型采用 Transformer 类架构，并通过以下关键技术提升行业适配能力：

- **多模态融合**：支持文本、图像、视频、雷达、红外、遥感等多源输入，并具备可控时空生成（STCG）能力，生成符合物理规律的多模态内容。
- **强推理能力**：结合思维链（Chain-of-Thought）与策略搜索技术，提升数学推理、复杂任务规划与工具调用能力。
- **全系列参数规格**：盘古 5.0 提供 E（嵌入式，十亿级）、P（专业，百亿级）、U（超大，135B/230B）、S（超级，万亿级）四个系列，分别适配端侧、低时延推理、复杂任务基础模型与跨领域多任务场景。

模型训练与推理通过华为云 ModelArts、MindFormers 等工具链支持，并可在华为云、私有化部署及端侧运行。

## 关键参数表

| 参数项 | 典型值/范围 | 备注/来源 |
|--------|-------------|-----------|
| 模型系列 | NLP / CV / 多模态 / 预测 / 科学计算 | 华为云官方 |
| 架构 | “5+N+X” 三层（L0 基础模型 / L1 行业模型 / L2 场景模型） | 华为云官方 |
| 参数规模 | E 系列 1B；P 系列 10B；U 系列 135B / 230B；S 系列万亿级 | 公开资料 |
| 训练框架 | MindSpore / PyTorch 适配 | 华为云官方 |
| 底层算力 | 华为昇腾 Atlas / 鲲鹏计算 | 华为云官方 |
| 软件栈 | CANN、MindSpore、MindIE、ModelArts、MindFormers | 华为云官方 |
| 部署方式 | 华为云 / 私有化 / 端侧 | 华为云官方 |
| 多模态能力 | 文本、图像、视频、雷达、红外、遥感理解与生成 | 华为云官方 |
| 行业落地 | 30+ 行业、400+ 场景 | 公开报道 |
| 典型行业模型 | 盘古矿山大模型、盘古钢铁大模型、盘古高铁大模型、盘古媒体大模型、盘古具身智能模型 | 公开报道 |
| 价格 | 按调用量 / 实例计费 | 华为云官方 |

## 应用场景

- **具身智能与人形机器人**：盘古具身智能模型为机器人提供自然语言理解、任务规划、动作生成与多模态感知能力，已在搭载盘古能力的“夸父”人形机器人等案例中亮相。
- **工业制造**：工业设计、钢铁质检、矿山安全生产、设备故障预测。
- **自动驾驶**：多模态感知大模型、 Occupancy 预测、场景理解。
- **气象与科学计算**：盘古气象大模型实现全球气象要素预测。
- **金融、政务、医疗**：OCR、智能客服、文档理解、医学影像分析。

## 供应链关系

- **开发商**：华为 / Huawei Cloud（`ent_company_huawei`）。
- **底层算力支撑**：华为昇腾 AI 计算平台（`ent_product_huawei_ascend`）。
- **上游关键零部件/材料**：昇腾 AI 处理器、Atlas 服务器、存储、光模块、液冷系统、数据与算法团队。
- **下游客户/应用场景**：车企、机器人整机厂（如乐聚 Kuavo-5 搭载盘古 AI）、制造企业、矿山、金融机构、政企客户。
- **竞争/对标**：商汤日日新/SenseCore、百度文心、阿里通义、科大讯飞星火、OpenAI GPT-4V。
- **知识图谱关系**：`ent_company_huawei` — `manufactures` → `ent_product_huawei_pangu`；`ent_product_huawei_pangu` — `runs_on` → `ent_product_huawei_ascend`。

## 来源与验证

1. [Huawei Enterprise Support：What is Pangu Large Models](https://support.huawei.com/enterprise/en/doc/EDOC1100404294/f6515733/what-is-pangu-large-models)
2. [HandWiki：Huawei PanGu 5.0 Technical Specifications](https://handwiki.org/wiki/Software:Huawei_PanGu)
3. [华为云盘古大模型行业落地报道](https://www.serverscn.com/news/-huawei-cloud-pangu-big-model-leads-the-chinese-market)
4. [附录 D 企业 Wiki：华为](../../../appendices/appendix-d/companies/company_huawei.md)