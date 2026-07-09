# 专著目录 ↔ 知识图谱同步工作流

> 本文件定义《人形机器人：从矿山到市场的知识图谱》（monograph 项目）与 `awesome-humanoid-robot` 知识图谱（KG）之间的内容迁移与双向维护流程。
>
> 设计原则：**专著是 KG 的系统性整理与叙事化表达；KG 是专著的结构化数据底层。** 二者同属于一个主项目生态，KG 网站（kg.rounds-tech.com）是读者进入该生态的可视化入口。

---

## 1. 项目定位

```
专著项目 (awesome-humanoid-robot-monograph)
    │ 系统性整理、章节叙事、学术表达
    ▼
知识图谱 (awesome-humanoid-robot)
    │ 实体、关系、来源、跨层链路
    ▼
KG 网站 (kg.rounds-tech.com)
       可视化入口、搜索、关系图谱浏览
```

- **专著**：按“总论 → 物理基础层 → 设计工程层 → 制造量产层 → 控制运动层 → AI 数据层 → 软件仿真层 → 评测基准 → 整机企业与市场 → 政策伦理与未来”展开，面向系统性阅读。
- **KG**：按 `entity` + `relationship` 组织，支持从概念/公式向下拆解到数学原理、推导方法等基础学科知识，面向查询、分析与证据链验证。
- **网站**：默认以**领域聚类视图**呈现 KG，降低 2000+ 节点一次性渲染的卡顿；点击聚类可展开该领域子图，并提供“全图视图”入口（带性能提示）。

---

## 2. 内容迁移方向

### 2.1 专著 → KG（主要方向）

专著每一章的“知识图谱锚点”需要沉淀为 KG 中的实体与关系：

| 专著元素 | KG 产物 | 说明 |
|---------|--------|------|
| 章节核心概念 | `concept` / `principle` / `formalism` 实体 | 如“零力矩点 (ZMP)”、“浮动基动力学” |
| 数学公式/推导 | `equation` / `formalism` 实体 | 如“欧拉-拉格朗日方程”、“QP 标准型” |
| 方法/算法 | `method` / `algorithm` 实体 | 如“MPC 步态优化”、“Diffusion Policy” |
| 系统/零部件 | `component` / `robot_system` 实体 | 如“谐波减速器”、“Tesla Optimus” |
| 数据/基准 | `dataset` / `benchmark` 实体 | 如“Open X-Embodiment”、“HumanoidBench” |
| 引用来源 | `sources` 字段 | 论文、标准、产品页、报告链接 |
| 跨层链路 | `relationship` 文件 | 如 `requires` / `is_part_of` / `implemented_on` |

### 2.2 KG → 专著（反向校验）

- KG 中的实体 `monograph_chapters` 字段反向标注所属专著章节，实现点击即跳转到对应章节草稿。
- KG 中的 `verification` 字段（`verified` / `pending` / `draft`）作为专著内容可信度的技术依据。

---

## 3. 实体内容规范

新增或补充实体时，Markdown 文件 frontmatter 必须包含以下字段：

```yaml
---
$id: ent_<unique_id>
type: principle   # concept / principle / formalism / equation / method / algorithm / component / ...
names:
  zh: 零力矩点
  en: Zero Moment Point
  ko: 영점(ZMP)
summary:
  zh: 衡量双足机器人动态平衡的关键指标，定义为地面反作用力合力矩水平分量为零的点。
domains:
  - 06_design_engineering
  - 07_ai_models_algorithms
layers:
  - principle
tags:
  - balance
  - locomotion
  - dynamics
verification: pending   # verified / pending / draft
sources:
  - url: https://example.com/paper
    title: "Vukobratović et al. (2004) — ZMP: Forty Years of its Life"
monograph_chapters:
  - number: 8
    title: 第 8 章 人形机器人设计原理
  - number: 15
    title: 第 15 章 运动生成与 Locomotion
---

正文（可选）：补充定义、公式、推导思路、与上下游概念的关系。
```

### 3.1 `verification` 状态约定

- `verified`：已有权威来源、人工审校通过。
- `pending`：已有来源但尚未人工复核。
- `draft`：仅作为占位或从专著目录初步抽取，待补充来源。

### 3.2 跨层链路原则

每个上层概念应尽量向下拆解到基础学科知识：

```textnrobot_system
  └─ technology / method
       └─ formalism / algorithm
            └─ principle
                 └─ equation / foundation
```

例如：

```text
MPC 步态优化
  ├─ requires → 浮动基动力学
  │     └─ based_on → 欧拉-拉格朗日方程
  │           └─ requires → 经典力学
  ├─ solves → QP 标准型
  │     └─ requires → 凸优化
  │           └─ based_on → KKT 条件
  └─ implemented_on → 人形机器人整机
```

---

