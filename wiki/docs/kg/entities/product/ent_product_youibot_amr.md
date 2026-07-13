---
id: ent_product_youibot_amr
type: product
'title:': 优艾智合 L1000 潜伏顶升移动机器人
domain: 04_assembly_integration_testing
theoretical_depth: system
aliases:
- Youibot L1000
- 优艾智合
status: active
created_at: 2026-07-01 00:00:00+00:00
updated_at: 2026-07-09 00:00:00+00:00
sources:
- id: youibot_amr_page
  type: website
  url: https://www.youibot.com
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-09 00:00:00+00:00
---





# youibot_amr

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [优艾智合 / Youibot](../../../appendices/appendix-d/companies/company_youibot.md) |
| **产品类别** | 潜伏顶升移动机器人（AMR） |
| **发布时间** | 未公开 |
| **状态** | 发布/商用 |
| **官网/来源** | [https://www.youibot.com](https://www.youibot.com) |

## 产品概述

Youibot L1000 是优艾智合面向工业物流场景推出的高负载潜伏顶升 AMR，支持 SLAM 激光导航与大规模集群调度。

## 产品图片

> Youibot L1000：请访问 [官方资料](https://www.youibot.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 外形尺寸 | 未公开 | 优艾智合官网 |
| 额定负载 | 1000 kg | 优艾智合官网 |
| 最大速度 | 未公开 | 优艾智合官网 |
| 导航方式 | SLAM 激光导航 | 优艾智合官网 |
| 定位精度 | ± 10 mm | 行业研报 |
| 续航 | 未公开 | 优艾智合官网 |
| 通信接口 | Wi-Fi / 5G / 调度系统 | 优艾智合官网 |
| 价格 | 未公开 | 需询价 |

## 供应链位置

- **制造商**：[优艾智合 / Youibot](../../../appendices/appendix-d/companies/company_youibot.md)
- **核心零部件/技术来源**：自研 SLAM 导航与调度系统；外购激光雷达、伺服电机、电池、控制器、结构件。
- **下游应用/客户**：半导体制造商、汽车 OEM、电力公司、3PL 物流企业。

## 知识图谱节点与关系

- 产品实体：`ent_product_youibot_amr`
- 制造商实体：`ent_company_youibot`
- 关键关系：
  - `rel_ent_company_youibot_manufactures_ent_product_youibot_amr`（`ent_company_youibot` → `manufactures` → `ent_product_youibot_amr`）

## 应用场景

- **半导体晶圆厂物流、汽车线边配送、电子仓储、人形机器人零部件运输。**
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
| 核心优势 | 高负载潜伏顶升设计，支持大规模集群调度与 MES/WMS 系统对接，适用于半导体与汽车物流场景。 | 未公开 |
| 价格 | 未公开 | 未公开 |

## 选购与部署建议

- 建议通过官方渠道确认最新软件版本、SDK 支持与售后培训。
- 科研与教育用户应优先评估二次开发接口、仿真平台兼容性与社区活跃度。
- 工业用户需结合具体工序验证负载、精度、防护等级与集成接口。

## 参考资料

1. [Youibot L1000 产品页](https://www.youibot.com)
2. [优艾智合 官网](https://www.youibot.com)
3. [公开资料与行业研报](https://www.youibot.com)