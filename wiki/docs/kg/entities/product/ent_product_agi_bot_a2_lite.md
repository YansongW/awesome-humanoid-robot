---
id: ent_product_agi_bot_a2_lite
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 智元 远征 A2 青春版
  en: AgiBot Expedition A2 Lite
status: active
sources:
- id: src_agibot_a2_lite_product
  type: website
  url: https://www.agibot.com/product/169/detail/4.html
- title: 智元远征 A2 人型机器人 | 智元机器人
- id: src_agibot_a2_lite_jwview
  type: website
  url: https://www.jwview.com/jingwei/html/m/08-18/628688.shtml
- title: 智元机器人产品上线，人形机器人最低售价 9.8 万元 | 中新经纬
- id: src_agibot_a2_lite_smzdm
  type: website
  url: https://www.smzdm.com/p/155782150/
- title: 智元机器人 AgiBot 远征 A2-青春版 | 什么值得买
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 智元 远征 A2 青春版 / AgiBot Expedition A2 Lite

## 概述

智元远征 A2 青春版（AgiBot Expedition A2 Lite）是智元机器人面向文娱商演场景推出的全尺寸双足人形机器人，身高 169 cm，体重约 60–63 kg，具备 23 个自由度，支持挥手、握手、京剧、太极、民族舞等预设动作，并可通过深度学习持续吸纳新动作模块。该产品于 2025 年 8 月上线智元商城与京东商城，限时售价 168,000 元，定位于商业表演、展览展示与群控演出。

## 工作原理 / 技术架构

远征 A2 青春版采用智元自研的“具身智脑”EI-Brain 框架，将机器人系统划分为云端超脑、大脑、小脑、脑干四级，分别负责任务级、技能级、指令级与伺服级控制。其任务级模型 WorkGPT 为智元自研的具身多模态大模型，通过视觉语言大模型理解用户意图并编排动作序列。

动力系统采用 PowerFlow 关节电机，官方旗舰版峰值扭矩超过 350 N·m，重量 1.6 kg。青春版公开参数显示最大扭矩 270 N·m，行走速度 0.5–0.8 m/s。电机功率密度 $\rho_P$ 可表示为

$$
\rho_P = \frac{P}{m} = \frac{T \cdot \omega}{m}
$$

其中 $T$ 为峰值扭矩，$\omega$ 为对应角速度，$m$ 为电机质量。

电池容量 14.4 Ah，站立续航约 4.5 小时，行走续航约 2 小时，支持热插拔换电。机身配备麦克风阵列、RGB-D 相机、激光雷达等传感器，支持群控编舞与 VR 遥操作选配件。

## 关键参数表

| 参数 | 数值/说明 | 备注 |
|------|-----------|------|
| 身高 | 169 cm | 官方商城 |
| 体重 | 约 60–63 kg | 官方/媒体报道 |
| 全身自由度 | 23 DOF | 青春版规格 |
| 臂长 | 50.4 cm | 第三方汇总 |
| 手臂最大负载 | 约 2 kg | 官方商城 |
| 最大扭矩 | 270 N·m | 媒体报道 |
| 行走速度 | 0.5–0.8 m/s | 官方商城 |
| 日常使用速度 | ≤0.6 m/s | 官方商城 |
| 电池容量 | 14.4 Ah | 官方商城 |
| 站立续航 | 约 4.5 h | 官方商城 |
| 行走续航 | 约 2 h | 官方商城 |
| 充电时间 | 约 2 h | 媒体报道 |
| 售价 | 198,000 元（限时 168,000 元）| 智元商城/京东 |
| 发货周期 | 尾款支付后 30 天 | 媒体报道 |
| 预设动作 | 挥手、握手、太极等 5 项 | 基础赠送 |
| 可选动作 | 哪吒舞、花球舞、打鼓等 | 需额外定制 |
| 感知元件 | 麦克风阵列、RGB-D 相机、激光雷达 | 旗舰版/青春版 |

## 应用场景

- **文娱商演**：舞台表演、开业庆典、展会暖场，通过群控编排实现多机同步舞蹈。
- **展览展示**：科技馆、博物馆、品牌展厅中的迎宾、导览与互动演示。
- **商业活动**：商场、景区、发布会中的品牌代言与人流吸引。
- **科研教学**：作为全尺寸人形平台用于动作学习、人机交互与群控算法研究。

## 供应链关系

智元远征 A2 青春版属于 **人形机器人整机层**，核心零部件包括 PowerFlow 关节电机、灵巧手、RGB-D 相机、激光雷达、电池包与计算平台。智元自研关节电机与 EI-Brain 软件框架，部分传感器与芯片依赖外部供应商。其商业模式以整机销售与场景化动作为增值服务为主，下游面向演艺公司、展览服务商、科研机构与个人消费者。

## 来源与验证

- 智元机器人官方产品页：https://www.agibot.com/product/169/detail/4.html
- 中新经纬报道（2025-08-18）：https://www.jwview.com/jingwei/html/m/08-18/628688.shtml
- 什么值得买商品页：https://www.smzdm.com/p/155782150/

官方未公开青春版全部机械参数（如精确关节扭矩分布、减速器类型、电池电压），表中部分数值来自商城页面与媒体报道；不同来源对体重（60 kg vs 63 kg）存在细微差异。