---
id: ent_product_scale_physical_ai
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: Scale Physical AI
  en: Scale Physical AI
status: active
sources:
- id: src_scale_physical_ai_blog
  type: website
  url: https://scale.com/blog/physical-ai
- id: src_ur_scale_ai
  type: website
  url: https://www.universal-robots.com/news-and-media/news-center/universal-robots-scale-ai-launch-imitation-learning-system-accelerate-ai-training-lab-to-factory/
- id: src_xmaquina_scale
  type: website
  url: https://www.xmaquina.io/blog/scale-ai-is-becoming-the-data-backbone-of-physical-ai
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# Scale Physical AI / Scale Physical AI

## 概述

Scale Physical AI 是 Scale AI 面向具身智能（embodied AI）与机器人领域推出的数据引擎服务。它通过在全球范围采集真实世界的第一视角（POV）人类操作演示视频，结合多模态标注、动作分段、力反馈与语言指令对齐，帮助机器人公司与基础模型实验室构建用于训练视觉-语言-动作（VLA）模型与世界模型的大规模高质量数据集。与文本或图像数据不同，机器人操作数据无法从互联网抓取，必须依赖真实物理交互逐条采集，这正是 Scale Physical AI 的核心价值。

## 工作原理 / 技术架构

Scale Physical AI 的数据流水线包括：

- **真实世界数据采集**：通过穿戴式设备或部署在生产现场的机器人，采集第一视角操作视频、关节轨迹、力/扭矩信号与视觉上下文。
- **多模态标注**：对动作边界、物体交互、抓取类型、接触力、语言指令进行结构化标注，形成动作-语言-视觉对齐数据。
- **数据飞轮**：将采集到的演示数据反馈给 VLA 模型训练，模型部署后在真实机器人上继续产生新数据，形成持续迭代闭环。
- **合成数据补充**：与 NVIDIA Isaac Sim 等仿真平台配合，扩展长尾场景与危险/昂贵场景的覆盖。

在模仿学习框架下，策略模型 \(\pi\) 的目标是最小化预测动作与专家演示动作之间的差异：
\[
\mathcal{L} = \mathbb{E}_{(o,a) \sim \mathcal{D}} \left[ \|\pi(o) - a\|^2 \right]
\]
其中 \(o\) 为观测（图像/语言/本体感觉），\(a\) 为专家动作，\(\mathcal{D}\) 为 Scale Physical AI 构建的演示数据集。

## 关键参数表

| 参数项 | 说明 |
|---|---|
| 数据类型 | 第一视角（POV）操作演示视频 |
| 采集方式 | 全球承包商穿戴设备采集 / 生产现场机器人采集 |
| 任务场景 | 家务、装配、搬运、工具使用 |
| 标注内容 | 动作分段、物体交互、力反馈、语言指令 |
| 目标模型 | 人形机器人 / 具身智能 VLA 模型、世界模型 |
| 已积累工时 | 超过 100,000 生产小时（旧金山原型实验室 + 全球贡献者） |
| 合作伙伴 | Universal Robots、Physical Intelligence、Generalist AI、Cobot 等 |
| 价格模式 | 企业定制 / 官方询价 |

## 应用场景

- **人形机器人家务操作训练**：抓取、摆放、清洁、烹饪等长程任务演示数据。
- **工业装配技能学习**：从人类演示中学习插拔、拧紧、分拣、包装等技能。
- **服务机器人交互策略**：基于语言指令与视觉观察生成多轮交互行为。
- **机器人基础模型数据供给**：为跨本体、跨任务的通用 VLA 模型提供训练燃料。

## 供应链关系

- **上游**：AWS/Google Cloud/Azure 云基础设施、全球众包与专家标注网络、AI 预标注模型、穿戴式采集设备、机器人本体（如 UR cobots）。
- **开发商**：Scale AI（美国旧金山，2016 年成立）。
- **下游客户**：人形机器人公司、具身智能初创企业、自动驾驶公司、基础模型实验室、工业机器人厂商。
- **竞争对标**：Tesla 自有标注团队、Covariant 数据飞轮、NVIDIA Physical AI Data Factory、Claru 等机器人专用数据服务商。
- **图谱位置**：`ent_company_scale_ai` → `manufactures` → `ent_product_scale_physical_ai`；与 `ent_product_scale_data_engine` 共同构成 Scale AI 数据产品矩阵。

## 来源与验证

- Scale Physical AI 的产品定位、数据类型与已积累工时来自 Scale AI 官方博客。
- 与 Universal Robots 合作推出的 UR AI Trainer 来自 UR 官方新闻稿。
- 行业定位与分析参考 xMaquina 公开文章。