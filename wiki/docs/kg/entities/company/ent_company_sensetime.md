---
id: ent_company_sensetime
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 商汤科技
  en: 商汤科技
status: active
sources:
- id: src_sensetime_official
  type: website
  url: https://www.sensetime.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 商汤科技 / 商汤科技

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 商汤科技 |
| **英文名** | SenseTime |
| **总部** | 中国香港/上海 |
| **成立时间** | 2014 年 |
| **官网** | [https://www.sensetime.com](https://www.sensetime.com) |
| **供应链环节** | 计算机视觉、多模态大模型、AI 算力、具身智能、自动驾驶 |
| **企业属性** | 上市公司（HKEX: 0020）、亚洲最大 AI 软件公司之一 |
| **母公司/所属集团** | 无（独立上市主体） |
| **数据来源** | 商汤官网、年报、公开新闻稿、行业研报 |

## 公司简介

商汤科技以计算机视觉与多模态大模型为核心，通过 SenseCore 大装置与日日新大模型，为具身智能与机器人提供感知、理解与决策能力。

商汤是中国领先的 AI 软件公司，业务涵盖智慧商业、智慧城市、智慧生活与智能汽车。SenseCore 大装置提供算力、算法与数据闭环；日日新（SenseNova）大模型体系覆盖语言、视觉、多模态与代码生成；商汤亦推出面向机器人/具身智能的感知与交互方案。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 日日新大模型 | 多模态基础模型 | SenseNova 5.0 / 5.5 | 具身智能、内容生成、智能客服 |
| SenseCore AI 大装置 | 算力与 MaaS 平台 | 临港 AIDC | 大模型训练、科研、行业 AI |
| 智能汽车与机器人 | 视觉感知与决策方案 | SenseAuto / 具身智能方案 | 自动驾驶、机器人 |

## 代表产品

### 商汤日日新 / 具身多模态模型

> 商汤日日新 / 具身多模态模型：请访问 [官方资料](https://www.sensetime.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 模型系列 | 日日新 SenseNova（语言/视觉/多模态/具身） | 商汤官网 |
| 参数规模 | 数十亿至千亿级（多规格） | 商汤公开资料 |
| 能力 | 图像理解、视频分析、自然语言交互、任务规划 | 商汤公开资料 |
| 具身能力 | 视觉语言动作（VLA）支持、环境理解、指令跟随 | 公开报道 |
| 部署 | 云端 API / 私有化 / 端侧适配 | 商汤官网 |
| 训练算力 | SenseCore 大装置 | 商汤官网 |
| 接口 | 商汤 API / 企业定制 | 商汤官网 |
| 价格 | 按调用量/私有化部署计费 | 商汤官网 |

**技术亮点**：多模态统一架构、强大的中文视觉理解、面向具身智能的动作规划与场景理解、SenseCore 训练推理一体化。

**应用场景**：人形机器人大脑、智能客服、内容生成、工业质检、自动驾驶感知。

### 商汤 SenseCore AI 大装置

> 商汤 SenseCore AI 大装置：请访问 [官方资料](https://www.sensetime.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 算力规模 | 临港 AIDC：数万张 GPU/AI 芯片 | 商汤公开资料 |
| 平台能力 | 算力、算法、数据闭环 | 商汤官网 |
| 服务形态 | MaaS、模型训练、微调、推理 | 商汤官网 |
| 模型仓库 | 日日新系列、行业大模型 | 商汤官网 |
| 能效 | 未公开 | - |
| 部署 | 公有云、私有化、混合云 | 商汤官网 |
| 客户 | 政企、汽车、金融、医疗等 | 商汤年报 |
| 价格 | 按算力/服务计费 | 商汤官网 |

**技术亮点**：全栈 AI 基础设施、支撑大模型全生命周期、为具身智能提供算力与数据闭环。

**应用场景**：大模型训练与推理、城市治理、自动驾驶、机器人智能体。

## 供应链位置

- **上游关键零部件/材料**：AI 芯片/服务器、数据中心、数据标注、开源框架、算力合作伙伴。
- **下游客户/应用场景**：车企、机器人厂商、政企客户、互联网平台、金融机构。
- **主要竞争对手/对标**：百度文心、阿里通义、华为盘古、科大讯飞星火、旷视、云从。

## 知识图谱节点与关系

- 公司实体：`ent_company_sensetime`
- 产品实体：`ent_product_sensetime_ruyi`、`ent_product_sensetime_sensecore`
- 关键关系：
  - `ent_company_sensetime` -- `manufactures` --> `ent_product_sensetime_ruyi`
  - `ent_company_sensetime` -- `manufactures` --> `ent_product_sensetime_sensecore`
  - `ent_product_sensetime_ruyi` -- `runs_on` --> `ent_product_sensetime_sensecore`
  - `ent_product_sensetime_ruyi` -- `uses` --> `ent_component_gpu_cluster`

## 参考资料

1. [官网](https://www.sensetime.com)
2. [商汤官网](https://www.sensetime.com)
3. 商汤科技 2024 年度报告