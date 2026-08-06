---
$id: ent_paper_prime_physically_consistent_robotic_iner_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PRIME: Physically-consistent Robotic Inertial and Motion Estimation for Legged and Humanoid Robots'
  zh: 'PRIME: Physically-consistent Robotic Inertial and Motion Estimation for Legged and Humanoid Robots'
  ko: 'PRIME: Physically-consistent Robotic Inertial and Motion Estimation for Legged and Humanoid Robots'
summary:
  en: Humanoid and legged robots interact with the environment through intermittent contacts, making accurate motion estimation
    fundamentally dependent on reasoning about contact dynamics. However, standard sensing pipelines-whether based on onboard
    proprioception with Extended Kalman Filters (EKFs) or external motion capture systems-recover only kinematics, while contact
    forces, contact timing, and.
  zh: PRIME 是一个面向腿式与类人机器人的离线全信息估计框架，将运动学测量与执行器命令细化为动力学一致的轨迹，同时联合估计摩擦接触力与物理一致的惯性参数。其核心贡献在于将平滑接触动力学嵌入最大后验（MAP）优化，通过解析梯度实现高效求解，并在四足与人形平台验证了惯性辨识与接触重建的精度提升。
  ko: Humanoid and legged robots interact with the environment through intermittent contacts, making accurate motion estimation
    fundamentally dependent on reasoning about contact dynamics. However, standard sensing pipelines-whether based on onboard
    proprioception with Extended Kalman Filters (EKFs) or external motion capture systems-recover only kinematics, while contact
    forces, contact timing, and.
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
- prime
- physically
- consistent
- robotic
- iner
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-classics (2026-08-05), source channel(s): xiaoze_P143. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2605.17681 PRIME: Physically-consistent Robotic Inertial and Motion Estimation for Legged a'
  url: https://arxiv.org/abs/2605.17681
  date: '2026-05-17'
  accessed_at: '2026-08-05'
---

## 概述

PRIME 是一个面向腿式与类人机器人的离线全信息估计框架，将运动学测量与执行器命令细化为动力学一致的轨迹，同时联合估计摩擦接触力与物理一致的惯性参数。其核心贡献在于将平滑接触动力学嵌入最大后验（MAP）优化，通过解析梯度实现高效求解，并在四足与人形平台验证了惯性辨识与接触重建的精度提升。

## 它改变了什么

现有感知管线（EKF 或 mocap）只输出运动学，接触力、接触时间与惯性参数不可观测，导致重建轨迹违反刚体动力学，尤其在接触丰富的运动中。这种不一致直接阻碍下游规划、控制以及数据驱动方法（如模仿学习、VLA 模型）在真实世界的部署。PRIME 改变的不是“多估一个量”，而是把估计问题从纯运动学拟合重构为动力学一致的全信息估计——这意味着接触序列不再需要预先指定，惯性参数不再依赖人工标定，而是从数据中与运动轨迹联合推断。

另一个关键改变在于接触建模的范式：传统接触约束估计器将接触检测与估计解耦（通过高度阈值或压力传感器预分配接触标志），PRIME 则用平滑互补约束将接触激活/脱离内化为优化变量。这消除了解耦带来的误差累积，使接触重建在滚动、部分支撑等复杂足部状态下的精度显著提升（仿真中相对力误差从 52.693% 降至 10.494%，由表内数值计算）。

## 方法拆解

### 问题形式化
将运动与参数估计构建为 MAP 问题，状态轨迹 x_{0:T} 与惯性参数 θ 联合优化，目标函数包含测量残差（编码器、mocap、扭矩）与参数正则化项，受离散动力学约束。

### 平滑接触动力学
- 采用 log-barrier 松弛逼近二阶锥互补约束，配合 Anitescu 风格摩擦锥，形成无约束凸优化子问题。
- 关键参数 κ 控制平滑程度：κ → ∞ 恢复硬接触，中等 κ 引入“远距离力”效应，提高对接触切换与测量噪声的鲁棒性。默认 κ = 500。
- 接触冲量（法向与切向）从一阶最优性条件恢复，无需直接力测量。

