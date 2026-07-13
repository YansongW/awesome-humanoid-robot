---
id: ent_product_songyan_dynamics_n2
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 松延动力 N2
  en: Noetix Robotics Athlete N2
status: active
sources:
- id: src_noetix_n2_official
  type: website
  url: https://noetixrobotics.com/en/n2
- title: Noetix Athlete N2 | Noetix Robotics
- id: src_humanoid_guide_n2
  type: website
  url: https://humanoid.guide/product/n2/
- title: Noetix Robotics N2 Specs & Price | Humanoid.guide
- id: src_canadasatellite_n2
  type: website
  url: https://www.canadasatellite.ca/eu-sl/Noetix-Athlete-N2-Universal-Humanoid-Robot.htm
- title: Noetix Athlete N2 Universal Humanoid Robot | Canada Satellite
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 松延动力 N2 / Noetix Robotics Athlete N2

## 概述

Noetix Robotics Athlete N2（中文常称“松延动力 N2”）是一款面向教育、科研与家庭陪伴的小型双足人形机器人，以“小体积、高动态”为卖点。其官方宣称是全球首款可在多种场景下完成连续后空翻的人形机器人，强调动态平衡、运动表现力与开放开发接口，定位为具身智能研究平台与青少年科普载体。

## 工作原理 / 技术架构

N2 采用 48 V 直流有齿电机驱动各关节，每条腿 5 个主动自由度、每只手臂 4 个主动自由度，全身共 18 DOF。双足行走控制基于深度强化学习（Deep RL）策略，状态空间 $\mathbf{s}$ 包含关节角度、角速度、躯干姿态、足底力等观测，动作空间 $\mathbf{a}$ 为各关节目标位置或力矩，通过最大化奖励函数

$$
R = r_{\text{velocity}} + r_{\text{balance}} + r_{\text{energy}} + r_{\text{smooth}}
$$

训练出鲁棒步态。相比基于模型的 ZMP（Zero Moment Point）控制，RL 策略对未知地形扰动具有更好的适应性。

膝关节峰值扭矩 150 N·m，结合 30 kg 整机重量，其比扭矩（specific torque）为

$$
\tau_{\text{specific}} = \frac{150\ \text{N·m}}{30\ \text{kg}} = 5\ \text{N·m/kg}
$$

感知层采用前向 + 下倾双深度相机，输出稠密点云用于地形估计与障碍物检测；计算平台可选 Rockchip RK3588s（6 TOPS）或 NVIDIA Jetson Orin Nano Super（67 TOPS）。

## 关键参数表

| 参数 | 数值/说明 | 来源 |
|------|-----------|------|
| 身高 | 118 cm | 官方产品页 |
| 体重 | 约 30 kg | 官方产品页 |
| 全身自由度 | 18 DOF | 官方产品页 |
| 单腿自由度 | 5 DOF | 官方产品页 |
| 单臂自由度 | 4 DOF | 官方产品页 |
| 膝关节峰值扭矩 | 150 N·m | 官方产品页 |
| 最大移动速度 | 3.2 m/s（约 11.5 km/h）| 官方与第三方评测 |
| 行走负载 | 约 5 kg | 官方产品页 |
| 电池 | 48 V / 7 Ah 锂电池 | 官方产品页 |
| 续航时间 | 1–2 h | 官方产品页 |
| 基础算力 | 6 TOPS（RK3588s）| N2 版本 |
| 教育版算力 | 6 + 67 TOPS（Jetson Orin Nano Super）| N2 EDU 版本 |
| 传感器 | 双深度相机、IMU、环形麦克风 | 官方产品页 |
| 通信 | Wi-Fi 6 / 蓝牙 5.2 | 官方产品页 |
| 末端执行器 | 球形手 / 五指灵巧手（选配）| 官方产品页 |

## 应用场景

- **高校与科研机构**：作为低成本双足平台，用于强化学习步态、运动控制、人机交互算法验证。
- **教育科普**：面向中小学、科技馆展示机器人运动能力与 AI 交互，支持可视化动作编程。
- **家庭陪伴**：N2 版本具备语音交互与视觉跟随功能，可承担简单递送、陪伴任务。
- **文娱表演**：舞蹈、后空翻等高动态动作适用于展会、舞台与短视频内容创作。

## 供应链关系

Noetix N2 属于 **人形机器人整机层**，核心零部件包括电机、减速器、电池、深度相机与计算板卡。官方资料显示其关节电机、控制算法与软件栈由 Noetix 自研，计算平台可选国产 Rockchip 或 NVIDIA Jetson，体现上游芯片与传感器供应商对整机性能的直接影响。作为小型人形机器人，其成本结构与供应链复杂度低于全尺寸人形平台。

## 来源与验证

- Noetix Robotics 官方 N2 产品页：https://noetixrobotics.com/en/n2
- Humanoid.guide 汇总规格：https://humanoid.guide/product/n2/
- Canada Satellite 产品说明：https://www.canadasatellite.ca/eu-sl/Noetix-Athlete-N2-Universal-Humanoid-Robot.htm

官方未公开全部机械设计细节（如减速器类型、精确关节范围），表中未公开项以官方标注或第三方聚合资料为准。