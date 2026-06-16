# 信息架构设计前分析：基于现有文档的六个问题

> **状态**：分析草案  
> **目的**：在构建正式信息架构之前，基于现有 README、项目章程和本体概述，分析六个核心问题的当前状态和待明确事项。

---

## 问题 1：有哪些类型的信息节点（实体）？

### 当前文档中的线索

`project_charter.md` 的提取模板中提到了一种实体类型：

> Company / Product / Paper / Dataset / Benchmark / Standard / Material / Process / Concept

`ontology/00_overview.md` 中也提到：

> **Entity type**: Company / Product / Paper / Dataset / Benchmark / Standard / Material / Process / Concept

### 分析

这 9 种实体类型是一个合理起点，但面对「从0到1量产」的全产业视角，还需要补充和细化：

| 当前实体 | 是否足够 | 待补充或拆分 |
|----------|----------|--------------|
| Company | 不够 | 需要区分 OEM整机厂、Tier-1供应商、Tier-2供应商、零部件厂商、软件公司、研究机构 |
| Product | 不够 | 需要区分整机产品、零部件产品、软件产品、材料产品、工具/设备 |
| Paper | 基本够 | 但需明确是否包含专利、白皮书、行业报告 |
| Dataset | 基本够 | — |
| Benchmark | 基本够 | — |
| Standard | 基本够 | 安全标准、行业规范、认证体系 |
| Material | 基本够 | 但需区分原材料、半成品、复合材料 |
| Process | 基本够 | 制造工艺、组装工艺、测试工艺 |
| Concept | 太宽泛 | 建议拆分为 Technology（技术路线）、BusinessModel（商业模式）、MarketSegment（市场细分） |

### 初步建议

将实体扩展为 12~15 种，并建立层级关系。例如：

```
Organization
├── OEM（整机厂）
├── Tier-1 Supplier（一级供应商）
├── Tier-2 Supplier（二级供应商）
├── Component Manufacturer（零部件制造商）
├── Software Vendor（软件厂商）
├── Research Institution（研究机构）
└── Standards Body（标准机构）

Product / Artifact
├── Robot System（整机系统）
├── Component（零部件）
├── Material（材料）
├── Software / Platform（软件/平台）
├── Tool / Equipment（工具/设备）
└── Facility / Factory（工厂/产线）

Knowledge
├── Paper（论文）
├── Patent（专利）
├── Report（报告）
├── Dataset（数据集）
├── Benchmark（基准）
├── Standard（标准）
└── Concept / Technology（概念/技术路线）

Market / Policy
├── Market Segment（市场细分）
├── Application Scenario（应用场景）
├── Regulation（法规）
└── Business Model（商业模式）
```

---

## 问题 2：节点之间可能存在哪些关系？

### 当前文档中的线索

`ontology/00_overview.md` 的「Cross-Cutting Relationships」一节列举了一些关系：

- Raw materials → Components：magnet supply affects motor performance and cost
- Components → Design：actuator torque density determines feasible morphology
- Design → Manufacturing：DFM determines yield
- Manufacturing → Mass Production：process capability determines scaling potential
- AI Models → Components：algorithms compensate for or require hardware
- Data → AI Models：data availability constrains learning-based approaches
- Benchmarks → Applications：benchmarks reflect deployment needs
- Policy → Applications：regulation determines market access
- Markets → Investment → R&D：market pull drives upstream innovation

### 分析

这些例子说明关系是**跨域、跨层、有方向**的，但文档没有给出关系类型的完整清单。为了让信息系统不坍塌，必须提前定义关系类型，而不是临时起意。

### 初步建议

关系可以分为以下几类：

#### 供应链关系（Supply Chain）

| 关系 | 方向 | 示例 |
|------|------|------|
| `supplies` | A → B | 磁材供应商 → 电机制造商 |
| `consumes` | A → B | 电机制造商 → 稀土磁材 |
| `produces` | A → B | 电机制造商 → 伺服电机 |
| `integrates` | A → B | 整机厂 → 电机 |
| `sources_from` | A → B | 整机厂 → 深圳供应链 |

