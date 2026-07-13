---
id: ent_company_casbot
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 灵宝 CASBOT
  en: CASBOT
status: active
sources:
- id: src_casbot_official
  type: website
  url: https://www.casbot.tech
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 灵宝 CASBOT / CASBOT

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 灵宝 CASBOT |
| **英文名** | CASBOT |
| **总部** | 中国北京 |
| **成立时间** | 2023 年 |
| **官网** | [https://www.casbot.tech](https://www.casbot.tech) |
| **供应链环节** | 整机 OEM / 通用类脑智能机器人 |
| **企业属性** | 中科院/清华/北理工背景、联想投资 |
| **母公司/所属集团** | 北京中科慧灵机器人技术有限公司 |
| **数据来源** | Casbot 官网、IT之家、雷峰网、CES 公开报道 |

## 公司简介

灵宝 CASBOT 是北京中科慧灵旗下人形机器人品牌，团队来自中国科学院、清华大学、北京理工大学等机构。

公司提出“以终为始，生而为人”，强调 CASBOT 01 的类脑智能与多场景落地能力，已在航天航海、应急救援、井下作业、工业制造和商业服务等领域建立合作。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 通用类人形 | 多场景通用操作 | CASBOT 01 | 家庭服务、工业制造、应急救援 |

## 代表产品

### CASBOT 01

> 灵宝 CASBOT 01：请访问 [官方资料](https://www.casbot.tech) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 179 cm | IT之家 / 雷峰网 |
| 重量 | 60 kg | IT之家 / 雷峰网 |
| 自由度 | 52 DOF | IT之家 |
| 负载/扭矩 | 单手额定负载 5 kg；五指仿生灵巧手重 800 g | IT之家 |
| 速度/转速 | 未公开 | - |
| 续航 | >4 h（双电池，支持 30 分钟快充） | IT之家 |
| 接口/通信 | Wi-Fi 6E / 5G | Casbot 官网 |
| 价格 | 未公开 | 需询价 |

**技术亮点**：自研行星/谐波/直线一体化关节（峰值扭矩密度 207 N·m/kg）、端到端多模态灵巧操作大模型、头部雷达+相机+显示屏、快拆背包式电池。

**应用场景**：整理衣物、组装台灯、更换灯泡、工业打螺丝、家庭管家。

### CASBOT 01 工业版（规划）

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 未公开 | - |
| 重量 | 未公开 | - |
| 自由度 | 未公开 | - |
| 负载/扭矩 | 未公开 | - |
| 速度/转速 | 未公开 | - |
| 续航 | 未公开 | - |
| 接口/通信 | 未公开 | - |
| 价格 | 未公开 | 需询价 |

**技术亮点**：面向智能制造场景优化，计划部署于联想等合作伙伴工厂产线。

**应用场景**：产线上下料、精密装配、质量检测。

## 供应链位置

- **上游关键零部件/材料**：自研一体化关节，外购高强度金属、电池、计算平台、视觉传感器。
- **下游客户/应用场景**：联想智能制造工厂、航天航海、应急救援、井下作业。
- **主要竞争对手/对标**：优必选 Walker、傅利叶 GR-1、智元 A2。

## 知识图谱节点与关系

- 公司实体：`ent_company_casbot`
- 产品实体：`ent_product_casbot_01`
- 关键关系：
  - `ent_company_casbot` -- `manufactures` --> `ent_product_casbot_01`
  - `ent_product_casbot_01` -- `uses` --> `ent_component_casbot_integrated_joint`

## 参考资料

1. [灵宝 CASBOT 官网](https://www.casbot.tech)
2. [IT之家 – CASBOT 01 发布](https://www.ithome.com/0/810/472.htm)
3. [雷峰网 – CASBOT 01 发布](https://www.leiphone.com/category/robot/Gy0hnPSsUSGhp64Y.html)
4. [PR Newswire – CASBOT 亮相 CES 2025](https://hk.prnasia.com/story/475468-1.shtml)
5. [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)