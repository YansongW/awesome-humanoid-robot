---
id: ent_component_engineai_q90h
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
status: active
names:
  zh: EngineAI Q90H 一体化关节电机
  en: EngineAI Q90H Integrated Joint Motor
sources:
- id: src_engineai_pm01
  type: website
- title: EngineAI PM01 Product Page
  url: https://www.engineai.com.cn/product-pm01.html
- id: src_engineai_official
  type: website
- title: EngineAI Official Website
  url: https://www.engineai.com.cn
- id: src_aiwiki_engineai_pm01
  type: article
- title: EngineAI PM01 Wiki
  url: https://aiwiki.ai/wiki/engineai_pm01
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
  review_notes: Q90H is EngineAI's proprietary integrated joint actuator for the PM01
    commercial edition; exact continuous/peak current and winding details are not
    publicly disclosed.
---


# EngineAI Q90H 一体化关节电机 / EngineAI Q90H Integrated Joint Motor

## 概述

EngineAI Q90H 是众擎机器人（EngineAI）自研的一体化关节电机模组，主要用于 PM01 商业版人形机器人的髋、膝等大扭矩关节。该模组将无框力矩电机、行星减速器、双编码器与驱动电路集成于关节内部，采用中空走线结构，峰值扭矩密度约 130 N·m/kg，最大关节扭矩 145 N·m。Q90H 面向高动态运动设计，支撑 PM01 实现 2 m/s 行走、前空翻等高难度动作。

## 工作原理 / 技术架构

Q90H 属于高集成度旋转作动器（Integrated Rotary Actuator），其力传递链为：

1. **无框力矩电机**：外转子永磁同步电机直接驱动关节输入轴，产生电磁转矩 $T_m$。
2. **行星减速器**：单级行星齿轮将电机转速降低、扭矩放大，减速比约 25:1。
3. **输出端**：扭矩经交叉滚子轴承传递到连杆，实现低摩擦、高刚性支撑。
4. **传感系统**：双编码器（电机端 + 输出端）提供全闭环位置与速度反馈；电流环用于力控，力控精度约 0.2 N·m（动力关节）。

关节输出扭矩与电机扭矩关系：
$$T_{joint} = \eta \cdot N \cdot T_m$$
其中 $N$ 为减速比，$\eta$ 为传动效率（行星减速器典型 90%–97%）。

峰值扭矩密度：
$$\rho_{torque} = \frac{T_{peak}}{m_{actuator}} \approx 130\ \text{N·m/kg}$$

## 关键参数表

| 参数 | 数值 | 备注/来源 |
|------|------|-----------|
| 制造商 | EngineAI（众擎机器人） | EngineAI 官网 |
| 应用机型 | PM01 商业版 | EngineAI 官网 / 经销商 |
| 关节类型 | 一体化旋转作动器 | EngineAI 公开资料 |
| 减速机构 | 行星减速器 | EngineAI 经销商资料 |
| 减速比 | 25:1 | 经销商产品页 |
| 最大关节扭矩 | 145 N·m | EngineAI 经销商资料 |
| 峰值扭矩密度 | 130 N·m/kg | EngineAI 经销商资料 |
| 最高转速 | 6400 rpm（电机端） | EngineAI 经销商资料 |
| 编码器 | 双编码器（电机端 + 输出端） | AIWiki / EngineAI |
| 轴承 | 交叉滚子轴承 | AIWiki |
| 重量 | 约 1.1 kg | EngineAI 经销商资料 |
| 电机型号（教育版） | Q25H | EngineAI 公开资料 |
| 力控精度 | 0.2 N·m（动力关节） | AIWiki |
| 工作电压 | 未公开 | - |
| 额定/峰值电流 | 未公开 | - |

## 应用场景

- **人形机器人 PM01 商业版**：髋、膝、踝等大扭矩关节，支撑高速行走与动态平衡。
- **高动态双足机器人**：为空翻、跑步、踢腿等爆发力动作提供关节动力。
- **协作机器人/外骨骼**：作为一体化关节模组，简化机械设计与布线。

## 供应链关系

- **制造商**：EngineAI（ent_company_engineai），深圳人形机器人公司。
- **上游关键物料**：稀土磁材、硅钢片、轴承、行星齿轮、编码器、驱动芯片、交叉滚子轴承。
- **下游整机集成**：PM01 商业版整机；Q90H 为 EngineAI 自研自用，不对外公开销售。
- **竞争/对标**：宇树科技关节模组、智元机器人关节、MIT Cheetah 作动器、Maxon 一体化关节。

## 来源与验证

- EngineAI PM01 产品页：https://www.engineai.com.cn/product-pm01.html
- EngineAI 官网：https://www.engineai.com.cn
- EngineAI PM01 Wiki：https://aiwiki.ai/wiki/engineai_pm01