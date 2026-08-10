---
$id: ent_paper_zhu_cycloidal_quasi_direct_drive_a_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Cycloidal Quasi-Direct Drive Actuator Designs with Learning-based Torque Estimation for Legged Robotics
  zh: 面向足式机器人的摆线准直驱执行器设计与基于学习的扭矩估计
  ko: 족운동 로봇을 위한 사이클로이드 의사직구동 액추에이터 설계 및 학습 기반 토크 추정
summary:
  en: This paper presents a 10:1 Cycloidal Quasi-Direct Drive (C-QDD) actuator for legged robots and a GRU-based Actuator
    Network that estimates output torque from actuator state history to reduce the sim-to-real gap caused by cycloidal gear
    nonlinearities.
  zh: 本文提出一种用于足式机器人的10:1摆线准直驱（C-QDD）执行器，并设计基于GRU的执行器网络，通过执行器状态历史估计输出扭矩，以减小摆线齿轮非线性导致的仿真到现实差距。
  ko: 이 논문은 족운동 로봇을 위한 10:1 사이클로이드 의사직구동(C-QDD) 액추에이터와, 사이클로이드 기어 비선형성으로 인한 시뮬레이션-현실 간격을 줄이기 위해 액추에이터 상태 이력으로부터 출력 토크를 추정하는
    GRU 기반 액추에이터 네트워크를 제시한다.
domains:
- 02_components
- 07_ai_models_algorithms
- 06_design_engineering
- 03_manufacturing_processes
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- component
- intelligence
tags:
- cycloidal_drive
- quasi_direct_drive
- cqdd
- actuator
- torque_estimation
- gru
- actuator_network
- legged_robotics
- sim_to_real
- proprioceptive_actuator
- high_torque_density
- impact_resilience
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.16591v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py [2026-08-04] body rewritten as full-text
    six-section deep read (.staging/deep_read, DeepSeek deepseek-chat T<=0.3, arXiv HTML full text); en/ko sections regenerated
    by translate pipeline. | WP1 dedup merge 2026-08-06: merged ent_paper_zhu_cycloidal_quasi_direct_drive_a_2024 into this
    card (rules: same_arxiv). Backup+manifest: .staging/cleanup_wp12/. 深读+数字白名单复核通过 2026-08-10（试点）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: Cycloidal Quasi-Direct Drive Actuator Designs with Learning-based Torque Estimation for Legged Robotics
  url: https://arxiv.org/abs/2410.16591
  date: '2024'
  accessed_at: '2026-06-25'
theoretical_depth:
- system
---
## 概述

本文提出一种集成10:1摆线齿轮箱的准直驱（QDD）执行器（C-QDD），并开发基于门控循环单元（GRU）的扭矩估计框架，以建模摆线齿轮引入的非线性扭矩波动，缩小强化学习中的sim-to-real差距。硬件验证表明C-QDD在扭矩密度（64.21 Nm/kg）和背隙（7.03 arcmin）上优于同类QDD，PVA-GRU扭矩估计RMSE达0.966 Nm，较调优MLP改善43.54%。

## 它改变了什么

传统QDD执行器依赖行星齿轮或正齿轮，在紧凑空间内难以承受冲击载荷，且齿轮承载能力受限。摆线齿轮虽具有高刚性、紧凑性和最小背隙，但其非线性扭矩输出（如扭矩波动）在RL仿真中未被建模，导致sim-to-real差距显著。作者真正改变的是：将摆线齿轮从"不可用于QDD"的默认假设中解放出来，通过集成设计和学习式扭矩估计，使摆线齿轮的高承载优势得以在足式机器人动态控制中发挥。

此外，制造公差对摆线齿轮性能影响显著，传统解析建模难以精确描述。本文用数据驱动方式替代解析建模，使扭矩估计框架能捕捉高频非线性特征（如17.61 Hz扭矩波动），这在以往QDD设计中是不可行的——以前要么忽略波动导致sim-to-real失败，要么依赖复杂且脆弱的解析模型。

## 方法拆解

