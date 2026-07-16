# OpenLoong / 青龙（国家地方共建人形机器人创新中心开源项目）调研档案

> 调研访问日期：2026-07-01。所有事实均附来源 URL（见文末）；未查到的信息标注"未知"。GitHub 星标等为检索时点快照。

## 基本信息

| 项目 | 内容 |
|---|---|
| 项目名 | OpenLoong（开放龙）/ "青龙"（Qinglong）开源人形机器人公版机 |
| 发起机构 | 国家地方共建人形机器人创新中心（上海，2023-12-28 成立、2024-05-17 揭牌）与人形机器人（上海）有限公司；2024-12-19 通过开放原子开源基金会（OpenAtom）TOC 评审，捐赠基金会孵化运营 |
| 开源许可证 | 主要代码仓库 Apache-2.0；OpenLoong-Hardware、OpenLoong-Dataset 许可证为自定义/未明确（GitHub 标记 NOASSERTION） |
| 硬件成本（BOM） | **未知**——开源公版机不自售，媒体口径"最终由生产商定价"；2025-08 社区另推出更轻量、更低成本的 NanoLoong（小型双足）并已开源 |
| 身高 / 重量 | 185 cm / 80 kg+（媒体与官方演讲口径为"身高超 185 cm、体重超 80 kg"） |
| 自由度 | 全身 43 个主动自由度（含五指灵巧手，覆盖头/臂/腿/腰/踝） |

## 执行器方案

- 2024 款"青龙"以**旋转执行器**为主驱动单元（2024 WAIC 官方演讲口径）；下一代公版机（生肖命名，演讲中称 "Deep Snake"）计划采用直线执行器。
- 具体电机/减速器型号、扭矩参数：在公开检索中未见统一规格表，详见 OpenLoong-Hardware 仓库的选型文件；**未知**项不臆造。
- 总线：EtherCAT（行业分析文章与 SDK 仓库均可佐证）。

## 计算平台与传感器

- 主控：搭载 400 TOPS 高算力控制器（2024 WAIC 发布口径）；具身智能操作系统（us 级响应目标）。
- 传感器：官方未发布统一传感器清单；生态项目（dora-rs/dora-openloong）实机集成 Intel RealSense D435 RGB-D 相机与麦克风阵列；硬件仓库含传感器选型与布局设计。
- 软件层另有"朱雀"大脑大模型、"玄武"小脑强化学习模型、"白虎"数据集、"麒麟"训练场等配套体系（属创新中心整体生态，非全部开源）。

## 软件栈

- **OpenLoong-Dyn-Control**：基于 MPC + WBC 的全身动力学控制框架，可部署于 MuJoCo 仿真，提供行走/跳跃/盲踩障碍三个示例，已在实物样机实现行走与盲踩障碍；内置主要依赖、分层模块化、强调易部署/易扩展/易理解。
- 其他仓库：Gymloong（训练平台）、MiniGym、Unity-RL-Playground（Unity RL 仿真）、OpenLoong-ROS、OpenLoong-Brain（大模型技能调度）、loong_driver_sdk（硬件驱动）、loong_sim/loong_deployment、OpenLoong-Dataset（行走/桌面分拣/场景作业数据）。
- 同步发布于 GitHub（`loongOpen` 组织）与 AtomGit（atomgit.com/openloong）。

## 文档与教程质量

- openloong.org.cn 社区 + SIG 组 + 线上线下活动（ROSCon China、ROS 暑期学校合作）；硬件开源包含设计指标、STEP 模型、电路原理图、安装维护手册。
- 中文文档为主，对国内开发者友好；英文资料少，国际化程度有限。
- 目标定位是产业"公版机/根技术"（对标 ROS 时刻），而非个人 DIY 教程，个人复现指导弱于 Berkeley/ToddlerBot 类项目。

## 社区活跃度

- GitHub `loongOpen` 组织（星标快照）：OpenLoong-Dyn-Control **339 stars**（2025-05-27 更新）；Unity-RL-Playground **315 stars**（2026-01-04）；OpenLoong-Hardware **115 stars**（2025-09-05）；Gymloong 90 stars；loong_driver_sdk 最新 push 2026-07-11（组织整体在维护）。
- 绝对星数不高，但有国家级生态背书与持续活动投入；国内媒体报道密度高。

## 新手友好度评估：2 / 5

- 优点：全球唯一的**全尺寸**人形全栈开源（硬件图纸 + MPC/WBC 控制 + 数据集）；中文资料；MuJoCo 仿真框架可以零硬件学习全身控制；NanoLoong 降低了实体门槛。
- 门槛：185 cm / 80 kg 全尺寸机型**个人无法在家复现**（加工、装配、安全均需机构级条件）；硬件许可证条款不够清晰；文档偏工程交付而非教学。
- 适合：国内高校/企业团队做全尺寸整机二次开发；个人新手建议只用其 MuJoCo 控制框架做学习，或关注 NanoLoong。

## 来源 URL（访问日期 2026-07-01）

- https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/main/README-zh.md （MPC+WBC 框架、MuJoCo 部署、运营主体说明；星标数据经 GitHub API 检索）
- https://www.cnblogs.com/jzssuanfa/p/19738897 （项目定位：全球首个全尺寸人形全栈开源、捐赠开放原子、"一高五难"、185 cm）
- https://www.163.com/dy/article/JLKV2OVS0511D0C3.html （开放原子 TOC 评审、43 自由度、185 cm/80 kg+、开源内容清单、GitHub/AtomGit 地址）
- https://www.leaderobot.com/news/5038 （硬件/软件/数据集全栈开源细节，2025-01）
- https://zhidao.baidu.com/question/1907415746738493860.html （2024 WAIC 官方演讲纪要转载：旋转执行器为主驱动、400 TOPS 算力、生肖公版机路线；一手页面未能直接验证）
- https://www.jiuyangongshe.com/a/10lrbcvet8x （青龙基于 EtherCAT 总线）
- https://github.com/dora-rs/dora-openloong （生态项目：RealSense D435 + 麦克风阵列实机集成）
- http://mp.weixin.qq.com/s?__biz=Mzk0MTg4NDE0Nw==&mid=2247486157&idx=1&sn=7293bd9df366f9883c8363f2f5b445f2 （NanoLoong 发布与开源，2025-08）
- https://sei.ecnu.edu.cn/87/ce/c33170a755662/page.htm （社区生态活动，2026-04）
- https://atomgit.com/openloong （AtomGit 镜像，未直接打开验证，地址引自媒体报道）