## 4. 工作流步骤

### Step 1：从专著目录提取锚点

1. 打开 `awesome-humanoid-robot-monograph/专著目录原始稿.md`。
2. 定位每章末尾的“**本章知识图谱锚点**”。
3. 将列出的实体类型、核心关系、关键链路复制到 `data/monograph-chapter-mapping.yaml` 中对应章节。

### Step 2：核对已有实体

1. 在 `research/` 目录下按 `type` 和 `domains` 搜索是否已有对应实体。
2. 若已存在：
   - 补充 `monograph_chapters` 字段。
   - 补充 `sources` 和 `verification` 字段。
   - 检查摘要是否覆盖专著中的定义要点。
3. 若不存在：
   - 在 `research/<type>/` 下新建 Markdown 文件。
   - 按第 3 节规范填写 frontmatter。
   - 编写一段不超过 200 字的摘要，确保学术严谨。

### Step 3：建立跨层关系

1. 在 `data/relationships/` 下新建关系文件，命名规范：
   `rel_<source_id>_<relation_type>_<target_id>.md`
2. 关系 frontmatter 示例：

```yaml
---
$id: rel_ent_method_mpc_locomotion_requires_ent_formalism_floating_base_dynamics
type: requires
source:
  id: ent_method_mpc_locomotion
target:
  id: ent_formalism_floating_base_dynamics
description:
  zh: 模型预测控制步态优化需要以浮动基动力学作为系统模型。
---
```

### Step 4：构建与审校

1. 运行 `python3 -m website.builder.build` 生成网站。
2. 检查：
   - 新增实体是否出现在搜索索引中。
   - 新增关系是否正确渲染在实体页“关系”区域。
   - 专著章节链接是否能正确跳转。
3. 对 `verification: pending` 的实体，安排人工复核后改为 `verified`。

### Step 5：反向更新专著

当 KG 中某个领域实体密度足够、关系链路清晰后，将关键发现写回专著对应章节，形成“锚点 → 实体 → 关系 → 叙事”的闭环。

---

## 5. 优先填充领域

按用户反馈与专著目录，优先补充以下领域的基础节点与跨层关系：

| 优先级 | 专著章节 | 领域 | 关键缺口示例 |
|-------|---------|------|-------------|
| P0 | 第 4 章 | `02_components` | 谐波减速器、RV 减速器、行星滚柱丝杠、FOC、电流/速度/位置环 |
| P0 | 第 8 章 | `06_design_engineering` | ZMP、COM、正/逆运动学、浮动基动力学、URDF/MJCF/SDFormat |
| P0 | 第 14 章 | `07_ai_models_algorithms` | PID、阻抗/导纳控制、全身控制、QP 框架、MPC |
| P1 | 第 15 章 | `07_ai_models_algorithms` | 步态规划、捕获点、直接配点法、shooting method、PPO/SAC、sim-to-real |
| P1 | 第 16 章 | `07_ai_models_algorithms` | 力闭合/形闭合、运动规划、MoveIt、OMPL、灵巧操作 |
| P1 | 第 18–19 章 | `07_ai_models_algorithms` / `09_data_datasets` | 行为克隆、Diffusion Policy、ACT、RT-2、OpenVLA、Open X-Embodiment |

---

## 6. 当前已映射的示例实体

部分实体已经存在并可通过 `monograph_chapters` 字段关联，例如：

- `ent_active_set_method`（Active Set Method）→ 第 14 章（QP 求解）
- `ent_foundation_convex_optimization` → 第 14 章、第 2 章
- `ent_formalism_inverse_dynamics_qp` → 第 14 章（全身控制）
- `ent_human_level_actuation_score` → 第 4 章、第 25 章
- `ent_method_hierarchical_qp_wbc` → 第 14 章

这些实体需要从本工作流角度补充 `monograph_chapters`、`verification` 与 `sources` 字段。

---

## 7. 质量门控

新增或修改实体/关系前，请自检：

- [ ] 是否至少有一个可信来源（论文 DOI、官方文档、标准号、权威报告）？
- [ ] `verification` 字段是否真实反映审校状态？
- [ ] 是否建立了至少一条向上的“属于/应用于”关系或向下的“依赖/基于”关系？
- [ ] 摘要是否避免空话，包含可验证的技术要点？
- [ ] 多语言名称是否至少包含中英文？

---

## 8. 相关文件

- `data/monograph-chapter-mapping.yaml`：专著章节与 KG 域/实体的机器可读映射。
- `research/`：KG 实体 Markdown 文件。
- `data/relationships/`：KG 关系 Markdown 文件。
- `website/templates/entry.html`：实体页模板（已支持 `verification`、`sources`、`monograph_chapters` 渲染）。
- `website/templates/index.html`：首页模板（已添加专著项目 banner）。