### 摆线齿轮箱设计
- 齿轮箱集成在定子内部，限制最大允许节圆直径，保持紧凑性
- 对比复合行星齿轮（太阳轮12齿、行星轮36/22齿、齿圈70齿，10:1减速比）与摆线齿轮承载能力
- 摆线轮廓由节圆直径2Z_r、偏心距Z_e和外销直径Z_p控制
- 输出销为18-8不锈钢精密肩螺钉，位于旋转中心19.5 mm处，每销最大扭矩59.13 Nm，总扭矩295.65 Nm
- 偏心距引起惯性不平衡，通过配重盘补偿：传动比Z_R = -Z_np/(Z_np - Z_nt) = -Z_nt（式1），偶数Z_R需2个盘，奇数需3个盘（式2-4）
- C-QDD采用2个配重盘（Z_R=10为偶数），但显著增加反射惯性，影响反向驱动性
- 采用非针轮外摆线环替代传统针轮设计，摆线盘和外环由4140合金钢制造（优于7075铝的刚性、耐磨性），线切割EDM加工，公差±2 μm

### GRU扭矩估计框架
- 输入向量两种变体：
  - PV-GRU：X_vt ∈ ℝ^{2L}，含关节误差q_e和速度q̇
  - PVA-GRU：X_at ∈ ℝ^{3L}，含q_e、q̇和加速度q̈
- 加入加速度q̈的理由：捕捉高频非线性扭矩动态（扭矩波动和振荡），位置和速度单独不足
- GRU架构选择：高效捕捉时间依赖，通过内部记忆处理历史状态，学习长期依赖
- 训练：监督学习，Adam优化器（初始学习率0.0001），One Cycle LR调度器
- 关键超参数：历史长度L=30（依据采样率和扭矩波动频率范围），GRU层数K=4（平衡复杂度与效率），批大小64

## 关键创新

1. **摆线齿轮与QDD的首次系统集成**：将10:1摆线齿轮箱集成在定子内部，实现64.21 Nm/kg扭矩密度（优于BEAR的47.7 Nm/kg和PULSE115-60的50 Nm/kg），同时保持7.03 arcmin的低背隙——这在以往QDD设计中因摆线齿轮的复杂性和制造敏感性而未被实现。

2. **学习式扭矩估计替代解析建模**：GRU框架（PVA-GRU）能预测17.61 Hz高频扭矩波动（地面真值17.24 Hz），相位偏移小于40°，而调优MLP无法捕捉0.6 Nm振幅、20 Hz频率的波动（相位偏移近180°）。这解决了摆线齿轮非线性扭矩输出导致的sim-to-real差距问题。

3. **加速度输入的引入**：PVA-GRU（含q̈）相比PV-GRU（不含q̈）在RMSE上改善3.7%，在平均误差上改善75.2%（0.097 vs 0.391 Nm），验证了加速度对捕捉高频扭矩动态的关键作用。

## 实验与结果

| 任务 | 基线 | 方法 | 关键指标 |
|------|------|------|----------|
| 扭矩估计 | 调优MLP | PVA-GRU | RMSE 0.966 Nm vs 1.711 Nm（改善43.54%） |
| 扭矩估计 | 调优MLP | PVA-GRU | 方差 0.923 Nm vs 2.903 Nm（改善68.21%） |
| 扭矩估计 | 基线MLP | PVA-GRU | RMSE 0.966 Nm vs 2.457 Nm |
| 扭矩波动预测 | PV-GRU | PVA-GRU | 平均误差 0.23 Nm vs 0.71 Nm |
| 反向驱动性 | [22] | C-QDD | 静态1.99 Nm vs 0.37 Nm；动态1.36 Nm vs - |
| 扭矩密度 | BEAR [35] | C-QDD | 64.2 Nm/kg vs 47.7 Nm/kg |
| 扭矩密度 | Lee et al. [5] | C-QDD | 64.2 Nm/kg vs 83.7 Nm/kg |

C-QDD性能：连续扭矩37.5 Nm，峰值89.9 Nm（受驱动板电流限制，低于BLDC预期的120 Nm），空载速度128.6 rpm，效率82.3%，背隙7.03±1.3 arcmin，扭矩控制带宽34.3 Hz（5 Nm），位置控制带宽22.13 Hz（5°）。GRU推理时间CPU 13 μs、GPU 2 μs，支持1 kHz以上控制回路。

## 边界与局限

