---
id: ent_company_ieee_sa
type: company
'title:': IEEE 标准协会 / IEEE Standards Association (IEEE SA)
domain: 04_assembly_integration_testing
theoretical_depth: system
aliases:
- IEEE Standards Association (IEEE SA)
- IEEE 标准协会
status: active
created_at: 2024-01-15 00:00:00+00:00
updated_at: 2026-07-01 00:00:00+00:00
sources:
- id: ent_company_ieee_sa_official
  type: website
  url: https://standards.ieee.org
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-01 00:00:00+00:00
  review_notes: Data sourced from official website and public reports; missing specs
    marked as 未公开.
---





# ieee_sa

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | IEEE 标准协会 |
| **英文名** | IEEE Standards Association (IEEE SA) |
| **总部** | 美国新泽西州皮斯卡塔韦 |
| **成立时间** | 1963（IEEE 标准业务可追溯至 1960 年代） |
| **官网** | [https://standards.ieee.org](https://standards.ieee.org) |
| **供应链环节** | 机器人标准、系统架构、伦理自治系统标准 |
| **企业属性** | IEEE 下属标准组织、非营利专业机构 |
| **母公司/所属集团** | IEEE（Institute of Electrical and Electronics Engineers） |
| **数据来源** | IEEE SA 官网、IEEE 标准数据库 |

## 公司简介

IEEE SA 是全球领先的电气、电子及信息技术标准制定机构，负责 IEEE 标准全生命周期管理，涵盖立项、草案评审、发布与维护。在机器人领域，IEEE SA 发布了本体、互操作、伦理与自治系统相关标准，被科研、产业与法规引用。

IEEE 1872 机器人本体标准、IEEE 7000 伦理设计流程标准等构成了 IEEE 在机器人领域的核心贡献。IEEE SA 还通过 Industry Connections 活动推动机器人、自动驾驶与人工智能的跨领域标准化。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 机器人本体与互操作标准 | 术语、本体与数据交换规范 | [IEEE 机器人标准族](../../../appendices/appendix-d/products/product_ieee_sa_robotics_standards.md) | 机器人研发、仿真、知识库 |
| 伦理与可信系统标准 | 系统工程伦理风险处理 | IEEE 7000 系列 | 自动驾驶、医疗机器人、人形机器人 |
| 行业连接与指南 | 预标准化研究与实施指南 | IEEE Industry Connections 报告 | 产业联盟、学术机构 |

## 代表产品

### IEEE 机器人标准族

> IEEE 机器人标准族：请访问 [官方资料](https://standards.ieee.org) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 标准系列 | IEEE 1872、IEEE 7000 等 | IEEE SA |
| 核心标准 | IEEE 1872-2015、IEEE 7000-2021 | IEEE 标准数据库 |
| 适用范围 | 机器人本体、系统互操作、伦理设计 | 公开资料 |
| 发布状态 | 现行/持续维护 | IEEE SA |
| 标准类型 | IEEE 标准、IEEE 指南/推荐规程 | IEEE |
| 价格 | 未公开 | IEEE 标准商店 |
| 认证属性 | 非强制，供产业与法规引用 | IEEE SA |

**技术亮点**：面向机器人知识表示、本体建模与伦理设计流程，强调系统级安全、透明性与可解释性。

**应用场景**：机器人知识图谱构建、跨平台互操作、伦理风险评估、人形机器人行为设计规范。

## 供应链位置

- **上游关键零部件/材料**：IEEE 会员与技术专家、研究机构、企业工作组、学术成果
- **下游客户/应用场景**：机器人制造商、自动驾驶公司、医疗机器人企业、科研机构、立法与监管机构
- **主要竞争对手/对标**：ISO/IEC 联合标准、ANSI/RIA R15.06、OMG 机器人标准、各国国家标准

## 知识图谱节点与关系

- 公司实体：`ent_company_ieee_sa`
- 产品实体：`ent_product_ieee_sa_robotics_standards`
- 零部件实体：`ent_component_ieee_sa_robotics_standards_core`
- 关键关系：
  - `ent_company_ieee_sa` -- `manufactures` --> `ent_product_ieee_sa_robotics_standards`
  - `ent_company_ieee_sa` -- `manufactures` --> `ent_component_ieee_sa_robotics_standards_core`
  - `ent_product_ieee_sa_robotics_standards` -- `uses` --> `ent_component_ieee_sa_robotics_standards_core`

## 参考资料

1. [IEEE SA 官网](https://standards.ieee.org)
2. [IEEE 1872-2015 标准页面](https://standards.ieee.org/standard/1872-2015.html)
3. [IEEE 7000-2021 标准页面](https://standards.ieee.org/standard/7000-2021.html)
4. [附录 D 企业目录](../../../appendices/appendix-d/index-companies.md)
5. 公开行业报告与市场资料
6. 数据更新备注：2026-07-01