### 解析梯度推导
- 平滑接触动力学的最优性条件 g(v⁺, θ) = 0，通过隐函数定理得到灵敏度 ∂v⁺/∂θ = −(∂g/∂v⁺)⁻¹(∂g/∂θ)。
- 该解析梯度使 PFIE 求解无需数值微分，是计算效率的关键。

### 惯性参数化
- 采用 Log-Cholesky 参数化，从参数 θ 到标准惯性参数 π 的光滑映射，闭式雅可比保证正定性，无需显式约束。

### 优化求解
- 整体 PFIE 用可行性驱动微分动态规划（FDDP）求解，允许从动力学不可行轨迹初始化，逐步将缺陷驱动至零。
- 动力学离散化采用半隐式欧拉；接触子问题用定制牛顿求解器，Armijo 回溯线搜索确定步长 α，DDP 反向传递加正则化 η 保证 Hessian 正定。

## 关键创新

1. **接触动力学与估计的端到端联合**：将接触序列、接触力与惯性参数统一为优化变量，而非预分配或阈值化。这是对“先检测后估计”范式的根本性替代，直接消除了解耦误差。
2. **解析梯度驱动的可微接触动力学**：通过隐函数定理获得闭式灵敏度，使 PFIE 求解在 1000 步时域内仅需约 200 s（Intel Core i9-13900），单步 rollout 带微分平均 80 μs，达到实用水平。
3. **Log-Cholesky 惯性参数化的物理一致性**：无需显式正定约束即可保证惯性矩阵物理可行，且闭式雅可比简化了优化中的导数计算——这是工程实现中容易被忽视但至关重要的设计。

## 实验与结果

### 仿真与硬件设置
- Hopper：2.5 s 时域，0.025 s 离散化，验证从有偏初始惯性模型出发的辨识能力。
- Go2 四足：10 s 时域，0.01 s 离散化（1000 样本），仿真含 3 kg 载荷与质心下移 0.1 m 两试验；硬件挂 2.3 kg 杠铃片。
- G1 人形：15 s 时域，0.01 s 离散化（1500 样本），采集行走、跑步、跳舞；跳舞序列用 Bertec-4060 力板（1000 Hz，±0.4 N 分辨率）验证接触力。

### 关键结果
| 指标 | PRIME | Baseline | 变化 |
|------|-------|----------|------|
| G1 仿真 RMSE_F [N] | 19.833 | 73.103 | −72.9%（由表内数值计算） |
| G1 仿真相对误差_F [%] | 10.494 | 52.693 | −80.1%（由表内数值计算） |
| G1 硬件 RMSE_F [N]（有 ID） | 24.486 | 26.141（无 ID） | −6.3%（由表内数值计算） |
| G1 硬件 FIE 成本 [×10³] | 1.016 | 1.880 | −46.0%（由表内数值计算） |

惯性辨识方面，Go2 硬件估计附加质量约 4.8 kg（实际 4.6 kg），G1 估计附加质量约 3.4 kg（实际 2.914 kg，含电池 2.496 kg），质心位置与加载方向一致。G1 总质量估计 38.029 kg 与尺度测量吻合，名义模型 35.115 kg 偏差 2.914 kg。

## 边界与局限

- **离线非实时**：PRIME 为全信息估计，G1 15 s 时域求解约 400 s，无法在线部署；移动时域估计（MHE）与到达成本设计未实现。
- **Anitescu 松弛的伪物理行为**：切向滑动可能伴随非零法向分离（虚假抬离），作者认为在接触牢固且短暂的场景中可接受，但极端滑动场景下可能失真。
- **可观测性未分析**：未研究有限感官信息下运动、接触力与惯性参数的可辨识性，以及任务结构对估计性能的影响。
- **上肢未建模**：G1 三指手未纳入模型，剩余力矩不匹配集中在上肢关节。
- **操作任务未验证**：公式可扩展至操作，但无实验证据。

## 工程启示

复现 PRIME 时，最先核对的是 κ 参数与测量权重。默认 κ = 500 在硬件噪声大时需从较小值初始化并逐步增大，否则平滑伪影可能主导估计。权重设置中，浮基线速度由 mocap 位置微分获得，噪声敏感故权重较低（1×10¹）；mocap 方向测量因校准偏差与标记遮挡质量下降，IMU 角速度更鲁棒（权重 1.5×10²）——这两处权重若不调，硬件实验会直接发散。

