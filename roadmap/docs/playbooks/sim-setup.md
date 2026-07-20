# 仿真环境从零搭建：先在数字世界里摔一万次

> ⚠️ 本路线图内容基于公开资料与理论知识整理，未经实机验证；涉及电气与机械操作时请自行核实安全规范。

人形机器人是最不该"先造出来再调"的硬件：真机摔一次是几百美元和一周工期，仿真里摔一万次不要钱。但仿真搭得不对，等于在物理学错误的世界里自我陶醉。本页六步走：选引擎 → 备模型 → 跑控制仿真 → 备 sim-to-real 工具箱 → 上基准 → 装环境。理论背景见 [第 23 章 仿真与物理引擎](/wiki/chapters/chapter-23/)，控制背景见 [第 14 章](/wiki/chapters/chapter-14/) 与 [第 15 章](/wiki/chapters/chapter-15/)。

## 第一步：选仿真引擎

**【做什么】** 先明确主任务，再对照下表选主力引擎（多数严肃团队用两个以上引擎交叉验证，降低单一引擎建模偏差的系统性风险——[第 23 章](/wiki/chapters/chapter-23/) 23.3.8 节的选型原则）：

| 引擎 | 物理内核 | 并行能力 | 渲染保真 | 接触质量 | 典型定位 |
|---|---|---|---|---|---|
| [MuJoCo](/entry/ent_software_mujoco_physics_engine_2022/) | 自研凸接触求解 | CPU 为主，MJX 提供 GPU 路线 | 中 | 高 | 控制研究、RL 训练 |
| [Isaac Sim](/entry/ent_software_nvidia_isaac_sim_2024/) + [Isaac Lab](/entry/ent_software_nvidia_isaac_lab_2024/) | PhysX | GPU 大规模并行 | 高（RTX 光追） | 中高 | 合成数据、大规模 RL |
| [Gazebo](/entry/ent_software_gazebo/) | ODE/Bullet/DART 等可选 | CPU 为主 | 中 | 中 | ROS 全栈集成测试 |
| [Genesis](/entry/ent_software_genesis_generative_physics_eng_2024/) | 自研统一求解器（刚体/软体/流体可微统一） | GPU 大规模并行 | 中高 | 中高（含软体） | 通用/生成式仿真 |
| [Drake](/entry/ent_software_drake_systems_toolbox_2024/) | 自研（hydroelastic 接触） | CPU | 中低 | 高（研究级） | 优化控制与形式化分析 |

（表据 [第 23 章](/wiki/chapters/chapter-23/) 23.3.8 节平台能力对比整理。）另有易混淆的角色：[Pinocchio](/entry/ent_software_pinocchio/) 不是仿真器，而是高效刚体动力学/运动学与解析导数计算的开源 C++ 库——做 MPC/WBC 时几乎必用它算动力学项，与仿真器互补。

**【为什么】** 各引擎立身之本不同：MuJoCo 把接触动力学表述为凸优化问题，接触平滑、物理一致性好，长期是腿足控制与深度 RL 论文的事实标准（第 23 章 23.3.1 节）；Isaac Sim 的核心优势是照片级渲染、支撑 GR00T 合成数据管道（来源：[Isaac Sim](/entry/ent_software_nvidia_isaac_sim_2024/) 卡片），Isaac Lab 在其上提供 RL 环境、奖励、域随机化的模块化抽象，内置 H1/G1 等人形任务示例；Gazebo 物理平庸但 ROS 生态无人能替；Drake 胜在动力学与数学规划的严谨联合；Genesis 把软体/可变形体统一进可微 GPU 框架，生态仍在积累。开源项目的实际选择可作锚点：ToddlerBot 用 MuJoCo/MJX 跑 PPO；Berkeley Humanoid Lite 基于 Isaac Lab；OpenLoong 的 MPC+WBC 框架部署在 MuJoCo；Upkie 用 PyBullet 零成本入门（来源：data/roadmap/research/ 各档案）。

**【你的情况怎么分析】** 按目标决策：

- **RL 行走/全身控制研究** → MuJoCo（要 GPU 大规模并行则 Isaac Lab），无 N 卡也玩得转。
- **视觉策略、VLA、合成数据** → Isaac Sim/Lab，前提是有一张支持 RTX 的 NVIDIA 显卡。
- **ROS/ROS2 全栈集成与导航** → Gazebo，别纠结物理精度。
- **MPC/WBC 算法推导与验证** → Drake + Pinocchio。
- 尝鲜**软体足底/柔性蒙皮交互** → 关注 Genesis，但别把它当唯一引擎。

