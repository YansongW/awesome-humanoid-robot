---
id: ent_component_xpeng_turing_chip
type: component
schema_version: 1
domain: 02_components
status: active
names:
  zh: 小鹏图灵 AI 芯片
  en: XPeng Turing AI Chip
sources:
- id: src_xpeng_turing_chip_official
  type: website
- title: 小鹏图灵 AI 芯片官网
  url: https://www.xiaopeng.com/turingaichip.html
- id: src_xpeng_10th_anniversary
  type: website
- title: 小鹏 MONA M03 发布暨十周年发布会
  url: https://www.xiaopeng.com/news/company_news/5355.html
- id: src_xpeng_ai_tech_day_2024
  type: website
- title: 何小鹏：小鹏图灵 AI 芯片已跑通智驾功能
  url: https://www.36kr.com/newsflashes/3024597233706501
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
  review_notes: Specifications from official press releases and verified industry
    reports; conflicting values annotated with source.
---


# 小鹏图灵 AI 芯片 / XPeng Turing AI Chip

## 概述

小鹏图灵 AI 芯片（XPeng Turing AI Chip）是小鹏汽车全栈自研的面向 AI 大模型定制的系统级芯片，可同时应用于 AI 汽车、AI 机器人（Iron）与飞行汽车。该芯片于 2024 年 8 月 23 日完成流片，并在 2024 年 11 月的小鹏 AI 科技日上宣布已跑通最新版本智驾功能。图灵芯片采用 DSA（Domain-Specific Architecture）面向神经网络的特定领域架构，集成 40 核 CPU、2 个自研 NPU、2 个独立 ISP 以及独立安全岛，目标是在车端/机器人端本地运行高达 30B 参数的大模型。

## 工作原理 / 技术架构

图灵芯片采用异构多核架构，核心计算单元包括：

1. **40 核 CPU**：提供通用控制、任务调度与系统服务算力。
2. **双自研 NPU**：面向 Transformer、CNN 等神经网络执行张量运算，是小鹏端到端大模型与 VLA（Vision-Language-Action）模型的主要算力来源。
3. **双独立 ISP**：一颗 ISP 用于 AI 感知（行车/机器人视觉），另一颗用于用户可感知的图像合成，实现感知与可视化并行处理。
4. **独立安全岛**：满足 L4 级自动驾驶功能安全需求，实时进行全车/全机无盲点安全监测。

在机器人应用中，图灵芯片的算力可支撑多模态感知、运动规划与端到端控制。其 INT8 峰值算力 $P$ 与模型推理延迟 $T$ 的近似关系可写为

$$
T \approx \frac{O}{P \cdot \eta}
$$

其中 $O$ 为模型单次推理所需运算量（operations），$\eta$ 为实际算力利用率。小鹏宣称通过软硬一体优化，图灵芯片算力利用率可达 100%，显著降低通用芯片的冗余算力浪费。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制造商 | 小鹏机器人 / XPeng Robotics | 小鹏官方 |
| 架构 | DSA 面向神经网络的特定领域架构 | 小鹏十周年发布会 |
| CPU | 40 核处理器 | 小鹏 AI 科技日 |
| NPU | 2 个自研 NPU | 小鹏十周年发布会 |
| ISP | 2 个独立 ISP | 小鹏十周年发布会 |
| 本地大模型 | 最高 30B 参数 | 小鹏官网 / 36 氪 |
| 汽车端 INT8 算力 | 约 750 TOPS | 行业研报 / 汽车之家 |
| 机器人端算力 | 高达 3000 T | 今日头条 / 公开报道（整机或多芯片配置） |
| 制程工艺 | 7 nm（公开报道） | 知乎 / 汽车之家 |
| 功能安全 | 独立安全岛设计 | 小鹏十周年发布会 |
| 应用领域 | AI 汽车、AI 机器人（Iron）、飞行汽车 | 小鹏官网 |
| 价格 | 未公开 | 自研自用，未对外销售 |

注：关于“3000 T”的描述，公开来源存在差异。部分报道指单颗芯片机器人端算力可达 3000 T，亦有来源称 3000 T 为整车/整机多颗图灵芯片的聚合算力（如小鹏 Ultra 车型四颗芯片合计）。本卡片同时列出两种口径，并标注来源。

## 应用场景

- **小鹏 Iron 人形机器人**：图灵芯片作为机器人“大脑”，支持视觉感知、语言理解、任务规划与全身运动控制，计划 2026 年底规模量产。
- **小鹏汽车智能驾驶**：首发搭载于小鹏 G7 等车型，支持 L3 级算力需求与端到端大模型部署。
- **飞行汽车**：作为“云-软-硬-芯”全链路闭环的算力底座，支撑低空飞行器的感知与决策。

## 供应链关系

小鹏机器人（`ent_company_xpeng_robotics`）作为图灵芯片的研制与使用主体，将其同时作为零部件实体（`ent_component_xpeng_turing_chip`）与产品实体（`ent_product_xpeng_iron` 的核心计算单元）。关系网络中：

- `ent_company_xpeng_robotics` -- `manufactures` --> `ent_component_xpeng_turing_chip`
- `ent_product_xpeng_iron` -- `uses` --> `ent_component_xpeng_turing_chip`

图灵芯片由小鹏汽车供应链体系支撑晶圆代工、封装测试与存储器配套。小鹏通过自研芯片降低对英伟达 Orin/Thor 等外部智驾芯片的依赖，形成“AI 汽车 + AI 机器人 + 飞行汽车”三位一体的芯片平台战略。

## 来源与验证

- 小鹏官网（turingaichip.html）明确列出 40 核处理器、30B 大模型、双 NPU、双 ISP 等核心卖点。
- 小鹏十周年发布会新闻稿（2024-08-28）披露图灵芯片流片成功、DSA 架构、独立安全岛及多端应用定位。
- 36 氪、汽车之家、华金证券研报等第三方来源提供了 750 TOPS、7 nm 制程、3000 T 等具体数值，但部分参数存在口径差异，已分别标注。