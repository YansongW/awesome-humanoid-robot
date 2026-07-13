---
id: ent_component_zhipu_glm4_model_core
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 智谱 GLM-4 大模型核心
  en: Zhipu AI GLM-4 Large Language Model Core
status: active
sources:
- id: src_zhipu_official
  type: website
- title: 智谱 AI 官网
  url: https://www.zhipuai.cn
- id: src_zhipu_glm4_api
  type: website
- title: 智谱 AI GLM-4 API 文档
  url: https://open.bigmodel.cn/dev/api/normal-model/glm-4
- id: src_zhipu_glm4_github
  type: website
- title: THUDM/GLM-4 GitHub
  url: https://github.com/THUDM/GLM-4
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Model parameter scale not publicly disclosed; missing values marked
    as 未公开.
---


# 智谱 GLM-4 大模型核心 / Zhipu AI GLM-4 Large Language Model Core

## 概述

智谱 GLM-4 大模型核心是北京智谱华章科技有限公司（Zhipu AI）基于 General Language Model（GLM）架构训练的旗舰大语言模型组件。该核心支撑 GLM-4 系列对话、推理、多模态理解（GLM-4V）、长文本处理（GLM-4-Long）与 Agent 执行（AutoGLM）能力，并通过智谱开放平台提供云端 API 与私有化部署。

## 工作原理 / 技术架构

GLM-4 基于 Transformer 架构，采用自回归空白填充（autoregressive blank infilling）的 GLM 预训练框架。模型将输入文本中的部分片段掩蔽为空白，并以自回归方式预测被掩蔽 token，统一了自然语言理解与生成任务。

在推理阶段，模型通过多头自注意力机制计算上下文表示。对于查询矩阵 $Q$、键矩阵 $K$、值矩阵 $V$，缩放点积注意力为

$$
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

其中 $d_k$ 为键向量维度。输出概率分布由最后一层线性映射与 softmax 得到：

$$
P(x_t \mid x_{<t}) = \text{softmax}(W_o h_t + b_o)
$$

$h_t$ 为第 $t$ 步隐藏状态，$W_o$、$b_o$ 为输出层参数。GLM-4 支持 Function Call、代码解释器与联网工具调用，使其可作为机器人 VLA（Vision-Language-Action）系统的“大脑”组件。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 模型架构 | GLM（General Language Model） | 智谱 AI 官网 |
| 模型类型 | 通用大语言模型 / 多模态大模型 | 智谱 AI 官网 |
| 上下文长度 | 128K（标准版）/ 最高 1M（GLM-4-Long） | 智谱 AI 官网 |
| 多模态能力 | GLM-4V 支持图文/视频理解 | 智谱 AI 官网 |
| 推理增强 | GLM-4-Plus 支持深度推理 | 智谱 AI 官网 |
| 工具调用 | 支持 Function Call、代码解释器、联网 | 智谱开放平台 |
| Agent 能力 | AutoGLM 支持自主任务执行 | 智谱 AI 官网 |
| 开源版本 | GLM-4-9B 系列 | GitHub THUDM/GLM-4 |
| 部署方式 | 云端 API / 私有化部署 | 智谱开放平台 |
| 参数量 | 未公开 | - |
| 训练数据规模 | 未公开 | - |
| 推理功耗 / 延迟 | 未公开 | - |

## 应用场景

- **机器人 VLA 决策**：作为人形机器人感知-语言-动作统一模型，解析自然语言指令并生成动作策略。
- **企业知识问答与客服**：金融、教育、能源等行业解决方案。
- **代码生成**：CodeGeeX 系列代码大模型的底层能力来源。
- **具身智能 Agent**：AutoGLM 驱动机器人在开放环境中执行多步骤任务。

## 供应链关系

- **上游**：GPU/AI 算力集群、训练数据、RLHF 标注、推理框架（如 vLLM）。
- **制造商**：`ent_company_zhipu_ai` -- `manufactures` --> `ent_component_zhipu_glm4_model_core`。
- **下游关系**：`ent_product_zhipu_glm4` -- `uses` --> `ent_component_zhipu_glm4_model_core`。
- **客户/应用**：企业开发者、机器人厂商、互联网公司、科研机构、垂直行业 ISV。
- **竞争对手/对标**：OpenAI GPT-4、Anthropic Claude、阿里巴巴通义千问、百度文心一言、字节豆包。

## 来源与验证

1. 智谱 AI 官网：https://www.zhipuai.cn
2. 智谱 AI GLM-4 API 文档：https://open.bigmodel.cn/dev/api/normal-model/glm-4
3. THUDM/GLM-4 GitHub：https://github.com/THUDM/GLM-4