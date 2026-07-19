# 计算平台选型：给机器人装一个"分层大脑"

> ⚠️ 本路线图内容基于公开资料与理论知识整理，未经实机验证；涉及电气与机械操作时请自行核实安全规范。

很多人攒人形机器人时第一个问题就是"买 Jetson 还是 NUC"。这是个错误的第一问。正确的第一问是：你的机器人身上到底跑哪几类计算任务，各自的延迟底线和失效后果是什么。选型的本质不是比哪块板子 TOPS 高，而是把任务分层之后，给每一层配上刚好好用的算力——多了浪费电池和预算，少了轻则步态发飘、重则当场摔倒。本页按四步走：分层 → 选平台 → 定实时性方案 → 评估端侧 VLA 推理。理论背景见 [第 6 章 计算、电源与热管理](/wiki/chapters/chapter-06/) 与 [第 22 章 软件中间件](/wiki/chapters/chapter-22/)。

## 第一步：把算力需求分成三层

**【做什么】** 拿一张纸，把你规划中的全部计算任务列出来，按"控制周期 × 失效后果"分到三层：

- **L0 底层实时层**：关节伺服环、力控、安全监控。关节电流环、力控和平衡控制通常要求 0.5–2 ms 的硬实时周期（见 [第 6 章](/wiki/chapters/chapter-06/) 6.4.7 节），超时即失稳。安全相关功能（急停、看门狗、过流/过温监控）必须放在独立于主控的 [安全 MCU（Safety Microcontroller Unit）](/entry/ent_component_safety_mcu/) 上——它在主计算单元死机时依然能切断动力。
- **L1 中层规划层**：状态估计、步态生成、MPC（模型预测控制）、全身控制（WBC）。典型频率 50–500 Hz，允许微秒到毫秒级抖动，但要求稳定的平均吞吐。
- **L2 上层智能层**：视觉感知、SLAM、语音、VLA（视觉-语言-动作）模型推理。频率 1–30 Hz 即可，单帧延迟大一点只是"反应慢半拍"，不会直接摔机。

**【为什么】** 三层的约束完全不同：L0 要的是**确定性**（determinism），不是算力；L2 要的是**峰值吞吐**（TOPS）与显存带宽，恰恰不要实时性保证。用一台不保证实时的 x86 主机直接跑 1 kHz 力控，等于把机器人的平衡交给操作系统的调度运气；反过来，为用不完的 TOPS 买单，会直接吃掉电池预算——ToddlerBot 的续航测试就是在机上推理时"过热降频为止"只坚持了 19 分钟（来源：data/roadmap/research/toddlerbot.md）。分层的深层原理是异构计算趋势：未来主控将是 CPU + GPU + NPU + 功能安全 MCU 的异构组合（参见 [安全 MCU](/entry/ent_component_safety_mcu/) 卡片中的趋势总结）。

**【你的情况怎么分析】** 关键看你的执行器方案：

- 用 **Dynamixel 总线舵机**（位置环在舵机固件里）：L0 已经被外包，主控只需几十 Hz 发位置指令。ToddlerBot 用现成通信板在 2 Mbps 波特率下实现 30 台电机全状态 50 Hz 反馈（来源：data/roadmap/research/toddlerbot.md），这种情况下 L0 层几乎可以不买专门硬件。
- 用 **自研准直驱（QDD）执行器**：电流环/力矩环在驱动板上，但上层力控闭环仍要 250 Hz–1 kHz。Berkeley Humanoid Lite 的做法是四肢各一条 CAN 2.0 总线（1 Mbps），执行器与 IMU 以 250 Hz 通信（来源：data/roadmap/research/berkeley-humanoid-lite.md），主控跑实时 Linux 即可胜任。
- 做 **全尺寸机型或要走功能安全认证**：安全 MCU 这一层不能省，且要考虑 ISO 13849、IEC 61508 等功能安全标准（来源：[安全 MCU](/entry/ent_component_safety_mcu/) 卡片）。

## 第二步：候选平台对比与真实案例

**【做什么】** 按第一步的分层结果，为 L1+L2 层（通常合一或分二）从下面四类候选中选主控：

