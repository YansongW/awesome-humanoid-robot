# AGENTS.md — 项目工作约定

本文件记录本仓库的数据纪律与常用工作流，供所有 AI 代理与贡献者遵守。
修改本文件提到的约定、结构或流程时，请同步更新本文件。

## 项目是什么

人形机器人知识图谱 + 产品化站点，目标是让零基础用户"查得懂、学得会、造得出"：

- **查**：知识图谱（`research/` 实体 + `data/relationships/` 关系）→ 静态站检索/图谱页
- **学**：Wiki 教科书（`wiki/docs/chapters/` 30 章 + `appendices/` 7 篇）
- **造**：0→1 路线图（`roadmap/docs/` 4 阶段页 + `missions/` M01–M20 任务页 + `playbooks/` 4 手册 + `data/roadmap_mapping.yaml` 卡片绑定）

## 数据铁律（最重要）

1. **只增不改**：不覆盖 `research/` 现有卡片与 `data/relationships/` 现有关系的任何字段/段落。
   唯一例外是**事实性错误**（如类型标错、张冠李戴的内容），且修正必须可追溯
   （在 verification notes 追加修正记录 + 提交信息说明 + 在 `.staging/` 留 manifest）。
2. **新关系必须带证据**：`verification.notes` 记录证据句与规则编号（如 `p6_llm_link`），
   使任一批次可整体回溯/撤销；`confidence` 按证据强度给（hedged 措辞一律 `low`）。
3. **禁止 ID 幻觉**：LLM 产出的 `target_id` 必须来自真实实体候选清单；
   落库前必须程序化校验两端点存在（dangling = 0 是硬门槛）。
4. **YAML 安全**：frontmatter 写入后必须 round-trip 校验（`yaml.safe_load`）；
   含 `---`、表格分隔符、冒号的字符串必须加引号。
5. **来源纪律**：具体参数（价格/扭矩/自由度等）必须有来源 URL；
   查不到的写"未知/需自行确认"，禁止编造；无来源的估算值一律标注"工程建议值"，
   需按读者的具体设计校核。
6. **公开页面禁止内部路径引用**：`roadmap/docs*/`、`wiki/docs*/`、实体正文等面向读者的内容，
   来源一律用一手 URL（GitHub 仓库/arXiv/官方页），禁止以仓库内部路径
   （如 `data/roadmap/research/xxx.md`）作为来源标注；内部溯源路径只允许出现在
   frontmatter `verification.notes`。指向公开仓库目录的 GitHub 链接
   （`github.com/YansongW/awesome-humanoid-robot/tree/main/...`）不受此限。
   CI（deploy.yml "Check for internal repo paths"）会对违规字面引用 fail。

## 目录速览

- `research/<type_plural>/*.md` — 实体卡（frontmatter + 正文 `## 概述` / `## 核心内容` / `## 参考`）
- `data/relationships/*.md` — 关系（纯 frontmatter，schema：`data/schema/v1/relationship_schema.json`）
- `data/roadmap_mapping.yaml` — 路线图↔卡片绑定（entities 区块由脚本生成，**勿手改**）
- `data/roadmap/research/` — 开源方案调研档案（带 URL 的一手来源）
- `wiki/docs/`、`roadmap/docs/` — Wiki 教科书与 0→1 路线图中文稿（两个独立产品，勿合并）
- `wiki/docs-en|ko/`、`roadmap/docs-en|ko/` — 对应 en/ko 翻译镜像（`translate_wiki_pages.py` 生成，结构同 zh）
- `website/builder/` — 静态站构建器（zh 根路径，en/ko 子路径）；模板在 `website/templates/`
- `web/` — FastAPI 本地 GUI（检索 / 子图 / LLM 问答 / 路线图视图）
- `scripts/` — 摄取、挖掘、审计、翻译脚本（见下）
- `.staging/` — 中间产物与进度检查点（gitignored）

## 常用命令

```bash
make help            # 全部命令
make kg              # 审计 + 连通性摘要
make site / serve    # 构建 / 本地预览静态站
make gui             # 本地 Web GUI (:8000)
make roadmap-check   # 重新生成路线图↔卡片绑定
```

## 关键脚本与何时用

| 脚本 | 用途 | 注意 |
|------|------|------|
| `scripts/audit_entry_quality.py --json-only` | 质量+连通性审计 | **不要用 MD 模式**（极慢）；报告在 `.staging/quality_reports/` |
| `scripts/build_latent_relationships.py [--write]` | 确定性挖潜关系（引用/共享来源/提及/wiki 共现） | 先干跑看数量与样本 |
| `scripts/link_zero_degree_entities.py [--llm] [--write]` | 缩写/机构匹配 + LLM 零度挂接 | LLM 模式有检查点，可安全重入；`--include-types` 限定类型 |
| `scripts/llm_classify_relations.py [--write]` | LLM 给提及对分型 | 进度写在 `.staging/llm_relation_progress.jsonl` |
| `scripts/build_roadmap_mapping.py` | 从路线图页面链接再生成 `entities:` 绑定 | 改路线图页面后必跑 |
| `scripts/translate_entry_bodies.py` | DeepSeek 翻译实体正文 en/ko | 幂等，可中断续跑；密钥在 `~/Desktop/.ai_credentials.txt`（**禁止打印**） |
| `scripts/auto_promote_staging.py` | 提升 staging 实体/关系到生产 | 带 schema 校验与端点检查 |
| `scripts/weekly_discovery.py [--dry-run] [--since YYYY-MM-DD]` | 每周 arXiv 新论文发现 → DeepSeek 起草中文卡 → schema 校验 → 写卡+报告 | 上限 30 篇/周；报告在 `.staging/weekly_discovery/`；CI 每周一自动跑并开 PR（`.github/workflows/weekly-discovery.yml`，需 secret `DEEPSEEK_API_KEY`） |

DeepSeek：endpoint `https://api.deepseek.com/chat/completions`，model `deepseek-chat`。

## 已知边界与遗留

- 20 篇边缘论文保持孤立（与主业关联弱，可接受）。
- 部分 company/component 实体是"新闻稿卡"（标题式命名）——属于 report 内容；
  已重定型一批（见 `scripts/fix_headline_entity_types.py` 与 `.staging/retype_manifest_*.json`），
  其余已挂边的留待后续专项。
- `ent_component_lidar_livox_mid360` 已并入 `ent_component_livox_mid_360_lidar_2024`（2026-07-20，见 `.staging/merge_livox_manifest_*.json`）。
- en/ko 的 Wiki 章节与路线图页是机翻/回退中文，翻译管线同实体正文。
- 路线图/Wiki 是面向公众的客观知识产品：页面只讲方法与可溯源事实，不挂统一免责声明，也不记录任何团队的实机建造过程；具体的实机建造（指标表、选型决策、实测数据）在独立工作区进行，不回写公共页面。
