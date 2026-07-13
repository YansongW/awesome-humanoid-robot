---
id: ent_product_casbot_01
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 灵宝 CASBOT 01 全尺寸双足人形机器人
  en: CASBOT 01 Humanoid Robot
status: active
sources:
- id: src_casbot_ithome
  type: article
  url: https://www.ithome.com/0/810/472.htm
- title: 灵宝 CASBOT 01 人形机器人发布
- id: src_casbot_leiphone
  type: article
  url: https://www.leiphone.com/category/robot/Gy0hnPSsUSGhp64Y.html
- title: 灵宝 CASBOT 首款人形机器人产品 CASBOT 01 发布
- id: src_casbot_official
  type: website
  url: https://www.casbot.tech
- title: 灵宝 CASBOT 官网
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 灵宝 CASBOT 01 / CASBOT 01

## 概述

灵宝 CASBOT 01 是北京中科慧灵机器人技术有限公司旗下品牌“灵宝 CASBOT”于 2024 年 11 月发布的首款全尺寸双足人形机器人，昵称“星期三”。该产品定位多场景落地的通用类脑智能机器人，身高 179 cm、体重 60 kg，全身 52 个自由度，端侧算力 550 TOPS，续航超过 4 小时。CASBOT 01 采用背包式快拆双电池设计，支持 30 分钟单电池快充，面向工业制造、应急救援、商业服务与科研教育等场景。

## 工作原理 / 技术架构

CASBOT 01 采用“本体 + 大脑”协同架构：

1. **感知系统**：头部具备 2 个自由度，集成多个 RGBD 相机、激光雷达、IMU 与显示屏，实现视听双模态交互。
2. **运动控制**：单腿 6 个自由度，部分关节可实现 360° 或更大运动空间；整体运动控制框架结合对抗运动先验与全身控制（WBC），实现双足稳定行走与全身作业。
3. **灵巧操作**：五指仿生灵巧手单手重量 800 g，额定负载 5 kg，集成触觉-力觉-视觉多源感知与驱-传-感-控一体化仿生设计。
4. **关节模组**：自研行星、谐波、直线三大系列一体化关节，峰值扭矩密度最高 207 N·m/kg，关节效率超过 80%，力矩控制精度小于 3%。
5. **具身智能**：端到端多模态灵巧操作大模型配合蒸馏与量化技术，实现对环境、对象、任务的泛化适应。

关节功率密度可写作

$$
\rho_P=\frac{P}{m}=\frac{\tau\,\omega}{m},
$$

其中 $\tau$ 为输出扭矩，$\omega$ 为角速度，$m$ 为关节质量。峰值扭矩密度 $\rho_\tau=\tau_{\max}/m$ 是 CASBOT 01 关节设计的核心指标之一。

## 关键参数表

| 参数 | 数值 / 说明 |
|---|---|
| 产品定位 | 全尺寸双足人形机器人 |
| 身高 | 179 cm |
| 体重 | 60 kg |
| 全身自由度 | 52 |
| 端侧算力 | 550 TOPS |
| 续航时间 | ＞4 h |
| 头部自由度 | 2 |
| 单腿自由度 | 6 |
| 五指灵巧手 | 800 g，额定负载 5 kg |
| 关节峰值扭矩密度 | 最高 207 N·m/kg |
| 关节效率 | ＞80% |
| 电池方案 | 背包式快拆双电池，30 min 单电池快充 |
| 运动能力 | 双足站立、稳定行走、跑步、跳跃 |

## 应用场景

- **工业制造**：精密装配、螺丝拧紧、物料搬运、产线巡检。
- **应急救援**：井下作业、灾害现场勘察与物资运输。
- **航天航海**：特殊环境下的操作与维护。
- **商业服务**：迎宾接待、导览讲解、物品递送。
- **科研教育**：具身智能算法验证、人机交互研究。

## 供应链关系

- **上游**：自研一体化关节、灵巧手、感知模组；外部供应高性能计算平台、电池、结构材料、传感器。
- **同层**：灵宝 CASBOT 作为系统整机商，与联想制造即服务等签署战略合作，是联想“火种计划”首批核心合作企业。
- **下游**：工业、应急救援、航天航海、商业服务等终端用户与集成商。

## 来源与验证

- IT之家发布报道：https://www.ithome.com/0/810/472.htm
- 雷锋网深度报道：https://www.leiphone.com/category/robot/Gy0hnPSsUSGhp64Y.html
- 灵宝 CASBOT 官网：https://www.casbot.tech