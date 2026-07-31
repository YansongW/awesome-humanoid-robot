# 产品 Backlog（可追踪）

> 依据 `docs/product/productization_analysis.md`（90 天路线）与历次迭代整理。
> 规则：完成即勾掉并注明日期/commit；新增项带优先级（P0 先做 / P1 尽快 / P2 排期）与来源。

## Month 1：让现有图谱可被消费（基本达成）

- [x] 搜索召回修复（全量扫描 + 完整摘要 + tags，9 查询全量召回）— 2026-07-29
- [x] M01–M20 路线图任务页（三语）— 2026-07-29
- [x] BYOK AI 问答（纯前端 RAG，零后端）— 2026-07-29
- [x] Graph + Chat 一体化（图谱页聊天面板、来源高亮、焦点子图）— 2026-07-29/30
- [x] Search-first AI（Perplexity 式：搜索页顶部 AI 回答模块，/ask/ 独立页拆除）— 2026-07-30
- [x] 全站审计 + CI 关卡（523 坏链修复，`scripts/audit_site_dist.py` 进 CI）— 2026-07-30
- [x] 1457 张英文化卡片中文化（zh 精要 + en 保留 + ko 补译）— 2026-07-30

## Month 2：演进与审阅闭环（进行中）

- [x] 研究室清单摄取（835 篇 → 净新增 323 → 终值 247 张卡上线：158 arXiv 全文卡 / 6 项目页卡 / 83 保守卡；484 重复、13 人工队列、7 零信息删除）— 2026-07-30 b45512f4+208a71db
- [x] 每周定时演进管线（arXiv 新成果 → LLM 起草 → PR 人工合并）— 2026-07-30 a42728d9；**secrets 待配置**
- [ ] **Review Inbox Web 审阅面板**：staging 草稿可视化 approve/reject/edit、verification badge 展示——自主演进放开的前置（NL 工作流排在它之后）— P0
- [ ] 机构实体目录（paper→机构 关系的前置；先批量建机构卡）— P1
- [ ] 重复行「来源补充」专项：清单 484 条重复行的来源 URL 补进现有卡（只增不改约束下另立项）— P1
- [ ] wiki 章节纳入问答/检索语料（519 页分块设计）— P1
- [ ] 首页图谱化（产品文档 P0 方向：首页即图谱画布）— P1
- [ ] 实体卡侧边栏（图谱节点点击出详情卡 + 「追问」动作，产品文档 P1）— P1
- [ ] 追问类问句检索优化（追问检测 → 跳过/改写当轮检索，减少噪声上下文）— P2
- [ ] 回答内联引用编号（[1][2] 逐句引用）— P2

## Month 3：通用性与商业化验证

- [ ] workstream 配置抽象（scripts/ai4sci_workstreams/ → 可配置模板）— P2
- [ ] 第二领域 demo（固态电池 / 大模型推理优化候选）— P2
- [ ] 订阅页与付费边界设计（Free/Learner/Pro/Team）— P2
- [ ] 画布上自然语言构建工作流（场景 B；排在 Review Inbox 之后）— P2

## 运维与债

- [ ] repo secrets 配置 DEEPSEEK_API_KEY（定时管线生效前提，需用户操作）
- [ ] qa-corpus 分片 gzip/按需进一步优化（当前分片 <1MB 可接受）
- [ ] 12 reports + 2 companies 卡的英文全文 Overview 段瘦身评估
- [ ] ko 的 summary.ko 翻译（当前只译了正文段）
- [ ] 触屏端图谱面板拖拽（touchstart）与 iOS 键盘遮挡