- 峰值扭矩89.9 Nm显著低于BLDC预期120 Nm，原因是驱动板电流限制——硬件瓶颈而非设计缺陷
- 反向驱动扭矩（静态1.99 Nm、动态1.36 Nm）高于其他QDD（[22]为0.37 Nm、[37]为0.97 Nm），作者认为考虑到更高齿轮比和扭矩能力仍属可比，但这对需要高反向驱动性的应用（如物理人机交互）可能构成限制
- PVA-GRU依赖噪声较大的加速度测量，预测均值随时间不如PV-GRU平滑，方差更大——在加速度信号质量差的场景下性能可能退化
- 论文未明确训练数据集规模，也未在真实足式机器人上验证sim-to-real效果（仅单倒立摆测试）
- 配重盘（2个）虽满足静态平衡，但作者承认动态稳定需3个盘，2个盘方案在高速动态下可能存在残余振动

## 工程启示

- **复现优先核对**：摆线齿轮的制造公差（±2 μm）和材料选择（4140合金钢）是性能关键，线切割EDM加工精度直接影响背隙和扭矩波动特性——若复现时加工精度不足，扭矩估计框架的输入分布会偏移
- **GRU超参数敏感性**：历史长度L=30和层数K=4是基于采样率和波动频率确定的，更换执行器或采样率时需重新调优；加速度输入（PVA-GRU）虽提升精度但依赖加速度计质量，工程上需评估传感器噪声水平
- **计算预算**：GRU在CPU上13 μs、GPU上2 μs，足以支持1 kHz控制回路；但MLP在CPU上<1 μs、GPU上4.227 μs（数据传输瓶颈），若控制频率更高或计算资源受限，需权衡精度与延迟
- **下游集成注意**：C-QDD反向驱动扭矩较高（1.99 Nm静态），在RL训练中需将扭矩波动模型纳入仿真，否则sim-to-real差距仍会存在；建议在仿真中直接使用PVA-GRU预测的扭矩补偿项
- **最易踩坑**：配重盘数量（2 vs 3）对动态稳定性的影响——偶数传动比下2个盘虽静态平衡，但高速动态下材料变形和制造误差可能导致振动，需实测验证

## 参考
- http://arxiv.org/abs/2410.16591v2

## Overview

This paper proposes a quasi-direct drive (QDD) actuator (C-QDD) integrating a 10:1 cycloidal gearbox, and develops a torque estimation framework based on Gated Recurrent Units (GRU) to model the nonlinear torque fluctuations introduced by the cycloidal gear, thereby narrowing the sim-to-real gap in reinforcement learning. Hardware validation shows that C-QDD outperforms comparable QDD actuators in torque density (64.21 Nm/kg) and backlash (7.03 arcmin), with the PVA-GRU torque estimation achieving an RMSE of 0.966 Nm, a 43.54% improvement over the tuned MLP.

## What It Changes

Traditional QDD actuators rely on planetary or spur gears, which struggle to withstand impact loads in compact spaces and have limited gear load capacity. Although cycloidal gears offer high rigidity, compactness, and minimal backlash, their nonlinear torque output (e.g., torque fluctuations) is not modeled in RL simulations, leading to significant sim-to-real gaps. What the authors truly change is: liberating cycloidal gears from the default assumption of "unsuitable for QDD," and through integrated design and learning-based torque estimation, enabling the high load-bearing advantages of cycloidal gears to be leveraged in dynamic control of legged robots.

Furthermore, manufacturing tolerances significantly affect cycloidal gear performance, making precise analytical modeling difficult. This paper replaces analytical modeling with a data-driven approach, enabling the torque estimation framework to capture high-frequency nonlinear features (e.g., 17.61 Hz torque fluctuations)—something infeasible in previous QDD designs, where fluctuations were either ignored (leading to sim-to-real failure) or relied on complex and fragile analytical models.

## Method Breakdown

### Cycloidal Gearbox Design
- The gearbox is integrated inside the stator, limiting the maximum allowable pitch circle diameter to maintain compactness
- Compares load capacity between compound planetary gears (sun gear 12 teeth, planet gears 36/22 teeth, ring gear 70 teeth, 10:1 reduction ratio) and cycloidal gears
- Cycloidal profile is controlled by pitch circle diameter \(2Z_r\), eccentricity \(Z_e\), and outer pin diameter \(Z_p\)
- Output pins are 18-8 stainless steel precision shoulder screws located 19.5 mm from the rotation center, each with a maximum torque of 59.13 Nm, totaling 295.65 Nm
- Eccentricity causes inertial imbalance, compensated by counterweight discs: transmission ratio \(Z_R = -Z_{np}/(Z_{np} - Z_{nt}) = -Z_{nt}\) (Eq. 1), even \(Z_R\) requires 2 discs, odd requires 3 discs (Eqs. 2-4)
- C-QDD uses 2 counterweight discs (\(Z_R=10\) is even), but this significantly increases reflected inertia, affecting backdrivability
- Adopts a non-pin-wheel outer cycloidal ring instead of the traditional pin-wheel design; cycloidal disc and outer ring are made of 4140 alloy steel (superior rigidity and wear resistance over 7075 aluminum), machined via wire EDM with tolerances of ±2 μm

