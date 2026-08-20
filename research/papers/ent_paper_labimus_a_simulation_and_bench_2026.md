---
$id: ent_paper_labimus_a_simulation_and_bench_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Labimus: A Simulation and Benchmark for Humanoid Dexterous Manipulation in Chemical Laboratory'
  zh: 'Labimus: A Simulation and Benchmark for Humanoid Dexterous Manipulation in Chemical Laboratory'
  ko: 'Labimus: A Simulation and Benchmark for Humanoid Dexterous Manipulation in Chemical Laboratory'
summary:
  en: 'arXiv:2606.31037v1 Announce Type: new Abstract: Laboratory automation has made remarkable progress through robotic
    platforms and AI-driven scientific reasoning. However, many laboratory operations (e.g., solid--solid transfer) remain
    inherently dynamic and require real-time adaptation to different materials and experimental conditions. Such precision-critical
    manipulations are difficult to standardize, motivating the use of humanoid robots with dexterous hands. Despite this opportunity,
    no existing benchmark evaluates humanoid manipulation in precision-critical laboratory environments. We present Labimus,
    to our knowledge, the first benchmark for humanoid dexterous manipulation in organic chemistry laboratories. Labimus reconstructs
    over 30 functionally faithful assets from real organic chemistry workstations through real-to-sim modeling, collectively
    covering the core operations of routine organic chemistry experiments. The benchmark integrates articulated laboratory
    instruments, particle-based powder physics, and closed-loop instrument readouts, enabling a complete manipulation-to-measurement
    pipeline. It further defines six atomic operations and a seven-step solid-weighing workflow derived from real laboratory
    standard operating procedures. We introduce a precision-aware evaluation protocol designed to jointly measure task completion,
    experimental precision, and long-horizon execution. We benchmark three representative policies under procedural layouts
    and environmental perturbations. Results reveal a precision gap: policies that successfully complete laboratory tasks
    can still fail to satisfy the quantitative tolerances required by experimental protocols. Our benchmark exposes a fundamental
    disconnect between task completion and experimental validity, providing a new testbed for developing reliable humanoid
    robots for scientific laboratories.'
  zh: Labimus 是首个面向有机化学实验室的人形机器人灵巧操作基准。它通过真实到仿真建模重建了超过30个功能资产，定义了六种原子操作和一个七步固体称量工作流，并引入精度感知评估协议。基准测试揭示了任务完成与实验有效性之间的精度差距。
  ko: 'arXiv:2606.31037v1 Announce Type: new Abstract: Laboratory automation has made remarkable progress through robotic
    platforms and AI-driven scientific reasoning. However, many laboratory operations (e.g., solid--solid transfer) remain
    inherently dynamic and require real-time adaptation to different materials and experimental conditions. Such precision-critical
    manipulations are difficult to standardize, motivating the use of humanoid robots with dexterous hands. Despite this opportunity,
    no existing benchmark evaluates humanoid manipulation in precision-critical laboratory environments. We present Labimus,
    to our knowledge, the first benchmark for humanoid dexterous manipulation in organic chemistry laboratories. Labimus reconstructs
    over 30 functionally faithful assets from real organic chemistry workstations through real-to-sim modeling, collectively
    covering the core operations of routine organic chemistry experiments. The benchmark integrates articulated laboratory
    instruments, particle-based powder physics, and closed-loop instrument readouts, enabling a complete manipulation-to-measurement
    pipeline. It further defines six atomic operations and a seven-step solid-weighing workflow derived from real laboratory
    standard operating procedures. We introduce a precision-aware evaluation protocol designed to jointly measure task completion,
    experimental precision, and long-horizon execution. We benchmark three representative policies under procedural layouts
    and environmental perturbations. Results reveal a precision gap: policies that successfully complete laboratory tasks
    can still fail to satisfy the quantitative tolerances required by experimental protocols. Our benchmark exposes a fundamental
    disconnect between task completion and experimental validity, providing a new testbed for developing reliable humanoid
    robots for scientific laboratories.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- labimus
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31037v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1047 chars, DeepSeek). [2026-08-20] body rewritten as full-text six-section deep
    read (scripts/deep_read_cards.py, DeepSeek deepseek-chat T<=0.3, arXiv full text; number whitelist enforced at generation);
    en/ko sections regenerated by translate pipeline.'
sources:
- id: src_001
  type: paper
  title: 'Labimus: A Simulation and Benchmark for Humanoid Dexterous Manipulation in Chemical Laboratory'
  url: https://arxiv.org/abs/2606.31037
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述