## 第二步：准备机器人模型

**【做什么】** 四个动作：

1. **格式转换**：从 CAD 或现成仓库得到 [URDF（机器人描述格式）](/entry/ent_technology_urdf_robot_description_format_2024/)——ROS 生态的标准 XML 格式，描述连杆、关节、惯性与几何；再转为 [MJCF（MuJoCo 仿真格式）](/entry/ent_technology_mjcf_simulation_format_2024/)（MuJoCo 的 `compile` 可直接加载 URDF）。进 Isaac 还需再转一层 USD。Berkeley Humanoid Lite 同时维护 URDF/MJCF/USD 三种格式（来源：data/roadmap/research/berkeley-humanoid-lite.md），"三格式齐全"的习惯值得照抄。
2. **碰撞体简化**：绝不可把高面数视觉网格直接当碰撞体——碰撞检测会慢一到两个数量级，用凸包分解或球/胶囊/盒等 primitive 近似替代（来源：第 23 章 23.4.3 节）。
3. **惯性参数核对**：质量属性按"CAD 理论值 → 称重实测值 → 系统辨识修正值"分级采信，整机质心误差控制在毫米级，否则平衡控制器在实机上会持续"惊讶"（来源：第 23 章 23.4.4 节）。
4. **接触参数标定**：足底与地面的接触刚度、阻尼、摩擦系数按"足底材料-地面材料"成对标定，并纳入后续域随机化范围（来源：第 23 章 23.4.4 节）。

**【为什么】** URDF 为可视化与 ROS 工具链而生，只支持树状结构、执行器模型弱；MJCF 为仿真与控制而生——编译期自动计算惯性、原生闭链等式约束、执行器与传感器是一等公民（来源：第 23 章 23.4.1/23.4.2 节）。转换每步都有信息损耗：惯性张量丢失、关节方向与限位约定差异、渲染材质与物理材质是两套体系（来源：第 23 章 23.4.3 节）。模型"以假乱真"靠的不是引擎而是这些建模细节。

**【你的情况怎么分析】** 复刻开源机型：直接用官方维护的描述文件（如 Upkie 的 `upkie_description` URDF 仓库，来源：data/roadmap/research/upkie.md），精力放在核对零位与执行器参数上。自研机型：先导出简化 URDF 跑通站立再迭代细化，不要等 CAD 完美才进仿真。关节零位标定是仿真与实机对齐的第一步，ToddlerBot 为此设计了 3D 打印零点校准治具，1 分钟完成校准（来源：data/roadmap/research/toddlerbot.md）。

## 第三步：跑通控制仿真流程

**【做什么】** 按三级火箭推进，每级有明确的"过关"标志：

1. **PID 站立**：用关节位置环 PID 让机器人站直不倒。过关标志：静态站立 60 秒以上，轻推能恢复。2. **MPC 行走**：接入基于模型的步态控制。可用 Pinocchio 算动力学、配 QP 求解器搭 MPC；或直接复现 OpenLoong-Dyn-Control——基于 MPC + WBC，含行走、跳跃、盲踩障碍三个示例，可部署于 MuJoCo（来源：data/roadmap/research/openloong-qinglong.md）。过关标志：平地连续行走 100 步不摔、步速可调。
3. **RL 训练**：用 [PPO（近端策略优化）](/entry/ent_algorithm_ppo/) 训练行走/全身策略——它限制策略更新步长以避免破坏性更新、提高样本效率，是腿足 RL 的默认起点（来源：PPO 卡片）。Upkie 工程自带 PID、MPC、强化学习（Stable-Baselines3）三种平衡控制范式示例与 Gymnasium 接口（来源：data/roadmap/research/upkie.md），是对比三种范式的现成教材。训练方法详见 [第 18 章](/wiki/chapters/chapter-18/)。

**【为什么】** 三级火箭顺序不能乱：PID 站立验证**模型正确性**（零位、轴向、质量属性）；MPC 验证**动力学建模**（执行器模型、接触参数）；RL 是在确认"仿真可信"之后，才用算力换策略性能。ToddlerBot 与 BHL 都实现了 RL 行走策略的零样本 sim-to-real（来源：各自调研档案），前提正是模型校准做在了前面。

