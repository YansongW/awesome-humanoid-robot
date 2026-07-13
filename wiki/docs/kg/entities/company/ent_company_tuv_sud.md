---
id: ent_company_tuv_sud
type: company
'title:': 南德意志集团 / TÜV SÜD
domain: 04_assembly_integration_testing
theoretical_depth: system
aliases:
- TÜV SÜD
- 南德意志集团
status: active
created_at: 2024-01-15 00:00:00+00:00
updated_at: 2026-07-01 00:00:00+00:00
sources:
- id: ent_company_tuv_sud_official
  type: website
  url: https://www.tuvsud.com
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-01 00:00:00+00:00
  review_notes: Data sourced from official website and public reports; missing specs
    marked as 未公开.
---





# tuv_sud

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 南德意志集团 |
| **英文名** | TÜV SÜD |
| **总部** | 德国慕尼黑 |
| **成立时间** | 1866 |
| **官网** | [https://www.tuvsud.com](https://www.tuvsud.com) |
| **供应链环节** | 机器人检测、安全认证、CE 标志、功能安全评估 |
| **企业属性** | 第三方检测认证机构（TIC）、上市公司 |
| **母公司/所属集团** | TÜV SÜD AG |
| **数据来源** | TÜV SÜD 官网、机器人认证服务页 |

## 公司简介

TÜV SÜD 是全球领先的第三方检测、检验与认证机构之一，在工业机械、汽车、电子电气与医疗设备领域具有悠久历史。其机器人安全认证服务覆盖工业机器人、协作机器人、服务机器人及人形机器人，帮助企业满足欧盟机械指令、CE 标志、功能安全（ISO 13849 / IEC 61508）及市场准入要求。

TÜV SÜD 在全球拥有多个测试实验室，可提供风险评估、型式试验、技术文件审查、现场审核与持续监督等一站式合规服务，是机器人产品进入欧洲及全球高端市场的重要合作伙伴。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 机器人安全认证 | CE 标志、机械指令合规 | [TÜV SÜD 机器人安全认证](../../../appendices/appendix-d/products/product_tuv_sud_robot_certification.md) | 工业机器人、协作机器人、人形机器人 |
| 功能安全评估 | SIL/PL 评估与验证 | ISO 13849 / IEC 61508 服务 | 机器人控制系统、安全部件 |
| 网络安全与可靠性 | IoT/机器人网络风险评估 | IEC 62443 相关服务 | 联网机器人、服务机器人 |

## 代表产品

### TÜV SÜD 机器人安全认证服务

> TÜV SÜD 机器人认证：请访问 [官方资料](https://www.tuvsud.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 服务类型 | 第三方安全认证、检测、审核 | TÜV SÜD 官网 |
| 适用法规 | 欧盟机械指令、CE 标志、UKCA、功能安全 | 公开资料 |
| 适用标准 | ISO 10218、ISO/TS 15066、ISO 13482、ISO 13849、IEC 61508 | TÜV SÜD |
| 测试内容 | 风险评估、型式试验、电磁兼容、技术文件审查 | 公开资料 |
| 服务周期 | 未公开 | 项目制 |
| 认证标志 | TÜV SÜD 标志、CE 符合性 | TÜV SÜD |
| 价格 | 未公开 | 商务报价 |

**技术亮点**：全球测试网络、跨学科安全专家、覆盖机械/电气/软件/网络安全全链路，支持从研发到量产的合规闭环。

**应用场景**：工业机器人出口欧盟、协作机器人 CE 认证、服务机器人市场准入、人形机器人安全评估与型式试验。

## 供应链位置

- **上游关键零部件/材料**：标准文本（ISO/IEC）、测试设备、实验室场地、认证资质、安全专家
- **下游客户/应用场景**：机器人 OEM、零部件供应商、系统集成商、出口贸易商、监管机构
- **主要竞争对手/对标**：SGS、UL Solutions、Intertek、DEKRA、Bureau Veritas

## 知识图谱节点与关系

- 公司实体：`ent_company_tuv_sud`
- 产品实体：`ent_product_tuv_sud_robot_certification`
- 零部件实体：`ent_component_tuv_sud_robot_certification_core`
- 关键关系：
  - `ent_company_tuv_sud` -- `manufactures` --> `ent_product_tuv_sud_robot_certification`
  - `ent_company_tuv_sud` -- `manufactures` --> `ent_component_tuv_sud_robot_certification_core`
  - `ent_product_tuv_sud_robot_certification` -- `uses` --> `ent_component_tuv_sud_robot_certification_core`

## 参考资料

1. [TÜV SÜD 官网](https://www.tuvsud.com)
2. [TÜV SÜD 产品认证服务](https://www.tuvsud.com/en/services/product-certification)
3. [附录 D 企业目录](../../../appendices/appendix-d/index-companies.md)
4. 公开行业报告与市场资料
5. 数据更新备注：2026-07-01