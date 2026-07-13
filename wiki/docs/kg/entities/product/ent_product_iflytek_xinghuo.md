---
id: ent_product_iflytek_xinghuo
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 科大讯飞星火认知大模型
  en: iFlytek Spark (Xinghuo) Cognitive Large Model
status: active
sources:
- id: src_iflytek_xinghuo_official
  type: website
  url: https://xinghuo.xfyun.cn/
- id: src_jademond_spark
  type: website
  url: https://www.jademond.com/glossary/iflytek-spark
- id: src_chinadaily_spark_x1
  type: website
  url: https://regional.chinadaily.com.cn/wic/2025-04/28/c_1089195.htm
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 科大讯飞星火认知大模型

## 概述

讯飞星火（iFlytek Spark，又称 Xinghuo / SparkDesk）是科大讯飞推出的 proprietary 大语言模型（LLM）系列，首发于 2023 年 5 月。该系列所有模型均基于华为昇腾（Ascend）AI 芯片与讯飞“飞星”国产算力平台进行训练，未使用 Nvidia 等受美国出口管制 GPU。截至 2026 年，旗舰版本为 Spark X2（2026 年 2 月发布），采用 Mixture-of-Experts（MoE）架构，总参数量约 $2930$ 亿，单次推理激活参数约 $300$ 亿，支持 130 余种语言，并在数学、代码、逻辑推理、医疗与法律等垂类任务上进行深度优化。讯飞星火采用“1+N”战略：一个通用基座模型加 N 个行业专用模型。

## 工作原理 / 技术架构

Spark 系列基于 Transformer / MoE 架构。MoE 模型通过门控网络（gating network）将输入 token 路由到少数专家子网络，从而在扩大模型容量的同时控制推理成本。设输入表示为 $\mathbf{x}$，门控输出为稀疏权重 $\mathbf{g} = \text{softmax}(\mathbf{W}_g \mathbf{x})$，经 Top-$k$ 选择后，模型输出为

$$
\mathbf{y} = \sum_{i \in \text{Top-}k} g_i \cdot \text{Expert}_i(\mathbf{x}).
$$

Spark X1/X2 在通用任务、深度推理、代码生成与多语言理解上进行联合训练。讯飞强调其训练全程在国产算力基础设施上完成：Spark X1 70B 基于华为 Ascend 910B；Spark X1.5/X2 基于飞星二号（Feixing-2）国产智能算力平台。由于科大讯飞自 2019 年起被列入美国实体清单，其算力供应链完全依赖华为昇腾生态。

## 关键参数表

| 参数 | Spark X1 | Spark X1.5 / X2 |
|---|---|---|
| 发布时间 | 2025 年 1 月 | 2025 年 11 月 / 2026 年 2 月 |
| 架构 | Dense Transformer | MoE（Mixture-of-Experts） |
| 总参数量 | $70\,\text{B}$ | 约 $293\,\text{B}$ |
| 激活参数量 | $70\,\text{B}$ | 约 $30\,\text{B}$ |
| 训练算力 | 华为 Ascend 910B | 飞星二号（华为 Ascend） |
| 语言支持 | 中文为主，2025 年 7 月升级至 130+ 语言 | 130+ 语言 |
| 核心能力 | 深度推理、数学、代码 | 深度推理、多语言、企业级任务 |
| 部署形态 | 消费端 App、API、政企私有化 | 消费端 App、API、政企私有化 |
| 商业模式 | API 调用、订阅、私有化部署 | API 调用、订阅、私有化部署 |

## 应用场景

讯飞星火在机器人及相关产业中的应用主要体现在“机器人大脑”与自然语言交互层：

- **人形机器人任务理解与规划**：将人类自然语言指令解析为可执行子任务序列，并与机器人动作规划系统对接。
- **多模态人机交互**：结合讯飞在语音识别与合成领域的优势，实现语音输入/输出、实时翻译与情感化对话。
- **行业垂类模型**：在教育、医疗、法律、汽车、政务、制造等领域提供专业知识问答与文档生成能力。
- **汽车智能座舱**：作为车载大模型，支撑导航、娱乐、车控与驾驶辅助的语义理解。

## 供应链关系

讯飞星火位于 AI 软件/模型层，其上游算力完全依赖华为昇腾芯片与飞星国产算力平台；中游为讯飞自研模型训练、微调与推理服务；下游通过 Spark API、讯飞开放平台及行业解决方案向机器人公司、汽车 OEM、政府机构与企业客户输出能力。在机器人产业链中，讯飞星火可作为“认知智能”模块被集成到人形机器人或具身智能系统中，与感知芯片（如地平线 Journey）、运动控制器、执行器等硬件形成软硬一体方案。

## 来源与验证

- 讯飞星火官方入口（https://xinghuo.xfyun.cn/）为面向消费者与企业用户的产品入口。
- Jademond 技术百科详细梳理了 Spark 从 V1 到 X2 的发布历程、训练硬件、参数规模、语言支持及“1+N”战略。
- China Daily 报道确认 Spark X1 完全基于华为 Ascend 芯片训练，并声称在整体基准性能上达到 OpenAI o1 与 DeepSeek R1 水平。