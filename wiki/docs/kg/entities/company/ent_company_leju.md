---
id: ent_company_leju
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 乐聚机器人
  en: Leju Robotics
status: active
sources:
- id: src_leju_official
  type: website
  url: https://www.lejurobot.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 乐聚机器人 / Leju Robotics

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 乐聚机器人 |
| **英文名** | Leju Robotics |
| **总部** | 中国深圳（创始团队来自哈尔滨工业大学） |
| **成立时间** | 2016 年 |
| **官网** | [https://www.lejurobot.com](https://www.lejurobot.com) |
| **供应链环节** | 整机 OEM / 开源鸿蒙人形机器人 |
| **企业属性** | 哈工大背景、开源生态、华为合作伙伴 |
| **母公司/所属集团** | 无 |
| **数据来源** | 乐聚官网、IT之家、36氪、机器人在线 |

## 公司简介

乐聚机器人由哈尔滨工业大学博士冷晓琨创立，聚焦高动态人形机器人与产业化。

公司与深开鸿合作推出国内首款基于开源鸿蒙（KaihongOS）的高动态人形机器人 KUAVO（夸父），强调“开箱即用”的科研平台和国产化供应链。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 高动态人形 | 科研、服务、工业协作 | KUAVO 4 / 4 Pro | 科研教育、展厅、工业 |
| 服务人形 | 导览、互动 | KUAVO MY | 展厅、商超、银行 |

## 代表产品

### KUAVO 4 Pro

> 乐聚 KUAVO 4 Pro：请访问 [官方资料](https://www.lejurobot.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 166 cm | aixzd.com / IT之家 |
| 重量 | 55 kg | aixzd.com |
| 自由度 | 30 DOF | IT之家 |
| 负载/扭矩 | 单腿峰值扭矩 220 N·m | 小熊 AI 网 |
| 速度/转速 | 行走 5 km/h | aixzd.com |
| 续航 | 约 1 h（6 Ah 电池） | aixzd.com |
| 接口/通信 | Wi-Fi、KaihongOS、ROS | 公开报道 |
| 价格 | 未公开 | 需询价 |

**技术亮点**：开源鸿蒙 KaihongOS、三段式躯干设计、Gemini-335L 双目深度相机、mid-360 激光雷达、NVIDIA Orin-NX 上位机。

**应用场景**：科研平台、展厅导览、商业服务、工业协作搬运。

### KUAVO（初代）

> 乐聚 KUAVO：请访问 [官方资料](https://www.lejurobot.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 未公开 | - |
| 重量 | 约 45 kg | 36氪 / 机器人在线 |
| 自由度 | 26 DOF | 机器人在线 |
| 负载/扭矩 | 未公开 | - |
| 速度/转速 | 最高 4.6 km/h；连续跳跃 >20 cm | 36氪 |
| 续航 | 未公开 | - |
| 接口/通信 | 开源鸿蒙、SDK、仿真平台 | IT之家 |
| 价格 | 约数十万元 | 36氪 |

**技术亮点**：国内首款可跳跃、可适应多地形行走的开源鸿蒙人形机器人，运动控制器开源。

**应用场景**：教育科研、特种服务、家庭服务前期验证。

## 供应链位置

- **上游关键零部件/材料**：深开鸿 KaihongOS、奥比中光深度相机、禾赛/览沃激光雷达、国产电机与减速器。
- **下游客户/应用场景**：高校、华为生态展厅、银行、工厂。
- **主要竞争对手/对标**：宇树 G1、傅利叶 GR-1、智元 A2。

## 知识图谱节点与关系

- 公司实体：`ent_company_leju`
- 产品实体：`ent_product_leju_kuavo_4pro`、`ent_product_leju_kuavo`
- 关键关系：
  - `ent_company_leju` -- `manufactures` --> `ent_product_leju_kuavo_4pro`
  - `ent_company_leju` -- `manufactures` --> `ent_product_leju_kuavo`
  - `ent_product_leju_kuavo_4pro` -- `uses` --> `ent_component_orbbec_gemini335`

## 参考资料

1. [乐聚机器人官网](https://www.lejurobot.com)
2. [IT之家 – 乐聚 KUAVO 科研版发布](https://www.ithome.com/0/800/849.htm)
3. [36氪 – 乐聚发布 KUAVO](https://so.html5.qq.com/page/real/search_news?docid=70000021_145656eac9b02752)
4. [aixzd.com – KUAVO 4 Pro 介绍](https://aixzd.com/robot/kuavo-4pro)
5. [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)