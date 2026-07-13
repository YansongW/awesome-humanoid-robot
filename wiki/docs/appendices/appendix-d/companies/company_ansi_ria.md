# 美国国家标准学会/机器人工业协会 / ANSI/RIA

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 美国国家标准学会 / 机器人工业协会 |
| **英文名** | ANSI / Robotics Industries Association (RIA, now A3) |
| **总部** | ANSI：美国华盛顿特区；RIA/A3：美国密歇根州安娜堡 |
| **成立时间** | ANSI 1918；RIA 1974（2019 年并入 A3） |
| **官网** | [https://www.ansi.org](https://www.ansi.org)、[https://www.a3.org](https://www.a3.org) |
| **供应链环节** | 美国机器人安全标准、行业培训、认证协调 |
| **企业属性** | ANSI 为非营利标准协调机构；RIA/A3 为行业协会 |
| **母公司/所属集团** | 无（ANSI 独立；A3 为行业协会） |
| **数据来源** | ANSI 官网、A3/RIA 官网、R15.06 标准页 |

## 公司简介

ANSI 负责协调美国自愿性标准与合格评定体系，并代表美国参与 ISO/IEC 标准活动。RIA（现 A3 机器人分会）是美国领先的机器人行业协会，长期主导工业机器人安全标准的制定与推广。

ANSI/RIA R15.06 是美国最重要的工业机器人安全标准，与国际标准 ISO 10218-1/-2 协调一致，被 OSHA、NFPA 及美国各州法规广泛引用，是工业机器人进入美国市场的关键合规依据。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 机器人安全标准 | 北美工业机器人安全要求 | [ANSI/RIA R15.06](../products/product_ansi_ria_r15_06.md) | 工业机器人、协作机器人、集成系统 |
| 行业认证与培训 | CMRA 认证机器人集成商等 | RIA 认证课程 | 系统集成商、终端用户 |
| 市场研究与活动 | 行业统计与展会 | A3 商业论坛 | 机器人产业链 |

## 代表产品

### ANSI/RIA R15.06 工业机器人安全标准

> ANSI/RIA R15.06：请访问 [官方资料](https://www.ansi.org) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 标准编号 | ANSI/RIA R15.06-2012 | ANSI/A3 |
| 对应国际标准 | ISO 10218-1:2011 / ISO 10218-2:2011 | ANSI 采用说明 |
| 适用范围 | 工业机器人、机器人系统、集成应用 | R15.06 |
| 发布状态 | 现行/持续维护 | ANSI/A3 |
| 技术内容 | 安全设计、安装、操作、维护、风险评估 | 公开资料 |
| 价格 | 未公开 | ANSI/A3 商店 |
| 认证属性 | 被美国法规与保险体系广泛引用 | ANSI/A3 |

**技术亮点**：与 ISO 10218 协调一致，覆盖机器人本体、机器人系统与集成应用，强调危险识别、安全距离与防护装置。

**应用场景**：汽车焊接/涂装机器人产线、协作机器人工作站、码垛/搬运系统集成、人形机器人工业场景落地。

## 供应链位置

- **上游关键零部件/材料**：ANSI 技术委员会、RIA/A3 会员企业、ISO/TC 299 输入、事故与测试数据
- **下游客户/应用场景**：北美机器人 OEM、系统集成商、终端制造商、保险公司、监管机构
- **主要竞争对手/对标**：ISO/TC 299、IEEE SA、CSA Z434、EN ISO 10218

## 知识图谱节点与关系

- 公司实体：`ent_company_ansi_ria`
- 产品实体：`ent_product_ansi_ria_r15_06`
- 零部件实体：`ent_component_ansi_ria_r15_06_core`
- 关键关系：
  - `ent_company_ansi_ria` -- `manufactures` --> `ent_product_ansi_ria_r15_06`
  - `ent_company_ansi_ria` -- `manufactures` --> `ent_component_ansi_ria_r15_06_core`
  - `ent_product_ansi_ria_r15_06` -- `uses` --> `ent_component_ansi_ria_r15_06_core`

## 参考资料

1. [ANSI 官网](https://www.ansi.org)
2. [A3 官网](https://www.a3.org)
3. [ANSI/RIA R15.06 标准页](https://webstore.ansi.org/standards/ria/ansiriar15062012)
4. [附录 D 企业目录](../index-companies.md)
5. 公开行业报告与市场资料
6. 数据更新备注：2026-07-01