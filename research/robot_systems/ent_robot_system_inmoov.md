---
$id: ent_robot_system_inmoov
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: InMoov
  zh: InMoov 3D 打印人形机器人
  ko: InMoov
summary:
  en: The first open-source 3D-printed life-size humanoid robot, started in 2012 by French sculptor Gael Langevin, printable on a home printer for as little as several hundred dollars in parts, with tendon-driven five-finger hands, standard hobby servos, Arduino low-level control and the MyRobotLab interaction framework, defaulting to an upper body without legs.
  zh: InMoov 是法国雕塑家 Gaël Langevin 于 2012 年发起的开源 3D 打印真人尺寸人形机器人，全部零件可在家用 3D 打印机上复现，成本可低至数百美元，标志性子系统为腱驱动五指手，采用标准航模舵机 + Arduino 低层控制 + MyRobotLab 交互框架，默认仅为上半身（无腿），是历史上被复制最多的开源人形机器人。
  ko: The first open-source 3D-printed life-size humanoid robot, started in 2012 by French sculptor Gael Langevin, printable on a home printer for as little as several hundred dollars in parts, with tendon-driven five-finger hands, standard hobby servos, Arduino low-level control and the MyRobotLab interaction framework, defaulting to an upper body without legs.
domains:
- 02_components
- 06_design_engineering
- 11_applications_markets
layers:
- midstream
- intelligence
functional_roles:
- system
- knowledge
tags:
- open_source
- humanoid_robot
- inmoov
- 3d_printed
- myrobotlab
- arduino
- hobby_servo
- tendon_driven_hand
- maker
- hri
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: '内容整理自调研档案 data/roadmap/research/inmoov.md（访问日期 2026-07-01）。无官方 BOM，成本为媒体/第三方数据库估算区间；身高/重量/自由度因构建者而异，所列数值为第三方报道口径。3D 打印部件为 CC BY-NC 3.0 非商业许可。'
sources:
- id: src_001
  type: website
  title: InMoov Official Project Page
  url: https://inmoov.fr/project/
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MyRobotLab GitHub Repository
  url: https://github.com/MyRobotLab/myrobotlab
  accessed_at: '2026-07-01'
---

## 概述

InMoov 是法国雕塑家/模型师 Gaël Langevin（Factice Ateliers）于 2012 年 1 月发起的个人开源项目，是首个可用家用 3D 打印机复现的真人尺寸开源人形机器人，软件生态依托 MyRobotLab 社区。整机真人尺寸（约 1.75–1.8 m 的报道口径），默认仅为上半身（头、躯干、双臂、双手），无腿；重量因构建而异（第三方报道约 30 kg，非官方数据）（来源：调研档案 inmoov.md，下同）。

许可证：3D 打印部件 CC BY-NC 3.0（署名-非商业）；MyRobotLab 框架历史上 GPLv2，现 GitHub 仓库标注 Apache-2.0。无官方 BOM，成本为媒体估算：约 $800（2015 年整机报道）；$900+ 且不含躯干与头部（2013 年报道）；$800–2,500 视舵机/电子件选型（2025 年第三方数据库）。到 2018 年全球已有近 1,000 台 InMoov 复制机（ESILV 报道），是历史上被复制最多的开源人形机器人。

## 核心内容

### 关键参数

| 项目 | 数值 | 来源 |
|---|---|---|
| 身高 / 重量 | 约 1.75–1.8 m / 约 30 kg（均第三方报道口径，非官方） | 第三方数据库 |
| 自由度 | 典型全构建约 28 台舵机、22–30 个可控自由度（第三方口径）；另有"约 45 关节"报道 | 第三方数据库 |
| 硬件成本 | 无官方 BOM；$800–2,500 估算区间 | 媒体 / 第三方数据库 |
| 低层控制 | Arduino Mega（舵机 PWM） | 调研档案 |
| 高层控制 | PC 运行 MyRobotLab（Java 框架，Python 绑定） | 调研档案 |
| 供电 | 通常台式电源（AC），移动底座版本可配电池 | 调研档案 |
| 新手友好度 | 3 / 5（调研档案评估） | 调研档案 |

### 执行器与机械

- 标准航模舵机（MG996R、HS-805BB 等社区常用型号），无定制执行器。
- 手部为腱（渔线）驱动五指，可抓握、比划手语级手势，是 InMoov 最具标志性的子系统（单手打印约 13–14 小时）；双手为全驱动五指（每手 5–6 舵机）。
- 设计软件为开源的 Blender；所有部件可在 12×12×12 cm 打印区间的家用 3D 打印机上复现。
- 工程量大：290 个零件、约 600 小时 3D 打印 + 约 400 小时装配调试（ESILV 学生团队报道口径）。

### 软件栈与传感器

- MyRobotLab（MRL）：服务化机器人框架，内置语音识别、OpenCV 视觉、聊天机器人（Program AB）、Web UI、手势捕捉等；主要面向交互而非运动控制。
- 社区有 ROS 移植（如 alansrobotlab/inmoov_ros，46 stars，2019 年后停更）；近年社区常见 Jetson/Raspberry Pi + LLM 的现代化改造。
- 传感器为社区自定义：双眼 USB 摄像头、麦克风（语音识别）、可选 Kinect/超声/IMU/RealSense。
- 无官方运动学/动力学仿真栈（Gazebo/Isaac/MuJoCo 均无官方支持）——它不是为行走研究设计的平台。

### 适合人群

- 适合：想低成本体验"造一台真人尺寸机器人"的 maker、艺术/教育/HRI 场景——零件全部家用打印机可造、舵机+Arduino 技术栈门槛低、社区大、做成后交互演示效果（语音、视觉、手势）震撼，是极佳的"机器人 maker 入门第一课"。
- 门槛：非商业许可限制商用；装配工程数百小时；没有腿、不能行走，动力学/RL/ROS 等现代人形技术栈在这里学不到；舵机精度与寿命有限。

## 参考

- [InMoov 官方项目页](https://inmoov.fr/project/)
- [MyRobotLab/myrobotlab GitHub 仓库](https://github.com/MyRobotLab/myrobotlab)
- [MyRobotLab/InMoov2（新一代构建包）](https://github.com/MyRobotLab/InMoov2)
