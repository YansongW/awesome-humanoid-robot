# 附录 F 知识图谱查询示例

本附录介绍如何在本站（kg.rounds-tech.com）上检索与浏览知识图谱，并给出常见问题的查询路径。

## F.1 站点结构速览

| 入口 | 地址 | 内容 |
|---|---|---|
| 首页 | `/` | 领域导航、类型导航、精选实体 |
| 搜索 | `/search/` | 全文检索（名称、摘要、正文、arXiv 号） |
| 图谱 | `/graph/` | 全量关系网络与社区聚类可视化 |
| Wiki | `/wiki/` | 30 章专著 + 附录 |
| 实体卡片 | `/entry/<实体ID>/` | 单个实体的摘要、正文、关系、来源 |
| 类型列表 | `/types/<类型>/` | 某一类型的全部实体 |

## F.2 搜索技巧

**关键词搜索**：在 `/search/` 输入中英文均可，例如：

- `宇树` 或 `Unitree` —— 查找公司、产品及相关论文
- `2304.13705` —— 直接用 arXiv 编号定位论文（如 ACT）
- `全身控制` —— 命中方法、概念、论文章节

**按类型过滤**：搜索结果页顶部点击类型标签，或使用 URL 参数：

```
/search/?type=paper            只看论文
/search/?type=company          只看公司
```

**按领域过滤**：使用 `domain` 参数（首页领域卡片即此链接）：

```
/search/?domain=07_ai_models_algorithms     AI 模型与算法
/search/?domain=04_actuators                执行器
/search/?domain=11_applications_markets     应用与市场
```

参数可组合：`/search/?domain=09_simulation_digital&type=benchmark`（仿真领域的评测基准）。

## F.3 图谱页用法

- **全图模式**：按社区（cluster）着色展示实体网络，可缩放、拖拽。
- **单实体子图**：在任意实体卡片页的"关系子图"中查看其一跳邻居；图谱页右上角搜索框可跳转指定实体。
- **关系类型**：连边标签已本地化，如 `is_based_on`（基于）、`evaluates_on`（评测于）、`uses_dataset`（使用数据集）。

## F.4 常见问题查询路径

**"某个方法的原理和出处？"**
搜索方法名 → 进入实体卡片 → 查看"核心内容"与"参考"来源；卡片"发出的关系"中 `has_prerequisite` 列出前置理论。

**"某个基准/数据集被哪些工作使用？"**
进入基准实体卡片 → "指向它的关系"中 `evaluates_on`（哪些方法在它上面评测）与 `uses_dataset`（哪些工作用了数据）。

**"某家公司的产品和供应链？"**
进入公司卡片 → 查看 `manufacturer_of`（制造的产品）、`supplies`/`sources_from`（供应与采购）关系；供应链全貌另见 Wiki 第 7 章与附录 D。

**"人形机器人某主题的系统综述？"**
先看 Wiki 对应章节（章节目录见 `/wiki/`），章节内引用的实体均有卡片页可继续深入。

## F.5 实体 ID 命名约定

实体 ID 统一为 `ent_<类型>_<名称>[_年份]`，例如：

- `ent_paper_action_chunking_transformer_2023` —— 论文
- `ent_method_whole_body_control` —— 方法
- `ent_company_unitree_robotics_2024` —— 公司
- `ent_standard_iso_13482_personal_care_robot_2014` —— 标准

关系 ID 为 `rel_<源实体ID>_<关系类型>_<目标实体ID>`。

## F.6 程序化访问

本站为纯静态站点，图谱数据以 JSON 公开：

```
/data/search-index.json   搜索索引（含摘要、领域、类型标签）
/data/relations.json      全量节点与连边
/data/clusters.json       社区聚类结果
/data/subgraphs/<实体ID>.json   单实体一跳子图
```

可直接 `fetch` 用于二次开发；源数据（YAML/Markdown）托管于 GitHub 仓库 `YansongW/awesome-humanoid-robot`。
