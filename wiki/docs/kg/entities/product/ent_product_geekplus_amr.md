---
id: ent_product_geekplus_amr
type: product
'title:': 极智嘉 P800 拣选机器人
domain: 04_assembly_integration_testing
theoretical_depth: system
aliases:
- Geek+ P800
- 极智嘉
status: active
created_at: 2026-07-01 00:00:00+00:00
updated_at: 2026-07-09 00:00:00+00:00
sources:
- id: geekplus_amr_page
  type: website
  url: https://www.geekplus.com/picking-robots
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-09 00:00:00+00:00
---





# geekplus_amr

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [极智嘉 / Geek+](../../../appendices/appendix-d/companies/company_geekplus.md) |
| **产品类别** | 货到人拣选机器人（AMR） |
| **发布时间** | 未公开 |
| **状态** | 发布/商用 |
| **官网/来源** | [https://www.geekplus.com](https://www.geekplus.com) |

## 产品概述

Geek+ P800 是极智嘉货到人拣选方案的核心移动机器人，可搬运标准货架至拣选工位，提升仓储拣选效率。

## 产品图片

> Geek+ P800：请访问 [官方资料](https://www.geekplus.com/picking-robots) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 外形尺寸 | 未公开 | 极智嘉官网 |
| 额定负载 | 800 kg（货架+货物） | 极智嘉官网 |
| 最大速度 | 未公开 | 极智嘉官网 |
| 导航方式 | SLAM 激光导航 / 二维码 | 极智嘉官网 |
| 定位精度 | ± 10 mm | 行业研报 |
| 续航 | 未公开 | 极智嘉官网 |
| 通信接口 | Wi-Fi / 5G / 机器人管理系统 | 极智嘉官网 |
| 价格 | 未公开 | 需询价 |

## 供应链位置

- **制造商**：[极智嘉 / Geek+](../../../appendices/appendix-d/companies/company_geekplus.md)
- **核心零部件/技术来源**：自研导航算法与机器人管理系统；外购激光雷达、伺服电机、电池、控制器、结构件。
- **下游应用/客户**：电商企业、零售商、医药企业、3PL、制造企业。

## 知识图谱节点与关系

- 产品实体：`ent_product_geekplus_amr`
- 制造商实体：`ent_company_geekplus`
- 关键关系：
  - `rel_ent_company_geekplus_manufactures_ent_product_geekplus_amr`（`ent_company_geekplus` → `manufactures` → `ent_product_geekplus_amr`）

## 应用场景

- **电商仓储、零售配送中心、医药物流、人形机器人零部件与整机仓储物流。**
- **商业服务**：用于导览、接待、展示与品牌互动。
- **工业制造**：在柔性产线执行搬运、装配、检测等任务。
- **科研教育**：作为机器人控制、AI 训练与具身智能研究的硬件平台。

## 扩展与生态

- 制造商提供官方 SDK、仿真工具与售后培训，具体细节需通过官方渠道确认。
- 可与主流 MES/WMS/PLC 系统对接，但接口协议需以官方文档为准。
- 建议部署前进行场景化验证与兼容性测试。

## 竞争对比

| 对比项 | 本产品 | 主要竞品 |
|--------|--------|----------|
| 定位 | 未公开 | 同类产品视具体场景而定 |
| 核心优势 | 货到人拣选方案，可提升仓储拣选效率 2–3 倍；支持大规模集群调度与多品牌设备混跑。 | 未公开 |
| 价格 | 未公开 | 未公开 |

## 选购与部署建议

- 建议通过官方渠道确认最新软件版本、SDK 支持与售后培训。
- 科研与教育用户应优先评估二次开发接口、仿真平台兼容性与社区活跃度。
- 工业用户需结合具体工序验证负载、精度、防护等级与集成接口。

## 参考资料

1. [Geek+ P800 产品页](https://www.geekplus.com/picking-robots)
2. [极智嘉 官网](https://www.geekplus.com)
3. [公开资料与行业研报](https://www.geekplus.com)