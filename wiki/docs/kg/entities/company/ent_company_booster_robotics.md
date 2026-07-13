---
id: ent_company_booster_robotics
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 加速进化
  en: Booster Robotics
status: active
sources:
- id: src_booster_robotics_official
  type: website
  url: https://www.booster.tech
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 加速进化 / Booster Robotics

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 加速进化 |
| **英文名** | Booster Robotics |
| **总部** | 中国北京 |
| **成立时间** | 2023 年 |
| **官网** | [https://www.booster.tech](https://www.booster.tech) |
| **供应链环节** | 整机 OEM / 人形机器人开发平台 |
| **企业属性** | 清华背景、开发者/竞赛平台、RoboCup 冠军 |
| **母公司/所属集团** | 无 |
| **数据来源** | Booster 官网、Bipedal 文档、科创板日报/36 氪 |

## 公司简介

加速进化面向开发者、高校与机器人竞赛，提供轻巧灵活、皮实耐摔的人形机器人平台，曾获 2025 RoboCup AdultSize 冠军。

Booster T1 身高约 1.2 m、体重 30 kg，全身 23 DOF，搭载 Intel i7 1370p 与 NVIDIA Jetson AGX Orin（200 TOPS），支持 ROS2、仿真平台与移动 App 控制。T1 可完成行走、足球、俯卧撑、武术等动态动作，是科研与竞赛领域广泛采用的平台。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 开发者人形机器人 | 科研、竞赛、教育 | Booster T1 | 高校、RoboCup、开发者 |
| 入门平台 | 低成本教育 | Booster K1 | 教育、初学者 |

## 代表产品

### Booster T1

![Booster T1](https://www.althumans.com/media/catalog/product/cache/7e65f7ea2c9ff177580b02a356862407/a/h/ah-booster-t1-01.jpg)


| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 118 cm（高） | Booster 官网 / Bipedal 文档 |
| 重量 | 30 kg | Booster 官网 / Bipedal 文档 |
| 自由度 | 23 DOF（可选配置最高 41 DOF） | Bipedal 文档 / 公开报道 |
| 负载/扭矩 | 膝关节峰值扭矩 130 N·m；空心轴关节电机 | Bipedal 文档 |
| 速度/转速 | 全向行走，具体速度未公开 | Bipedal 文档 |
| 续航 | 10.5 Ah 电池；行走约 2 h，站立约 4 h | Booster 官网 |
| 接口/通信 | ROS 2、USB、Ethernet、Wi-Fi 6、蓝牙 5.2、移动 App | Booster 官网 |
| 价格 | 约 19.9 万元起（公开报道） | 36 氪 / 公开报道 |

**技术亮点**：Intel i7 1370p + NVIDIA Jetson AGX Orin 200 TOPS、全向行走、抗干扰、仿真平台支持（Isaac Sim/Mujoco）、RoboCup 2025 冠军版

**应用场景**：高校科研、RoboCup 竞赛、运动控制算法验证、AI 训练、工业自动化原型。

### Booster K1

> Booster K1：请访问 [官方资料](https://www.booster.tech) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 未公开 | - |
| 重量 | 未公开 | - |
| 自由度 | 未公开 | - |
| 负载/扭矩 | 未公开 | - |
| 速度/转速 | 未公开 | - |
| 续航 | 未公开 | - |
| 接口/通信 | 未公开 | - |
| 价格 | 5999 美元起 | Booster 官网 |

**技术亮点**：入门级具身智能开发平台，降低人形机器人学习与开发门槛

**应用场景**：教育、入门开发、轻量研究。

## 供应链位置

- **上游关键零部件/材料**：自研空心轴关节电机、NVIDIA Jetson AGX Orin、Intel i7 计算平台、深度相机、9 轴 IMU、电池。
- **下游客户/应用场景**：高校科研团队、RoboCup 参赛队、开发者、工业原型客户。
- **主要竞争对手/对标**：宇树 G1、松延 N2、Robotis OP3

## 知识图谱节点与关系

- 公司实体：`ent_company_booster_robotics`
- 产品实体：`ent_product_booster_t1`
- 关键关系：
  - `ent_company_booster_robotics` -- `manufactures` --> `ent_product_booster_t1`
  - `ent_product_booster_t1` -- `uses` --> `ent_component_nvidia_jetson_agx_orin`

## 参考资料

1. [Booster T1 官网](https://www.booster.tech/booster-t1/)
2. [Bipedal – Booster T1 文档](http://www.docs.bipedal.de/projects/t1/html/overview.html)
3. [科创板日报 – CES 报道](https://www.cls.cn/detail/1912332)