#### 技术依赖关系（Technical Dependency）

| 关系 | 方向 | 示例 |
|------|------|------|
| `enables` | A → B | 高扭矩密度执行器 → 双足动态行走 |
| `requires` | A → B | VLA → GPU计算单元 |
| `constrains` | A → B | 电池能量密度 → 续航时间 |
| `compensates_for` | A → B | 算法 → 传感器精度不足 |

#### 层级派生关系（Hierarchical / Derivation）

| 关系 | 方向 | 示例 |
|------|------|------|
| `is_part_of` | A → B | 电机 → 执行器模组 |
| `is_subsystem_of` | A → B | 执行器模组 → 腿部 |
| `is_instance_of` | A → B | Tesla Optimus → 人形机器人整机 |
| `is_prerequisite_for` | A → B | 仿真环境 → sim-to-real训练 |

#### 市场与政策关系（Market & Policy）

| 关系 | 方向 | 示例 |
|------|------|------|
| `serves` | A → B | 人形机器人 → 汽车制造 |
| `regulated_by` | A → B | 人形机器人 → ISO安全标准 |
| `drives_demand_for` | A → B | 劳动力短缺 → 人形机器人 |
| `competes_with` | A ↔ B | 人形机器人 ↔ 工业机器人 |

#### 验证与引用关系（Provenance）

| 关系 | 方向 | 示例 |
|------|------|------|
| `cites` | A → B | 条目 → 原始论文 |
| `verified_by` | A → B | 论断 → 来源 |
| `conflicts_with` | A ↔ B | 来源A ↔ 来源B |

---

## 问题 3：节点如何分层、分域？

### 当前文档中的线索

`ontology/00_overview.md` 将价值链分为四层：

```
上游：01 原材料 / 02 零部件 / 03 制造工艺
中游：04 组装集成测试 / 05 量产 / 06 设计工程
智能层：07 AI模型算法 / 08 软件中间件 / 09 数据数据集
验证与市场层：10 评测基准 / 11 应用市场 / 12 政策法规
```

同时每个条目有标签：

> **Domain**: one or more of the ten domains above  
> **Layer**: Upstream / Midstream / Intelligence / Validation-Markets

### 分析

当前分层是合理的，但有两个问题：

1. **设计工程（06）放在中游是否合适？** 设计实际上是贯穿上游到中游的，它影响零部件选择和制造工艺，又被制造可行性约束。
2. **AI/软件/数据放在「智能层」是否与其他层正交？** 它们实际上渗透到所有层：制造工艺中有AI质检，组装中有AI辅助校准，应用层有AI任务规划。

### 初步建议

保留四层作为**价值链主分层**，但引入第二个维度：**功能角色（Functional Role）**。这样每个节点可以有两个标签：

| 维度 | 选项 |
|------|------|
| **价值链层（Value Chain Layer）** | Upstream / Midstream / Intelligence / Validation-Markets |
| **功能角色（Functional Role）** | Material / Component / Process / System / Intelligence / Market / Policy |

例如：
- 一个电机制造商：Layer = Upstream, Role = Component
- 一个仿真软件：Layer = Intelligence, Role = Tool/Platform
- 一个AI质检算法：Layer = Midstream（因为它用于制造），Role = Intelligence

这样既能保持产业链视角，又能表达技术的跨层渗透。

---

## 问题 4：跨域关系如何被显式表达和追踪？

### 当前文档中的线索

`project_charter.md` 提到：

> Cross-links: Related entries in other domains

`ontology/00_overview.md` 提到：

> These relationships are captured in per-domain documents through **cross-links**.

### 分析

「Cross-links」是一个好的概念，但没有说明如何具体实现。如果只是 markdown 里的互相链接，未来节点多了以后无法做查询、分析和可视化。

### 初步建议

跨域关系应该被**显式建模为独立对象**，而不是隐式链接。建议：

1. **关系作为一等公民**：每个关系有自己的 ID、类型、方向、来源节点、目标节点、验证状态、引用来源。
2. **关系类型受限**：使用预定义的关系类型（见问题2），不允许随意造词。
3. **关系可跨域**：明确允许 A 域节点 → B 域节点的关系，并在架构中支持。
4. **机器可读**：关系存储为 JSON/YAML，便于后续导入图数据库或做网络分析。

