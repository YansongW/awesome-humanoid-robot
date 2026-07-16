# ROBOTIS OP3 / DARwIn-OP（达尔文开放平台人形机器人）调研档案

> 调研访问日期：2026-07-01。所有事实均附来源 URL（见文末）；未查到的信息标注"未知"。GitHub 星标等为检索时点快照。
> 说明：DARwIn-OP（2010，又名 ROBOTIS OP）、ROBOTIS OP2、ROBOTIS OP3 是同一产品线的三代，本档案合并介绍。

## 基本信息

| 项目 | 内容 |
|---|---|
| 项目名 | ROBOTIS OP3；前身 DARwIn-OP（Dynamic Anthropomorphic Robot with Intelligence – Open Platform，达尔文开放平台） |
| 发起机构 | DARwIn-OP 由 Virginia Tech RoMeLa（Dennis Hong 团队）牵头，联合 University of Pennsylvania、Purdue University 与韩国 ROBOTIS 开发，美国 NSF 资助；OP3 由 ROBOTIS 主导 |
| 开源许可证 | OP3 ROS 软件包 Apache-2.0（GitHub ROBOTIS-GIT）；DARwIn-OP 硬件 CAD 与软件历史上免费公开（SourceForge `darwinop` 项目页至今仍可访问，HTTP 200）；本质是"开放平台的商业整机"，非社区开源硬件项目 |
| 硬件成本 | OP3 现价 $13,764.35（robotis.us，2026 年页面快照）；Generation Robots 约 €12,113（含税）；DARwIn-OP 2010 年售价 $12,000（教育折扣 $9,600），第三方 3D 打印克隆约 $6,100 |
| 身高 / 重量 | OP3：约 510 mm / 约 3.5 kg（无外壳）；DARwIn-OP：455 mm / 2.8 kg |
| 自由度 | 20 |

## 执行器方案

- OP3：20 台 **DYNAMIXEL XM430-W350-R** 智能舵机（减速比 353.5:1，失速扭矩 4.1 N·m，支持电流环力控、DYNAMIXEL Protocol 2.0）。
- DARwIn-OP：20 台 MX-28（内置 maxon RE-max 电机，失速扭矩 2.5 N·m，Protocol 1.0）。
- 高减速比舵机方案：位置控制精度高、易用，但无本体感知力控能力，不适合高动态运动控制研究。

## 计算平台与传感器

- OP3 主控：Intel NUC（Core i3 双核、8GB DDR4、250GB M.2 SSD）；子控制器 OpenCR（替代 DARwIn-OP 的 CM-730）。
- 传感器：Logitech C920 摄像头、IMU（3 轴陀螺 + 3 轴加速度计 + 3 轴磁力计）、扬声器、RGB LED、4 按键。
- 电池：3 芯 11.1V LiPo（新版 3300 mAh），支持热插拔换电。
- DARwIn-OP 主控为 Intel Atom 级 SBC，USB 摄像头，配置已过时。

## 软件栈

- **2025 年 OP3 复刻版原生转向 ROS2**（e-Manual 口径），配套 DYNAMIXEL SDK，C++ 开发，Ubuntu 64 位。
- 官方提供行走/动作编辑（`op3_action_editor`）、Gazebo 仿真模型等 ROS 包；RoboCup 足球生态积累深厚。
- DARwIn-OP 时代软件支持 C++/Python/LabVIEW/MATLAB，曾获 RoboCup 2011、2012 儿童组冠军。

## 文档与教程质量

- ROBOTIS e-Manual 极其完善（规格、装配、教程、ROS 包逐条文档），是行业文档标杆。
- OP（DARwIn-OP）与 OP2 已停产（e-Manual 官方 WARNING）；OP3 为当前在售型号。

## 社区活跃度

- GitHub `ROBOTIS-GIT/ROBOTIS-OP3`：约 **157 stars / 65 forks**，最近 push 2025-02-26（伴随 2025 ROS2 复刻更新）。
- 学术用户基数大（RoboCup 社区），但代码托管分散，DARwIn-OP 原始代码在 SourceForge，现代化程度低。

## 新手友好度评估：3 / 5

- 优点：开箱即用的成熟产品、文档顶级、舵机即插即用、ROS2 生态入门路径清晰；对只想写上层算法不想造硬件的用户省事。
- 门槛：约 $1.4 万美元的价格对个人爱好者过高；"开源"主要体现在软件与 CAD 层面，整机只能买成品；舵机方案学不到准直驱/力控等当前主流技术。
- 适合：预算充足的学校/实验室教学与 RoboCup 参赛；不适合追求低成本 DIY 或前沿控制研究的新手。

## 来源 URL（访问日期 2026-07-01）

- https://emanual.robotis.com/docs/en/platform/op3/introduction/ （OP3 规格：510 mm / 3.5 kg / 20 DoF / XM430-W350 / NUC i3 / 2025 ROS2 复刻 / OP·OP2 停产提示）
- https://www.robotis.us/robotis-op3-us/ （OP3 美国售价 $13,764.35）
- https://www.generationrobots.com/en/402897-robotis-op-3.html （欧洲售价约 €12,113）
- https://github.com/ROBOTIS-GIT/ROBOTIS-OP3 （ROS 包，Apache-2.0；星标数据经 GitHub API 检索）
- https://www.romela.org/darwin-op-open-platform-humanoid-robot-for-research-and-education/ （DARwIn-OP 规格与 NSF 项目背景，455 mm / 2.8 kg）
- https://www.popsci.com/technology/article/2010-12/meet-darwin-op-americas-newest-humanoid-robot/ （DARwIn-OP 2010 售价 $12,000 / 教育价 $9,600，Humanoids 2010 发布）
- https://www.maxongroup.com/en/knowledge-and-support/blog/intelligent-robots-for-research-and-soccer-19310 （DARwIn-OP 开源属性、maxon 电机、RoboCup 2012 冠军）
- https://www.hackster.io/avatar/my-3d-printing-journey-to-create-a-darwin-op-clone-8e385e （克隆机成本约 $6,100，Virginia Tech RoMeLa + UPenn + Purdue + ROBOTIS 合作背景）
- https://sourceforge.net/projects/darwinop/ （DARwIn-OP 原始开源项目页，访问返回 200）
