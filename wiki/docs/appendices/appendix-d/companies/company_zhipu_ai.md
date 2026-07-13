# 智谱 AI / Zhipu AI

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 智谱 AI |
| **英文名** | Zhipu AI |
| **总部** | 中国北京 |
| **成立时间** | 2019 |
| **官网** | [https://www.zhipuai.cn / https://open.bigmodel.cn](https://www.zhipuai.cn) |
| **供应链环节** | 大语言模型、多模态模型、具身智能、AI Agent |
| **企业属性** | 独角兽企业、清华系、GLM 大模型团队 |
| **母公司/所属集团** | 独立运营（北京智谱华章科技有限公司） |
| **数据来源** | 智谱 AI 官网、开放平台文档、GitHub 技术报告 |

## 公司简介

智谱 AI（Zhipu AI）由清华大学计算机系知识工程实验室技术成果转化而来，致力于打造国产自主可控的通用人工智能大模型。公司基于 GLM（General Language Model）架构推出 GLM-4 系列大模型，并拓展到视觉语言模型 GLM-4V、代码模型 CodeGeeX、视频生成 CogVideo 及具身智能 Agent 平台 AutoGLM。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| GLM 大语言模型 | 通用对话与推理 | GLM-4 / GLM-4-Plus / GLM-4-Long | 企业应用、科研 |
| 多模态模型 | 图文/视频理解生成 | GLM-4V / CogView / CogVideo | 内容创作、机器人 VLA |
| 代码与 Agent | 代码生成与自主 Agent | CodeGeeX / AutoGLM | 软件开发、具身智能 |
| 开放平台 | API 与行业解决方案 | BigModel | 金融、教育、能源、机器人 |

## 代表产品

### 智谱 AI GLM-4 大模型

> 智谱 AI GLM-4 大模型：请访问 [官方资料](https://www.zhipuai.cn) 查看。

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

**技术亮点**：国产自主 GLM 架构、长文本/多模态/深度推理、Agent 与工具调用能力、开源 9B 生态。

**应用场景**：智能客服、知识问答、内容创作、代码生成、机器人 VLA、具身智能决策、金融/教育/能源行业解决方案。

### 智谱 AI CodeGeeX 代码大模型

> 智谱 AI CodeGeeX 代码大模型：请访问 [官方资料](https://www.zhipuai.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 代码生成大模型 | 智谱 AI 官网 |
| 功能 | 代码补全、注释、修复、翻译 | 智谱 AI 官网 |
| 版本 | CodeGeeX-4 | 智谱 AI 官网 |
| 价格 | 未公开 | - |

**技术亮点**：支持多语言代码生成与智能体编程，提升软件开发效率。

**应用场景**：IDE 插件、软件工程、自动化编程。

## 供应链位置

- **上游关键零部件/材料**：GPU/AI 算力集群、训练数据、RLHF 标注、推理框架
- **下游客户/应用场景**：企业开发者、机器人厂商、互联网公司、科研机构、垂直行业 ISV
- **主要竞争对手/对标**：OpenAI GPT-4、Anthropic Claude、阿里巴巴通义千问、百度文心一言、字节豆包

## 知识图谱节点与关系

- 公司实体：`ent_company_zhipu_ai`
- 产品实体：`ent_product_zhipu_glm4`
- 零部件实体：`ent_component_zhipu_glm4_model_core`
- 关键关系：
  - `ent_company_zhipu_ai` -- `manufactures` --> `ent_product_zhipu_glm4`
  - `ent_company_zhipu_ai` -- `manufactures` --> `ent_component_zhipu_glm4_model_core`
  - `ent_product_zhipu_glm4` -- `uses` --> `ent_component_zhipu_glm4_model_core`

## 参考资料

1. [智谱 AI官网](https://www.zhipuai.cn)
2. [智谱 AI GLM-4 大模型产品/资料页](https://open.bigmodel.cn/dev/api/normal-model/glm-4)
3. 公司年报、产品 datasheet 与公开新闻稿
4. [附录 D 产品目录](../index-products.md)