| 平台 | AI 算力 | 功耗 | 价格 | 生态 | 实时性定位 |
|---|---|---|---|---|---|
| [NVIDIA Jetson AGX Orin](/entry/ent_component_nvidia_jetson_agx_orin_2024/) 64GB | 最高 275 TOPS (INT8) | 15–60 W 可配置 | 开发者套件约 1,999 USD（第三方参考价） | JetPack / Isaac ROS / Isaac Sim 统一生态，16 通道 MIPI CSI-2 | 软实时（配 PREEMPT_RT），L1+L2 通吃 |
| Jetson Orin NX 16GB | 最高 157 TOPS | 10–40 W | 需自行向供应商确认 | 同 AGX Orin 生态，尺寸更小 | 软实时，L2 为主、兼顾 L1 |
| [NVIDIA Jetson Thor](/entry/ent_component_nvidia_jetson_thor/) | Blackwell 架构，面向端侧 VLA/VLM 设计；具体 TOPS 需自行向供应商确认 | 75–120 W 级（来源：[安全 MCU](/entry/ent_component_safety_mcu/) 卡片） | 需自行向供应商确认 | 面向"物理 AI"的旗舰生态 | L2 专用，L0/L1 需另配 |
| Intel N95 迷你 PC | 无专用 NPU，AI 算力以 CPU/集显为主（具体 TOPS 需自行向供应商确认） | 低功耗 x86（具体 TDP 需自行向供应商确认） | 约 129 USD（来源：data/roadmap/research/berkeley-humanoid-lite.md） | 标准 x86 Linux/ROS 生态 | 软实时，L1 够用、L2 只能跑小模型 |
| Intel NUC（Core i3 级） | 同上 | 同上 | 整机级价格，需自行向供应商确认 | 成熟 ROS/ROS2 生态 | 软实时，教学/开发定位 |
| 树莓派（Raspberry Pi 4） | 无 AI 加速器，仅 CPU | 单板级低功耗（具体数值需自行向供应商确认） | 需自行向供应商确认 | 社区生态极大、Python 友好 | 软实时，仅 L1 轻量控制 |

（Orin 系列算力/功耗/价格来源：[Jetson AGX Orin](/entry/ent_component_nvidia_jetson_agx_orin_2024/) 卡片及其竞争对比表。）

再看五个真实开源项目是怎么选的（来源均为 data/roadmap/research/ 调研档案）：

- **ToddlerBot（斯坦福）→ Jetson Orin NX 16GB**：要在机上跑 300M 参数扩散策略（约 100 ms 推理延迟）和 10 Hz 立体深度估计，必须有机上 GPU，Orin NX 是性能/体积的平衡点。
- **Berkeley Humanoid Lite → Intel N95 迷你 PC（约 $129）**：RL 行走策略的网络很小，N95 同时跑底层控制与策略部署就够了，把预算全让给了 22 台执行器。
- **Upkie → Raspberry Pi 4 + mjbots pi3hat（CAN 扩展板）**：轮足平衡控制的 PID/MPC/RL 示例全是小模型，树莓派 + CAN 扩展板是最省心的组合。
- **ROBOTIS OP3 → Intel NUC（Core i3 双核、8GB DDR4、250GB M.2 SSD）+ OpenCR 子控制器**：典型的 L1/L2 在 x86 主机、L0 在微控制器的双板分工。
- **OpenLoong 青龙 → 400 TOPS 高算力控制器 + EtherCAT 总线**：全尺寸 43 自由度公版机，上层大模型调度需要大算力（2024 WAIC 发布口径，一手页面未能直接验证，引用时注意）。

**【为什么】** 规律很清楚：**执行器越"笨"（舵机）、策略越小，主控越便宜；机上要跑大模型，才轮到 Jetson 出场。** Orin 系列的核心卖点不是 TOPS 数字本身，而是"统一生态"——JetPack SDK、Isaac ROS 与 Isaac Sim 让仿真里训练的策略能近乎原样部署到机上（来源：[Jetson AGX Orin](/entry/ent_component_nvidia_jetson_agx_orin_2024/) 卡片）。而 [Jetson Thor](/entry/ent_component_nvidia_jetson_thor/) 的定位更进一步：Blackwell 架构专为在设备端运行多模态生成式 AI 与 VLA 策略设计，但 75–120 W 级功耗意味着它不是"升级换板"那么简单，而是散热、电池、结构都要跟着重新设计的一代平台。

