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

## 发现层（2026-08-04 boss 指出 Ego2Robot 漏网后的整改）

- [x] 每周定时管线（arXiv）— 建成但**因缺 secret 从未成功运行**（2026-08-03 首跑失败）
- [ ] **激活**：repo secrets 配 DEEPSEEK_API_KEY（用户操作）→ 手动触发补跑验证
- [ ] **策展网**：跟踪策展型仓库更新（RealXiaoze/humanoid-motion-intelligence 等），新解读 → 建卡挂链 — P0
- [ ] **"丢链接即建卡"通道**：用户转发链接（微信/arXiv/项目页）→ 1 小时内深读建卡——高信号源是用户自己；微信文机器不可抓，人是最强雷达 — P0（也是 OpenSci4X「收进图谱」功能原型）
- [ ] 发现层三源合一：arXiv 宽网 + 策展网 + 用户雷达，统一进 staging → 审阅 — P1

## 阻塞项：Mac mini 任务移交（agent-bridge）

**状态**：BLOCKED — Mac mini（songmac-mini，100.102.58.80）sshd 只收密钥且未授权 MacBook 公钥；Tailscale SSH server 未启用；无密码认证；无其他开放端口。
**解锁条件**：有人在 mini 现场执行一条命令（把 MacBook 公钥写入 ~/.ssh/authorized_keys）。
**现场傻瓜命令**（在 mini 的终端执行）：
```bash
mkdir -p ~/.ssh && chmod 700 ~/.ssh && echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGz6GVi91MGvgPyQW69emWdqXnt2I9RwmOQqfsAqgG0G agentctl@MacBook-Air" >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys && echo OK
```
**解锁后动作**：agentctl 挂载长期批处理任务（RUNBOOK-remote-batch.md 任务 A/B）到 mini 的 kimi cli（tmux 持久、断线不丢）。
**过渡方案**：批处理在 MacBook Air 本地跑（管线幂等，桥通后无缝移交）。记录于 2026-08-11。

## 进行中任务台账（2026-08-31 快照）

### 自动巡航中（无需人工）
- [ ] **存量论文卡深读滚动**：片 1–10 已上线（900 张）。剩余片 11–14（~500 张），代理滚动中，每片验收链+RUNBOOK，主代理逐批提交推送。管线自片 7 起零人工修正
- [ ] **Mac mini 移交桥**：cron `ddb2e1da` 每 3 天 11:23 探活。解锁条件=现场傻瓜命令（本文件底部「阻塞项」），桥通后把滚动任务迁到 mini

### 待执行（排队）
- [ ] **report 类 94 张专项**：新闻稿卡的处理方案（定型/重写/保留策略），排在深读滚动之后
- [ ] **wiki 章节纳入 QA 语料**（519 页分块设计）
- [ ] **en 六段镜像**（论文卡 en 从摘要节升级为六段镜像，~$1.5，管线现成）
- [ ] **18 张 ent_paper_* 命名卡 retype 专项**（methods/ 邻居）
- [ ] **拼音/英文重复公司卡合并**（sanhuazhikong、tuopujituan 2 对）
- [ ] **JS 重站规格补强**（Tesla/Figure 等，需带渲染的抓取通道）
- [ ] **example.com 占位图**（wiki/TODO-images.md 一张）
- [ ] **未产出卡补全文**：深读滚动中 no_fulltext 卡（累积约 90 张，需人工供 PDF 或等 arXiv HTML 版）

### 等 boss 人工
- [ ] **审合 PR #1**（每周管线首张，6 篇新论文）
- [ ] **kap-server 原型真机目验**（localhost:8000，重点：diff 卡接受/分支 tab 真实节点/刷新恢复）
- [ ] **教材卡抽验**（WBC/准直驱/G1 等 3–5 张）
