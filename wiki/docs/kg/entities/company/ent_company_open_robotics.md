---
id: ent_company_open_robotics
schema_version: 1
type: company
'title:': Open Robotics
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: Open Robotics
  en: Open Robotics
aliases:
- Open Robotics
- Open Robotics
status: active
sources:
- id: src_open_robotics_official
  type: website
  url: https://www.openrobotics.org
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01 00:00:00+00:00
---





# Open Robotics / Open Robotics

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | Open Robotics |
| **英文名** | Open Robotics |
| **总部** | 美国加利福尼亚州山景城 |
| **成立时间** | 2012 |
| **官网** | [https://www.openrobotics.org](https://www.openrobotics.org) |
| **供应链环节** | 开源机器人软件平台、中间件、仿真 |
| **企业属性** | 非营利基金会（OSRF）+ Intrinsic 收购商业子公司 |
| **母公司/所属集团** | Open Source Robotics Foundation（OSRF） |
| **数据来源** | Open Robotics 官网、ROS 与 Gazebo 官方文档 |

## 公司简介

Open Robotics 维护 ROS、ROS 2、Gazebo 仿真器与 Open-RMF，是全球机器人软件的事实标准。

ROS/ROS 2 提供机器人中间件、算法库与工具链；Gazebo 提供高保真 3D 物理仿真；Open-RMF 协调多机器人 fleets。大部分人形机器人项目均依赖这些开源平台。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| ROS 2 | 机器人操作系统第二代 | ROS 2 Jazzy 等 | 中间件、导航、控制、感知 |
| Gazebo | 3D 物理仿真器 | Gazebo Harmonic/Ionic | 机器人仿真、Sim2Real、传感器验证 |
| Open-RMF | 机器人中间件框架 | Open-RMF | 多机器人调度与协同 |

## 代表产品

### ROS 2

> ROS 2：请访问 [官方资料](https://www.openrobotics.org) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 版本 | Jazzy Jalisco（LTS，2024）等 | ROS 官方文档 |
| 许可 | Apache 2.0 / BSD | 官方仓库 |
| 通信中间件 | DDS（默认 eProsima Fast DDS） | 官方文档 |
| 支持语言 | C++ / Python | 官方文档 |
| 支持平台 | Linux、RTOS、嵌入式 | 官方文档 |
| 实时性 | 支持实时控制（取决于平台与 RMW） | 官方文档 |
| 核心生态 | Nav2、MoveIt 2、ros2_control、rviz2 | 官方文档 |
| 价格 | 免费开源 | - |

**技术亮点**：去中心化架构、DDS 通信、跨平台支持、庞大算法与工具生态、被绝大多数人形机器人采用。

**应用场景**：机器人软件开发、导航、操纵、仿真到真实部署。


### Gazebo

> Gazebo：请访问 [官方资料](https://www.openrobotics.org) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 版本 | Harmonic / Ionic 等 | Gazebo 官方 |
| 许可 | Apache 2.0 | 官方仓库 |
| 物理引擎 | ODE、Bullet、DART、Simbody | 官方文档 |
| 渲染 | OGRE | 官方文档 |
| 模型格式 | SDF、URDF | 官方文档 |
| ROS 集成 | ros_gz_bridge 与原生插件 | 官方文档 |
| 传感器仿真 | 相机、LiDAR、IMU、深度相机、GPS 等 | 官方文档 |
| 价格 | 免费开源 | - |

**技术亮点**：多物理引擎支持、高质量传感器仿真、与 ROS/ROS 2 深度集成、广泛用于 Sim2Real 研究。

**应用场景**：机器人算法验证、数字孪生、强化学习训练、传感器模型测试。


## 供应链位置

- **上游关键零部件/材料**：DDS 实现、物理引擎、图形渲染、操作系统与编译工具链。
- **下游客户/应用场景**：几乎所有人形机器人 OEM、研究机构、自动驾驶与物流机器人企业。
- **主要竞争对手/对标**：NVIDIA Isaac Sim、Unity、Unreal Engine、CoppeliaSim、Webots。

## 知识图谱节点与关系

- 公司实体：`ent_company_open_robotics`
- 产品/平台实体：`ent_software_platform_open_robotics_ros2`、`ent_software_platform_open_robotics_gazebo`
- 关键关系：
  - `rel_ent_company_open_robotics_develops_ent_software_platform_open_robotics_ros2`（`ent_company_open_robotics` → `develops` → `ent_software_platform_open_robotics_ros2`）
  - `rel_ent_company_open_robotics_develops_ent_software_platform_open_robotics_gazebo`（`ent_company_open_robotics` → `develops` → `ent_software_platform_open_robotics_gazebo`）

## 参考资料

1. [Open Robotics 官网](https://www.openrobotics.org)
2. [ROS 2 官方文档](https://docs.ros.org/en/rolling/)
3. [Gazebo 官方文档](https://gazebosim.org/home)