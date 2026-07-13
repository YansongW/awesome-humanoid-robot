---
id: ent_product_zhipu_glm4
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 智谱 AI GLM-4 大模型
  en: Zhipu AI GLM-4 Large Language Model
status: active
sources:
- id: src_ent_product_zhipu_glm4_official
  type: website
  url: https://open.bigmodel.cn/dev/api/normal-model/glm-4
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01 00:00:00+00:00
---





# 智谱 AI GLM-4 大模型 / Zhipu AI GLM-4 Large Language Model

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [智谱 AI / Zhipu AI](../../../appendices/appendix-d/companies/company_zhipu_ai.md) |
| **产品类别** | 通用大语言模型 / 多模态大模型 |
| **发布时间** | 2024 年发布，持续迭代（GLM-4-Plus 等） |
| **状态** | 量产/商用 |
| **官网/来源** | [智谱 AI GLM-4 大模型产品/资料页](https://open.bigmodel.cn/dev/api/normal-model/glm-4) |

## 产品概述

GLM-4 是智谱 AI 推出的新一代通用大语言模型，基于自研 GLM 架构训练，具备强大的语言理解、指令遵循、长文本处理、逻辑推理与多轮对话能力。GLM-4 系列包含标准版、Plus 推理版、Long 长文本版、Flash 轻量版及 9B 开源版本，并通过 BigModel 开放平台提供 API 服务，可支撑智能客服、知识问答、代码生成与机器人 VLA 等应用。

## 产品图片

> 智谱 AI GLM-4 大模型：请访问 [官方资料](https://open.bigmodel.cn/dev/api/normal-model/glm-4) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 通用大语言模型 / 多模态大模型 | 智谱 AI 官网 |
| 架构 | GLM（General Language Model） | 智谱 AI 官网 |
| 参数量 | 未公开（百亿/千亿级） | 智谱 AI 官网 |
| 上下文长度 | 128K（标准版）/ 最高 1M（GLM-4-Long） | 智谱 AI 官网 |
| 多模态 | GLM-4V 支持图文/视频理解 | 智谱 AI 官网 |
| 推理能力 | GLM-4-Plus 支持深度推理 | 智谱 AI 官网 |
| 工具调用 | 支持 Function Call、代码解释器、联网 | 智谱 AI 官网 |
| Agent 能力 | AutoGLM 支持自主任务执行 | 智谱 AI 官网 |
| 接口 | REST API / SSE 流式 | 智谱开放平台 |
| 部署方式 | 云端 API / 私有化部署 | 智谱开放平台 |
| 开源版本 | GLM-4-9B 系列（HuggingFace/GitHub） | GitHub THUDM/GLM-4 |
| 价格 | 按量计费（API）/ 未公开（私有化） | - |

## 供应链位置

- **制造商**：[智谱 AI / Zhipu AI](../../../appendices/appendix-d/companies/company_zhipu_ai.md)
- **核心零部件/技术来源**：GPU/AI 算力集群、训练数据、RLHF 标注、推理框架
- **下游应用/客户**：企业开发者、机器人厂商、互联网公司、科研机构、垂直行业 ISV

## 知识图谱节点与关系

- 产品实体：`ent_product_zhipu_glm4`
- 零部件实体：`ent_component_zhipu_glm4_model_core`
- 制造商实体：`ent_company_zhipu_ai`
- 关键关系：
  - `rel_ent_company_zhipu_ai_manufactures_ent_product_zhipu_glm4`（`ent_company_zhipu_ai` → `manufactures` → `ent_product_zhipu_glm4`）
  - `rel_ent_company_zhipu_ai_manufactures_ent_component_zhipu_glm4_model_core`（`ent_company_zhipu_ai` → `manufactures` → `ent_component_zhipu_glm4_model_core`）
  - `ent_product_zhipu_glm4` -- `uses` --> `ent_component_zhipu_glm4_model_core`

## 应用场景

- **智能客服、知识问答、内容创作、代码生成、机器人 VLA、具身智能决策、金融/教育/能源行业解决方案**

## 竞争对比

| 对比项 | 本产品 | 主要竞品 A | 主要竞品 B |
|--------|--------|------------|------------|
| 类型 | 见规格参数表 | 同类产品 | 同类产品 |
| 核心优势 | 官方公开性能指标 | 竞品公开指标 | 竞品公开指标 |
| 生态/服务 | 制造商官方支持 | 竞品生态 | 竞品生态 |

## 选购与部署建议

- 根据目标应用的分辨率、量程、精度或算力需求选择具体型号。
- 部署前确认接口、供电、散热、机械安装与环境温度范围匹配。
- 建议通过官方渠道或授权代理商获取最新固件、SDK 与技术支持。

## 相关词条

- [制造商：智谱 AI / Zhipu AI](../../../appendices/appendix-d/companies/company_zhipu_ai.md)
- [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)

## 参考资料

1. [智谱 AI官网](https://www.zhipuai.cn)
2. [智谱 AI GLM-4 大模型产品/资料页](https://open.bigmodel.cn/dev/api/normal-model/glm-4)
3. 产品 datasheet 与公开技术报道
4. [附录 D 企业目录](../../../appendices/appendix-d/index-companies.md)