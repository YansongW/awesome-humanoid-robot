---
id: ent_company_dobot
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 越疆科技
  en: Dobot / Yuejiang Technology
status: active
sources:
- id: src_dobot_official
  type: website
  url: https://www.dobot.cn
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 越疆科技 / Dobot / Yuejiang Technology

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 越疆科技 |
| **英文名** | Dobot / Yuejiang Technology |
| **总部** | 中国广东深圳 |
| **成立时间** | 2015 年 |
| **官网** | [https://www.dobot.cn](https://www.dobot.cn) |
| **供应链环节** | 整机 OEM / 协作机器人 + 人形机器人 + 遥操作训练平台 |
| **企业属性** | 协作机器人龙头向具身智能延伸 |
| **母公司/所属集团** | 无 |
| **数据来源** | 越疆官网、Dobot X-Trainer 用户手册与宣传册、36 氪 |

## 公司简介

越疆科技以协作机器人起家，逐步进入具身智能机器人、遥操作数据训练平台与人形机器人领域。

越疆拥有 CRA、CR、Nova、MG400、X-Trainer、Magician 等协作与教育机器人产品线，累计出货量行业领先。2024 年起推出 X-Trainer 双臂遥操作 AI 训练平台，面向科研与数据采集团队；2025 年发布工业人形机器人 ATOM-M，布局汽车、电子、半导体等柔性制造场景。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 协作机器人 | 工业、商业、教育 | CRA / CR / Nova / MG400 | 3C、汽车、科研教育 |
| 具身智能与人形 | 遥操作训练、工业人形 | X-Trainer / ATOM-M | 数据采集、汽车电子柔性产线 |

## 代表产品

### Dobot X-Trainer

![Dobot X-Trainer](https://www.dobot-robots.com/media/upload/2024/x-trainer/tab.png)


| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 底座 1400×1000 mm（轻量版，不含把手） | Dobot X-Trainer 用户手册 |
| 重量 | 未公开 | - |
| 自由度 | 主手 6-DOF×2，从手 Nova 2 协作臂×2 | 用户手册 |
| 负载/扭矩 | 单臂可搬 2 kg，双臂 3 kg；夹爪最大行程 95 mm | 宣传册 |
| 速度/转速 | 末端最高速度 1.6 m/s | 宣传册 |
| 续航 | 市电供电 | - |
| 接口/通信 | 千兆网口、USB、WiFi（Nova 2 选配） | 用户手册 |
| 价格 | 未公开 | 需询价 |

**技术亮点**：工业级 Nova 2 协作臂从手、±0.05 mm 重复定位精度、25 Hz 端到端运动接口、VR/手柄遥操作、数据采集 SDK

**应用场景**：具身智能数据采集、模仿学习、科研教育、AGI 场景仿真与竞赛。

### Dobot ATOM-M

> Dobot ATOM-M：请访问 [官方资料](https://www.dobot.cn) 查看。

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

**技术亮点**：轮式人形一体化全身控制、手-眼-脚协同、双臂高精度操作，适配汽车/电子/半导体多品种小批量柔性生产

**应用场景**：柔性制造、无人化车间搬运与装配。

## 供应链位置

- **上游关键零部件/材料**：自研协作机器人关节、电机、减速器、控制器；Intel RealSense D405 深度相机；NVIDIA Jetson 算力平台。
- **下游客户/应用场景**：高校科研、工业数据采集团队、汽车/电子/半导体制造商。
- **主要竞争对手/对标**：优傲 UR、Fanuc、遨博、节卡、大族机器人

## 知识图谱节点与关系

- 公司实体：`ent_company_dobot`
- 产品实体：`ent_product_dobot_x_trainer`
- 零部件实体：`ent_component_dobot_nova2`
- 关键关系：
  - `ent_company_dobot` -- `manufactures` --> `ent_product_dobot_x_trainer`
  - `ent_company_dobot` -- `manufactures` --> `ent_component_dobot_nova2`
  - `ent_product_dobot_x_trainer` -- `uses` --> `ent_component_dobot_nova2`

## 参考资料

1. [Dobot X-Trainer 产品页](https://www.dobot-robots.com/products/humanoid-robots/x-trainer.html)
2. [Dobot X-Trainer 宣传册](https://www.roscomponents.com/wp-content/uploads/2026/02/X-Trainer-leaflet-Lightweight-Base_Brochure.pdf)
3. [越疆科技官网](https://www.dobot.cn)