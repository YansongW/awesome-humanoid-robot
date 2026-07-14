---
$id: ent_robot_system_figure_02
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: Figure 02
  zh: Figure 02
  ko: 피규어 02
summary:
  en: Humanoid robot developed by Figure AI for logistics and manufacturing, featuring onboard vision-language models and
    16-degree-of-freedom hands.
  zh: Figure AI 为物流和制造业开发的人形机器人，配备 onboard 视觉语言模型和 16 自由度手部。
  ko: Figure AI가 물류 및 제조업용으로 개발한 휴인oid 로봇으로, 온보드 비전-언어 모델과 16자유도 손을 갖추고 있습니다.
domains:
- 06_design_engineering
- 11_applications_markets
layers:
- midstream
- validation_markets
functional_roles:
- system
- knowledge
tags:
- figure
- figure_02
- humanoid
- robot_system
- vla
- manipulation
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/products/product_figure_02.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Figure AI Official Website
  url: https://www.figure.ai/
  date: '2026'
  accessed_at: '2026-06-24'
- id: src_002
  type: website
  title: Built In — What Is Figure AI Building?
  url: https://builtin.com/articles/figure-ai
  date: '2024'
  accessed_at: '2026-06-24'
theoretical_depth:
- system
---
## 概述
Figure 02是人形机器人领域的重要robot_system。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## Figure 02

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [Figure AI](../companies/company_figure_ai.md) |
| **产品类别** | 通用人形机器人 |
| **发布时间** | 2024 年 8 月 |
| **状态** | 企业试点/限量部署 |
| **官网/来源** | [Figure AI 官网](https://www.figure.ai) |

### 产品概述

Figure 02 是 Figure AI 推出的第二代通用人形机器人，面向工业制造与物流场景设计。整机采用哑光黑外观与集成式线缆布局，搭载 Figure 自研的 Helix VLA（Vision-Language-Action）AI 模型，能够在 200 Hz 频率下控制上半身，实现零样本抓取数千种未见过物体。

Figure 02 已在 BMW Spartanburg 等汽车制造基地进行实际任务验证，主要负责底盘装配、物料搬运等与人协作的工序。其双 NVIDIA RTX GPU 计算模块提供约 3 倍于 Figure 01 的端侧推理能力，6 颗 RGB 摄像头与多模态传感器支撑全天候环境感知。

### 产品图片

> Figure 02：请访问 [官方资料](https://www.figure.ai) 查看。

### 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 168 cm（高） | 公开规格 |
| 重量 | 约 70 kg | 公开规格 |
| 自由度（整机） | 28 DOF（手部 16 DOF/对） | 公开规格 |
| 关键性能指标 | 手部负载 25 kg；整机搬运 20 kg | 公开规格 |
| 行走速度 | 约 1.2 m/s | 公开规格 |
| 续航 | 约 5 小时 | 公开规格 |
| 电池容量 | 2.25 kWh（躯干集成） | 公开规格 |
| 计算平台 | 双 NVIDIA RTX GPU 模块 | Figure AI |
| 价格 | 未公开（行业估计约 130,000 USD） | 第三方估计 |

### 供应链位置

- **制造商**：[Figure AI](../companies/company_figure_ai.md)
- **核心零部件/技术来源**：NVIDIA GPU 计算模块、自研 Helix VLA 模型、OpenAI 语音交互、6×RGB 摄像头与深度感知模块。
- **下游应用/客户**：BMW 制造基地、物流仓储、汽车装配线。

### 知识图谱节点与关系

- 产品实体：`ent_product_figure_ai_figure_02`
- 制造商实体：`ent_company_figure_ai`
- 关键关系：
  - `rel_ent_company_figure_ai_manufactures_ent_product_figure_ai_figure_02`（`ent_company_figure_ai` → `manufactures` → `ent_product_figure_ai_figure_02`）

### 应用场景

- **汽车制造**：BMW Spartanburg 等基地执行底盘装配、线束安装与物料搬运。
- **仓储物流**：标准化箱体的分拣、搬运与产线补货。
- **工业协作**：与人类工人并肩完成需要灵巧双手的装配与检测任务。

### 竞争对比

| 对比项 | Figure 02 | Tesla Optimus Gen 3 | Agility Digit |
|--------|-----------|---------------------|---------------|
| 定位 | 工业制造人形 | 通用/工业人形 | 物流仓储人形 |
| AI 架构 | Helix VLA | FSD 衍生神经网络 | 专有感知/规划栈 |
| 续航 | 约 5 h | 约 2–4 h（估计） | 约 4 h |
| 核心优势 | 端侧 VLA、宝马部署、手部负载 | 制造规模目标、成本控制 | 物流部署成熟度 |

### 选购与部署建议

- Figure 02 当前以企业试点为主，建议直接联系 Figure AI 评估工厂场景可行性。
- 部署前需确认 Helix VLA 模型对目标工件的泛化能力，并规划训练数据收集流程。

### 参考资料

1. [Figure AI 官网](https://www.figure.ai)
2. [Robozaps – Figure 02 Review](https://blog.robozaps.com/b/figure-02-review)
3. [Humanoid.Guide – Figure 02](https://humanoid.guide/product/figure-02/)
4. [The Robot Report – Figure BMW Deployment](https://www.therobotreport.com)

## 参考
- [Figure AI Official Website](https://www.figure.ai/)
- [Built In — What Is Figure AI Building?](https://builtin.com/articles/figure-ai)
- 项目 Wiki：appendix-d/products/product_figure_02.md

