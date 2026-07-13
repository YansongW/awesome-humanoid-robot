---
id: ent_company_galbot
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 银河通用
  en: Galbot
status: active
sources:
- id: src_galbot_official
  type: website
  url: https://www.galbot.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 银河通用 / Galbot

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 银河通用机器人 |
| **英文名** | Galbot |
| **总部** | 中国北京 |
| **成立时间** | 2023 年 |
| **官网** | [https://www.galbot.com](https://www.galbot.com) |
| **供应链环节** | 整机 OEM / 轮式双臂人形机器人 |
| **企业属性** | 初创、北大背景、具身智能大模型 |
| **母公司/所属集团** | 无 |
| **数据来源** | Galbot 官网、使用手册、东方财富网、WAIC 报道 |

## 公司简介

银河通用机器人由北大背景团队创立，提出“具身智能大模型 + 轮式人形”路线，以 Galbot G1 为核心产品。

G1 采用 360° 全向轮底盘与可折叠躯干，强调在零售、医疗、工业等结构化场景中的泛化操作能力，并曾与斯坦福大学合作开发 Open6DOR 仿真平台。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 轮式人形 | 零售分拣、家庭服务、医疗辅助 | Galbot G1 | 前置仓、药店、商超、家庭 |
| 服务机器人 | 迎宾、配送 | Galbot S1 | 展厅、医院 |

## 代表产品

### Galbot G1

> Galbot G1：请访问 [官方资料](https://www.galbot.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 标准姿态 173 cm（最高） | Galbot 官网 / 使用手册 |
| 重量 | 约 92.5 kg（整机） | Galbot 使用手册 |
| 自由度 | 24 DOF（不含末端执行器） | Galbot 使用手册 |
| 负载/扭矩 | 单臂末端负载 5 kg，双臂合计 10 kg | Galbot 使用手册 |
| 速度/转速 | 底盘最大 1.5 m/s | Galbot 使用手册 |
| 续航 | 约 8 h（48 V / 30 Ah 电池） | Galbot 使用手册 |
| 接口/通信 | Wi-Fi 2.4/5 GHz、蓝牙 5.2、USB3.0、HDMI | Galbot 使用手册 |
| 价格 | 未公开 | 需询价 |

**技术亮点**：360° 全向轮底盘、躯干升降 65 cm、0–2.1 m 垂直作业空间、NVIDIA AGX Orin 64 GB（275 TOPS）、GroceryVLA 具身大模型。

**应用场景**：无人药店药品分拣、商超货架补货、前置仓拣选、家庭服务。

### Galbot S1

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

**技术亮点**：轮式服务机器人平台，面向迎宾、配送等轻交互场景。

**应用场景**：展厅、医院、办公空间。

## 供应链位置

- **上游关键零部件/材料**：NVIDIA Orin 计算平台、全向轮底盘、谐波/行星减速器、视觉传感器。
- **下游客户/应用场景**：医药零售、商超、三甲医院、工业制造（百达精工等）。
- **主要竞争对手/对标**：智元 A2-W、逐际动力 CL-1、协作机器人 + AMR 组合方案。

## 知识图谱节点与关系

- 公司实体：`ent_company_galbot`
- 产品实体：`ent_product_galbot_g1`
- 关键关系：
  - `ent_company_galbot` -- `manufactures` --> `ent_product_galbot_g1`
  - `ent_product_galbot_g1` -- `uses` --> `ent_component_nvidia_jetson_agx_orin`

## 参考资料

1. [Galbot 官网](https://www.galbot.com)
2. [Galbot G1 产品页](https://www.galbot.com/g1)
3. [Galbot G1 快速使用手册](https://www.robotsj.cn/shiyongshouce/1654.html)
4. [东方财富网 – 银河通用人形机器人布局](https://finance.eastmoney.com/)
5. [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)