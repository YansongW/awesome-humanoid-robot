# THORMANG3（ROBOTIS 全尺寸人形机器人）调研档案

> 调研访问日期：2026-07-01。所有事实均附来源 URL（见文末）；未查到的信息标注"未知"。GitHub 星标等为检索时点快照。

## 基本信息

| 项目 | 内容 |
|---|---|
| 项目名 | THORMANG3（Tactical Hazardous Operations Robot，第三代） |
| 发起机构 | ROBOTIS（韩国）；THOR 系列源于 DARPA Robotics Challenge 2015 决赛平台（Team ROBOTIS） |
| 开源许可证 | ROS 软件包开源于 GitHub（ROBOTIS-GIT/ROBOTIS-THORMANG-* 系列，COMMON 包许可证标记为"Other/未明确"）；整机 STP 三维模型官方公开下载；本质是商业整机 + 开源控制软件 |
| 硬件成本 | **未知**——官方无公开标价，经销商页面标注"需询价、交货期 12 周"（Cyber Robotics HK，2025 年页面）；历史定位为"相对可负担的全尺寸平台"，无确切数字，不臆测 |
| 身高 / 重量 | 137.5 cm / 42 kg |
| 自由度 | 29 |

## 执行器方案

- 29 台 **DYNAMIXEL-P（原 DYNAMIXEL PRO）系列一体化伺服**（2019 年 6 月起由 PRO 换型为 P 系列）：
  - PH54-200-S500-R（200W）× 10（腿部大关节）
  - PH54-100-S500-R（100W）× 11
  - PH42-020-S300-R（20W）× 8（小关节）
- 谐波减速 + 高功率密度伺服是 DRC 时代全尺寸平台的典型方案，扭矩充足但单台舵机价格昂贵，整机成本主要在此。

## 计算平台与传感器

- 计算：2 台 Intel NUC（Core i5、8GB DDR4、128GB M.2 SSD），分工运动控制（MPC）与感知（PPC）；机载 D-Link DIR-806A 无线路由。
- 传感器：Logitech C920 相机；Intel RealSense（选配）；Hokuyo UTM-30LX-EW 激光雷达（选配）；双脚踝 ATI Mini58 六维力/力矩传感器 ×2；MicroStrain 3DM-GX4-25 IMU。
- 电池：22V 22000 mAh + 18.5V 11000 mAh 双电池；也可外接电源（执行器需 0–30V/100A 电源）。
- 附带无线急停、吊装带（carabiner + rope）与升降架——全尺寸机型的安全标配。

## 软件栈

- Ubuntu LTS 64 位 + **ROS1**，C++ 开发；官方提供行走（walking）、操作（manipulation）、感知（PPC）、Gazebo 仿真（COMMON 包）等完整 ROS 包。
- 全套 e-Manual 教程（快速上手、校准、教程、开发）；STP 模型可用于二次机械设计。
- 未提供 ROS2 官方支持（检索时点未见）。

## 文档与教程质量

- e-Manual 完善程度与 OP3 同级：规格、包装清单、外接电源规格、安全须知一应俱全。
- 但软件包代码停留在 ROS1 时代（多数仓库 2016–2018 年后无实质更新），现代工具链（ROS2、Isaac/MuJoCo）缺失。

## 社区活跃度

- GitHub `ROBOTIS-GIT/ROBOTIS-THORMANG-COMMON`：仅 **5 stars / 10 forks**，最后 push 2018-04-01；MPC/PPC/Tools 等兄弟仓库均为 2016 年创建、长期停更。
- 用户集中在少数有 DRC 传承的实验室（如 THOR 系团队）；公开社区讨论稀少。

## 新手友好度评估：1 / 5

- 优点：29 自由度全尺寸平台、F/T 传感器 + 激光雷达配置齐全、ROBOTIS 文档规范、DRC 血统。
- 门槛：42 kg、137 cm 的全尺寸机型对场地/安全/人员要求极高；价格需询价且必然远超个人预算；ROS1 软件栈陈旧，维护投入大。
- 适合：有全尺寸平台刚性需求的大学/研究所实验室；**完全不适合个人新手**——想玩全尺寸请直接看 OpenLoong 的仿真框架。

## 来源 URL（访问日期 2026-07-01）

- https://emanual.robotis.com/docs/en/platform/thormang3/introduction/ （规格：29 DoF / 137.5 cm / 42 kg / DYNAMIXEL-P 清单 / 双 NUC / 传感器 / 电池 / STP 下载 / 2019 换型说明）
- https://github.com/robotis-git/robotis-thormang-common （ROS 包与规格表；星标与停更时间经 GitHub API 检索）
- https://github.com/ROBOTIS-GIT/ROBOTIS-THORMANG-MPC 与 https://github.com/ROBOTIS-GIT/ROBOTIS-THORMANG-PPC （运动/感知 ROS 包，2016 年创建）
- http://wiki.ros.org/ROBOTIS （THORMANG3 基于 DYNAMIXEL PRO、DARPA Robotics Challenge 2015 决赛平台）
- https://www.robotics.com.hk/product/thormang3/ （经销商：价格需询价、交货期 12 周）
- https://emanual.robotis.com/docs/en/platform/ （平台总览页：OP 与 OP2 已停产，THORMANG3 仍在列表中）