最容易踩坑的是接触模型选择：G1 平面足必须用四角点接触近似，点接触模型虽框架不变但会损失精度。惯性参数正则化权重（4×10⁻²）不可省，否则 Log-Cholesky 参数化可能收敛到物理不合理的局部最优。对下游团队，建议先跑通 Go2 仿真试验（含 3 kg 载荷与质心下移 0.1 m）验证辨识方向正确，再上硬件；硬件实验需确保 mocap 与力板时间同步，否则接触力 RMSE 会显著恶化。

## Overview
Humanoid and legged robots interact with the environment through intermittent contacts, making accurate motion estimation fundamentally dependent on reasoning about contact dynamics. However, standard sensing pipelines-whether based on onboard proprioception with Extended Kalman Filters (EKFs) or external motion capture systems-recover only kinematics, while contact forces, contact timing, and inertial parameters remain unobserved. As a result, purely kinematic reconstructions often violate rigid-body dynamics, particularly during contact-rich motions. To enable accurate motion estimation from onboard kinematics in real-world deployment, we propose PRIME (Physically-consistent Robotic Inertial and Motion Estimation), a Maximum A Posteriori (MAP) formulation that refines measured kinematics and actuator commands into a dynamically consistent trajectory while jointly estimating frictional contact forces and physically consistent inertial parameters. Our approach incorporates differentiable contact dynamics with smoothed complementarity constraints and an Anitescu-style friction model, yielding a smooth optimization problem that remains tractable across versatile contact transitions. We evaluate PRIME on contact-rich locomotion with quadrupedal robots and the Unitree G1 humanoid, demonstrating improved trajectory consistency and accurate inertial parameter identification. Beyond improving state estimation and feedback control with calibrated inertial parameters, PRIME produces force- and contact-annotated motion reconstructions from real robots in deployment, which can be used to provide high-quality data for downstream learning applications, including large-scale behavior modeling and robot foundation models.

## 参考
- https://arxiv.org/abs/2605.17681

## 개요

PRIME은 다리 및 휴머노이드 로봇을 위한 오프라인 전정보(full-information) 추정 프레임워크로, 운동학적 측정과 액추에이터 명령을 동역학적으로 일관된 궤적으로 정제하면서 마찰 접촉력과 물리적으로 일관된 관성 파라미터를 동시에 추정합니다. 핵심 기여는 평활 접촉 동역학을 최대 사후(MAP) 최적화에 내장하고, 해석적 기울기를 통해 효율적으로 해를 구하며, 사족 및 휴머노이드 플랫폼에서 관성 식별과 접촉 재구성의 정확도 향상을 검증한 것입니다.

## 그것이 바꾸는 것

기존 인식 파이프라인(EKF 또는 모캡)은 운동학만 출력하며, 접촉력, 접촉 시간, 관성 파라미터는 관측 불가능하여 재구성된 궤적이 강체 동역학을 위반합니다. 특히 접촉이 풍부한 운동에서 이러한 불일치가 두드러집니다. 이러한 불일치는 하류의 계획, 제어, 그리고 데이터 기반 방법(모방 학습, VLA 모델 등)의 실제 세계 배포를 직접적으로 방해합니다. PRIME이 바꾸는 것은 "하나의 양을 더 추정하는 것"이 아니라, 추정 문제를 순수 운동학적 피팅에서 동역학적으로 일관된 전정보 추정으로 재구성하는 것입니다. 이는 접촉 시퀀스를 사전에 지정할 필요가 없고, 관성 파라미터가 수동 보정에 의존하지 않으며, 데이터로부터 운동 궤적과 함께 공동으로 추론된다는 것을 의미합니다.

또 다른 핵심 변화는 접촉 모델링의 패러다임에 있습니다. 기존 접촉 제약 추정기는 접촉 감지와 추정을 분리합니다(높이 임계값 또는 압력 센서로 접촉 플래그 사전 할당). PRIME은 평활 상보 제약을 사용하여 접촉 활성화/이탈을 최적화 변수로 내재화합니다. 이는 분리로 인한 오차 누적을 제거하고, 구름, 부분 지지 등 복잡한 발 상태에서 접촉 재구성 정확도를 크게 향상시킵니다(시뮬레이션에서 상대 힘 오차가 52.693%에서 10.494%로 감소, 표 내 수치로 계산).

