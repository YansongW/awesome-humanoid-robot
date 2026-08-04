---
$id: ent_paper_minimalist_retargeting_guided_reinforcem_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Minimalist Retargeting-Guided Reinforcement Learning Recipe for Dexterous Manipulation
  zh: A Minimalist Retargeting-Guided Reinforcement Learning Recipe for Dexterous Manipulation
  ko: A Minimalist Retargeting-Guided Reinforcement Learning Recipe for Dexterous Manipulation
summary:
  en: 'Recent work in humanoid whole-body control has found success with a simple recipe: retarget human motion to robot kinematic
    references, then train policies via reinforcement learning (RL) to track them. But how does this recipe transfer to dexterous
    manipulation? The answer is not obvious, as manipulation involves complex, contact-rich dynamics and requires delicate
    regulation of contact modes.'
  zh: 本文提出 Regrind，一个从单个人类演示学习灵巧操作的极简配方：交互感知运动重定向（interaction-aware retargeting）生成物理可行的参考轨迹，配合残差 RL、数据增强和课程域随机化，实现仿真到真实的零样本迁移。作者在剪刀和螺丝刀两个任务、LEAP
    和 WUJI 两种机械手上验证了该方法，在仿真中达到接近完美的成功率，并在真实世界三个任务中可靠转移。
  ko: 'Recent work in humanoid whole-body control has found success with a simple recipe: retarget human motion to robot kinematic
    references, then train policies via reinforcement learning (RL) to track them. But how does this recipe transfer to dexterous
    manipulation? The answer is not obvious, as manipulation involves complex, contact-rich dynamics and requires delicate
    regulation of contact modes.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- minimalist
- retargeting
- guided
- reinforcem
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Catch-up sweep 2026-08-05, source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section interpretation
    by DeepSeek (deepseek-chat, T<=0.3) with fact guardrails.'
sources:
- id: src_001
  type: paper
  title: arXiv:2607.11874 A Minimalist Retargeting-Guided Reinforcement Learning Recipe for Dexterous Mani
  url: https://arxiv.org/abs/2607.11874
  date: '2026-07-13'
  accessed_at: '2026-08-05'
---

## 概述

本文提出 Regrind，一个从单个人类演示学习灵巧操作的极简配方：交互感知运动重定向（interaction-aware retargeting）生成物理可行的参考轨迹，配合残差 RL、数据增强和课程域随机化，实现仿真到真实的零样本迁移。作者在剪刀和螺丝刀两个任务、LEAP 和 WUJI 两种机械手上验证了该方法，在仿真中达到接近完美的成功率，并在真实世界三个任务中可靠转移。

## 它改变了什么

灵巧操作领域长期被遥操作主导——在真实机器人上人工收集演示，成本高、泛化差。人形全身控制中「人类运动重定向→仿真 RL→部署」的配方已被证明有效，但直接迁移到灵巧手时遭遇瓶颈：简单运动学重定向（如 Mink IK）紧密匹配手部姿态却忽略手-物体交互，产生物理上不可行的轨迹，对下游 RL 是劣质参考。现有尝试如 SPIDER 虽考虑物理约束，但性能极差（仿真成功率 0%）。

Regrind 真正改变的是对「重定向」这一环节的定位：它不再只是把人类运动映射到机器人运动学，而是通过交互网格（interaction mesh）保留手-物体之间的空间和接触语义，使重定向输出本身成为 RL 可用的高质量参考。同时，它证明了灵巧操作中 sim-to-real 的敏感性远高于运动任务——摩擦、柔顺性、几何的小误差会因持续接触迅速累积，因此需要比运动任务更精细的域随机化和系统辨识。

## 方法拆解

### 整体流程
Real-to-Sim-to-Real 管线，从单个 3D 人类演示（MANO 手部关键点 + 物体 6D 位姿）学习 RL 策略。

