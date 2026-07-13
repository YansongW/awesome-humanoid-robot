---
id: ent_product_yaskawa_motoman
type: product
'title:': Yaskawa MOTOMAN HC20DTP 协作机器人
domain: 04_assembly_integration_testing
theoretical_depth: system
aliases:
- MOTOMAN HC20DTP
- Yaskawa
status: active
created_at: 2026-07-01 00:00:00+00:00
updated_at: 2026-07-09 00:00:00+00:00
sources:
- id: yaskawa_motoman_page
  type: website
  url: https://www.yaskawa.com/products/robotics/collaborative-robots/motoman-hc20dtp
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-09 00:00:00+00:00
---





# yaskawa_motoman

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [安川电机 / Yaskawa Electric Corporation](../../../appendices/appendix-d/companies/company_yaskawa.md) |
| **产品类别** | 六轴协作机器人 |
| **发布时间** | 未公开 |
| **状态** | 发布/商用 |
| **官网/来源** | [https://www.yaskawa.com](https://www.yaskawa.com) |

## 产品概述

MOTOMAN HC20DTP 是安川电机推出的高负载协作机器人，支持 20 kg 负载与 IP67 手腕防护，可在高卫生标准与恶劣环境下实现人机协作。

## 产品图片

> MOTOMAN HC20DTP：请访问 [官方资料](https://www.yaskawa.com/products/robotics/collaborative-robots/motoman-hc20dtp) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 轴数 | 6 | Yaskawa 官网 |
| 最大负载 | 20 kg | Yaskawa 官网 |
| 最大工作半径 | 1900 mm | Yaskawa 官网 |
| 重复定位精度 | ± 0.05 mm | Yaskawa 官网 |
| 机械单元重量 | 未公开 | Yaskawa 官网 |
| 防护等级 | IP67（手腕）/ IP54（本体） | Yaskawa 官网 |
| 安装方式 | 地面 / 倒挂 | Yaskawa 官网 |
| 价格 | 未公开 | 需询价 |

## 供应链位置

- **制造商**：[安川电机 / Yaskawa Electric Corporation](../../../appendices/appendix-d/companies/company_yaskawa.md)
- **核心零部件/技术来源**：自研伺服驱动、控制器与运动控制算法；外购减速器、电机、编码器、结构件。
- **下游应用/客户**：汽车 OEM、食品与饮料、电子制造、物流仓储、自动化集成商。

## 知识图谱节点与关系

- 产品实体：`ent_product_yaskawa_motoman`
- 制造商实体：`ent_company_yaskawa`
- 关键关系：
  - `rel_ent_company_yaskawa_manufactures_ent_product_yaskawa_motoman`（`ent_company_yaskawa` → `manufactures` → `ent_product_yaskawa_motoman`）

## 应用场景

- **食品加工、包装、机床上下料、人形机器人零部件装配与检测。**
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
| 核心优势 | 高负载协作能力、食品级润滑可选、IP67 手腕防护，适合高卫生标准与恶劣环境下的协作作业。 | 未公开 |
| 价格 | 未公开 | 未公开 |

## 选购与部署建议

- 建议通过官方渠道确认最新软件版本、SDK 支持与售后培训。
- 科研与教育用户应优先评估二次开发接口、仿真平台兼容性与社区活跃度。
- 工业用户需结合具体工序验证负载、精度、防护等级与集成接口。

## 参考资料

1. [MOTOMAN HC20DTP 产品页](https://www.yaskawa.com/products/robotics/collaborative-robots/motoman-hc20dtp)
2. [安川电机 官网](https://www.yaskawa.com)
3. [公开资料与行业研报](https://www.yaskawa.com)