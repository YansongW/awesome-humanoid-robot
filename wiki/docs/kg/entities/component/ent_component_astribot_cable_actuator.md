---
id: ent_component_astribot_cable_actuator
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: 星尘智能绳驱执行器
  en: Astribot Cable-Driven Actuator
sources:
- id: src_astribot_official
  type: website
- title: Astribot 星尘智能官网
  url: https://www.astribot.com/en/product
- id: src_astribot_suite
  type: website
- title: 星尘智能 Astribot Suite 发布报道
  url: http://mp.weixin.qq.com/s?__biz=Mzg2NjYxMjcxNQ==&mid=2247492022&idx=1&sn=014e70d70be0d5cb3844052b4f4cc38f
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
  review_notes: Specifications from Astribot official website and public reports;
    detailed actuator-level parameters are not fully disclosed and marked as 未公开.
---


# 星尘智能绳驱执行器 / Astribot Cable-Driven Actuator

## 概述

星尘智能绳驱执行器是 Astribot 自研的柔性传动执行机构，用于驱动 Astribot S1 等人形机器人的全身关节。该执行器通过高强度绳索模拟人体肌腱传动，将电机布置于关节近端或躯干内部，从而显著降低末端惯量、提升动态响应，并赋予机器人被动柔顺性与安全的人机交互能力。

## 工作原理与技术架构

绳驱执行器的基本工作原理为：

1. **电机-绳索-关节耦合**：电机位于关节近端，通过卷绕或牵引绳索将力和运动传递到远端关节；绳索可类比为肌腱，关节处设置滑轮或绞盘实现力与位移传递。
2. **柔性传动**：绳索具有低刚度、高阻尼特性，可在接触冲击时吸收能量，提供被动顺应性。
3. **力/位混合控制**：通过电机端编码器与关节端编码器（或视觉）实现双环闭环控制，结合拉力传感器实现精确的力控操作。
4. **刚柔耦合动力学**：星尘智能通过刚柔混合动力学建模与控制优化，实现最小控制延迟和高精度轨迹跟踪。

在理想滑轮-绳索模型中，关节输出力矩 $T$ 与电机输出力矩 $T_m$、减速比 $N$、滑轮半径 $r$ 的关系可近似为：

$$
T = N \cdot T_m \cdot \frac{r_{\text{joint}}}{r_{\text{motor}}}
$$

绳索传动还引入了弹性环节，其等效刚度 $k$ 与绳索长度 $L$、截面积 $A$、弹性模量 $E$ 相关：

$$
k = \frac{E A}{L}
$$

较低的等效刚度有助于实现柔顺交互，但也对控制带宽提出更高要求。

## 关键参数

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 传动方式 | 绳驱（ cable-driven ）| Astribot 官网 |
| 执行器布局 | 电机后置、绳索远端传动 | Astribot 公开报道 |
| 单臂自由度 | 7 DOF | Astribot 官网 |
| 单臂额定负载 | 5 kg | Astribot 官网 |
| 单臂峰值负载 | 10 kg | Astribot 官网 |
| 末端最高速度 | ≥10 m/s | Astribot 官网 |
| 末端重复定位精度 | ±0.1 mm | Astribot 官网 |
| 末端峰值加速度 | 100 m/s² | Astribot 公开报道 |
| 电机类型 | 未公开 | - |
| 绳索材料 | 未公开 | - |
| 减速机构 | 未公开 | - |
| 控制接口 | ROS 2 / Python SDK / Gigabit Ethernet / Wi-Fi | Astribot 技术文档 |
| 价格 | 未公开 | - |

注：星尘智能未单独公布执行器级别的额定扭矩、功率、绳索张力、刚度等参数，上表所列主要为整机 S1 的公开性能指标。

## 应用场景

- **通用 AI 机器人助理**：Astribot S1 执行叠衣、炒菜、书法、泡茶等复杂操作任务。
- **科研与教育**：作为全身操作机器人平台，支持机器人学习、遥操作与 VLA 算法研究。
- **新零售展示**：商业服务场景中的互动展示与商品操作。
- **智慧养老**：辅助性操作与陪伴服务。
- **柔性制造小批量装配**：利用柔顺力控完成精密装配任务。

## 供应链关系

- **上游**：高性能电机、高强度绳索/ tendon、力/拉力传感器、编码器、控制器、轻量化结构件。
- **制造商**：星尘智能（Astribot）通过关系 `ent_company_astribot -- manufactures --> ent_component_astribot_cable_actuator` 记录于知识图谱。
- **下游**：整机产品 `ent_product_astribot_s1` 使用该执行器作为核心传动部件。与 Figure 02、特斯拉 Optimus、优必选 Walker 等形成竞争。

## 来源与验证

绳驱执行器的技术路线与整机性能参数来自 Astribot 官网、百度百科及公开新闻报道。由于 Astribot 未单独发布执行器级 datasheet，电机型号、绳索材料、减速比、额定扭矩等执行器内部参数未公开，已标注为未公开。