示例：

```yaml
relationship:
  id: rel_001
  type: supplies
  source:
    id: company_neo_materials
    domain: 01_raw_materials
  target:
    id: company_motor_maker_x
    domain: 02_components
  description: 稀土磁材供应商向电机制造商供应钕铁硼磁材
  status: verified
  sources:
    - url: https://example.com/annual-report-2025
      date: 2025-03-15
```

---

## 问题 5：验证状态、多语言、来源引用如何被结构化？

### 当前文档中的线索

验证状态（`project_charter.md`）：

| Level | Meaning |
|-------|---------|
| ✅ Verified | Claim is supported by a primary source and has been reviewed |
| ⚠️ Partially verified | Supported by secondary sources or plausible inference |
| ❓ Unverified | Mentioned in sources but not independently confirmed |
| 🔮 Speculative | Forward-looking or analytic claim, clearly marked as such |

多语言：README、charter、ontology 已有英文、中文、韩文版本。

来源引用：提取模板中有 Source 字段。

### 分析

当前状态是文档级别的多语言，但**条目级别的多语言**还没有设计。未来一个公司或零部件可能有中英韩三种名称和描述。

验证状态也需要细化：谁验证的？什么时候？基于什么来源？

### 初步建议

#### 验证状态结构化

每个条目/关系都有 `verification` 对象：

```yaml
verification:
  status: verified | partially_verified | unverified | speculative
  reviewed_by: human | ai | human_and_ai
  reviewed_at: 2026-06-16
  confidence: high | medium | low
  notes: 基于公司年报和第三方拆解报告
```

#### 来源引用结构化

```yaml
sources:
  - id: src_001
    type: primary | secondary | press_release | patent | report | paper
    url: https://...
    title: ...
    date: 2026-05-20
    accessed_at: 2026-06-16
    archived_url: ...
```

#### 多语言结构化

```yaml
names:
  en: Rare-earth Permanent Magnet
  zh: 稀土永磁体
  ko: 희토류 영구자석

descriptions:
  en: ...
  zh: ...
  ko: ...
```

---

## 问题 6：机器可读格式是什么（JSON/YAML schema）？

### 当前文档中的线索

目前没有 schema 定义，只有 markdown 文档。

### 分析

如果只有 markdown，未来无法实现：
- 关系查询
- 自动一致性检查
- 多语言同步
- 数据可视化
- AI 批量处理

### 初步建议

采用 **YAML frontmatter + markdown body** 的混合格式：

```yaml
---
id: ent_001
type: material
names:
  en: Neodymium-Iron-Boron Magnet
  zh: 钕铁硼磁体
  ko: 네오디뮴 철 붕자석
domains:
  - 01_raw_materials
layers:
  - upstream
functional_roles:
  - material
summary:
  en: ...
  zh: ...
  ko: ...
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: 2026-06-16
sources:
  - id: src_001
    type: report
    url: https://...
relationships:
  - id: rel_001
    type: consumed_by
    target_id: ent_002
---

# Markdown body for long-form narrative
...
```

这种格式兼顾：
- 人类可读（markdown 正文）
- 机器可读（YAML frontmatter）
- Git 友好（纯文本）
- AI 可处理（结构化数据）

同时定义两个 JSON Schema：
- `entry_schema.json`：节点 schema
- `relationship_schema.json`：关系 schema

---

## 综合结论

在填充任何领域内容之前，我们需要先建立：

1. **扩展后的实体类型清单**（12~15 种，带层级）
2. **预定义的关系类型词典**（供应链、技术依赖、层级派生、市场政策、验证引用）
3. **双维度标签系统**（价值链层 + 功能角色）
4. **关系作为一等公民的数据模型**
5. **验证、来源、多语言的结构化字段**
6. **YAML frontmatter + markdown 的条目格式 + JSON Schema**

下一步：基于以上分析，产出正式的 `docs/architecture/information_model.md` 和配套 schema 文件。