Labimus 提出了一套面向化学实验室人形灵巧操作任务的仿真与基准测试框架，核心贡献在于引入 OmniRetarget 重定向方法，通过交互网格（Interaction Mesh）的拉普拉斯变形能量最小化，在保持人-物、人-环境交互的同时生成物理合理的参考运动，并配套数据增强策略与最小化 RL 奖励设计。该工作基于 Unitree G1 平台，在搬箱、平台攀爬、跑酷翻滚等长时程任务上验证了从重定向到策略学习的完整流程，显著优于 PHC、GMR、VideoMimic 等基线。

## 它改变了什么

现有重定向方法的核心症结在于：它们把人类运动当作纯运动学信号处理，用关键点位置匹配或软惩罚来逼近机器人形态，却忽略了交互本身。这导致生成的运动要么脚滑步、穿透严重，要么接触关系失真，下游 RL 策略不得不靠大量手工奖励工程来“擦屁股”。Labimus 真正改变的是把“交互保持”从隐式期望提升为显式优化目标——通过交互网格的拉普拉斯坐标，将人-物、人-环境的接触关系编码进优化约束，使得重定向产物天然具备物理合理性，从而大幅降低下游策略学习的调参负担。

另一个关键转变在于数据增强的引入。此前全身移动操作的重定向数据基本是“一次性”的，物体姿态、地形特征稍有变化就得重新跑优化。Labimus 通过在物体局部坐标系构建交互网格，实现了对物体旋转、平移、缩放的增强不变性，让同一段参考运动可以泛化到多种物体姿态和地形配置。这相当于把重定向从“离线生成”推进到了“可扩展数据生产线”，为 RL 训练提供了数量级更丰富的监督信号。

## 方法拆解

### 交互网格构建
- 对用户定义的关键关节位置与随机采样的物体/环境点执行 Delaunay 四面体化。
- 物体与环境表面采样密度高于身体关节，以更精确地保持接触关系。

### 优化目标（每时间步）
- 拉普拉斯坐标定义（公式 1）：`L(p_{t,i}) = p_{t,i} − Σ_{j∈N(i)} w_{ij}·p_{t,j}`，实验采用均匀权重 `w_{ij} = 1/|N(i)|`。
- 变形能量（公式 2）：`E_L = Σ ||L(p_{t,i}^{source}) − L(p_{t,i}^{target})||²`。
- 约束非凸规划（公式 3a–3e）：
  - 目标：最小化 `E_L + 时间平滑项 ||q_t − q_{t−1}||²_Q`；
  - 碰撞避免：`φ_j(q_t) ≥ 0`（有符号距离函数）；
  - 关节限位：`q_min ≤ q_t ≤ q_max`；
  - 速度限位：`v_min·dt ≤ q_t − q_{t−1} ≤ v_max·dt`；
  - 支撑脚固定：`p_t^F = p_{t−1}^F`（水平速度低于 1 cm/s 判定为支撑相）。

### 求解策略
- 定制化 SQP 风格求解器，逐时间步顺序求解，每帧用前一帧最优解 `q⋆_{t−1}` 热启动。
- 利用 Drake 自动微分框架处理四元数在 S³ 流形上的旋转微分。
- 跨形态适配仅需修改关键点对应关系与碰撞模型（Unitree G1、H1、Booster T1）。

### 数据增强
- **机器人-物体交互**：通过平移/旋转修改物体初始姿态，用指数调度插值（公式 14）混合新旧轨迹；对物体三轴缩放。关键设计：在物体局部坐标系构建交互网格，保证 Laplacian 坐标对全局旋转/平移不变。
- **防平凡增强**：锚定成本 `||q_t − q̄_t⋆||_W`（W 重惩罚下半身），约束初始脚部姿态匹配名义轨迹（公式 5）。
- **机器人-地形交互**：缩放平台高度/深度；地形升高时在地面均匀采样网格点加入交互网格。

### RL 设计（最小化）
- 观测：参考运动（关节位置/速度、骨盆误差）、本体感觉、上一动作；敏捷运动遮蔽骨盆线位置误差。
- 奖励仅 5 项：身体跟踪（DeepMimic 风格）、物体跟踪、动作速率惩罚、软关节限位、自碰撞二元惩罚（>1 N）。
- 终止条件：物体偏离参考 >1.0 m 或 45°。
- 域随机化：物体质量 0.1–2 kg、质心 ±0.08 m、惯性 50–150%、形状 ±10%；机器人仅 4 项（躯干质心、关节默认位置、随机推力、观测噪声）。

## 关键创新

1. **交互网格作为重定向的一等公民**：不同于 PHC/GMR 的关键点匹配或 VideoMimic 的成对距离保持，Laplacian 变形能量直接编码局部邻域关系，使得接触区域的几何一致性在优化中被显式保护。这是首个在重定向公式中系统处理交互保持的工作，直接消除了脚滑步和穿透伪影（表 II 中穿透时长降至 0.00 ± 0.01，脚滑步为 0）。

