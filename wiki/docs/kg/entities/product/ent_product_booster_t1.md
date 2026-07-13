---
id: ent_product_booster_t1
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: Booster T1
  en: Booster T1
status: active
sources:
- id: src_booster_t1_official
  type: website
  url: https://www.booster.tech
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# Booster T1 / Booster T1

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [加速进化 / Booster Robotics](../../../appendices/appendix-d/companies/company_booster_robotics.md) |
| **产品类别** | 通用人形机器人 |
| **发布时间** | 未公开 |
| **状态** | 量产/商用 |
| **官网/来源** | [https://www.booster.tech](https://www.booster.tech) |

## 产品概述

高校科研、RoboCup 竞赛、运动控制算法验证、AI 训练、工业自动化原型。

Booster T1 是 加速进化 的代表产品。Intel i7 1370p + NVIDIA Jetson AGX Orin 200 TOPS、全向行走、抗干扰、仿真平台支持（Isaac Sim/Mujoco）、RoboCup 2025 冠军版。主要规格包括：118 cm（高）（尺寸）、30 kg（重量）、23 DOF（可选配置最高 41 DOF）（自由度）。

## 产品图片

![Booster T1](https://www.althumans.com/media/catalog/product/cache/7e65f7ea2c9ff177580b02a356862407/a/h/ah-booster-t1-01.jpg)


## 规格参数表

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

## 供应链位置

- **制造商**：[加速进化 / Booster Robotics](../../../appendices/appendix-d/companies/company_booster_robotics.md)
- **核心零部件/技术来源**：自研空心轴关节电机、NVIDIA Jetson AGX Orin、Intel i7 计算平台、深度相机、9 轴 IMU、电池。
- **下游应用/客户**：高校科研、RoboCup 竞赛、运动控制算法验证、AI 训练、工业自动化原型。

## 知识图谱节点与关系

- 产品实体：`ent_product_booster_t1`
- 制造商实体：`ent_company_booster_robotics`
- 关键关系：
  - `rel_ent_company_booster_robotics_manufactures_ent_product_booster_t1`（`ent_company_booster_robotics` → `manufactures` → `ent_product_booster_t1`）
  - `ent_product_booster_t1` -- `uses` --> `ent_component_nvidia_jetson_agx_orin`

## 应用场景

- **高校科研、RoboCup 竞赛、运动控制算法验证、AI 训练、工业自动化原型。**

## 竞争对比

| 对比项 | 本产品 | 主要竞品 |
|--------|--------|----------|
| 定位 | 通用人形机器人 | 同类产品视具体场景而定 |
| 核心优势 | Intel i7 1370p + NVIDIA Jetson AGX Orin 200 TOPS、全向行走、抗干扰、仿真平台支持（Isaac Sim/Mujoco）、RoboCup 2025 冠军版 | 未公开 |
| 价格 | 约 19.9 万元起（公开报道） | 未公开 |

## 选购与部署建议

- 建议通过官方渠道确认最新软件版本、SDK 支持与售后培训。
- 科研与教育用户应优先评估二次开发接口、仿真平台兼容性与社区活跃度。
- 工业用户需结合具体工序验证负载、精度、防护等级与集成接口。

## 参考资料

1. [Booster T1 官网](https://www.booster.tech/booster-t1/)
2. [Bipedal – Booster T1 文档](http://www.docs.bipedal.de/projects/t1/html/overview.html)
3. [科创板日报 – CES 报道](https://www.cls.cn/detail/1912332)