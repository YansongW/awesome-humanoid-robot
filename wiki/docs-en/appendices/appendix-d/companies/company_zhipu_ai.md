# Zhipu AI

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 智谱 AI |
| **English Name** | Zhipu AI |
| **Headquarters** | Beijing, China |
| **Founded** | 2019 |
| **Official Website** | [https://www.zhipuai.cn / https://open.bigmodel.cn](https://www.zhipuai.cn) |
| **Supply Chain Segment** | Large Language Models, Multimodal Models, Embodied Intelligence, AI Agent |
| **Company Type** | Unicorn, Tsinghua-affiliated, GLM Large Model Team |
| **Parent Company/Group** | Independent (Beijing Zhipu Huazhang Technology Co., Ltd.) |
| **Data Source** | Zhipu AI official website, Open Platform documentation, GitHub technical reports |

## Company Overview

Zhipu AI, spun off from the Knowledge Engineering Lab of Tsinghua University's Department of Computer Science, is dedicated to building domestically developed, independently controllable general-purpose AI large models. Based on the GLM (General Language Model) architecture, the company has launched the GLM-4 series of large models and expanded into the visual language model GLM-4V, the code model CodeGeeX, the video generation model CogVideo, and the embodied intelligence Agent platform AutoGLM.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|-------------------------|-------------------|
| GLM Large Language Model | General conversation and reasoning | GLM-4 / GLM-4-Plus / GLM-4-Long | Enterprise applications, scientific research |
| Multimodal Model | Image-text/video understanding and generation | GLM-4V / CogView / CogVideo | Content creation, robot VLA |
| Code and Agent | Code generation and autonomous Agent | CodeGeeX / AutoGLM | Software development, embodied intelligence |
| Open Platform | API and industry solutions | BigModel | Finance, education, energy, robotics |

## Representative Products

### Zhipu AI GLM-4 Large Model

> Zhipu AI GLM-4 Large Model: Please visit [Official Documentation](https://www.zhipuai.cn) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Type | General Large Language Model / Multimodal Large Model | Zhipu AI official website |
| Architecture | GLM (General Language Model) | Zhipu AI official website |
| Parameters | Not disclosed (tens of billions/hundreds of billions) | Zhipu AI official website |
| Context Length | 128K (Standard) / Up to 1M (GLM-4-Long) | Zhipu AI official website |
| Multimodal | GLM-4V supports image-text/video understanding | Zhipu AI official website |
| Reasoning Capability | GLM-4-Plus supports deep reasoning | Zhipu AI official website |
| Tool Calling | Supports Function Call, code interpreter, internet access | Zhipu AI official website |
| Agent Capability | AutoGLM supports autonomous task execution | Zhipu AI official website |
| Interface | REST API / SSE streaming | Zhipu Open Platform |
| Deployment | Cloud API / Private deployment | Zhipu Open Platform |
| Open Source Version | GLM-4-9B series (HuggingFace/GitHub) | GitHub THUDM/GLM-4 |
| Pricing | Pay-as-you-go (API) / Not disclosed (Private) | - |

**Technical Highlights**: Domestically developed GLM architecture, long text/multimodal/deep reasoning, Agent and tool calling capabilities, open-source 9B ecosystem.

**Application Scenarios**: Intelligent customer service, knowledge Q&A, content creation, code generation, robot VLA, embodied intelligence decision-making, finance/education/energy industry solutions.

### Zhipu AI CodeGeeX Code Model

> Zhipu AI CodeGeeX Code Model: Please visit [Official Documentation](https://www.zhipuai.cn) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Type | Code Generation Large Model | Zhipu AI official website |
| Features | Code completion, comments, fixing, translation | Zhipu AI official website |
| Version | CodeGeeX-4 | Zhipu AI official website |
| Pricing | Not disclosed | - |

**Technical Highlights**: Supports multilingual code generation and agent-based programming, improving software development efficiency.

**Application Scenarios**: IDE plugins, software engineering, automated programming.

## Supply Chain Position

- **Upstream Key Components/Materials**: GPU/AI computing clusters, training data, RLHF annotation, inference frameworks
- **Downstream Customers/Application Scenarios**: Enterprise developers, robot manufacturers, internet companies, research institutions, vertical industry ISVs
- **Main Competitors/Comparables**: OpenAI GPT-4, Anthropic Claude, Alibaba Tongyi Qianwen, Baidu ERNIE Bot, ByteDance Doubao

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_zhipu_ai`
- Product Entity: `ent_product_zhipu_glm4`
- Component Entity: `ent_component_zhipu_glm4_model_core`
- Key Relationships:
  - `ent_company_zhipu_ai` -- `manufactures` --> `ent_product_zhipu_glm4`
  - `ent_company_zhipu_ai` -- `manufactures` --> `ent_component_zhipu_glm4_model_core`
  - `ent_product_zhipu_glm4` -- `uses` --> `ent_component_zhipu_glm4_model_core`

## References

1. [Zhipu AI Official Website](https://www.zhipuai.cn)
2. [Zhipu AI GLM-4 Large Model Product/Documentation Page](https://open.bigmodel.cn/dev/api/normal-model/glm-4)
3. Company annual reports, product datasheets, and public press releases
4. [Appendix D Product Catalog](../index-products.md)
