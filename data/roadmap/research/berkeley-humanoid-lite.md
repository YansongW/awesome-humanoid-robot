# Berkeley Humanoid Lite（伯克利轻量人形机器人）调研档案

> 调研访问日期：2026-07-01。所有事实均附来源 URL（见文末）；未查到的信息标注"未知"。GitHub 星标等为检索时点快照。

## 基本信息

| 项目 | 内容 |
|---|---|
| 项目名 | Berkeley Humanoid Lite（伯克利轻量人形机器人） |
| 发起机构 | UC Berkeley 混合机器人实验室（Hybrid Robotics Group，Koushil Sreenath 团队）与 SLICE 实验室；属 BAIR Commons HIC 仓库 |
| 开源许可证 | 代码 MIT License；CAD 等其他资产 CC BY-SA 4.0 |
| 硬件成本（BOM） | 整机 BOM：美国采购约 $4,312，中国采购约 $3,236（论文/技术报告 BOM 表）；官方宣传口径"低于 $5,000" |
| 身高 / 重量 | 0.8 m / 16 kg |
| 自由度 | 22 个主动自由度（每条腿 6、每条臂 5，论文对比表）；另有成人尺寸扩展构型（7 自由度腿 + 灵巧手） |
| 论文 | arXiv:2504.17249（2025-04） |

## 执行器方案

- 两种规格自研准直驱执行器：6512（10 台）与 5010（12 台），核心为 **3D 打印摆线针轮（cycloidal）减速器**，全部结构件可用普通桌面 FDM 打印机（PLA）制造。
- 6512 执行器 BOM 约 $188（美国）/ $157（中国）：MAD Components M6C12 150KV 无人机无刷电机（$129）+ ST B-G431B-ESC1 驱动板（$19）+ AS5600 磁编码器（$3）+ 轴承/紧固件/打印件。
- 摆线齿轮多齿分担载荷，论文用 60 小时耐久测试验证塑料齿轮可靠性；也兼容 Moteus / ODrive / VESC 等第三方驱动器。

## 计算平台与传感器

- 主控：Intel N95 迷你 PC（约 $129），置于躯干；同时跑底层控制与 RL 策略部署。
- 通信：四肢各一条 CAN 2.0 总线（1 Mbps，经 USB-CAN 适配器接入），执行器与 IMU 通信速率 250 Hz；单条 CAN 总线最多 64 设备，便于重构成四足/双足/半人马等形态。
- 传感器：BNO085 IMU（手机级，经 Arduino 以 USB 接入）；遥操作用 SteamVR 基站 + 手柄。
- 电池：6S 4000 mAh LiPo，约 30 分钟续航，可外接电源。

## 软件栈

- 训练与仿真：基于 **NVIDIA Isaac Lab** 组织目录结构（URDF / MJCF / USD 三种描述格式齐全），支持策略训练、sim2sim 验证；RL 运动控制策略实现**零样本 sim-to-real**。
- 部署：`berkeley_humanoid_lite_lowlevel` 子目录为真机底层代码（C 语言，独立于训练栈），单独拷到机上即可部署。
- 还支持动捕、SteamVR 遥操作双臂（魔方、写字、搭积木演示）。

## 文档与教程质量

- 官方 GitBook 文档站（GitHub README 有 Documentation 入口），覆盖软硬件搭建；CAD 与 3D 打印文件通过 GitHub Releases 发布。
- 论文与 Berkeley EECS 技术报告（EECS-2025-207）给出完整 BOM 表、执行器测试数据，透明度高。
- 组装周期：现货件一周内到货，打印约一周，整机组装约 3 天（论文口径）。

## 社区活跃度

- GitHub `HybridRobotics/Berkeley-Humanoid-Lite`：**约 1,417 stars / 215 forks**，创建于 2025-03-17，最近 push 2026-03-10（活跃）。
- 有 Discord 社区与微信群（官网挂出入群二维码）。

## 新手友好度评估：3.5 / 5

- 优点：$4-5k 就能造出能跑 RL 行走的 22 自由度人形，文档 + BOM + 打印文件齐全，社区活跃，性价比在开源人形里属第一梯队。
- 门槛：需要自己打印摆线减速器并装配 22 台执行器、焊接 CAN 总线、烧录 FOC 固件，嵌入式与 3D 打印经验不足者容易卡壳；16 kg 机型已需要一定的操作安全意识。
- 适合：有一定动手能力、目标是做 RL 运动控制研究的个人/实验室，而非零基础爱好者。

## 来源 URL（访问日期 2026-07-01）

- https://github.com/HybridRobotics/Berkeley-Humanoid-Lite （仓库、许可证、模块结构；星标数据经 GitHub API 检索）
- https://lite.berkeley-humanoid.org/ （项目主页、性能指标定义、社区入口）
- https://arxiv.org/abs/2504.17249 （论文摘要：sub-$5,000、摆线减速器、零样本迁移）
- https://arxiv.org/html/2504.17249v1 （系统设计：0.8 m / 16 kg / Intel N95 / CAN / BOM 表 / 执行器细节）
- https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/Archive/EECS-2025-207.pdf （技术报告：完整 BOM 美国 $4,312 / 中国 $3,236，对比表 22 DoF）
