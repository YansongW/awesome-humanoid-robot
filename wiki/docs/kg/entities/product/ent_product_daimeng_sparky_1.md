---
id: ent_product_daimeng_sparky_1
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 戴盟 Sparky 1 心灵手巧型通用人形机器人
  en: Daimeng Sparky 1 Humanoid Robot
status: active
sources:
- id: src_daimeng_aikeji_review_2024
  type: article
  url: http://mp.weixin.qq.com/s?__biz=MzA5ODEzMjIyMA==&mid=2247713810&idx=1&sn=7b99eae4ee0b79d580a58f13e4b62c7e
- title: 戴盟机器人王煜：「具身技能」才能发挥人形机器人的作用
- id: src_daimeng_robot_china_2024
  type: article
  url: https://www.robot-china.com/news/202403/20/88110.html
- title: 戴盟机器人发布 Sparky 1：人形机器人两大阵营已现
- id: src_daimeng_official
  type: website
  url: https://www.dmrobot.com
- title: Daimeng Robotics Official Website
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 戴盟 Sparky 1 / Daimeng Sparky 1

## 概述

戴盟 Sparky 1 是由戴盟（深圳）机器人科技有限公司于 2024 年 3 月发布的“心灵手巧型”通用人形机器人。该产品由香港科技大学孵化团队王煜（Michael Yu Wang）教授、段江哗博士领衔研发，聚焦上肢“手-臂-脑”一体化精细操作，下肢可根据场景选配轮式或足式平台。Sparky 1 采用自研新型视触觉传感器、五指灵巧手以及多模态集成技术，能够通过外骨骼遥操作采集数据进行端到端技能学习，可完成插线束、焊接电路板、滴试剂、熨衣服、倒酒、整理书架等精细任务。

## 工作原理 / 技术架构

Sparky 1 的核心技术路线为“视触觉融合 + 仿人灵巧操作 + 模仿学习”。

1. **视触觉传感**：指尖与手掌集成的新型视触觉传感器基于接触面图像感知，替代传统点阵式压力测量，可获取更丰富的局部几何与力分布信息。
2. **五指灵巧手**：采用驱-传-感-控一体化设计，配合腕部力/触觉反馈，实现类似人手的抓握与工具使用。
3. **多模态融合**：视觉、触觉、语言与动作信号在统一框架下融合，形成端到端操作策略。
4. **数据驱动学习**：通过自研外骨骼遥操作装置采集人类示教数据，利用模仿学习与强化学习训练策略网络。

机器人操作臂的正运动学可描述为

$$
T(\theta_1,\dots,\theta_n)=e^{[S_1]\theta_1}\cdots e^{[S_n]\theta_n}\,T(0),
$$

其中 $[S_i]$ 为第 $i$ 个关节的螺旋坐标矩阵，$T(0)$ 为初始位姿。灵巧手的多自由度（DoF）配置使得末端位姿空间 $SE(3)$ 内的可达性与可操作性显著提升。

## 关键参数表

| 参数 | 数值 / 说明 |
|---|---|
| 产品定位 | 心灵手巧型通用人形机器人 |
| 发布时间 | 2024 年 3 月 |
| 下肢形态 | 轮式 / 足式可选配 |
| 灵巧手 | 五指，集成视触觉传感器 |
| 典型作业高度 | 可完成 2.2 m 书架整理 |
| 视觉系统 | 多相机视觉 + 触觉图像融合 |
| 整机身高 | 未公开 |
| 整机重量 | 未公开 |
| 全身自由度 | 未公开 |
| 续航时间 | 未公开 |

## 应用场景

- **工业制造**：3C 产线精密插拔、焊接、零件装配，无需改造产线即可快速部署。
- **物流仓储**：按物体体积与形状规划路径，完成搬运与分拣。
- **科研教育**：实验辅助、试剂滴定、线束整理等高精度操作。
- **医疗健康**：手术辅助、康复训练等需要精细力控的任务。
- **家庭服务**：养老助老、简单家务、物品递送。

## 供应链关系

在公司-产品-零部件网络中，戴盟机器人处于系统整机集成商位置：

- **上游**：自研视触觉传感器、五指灵巧手、关节模组、计算平台、外骨骼遥操作装置；部分通用电子元器件、电机、减速器由外部供应商提供。
- **同层**：与香港科技大学等学术机构存在技术孵化关系。
- **下游**：面向工业、物流、科研、医疗及家庭服务场景的终端用户与系统集成商。

## 来源与验证

- AI 科技评论对戴盟机器人王煜教授的专访：http://mp.weixin.qq.com/s?__biz=MzA5ODEzMjIyMA==&mid=2247713810&idx=1&sn=7b99eae4ee0b79d580a58f13e4b62c7e
- 中国机器人网发布报道：https://www.robot-china.com/news/202403/20/88110.html
- 戴盟机器人官网：https://www.dmrobot.com

精确整机尺寸、重量、自由度、续航等参数目前未在公开资料中披露，本卡片以“未公开”标注。