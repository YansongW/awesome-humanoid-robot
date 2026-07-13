# SGS 机器人检测认证服务 / SGS Robotics Testing and Certification Service

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [SGS / 瑞士通用公证行](../companies/company_sgs.md) |
| **产品类别** | 机器人检测、认证与市场准入服务 |
| **发布时间** | 持续提供 |
| **状态** | 商用/项目制 |
| **官网/来源** | [SGS 官网](https://www.sgs.com) |

## 产品概述

SGS 机器人检测认证服务面向工业机器人、协作机器人、服务机器人及人形机器人全生命周期，提供电气安全、机械安全、电磁兼容、无线射频、功能安全、软件与网络安全、环境可靠性及全球市场准入认证。服务覆盖研发阶段预测试、正式认证、工厂审核与持续监督，帮助客户缩短上市周期并降低合规风险。

## 产品图片

> SGS 机器人检测认证：请访问 [官方资料](https://www.sgs.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 服务类型 | 检测、认证、验证、审核、培训 | SGS 官网 |
| 适用机器人 | 工业、协作、服务、人形机器人 | 公开资料 |
| 适用法规 | CE、UKCA、FCC、IC、VCCI、CCC 等 | SGS |
| 适用标准 | ISO 10218、ISO/TS 15066、ISO 13482、IEC 61508、ISO 13849、IEC 60204、IEC 62443 | 公开资料 |
| 测试内容 | 电气安全、机械安全、EMC、无线、功能安全、环境可靠性、网络安全 | SGS |
| 服务周期 | 未公开 | 项目制 |
| 认证标志 | SGS 标志、CE、CB、NRTL 等 | SGS |
| 价格 | 未公开 | 商务报价 |
| 全球网络 | 欧洲、亚太、北美、拉美多地实验室 | SGS 官网 |

## 供应链位置

- **制造商**：[SGS / 瑞士通用公证行](../companies/company_sgs.md)
- **核心零部件/技术来源**：国际标准文本、测试仪器、认证资质、功能安全与网络安全专家团队
- **下游应用/客户**：机器人 OEM、零部件供应商、系统集成商、跨境贸易商、零售商

## 知识图谱节点与关系

- 产品实体：`ent_product_sgs_robotics_testing`
- 零部件实体：`ent_component_sgs_robotics_testing_core`
- 制造商实体：`ent_company_sgs`
- 关键关系：
  - `rel_ent_company_sgs_manufactures_ent_product_sgs_robotics_testing`（`ent_company_sgs` → `manufactures` → `ent_product_sgs_robotics_testing`）
  - `rel_ent_company_sgs_manufactures_ent_component_sgs_robotics_testing_core`（`ent_company_sgs` → `manufactures` → `ent_component_sgs_robotics_testing_core`）
  - `rel_ent_product_sgs_robotics_testing_uses_ent_component_sgs_robotics_testing_core`（`ent_product_sgs_robotics_testing` → `uses` → `ent_component_sgs_robotics_testing_core`）

## 应用场景

- **消费级机器人上市**：扫地机器人、教育机器人等的电气/EMC/无线认证。
- **工业机器人出口**：CE、UKCA、北美市场准入与合规文件支持。
- **协作机器人安全验证**：ISO/TS 15066 与 ISO 10218 差距分析与测试。
- **人形机器人全链合规**：从关节、控制器到整机的安全、功能安全与网络安全评估。

## 竞争对比

| 对比项 | 本产品 | 主要竞品 A | 主要竞品 B |
|--------|--------|------------|------------|
| 机构 | SGS | TÜV SÜD | UL Solutions |
| 优势区域 | 全球消费品、跨境贸易 | 德国/欧洲汽车与工业 | 北美安全标志 |
| 特色 | 全品类、全球网络最广 | 功能安全深度 | UL 标志权威性 |

## 选购与部署建议

- 根据目标市场提前规划认证路径，避免重复测试。
- 利用 SGS 预测试服务在设计阶段发现潜在合规问题。
- 准备完整 BOM、电路图、风险分析与软件文档以加速认证。

## 相关词条

- [制造商：SGS / 瑞士通用公证行](../companies/company_sgs.md)
- [附录 D.4 重点产品 Wiki](../index-products.md)

## 参考资料

1. [SGS 官网](https://www.sgs.com)
2. [SGS 服务目录](https://www.sgs.com)
3. SGS 公开服务手册
4. [附录 D 企业目录](../index-companies.md)