# BRUCE（Westwood Robotics 儿童尺寸开源人形平台）调研档案

> 调研访问日期：2026-07-01。所有事实均附来源 URL（见文末）；未查到的信息标注"未知"。GitHub 星标等为检索时点快照。

## 基本信息

| 项目 | 内容 |
|---|---|
| 项目名 | BRUCE（Bipedal Robot Unit with Compliance Enhanced） |
| 发起机构 | Westwood Robotics（西木科技，2018 年由 UCLA RoMeLa 前核心成员创立）与 UCLA RoMeLa 联合开发；设计论文 Liu et al., ICRA 2022 |
| 开源许可证 | 官方定位为"开放平台（open platform）"，宣称开源软件与模型；但**整机控制框架的公开仓库在 GitHub 检索中未找到**（截至 2026-07-01，未能直接验证其许可证条款）；组件级仓库（PyBEAR、BRUCE_SENSE、Wireless_ESTOP 等）开源于 `Westwood-Robotics` 组织 |
| 硬件成本 | 第三方论文对比表（ToddlerBot, arXiv:2502.00893 Table I）列为约 **$6.5K** 量级（"code"级开源）；官方页面为询价制，未公开标价 |
| 身高 / 重量 | 70 cm / 4.8 kg |
| 自由度 | 16（每条腿 5、每条臂 3） |

## 执行器方案

- 自研 **Koala BEAR 本体感知（proprioceptive）准直驱执行器**：单台仅 250 g，峰值扭矩 10.5 N·m（腿部关节口径）；关键关节（膝等）采用**液态冷却**以支撑爆发力矩与持续高动态输出。
- 碳纤维复合材料骨架，拓扑优化，高度模块化，便于维修更换——其技术血统与 UCLA ARTEMIS 的 BEAR 系列执行器一致（半直驱/QDD 路线）。

## 计算平台与传感器

- 主控：算力 6 TOPS、8GB 内存、32GB 存储，支持主流深度学习框架（展品页口径）。
- 传感器：4 个足底接触传感器；6 轴 IMU，通信/采样速率 2 kHz。
- 电池：3000 mAh，连续动态运行约 20 分钟；独立无线急停装置；SSH 经 Wi-Fi/蓝牙控制。

## 软件栈

- 可变周期（variable-frequency）MPC 运控算法，支持行走/跑步/跳跃等高动态行为；模型库与仿真环境被多篇第三方论文用作 benchmark（如 arXiv:2511.00840 的步态规划对比研究）。
- 官方宣称"开源软件和模型""积极迭代 GitHub Repo 和 Wiki"；实际公开内容以执行器（PyBEAR）、传感（BRUCE_SENSE）、无线急停等组件级仓库为主。
- 无 ROS/ROS2 官方栈的公开证据（未检索到）；支持主流 DL 框架。

## 文档与教程质量

- 官方提供 Wiki 与 GitHub 文档（展品页自述"积极迭代"）；UCL 等高校将其列为科研平台并建有实验页面。
- 因其主要面向专业开发者与科研机构销售，公开新手向教程有限；获取渠道为商务采购而非自助复刻。

## 社区活跃度

- GitHub `Westwood-Robotics` 组织：PyBEAR 13 stars（2025-08 更新）、BRUCE_SENSE 7 stars、Wireless_ESTOP 5 stars（2025-11 更新）、THEMIS-Simulation-Model（2026-05 更新）——组件级维护在持续，但星数很低。
- 整机被多所欧美大学与研究公司采用（官方与 UCL 页面口径），学术引用（RoMeLa/第三方论文）是其主要社区存在形式；无公开 Discord/论坛类社区。

## 新手友好度评估：2 / 5

- 优点：70 cm / 4.8 kg 的小体型 + 准直驱 + 液冷，是"能跑能跳"的少数派小型高动态双足平台；BEAR 执行器与 MPC 栈对研究高动态运控的人很有价值。
- 门槛：整机开源程度存疑（公开仓库只见组件级），个人无法自助复刻，只能商务采购；文档面向专业用户；$6.5K 级价位叠加采购流程，对新手不友好。
- 适合：高校实验室做高动态双足运控研究；新手可关注其开源组件（PyBEAR 等）学习准直驱执行器，但不建议作为 0→1 首台机器人。

## 来源 URL（访问日期 2026-07-01）

- https://www.worldrobotconference.com/ex/product/244.html （WRC 展品页：16 DoF、70 cm/4.8 kg、250 g/8 N·m 执行器、液冷、6 TOPS、3000 mAh、可变周期 MPC、开源软件与模型）
- https://www.aparobot.com/robots/bruce （Koala BEAR 液冷执行器、4 接触传感器 + IMU 2 kHz、碳纤维、约 20 分钟续航）
- https://arxiv.org/html/2511.00840v2 （第三方论文：BRUCE 源自 RoMeLa × Westwood，70 cm / 4.8 kg，用作 locomotion benchmark）
- https://arxiv.org/html/2502.00893v2 （ToddlerBot 论文对比表：BRUCE $6.5K、"code"级开源）
- https://www.roboticssummit.com/westwood-robotics-debuting-next-gen-themis-humanoid/ （Westwood Robotics 2018 年创立背景、BRUCE 定位 STEAM 教育与科研开放平台）
- https://github.com/Westwood-Robotics （组件级开源仓库：PyBEAR、BRUCE_SENSE、Wireless_ESTOP；星标经 GitHub API 检索；整机仓库未检索到）
- https://rpl-as-ucl.github.io/robots/ （UCL 实验室采用 BRUCE 作为科研平台）
- https://finance.sina.com.cn/stock/stockzmt/2024-02-17/doc-inaiiazh3494409.shtml （行业报告：Koala BEAR 250 g / 峰值 10.5 N·m、半直驱路线、与 ARTEMIS BEAR 的技术关系）
