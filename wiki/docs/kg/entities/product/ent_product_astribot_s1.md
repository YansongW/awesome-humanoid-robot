---
id: ent_product_astribot_s1
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: Astribot S1
  en: Astribot S1
status: active
sources:
- id: src_astribot_s1_official
  type: website
  url: https://www.astribot.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# Astribot S1 / Astribot S1

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [星尘智能 / Astribot](../../../appendices/appendix-d/companies/company_astribot.md) |
| **产品类别** | 通用人形机器人 |
| **发布时间** | 2024 年 8 月 |
| **状态** | 量产/商用 |
| **官网/来源** | [https://www.astribot.com](https://www.astribot.com) |

## 产品概述

叠衣、炒菜、清洁、书法、泡功夫茶、科研实验、养老陪护、新零售展示。

Astribot S1 是 星尘智能 的代表产品。绳驱传动、±0.1 mm 重复定位精度、100 m/s² 末端加速度、力控安全、VR 遥操作与零代码可视化界面。主要规格包括：170 cm（高）（尺寸）、80 kg（重量）、全身 23 DOF（单臂 7 DOF×2，躯干 4 DOF，头部 2 DOF，全向轮式底盘 3 DOF）（自由度）。

## 产品图片

![Astribot S1](https://cdn.shopify.com/s/files/1/0659/1437/2184/files/Astribot_image_1_resized.png?v=1768350773&width=800)


## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 170 cm（高） | Astribot 官网 |
| 重量 | 80 kg | Astribot 官网 |
| 自由度 | 全身 23 DOF（单臂 7 DOF×2，躯干 4 DOF，头部 2 DOF，全向轮式底盘 3 DOF） | Astribot 官网 / 技术文档 |
| 负载/扭矩 | 单臂水平伸展额定负载 5 kg，峰值 10 kg | Astribot 官网 |
| 速度/转速 | 末端最高速度 ≥10 m/s | Astribot 官网 |
| 续航 | 4–6 小时（支持插电） | Astribot 官网 |
| 接口/通信 | ROS 2 / Python SDK、Gigabit Ethernet、Wi-Fi | 技术文档 |
| 价格 | 科研版约 ¥50 万；企业/科研级约 $96,000–$150,000 | 公开报道 |

## 供应链位置

- **制造商**：[星尘智能 / Astribot](../../../appendices/appendix-d/companies/company_astribot.md)
- **核心零部件/技术来源**：自研绳驱执行器、高性能电机、力/扭矩传感器、计算平台；外购相机、激光雷达、电池。
- **下游应用/客户**：叠衣、炒菜、清洁、书法、泡功夫茶、科研实验、养老陪护、新零售展示。

## 知识图谱节点与关系

- 产品实体：`ent_product_astribot_s1`
- 制造商实体：`ent_company_astribot`
- 关键关系：
  - `rel_ent_company_astribot_manufactures_ent_product_astribot_s1`（`ent_company_astribot` → `manufactures` → `ent_product_astribot_s1`）
  - `ent_product_astribot_s1` -- `uses` --> `ent_component_astribot_cable_actuator`

## 应用场景

- **叠衣、炒菜、清洁、书法、泡功夫茶、科研实验、养老陪护、新零售展示。**

## 竞争对比

| 对比项 | 本产品 | 主要竞品 |
|--------|--------|----------|
| 定位 | 通用人形机器人 | 同类产品视具体场景而定 |
| 核心优势 | 绳驱传动、±0.1 mm 重复定位精度、100 m/s² 末端加速度、力控安全、VR 遥操作与零代码可视化界面 | 未公开 |
| 价格 | 科研版约 ¥50 万；企业/科研级约 $96,000–$150,000 | 未公开 |

## 选购与部署建议

- 建议通过官方渠道确认最新软件版本、SDK 支持与售后培训。
- 科研与教育用户应优先评估二次开发接口、仿真平台兼容性与社区活跃度。
- 工业用户需结合具体工序验证负载、精度、防护等级与集成接口。

## 参考资料

1. [Astribot 官网产品页](https://www.astribot.com/en/product)
2. [RobotScope – Astribot 公司资料](https://robotscope.net/companies/astribot/)
3. [百度百科 – Astribot S1](https://baike.baidu.com/item/Astribot%20S1/64813493)