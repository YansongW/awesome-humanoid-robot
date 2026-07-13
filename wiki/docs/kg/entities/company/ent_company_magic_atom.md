---
id: ent_company_magic_atom
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 魔法原子
  en: MagicLab / Magic Atom
status: active
sources:
- id: src_magic_atom_official
  type: website
  url: https://www.magiclab.top
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 魔法原子 / MagicLab / Magic Atom

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 魔法原子（魔法原子机器人科技有限公司） |
| **英文名** | MagicLab / Magic Atom |
| **总部** | 中国无锡/苏州 |
| **成立时间** | 2024 年 1 月 |
| **官网** | [https://www.magiclab.top](https://www.magiclab.top) |
| **供应链环节** | 整机 OEM / 通用人形机器人 |
| **企业属性** | 初创独角兽、追觅系具身智能企业 |
| **母公司/所属集团** | 追觅科技（战略孵化/投资） |
| **数据来源** | 魔法原子官网、WRC 展商信息、央视网、什么值得买 |

## 公司简介

魔法原子是一家专注于具身智能和通用人形机器人研发、生产与产业化落地应用的高科技企业。公司前身可追溯至追觅科技内部的具身智能与人形机器人研发团队，2024 年 1 月正式独立注册。核心团队来自清华大学、上海交通大学、浙江大学、北京航空航天大学、纽约大学等国内外知名高校，研发人员占比超过 80%。

公司坚持软硬一体全栈自研，核心硬件覆盖全关节模组、灵巧手、减速器、驱动器等关键零部件，并在运动控制、导航、多模态感知与具身操作等算法领域建立优势。其产品矩阵包括全尺寸通用人形机器人 MagicBot Gen1、高动态小人形机器人 MagicBot Z1 以及系列化四足机器人。2026 年，魔法原子成为央视春晚智能机器人战略合作伙伴。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 全尺寸人形机器人 | 通用服务与工业操作 | MagicBot Gen1 | 工业、商业、家庭 |
| 高动态小人形机器人 | 科研教育与轻量服务 | MagicBot Z1 | 科研、教育、娱乐 |
| 四足机器人 | 陪伴、巡检与表演 | MagicDog / MagicDog-W / MagicDog-Y1 | 家庭、文旅、工业巡检 |

## 代表产品

### MagicBot Gen1

> MagicBot Gen1：请访问 [官方资料](https://www.magiclab.top) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 174 cm | 世界机器人大会展商资料 |
| 重量 | 未公开 | - |
| 自由度 | 42 个主动自由度 | 世界机器人大会展商资料 |
| 负载/扭矩 | 未公开 | - |
| 速度/转速 | 未公开 | - |
| 续航 | 未公开 | - |
| 接口/通信 | 自研场景大模型“原子万象” | 央视网报道 |
| 价格 | 未公开 | 需询价 |

**技术亮点**：核心零部件自研率超 90%，搭载自研关节模组与灵巧手，内置多模态感知算法与大语言模型，支持多机协作。

**应用场景**：工业上下料、汽车导购、交通疏导、新闻播报、商业导览、家庭助理。

### MagicBot Z1

> MagicBot Z1：请访问 [官方资料](https://www.magiclab.top) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 140 cm | Gasgoo/CES 2026 报道 |
| 重量 | 未公开 | - |
| 自由度 | 50 个仿生关节、基础 24 DOF（可扩展） | Gasgoo 报道 |
| 负载/扭矩 | 单关节最大输出扭矩 >130 N·m | Gasgoo 报道 |
| 速度/转速 | 奔跑速度突破 4 m/s | 全球合作伙伴大会 |
| 续航 | 未公开 | - |
| 接口/通信 | 360° 感知、自主导航、多模态对话 | Gasgoo 报道 |
| 价格 | 未公开 | 需询价 |

**技术亮点**：高动态运动能力，可完成连续起身、下腰、越跳等复杂动作；采用自研高性能关节模组。

**应用场景**：科研教育、商业服务、工业操作、家庭陪伴。

## 供应链位置

- **上游关键零部件/材料**：自研关节模组、灵巧手、减速器、驱动器；与追觅共享电机、电控、结构件供应链。
- **下游客户/应用场景**：追觅工厂、江苏广电、无锡政府、商业综合体、文旅景区。
- **主要竞争对手/对标**：智元机器人、傅利叶智能、优必选、银河通用。

## 知识图谱节点与关系

- 公司实体：`ent_company_magic_atom`
- 产品实体：`ent_product_magic_atom_magicbot_gen1`、`ent_product_magic_atom_magicbot_z1`
- 关键关系：
  - `ent_company_magic_atom` -- `manufactures` --> `ent_product_magic_atom_magicbot_gen1`
  - `ent_company_magic_atom` -- `manufactures` --> `ent_product_magic_atom_magicbot_z1`

## 参考资料

1. [魔法原子官网](https://www.magiclab.top)
2. [世界机器人大会 – 魔法原子展商信息](https://www.worldrobotconference.com/expo/company/450.html)
3. [央视网 – 魔法原子成为 2026 春晚机器人战略合作伙伴](https://1118.cctv.com/2026/01/26/ARTIVr7vNNg1L6XF2som2ZnS260126.shtml)
4. [Gasgoo – CES 2026 魔法原子将携多款机器人亮相](https://m.gasgoo.com/news/70441287.html)
5. [什么值得买 – 魔法原子与追觅科技关系](https://post.smzdm.com/p/ax6qz4q4)