### GRU Torque Estimation Framework
- Two variants of input vectors:
  - PV-GRU: \(X_{vt} \in \mathbb{R}^{2L}\), containing joint error \(q_e\) and velocity \(\dot{q}\)
  - PVA-GRU: \(X_{at} \in \mathbb{R}^{3L}\), containing \(q_e\), \(\dot{q}\), and acceleration \(\ddot{q}\)
- Rationale for adding acceleration \(\ddot{q}\): captures high-frequency nonlinear torque dynamics (torque fluctuations and oscillations), which position and velocity alone are insufficient to capture
- GRU architecture choice: efficiently captures temporal dependencies, processes historical states through internal memory, and learns long-term dependencies
- Training: supervised learning, Adam optimizer (initial learning rate 0.0001), One Cycle LR scheduler
- Key hyperparameters: history length \(L=30\) (based on sampling rate and torque fluctuation frequency range), GRU layers \(K=4\) (balancing complexity and efficiency), batch size 64

## Key Innovations

1. **First systematic integration of cycloidal gears with QDD**: Integrates a 10:1 cycloidal gearbox inside the stator, achieving a torque density of 64.21 Nm/kg (outperforming BEAR's 47.7 Nm/kg and PULSE115-60's 50 Nm/kg) while maintaining low backlash of 7.03 arcmin—previously unrealized in QDD designs due to the complexity and manufacturing sensitivity of cycloidal gears.

2. **Learning-based torque estimation replacing analytical modeling**: The GRU framework (PVA-GRU) predicts 17.61 Hz high-frequency torque fluctuations (ground truth 17.24 Hz) with a phase offset of less than 40°, whereas the tuned MLP fails to capture fluctuations with 0.6 Nm amplitude and 20 Hz frequency (phase offset near 180°). This addresses the sim-to-real gap caused by the nonlinear torque output of cycloidal gears.

3. **Introduction of acceleration input**: PVA-GRU (with \(\ddot{q}\)) improves RMSE by 3.7% and mean error by 75.2% (0.097 vs 0.391 Nm) compared to PV-GRU (without \(\ddot{q}\)), validating the critical role of acceleration in capturing high-frequency torque dynamics.

## Experiments and Results

| Task | Baseline | Method | Key Metric |
|------|----------|--------|------------|
| Torque estimation | Tuned MLP | PVA-GRU | RMSE 0.966 Nm vs 1.711 Nm (43.54% improvement) |
| Torque estimation | Tuned MLP | PVA-GRU | Variance 0.923 Nm vs 2.903 Nm (68.21% improvement) |
| Torque estimation | Baseline MLP | PVA-GRU | RMSE 0.966 Nm vs 2.457 Nm |
| Torque fluctuation prediction | PV-GRU | PVA-GRU | Mean error 0.23 Nm vs 0.71 Nm |
| Backdrivability | [22] | C-QDD | Static 1.99 Nm vs 0.37 Nm; Dynamic 1.36 Nm vs - |
| Torque density | BEAR [35] | C-QDD | 64.2 Nm/kg vs 47.7 Nm/kg |
| Torque density | Lee et al. [5] | C-QDD | 64.2 Nm/kg vs 83.7 Nm/kg |

C-QDD performance: continuous torque 37.5 Nm, peak torque 89.9 Nm (limited by driver board current, below the BLDC-expected 120 Nm), no-load speed 128.6 rpm, efficiency 82.3%, backlash 7.03±1.3 arcmin, torque control bandwidth 34.3 Hz (5 Nm), position control bandwidth 22.13 Hz (5°). GRU inference time: 13 μs on CPU, 2 μs on GPU, supporting control loops above 1 kHz.

## Boundaries and Limitations