**【你的情况怎么分析】** 按预算与目标三选一：

- **预算 < $500、目标 RL 行走**：照抄 BHL 配方（N95 级迷你 PC），把钱花在执行器上。前提是你的策略网络小（MLP 级），且视觉需求低。
- **预算 $1,000–2,000、要做机上感知/扩散策略/VLA**：Orin NX 或 AGX Orin。先算显存：模型参数量 × 量化精度 + 激活值，16GB 能装下 3 亿参数级扩散策略（ToddlerBot 实证），更大的 VLA 模型需要 64GB 版本。
- **瞄准下一代端侧大模型**：关注 Thor，但把散热（75–120 W 级已进入液冷/相变讨论区间，来源：[安全 MCU](/entry/ent_component_safety_mcu/) 卡片）和电池容量作为前置设计约束，而不是买回来再想办法。

## 第三步：确定实时性方案

**【做什么】** 给 L0/L1 层选一条实时路线，主流有四条：

1. **[Linux RT-PREEMPT](/entry/ent_software_rt_preempt_linux/)**：给主线 Linux 打实时补丁，使内核大部分代码可抢占、中断线程化，提供数十微秒级调度延迟（来源：[QNX](/entry/ent_software_qnx/) 卡片对比节）。保留完整 Linux 生态，是个人与实验室的默认选项。打补丁后必须用 `cyclictest` 在真实负载下实测最大延迟（方法见 [第 6 章](/wiki/chapters/chapter-06/) 6.4.7 节）。
2. **[EtherCAT](/entry/ent_technology_ethercat_2024/) 主站**：实时性下沉到总线。EtherCAT 的"飞读飞写"（processing on the fly）让从站在帧经过时即时读写，配合分布式时钟（Distributed Clocks）让所有关节共享统一时间基准（来源：EtherCAT 卡片）。主控跑 PREEMPT_RT + EtherCAT 主站协议栈即可驱动 1 ms 级关节回路，OpenLoong 青龙即采用 EtherCAT 总线（来源：data/roadmap/research/openloong-qinglong.md）。
3. **双内核/硬 RTOS**：Xenomai 在 Linux 旁跑独立实时核，调度延迟可低至微秒级但配置维护复杂；[QNX](/entry/ent_software_qnx/) 是商业微内核 RTOS，文件系统、网络栈都作为用户态服务运行，广泛用于汽车与医疗，可靠性与认证体系完整但要付授权费（来源：QNX 卡片）。
4. **MCU 硬实时**：把电流环、安全逻辑彻底交给单片机（如 OP3 的 OpenCR 子控制器，来源：data/roadmap/research/robotis-op3-darwin-op.md），主控只做软实时任务。资源受限节点可用 Zephyr 这类开源 RTOS（来源：QNX 卡片）。

**【为什么】** 标准 Linux 的内核临界区会让高优先级任务等待不可预测的时间，数十到数百微秒的抖动对 1 ms 控制环是致命的（原理详见 [第 6 章](/wiki/chapters/chapter-06/) 6.4.7 节）。实时方案的选择本质是"把确定性放在哪一层"：放在内核（PREEMPT_RT）、放在总线（EtherCAT）、放在专用 OS（QNX），还是放在专用芯片（MCU）。

**【你的情况怎么分析】** 决策顺序：

- 舵机方案 → 什么实时补丁都可以不打，先把机器人跑起来。
- 自研 QDD + CAN 总线（BHL 路线）→ PREEMPT_RT 足够，成本低、资料多。
- 自研 QDD + 多关节高同步要求（>20 关节、1 ms 环）→ EtherCAT 主站，前期投入高但这是工业界验证过的路。
- 未来要走车规/医疗级认证 → 现在就可以了解 QNX 概念，但个人原型阶段不必付费上马。

## 第四步：评估端侧 VLA 推理需求

**【做什么】** 如果你的路线图上写着"机器人听懂指令自己干活"，就要为 [端侧 VLA 推理（On-Device VLA Inference）](/entry/ent_tech_on_device_vla_inference/) 做专门的算力预算：列出目标 VLA 模型的参数量、量化方案（INT8/FP16）、要求的动作输出频率，反推显存与 TOPS 需求。VLA 理论背景见 [第 19 章](/wiki/chapters/chapter-19/)。

