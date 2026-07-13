---
id: ent_company_sgs
type: company
'title:': 瑞士通用公证行 / SGS S.A.
domain: 04_assembly_integration_testing
theoretical_depth: system
aliases:
- SGS S.A.
- 瑞士通用公证行
status: active
created_at: 2024-01-15 00:00:00+00:00
updated_at: 2026-07-01 00:00:00+00:00
sources:
- id: ent_company_sgs_official
  type: website
  url: https://www.sgs.com
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-01 00:00:00+00:00
  review_notes: Data sourced from official website and public reports; missing specs
    marked as 未公开.
---





# sgs

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 瑞士通用公证行 |
| **英文名** | SGS S.A. |
| **总部** | 瑞士日内瓦 |
| **成立时间** | 1878 |
| **官网** | [https://www.sgs.com](https://www.sgs.com) |
| **供应链环节** | 机器人检测、认证、验证、功能安全、全球市场准入 |
| **企业属性** | 第三方检测认证机构（TIC）、上市公司 |
| **母公司/所属集团** | SGS S.A.（SIX 瑞士交易所上市） |
| **数据来源** | SGS 官网、机器人测试服务页 |

## 公司简介

SGS 是全球最大的检验、鉴定、测试与认证机构之一，业务覆盖农业、工业、消费品与生命科学等领域。在机器人产业，SGS 提供从原材料、零部件到整机系统的测试、认证与功能安全评估服务，支持制造商进入欧盟、北美、亚太等全球市场。

SGS 的机器人服务涵盖电气安全、机械安全、电磁兼容、无线射频、功能安全、软件评估与网络安全，并可提供工厂审核、供应链验证与培训，是机器人产业链中关键的合规与质量守门人。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 机器人测试与认证 | 整机与零部件合规 | [SGS 机器人检测认证服务](../../../appendices/appendix-d/products/product_sgs_robotics_testing.md) | 工业机器人、协作机器人、服务机器人、人形机器人 |
| 功能安全服务 | SIL/PL 评估 | IEC 61508 / ISO 13849 服务 | 机器人控制器、安全系统 |
| 供应链与体系认证 | ISO 9001/14001/45001 | 管理体系认证 | 机器人制造与集成商 |

## 代表产品

### SGS 机器人检测认证服务

> SGS 机器人检测认证：请访问 [官方资料](https://www.sgs.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 服务类型 | 检测、认证、验证、审核 | SGS 官网 |
| 适用法规 | CE、UKCA、FCC、IC、VCCI、CCC 等 | 公开资料 |
| 适用标准 | ISO 10218、ISO/TS 15066、ISO 13482、IEC 61508、ISO 13849、IEC 60204 | SGS |
| 测试内容 | 电气安全、机械安全、EMC、无线、功能安全、环境可靠性 | 公开资料 |
| 服务周期 | 未公开 | 项目制 |
| 认证标志 | SGS 标志、CE、CB、北美 NRTL 等 | SGS |
| 价格 | 未公开 | 商务报价 |

**技术亮点**：全球最大 TIC 网络之一、跨行业经验、可提供从研发到量产的全链条合规与质量服务。

**应用场景**：消费级机器人 FCC/CE 认证、工业机器人出口、协作机器人安全验证、人形机器人整机合规与供应链审核。

## 供应链位置

- **上游关键零部件/材料**：国际标准、检测设备、全球实验室网络、认证资质、行业专家
- **下游客户/应用场景**：机器人 OEM、零部件供应商、贸易商、零售商、监管机构
- **主要竞争对手/对标**：TÜV SÜD、UL Solutions、Intertek、Bureau Veritas、DEKRA

## 知识图谱节点与关系

- 公司实体：`ent_company_sgs`
- 产品实体：`ent_product_sgs_robotics_testing`
- 零部件实体：`ent_component_sgs_robotics_testing_core`
- 关键关系：
  - `ent_company_sgs` -- `manufactures` --> `ent_product_sgs_robotics_testing`
  - `ent_company_sgs` -- `manufactures` --> `ent_component_sgs_robotics_testing_core`
  - `ent_product_sgs_robotics_testing` -- `uses` --> `ent_component_sgs_robotics_testing_core`

## 参考资料

1. [SGS 官网](https://www.sgs.com)
2. [SGS 服务目录](https://www.sgs.com)
3. [附录 D 企业目录](../../../appendices/appendix-d/index-companies.md)
4. 公开行业报告与市场资料
5. 数据更新备注：2026-07-01