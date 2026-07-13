---
id: ent_product_humanoid_robot_wrist
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 人形机器人腕关节
  en: Humanoid Robot Wrist
status: active
sources:
- id: src_dexwrist_paper
  type: website
  url: https://arxiv.org/html/2507.01008v1
- id: src_xrobotek_wrist_actuator
  type: website
  url: https://www.xrobotek.com/products/linear-joint-actuator-xla15s50-6r000.html
- id: src_cubemars_wrist_guide
  type: website
  url: https://www.cubemars.com/the-right-joint-motors-for-humanoid-robots-selection.html
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 人形机器人腕关节

## 概述

人形机器人腕关节是连接小臂与末端执行器（如灵巧手或工具）的关键运动副，通常需要模拟人类手腕的 $2$ 至 $3$ 个自由度：屈/伸（Flexion/Extension, F/E）、桡/尺偏（Radial/Ulnar Deviation, R/U）以及旋前/旋后（Pronation/Supination, P/S）。腕关节的设计需在紧凑空间内实现足够的扭矩输出、运动范围与反向驱动性，同时尽可能降低重量与惯量，以提升手臂的动态响应与能耗效率。根据 DexWrist 等研究，完成约 $93\%$ 日常生活活动（ADL）所需的腕部扭矩约为 $3\,\text{N}\cdot\text{m}$；而工业搬运场景可能需要 $10\,\text{N}\cdot\text{m}$ 以上。

## 工作原理 / 技术架构

人形机器人腕关节通常采用两种结构形式：

1. **串联腕（Serial Wrist）**：屈/伸与偏摆由两个相互垂直的旋转关节串联构成，结构简单、控制直观，但会增加末端惯量并减小工作空间。
2. **并联腕（Parallel Kinematic Wrist, PKM）**：采用 2-(R, RR) 等并联机构将两个自由度局部化，能够在更小空间内获得更大的运动范围与刚度，DexWrist 研究表明其约束空间可达性相比串联腕提升约 $88\%$。

腕关节的驱动方式包括：

- **旋转电机 + 谐波/行星减速器**：通过减速比 $i$ 放大电机扭矩，输出扭矩 $T_{\text{out}} = T_{\text{motor}} \cdot i \cdot \eta$。
- **直线电机/线性执行器 + 连杆机构**：如 XLA15S50 线性关节执行器通过滚柱丝杠将电机旋转转换为直线推力，再经连杆驱动腕部运动。

为了保障人机交互安全，腕关节常设计为低反向驱动阻力，使得外部碰撞力可轻易推动关节，避免对人员或环境造成伤害。

## 关键参数表

| 参数 | 典型范围 / 设计目标 | 示例：XLA15S50 腕部线性执行器 |
|---|---|---|
| 自由度 | $2$ – $3$ DOF（F/E、R/U、P/S） | 线性驱动单元 |
| 屈/伸扭矩 | $3\text{–}12\,\text{N}\cdot\text{m}$（依负载） | — |
| 桡/尺偏扭矩 | $3\text{–}11\,\text{N}\cdot\text{m}$ | — |
| 旋前/旋后扭矩 | $1\text{–}5\,\text{N}\cdot\text{m}$ | — |
| 运动范围（F/E） | 约 $\pm 45^\circ$ – $\pm 80^\circ$ | — |
| 运动范围（R/U） | 约 $\pm 20^\circ$ – $\pm 40^\circ$ | — |
| 外径 | 通常 $\leq 60\,\text{mm}$ | $\phi 48\,\text{mm}$ |
| 重量 | $0.3\text{–}1.5\,\text{kg}$ | $0.75\,\text{kg}$ |
| 直线推力 | — | $1500\,\text{N}$ |
| 定位重复精度 | $\pm 0.05^\circ$ 量级 | $\pm 0.01\,\text{mm}$ |

## 应用场景

人形机器人腕关节决定了末端执行器的空间指向与柔顺交互能力：

- **灵巧操作**：在抓取、插拔、旋转旋钮等任务中提供末端姿态调整自由度。
- **工具使用**：使机器人能够像人类一样握持并使用螺丝刀、扳手、餐具等工具。
- **人机协作**：通过力控腕关节实现柔顺接触，降低碰撞风险。
- **服务与护理**：在辅助进食、康复训练等场景中提供自然、灵活的手部姿态。

## 供应链关系

腕关节模块位于人形机器人产业链的中上游。其核心零部件包括无框力矩电机、谐波/行星减速器、滚柱丝杠、力矩传感器、磁编码器与轴承；集成商将这些零部件封装为腕关节模组，供应给人形机器人本体厂商（如 Tesla Optimus、Figure、傅利叶、优必选等）。部分公司（如 XRobotek）直接将线性关节执行器作为腕部解决方案销售，使机器人 OEM 能够快速集成。腕关节的性能直接影响整机抓取成功率、工作空间与安全性，是“上肢—末端—环境”交互链中的关键枢纽。

## 来源与验证

- DexWrist 论文（arXiv 2507.01008v1）基于人体生物力学数据提出腕关节设计目标，指出 $3\,\text{N}\cdot\text{m}$ 扭矩可覆盖 $93\%$ 的 ADL 任务，并通过并联机构将约束空间可达性提升 $88\%$。
- XRobotek XLA15S50 产品页说明该线性执行器专为腕关节设计，外径 $48\,\text{mm}$、推力 $1500\,\text{N}$、重量 $0.75\,\text{kg}$、重复定位精度 $\pm 0.01\,\text{mm}$。
- CubeMars 人形机器人关节电机选型指南将腕关节列为“精细控制核心”，扭矩需求 $1\text{–}20\,\text{N}\cdot\text{m}$，并推荐小型无框/直驱电机方案。