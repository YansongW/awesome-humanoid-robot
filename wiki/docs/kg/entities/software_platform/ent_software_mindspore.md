---
id: ent_software_mindspore
schema_version: 1
type: software_platform
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 昇思 MindSpore
  en: MindSpore
status: active
sources:
- id: src_mindspore_official
  type: website
  url: https://www.mindspore.cn/
- id: src_mindspore_whitepaper
  type: white_paper
  url: https://mindspore-website.obs.cn-north-4.myhuaweicloud.com/white_paper/MindSpore_white_paperV1.1.pdf
- id: src_mindspore_architecture
  type: website
  url: https://www.mindspore.cn/docs/programming_guide/zh-CN/r1.3/architecture.html
- id: src_huawei_ascend
  type: website
  url: https://www.hiascend.com/
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 昇思 MindSpore

## 概述

昇思 MindSpore 是华为开源的新一代全场景 AI 框架，定位是为端、边、云提供统一的深度学习训练与推理能力。其设计目标为“易开发、高效执行、全场景覆盖”，通过源码转换（Source Code Transformation, SCT）实现自动微分，并原生适配昇腾（Ascend）AI 处理器及 CANN 异构计算架构。MindSpore 广泛应用于大模型训练、具身智能、机器人感知与决策算法等场景。

## 工作原理 / 技术架构

MindSpore 采用分层架构，核心由前端表达层、编译优化层、数据处理层和全场景运行时组成：

- **MindExpression（ME）**：基于 Python 的统一前端 API，支持面向对象与函数式编程范式，用户以常规 Python 方式构建神经网络。
- **MindCompiler**：基于端云统一的 MindIR 中间表示，完成硬件无关优化（类型推导、表达式化简、自动微分）与硬件相关优化（自动并行、内存复用、算子融合、流水线执行）。自动微分采用源码转换机制，将 Python 代码转换为 ANF 图并自动生成反向节点。
- **MindData**：负责训练数据流水线，包括加载、增强、格式转换与异构加速。
- **MindRT**：覆盖云侧、边缘侧与端侧 IoT 的运行时，实现计算图的高效调度与执行。
- **MindInsight / MindArmour**：分别提供可视化调优工具与模型安全、隐私保护能力。

框架支持 PyNative（动态图）与 Graph（静态图）两种模式，并可在两种模式间无缝切换；内置数据并行、模型并行、混合并行及自动并行策略，可用一行配置将训练任务扩展到多设备。

## 关键参数表

| 参数项 | 数值 / 说明 |
|--------|-------------|
| 框架名称 | 昇思 MindSpore |
| 当前主版本 | 2.9.0（官方文档公开版本） |
| 开源许可 | Apache 2.0 |
| 支持硬件 | Ascend、GPU、CPU、端侧 MCU |
| 编程语言 | Python 3.9–3.12，C/C++ 扩展 |
| 核心中间表示 | MindIR |
| 运行模式 | PyNative / Graph，动静统一 |
| 并行能力 | 数据并行、模型并行、混合并行、自动并行 |
| 主要工具链 | MindData、MindInsight、MindArmour |
| 适配生态 | CANN、盘古大模型、昇腾推理卡 |

## 应用场景

- **具身智能大模型训练**：在昇腾集群上训练多模态具身模型，支持机器人任务理解与动作生成。
- **机器人感知模型**：用于视觉检测、语义分割、目标跟踪等模型的训练与端侧部署。
- **工业视觉质检**：结合 In-Sight 等工业相机数据，完成缺陷检测与 OCR 模型的训练。
- **边缘推理**：基于 Atlas 200I DK 等边缘设备，将 MindSpore Lite 模型部署到机器人本体。

## 供应链关系

在公司—产品—零部件知识图谱中，MindSpore 属于**软件平台层**：

- **上游**：昇腾 AI 芯片、GPU/CPU 计算硬件、CANN 异构计算架构、操作系统与编译器。
- **自身位置**：`ent_software_mindspore` 作为通用 AI 框架，为昇腾计算平台提供模型开发与运行时支撑；图谱关系 `ent_product_huawei_ascend -- uses --> ent_software_mindspore`。
- **下游**：盘古大模型、机器人感知/决策算法、工业视觉解决方案及第三方 AI 应用。

## 来源与验证

- 昇思 MindSpore 官方首页：https://www.mindspore.cn/
- MindSpore 白皮书 V1.1：https://mindspore-website.obs.cn-north-4.myhuaweicloud.com/white_paper/MindSpore_white_paperV1.1.pdf
- MindSpore 总体架构文档：https://www.mindspore.cn/docs/programming_guide/zh-CN/r1.3/architecture.html
- 华为昇腾社区：https://www.hiascend.com/

以上资料均来自官方公开文档与白皮书，核心版本与功能以官方最新发布为准。