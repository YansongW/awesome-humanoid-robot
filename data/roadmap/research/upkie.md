# Upkie（开源轮足双足机器人）调研档案【补充项目】

> 调研访问日期：2026-07-01。所有事实均附来源 URL（见文末）；未查到的信息标注"未知"。GitHub 星标等为检索时点快照。
> 入选理由：$3,000 级、文档极佳、纯 Python 即可上手的轮足（wheeled biped）平台，是个人从零做"会平衡的双足类机器人"最现实的路径之一。

## 基本信息

| 项目 | 内容 |
|---|---|
| 项目名 | Upkie（轮足双足机器人，含 Upkie Zero / Upkie Standard / 2026 硬件 v2 等构型） |
| 发起机构 | 社区开源项目，核心作者 Stéphane Caron（Inria）等；建立在 mjbots 开源执行器生态之上 |
| 开源许可证 | Apache-2.0（轮胎网格为 CC BY 4.0）；所用 mjbots 执行器的固件/硬件/软件同样全开源 |
| 硬件成本（BOM） | 约 **$3,000** 现成组件 + 60 小时以上 3D 打印（官方 hackaday 口径） |
| 身高 / 重量 | 未见官方统一数值（桌面级轮足机器人，因构型而异），**未知** |
| 自由度 | 6（每腿 3：髋、膝、驱动轮） |

## 执行器方案

- **mjbots qdd100 准直驱无刷伺服** ×4（髋/膝）+ moteus 驱动器（轮），全部固件开源、可力控。
- 轮足混合：靠轮保持平衡、靠腿应对不平地形——相比纯步行双足，控制难度与机械风险显著降低。

## 计算平台与传感器

- 主控：Raspberry Pi 4 + mjbots pi3hat（CAN 扩展板）+ 电源分配板；IMU 集成于 pi3hat。
- 可选 OAK-D Lite 相机支架等社区配件；2026 年 1 月发布硬件 v2：躯干一体化打印、腿部重新设计、宽度缩减 6 cm。

## 软件栈

- Python 或 C++，Linux/macOS 开发、部署到机上树莓派；`pixi`/`uv` 一条命令即可跑仿真示例（PyBullet）。
- 开箱自带三种平衡控制范式示例：**PID、MPC（qpmpc）、强化学习（Stable-Baselines3）**；Gymnasium 标准接口；另有社区 GPU RL 方案（MjLab Upkie）。
- 不依赖 ROS（可用 xacro/URDF 描述，兼容 Pinocchio 等库）。

## 文档与教程质量

- 逐步构建指南（step-by-step build instructions）+ Hackaday 项目页 + GitHub Discussions/聊天室；FOSDEM 2026 有官方经验分享演讲并现场发布硬件 v2。
- 仿真零成本上手（无需先买硬件），是真机前很好的学习路径。

## 社区活跃度

- GitHub `upkie/upkie`：**386 stars / 52 forks**，最近 push 2026-07-12（检索时点仍高频更新）；`upkie/parts`（CAD/打印件）、`upkie/upkie_description`（URDF）同步维护。
- 被 awesome-open-source-robots 等知名清单收录；中文创客社区（DFRobot 等）有翻译报道。

## 新手友好度评估：4 / 5

- 优点：$3k 价位、全开源到电机固件、文档完整、仿真先行、Python 栈；轮足形态避开了纯双足步行的调参地狱，成功率高、摔机代价小。
- 门槛：60+ 小时打印与装配仍需耐心；轮足不是"走路"的人形，若目标是仿人步态研究则不匹配。
- 适合：想在真实硬件上学平衡控制/RL 部署的个人开发者与课程项目；可作为进阶纯双足（Berkeley Humanoid Lite 等）前的练兵平台。

## 来源 URL（访问日期 2026-07-01）

- https://github.com/upkie/upkie （主仓库：构建/控制全部材料，Apache-2.0；星标经 GitHub API 检索）
- https://hackaday.io/project/185729-upkie-wheeled-biped-robots （官方项目页：$3,000 组件、60+ 小时打印、部件清单、2026-01 硬件 v2 发布说明）
- https://pypi.org/project/upkie/ （PyPI 文档：仿真示例、RL playgrounds、与 ODRI/mjbots 的生态关系）
- https://fosdem.org/2026/schedule/event/8PUMMD-open-source-robotics-practice-upkie-wheeled-bipeds/ （FOSDEM 2026 演讲：软件栈 Gymnasium/moteus/PyBullet、$3,000 成本、v2 发布）
- https://github.com/upkie/parts 与 https://github.com/upkie/upkie_description （3D 打印/CAD 与 URDF 描述仓库，Apache-2.0/CC BY 4.0 细节）
- https://mc.dfrobot.com.cn/thread-317789-1-1.html （中文社区报道：Upkie Zero 部件清单与成本口径）