- Peak torque of 89.9 Nm is significantly lower than the BLDC-expected 120 Nm, due to driver board current limits—a hardware bottleneck rather than a design flaw
- Backdriving torque (static 1.99 Nm, dynamic 1.36 Nm) is higher than other QDD actuators ([22] at 0.37 Nm, [37] at 0.97 Nm); the authors argue this remains comparable given the higher gear ratio and torque capability, but it may limit applications requiring high backdrivability (e.g., physical human-robot interaction)
- PVA-GRU relies on noisy acceleration measurements; its prediction mean is less smooth over time than PV-GRU and has larger variance—performance may degrade in scenarios with poor acceleration signal quality
- The paper does not specify the training dataset size, nor does it validate sim-to-real effectiveness on a real legged robot (only single inverted pendulum tests)
- Counterweight discs (2) satisfy static balance, but the authors acknowledge that dynamic stability requires 3 discs; the 2-disc configuration may exhibit residual vibration under high-speed dynamics

## Engineering Insights

- **Prioritize verification during reproduction**: Manufacturing tolerances (±2 μm) and material selection (4140 alloy steel) for cycloidal gears are critical to performance; wire EDM machining precision directly affects backlash and torque fluctuation characteristics—if machining precision is insufficient during reproduction, the input distribution of the torque estimation framework will shift
- **GRU hyperparameter sensitivity**: History length \(L=30\) and layers \(K=4\) are determined based on sampling rate and fluctuation frequency; re-tuning is required when changing actuators or sampling rates; acceleration input (PVA-GRU) improves accuracy but depends on accelerometer quality, requiring engineering evaluation of sensor noise levels
- **Computational budget**: GRU runs at 13 μs on CPU and 2 μs on GPU, sufficient for 1 kHz control loops; however, MLP runs at <1 μs on CPU and 4.227 μs on GPU (data transfer bottleneck); if control frequency is higher or computational resources are constrained, a trade-off between accuracy and latency is needed
- **Downstream integration considerations**: C-QDD's higher backdriving torque (1.99 Nm static) requires incorporating the torque fluctuation model into simulation during RL training; otherwise, the sim-to-real gap persists; it is recommended to directly use PVA-GRU-predicted torque compensation terms in simulation
- **Most common pitfall**: The impact of counterweight disc count (2 vs 3) on dynamic stability—with even transmission ratios, 2 discs achieve static balance, but under high-speed dynamics, material deformation and manufacturing errors may cause vibration, requiring empirical validation

## 개요

본 논문은 10:1 사이클로이드 감속기를 통합한 준직구동(QDD) 액추에이터(C-QDD)를 제안하고, 게이트 순환 유닛(GRU) 기반 토크 추정 프레임워크를 개발하여 사이클로이드 기어가 도입하는 비선형 토크 변동을 모델링함으로써 강화학습에서의 sim-to-real 격차를 줄인다. 하드웨어 검증 결과 C-QDD는 토크 밀도(64.21 Nm/kg)와 백래시(7.03 arcmin)에서 유사 QDD보다 우수하며, PVA-GRU 토크 추정 RMSE는 0.966 Nm로 튜닝된 MLP 대비 43.54% 개선되었다.

## 무엇을 바꾸었는가

기존 QDD 액추에이터는 유성 기어나 평기어에 의존하여 컴팩트한 공간에서 충격 하중을 견디기 어렵고 기어 하중 용량이 제한적이다. 사이클로이드 기어는 높은 강성, 컴팩트함, 최소 백래시를 갖지만, 비선형 토크 출력(예: 토크 변동)이 RL 시뮬레이션에서 모델링되지 않아 sim-to-real 격차가 크다. 저자가 실제로 바꾼 것은 사이클로이드 기어를 "QDD에 사용 불가"라는 기본 가정에서 해방시켜, 통합 설계와 학습 기반 토크 추정을 통해 사이클로이드 기어의 높은 하중 용량 이점을 족형 로봇의 동적 제어에서 활용할 수 있게 한 것이다.

또한 제조 공차는 사이클로이드 기어 성능에 큰 영향을 미치며, 기존 해석적 모델링으로는 정밀하게 설명하기 어렵다. 본 논문은 데이터 기반 방식으로 해석적 모델링을 대체하여 토크 추정 프레임워크가 고주파 비선형 특성(예: 17.61 Hz 토크 변동)을 포착할 수 있게 한다. 이는 기존 QDD 설계에서는 불가능했던 것이다—이전에는 변동을 무시하여 sim-to-real 실패를 초래하거나, 복잡하고 취약한 해석 모델에 의존해야 했다.

## 방법 분해