**【你的情况怎么分析】** 时间分配建议：新手在 PID 站立卡住不要慌，这阶段暴露的模型错误最便宜；有控制理论基础者可快速过完 PID，把精力放在 MPC 与 RL 的对比上——最终用哪套上机取决于执行器能力（舵机力控弱，RL 输出位置目标更现实；QDD 可力控，两者皆可行）。

## 第四步：备齐 sim-to-real 工具箱

**【做什么】** 三件工具，按"收缩差距、钝化敏感、工程兜底"的顺序配齐：

1. **[系统辨识（System Identification）](/entry/ent_method_system_identification/)**：用测量数据建模型，把仿真"拉向"现实。单关节用扫频/阶跃激励拟合增益、延迟、摩擦曲线；整机在约束下采集激励轨迹优化惯性参数（第 23 章 23.7.3 节）。ToddlerBot 的经验：同型号电机只做 1 次 sysID 即可迁移到全部 30 台电机（来源：data/roadmap/research/toddlerbot.md）。2. **[域随机化（Domain Randomization）](/entry/ent_method_domain_randomization/)**：训练时随机化仿真参数，让策略对剩余误差不敏感。人形典型随机化项：连杆质量与质心（±10% 量级）、关节摩擦与阻尼、地面摩擦、执行器增益与延迟、传感器噪声、外力推扰（第 23 章 23.7.2 节）。范围由 sysID 给先验——过宽学出保守策略，过窄迁移失败；可搭配观测历史让策略隐式在线辨识参数，或用"先窄后宽"的课程式收敛。
3. **[硬件在环（HIL）](/entry/ent_method_hardware_in_the_loop/)**：上机前的在环阶梯——SiL（软件在环验证逻辑）→ HIL（控制软件跑在真实车载平台上，经真实 EtherCAT/CAN 总线与实时仿真器闭环，验证实时性与通信时序）→ 单关节/单腿台架 → 吊架保护下整机首测（第 23 章 23.7.4 节）。
**【为什么】** 现实差距分三类：可参数化差距（质量、摩擦、延迟——sysID 收缩、域随机化覆盖）、结构性差距（齿隙、迟滞、软体变形——建模补充或结构规避）、感知分布差距（渲染与真实图像差异——视觉域随机化或真实数据混合）（第 23 章 23.7.1 节）。HIL 对仿真有特殊要求：必须按墙上时间同步推进（实时率 RTF = 1），超时即表现为控制器侧总线丢帧，故 HIL 用确定性调度与精简模型，而非 RL 训练的高吞吐变体（第 23 章 23.7.4 节）。

**【你的情况怎么分析】** 预算有限的个人开发者：sysID 一定要做（成本只是时间），域随机化一定要开（成本只是算力），HIL 可简化为"SiL + 单执行器台架"两级。机构团队做全尺寸机型：完整在环阶梯是安全底线，不可裁剪——80 kg 级机器首测必须吊架保护。

## 第五步：用基准测试量化你的策略

**【做什么】** 策略练成后，先在公开基准上跑分再谈上机：

- **[HumanoidBench](/entry/ent_benchmark_humanoidbench/)**：基于 Unitree H1 形态的全身人形基准，40 余项任务覆盖纯移动（行走、奔跑、平衡）、纯操作（伸取、搬运、插放）与移动-操作耦合三类，统一模型与环境参数使跨算法比较有意义（第 23 章 23.8.1 节与基准卡片）。
- **[ManiSkill](/entry/ent_benchmark_maniskill/)**：面向可泛化操作技能的统一基准，第三代 ManiSkill3 把物理并行与渲染并行同时 GPU 化，带视觉观测的操作任务也能高吞吐采样，配套演示数据与基线（第 23 章 23.3.7/23.8.2 节）。评测方法论见 [第 25 章 机器人评测体系](/wiki/chapters/chapter-25/)。

**【为什么】** 基准的价值是把"我训练得不错"从轶事变成可量化比较的协议；局限也要清楚——HumanoidBench 仅覆盖仿真且形态绑定 H1，向你的机型与真实硬件外推仍需额外验证（第 23 章 23.8.1 节）。工程上还应建"事故驱动场景库"：把每次实机失败转化为可复现的仿真用例纳入回归（第 23 章 23.8.3 节）。

**【你的情况怎么分析】** 做行走研究：先跑 HumanoidBench 移动类任务看相对排名；做操作：ManiSkill 的演示数据能省掉你自己采数据的几周时间；做产品化：公开基准只是入场券，私有场景库才是主体。