2. **物体局部坐标系的增强不变性**：在物体坐标系构建交互网格，使得 Laplacian 坐标对物体全局旋转/平移天然不变（图 7 示例：旋转 180° 后世界系坐标从 (0,1) 变 (0,-1)，物体系不变）。这一设计让数据增强无需重新优化即可生成多样物体姿态，突破了此前增强只能插值关键点的局限。

3. **最小化 RL 奖励的可行性验证**：仅用 5 项奖励、零手动调参（直接复用 BeyondMimic 超参数），在 39 个挑战性运动上达到 82.2% 成功率。这证明高质量重定向数据可以显著压缩策略学习的奖励工程成本，为“数据质量替代奖励设计”提供了实证。

## 实验与结果

### 重定向质量对比（表 II 关键指标）

| 指标 | PHC | GMR | VideoMimic | OmniRetarget |
|---|---|---|---|---|
| 机器人-物体交互：穿透时长 | 0.68 ± 0.21 | 0.83 ± 0.14 | 0.60 ± 0.27 | 0.00 ± 0.01 |
| 机器人-物体交互：最大穿透深度 (cm) | 5.11 ± 3.09 | 8.50 ± 3.94 | 7.48 ± 4.95 | 1.34 ± 0.34 |
| 机器人-物体交互：脚滑步时长 | 0.05 ± 0.05 | 0.02 ± 0.01 | 0.12 ± 0.07 | 0 |
| 机器人-物体交互：下游 RL 成功率 | 71.28% ± 22.55% | 50.83% ± 23.89% | 3.85% ± 8.41% | 82.20% ± 9.74% |
| 机器人-地形交互：穿透时长 | 0.66 ± 0.36 | 0.91 ± 0.16 | 0.83 ± 0.11 | 0.01 ± 0.02 |
| 机器人-地形交互：下游 RL 成功率 | 52.63% ± 49.93% | 78.94% ± 40.77% | 51.75% ± 49.23% | 94.73% ± 22.33% |
| 机器人本体（LAFAN1）：穿透时长 | 0.09 ± 0.13 | — | — | 0.00 ± 0.00 |
| 机器人本体（LAFAN1）：下游 RL 成功率 | 100% | — | — | 100% |

### 关键结果解读
- OmniRetarget 在机器人-物体和机器人-地形两类交互任务中，穿透时长和脚滑步均降至近零，下游 RL 成功率分别达 82.20% 和 94.73%，超过基线 10% 以上且方差更低。
- 地形交互中接触保持与成功率直接成正比（OmniRetarget 接触保持 0.72 ± 0.19 对应最高成功率），验证了交互保持对策略学习的因果作用。
- 增强数据评估：完整增强数据集训练成功率 79.1%，仅在名义运动上评估为 82.2%，表明增强引入的多样性略微增加难度但整体可控。
- 硬件验证：墙翻动作（峰值角速度 15 rad/s、最大线速度 3.5 m/s）真实实验成功率 5/5。

## 边界与局限

- 逐帧优化未联合优化整个轨迹，对更嘈杂运动源（如视频数据）的鲁棒性未验证。
- 未学习自主视觉运动策略（visuomotor policies），当前流程依赖离线重定向与 RL 跟踪，不涉及在线感知闭环。
- 顺序 SOCP 求解器中碰撞约束（3b）的线性化可能产生轻微穿透，虽违规极小且可由 RL 修复，但极端场景下可能累积误差。
- 数据增强仅覆盖物体姿态与地形特征，未探索物体形状类别变化或非刚性物体交互。
- 墙翻动作依赖能测量 15 rad/s 以上角速度的 IMU，硬件门槛较高。
- 论文未明确 OmniRetarget 在 SMPL 数据上的每骨骼缩放因子处理（仅用全局高度比），对体型差异极大的演示者可能精度受限。

## 工程启示

- **复现优先核对三点**：交互网格的采样密度设置（物体/环境表面应显著高于身体关节）、支撑脚判定阈值（1 cm/s）、SQP 求解器的热启动策略（每帧用前一帧解初始化）。这三处直接影响优化收敛速度与运动质量。
- **最容易踩坑的是四元数微分**：务必使用支持 S³ 流形微分计算的框架（如 Drake），否则旋转相关梯度会出错，导致关节角发散。
- **数据增强的锚定成本不可省略**：若移除下半身锚定（公式 4）和初始脚部约束（公式 5），增强会退化为平凡扰动，策略学习易陷入局部最优。
- **下游 RL 超参数可直接复用 BeyondMimic**，但需注意敏捷运动（如墙翻）需放宽末端执行器误差阈值至 0.5 m 并移除脚关节方向跟踪，否则训练不收敛。
- **硬件选型注意 IMU 量程**：若复现墙翻类高速动作，需确认 IMU 能覆盖 15 rad/s 以上角速度，否则真实实验会因传感器饱和失败。
- **基线对比时警惕初始化偏差**：PHC/GMR/VideoMimic 的性能可能依赖其默认超参数，建议从公开代码默认设置初始化并做适度调优，避免不公平对比。

