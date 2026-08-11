# 远程批处理运行手册（RUNBOOK-remote-batch）

**读者**：一台只 clone 了本仓库的干净机器上的 kimi cli 代理。
**目标**：在该机器上独立运行两条长期批处理管线（教材化 / 深读），产出可验收的批次报告。
**铁律**：**禁止任何 git 提交与推送**——一切改动留在工作区，由本机主代理统一收口；状态与产物一律写 `.staging/`（gitignored）。

---

## 0. 前置准备

```bash
git clone <repo-url> awesome-humanoid-robot && cd awesome-humanoid-robot
python3.11 -m venv .venv && source .venv/bin/activate
pip install -r scripts/requirements.txt -r website/requirements.txt
export DEEPSEEK_API_KEY="sk-..."   # 向 boss 索取；禁止打印、禁止写入仓库
```

自检：`.venv/bin/python -c "import requests, yaml, jsonschema, fitz; print('deps ok')"`。

三条管线脚本（仓库内，`--help` 看用法）：

| 脚本 | 用途 |
|------|------|
| `scripts/deep_read_cards.py` | 论文卡六段深读（select/fetch/generate/apply/check/run） |
| `scripts/textbook_grade_cards.py` | 非论文卡教材化（select/fetch/corpus/audit/apply/translate/check） |
| `scripts/audit_card_numbers.py` | 数字白名单审计（whitelist/deepread 两模式，v6 口径） |

---

## 1. 任务 A：全库教材化滚动（约 430 张非论文卡）

**范围与顺序**（每批 50 张，逐批验收后再开下一批）：

| 批 | 类型参数 | 数量级 | 备注 |
|----|----------|--------|------|
| A1 | `--type method` | ~190（B1 已完成 Top 20） | 长尾卡邻居稀疏，wiki 覆盖下降，正文撰写更重 |
| A2 | `--type component` / `technology` / `software_platform` | 47 / 28 / 16 | 需官网/数据手册来源 |
| A3 | `--type concept` / `principle` / `formalism` / `algorithm` / `equation` / `theorem` / `foundation` | ~58 | wiki 覆盖最好 |
| A4 | `--type robot_system` / `oem` / `company` / `component_manufacturer` / `tier1_supplier` | ~48 | 官网规格页为主 |
| A5 | `--type dataset` / `benchmark` / `standard` / 其余小类 | ~41 | 官方页 + 论文摘要 |

`report` 类型（94 张新闻稿卡）**不在本任务范围**，另立专项。

### 单批工作流（以 A1 第一批 50 张为例）

```bash
# 1. 选卡：按图谱度数取 Top 50（自动跳过已升级卡）
.venv/bin/python scripts/textbook_grade_cards.py select --type method --top 50

# 2. 取材：把每张卡的一手来源 URL 填进 .staging/textbook_grade_run/targets.json
#    的 "urls" 字段（{"slug": "https://..."}，每卡 1-4 个：官方文档/arXiv 摘要/官网规格页），然后：
.venv/bin/python scripts/textbook_grade_cards.py fetch

# 3. 语料：声明本批相关的 wiki 章节（grep wiki/docs/chapters 定位），生成数字审计语料映射
.venv/bin/python scripts/textbook_grade_cards.py corpus --chapters chapter-14 chapter-08 --neighbors 6

# 4. 撰写正文（agent 手工完成，质量核心）：每张卡写
#    .staging/textbook_grade_run/bodies/<id>.zh.md，结构见 §3「正文规范」

# 5. 数字白名单审计（必须全 OK 才能继续）
.venv/bin/python scripts/textbook_grade_cards.py audit

# 6. 写入（frontmatter 仅 notes 追加 + round-trip 断言 + 自动备份；幂等）
.venv/bin/python scripts/textbook_grade_cards.py apply

# 7. 翻译重建 en/ko（仅本批卡，勿全库跑）
.venv/bin/python scripts/textbook_grade_cards.py translate

# 8. 本批校验
.venv/bin/python scripts/textbook_grade_cards.py check

# 9. 全库验证（见 §4 完成标准）
```

## 2. 任务 B：深读存量滚动（约 1500 张未深读论文卡）

```bash
# 每片 100 张，自动跳过已有六段深读的卡
.venv/bin/python scripts/deep_read_cards.py run --limit 100 --workers 4
# 或分阶段：select --limit 100 → fetch → generate --workers 7 → apply → check
```

- 重跑同一片时 select 结果可能漂移（先前排完的卡已被标记），**建议逐片新开**：`select --limit 100` 后直接顺序执行到 check，再开下一片；所有阶段幂等，中断后原命令重跑即可续。
- 分片完成后重建 en/ko：`.venv/bin/python scripts/translate_entry_bodies.py --limit <n>` **仅限缺翻译的卡**（脚本幂等跳过已有译文）；如需精确控制，参照 `textbook_grade_cards.py translate` 的逐卡驱动方式。