**【为什么】** 把 VLA 放在机上而不是云端，是被三个硬约束逼的：**延迟**（动作指令经不起网络往返）、**连接性**（机器人不能离了 Wi-Fi 就变砖）、**隐私**（家庭场景的图像不该出户）（来源：[端侧 VLA 推理](/entry/ent_tech_on_device_vla_inference/) 卡片）。但端侧部署的代价是模型必须塞进有限的显存与功耗预算，需要量化、剪枝、蒸馏等压缩技术（来源：[安全 MCU](/entry/ent_component_safety_mcu/) 卡片趋势节）。已有的实证锚点：300M 参数扩散策略在 Orin NX 16GB 上约 100 ms 延迟（来源：data/roadmap/research/toddlerbot.md）——100 ms 对操作任务可用，对动态平衡则必须留给 L1 层的小模型。

**【你的情况怎么分析】** 诚实回答三个问题：你的 VLA 模型有多大（1B 以下可考虑 Orin NX/AGX Orin，更大请直接看 Thor 级或接受云端混合架构）？动作输出频率要求多高（操作任务 5–10 Hz 通常够，全身动态控制不能依赖 VLA 直接输出）？断网时机器人必须保有什么能力（至少要有机上保安全的小策略）？VLA 推理性能与模型、量化配置强相关，具体延迟数据建议参考 VLA-Perf 等基准论文（来源：[端侧 VLA 推理](/entry/ent_tech_on_device_vla_inference/) 卡片）并在目标硬件上实测。

## 验收标准

- 你有一张任务分层表：每个计算任务标注了目标频率、可容忍延迟、失效后果，且 L0 任务都有独立的兜底路径（安全 MCU 或驱动器本地环）。
- 主控选型有书面理由：能说出"为什么是这块板子"，并用至少一个同量级开源项目的配置作为对照（如"我做 RL 行走 + 小策略，选 N95 级，参照 BHL"）。
- 若走实时 Linux 路线：已在目标硬件上跑过 `cyclictest`，记录空载与压力负载下的最大调度延迟，且与控制环周期有至少一个数量级的裕量。
- 若规划 VLA：已写下目标模型的参数量、量化方案、预期显存占用，并确认所选平台的显存容量留有 30% 以上余量。
- 电源与散热核算完成：主控满载功耗（如 AGX Orin 60 W、Thor 75–120 W 级）已计入整机功耗预算与散热设计。

## 常见坑与排查

| 症状 | 可能原因 | 排查动作 |
|---|---|---|
| 机器人在仿真里稳、上真机就抖 | 控制环周期不达标，调度延迟抖动 | `cyclictest` 实测最大延迟；检查是否打了 PREEMPT_RT 补丁、是否做了 CPU 隔离与内存锁定 |
| 跑推理几分钟后性能骤降 | 过热降频（ToddlerBot 实测 19 分钟即降频，来源：其调研档案） | 监控芯片温度与频率曲线；改善风道/加均热板；降低功耗模式档位重新标定 |
| EtherCAT 偶发丢帧、关节报错 | 主站调度超时或 DC 同步未配置 | 检查工作计数器（Working Counter）返回值；确认分布式时钟已启用；用 PREEMPT_RT + 独占 CPU 核跑主站 |
| VLA 模型装不进显存或推理极慢 | 模型过大、未量化 | 先 INT8/FP16 量化再测；换算显存需求与平台规格对比；考虑动作分块（action chunking）降低推理频率 |
| NUC/迷你 PC 上 ROS 节点偶发延迟尖峰 | 标准内核调度抖动 + USB 设备中断争抢 | 打实时补丁；中断亲和性（IRQ affinity）绑定到非实时核；把 CAN/IMU 的 USB 适配器换到独立 USB 控制器 |
| 主控死机后机器人失控倒地 | 缺少独立安全层 | 补上安全 MCU 看门狗与急停回路，做到主控断电时驱动器自动下使能 |

## 配套阅读

- [阶段 2 · 双足平台](../stage-2-biped.md) —— 主控平台在行走控制中的部署
- [阶段 3 · 完整人形](../stage-3-humanoid.md) —— 分层算力与端侧 VLA 推理
- [路线图总览](../index.md)
