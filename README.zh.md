<div align="center">

# Awesome Humanoid Robot 人形机器人 🤖

**一个围绕「人形机器人从 0 到 1 量产与产业化应用」构建的 curated 多语言知识图谱。**

<p>
  <img src="https://img.shields.io/badge/status-public%20v0.1.0-success" alt="Status: public v0.1.0" />
  <img src="https://img.shields.io/badge/entries-2102-green" alt="2102 entries" />
  <img src="https://img.shields.io/badge/relationships-924-brightgreen" alt="924 relationships" />
  <img src="https://img.shields.io/badge/languages-zh%2Fen%2Fko-blue" alt="Languages: zh/en/ko" />
  <img src="https://img.shields.io/badge/validation-passing-success" alt="Validation passing" />
</p>

🌐 **在线站点**：[kg.rounds-tech.com](https://kg.rounds-tech.com)  
🌐 [English](README.md) · [简体中文](README.zh.md) · [한국어](README.ko.md)

⭐ 如果这张「地图」对你的研究或开发有帮助，欢迎点个 Star，帮助更多同行发现它。

</div>

---

## 📌 这是什么项目？

**Awesome Humanoid Robot** 是一个结构化、可持续演进的开放知识库，围绕一个核心问题展开：

> **如何实现人形机器人从 0 到 1 的量产与产业化应用？**

它追踪整条旅程中的每一个环节——从原材料、零部件、制造工艺，到设计工程、AI、软件、数据、组装测试、量产、应用场景、市场、政策与监管。我们不再满足于简单的论文列表或产品清单，而是将整个人形机器人产业建模为一张**知识图谱**：实体是节点，关系是带类型的边，每条论断都可追溯到来源。

在 **v0.1.0** 阶段，项目已从研究流水线演进为产品化的知识服务：

- 🌐 公开发布的多语言网站 **[kg.rounds-tech.com](https://kg.rounds-tech.com)**，支持搜索、交互式关系图谱与关联 Wiki。
- 📖 仓库内置 **Wiki**，源自《人形机器人：从矿山到市场》一书，提供系统化、按章节展开的叙事内容。
- 🔗 Wiki 章节与 KG 实体双向链接，读者可在叙事阅读与结构化查询之间自由切换。

项目采用 **AI 辅助、人工核验** 的方式。我们用 AI4Sci 流水线加速发现、提取与综合，但在任何内容被提升到生产环境之前，都必须经过人工审阅。

---

## ✨ v0.1.0 更新亮点

- 🌐 **产品站点上线**：[kg.rounds-tech.com](https://kg.rounds-tech.com) —— 中英韩三语界面、全文搜索、交互式 Cytoscape 图谱与关联 Wiki。
- 📖 **仓库内置 Wiki** —— 源自《人形机器人：从矿山到市场》的 30 章叙事正文 + 7 个附录，正确渲染提示框、Mermaid 图表与 KaTeX 公式。
- 🗂️ **2,102 个已校验 KG 实体**、**924 条带类型关系**，覆盖从原材料到市场应用的全栈。
- 🔄 **自动化 CI/CD** —— 每次 `main` 分支推送后，GitHub Actions 自动构建并部署到 GitHub Pages。
- 🛡️ **加固的部署流程** —— 并发控制与干净的 `gh-pages` 分支重建，避免竞态条件导致的推送失败。

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

## 🌐 产品：KG 网站

`website/` 目录构建了知识图谱的静态产品级前端。

**在线地址**：[https://kg.rounds-tech.com](https://kg.rounds-tech.com)

v0.1.0 功能：

- **三语界面** —— 独立的 `zh`、`en`、`ko` 站点，顶部可一键切换语言。
- **按领域浏览** —— 按产业领域或实体类型探索知识图谱。
- **全文搜索** —— 客户端搜索，支持类型筛选与语言感知标签。
- **交互式关系图谱** —— 基于 Cytoscape.js 的聚类视图与全图视图。
- **实体详情页** —— 摘要、领域、层级、关系、相关实体及关联 Wiki 章节。
- **集成 Wiki** —— 30 章正文 + 7 个附录，正确渲染提示框、Mermaid 图表与 KaTeX 公式。

本地构建：

```bash
cd website
pip install -r requirements.txt
python3 -m builder.build
# 启动本地服务
python3 -m http.server 8080 --directory dist
```

实验性的 FastAPI 后端（自然语言问答）位于 `web/`，详见 [`web/README.md`](web/README.md)。

---

## 🗺️ 你能在这里找到什么？

| 领域 | 追踪内容 |
|------|---------|
| **基础学科** | 支撑所有工程领域的跨学科数学、物理、化学与计算机科学概念 |
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

1. **系统性扫描** —— 工作流向 arXiv、Semantic Scholar 及网络来源发起查询，发现相关论文和产业情报。
2. **相关性分类** —— LLM 针对核心问题给每篇来源打分，过滤低相关性内容。
3. **结构化提取** —— LLM 起草带类型的条目、多语言摘要和候选关系。
4. **暂存** —— 所有 AI 草稿进入 `.staging/`，隔离等待审阅。
5. **自动审阅** —— `scripts/ai4sci_autonomous_review.py` 校验 schema、来源与重复项，自动归档高置信度草稿。
6. **人工审阅** —— 审阅者检查剩余队列，对边界情况进行拒绝或微调。
7. **集成与验证** —— 通过审核的条目进入 `research/` 与 `data/relationships/`，并必须通过 `scripts/validate_entries.py`。

运行每日入库流水线：

```bash
bash scripts/ingest_all_sources.sh
```

框架文档见 [`docs/ingestion/README.md`](docs/ingestion/README.md)；旧版 AI4Sci 流水线见 [`docs/ai4sci/literature_review_pipeline.md`](docs/ai4sci/literature_review_pipeline.md)。

---

## 🚀 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/YansongW/awesome-humanoid-robot.git
cd awesome-humanoid-robot

# 2. 校验当前知识图谱
python scripts/validate_entries.py

# 3. 构建产品网站
cd website
pip install -r requirements.txt
python3 -m builder.build
python3 -m http.server 8080 --directory dist

# 4. 运行统一入库流水线（每日 cron）
python -m ingestion.pipeline --all

# 5. 启动实验性 FastAPI 问答后端（可选）
pip install -r web/requirements.txt
export AI4SCI_API_KEY="your-openai-compatible-key"
export AI4SCI_BASE_URL="https://api.deepseek.com/v1"
uvicorn web.app:app --reload --host 127.0.0.1 --port 8000
```

凭证配置见 [`docs/ai4sci/literature_review_pipeline.md`](docs/ai4sci/literature_review_pipeline.md) 和 [`web/README.md`](web/README.md)。

---

## 📊 项目统计

| 指标 | 数量 |
|------|------|
| 生产环境实体 | 2,102 |
| 关系 | 924 |
| 本体领域 | 13（12 + `00_foundations`） |
| 实体类型 | 24 |
| Wiki 章节 | 30 |
| Wiki 附录 | 7 |
| 支持语言 | 中 / 英 / 韩 |
| 校验状态 | ✅ 通过 |

---

## 🛣️ 路线图

| 阶段 | 目标 | 状态 |
|------|------|------|
| **Phase 0** | 信息架构、schema、校验 | ✅ 完成 |
| **Phase 1** | 各领域本体文档（01–12） | ✅ 完成 |
| **Phase 2** | 工作流驱动的内容填充与 schema/关系演进 | ✅ 完成 |
| **Phase 2.5** | 产品级静态网站（搜索、图谱、Wiki） | ✅ 完成 |
| **Phase 3** | 公开发布 v0.1.0（开源 + 上线） | ✅ 完成 |
| **Phase 4** | 内容完整性：补齐缺口、深化基础学科、扩展 Wiki–KG 链接 | 🔄 进行中 |
| **Phase 5** | 审校工作流、社区贡献、v0.2.0 | ⏳ 计划中 |

完整工作流 TODO 见 [`docs/ai4sci/WORKSTREAM_TREE.md`](docs/ai4sci/WORKSTREAM_TREE.md)，最新会话记录见 [`docs/session_status.md`](docs/session_status.md)。

---

## 👥 这适合谁？

- **研究人员** —— 按问题领域和产业层级查找最新进展。
- **工程师** —— 发现与所负责子系统相关的零部件供应商、仿真工具、数据集与基准。
- **创业者 / 投资人** —— 绘制供应链地图、识别缺口、跟踪竞争对手。
- **制造与运营** —— 理解工厂设计、良率、成本驱动因素与规模化权衡。
- **政策制定者** —— 理解监管、安全与伦理格局。

---

## 🤝 贡献指南

公开贡献指南将在 Phase 5 发布。在此之前：

- 内容由核心团队借助 AI4Sci 策划。
- 如果你有访问权限，请添加带来源链接和审校状态的条目。
- 对不确定或相互矛盾的论断，请通过 issue 标记。
- 遵循 [`docs/ontology/`](docs/ontology/) 中的本体结构和 [`docs/architecture/information_model.md`](docs/architecture/information_model.md) 中的条目格式。

---

## 📂 目录结构

```
awesome-humanoid-robot/
├── README.md                          # 本文件
├── README.zh.md                       # 简体中文
├── README.ko.md                       # 한국어
├── LICENSE                            # MIT 许可证（代码）
├── docs/
│   ├── project_charter.md             # 项目范围、原则与治理
│   ├── WIKI-KG-SYNC.md                # Wiki ↔ KG 同步工作流
│   ├── ontology/                      # 产业链本体文档（01–12 + 总览）
│   ├── architecture/                  # 信息模型与预设计分析
│   └── ai4sci/                        # AI4Sci 流水线文档与工作流分类
├── research/                          # 生产环境知识库条目
│   ├── foundations/                   # 数学、物理、化学、计算机科学概念
│   ├── materials/                     # 原材料
│   ├── components/                    # 零部件与子系统
│   ├── companies/                     # 公司档案与产业生态
│   ├── papers/                        # 论文笔记
│   └── datasets/                      # 数据集笔记
├── data/
│   ├── schema/v1/                     # JSON Schema
│   ├── relationships/                 # 独立关系文件
│   └── wiki-chapter-mapping.yaml      # Wiki 章节 ↔ KG 实体映射
├── wiki/                              # 仓库内置 Wiki 源文件（Markdown + MkDocs 配置）
│   ├── docs/chapters/                 # 30 章叙事正文
│   ├── docs/appendices/               # 7 个附录
│   └── mkdocs.yml                     # MkDocs 配置
├── website/                           # 产品级静态网站构建器与资源
│   ├── builder/                       # Python 静态站点生成器
│   ├── templates/                     # Jinja2 HTML 模板
│   ├── src/                           # CSS / JS 资源
│   └── dist/                          # 生成的站点（git 忽略）
├── web/                               # 实验性 FastAPI 问答后端
│   ├── app.py
│   ├── kg_store.py
│   ├── llm_qa.py
│   └── README.md
├── scripts/                           # AI4Sci 辅助脚本
│   ├── ai4sci_lib/
│   ├── ai4sci_workstreams/
│   ├── ai4sci_paper_pipeline.py
│   ├── ai4sci_batch_pipeline.py
│   ├── ai4sci_orchestrator.py
│   ├── ai4sci_review.py
│   ├── ai4sci_status.py
│   └── validate_entries.py
└── .staging/                          # 等待人工审阅的 AI 草稿
```

---

## 📜 许可协议

- **代码**（构建器、脚本、网站前端等）：[MIT](LICENSE)
- **Wiki 内容**（`wiki/`）：[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)

---

<div align="center">

**Built with curiosity, rigor, and a belief that humanoid robotics needs a map, not just more demos.**

</div>
