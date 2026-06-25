<div align="center">

# Awesome Humanoid Robot 人形机器人 🤖

**一个围绕「人形机器人从 0 到 1 量产与产业化应用」构建的 curated 知识图谱。**

<p>
  <img src="https://img.shields.io/badge/status-private%20pre--v0.1.0-blueviolet" alt="Status: private pre-v0.1.0" />
  <img src="https://img.shields.io/badge/entries-82-green" alt="82 entries" />
  <img src="https://img.shields.io/badge/relationships-58-brightgreen" alt="58 relationships" />
  <img src="https://img.shields.io/badge/workstreams-23-orange" alt="23 workstreams" />
  <img src="https://img.shields.io/badge/validation-passing-success" alt="Validation passing" />
</p>

🌐 [English](README.md) · [简体中文](README.zh.md) · [한국어](README.ko.md)

</div>

---

## 📌 这是什么项目？

**Awesome Humanoid Robot** 是一个结构化、可持续演进的开放知识库，围绕一个核心问题展开：

> **如何实现人形机器人从 0 到 1 的量产与产业化应用？**

它追踪整条旅程中的每一个环节——从原材料、零部件、制造工艺，到设计工程、AI、软件、数据、组装测试、量产、应用场景、市场、政策与监管。我们不再满足于简单的论文列表或产品清单，而是将整个人形机器人产业建模为一张**知识图谱**：实体是节点，关系是带类型的边，每条论断都可追溯到来源。

项目采用 **AI 辅助、人工核验** 的方式。我们用 AI4Sci 流水线加速发现、提取与综合，但在任何内容被提升到生产环境之前，都必须经过人工审阅。

---

## 🎯 为什么要做这个项目？

人形机器人正处于一个关键拐点。全球实验室已经能够造出能走路、能操作、能交互的机器人。但**能在演示中工作的机器人**，与**能够大规模生产、部署和维护的真实产品**，是完全不同的两件事。

这个差距不只是一个 AI 问题，而是一个**系统工程问题**，它连接着：

- 🪨 **材料科学** —— 稀土磁材、电池化学、轻质合金
- ⚙️ **精密制造** —— 机加工、绕线、铸造、装配、质控
- 🌐 **全球供应链** —— Tier-1/Tier-2 供应商、区域产业生态、成本结构
- 🧠 **AI 与软件** —— VLA、世界模型、控制、规划、sim-to-real
- 📊 **数据基础设施** —— 数据集、仿真器、基准测试、车队遥测
- 🏭 **量产制造** —— 工厂设计、良率优化、BOM 成本工程
- ⚖️ **政策与社会** —— 安全标准、认证、责任、劳动力影响

今天，关于这些层次的信息分散在学术论文、公司新闻稿、拆解报告、行业分析和技术博客中。研究者、工程师、创业者、投资人和政策制定者都缺少一张**单一、结构化、可验证的地图**来展示：各个环节如何咬合、瓶颈在哪里、哪些权衡决定了成败。

这个项目就是那张地图。

> 我们的目标不是收集每一篇论文，而是理解**从矿山到市场的完整旅程**，并让这些理解可验证、可复用、可由社区共同维护。

---

## 🗺️ 你能在这里找到什么？

| 领域 | 追踪内容 |
|------|---------|
| **原材料与关键资源** | 稀土元素、磁材、轻质金属、复合材料、半导体、电池化学 |
| **零部件与子系统** | 执行器、电机、减速器/齿轮箱、传感器、电池、计算单元、末端执行器、线缆、结构件 |
| **供应链与制造工艺** | 一级/二级供应商、制造工艺、质量控制、成本结构、区域产业生态 |
| **设计与工程** | 机械设计、运动学、动力学、人形形态、自由度、安全设计 |
| **组装、集成与测试** | 产线、校准、系统集成、测试台、验证协议 |
| **量产与规模化** | 工厂设计、产能爬坡、单位经济性、BOM 分析、良率优化 |
| **AI、模型与算法** | VLA、世界模型、 locomotion 策略、 manipulation 策略、规划、sim-to-real、SLAM、遥操作 |
| **软件与中间件** | ROS 2、实时操作系统、仿真栈、数字孪生、机群管理、数据管道 |
| **数据与数据集** | 遥操作数据、动作捕捉、仿真数据、多模态数据集、数据授权 |
| **评测与基准** | 仿真基准、真实任务、硬件在环测试、安全标准 |
| **应用与市场** | 工业制造、物流、医疗、家庭、零售、科研、国防、娱乐 |
| **公司与产业生态** | 初创公司、整机厂、零部件供应商、研究机构、融资、合作 |
| **政策、监管与伦理** | 安全标准、责任、劳动力影响、隐私、人机交互规范 |
| **基础学科** | 支撑所有工程领域的跨学科数学、物理、化学与计算机科学概念 |

---

## 🏗️ 架构优先方法

在填充任何内容之前，我们先建立了一个正式的信息模型，能够把整条产业链表示为一张图。

- **图优先**：实体是节点，关系是有向、带类型的边。
- **双标签**：每个实体同时具有**价值链层**（基础层 / 上游 / 中游 / 智能层 / 验证与市场层）和**功能角色**（材料 / 零部件 / 工艺 / 系统 / 智能 / 等）。
- **基础学科域**：跨领域的数学、物理、化学、计算机科学主题归入 `00_foundations`，可被多棵工程树共享。
- **关系作为一等公民**：跨域链接是显式的、带类型的、可验证的。
- **多语言内建**：名称、摘要和描述以语言映射形式存储（中 / 英 / 韩）。
- **版本化 schema**：条目和关系 schema 均可版本化、可扩展。
- **细粒度理论深度**：方程、算子、变量、常数、算法、近似方法都可以是显式节点。
- **YAML frontmatter + Markdown**：条目兼顾人类可读与机器可读。

