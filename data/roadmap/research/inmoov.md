# InMoov（开源 3D 打印真人尺寸人形机器人）调研档案

> 调研访问日期：2026-07-01。所有事实均附来源 URL（见文末）；未查到的信息标注"未知"。GitHub 星标等为检索时点快照。

## 基本信息

| 项目 | 内容 |
|---|---|
| 项目名 | InMoov（无官方中文名，社区多直呼 InMoov） |
| 发起机构 | 个人开源项目：法国雕塑家/模型师 Gaël Langevin（Factice Ateliers），2012 年 1 月发起；软件生态依托 MyRobotLab 社区 |
| 开源许可证 | 3D 打印部件：CC BY-NC 3.0（署名-非商业）；MyRobotLab 框架历史上 GPLv2，现 GitHub 仓库标注 Apache-2.0 |
| 硬件成本（BOM） | 无官方 BOM；媒体估算：约 $800（2015 年整机报道）；$900+ 且不含躯干与头部（2013 年报道）；$800–2,500 视舵机/电子件选型（2025 年第三方数据库） |
| 身高 / 重量 | 真人尺寸（约 1.75–1.8 m 的报道口径）；默认仅为上半身（头、躯干、双臂、双手），无腿；重量因构建而异（第三方报道约 30 kg，非官方数据） |
| 自由度 | 因构建者而异；典型全构建约 28 台舵机、22–30 个可控自由度（第三方数据库口径），另有"约 45 关节"的报道口径；双手为全驱动五指（每手 5–6 舵机腱驱动） |

## 执行器方案

- 标准航模舵机（MG996R、HS-805BB 等社区常用型号），无定制执行器。
- 手部为**腱（渔线）驱动五指**，可抓握、比划手语级手势，是 InMoov 最具标志性的子系统（单手打印约 13–14 小时）。
- 设计软件为开源的 Blender；所有部件可在 12×12×12 cm 打印区间的家用 3D 打印机上复现。

## 计算平台与传感器

- 低层控制：Arduino Mega（舵机 PWM）；高层控制：PC 运行 MyRobotLab（Java 框架，Python 绑定）。
- 传感器为社区自定义：双眼 USB 摄像头、麦克风（语音识别）、可选 Kinect/超声/IMU/RealSense。
- 供电：通常台式电源（AC），移动底座版本可配电池。
- 官方"神经板"（Nervo Board）等转接件可在 inmoov.fr 商店购买。

## 软件栈

- **MyRobotLab（MRL）**：服务化机器人框架，内置语音识别、OpenCV 视觉、聊天机器人（Program AB）、Web UI、手势捕捉等；主要面向交互而非运动控制。
- 社区有 ROS 移植（如 `alansrobotlab/inmoov_ros`，46 stars，2019 年后停更）；近年社区常见 Jetson/Raspberry Pi + LLM 的现代化改造。
- 无官方运动学/动力学仿真栈（Gazebo/Isaac/MuJoCo 均无官方支持）——它不是为行走研究设计的平台。

## 文档与教程质量

- inmoov.fr 提供分部位构建指南（手→前臂→臂→头→躯干），STL 经官网与 Thingiverse 分发；社区论坛与全球 builder 博客生态成熟。
- 工程量大：290 个零件、约 600 小时 3D 打印 + 约 400 小时装配调试（ESILV 学生团队报道口径）。
- 到 2018 年，全球已有近 1,000 台 InMoov 复制机（ESILV 报道），是历史上被复制最多的开源人形机器人。

## 社区活跃度

- GitHub：`MyRobotLab/myrobotlab` 约 **257 stars**，最近 push 2026-06-15（活跃）；`MyRobotLab/InMoov` 145 stars（2025-01 停更）；`MyRobotLab/InMoov2`（新一代）37 stars，最近 push 2026-06-11（活跃）。
- 主设计分发在官网/Thingiverse 而非 GitHub，GitHub 星标不能反映真实社区规模；论坛与线下 maker 社区仍有人维护。

## 新手友好度评估：3 / 5

- 优点：成本可低至数百美元、零件全部家用打印机可造、舵机+Arduino 技术栈门槛低、社区大、做成后交互演示效果（语音、视觉、手势）震撼，是极佳的"机器人 maker 入门第一课"。
- 门槛：非商业许可限制商用；装配工程数百小时；**没有腿、不能行走**，动力学/RL/ROS 等现代人形技术栈在这里学不到；舵机精度与寿命有限。
- 适合：想低成本体验"造一台真人尺寸机器人"的 maker、艺术/教育/HRI 场景；不适合以双足行走或运动控制为学习目标的新手。

## 来源 URL（访问日期 2026-07-01）

- https://inmoov.fr/project/ （项目官方介绍：2012 年 1 月发起、首个 3D 打印真人尺寸开源机器人、Blender + MyRobotLab、CC BY-NC 许可）
- https://github.com/MyRobotLab/myrobotlab 与 https://github.com/MyRobotLab/InMoov2 （软件框架与新一代构建包；星标与更新时间经 GitHub API 检索）
- https://github.com/DamageStudios/inMoov （第三方镜像：CC BY-NC 3.0、MRL GPLv2 历史许可证说明）
- https://www.roboticmagazine.com/hobby-kits-toys/3d-printed-robot-diy-inmoov （2013 年成本报道：不含躯干头部已超 $900）
- https://gadizmo.com/inmoov-the-diy-humanoid-robot-you-can-print-from-home.php （2015 年报道：约 $800、单手打印 13–14 小时）
- https://humanoid.press/database/humanoid-press-database-inmoov/ （第三方数据库：$800–2,500 成本区间、~45 关节、舵机型号、传感器/计算配置汇总）
- https://www.humanoid-robots.io/robot/inmoov-by-inmoov （第三方数据库：175 cm、约 30 kg、22–30 DoF——非官方口径）
- https://www.esilv.fr/en/a-3d-printed-open-source-robot-davincibot-and-the-inmoov-project/ （290 零件 / 600 小时打印 / 400 小时装配 / 全球近千台复制，2018）
- https://library.iated.org/view/FORMANEK2023INM （学术使用报告：MRL 在课堂场景的局限与 ROS 移植动机）