## 3. 正文规范（教材化卡撰写硬要求）

1. **九段结构**：是什么（准确定义）→ 为什么存在（痛点/历史定位）→ 原理拆解（机制/公式，真技术细节）→ 关键参数与规格（表，每行带来源）→ 横向对比 → 谁在用/应用案例 → 局限与边界 → 常见误区 → 相关知识（图谱实体 id，必须真实存在）。
2. **数字纪律**：每个数字必须能在语料（抓取的 sources/*.txt + corpus_map 声明的 wiki/邻居卡）中逐字查到；查不到的写「未知/需自行确认」；估算/判断标「工程建议值」或「工程判断」；由语料数字推算的标「（按 … 推算）」。
3. **来源纪律**：`## 参考` 只放一手 URL（官网/arXiv/DOI/GitHub）；禁止仓库内部路径（公开 GitHub tree 链接除外）；DOI 先用 `api.crossref.org/works/<doi>` 核验标题再引用。
4. **排版纪律**：表格单元格避免独立的「无」（会译成裸 `None` 触发站点审计警告，改用「—」）；`]` 与 `(` 不得相邻（链接除外）。
5. **frontmatter 只读**：只允许 append `verification.notes`（apply 阶段脚本自动完成并断言）。
6. 风格参照试点 6 卡（`research/technologies/ent_technology_quasi_direct_drive_actuator_2024.md` 等）：大学教材的严谨 + 「它真正改变的不是 X 而是 Y」式判断句。

## 4. 每批完成标准（全绿才算完）

1. `textbook_grade_cards.py check` / `deep_read_cards.py check`：schema 全过、六段/九段齐全、数字抽查全中；
2. 数字审计：`audit` 阶段 0 MISS（教材化）或 `check` 数字采样全中（深读）；
3. KGStore 三语加载无异常：
   `.venv/bin/python -c "import sys; sys.path.insert(0,'website'); from builder.loader import KGStore; ks=KGStore(lang='zh'); ks.load(); print(len(ks.entries), len(ks.relationships))"`
4. 站点构建 + 审计 broken=0：
   `.venv/bin/python -m website.builder.build && .venv/bin/python scripts/audit_site_dist.py`（`DONE broken=0` 才收）。

### 批次报告格式

写 `.staging/batch_reports/<batch_id>.md`，内容固定六节：

1. 目标清单（卡 id + 度数 + 类型）；
2. 取材统计（抓取成功/失败 URL 清单，失败原因）；
3. 前后规模对比（zh 字符数 before/after）；
4. 核验证据（check/audit/KGStore/构建/站点审计的原始数字）；
5. 成本（API 调用次数、usage.json 的 token 数、用时）；
6. 遗留问题与建议。

## 5. 明确禁止

- **git commit / push / checkout / reset 等一切 git 变更**（收口由本机主代理统一做）；
- 修改 frontmatter 除 `verification.notes` 追加以外的任何字段；
- 全库无差别跑翻译脚本（会误触他卡）；
- 编造任何数字或来源 URL；抓不到就写「需补充」；
- 把 `DEEPSEEK_API_KEY` 写进任何文件或打印到日志。

## 6. 故障处理

| 症状 | 处理 |
|------|------|
| DeepSeek 连接重置 / 超时 | 脚本已把合成输入压缩到 ≤20K 字符并带 3 次退避重试；仍失败则隔 10 分钟重跑同一命令（幂等续跑） |
| 生成输出截断（段不全） | 已固化 max_tokens=8000 + 逐段拼接兜底；单卡反复失败则把该卡从 targets.json 移除并记入批次报告「遗留」 |
| arXiv HTML 抓取失败 | fetch 已带 v1/v2/bare/ar5iv 四镜像 + PDF(PyMuPDF) 兜底；全失败记 `fail`，检查本机网络后重跑 |
| 数字审计 MISS | 打开报告列出的卡与缺失数字：要么在语料中找到出处并补进 corpus_map，要么把该数字从正文删除/改「需自行确认」，再重跑 audit |
| 站点审计 broken>0 | 先确认是否本批引入：`grep 卡名 .staging/site_audit/report.md`；是本批引入的链接错误则修正文 `](` 或链接，重建重审 |
| 翻译失败（fail_en/fail_ko） | 单卡重跑 `translate` 阶段（幂等跳过已完成项）；连续失败检查 API 额度与密钥 |
| 中断/掉电 | 所有阶段按文件存在性幂等，原命令重跑即可；`.staging/` 下进度文件勿删 |

## 7. 参考实现（已验证批次）

- 试点 6 卡 + B1 方法类 20 卡的产物与报告：本机 `.staging/textbook_grade/`（REPORT.md、REPORT_B1.md，含完整核验证据格式）；
- 深读批次报告：`.staging/deep_read/manifest.md`、`.staging/catchup/REPORT_BATCH4.md`。