### 步骤 1：交互感知运动重定向
- 源点集 𝒫̃ₜ = 𝒫ₜᵒ ∪ 𝒫ₜʰ（物体关键点 ∪ 人手关键点），目标点集 𝒫ₜ(qₜ) = 𝒫ₜᵒ ∪ 𝒫ₜʳ(qₜ）（物体关键点 ∪ 机器人关键点）。
- 优化目标：min Σ D(ℳ(𝒫̃ₜ), ℳ(𝒫ₜ(qₜ))) + λ Σ ‖qₜ − qₜ₋₁‖²₂，约束 q₀:ₜ₋₁ ∈ 𝒬。
- 交互网格由 Delaunay 四面体化定义，变形能 D = Σᵢ ‖Lᵢ(𝒫̃ₜ) − Lᵢ(𝒫ₜ(qₜ))‖₂，其中 Lᵢ(𝒫) = pᵢ − (1/|𝒩ᵢ|) Σⱼ∈𝒩ᵢ pⱼ。
- 可行集 𝒬 包含：关节限位、速度界（v_min Δt ≤ q_t − q_{t-1} ≤ v_max Δt）、非穿透约束（φ_j(q_t) ≥ 0，激活机器人-物体和机器人-环境碰撞对）。
- 求解器：SQP 风格，逐时间步顺序求解，每帧少量迭代，凸子问题用 MOSEK 通过 Drake 的 MathematicalProgram 求解。

### 步骤 2：参考运动引导的残差 RL
- 动作空间：qₜᵗᵃʳᵍᵉᵗ = q̄ₜ + α ⊙ π_θ(q̄ₜ, oₜ)，α 控制每自由度动作幅度。
- 观测空间（非对称 actor-critic）：Actor 观测物体位姿（位置 + Rot6D）、铰接关节位置、机器人关节位置（当前和上一时间步）、上一动作、相位变量 φ ∈ [0,1]；刻意避免速度等噪声传感器。Critic 额外获得指尖位置和关节速度。
- 奖励函数（式 8）：r_t = Σ_k w_k φ_k(e_{k,t})，密集奖励，比较模拟状态与重定向参考。跟踪项用指数核 φ_lin(e; σ) = exp(−e/σ)，平方误差项 φ_sq(c; σ) = exp(−c/σ²)。
- 关键奖励项：物体关键点位置（σ=0.02，权重 1.5）、物体线速度（σ=1.0，权重 1.0）、物体角速度（σ=3.14，权重 1.0）、腕部位置（σ=0.02，权重 0.05）、腕部姿态（σ=0.2，权重 0.05）、动作幅度/速率/越界惩罚、提前终止惩罚（−10.0）。

### 步骤 3：数据增强
- 参考状态初始化（RSI）：重置时采样随机演示相位，加小扰动。
- 轨迹增强：对每个 episode 施加扰动 (Δp, Δψ)，Δp_xy ∈ [−5, 5]² cm，Δp_z = 0，Δψ ∈ [−30°, 30°]；混合权重 w(t) 按式(11)线性插值，在 t_pickup 和 t_use 之间混合消除。
- 变换：位置加 w(t)Δp，旋转乘 R_z(w(t)Δψ)，手部腕部和指尖位置绕未扰动物体根刚性映射，手指关节参考不变。不重新运行重定向优化，直接变换物体和手部根部位姿。

### 步骤 4：域随机化与课程学习
- DR 通过 Isaac Lab event terms 实现，每环境独立采样：物体 CoM 偏移、几何缩放、摩擦、质量缩放、关节 k_p/k_d 缩放、手指默认关节偏移。
- 重力课程：从 0 到 9.81 m/s² 按 130k 环境步线性增加。
- 随机推力课程：130k 步后激活，170k 步达最大（线速度 ±0.5 m/s，角速度 ±1.0 rad/s，间隔 1–5 s）。
- 观测噪声：位置 ±2 mm，旋转 ±0.02 rad，关节 ±0.02 rad；观测时间延迟均匀采样 [0, 2] 控制步。
- 终止条件：物体出工作空间、手离物体太远、物体偏离目标配置超阈值（关键点位置误差 > 0.15 m）；WUJI 手额外终止：指尖与桌面接触力 > 10N（电机不可反向驱动）。

## 关键创新

1. **交互感知重定向作为 RL 参考**：不同于 OmniRetarget 仅做运动学匹配，Regrind 在重定向优化中显式保留手-物体交互网格的变形能，使参考轨迹物理可行且保留接触语义。这是灵巧操作中首次将交互感知重定向与 RL 训练系统结合，且被证明是性能的关键（对比 DexMachina 在剪刀任务上 SR 从 99.8% 降至 22.3%）。

2. **时变刚性变换数据增强**：不重新运行重定向优化，而是对重定向轨迹施加时变 SE(3) 扰动（位置 ±5 cm、旋转 ±30°），在训练时动态生成无限增强轨迹，同时保留原始交互关系。这比重新优化更高效，且显著提升真实世界泛化（随机初始配置下 LEAP-Scissors SR 8/10）。

3. **极简奖励设计**：仅用关键点位置、速度、腕部姿态和动作正则项，不需要显式接触先验或力反馈，却能达到接近完美的仿真成功率。这降低了方法对任务特定知识的依赖，使其可泛化到不同物体和机器人。

## 实验与结果

**仿真性能**（表 1，SPIDER 平均 5 种子，其他 3 种子 × 1024 rollout）：

| 方法 | LEAP-Scissors SR | LEAP-Screwdriver SR | WUJI-Scissors SR | WUJI-Screwdriver SR |
|------|------|------|------|------|
| Regrind (Ours) | 99.8% | 99.7% | 98.7% | 98.8% |
| SPIDER | 0.0% | 0.0% | 0.0% | 0.0% |
| DexMachina | 22.3% | 99.7% | 0.0% | 99.3% |
| Mink IK + RL | 2.0% | 0.0% | 0.0% | 3.1% |

**真实世界性能**（表 2，零样本转移）：

| 方法 | LEAP-Scissors SR | LEAP-Screwdriver SR | WUJI-Scissors SR | WUJI-Screwdriver SR |
|------|------|------|------|------|
| Regrind (Ours) | 9/10 | 10/10 | 0/10 | 9/10 |
| DexMachina | 0/10 | 2/10 | — | 5/10 |
| Mink IK + RL | — | — | — | 0/10 |

**真实世界泛化**（表 3，随机初始配置 ±5 cm、±30°）：LEAP-Scissors 8/10，LEAP-Screwdriver 10/10，WUJI-Screwdriver 9/10。

**关键解读**：SPIDER 完全失败（仿真 SR 0%），说明基于物理的重定向虽考虑动力学但生成轨迹质量差。DexMachina 在螺丝刀任务上仿真接近完美但真实转移差（2/10），说明缺乏交互保留的重定向使策略易利用仿真伪影。Regrind 在三个任务上可靠转移，唯一失败的 WUJI-Scissors 归因于非反向驱动电机的 sim-to-real 差距和真实剪刀网格不准确。

## 边界与局限

论文未明确讨论局限，但从方法可推断：部署依赖运动捕捉获取物体状态，未解决视觉感知问题；需要仔细的系统辨识（真实机器人响应延迟 1–2 步被建模为观测时间延迟）；未涉及多任务学习、长期操作、双手操作、非刚性物体；WUJI-Scissors 任务在所有方法下均失败，说明非反向驱动电机的 sim-to-real 差距仍是开放问题。论文未提及推理频率、训练时间等工程细节。

## 工程启示

复现时先核对三个关键点：**重定向求解器的可行集定义**（特别是碰撞对过滤和速度界）直接影响参考轨迹质量；**数据增强的扰动范围**（±5 cm、±30°）和混合权重 w(t) 的插值区间（t_pickup 到 t_use）决定策略的泛化边界；**系统辨识**——真实机器人响应延迟 1–2 步（30–60 ms）必须在仿真观测管线中建模，否则 sim-to-real 会失败。

最容易踩坑的地方：WUJI 手的非反向驱动电机需要额外终止条件（指尖接触力 > 10N），否则训练会利用不可行的接触模式；LEAP 手需使用 3D 打印加大物体（s=2 缩放），直接使用真实尺寸物体可能导致几何不匹配；奖励权重中动作幅度惩罚（仅 WUJI）和提前终止惩罚（−10.0）对训练稳定性影响大，需按表 4 精确设置。基线对比时注意 SPIDER 需用官方实现（MuJoCo Warp 工作流），DexMachina 需自定义实现并加碰撞感知后处理，否则对比不公平。

## Overview
Recent work in humanoid whole-body control has found success with a simple recipe: retarget human motion to robot kinematic references, then train policies via reinforcement learning (RL) to track them. But how does this recipe transfer to dexterous manipulation? The answer is not obvious, as manipulation involves complex, contact-rich dynamics and requires delicate regulation of contact modes and forces. We present REGRIND, a minimalist retargeting-guided RL pipeline that learns dexterous manipulation policies from a single human demonstration. REGRIND retargets human hand-object motion to a robot reference that preserves hand-object spatial and contact relationships, trains a residual RL policy in simulation to track object-centric keypoints along that reference, and transfers the resulting policy zero-shot to hardware with careful system identification. The resulting policies produce fluid, human-like behavior on two different multi-fingered hands across contact-rich tool-use tasks, including operating a pair of scissors and turning a screwdriver. Through systematic hardware experiments, we identify and analyze the key factors that govern sim-to-real transfer in dexterous manipulation, offering practical guidance for retargeting-based learning in contact-rich settings. Videos and code are available at https://yunhaifeng.com/REGRIND.

## 参考
- https://arxiv.org/abs/2607.11874

## 개요

본 논문은 단일 인간 시연으로부터 손재주 조작을 학습하는 극도로 간결한 레시피인 Regrind를 제안한다: 상호작용 인식 모션 리타게팅(interaction-aware retargeting)이 물리적으로 실행 가능한 참조 궤적을 생성하고, 잔차 강화학습(Residual RL), 데이터 증강, 커리큘럼 도메인 무작위화를 결합하여 시뮬레이션-실제(zero-shot sim-to-real) 전이를 달성한다. 저자들은 가위와 드라이버 두 가지 작업, LEAP 및 WUJI 두 가지 로봇 손에서 이 방법을 검증했으며, 시뮬레이션에서 거의 완벽한 성공률을 달성하고 실제 세계 세 가지 작업에서 안정적으로 전이됨을 확인했다.

## 무엇이 바뀌었는가

손재주 조작 분야는 오랫동안 원격 조작(teleoperation)이 지배해 왔다—실제 로봇에서 수동으로 시연을 수집하는 방식은 비용이 높고 일반화가 어렵다. 인간형 전신 제어에서 '인간 모션 리타게팅 → 시뮬레이션 RL → 배포' 레시피는 효과적임이 입증되었지만, 손재주 손으로 직접 전이할 때 병목에 직면한다: 단순 운동학적 리타게팅(예: Mink IK)은 손 자세를 밀접하게 일치시키지만 손-물체 상호작용을 무시하여 물리적으로 실행 불가능한 궤적을 생성하며, 이는 하류 RL에게 열등한 참조가 된다. SPIDER와 같은 기존 시도는 물리적 제약을 고려하지만 성능이 극히 낮다(시뮬레이션 성공률 0%).

Regrind가 진정으로 바꾼 것은 '리타게팅' 단계의 위상이다: 더 이상 인간 모션을 로봇 운동학에 단순 매핑하는 것이 아니라, 상호작용 메시(interaction mesh)를 통해 손-물체 간의 공간적 및 접촉 의미론을 보존하여 리타게팅 출력 자체가 RL이 사용할 수 있는 고품질 참조가 되게 한다. 동시에, 손재주 조작에서 sim-to-real 민감도가 운동 작업보다 훨씬 높다는 것을 입증한다—마찰, 유연성, 기하학의 작은 오차가 지속적인 접촉으로 인해 빠르게 누적되므로, 운동 작업보다 더 정밀한 도메인 무작위화와 시스템 식별이 필요하다.

## 방법 분해

### 전체 흐름
Real-to-Sim-to-Real 파이프라인으로, 단일 3D 인간 시연(MANO 손 키포인트 + 물체 6D 자세)에서 RL 정책을 학습한다.

### 단계 1: 상호작용 인식 모션 리타게팅
- 소스 포인트 집합 𝒫̃ₜ = 𝒫ₜᵒ ∪ 𝒫ₜʰ(물체 키포인트 ∪ 인간 손 키포인트), 타겟 포인트 집합 𝒫ₜ(qₜ) = 𝒫ₜᵒ ∪ 𝒫ₜʳ(qₜ)(물체 키포인트 ∪ 로봇 키포인트).
- 최적화 목표: min Σ D(ℳ(𝒫̃ₜ), ℳ(𝒫ₜ(qₜ))) + λ Σ ‖qₜ − qₜ₋₁‖²₂, 제약 q₀:ₜ₋₁ ∈ 𝒬.
- 상호작용 메시는 Delaunay 사면체화로 정의되며, 변형 에너지 D = Σᵢ ‖Lᵢ(𝒫̃ₜ) − Lᵢ(𝒫ₜ(qₜ))‖₂, 여기서 Lᵢ(𝒫) = pᵢ − (1/|𝒩ᵢ|) Σⱼ∈𝒩ᵢ pⱼ.
- 실행 가능 집합 𝒬는 다음을 포함: 관절 한계, 속도 경계(v_min Δt ≤ q_t − q_{t-1} ≤ v_max Δt), 비관통 제약(φ_j(q_t) ≥ 0, 로봇-물체 및 로봇-환경 충돌 쌍 활성화).
- 솔버: SQP 스타일, 시간 단계별 순차 해석, 각 프레임에서 소량 반복, 볼록 하위 문제는 Drake의 MathematicalProgram을 통해 MOSEK로 해석.

### 단계 2: 참조 모션 유도 잔차 RL
- 행동 공간: qₜᵗᵃʳᵍᵉᵗ = q̄ₜ + α ⊙ π_θ(q̄ₜ, oₜ), α는 자유도별 행동 크기를 제어.
- 관측 공간(비대칭 actor-critic): Actor는 물체 자세(위치 + Rot6D), 관절 관절 위치, 로봇 관절 위치(현재 및 이전 시간 단계), 이전 행동, 위상 변수 φ ∈ [0,1]을 관측; 속도 등 노이즈 센서는 의도적으로 제외. Critic은 추가로 손끝 위치와 관절 속도를 획득.
- 보상 함수(식 8): r_t = Σ_k w_k φ_k(e_{k,t}), 밀집 보상, 시뮬레이션 상태와 리타게팅 참조 비교. 추적 항은 지수 커널 φ_lin(e; σ) = exp(−e/σ), 제곱 오차 항은 φ_sq(c; σ) = exp(−c/σ²).
- 핵심 보상 항: 물체 키포인트 위치(σ=0.02, 가중치 1.5), 물체 선속도(σ=1.0, 가중치 1.0), 물체 각속도(σ=3.14, 가중치 1.0), 손목 위치(σ=0.02, 가중치 0.05), 손목 자세(σ=0.2, 가중치 0.05), 행동 크기/속도/범위 위반 패널티, 조기 종료 패널티(−10.0).

### 단계 3: 데이터 증강
- 참조 상태 초기화(RSI): 리셋 시 무작위 시연 위상 샘플링, 작은 섭동 추가.
- 궤적 증강: 각 에피소드에 섭동(Δp, Δψ) 적용, Δp_xy ∈ [−5, 5]² cm, Δp_z = 0, Δψ ∈ [−30°, 30°]; 혼합 가중치 w(t)는 식(11)에 따라 선형 보간, t_pickup과 t_use 사이에서 혼합 제거.
- 변환: 위치에 w(t)Δp 추가, 회전에 R_z(w(t)Δψ) 곱하기, 손 손목 및 손끝 위치는 섭동되지 않은 물체 루트를 기준으로 강체 매핑, 손가락 관절 참조는 불변. 리타게팅 최적화를 재실행하지 않고 물체 및 손 루트 자세를 직접 변환.

### 단계 4: 도메인 무작위화 및 커리큘럼 학습
- DR은 Isaac Lab 이벤트 항목으로 구현, 각 환경별 독립 샘플링: 물체 CoM 오프셋, 기하학 스케일링, 마찰, 질량 스케일링, 관절 k_p/k_d 스케일링, 손가락 기본 관절 오프셋.
- 중력 커리큘럼: 0에서 9.81 m/s²까지 130k 환경 단계에 걸쳐 선형 증가.
- 무작위 힘 커리큘럼: 130k 단계 후 활성화, 170k 단계에서 최대(선속도 ±0.5 m/s, 각속도 ±1.0 rad/s, 간격 1–5 s).
- 관측 노이즈: 위치 ±2 mm, 회전 ±0.02 rad, 관절 ±0.02 rad; 관측 시간 지연은 [0, 2] 제어 단계에서 균일 샘플링.
- 종료 조건: 물체가 작업 공간 이탈, 손이 물체에서 너무 멀어짐, 물체가 타겟 구성에서 임계값 이상 이탈(키포인트 위치 오차 > 0.15 m); WUJI 손 추가 종료: 손끝-테이블 접촉력 > 10N(모터 비역구동).

## 핵심 혁신

1. **RL 참조로서의 상호작용 인식 리타게팅**: OmniRetarget이 운동학적 매칭만 수행하는 것과 달리, Regrind는 리타게팅 최적화에서 손-물체 상호작용 메시의 변형 에너지를 명시적으로 보존하여 참조 궤적이 물리적으로 실행 가능하고 접촉 의미론을 유지하게 한다. 이는 손재주 조작에서 상호작용 인식 리타게팅과 RL 훈련 시스템을 결합한 최초의 사례이며, 성능의 핵심으로 입증되었다(DexMachina 대비 가위 작업 SR 99.8% → 22.3%).

2. **시간 가변 강체 변환 데이터 증강**: 리타게팅 최적화를 재실행하지 않고, 리타게팅 궤적에 시간 가변 SE(3) 섭동(위치 ±5 cm, 회전 ±30°)을 적용하여 훈련 중 무한 증강 궤적을 동적으로 생성하면서 원래 상호작용 관계를 보존한다. 이는 재최적화보다 효율적이며, 실제 세계 일반화를 크게 향상시킨다(무작위 초기 구성에서 LEAP-Scissors SR 8/10).

3. **극도로 간결한 보상 설계**: 키포인트 위치, 속도, 손목 자세 및 행동 정규화 항만 사용하며, 명시적 접촉 사전 지식이나 힘 피드백이 필요 없음에도 시뮬레이션에서 거의 완벽한 성공률을 달성한다. 이는 작업 특정 지식에 대한 의존도를 낮추어 다양한 물체와 로봇에 일반화 가능하게 한다.

## 실험 및 결과

**시뮬레이션 성능**(표 1, SPIDER 평균 5 시드, 기타 3 시드 × 1024 롤아웃):

| 방법 | LEAP-Scissors SR | LEAP-Screwdriver SR | WUJI-Scissors SR | WUJI-Screwdriver SR |
|------|------|------|------|------|
| Regrind (Ours) | 99.8% | 99.7% | 98.7% | 98.8% |
| SPIDER | 0.0% | 0.0% | 0.0% | 0.0% |
| DexMachina | 22.3% | 99.7% | 0.0% | 99.3% |
| Mink IK + RL | 2.0% | 0.0% | 0.0% | 3.1% |

**실제 세계 성능**(표 2, 제로샷 전이):

| 방법 | LEAP-Scissors SR | LEAP-Screwdriver SR | WUJI-Scissors SR | WUJI-Screwdriver SR |
|------|------|------|------|------|
| Regrind (Ours) | 9/10 | 10/10 | 0/10 | 9/10 |
| DexMachina | 0/10 | 2/10 | — | 5/10 |
| Mink IK + RL | — | — | — | 0/10 |

**실제 세계 일반화**(표 3, 무작위 초기 구성 ±5 cm, ±30°): LEAP-Scissors 8/10, LEAP-Screwdriver 10/10, WUJI-Screwdriver 9/10.

**핵심 해석**: SPIDER는 완전히 실패(시뮬레이션 SR 0%)하여, 물리 기반 리타게팅이 동역학을 고려하지만 생성 궤적 품질이 낮음을 시사한다. DexMachina는 드라이버 작업에서 시뮬레이션이 거의 완벽하지만 실제 전이가 낮아(2/10), 상호작용 보존이 부족한 리타게팅이 정책이 시뮬레이션 아티팩트를 활용하게 만든다는 것을 보여준다. Regrind는 세 가지 작업에서 안정적으로 전이되며, 유일한 실패인 WUJI-Scissors는 비역구동 모터의 sim-to-real 격차와 실제 가위 메시 부정확성에 기인한다.

## 경계 및 한계

논문은 한계를 명시적으로 논의하지 않았지만, 방법에서 추론할 수 있다: 배포는 모션 캡처를 통해 물체 상태를 획득하는 데 의존하며, 시각적 인식 문제를 해결하지 않음; 정밀한 시스템 식별 필요(실제 로봇 응답 지연 1–2 단계가 관측 시간 지연으로 모델링됨); 다중 작업 학습, 장기 조작, 양손 조작, 비강체 물체는 다루지 않음; WUJI-Scissors 작업은 모든 방법에서 실패하여 비역구동 모터의 sim-to-real 격차가 여전히 열린 문제임을 시사. 논문은 추론 빈도, 훈련 시간 등 엔지니어링 세부 사항을 언급하지 않음.

## 엔지니어링 시사점

재현 시 세 가지 핵심 사항을 먼저 확인하라: **리타게팅 솔버의 실행 가능 집합 정의**(특히 충돌 쌍 필터링 및 속도 경계)는 참조 궤적 품질에 직접 영향을 미침; **데이터 증강의 섭동 범위**(±5 cm, ±30°) 및 혼합 가중치 w(t)의 보간 구간(t_pickup에서 t_use까지)은 정책의 일반화 경계를 결정; **시스템 식별**—실제 로봇 응답 지연 1–2 단계(30–60 ms)는 시뮬레이션 관측 파이프라인에서 모델링해야 하며, 그렇지 않으면 sim-to-real이 실패함.

가장 함정에 빠지기 쉬운 부분: WUJI 손의 비역구동 모터는 추가 종료 조건(손끝 접촉력 > 10N)이 필요하며, 그렇지 않으면 훈련이 실행 불가능한 접촉 패턴을 활용함; LEAP 손은 3D 프린팅 확대 물체(s=2 스케일링)를 사용해야 하며, 실제 크기 물체를 직접 사용하면 기하학적 불일치가 발생할 수 있음; 보상 가중치 중 행동 크기 패널티(WUJI만 해당) 및 조기 종료 패널티(−10.0)는 훈련 안정성에 큰 영향을 미치므로 표 4에 따라 정확히 설정해야 함. 기준선 비교 시 SPIDER는 공식 구현(MuJoCo Warp 워크플로우)을 사용해야 하고, DexMachina는 맞춤 구현 및 충돌 인식 후처리 추가가 필요하며, 그렇지 않으면 비교가 공정하지 않음.