### 사이클로이드 감속기 설계
- 감속기는 고정자 내부에 통합되어 최대 허용 피치 원 직경을 제한하고 컴팩트함을 유지
- 복합 유성 기어(태양 기어 12톱니, 유성 기어 36/22톱니, 링 기어 70톱니, 10:1 감속비)와 사이클로이드 기어의 하중 용량 비교
- 사이클로이드 프로파일은 피치 원 직경 2Z_r, 편심 거리 Z_e, 외부 핀 직경 Z_p에 의해 제어
- 출력 핀은 18-8 스테인리스 스틸 정밀 숄더 나사로, 회전 중심에서 19.5 mm 위치, 핀당 최대 토크 59.13 Nm, 총 토크 295.65 Nm
- 편심 거리는 관성 불균형을 유발하며, 밸런스 디스크로 보상: 감속비 Z_R = -Z_np/(Z_np - Z_nt) = -Z_nt (식 1), 짝수 Z_R은 2개 디스크, 홀수는 3개 디스크 필요 (식 2-4)
- C-QDD는 2개의 밸런스 디스크 사용(Z_R=10은 짝수), 그러나 반사 관성이 크게 증가하여 역구동성에 영향
- 기존 핀 휠 외 사이클로이드 링 대신 비핀 휠 외 사이클로이드 링 채택, 사이클로이드 디스크와 외부 링은 4140 합금강으로 제조(7075 알루미늄보다 강성, 내마모성 우수), 와이어 EDM 가공, 공차 ±2 μm

### GRU 토크 추정 프레임워크
- 입력 벡터 두 가지 변형:
  - PV-GRU: X_vt ∈ ℝ^{2L}, 관절 오차 q_e와 속도 q̇ 포함
  - PVA-GRU: X_at ∈ ℝ^{3L}, q_e, q̇ 및 가속도 q̈ 포함
- 가속도 q̈ 추가 이유: 고주파 비선형 토크 동역학(토크 변동 및 진동) 포착, 위치와 속도만으로는 불충분
- GRU 아키텍처 선택: 시간 의존성을 효율적으로 포착, 내부 메모리를 통해 과거 상태 처리, 장기 의존성 학습
- 훈련: 지도 학습, Adam 옵티마이저(초기 학습률 0.0001), One Cycle LR 스케줄러
- 주요 하이퍼파라미터: 히스토리 길이 L=30(샘플링 레이트와 토크 변동 주파수 범위 기반), GRU 레이어 수 K=4(복잡성과 효율성 균형), 배치 크기 64

## 핵심 혁신

1. **사이클로이드 기어와 QDD의 최초 체계적 통합**: 10:1 사이클로이드 감속기를 고정자 내부에 통합하여 64.21 Nm/kg 토크 밀도(BEAR의 47.7 Nm/kg 및 PULSE115-60의 50 Nm/kg보다 우수)를 달성하면서 7.03 arcmin의 낮은 백래시 유지—이는 기존 QDD 설계에서 사이클로이드 기어의 복잡성과 제조 민감성 때문에 실현되지 못했던 것이다.

2. **해석적 모델링 대체 학습 기반 토크 추정**: GRU 프레임워크(PVA-GRU)는 17.61 Hz 고주파 토크 변동(실측 17.24 Hz)을 예측할 수 있으며 위상 오프셋이 40° 미만인 반면, 튜닝된 MLP는 0.6 Nm 진폭, 20 Hz 주파수의 변동을 포착하지 못한다(위상 오프셋 약 180°). 이는 사이클로이드 기어의 비선형 토크 출력으로 인한 sim-to-real 격차 문제를 해결한다.

3. **가속도 입력 도입**: PVA-GRU(q̈ 포함)는 PV-GRU(q̈ 미포함) 대비 RMSE에서 3.7% 개선, 평균 오차에서 75.2% 개선(0.097 vs 0.391 Nm)되어 고주파 토크 동역학 포착에 가속도의 핵심 역할을 검증한다.

## 실험 및 결과