## 방법 분해

### 문제 정식화
운동 및 파라미터 추정을 MAP 문제로 구축하고, 상태 궤적 x_{0:T}와 관성 파라미터 θ를 공동 최적화합니다. 목적 함수는 측정 잔차(엔코더, 모캡, 토크)와 파라미터 정규화 항을 포함하며, 이산 동역학 제약 조건을 따릅니다.

### 평활 접촉 동역학
- 로그-배리어 완화를 사용하여 2차 원뿔 상보 제약을 근사하고, Anitescu 스타일 마찰 원뿔과 결합하여 무제약 볼록 최적화 하위 문제를 형성합니다.
- 핵심 파라미터 κ는 평활도 정도를 제어합니다: κ → ∞는 경성 접촉을 복원하고, 중간 κ는 "원거리 힘" 효과를 도입하여 접촉 전환 및 측정 잡음에 대한 강건성을 높입니다. 기본값 κ = 500.
- 접촉 충격량(법선 및 접선)은 1차 최적성 조건에서 복원되며, 직접적인 힘 측정이 필요 없습니다.

### 해석적 기울기 유도
- 평활 접촉 동역학의 최적성 조건 g(v⁺, θ) = 0에서 암시 함수 정리를 통해 민감도 ∂v⁺/∂θ = −(∂g/∂v⁺)⁻¹(∂g/∂θ)를 얻습니다.
- 이 해석적 기울기는 PFIE 해석에 수치 미분이 필요 없게 하여 계산 효율성의 핵심입니다.

### 관성 파라미터화
- Log-Cholesky 파라미터화를 사용하여 파라미터 θ에서 표준 관성 파라미터 π로의 매끄러운 매핑을 제공하며, 폐형 야코비안이 양의 정부호성을 보장하여 명시적 제약이 필요 없습니다.

### 최적화 해석
- 전체 PFIE는 실현 가능성 기반 미분 동역학 프로그래밍(FDDP)으로 해결되며, 동역학적으로 실현 불가능한 궤적에서 초기화하여 결함을 점진적으로 0으로 구동합니다.
- 동역학 이산화는 반암시적 오일러를 사용하고, 접촉 하위 문제는 맞춤형 뉴턴 해석기로 해결하며, Armijo 후퇴 라인 서치로 스텝 크기 α를 결정하고, DDP 역전파에 정규화 η를 추가하여 Hessian의 양의 정부호성을 보장합니다.

## 핵심 혁신

1. **접촉 동역학과 추정의 종단 간 공동 처리**: 접촉 시퀀스, 접촉력, 관성 파라미터를 사전 할당이나 임계값 대신 최적화 변수로 통합합니다. 이는 "감지 후 추정" 패러다임에 대한 근본적 대안으로, 분리 오차를 직접 제거합니다.
2. **해석적 기울기 기반 미분 가능 접촉 동역학**: 암시 함수 정리를 통해 폐형 민감도를 얻어 PFIE 해석이 1000스텝 시간 영역에서 약 200초(Intel Core i9-13900)가 소요되고, 단일 스텝 롤아웃 미분 평균 80μs로 실용적 수준에 도달합니다.
3. **Log-Cholesky 관성 파라미터화의 물리적 일관성**: 명시적 양의 정부호 제약 없이 관성 행렬의 물리적 실현 가능성을 보장하며, 폐형 야코비안이 최적화에서 도함수 계산을 단순화합니다. 이는 엔지니어링 구현에서 간과되기 쉽지만 매우 중요한 설계입니다.

## 실험 및 결과

### 시뮬레이션 및 하드웨어 설정
- Hopper: 2.5초 시간 영역, 0.025초 이산화, 편향된 초기 관성 모델에서의 식별 능력 검증.
- Go2 사족: 10초 시간 영역, 0.01초 이산화(1000 샘플), 시뮬레이션은 3kg 하중 및 질량 중심 0.1m 하강 두 실험 포함; 하드웨어는 2.3kg 바벨 플레이트 장착.
- G1 휴머노이드: 15초 시간 영역, 0.01초 이산화(1500 샘플), 보행, 달리기, 춤 동작 수집; 춤 시퀀스는 Bertec-4060 힘 플레이트(1000Hz, ±0.4N 분해능)로 접촉력 검증.