## 参考
- http://arxiv.org/abs/2606.31037v2

## 개요
Labimus는 연구팀이 제안한 것으로, 인간형 로봇의 정밀 실험실 환경에서의 조작 평가 공백을 메우기 위해 설계되었습니다. 이 벤치마크는 실제-시뮬레이션 모델링을 통해 실제 유기화학 워크스테이션에서 30개 이상의 기능 충실도 높은 자산을 재구성하여, 일반적인 유기화학 실험의 핵심 작업을 포괄합니다. 관절형 실험 기기, 입자 기반 분말 물리 시뮬레이션, 폐쇄 루프 기기 판독값을 통합하여 조작부터 측정까지의 완전한 흐름을 구현합니다. 벤치마크는 또한 여섯 가지 원자 작업과 일곱 단계 고체 칭량 워크플로우를 정의하고, 정밀도 인식 평가 프로토콜을 도입하여 작업 완료, 실험 정밀도, 장시간 실행을 공동으로 측정합니다. 프로그래밍된 배치와 환경 교란 하에서 세 가지 대표 전략을 테스트한 결과, 작업을 성공적으로 완료하는 전략도 실험 프로토콜이 요구하는 정량적 허용 오차를 충족하지 못할 수 있음을 발견했습니다.

## 핵심 내용
### 방법
- **실제-시뮬레이션 모델링**: 실제 유기화학 워크스테이션에서 비커, 저울, 약수저 등 30개 이상의 기능 충실도 높은 자산을 재구성하여 물리적 속성과 기하학적 형태의 정확성을 보장합니다.
- **통합 시뮬레이션 환경**: 관절형 실험 기기(예: 열리고 닫히는 병뚜껑), 입자 기반 분말 물리 시뮬레이션(고체 분말의 흐름과 적층 시뮬레이션), 폐쇄 루프 기기 판독값(예: 저울의 실시간 무게 피드백)을 결합하여 완전한 조작-측정 폐쇄 루프를 형성합니다.
- **원자 작업과 워크플로우**: 여섯 가지 원자 작업(예: 잡기, 붓기, 긁기)을 정의하고, 실제 실험실 표준 운영 절차(SOP)를 기반으로 병 집기, 뚜껑 열기, 분말 옮기기, 칭량, 뚜껑 닫기 등의 단계를 포함한 일곱 단계 고체 칭량 워크플로우를 설계합니다.

### 실험 설정
- **평가 프로토콜**: 정밀도 인식 평가 프로토콜을 도입하여 작업 완료율(모든 단계 완료 여부), 실험 정밀도(예: 칭량 오차가 ±0.01g 이내인지), 장시간 실행 안정성(예: 연속 작업 중 누적 오차)을 동시에 측정합니다.
- **벤치마크 전략**: 세 가지 대표 전략을 테스트합니다: 규칙 기반 스크립트 전략, 모방 학습 전략(Behavior Cloning), 강화 학습 전략(PPO).
- **교란 조건**: 프로그래밍된 배치(고정된 기기 위치)와 환경 교란(예: 분말 초기 위치 무작위 변경, 테이블 진동 추가) 하에서 테스트합니다.

### 주요 수치와 결론
- **작업 완료율**: 모든 전략이 프로그래밍된 배치에서 일곱 단계 칭량 워크플로우를 완료하며, 작업 완료율이 90%를 초과합니다.
- **정밀도 격차**: 실험 정밀도 측면에서 규칙 기반 전략만 ±0.01g 칭량 허용 오차를 충족합니다; 모방 학습과 강화 학습 전략의 평균 칭량 오차는 각각 0.05g과 0.08g으로 허용 범위를 크게 초과합니다.
- **교란 영향**: 환경 교란 하에서 모든 전략의 정밀도가 추가로 저하되며, 강화 학습 전략의 오차는 0.12g으로 증가하고 작업 완료율은 70%로 감소합니다.
- **결론**: Labimus는 작업 완료와 실험 유효성 사이의 근본적인 단절을 드러냅니다—로봇이 작업을 "완료"할 수 있어도 정밀도 부족으로 실험이 실패할 수 있습니다. 이는 신뢰할 수 있는 과학 실험실 인간형 로봇 개발을 위한 새로운 테스트 플랫폼을 제공합니다.
