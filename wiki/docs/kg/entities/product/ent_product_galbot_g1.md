---
id: ent_product_galbot_g1
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: Galbot G1
  en: Galbot G1
status: active
sources:
- id: src_galbot_official
  type: website
  url: https://www.galbot.com/g1
- title: Galbot G1 Official Product Page
- id: src_sonnyrobotics_galbot
  type: website
  url: https://sonnyrobotics.com/products/galbot-g1
- title: Galbot G1 Wheeled Humanoid Robot — Sonny Robotics
- id: src_ronomics_galbot
  type: website
  url: https://ronomics.com/galbot-picks-up-153m-to-commercialize-g1-semi-humanoid/
- title: Galbot picks up $153M to commercialize G1 semi-humanoid
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# Galbot G1 / Galbot G1

## 概述

Galbot G1 是北京银河通用机器人有限公司（Galbot / Galaxy General Robot Co.）推出的轮式双臂可折叠人形机器人，定位于家庭服务与商业零售场景。整机身高 173 cm，体重约 85 kg，采用 360° 全向轮式底盘替代双足行走机构，通过躯干升降与折叠腿结构覆盖 65 cm 的垂直作业区间，最大作业高度可达 240 cm。G1 已在药店、便利店、仓储物流等场景中实现 24 小时商用部署。

## 工作原理 / 技术架构

### 移动与操作机构
G1 采用全向轮式移动底盘（omnidirectional wheeled base），水平面内可实现前后、横移与斜向运动，无需先调整机身朝向。与双足人形相比，轮式结构将能量主要用于上肢操作与计算，而非姿态维持，这是其续航显著延长的关键。

机身垂直运动由躯干升降机构实现，升降行程 65 cm，结合 190 cm 臂展，形成

$$
H_{\text{reach}} = H_{\text{torso}} + \Delta h + L_{\text{arm}} \approx 240\ \text{cm}
$$

的最大作业高度，可覆盖标准货架与人居环境中的高处取物任务。

### 感知与智能
G1 搭载以 RGB-D 相机、触觉传感器、四麦克风阵列为核心的多模态感知系统，导航采用纯视觉方案（无需二维码或 LiDAR）。其 AI 系统 AstraBrain 集成：

- **GraspVLA**：端到端抓取基础模型，支持 5,000 种以上物品的零样本抓取；
- **TrackVLA**：视觉导航模型；
- **GroceryVLA**：零售场景专用模型；
- **NavFoM**：导航基础模型。

抓取成功率公开数据为 95%–97%。Premium 版本搭载 NVIDIA Jetson Thor 计算平台。

## 关键参数表

| 参数 | 数值 |
|------|------|
| 身高 | 173 cm |
| 体重 | 约 85 kg |
| 臂展 | 190 cm |
| 躯干升降行程 | 65 cm |
| 最大作业高度 | 240 cm |
| 自由度 | 25 / 34 / 47（不同配置报道差异） |
| 单臂自由度 | 7 |
| 单手自由度 | 12 |
| 单臂负载 | 5 kg |
| 双臂负载 | 5–10 kg |
| 最大移动速度 | 5 km/h |
| 典型行走速度 | 3 km/h |
| 续航 | 最长 10 h |
| 感知系统 | RGB-D 相机、触觉传感器、4 麦克风阵列 |
| 导航方式 | 纯视觉，无 LiDAR |
| 通信 | WiFi、以太网、USB、云端 |
| 参考价格区间 | 约 63–84 万元人民币 |

## 应用场景

- **零售与便利店**：货架补货、盘点、拣货、打包；
- **药店**：24 小时药品递送与导购；
- **仓储物流**：小件搬运与分拣；
- **家庭服务**：折叠衣物、倒水、拾取物品等（已在公开演示中验证）。

## 供应链关系

Galbot G1 位于“整机厂商—核心零部件—上游算力/传感”链条的整机集成端：

- **整机**：北京银河通用机器人有限公司；
- **计算平台**：Premium 版采用 NVIDIA Jetson Thor；
- **传感器**：RGB-D 深度相机、触觉传感器等由多家视觉与力觉传感器供应商提供；
- **场景落地**：与京东、连锁药店、便利店及汽车/电子制造企业合作部署。

## 来源与验证

- Galbot 官方产品页（https://www.galbot.com/g1）
- 第三方经销商技术规格汇总（Sonny Robotics、SVRC、Robotseuropa 等）
- 公开报道：Ronomics（2026-02-24）、Robozaps Review（2026-07-11）

> 注：不同公开来源对总自由度（25 / 34 / 47 DOF）报道存在差异，表中列出以供交叉比对；具体配置需以官方 datasheet 为准。