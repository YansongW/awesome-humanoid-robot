---
id: ent_component_dobot_nova2
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 越疆 Dobot Nova 2 协作机器人
  en: Dobot Nova 2 Collaborative Robot
status: active
sources:
- id: src_dobot_official
  type: website
- title: 越疆科技官网
  url: https://www.dobot.cn
- id: src_dobot_x_trainer
  type: website
- title: Dobot X-Trainer 产品页
  url: https://www.dobot.cn/products/humanoid-robots/x-trainer.html?lang=cn
- id: src_terra_nova2
  type: website
- title: Terra Robotics – Dobot Nova 2 Specifications
  url: https://terra-robotics.de/en/products/dobot-nova-2
- id: src_top3dshop_nova2
  type: website
- title: Top3DShop – DOBOT Nova 2
  url: https://top3dshop.com/product/dobot-nova-2-collaborative-robot
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from official and verified distributor pages; missing
    values marked as 未公开.
---


# 越疆 Dobot Nova 2 协作机器人 / Dobot Nova 2 Collaborative Robot

## 概述

Dobot Nova 2 是越疆科技（Dobot / Yuejiang Technology）推出的六轴协作机器人（Cobot），面向餐饮、零售、理疗、教育及轻工业装配场景。该机型负载 2 kg、工作半径 625 mm、重复定位精度 ±0.05 mm，以紧凑设计、图形化编程与安全协作功能为特点，是越疆 X-Trainer 双臂遥操作训练平台的从手基础机型之一。

## 工作原理 / 技术架构

Nova 2 为六自由度（6-DOF）串联机械臂，各关节由伺服电机、谐波/行星减速器与编码器组成。控制器通过正逆运动学将末端位姿 $X$ 映射为关节角 $q$：

$$
X = f(q)
$$

其中 $f(\cdot)$ 为机械臂正运动学映射。逆运动学求解 $q = f^{-1}(X)$，用于轨迹规划与笛卡尔空间控制。

重复定位精度 $\varepsilon$ 表征机器人在相同条件下多次到达同一目标点的最大位置偏差，Nova 2 标称为 ±0.05 mm。末端最大线速度 $v_{\text{TCP}}$ 为 1.6 m/s。

安全方面，Nova 2 配备智能传感器与五级可调保护，碰撞检测响应时间约 0.01 s，断电时保持姿态（pose freeze）。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 轴数 | 6 轴 | Terra Robotics / Top3DShop |
| 负载 | 2 kg | Terra Robotics / Top3DShop |
| 工作半径 | 625 mm | Terra Robotics / Top3DShop |
| 重复定位精度 | ±0.05 mm | Terra Robotics / Top3DShop |
| 最大 TCP 速度 | 1.6 m/s | Terra Robotics / Top3DShop |
| 自重 | 11 kg | Terra Robotics |
| 防护等级 | IP54 | Terra Robotics |
| 工作温度 | 0 °C – 50 °C | Terra Robotics |
| 功耗 | 约 100 W（典型） | 行业汇总 |
| 碰撞停止响应时间 | 约 0.01 s | Terra Robotics |
| 编程方式 | 拖拽示教、图形化界面、DobotStudio Pro / CRStudio | Terra Robotics |
| 通信接口 | TCP/IP、Modbus TCP/RTU、RS485、USB | Terra Robotics |
| 安全等级 / 认证 | 未公开完整认证清单 | - |

## 应用场景

- **餐饮服务**：咖啡拉花、饮品调配、面条/小吃制作（单台 Nova 可日处理约 500 杯咖啡或 300 碗面条）。
- **零售展示**：商店与展厅的交互式演示、商品摆放。
- **理疗康复**：按摩、艾灸等低负载、高精度接触式任务。
- **科研教育**：机器人编程教学、数据采集与模仿学习。
- **轻工业装配**：螺丝锁付、小型零件搬运、实验室自动化。

## 供应链关系

- **上游**：自研协作机器人关节、电机、减速器、控制器；Intel RealSense 深度相机；NVIDIA Jetson 算力平台。
- **制造商**：`ent_company_dobot` -- `manufactures` --> `ent_component_dobot_nova2`。
- **下游整机**：Nova 2 作为 X-Trainer 遥操作平台的从手，构成 `ent_product_dobot_x_trainer` -- `uses` --> `ent_component_dobot_nova2`。
- **客户**：高校科研、餐饮连锁、零售集成商、医疗康复机构。
- **竞争对手/对标**：Universal Robots UR3/UR5、遨博、节卡、大族机器人、艾利特。

## 来源与验证

1. 越疆科技官网：https://www.dobot.cn
2. Dobot X-Trainer 产品页：https://www.dobot.cn/products/humanoid-robots/x-trainer.html?lang=cn
3. Terra Robotics Dobot Nova 2 规格页：https://terra-robotics.de/en/products/dobot-nova-2
4. Top3DShop 产品页：https://top3dshop.com/product/dobot-nova-2-collaborative-robot