# Poppy Humanoid（罂粟人形机器人）调研档案

> 调研访问日期：2026-07-01。所有事实均附来源 URL（见文末）；未查到的信息标注"未知"。GitHub 星标等为检索时点快照。

## 基本信息

| 项目 | 内容 |
|---|---|
| 项目名 | Poppy Humanoid（Poppy 人形机器人，"Poppy"为注册商标） |
| 发起机构 | 法国 Inria Bordeaux Sud-Ouest 的 Flowers 团队（联合 Ensta ParisTech），2012 年启动，源于 Matthieu Lapeyre 的博士论文（导师 Pierre-Yves Oudeyer），ERC Explorer 资助；现由非营利组织 Poppy Station 维护社区 |
| 开源许可证 | 硬件 CC BY-SA 4.0；软件 GPLv3；文档 CC-BY-SA 4.0 |
| 硬件成本（BOM） | 约 €7,500–8,000（2014 年官方口径，其中电机约 €5,000）；Génération Robots 套件约 €9,000；社区估算全套约 €9,588 |
| 身高 / 重量 | 约 84 cm / 约 3.5 kg |
| 自由度 | 25（含 5 自由度全驱动仿生脊柱，屈膝式腿构型） |

## 执行器方案

- 25 台 **ROBOTIS Dynamixel 智能舵机**，TTL 串行总线级联；按关节扭矩需求混用 AX 系列（肢体小关节）与 MX 系列（躯干/大腿等高扭矩关节），装配手册注明 MX-28 已迭代为 MX-28AT。
- 高减速比舵机 + 串联弹性/柔顺模式：可手动反驱（compliant mode），适合"手把手"示教编程，这是 Poppy 教学设计的核心卖点。
- 全身结构件 3D 打印（家用打印机即可），骨架轻量化、仿生比例。

## 计算平台与传感器

- 主控：Raspberry Pi 3/4（或 Odroid），经 USB2AX / U2D2 接 Dynamixel 总线，无需额外 MCU。
- 传感器（2014 完整版配置）：16 个 FSR 力传感器、2 个 PS Eye 相机、1 个 IMU、4.3 英寸 LCD 屏、双麦克风。
- 供电：早期版本需外接电源（无电池），移动性受限。

## 软件栈

- **pypot**（项目自研 Python Dynamixel 库）+ 各机器人专属 Python 包；支持 Jupyter Notebook、Scratch/Snap! 图形化编程、REST API/Web 控制。
- 仿真：CoppeliaSim（原 V-REP）官方模型 + 轻量 3D Web 查看器，可零硬件开发调试。
- 提供 ROS 桥接（社区维护）；预配置系统镜像（SD 卡刷入即用）。

## 文档与教程质量

- docs.poppy-project.org 结构化文档（入门/装配/安装/编程四部分），25 步装配手册 + 25 集装配视频；文档最后更新于 2022-12-20，此后维护基本停滞。
- 教育与科研案例丰富（发展机器人学、HRI、行走研究数十篇论文），曾是全球机器人教育标杆项目。

## 社区活跃度

- GitHub `poppy-project/poppy-humanoid`：约 **1,007 stars / 281 forks**，但**最后 push 为 2021-12-06**，主仓库已多年停更。
- 论坛（forum.poppy-project.org）历史积累厚；第三方仍有衍生项目（如 Poppyrate 低成本改型、orobot.io 云控集成），但官方团队重心已转移，社区热度明显低于新兴项目。

## 新手友好度评估：3.5 / 5

- 优点：为教育而生——Python/Scratch 双轨、柔顺反驱示教、仿真先行、装配视频完整，是"零基础接触人形机器人"历史上最友好的平台之一。
- 门槛：约 €9,000 的套件价格远超当代替代品；主仓库停更意味着新系统/新 Python 版本兼容性要自己踩坑；25 台 Dynamixel 的采购与维护成本高。
- 适合：看重教学体系与人机交互（而非运动性能）的教育者；想做具身认知/HRI 研究的团队。想做行走/RL 的新手建议转看 ToddlerBot 等新一代平台。

## 来源 URL（访问日期 2026-07-01）

- https://github.com/poppy-project/poppy-humanoid （仓库与项目描述；星标与停更时间经 GitHub API 检索）
- https://docs.poppy-project.org/en/ （官方文档，CC-BY-SA 4.0，更新于 2022-12-20）
- https://docs.poppy-project.org/en/assembly-guides/poppy-humanoid/ （25 步装配手册、25 电机清单、MX-28→MX-28AT 说明）
- https://www.numerama.com/sciences/27530-poppy-un-robot-humanoiumlde-open-source-made-in-france.html （84 cm / 3.5 kg / 25 电机 / 16 FSR / 双相机 / Raspberry Pi / €7,500–8,000，2014）
- https://orobot.io/ （硬件 CC BY-SA 4.0、软件 GPLv3 许可证确认；25 DoF / Dynamixel 总线 / pypot 描述）
- https://eduengteam.com/projects-for-3d-printed-humanoid-robots/ （2012 年起源、Poppy Station、Raspberry Pi/Odroid、CoppeliaSim 仿真、Scratch/Python/ROS）
- https://blog.csdn.net/vandh/article/details/138169489 （社区估算总成本约 €9,588，2024）
- https://www.zecloud.fr/poppyrate/ （Génération Robots 套件约 €9,000；高成本主要来自 25 台高端舵机）
