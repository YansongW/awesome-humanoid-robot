---
id: ent_company_iso
type: company
'title:': 国际标准化组织 / International Organization for Standardization (ISO)
domain: 04_assembly_integration_testing
theoretical_depth: system
aliases:
- International Organization for Standardization (ISO)
- 国际标准化组织
status: active
created_at: 2024-01-15 00:00:00+00:00
updated_at: 2026-07-01 00:00:00+00:00
sources:
- id: ent_company_iso_official
  type: website
  url: https://www.iso.org
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-01 00:00:00+00:00
  review_notes: Data sourced from official website and public reports; missing specs
    marked as 未公开.
---





# iso

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 国际标准化组织 |
| **英文名** | International Organization for Standardization (ISO) |
| **总部** | 瑞士日内瓦 |
| **成立时间** | 1947 |
| **官网** | [https://www.iso.org](https://www.iso.org) |
| **供应链环节** | 机器人标准、安全标准、测试规范、合格评定 |
| **企业属性** | 非政府国际组织 |
| **母公司/所属集团** | 无 |
| **数据来源** | ISO 官网、ISO/TC 299 技术委员会页面 |

## 公司简介

ISO 是全球最大的非政府性国际标准组织，由 170 多个国家标准机构组成。其下属的 ISO/TC 299 “机器人”技术委员会负责制定工业机器人、服务机器人、协作机器人及个人护理机器人的安全、性能与互操作标准，是全球机器人产业最重要的标准来源之一。

ISO/TC 299 与 IEC/TC 44 等委员会协同工作，发布的 ISO 10218、ISO/TS 15066、ISO 13482 等标准被各国法规、认证机构与机器人制造商广泛采用，为人形机器人、协作机器人及移动服务机器人的安全设计提供基准。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| ISO/TC 299 机器人标准 | 机器人安全与性能规范 | [ISO/TC 299 机器人标准族](../../../appendices/appendix-d/products/product_iso_tc299_standards.md) | 工业机器人、协作机器人、服务机器人、人形机器人 |
| 合格评定与导则 | 认证、测试与实施指南 | ISO/IEC 17000 系列、ISO/TR 20218 | 第三方检测、法规合规、市场准入 |
| 培训与出版物 | 标准解读与实施支持 | ISO 在线商店、技术报告 | 制造商、集成商、监管机构 |

## 代表产品

### ISO/TC 299 机器人标准族

> ISO/TC 299：请访问 [官方资料](https://www.iso.org) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 技术委员会 | ISO/TC 299（机器人） | ISO 官网 |
| 核心标准 | ISO 10218-1/-2、ISO/TS 15066、ISO 13482、ISO/TR 20218-1/-2 | ISO/TC 299 |
| 适用范围 | 工业机器人、协作机器人、服务机器人、人形机器人 | ISO 公开资料 |
| 发布状态 | 持续更新/现行 | ISO 官网 |
| 标准语言 | 英文、法文；中文为国家采用版 | ISO |
| 成员国 | 约 30 个参与国 + 观察国 | ISO/TC 299 |
| 价格 | 未公开 | ISO 在线商店 |

**技术亮点**：全球共识制定程序、与 IEC/TC 44 联合、覆盖机器人全生命周期安全，可直接转化为各国国家标准与 CE/UKCA 等法规符合性基础。

**应用场景**：工业机器人安全设计、协作机器人碰撞阈值设定、个人护理机器人风险评估、人形机器人整机与系统集成合规。

## 供应链位置

- **上游关键零部件/材料**：各成员国技术专家、行业联盟、研究机构、测试数据、法规需求
- **下游客户/应用场景**：机器人 OEM、系统集成商、认证机构（TÜV SÜD、SGS、UL）、监管机构、终端用户
- **主要竞争对手/对标**：IEC/TC 44、IEEE SA、ANSI/RIA、CEN/CENELEC、各国标准化机构

## 知识图谱节点与关系

- 公司实体：`ent_company_iso`
- 产品实体：`ent_product_iso_tc299_standards`
- 零部件实体：`ent_component_iso_tc299_standards_core`
- 关键关系：
  - `ent_company_iso` -- `manufactures` --> `ent_product_iso_tc299_standards`
  - `ent_company_iso` -- `manufactures` --> `ent_component_iso_tc299_standards_core`
  - `ent_product_iso_tc299_standards` -- `uses` --> `ent_component_iso_tc299_standards_core`

## 参考资料

1. [ISO 官网](https://www.iso.org)
2. [ISO/TC 299 机器人技术委员会](https://www.iso.org/committee/5915511.html)
3. [附录 D 企业目录](../../../appendices/appendix-d/index-companies.md)
4. [附录 D 产品目录](../../../appendices/appendix-d/index-products.md)
5. 公开行业报告与市场资料
6. 数据更新备注：2026-07-01