## 第六步：硬件配置与安装落地

**【做什么】** 按引擎准备硬件并安装：

- **MuJoCo 路线**：纯 CPU 即可，`pip install mujoco` 起步；ToddlerBot 证明"仿真 + RL 训练 + 部署"全链路可纯 Python、pip 一键安装（Python >= 3.10）（来源：data/roadmap/research/toddlerbot.md）。GPU 只对 MJX 大规模并行训练必要。
- **Isaac Sim/Lab 路线**：需支持 RTX 光追的 NVIDIA 显卡与匹配的驱动/CUDA 版本；具体显卡型号与显存下限随版本变化，需自行向供应商（官方文档）确认当前版本要求。
- **Genesis 路线**：GPU 加速，安装前确认其当前版本对 CUDA 的要求。
- **Upkie 式零成本上手**：`pixi`/`uv` 一条命令跑仿真示例，适合买硬件前先学控制（来源：data/roadmap/research/upkie.md）。

**【为什么】** 安装的坑九成集中在三处：NVIDIA 驱动与 CUDA toolkit 版本错配、headless 服务器缺显示环境（需 EGL/Vulkan 离屏渲染配置）、Python 环境混用导致动态库冲突。先让引擎官方示例跑起来，再加载自己的模型——隔离"环境问题"与"模型问题"。
**【你的情况怎么分析】** 只有笔记本（无 N 卡）：MuJoCo + CPU 训练完全可行，小型 MLP 策略以天计可接受；有一张 RTX 游戏卡：Isaac Lab 与 Genesis 都能跑，显存决定并行环境数；有服务器/多卡：才考虑 Isaac Gym 式数千并行环境与端到端 GPU 管线（观测与动作张量不出显存，第 23 章 23.3.3 节）。

## 验收标准

- 仿真器官方示例在你机器上跑通，且能说清为什么主选这个引擎（对照第一步选型表）。
- 机器人模型在仿真中：各关节轴向/限位逐一核对无误，碰撞体为简化几何，惯性参数来源有记录（CAD/称重/sysID 哪一级）。
- PID 站立、MPC 行走（或开源 MPC 示例复现）、PPO 行走训练三级流程至少完成前两级，每级有录屏与日志存档。
- sim-to-real 三件套有落地记录：sysID 数据与拟合参数、域随机化范围清单（注明依据）、SiL/HIL 测试报告。
- 至少在一个公开基准（HumanoidBench 或 ManiSkill）上跑出可复现的基线分数，命令与随机种子有记录。

## 常见坑与排查

| 症状 | 可能原因 | 排查动作 |
|---|---|---|
| URDF 转 MJCF 后机器人"散架"或抽搐 | 惯性参数缺失/错误、关节轴向约定差异 | 逐关节核对 `<origin>` 与 axis；检查每个 link 的 inertial 完整性；用 `simulate` 交互模式单关节激励测试 |
| 仿真帧率极低 | 高面数视觉网格被用作碰撞体 | 换凸包/primitive 碰撞体；为不可能相触的连杆对显式禁用碰撞对 |
| Isaac Sim 启动黑屏/闪退 | 驱动与 CUDA 版本错配、显存不足 | 核对官方版本兼容矩阵；`nvidia-smi` 确认驱动；降并行环境数或关光追试跑 |
| 无显示器服务器渲染报错 | 缺 EGL/Vulkan 离屏渲染配置 | 按引擎文档配置 headless 渲染环境变量；先跑纯物理不渲染验证 |
| RL 训练曲线不涨 | 奖励设计问题或物理步长/控制频率不匹配 | 先用官方基线环境复现；检查物理步进与策略步进的频率解耦设置 |
| sim-to-real 上机即摔 | 域随机化范围未覆盖真实参数、未做 sysID | 回做执行器扫频辨识；核对零位标定；把实机失败姿态在仿真里回放复现 |
| HIL 中控制器报总线丢帧 | 仿真未按实时率推进（RTF ≠ 1） | 换精简物理模型；实时内核 + 独占核跑仿真；监控每帧实际耗时 |

## 配套阅读

- [阶段 0 · 基础筑基](../stage-0-foundations.md) —— 仿真初体验的入门路径
- [阶段 2 · 双足平台](../stage-2-biped.md) —— 从仿真行走到 sim-to-real
- [路线图总览](../index.md)