### 핵심 결과
| 지표 | PRIME | Baseline | 변화 |
|------|-------|----------|------|
| G1 시뮬레이션 RMSE_F [N] | 19.833 | 73.103 | −72.9%(표 내 수치로 계산) |
| G1 시뮬레이션 상대 오차_F [%] | 10.494 | 52.693 | −80.1%(표 내 수치로 계산) |
| G1 하드웨어 RMSE_F [N] （ID 포함） | 24.486 | 26.141(ID 없음) | −6.3%(표 내 수치로 계산) |
| G1 하드웨어 FIE 비용 [×10³] | 1.016 | 1.880 | −46.0%(표 내 수치로 계산) |

관성 식별 측면에서 Go2 하드웨어는 추가 질량 약 4.8kg(실제 4.6kg)을 추정했고, G1은 추가 질량 약 3.4kg(실제 2.914kg, 배터리 2.496kg 포함)을 추정했으며, 질량 중심 위치는 하중 방향과 일치했습니다. G1 총 질량 추정치 38.029kg은 치수 측정과 일치했고, 명목 모델 35.115kg과 2.914kg의 편차를 보였습니다.

## 경계 및 한계

- **오프라인 비실시간**: PRIME은 전정보 추정으로, G1 15초 시간 영역 해석에 약 400초가 소요되어 온라인 배포가 불가능합니다. 이동 시간 영역 추정(MHE) 및 도달 비용 설계는 구현되지 않았습니다.
- **Anitescu 완화의 유사 물리적 동작**: 접선 슬라이딩에 0이 아닌 법선 분리(가짜 이탈)가 동반될 수 있으며, 저자는 접촉이 견고하고 짧은 시나리오에서는 허용 가능하지만 극단적인 슬라이딩 시나리오에서는 왜곡될 수 있다고 판단합니다.
- **관측 가능성 미분석**: 제한된 감각 정보 하에서 운동, 접촉력, 관성 파라미터의 식별 가능성과 작업 구조가 추정 성능에 미치는 영향은 연구되지 않았습니다.
- **상지 미모델링**: G1 3손가락 손은 모델에 포함되지 않았으며, 잔여 토크 불일치는 상지 관절에 집중됩니다.
- **조작 작업 미검증**: 공식은 조작으로 확장 가능하지만 실험적 증거는 없습니다.

## 엔지니어링 시사점

PRIME을 재현할 때 가장 먼저 확인해야 할 것은 κ 파라미터와 측정 가중치입니다. 기본값 κ = 500은 하드웨어 잡음이 클 때 작은 값에서 초기화하여 점진적으로 증가시켜야 하며, 그렇지 않으면 평활 아티팩트가 추정을 지배할 수 있습니다. 가중치 설정에서 부동 기준선 속도는 모캡 위치 미분으로 얻어지며 잡음에 민감하므로 가중치가 낮습니다(1×10¹). 모캡 방향 측정은 보정 편향과 마커 가림으로 품질이 저하되므로 IMU 각속도가 더 강건합니다(가중치 1.5×10²). 이 두 가중치를 조정하지 않으면 하드웨어 실험이 직접 발산합니다.

가장 함정에 빠지기 쉬운 것은 접촉 모델 선택입니다. G1 평면 발은 4점 접촉 근사가 필수이며, 점 접촉 모델은 프레임워크가 동일하더라도 정확도를 잃습니다. 관성 파라미터 정규화 가중치(4×10⁻²)는 생략할 수 없으며, 그렇지 않으면 Log-Cholesky 파라미터화가 물리적으로 비합리적인 국소 최적해로 수렴할 수 있습니다. 하류 팀에게는 먼저 Go2 시뮬레이션 실험(3kg 하중 및 질량 중심 0.1m 하강 포함)을 실행하여 식별 방향이 올바른지 검증한 후 하드웨어로 넘어갈 것을 권장합니다. 하드웨어 실험에서는 모캡과 힘 플레이트의 시간 동기화를 보장해야 하며, 그렇지 않으면 접촉력 RMSE가 크게 악화됩니다.