详见 [`docs/architecture/information_model.md`](docs/architecture/information_model.md) 和 [`data/schema/v1/`](data/schema/v1/)。

---

## ⚙️ 工作流程：AI4Sci + 人工审阅

1. **系统性扫描** —— 工作流向 arXiv、Semantic Scholar 以及（计划中）网络来源发起查询，发现相关论文和产业情报。
2. **相关性分类** —— LLM 针对核心问题给每篇来源打分，过滤低相关性内容。
3. **结构化提取** —— LLM 起草带类型的条目、多语言摘要和候选关系。
4. **暂存** —— 所有 AI 草稿进入 `.staging/`，隔离等待审阅。
5. **人工审阅** —— 审阅者批准、编辑或拒绝每份草稿。
6. **集成与验证** —— 通过审阅的条目进入 `research/` 和 `data/relationships/`，并必须通过 `scripts/validate_entries.py`。

完整流程见 [`docs/ai4sci/literature_review_pipeline.md`](docs/ai4sci/literature_review_pipeline.md)。

---

## 🚀 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/YansongW/awesome-humanoid-robot.git
cd awesome-humanoid-robot

# 2. 激活虚拟环境
source .venv/bin/activate

# 3. 验证当前知识图谱
python scripts/validate_entries.py

# 4. 运行单个工作流（示例：VLA 调研）
python scripts/ai4sci_batch_pipeline.py \
  scripts/ai4sci_workstreams/definition/algorithm_survey/vla.yaml \
  --max-papers 5 --max-workers 2

# 5. 或并行运行多个工作流
python scripts/ai4sci_orchestrator.py --max-workers 2 --max-batch-workers 1 --max-papers 5

# 6. 审阅暂存输出
python scripts/ai4sci_review.py
```

凭证配置方式见 [`docs/ai4sci/literature_review_pipeline.md`](docs/ai4sci/literature_review_pipeline.md)。

---

## 📊 项目数据

| 指标 | 数量 |
|------|------|
| 生产级条目 | 80 |
| 关系 | 57 |
| 工作流配置 | 16 |
| 本体域 | 12 + `00_foundations` |
| 支持语言 | 中 / 英 / 韩 |
| 验证状态 | ✅ 通过 |

---

## 🛣️ 路线图

| 阶段 | 目标 | 状态 |
|------|------|------|
| **Phase 0** | 信息架构、Schema、验证机制 | ✅ 已完成 |
| **Phase 1** | 各域本体文档（01–12） | ✅ 已完成 |
| **Phase 2** | 工作流驱动的内容填充 | 🔄 进行中 |
| **Phase 3** | 内部审阅、验证流程、v0.1.0 公开发布 | ⏳ 计划中 |

完整工作流 TODO 见 [`docs/ai4sci/WORKSTREAM_TREE.md`](docs/ai4sci/WORKSTREAM_TREE.md)，最新会话记录见 [`docs/session_status.md`](docs/session_status.md)。

---

## 👥 适合谁？

- **研究者** —— 按问题域和产业层次了解人形机器人最新进展。
- **工程师** —— 发现与自身子系统相关的零部件供应商、仿真工具、数据集和基准。
- **创业者 / 投资人** —— 绘制供应链、发现缺口、跟踪竞争对手。
- **制造与运营** —— 理解工厂设计、良率、成本驱动因素和规模化权衡。
- **政策制定者** —— 理解监管、安全与伦理格局。

---

## 🤝 参与贡献

> 公开贡献指南将在 `v0.1.0` 发布。

在此之前，内容由核心团队借助 AI4Sci 整理。如果你有权访问本私有仓库，请：

- 按来源链接和验证状态添加条目。
- 标记不确定或相互冲突的论断。
- 遵循 [`docs/ontology/`](docs/ontology/) 和 [`docs/architecture/information_model.md`](docs/architecture/information_model.md) 中的条目格式与关系类型。

---

## 📂 目录结构

```
awesome-humanoid-robot/
├── README.md                          # 英文主文档
├── README.zh.md                       # 简体中文（本文件）
├── README.ko.md                       # 韩文
├── docs/
│   ├── project_charter.md             # 项目章程
│   ├── ontology/                      # 产业链本体文档（01–12 + 总览）
│   ├── architecture/                  # 信息模型与预设计分析
│   └── ai4sci/                        # AI4Sci 流水线文档与工作流谱系
├── research/                          # 生产级知识库条目
│   ├── foundations/                   # 数学、物理、化学、计算机科学概念
│   ├── materials/                     # 原材料
│   ├── components/                    # 零部件与子系统
│   ├── companies/                     # 公司画像与产业地图
│   ├── papers/                        # 论文笔记
│   └── datasets/                      # 数据集笔记
├── data/
│   ├── schema/v1/                     # JSON Schema
│   └── relationships/                 # 独立关系文件
├── scripts/                           # AI4Sci 辅助脚本
│   ├── ai4sci_lib/                    # 可复用流水线阶段
│   ├── ai4sci_workstreams/            # 工作流 YAML 配置
│   ├── ai4sci_paper_pipeline.py
│   ├── ai4sci_batch_pipeline.py
│   ├── ai4sci_orchestrator.py
│   ├── ai4sci_review.py
│   ├── ai4sci_status.py
│   └── validate_entries.py
└── .staging/                          # AI 生成的草稿，等待人工审阅
```

---

## 📜 许可

公开前确定。

---

<div align="center">

**以好奇心与严谨构建——我们相信，人形机器人需要的是一张地图，而不仅是更多演示。**

</div>