| 작업 | 기준선 | 방법 | 핵심 지표 |
|------|------|------|----------|
| 토크 추정 | 튜닝된 MLP | PVA-GRU | RMSE 0.966 Nm vs 1.711 Nm(43.54% 개선) |
| 토크 추정 | 튜닝된 MLP | PVA-GRU | 분산 0.923 Nm vs 2.903 Nm(68.21% 개선) |
| 토크 추정 | 기준선 MLP | PVA-GRU | RMSE 0.966 Nm vs 2.457 Nm |
| 토크 변동 예측 | PV-GRU | PVA-GRU | 평균 오차 0.23 Nm vs 0.71 Nm |
| 역구동성 | [22] | C-QDD | 정적 1.99 Nm vs 0.37 Nm; 동적 1.36 Nm vs - |
| 토크 밀도 | BEAR [35] | C-QDD | 64.2 Nm/kg vs 47.7 Nm/kg |
| 토크 밀도 | Lee et al. [5] | C-QDD | 64.2 Nm/kg vs 83.7 Nm/kg |

C-QDD 성능: 연속 토크 37.5 Nm, 피크 89.9 Nm(드라이버 보드 전류 제한으로 BLDC 예상 120 Nm보다 낮음), 무부하 속도 128.6 rpm, 효율 82.3%, 백래시 7.03±1.3 arcmin, 토크 제어 대역폭 34.3 Hz(5 Nm), 위치 제어 대역폭 22.13 Hz(5°). GRU 추론 시간 CPU 13 μs, GPU 2 μs로 1 kHz 이상 제어 루프 지원.

## 경계 및 한계

- 피크 토크 89.9 Nm는 BLDC 예상 120 Nm보다 현저히 낮으며, 원인은 드라이버 보드 전류 제한—설계 결함이 아닌 하드웨어 병목
- 역구동 토크(정적 1.99 Nm, 동적 1.36 Nm)는 다른 QDD([22]의 0.37 Nm, [37]의 0.97 Nm)보다 높으며, 저자는 더 높은 기어비와 토크 용량을 고려하면 여전히 비교 가능하다고 주장하지만, 높은 역구동성이 필요한 응용(예: 물리적 인간-로봇 상호작용)에서는 제한이 될 수 있음
- PVA-GRU는 노이즈가 큰 가속도 측정에 의존하며, 예측 평균은 시간에 따라 PV-GRU만큼 매끄럽지 않고 분산이 더 큼—가속도 신호 품질이 낮은 시나리오에서는 성능이 저하될 수 있음
- 논문은 훈련 데이터 세트 규모를 명시하지 않았으며, 실제 족형 로봇에서 sim-to-real 효과를 검증하지 않음(단일 역진자 테스트만 수행)
- 밸런스 디스크(2개)는 정적 균형을 충족하지만, 저자는 동적 안정성을 위해 3개 디스크가 필요하다고 인정하며, 2개 디스크 방식은 고속 동적 조건에서 잔류 진동이 있을 수 있음

## 공학적 시사점

- **재현 시 우선 확인 사항**: 사이클로이드 기어의 제조 공차(±2 μm)와 재료 선택(4140 합금강)은 성능의 핵심이며, 와이어 EDM 가공 정밀도는 백래시와 토크 변동 특성에 직접 영향을 미침—재현 시 가공 정밀도가 부족하면 토크 추정 프레임워크의 입력 분포가 편향됨
- **GRU 하이퍼파라미터 민감성**: 히스토리 길이 L=30과 레이어 수 K=4는 샘플링 레이트와 변동 주파수에 기반하여 결정되며, 액추에이터나 샘플링 레이트를 변경할 때 재튜닝 필요; 가속도 입력(PVA-GRU)은 정밀도를 높이지만 가속도계 품질에 의존하므로 공학적으로 센서 노이즈 수준 평가 필요
- **계산 예산**: GRU는 CPU에서 13 μs, GPU에서 2 μs로 1 kHz 제어 루프를 지원하기에 충분; 그러나 MLP는 CPU에서 <1 μs, GPU에서 4.227 μs(데이터 전송 병목)이므로 제어 주파수가 더 높거나 계산 자원이 제한된 경우 정밀도와 지연 시간 간의 균형 필요
- **하류 통합 주의 사항**: C-QDD의 역구동 토크가 비교적 높으므로(정적 1.99 Nm), RL 훈련에서 토크 변동 모델을 시뮬레이션에 포함하지 않으면 sim-to-real 격차가 여전히 존재; 시뮬레이션에서 PVA-GRU가 예측한 토크 보상 항을 직접 사용할 것을 권장
- **가장 흔한 함정**: 밸런스 디스크 수(2 vs 3)의 동적 안정성 영향—짝수 감속비에서 2개 디스크는 정적 균형을 이루지만, 고속 동적 조건에서 재료 변형과 제조 오차로 인한 진동이 발생할 수 있으므로 실측 검증 필요
