---
$id: ent_paper_thorarena_benchmarking_humanoid_physical_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ThorArena: Benchmarking Humanoid Physical Interaction with Human Motion-Force Demonstrations'
  zh: 'ThorArena: Benchmarking Humanoid Physical Interaction with Human Motion-Force Demonstrations'
  ko: 'ThorArena: Benchmarking Humanoid Physical Interaction with Human Motion-Force Demonstrations'
summary:
  en: Humanoid robots are increasingly expected to perform contact-rich tasks that require not only accurate whole-body motion
    but also robust physical interaction with surrounding objects and humans. Although recent advances in humanoid motion
    imitation and whole-body control have achieved remarkable tracking performance, existing datasets and benchmarks primarily
    focus on kinematic motion while.
  zh: ThorArena 是一个面向人形机器人物理交互的基准测试框架，由研究团队构建，核心贡献在于将人类运动示范、实测交互力与力感知评估指标统一整合到同一评估体系中。该基准通过同步回放记录的外力，并引入力分层跟踪误差与 FATS 评分，揭示了仅基于运动学评估的不足，为物理交互场景下的全身控制策略提供了标准化评测手段。
  ko: Humanoid robots are increasingly expected to perform contact-rich tasks that require not only accurate whole-body motion
    but also robust physical interaction with surrounding objects and humans. Although recent advances in humanoid motion
    imitation and whole-body control have achieved remarkable tracking performance, existing datasets and benchmarks primarily
    focus on kinematic motion while.
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
- thorarena
- benchmarking
- humanoid
- physical
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch4-catchup (2026-08-05), source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2607.06052 ThorArena: Benchmarking Humanoid Physical Interaction with Human Motion-Force De'
  url: https://arxiv.org/abs/2607.06052
  date: '2026-07-07'
  accessed_at: '2026-08-05'
---

## 概述

ThorArena 是一个面向人形机器人物理交互的基准测试框架，由研究团队构建，核心贡献在于将人类运动示范、实测交互力与力感知评估指标统一整合到同一评估体系中。该基准通过同步回放记录的外力，并引入力分层跟踪误差与 FATS 评分，揭示了仅基于运动学评估的不足，为物理交互场景下的全身控制策略提供了标准化评测手段。

## 它改变了什么

现有的人形机器人评估体系存在一个根本性盲区：几乎所有数据集和基准都聚焦于运动学轨迹的复现精度，而将外部交互力视为一种隐式扰动或噪声。这种范式在自由空间运动跟踪中或许可行，但一旦策略部署到需要与物理世界持续接触的真实场景——比如推拉重物、协作搬运——仅凭运动学误差或任务成功率根本无法反映控制策略在力作用下的真实鲁棒性。ThorArena 真正改变的是评估的“物理真实性”维度：它不再把外力当作需要抑制的干扰，而是将其作为评估协议中一个显式、可控、可回放的输入变量。

这一转变的深层意义在于，它迫使研究者直面一个此前被回避的问题：一个在自由空间跟踪表现优异的策略，在持续外力作用下可能完全失效。ThorArena 通过引入力分层评估和鲁棒性比等诊断指标，将“策略在何种力水平下退化”这一信息显式地纳入评分体系，使得不同策略在物理交互场景下的优劣对比变得可量化、可复现。这实质上把评估从“运动学保真度”推进到了“力-运动耦合鲁棒性”的层面。

## 方法拆解

### 数据采集与任务设计
- 操作员佩戴 PICO 4 Ultra 头显与身体追踪器采集全身运动，双手各配备一个力传感器（通过 3D 打印挂钩固定），同步记录三轴力向量。
- 设计了 6 种代表性力交互任务：clean_table、liftdown_water、liftup_water、pull_chair、push_chair、syn_carry，覆盖垂直载荷、水平推力与协作场景。

### 力感知评估指标
- 基础跟踪误差 e_kp(t) = (1/N) Σ ‖x_ref_{k,t} − x_{k,t}‖₂，参考关键点每时间步重新锚定到机器人当前根位姿，消除全局根漂移影响。
- 按总施加手力的第 33 与第 66 百分位数将时间步分为低、中、高力区间。
- 力感知跟踪误差 E_i = √(w_low·(E_low)² + w_mid·(E_mid)² + w_high·(E_high)²)，权重 (w_low, w_mid, w_high) = (0.2, 0.3, 0.5)，强调高力区间。
- FATS 评分 S_i = 100·exp(−E_i/σ)·s_i，σ = 0.15 m，s_i = min(T_i/T_ref, 1) 为生存因子。
- 诊断指标：鲁棒性比 ρ = E_low / E_high，功率开销 η = P_high / P_low。

### 评估协议
- 基准运行器同步回放记录的力，将传感器坐标系力向量变换到手局部坐标系，再根据模拟手位姿转换到世界坐标系施加。
- 力系数设为 (1) 复现实测交互力，设为 (0) 禁用外力。
- 采用确定性全覆盖调度，所有示范序列在相同力回放协议下各评估一次，使用多个并行模拟环境。
- 统一策略适配器接口，每个策略在固定的部署兼容动力学配置下评估，跨任务保持不变。

## 关键创新

1. **力感知评估指标的引入**：首次将力分层与加权误差结合，通过第 33/66 百分位数划分力区间，并赋予高力区间更高权重（0.5），使得评估结果直接反映策略在强力交互下的退化程度。这一设计比单纯的任务成功率或运动学误差更能刻画物理交互的本质挑战。

2. **外力回放协议**：将记录的实测交互力作为可复现的评估输入，通过力系数控制是否施加外力，实现了“有外力”与“无外力”两种设置的对照评估。这种设计使得策略在相同力条件下的对比成为可能，消除了不同演示中力差异带来的混淆。

3. **诊断指标与主指标分离**：鲁棒性比 ρ 与功率开销 η 不进入 FATS 公式，而是作为独立诊断维度。这避免了单一指标掩盖策略在特定力区间的缺陷，例如 TWIST2 的高鲁棒性比实际反映的是其较大的低力基线误差，而非真正的强力鲁棒性。

## 实验与结果

实验对比了 4 种全身控制策略（Thor2、TWIST2、GMT、SONIC）在 6 个子任务上的表现，每种策略在有外力与无外力两种设置下评估。

| 指标 | Thor2 | TWIST2 | GMT | SONIC |
|------|-------|--------|-----|-------|
| FATS（外力） | 81.71 | 73.78 | 71.06 | 70.04 |
| Survival | 1.000 | 0.941 | 0.916 | 0.957 |
| Low KP (mm) | 27.8 | 37.5 | 37.8 | 43.9 |
| High KP (mm) | 33.8 | 40.7 | 42.4 | 54.1 |
| Robustness ρ | 0.812 | 0.908 | 0.888 | 0.816 |
| Power η | 1.27 | 1.23 | 1.37 | 1.22 |

关键发现：
- Thor2 在全部 6 个子任务上排名第一，平均 FATS 最高（81.71），生存率接近完美（1.000）。
- push_chair 是基准中最具挑战性的任务，TWIST2、GMT、SONIC 的生存率降至 0.73–0.81，持续水平力直接威胁平衡。
- 无外力设置下所有策略生存率接近 1.0，Thor2 FATS 为 84.31，最低关键点误差为 26.1 mm，性能差异主要来自上半身跟踪精度。

## 边界与局限

论文明确承认数据集规模有限：每个任务仅 60 条原始示范序列，共 360 条，覆盖的任务类型和力条件相对有限。力分层阈值（第 33/66 百分位数）和 FATS 公式的有效性尚未通过系统实验充分验证。基准目前仅在仿真环境中评估，未进行物理机器人验证，其现实适用性及与仿真结果的一致性尚待确认。此外，评估仅覆盖 4 种策略，未扩展到更多人形机器人本体和控制系统。

## 工程启示

复现或使用 ThorArena 时，首先应核对力回放协议的正确性：传感器坐标系到世界坐标系的变换链必须严格遵循论文描述，否则外力施加位置和方向将出现偏差。其次，FATS 公式中的 σ 参数（0.15 m）对评分灵敏度影响显著，不同机器人本体可能需要重新标定。最易踩坑的点在于力分层阈值的计算——必须基于每个数据集内的总施加手力分布计算第 33/66 百分位数，而非使用全局固定阈值。对于下游团队，建议在评估前先运行无外力设置作为基线，确认策略的跟踪精度达标后再引入外力，以便隔离力鲁棒性因素。诊断指标（ρ 和 η）应结合绝对误差联合解读，避免被单一指标误导。

## Overview
Humanoid robots are increasingly expected to perform contact-rich tasks that require not only accurate whole-body motion but also robust physical interaction with surrounding objects and humans. Although recent advances in humanoid motion imitation and whole-body control have achieved remarkable tracking performance, existing datasets and benchmarks primarily focus on kinematic motion while largely overlooking synchronized interaction forces. As a result, current evaluations fail to capture how external interaction forces affect tracking accuracy, stability, and control robustness. In this paper, we present ThorArena, a benchmark for evaluating force-aware humanoid interaction based on human demonstrations with synchronized motion and force measurements. We collect a real-world interaction dataset that simultaneously captures whole-body human motion and forces exerted by both hands across six representative physical interaction tasks. Based on these demonstrations, we propose force-aware evaluation metrics that jointly assess whole-body tracking accuracy, robustness under different force levels, control effort, and episode survival through the Force-Aware Tracking Score (FATS) and complementary diagnostic metrics. We further establish a unified benchmark protocol that replays recorded interaction forces in simulation and provides a standardized evaluation interface for different humanoid control policies. Experiments on representative whole-body control policies demonstrate that force-aware evaluation reveals substantial performance differences that remain largely hidden under conventional no-force evaluation. ThorArena provides a practical and reproducible framework for studying force-aware humanoid interaction and offers a new benchmark for evaluating contact-rich humanoid behaviors.

## 参考
- https://arxiv.org/abs/2607.06052

## 개요

ThorArena는 휴머노이드 로봇의 물리적 상호작용을 위한 벤치마크 프레임워크로, 연구팀이 구축했으며 핵심 기여는 인간의 동작 시연, 실측 상호작용 힘, 힘 인식 평가 지표를 하나의 평가 체계에 통합한 점입니다. 이 벤치마크는 기록된 외력을 동기화하여 재생하고 힘 계층화 추적 오차와 FATS 점수를 도입함으로써 운동학 기반 평가만의 한계를 드러내며, 물리적 상호작용 시나리오에서의 전신 제어 전략에 표준화된 평가 수단을 제공합니다.

## 무엇을 바꾸었는가

기존 휴머노이드 로봇 평가 체계에는 근본적인 사각지대가 있습니다. 거의 모든 데이터셋과 벤치마크가 운동학적 궤적 재현 정밀도에 초점을 맞추고 외부 상호작용 힘을 암묵적 교란 또는 노이즈로 간주합니다. 이러한 패러다임은 자유 공간 운동 추적에서는 유효할 수 있지만, 전략이 물리적 세계와 지속적으로 접촉해야 하는 실제 시나리오(예: 무거운 물체 밀고 당기기, 협동 운반)에 배치되면 운동학적 오차나 작업 성공률만으로는 힘 작용 하에서 제어 전략의 실제 강건성을 반영할 수 없습니다. ThorArena가 진정으로 바꾼 것은 평가의 "물리적 현실성" 차원입니다. 외력을 억제해야 할 교란으로 취급하지 않고 평가 프로토콜에서 명시적이고 제어 가능하며 재생 가능한 입력 변수로 간주합니다.

이러한 전환의 심층적 의미는 연구자들이 이전에 회피했던 문제를 정면으로 마주하게 한다는 점입니다. 자유 공간 추적에서 우수한 성능을 보이는 전략이 지속적인 외력 하에서는 완전히 실패할 수 있다는 것입니다. ThorArena는 힘 계층화 평가와 강건성 비율 같은 진단 지표를 도입하여 "전략이 어떤 힘 수준에서 성능이 저하되는가"라는 정보를 점수 체계에 명시적으로 포함시킴으로써, 물리적 상호작용 시나리오에서 서로 다른 전략 간의 우열 비교를 정량화하고 재현 가능하게 만듭니다. 이는 본질적으로 평가를 "운동학적 충실도"에서 "힘-운동 결합 강건성" 수준으로 끌어올린 것입니다.

## 방법 분해

### 데이터 수집 및 작업 설계
- 작업자는 PICO 4 Ultra 헤드셋과 신체 추적기를 착용하여 전신 동작을 수집하며, 양손에 각각 힘 센서(3D 프린팅 후크로 고정)를 장착하여 3축 힘 벡터를 동기 기록합니다.
- 6가지 대표적인 힘 상호작용 작업을 설계했습니다: clean_table, liftdown_water, liftup_water, pull_chair, push_chair, syn_carry로, 수직 하중, 수평 추력 및 협동 시나리오를 포괄합니다.

### 힘 인식 평가 지표
- 기본 추적 오차 e_kp(t) = (1/N) Σ ‖x_ref_{k,t} − x_{k,t}‖₂, 참조 키포인트는 각 시간 단계마다 로봇의 현재 루트 자세로 재앵커링되어 전역 루트 드리프트 영향을 제거합니다.
- 총 가해진 손 힘의 33번째 및 66번째 백분위수에 따라 시간 단계를 저/중/고 힘 구간으로 나눕니다.
- 힘 인식 추적 오차 E_i = √(w_low·(E_low)² + w_mid·(E_mid)² + w_high·(E_high)²), 가중치 (w_low, w_mid, w_high) = (0.2, 0.3, 0.5)로 고힘 구간을 강조합니다.
- FATS 점수 S_i = 100·exp(−E_i/σ)·s_i, σ = 0.15 m, s_i = min(T_i/T_ref, 1)는 생존 인자입니다.
- 진단 지표: 강건성 비율 ρ = E_low / E_high, 전력 오버헤드 η = P_high / P_low.

### 평가 프로토콜
- 벤치마크 러너는 기록된 힘을 동기화하여 재생하며, 센서 좌표계의 힘 벡터를 손 로컬 좌표계로 변환한 후 시뮬레이션된 손 자세에 따라 월드 좌표계로 변환하여 적용합니다.
- 힘 계수는 (1)로 설정하면 실측 상호작용 힘을 재현하고, (0)으로 설정하면 외력을 비활성화합니다.
- 결정적 전체 커버리지 스케줄링을 채택하여 모든 시연 시퀀스를 동일한 힘 재생 프로토콜 하에서 각각 한 번씩 평가하며, 여러 병렬 시뮬레이션 환경을 사용합니다.
- 통합 정책 어댑터 인터페이스를 통해 각 정책은 고정된 배포 호환 동역학 구성에서 평가되며, 작업 간에 일관성을 유지합니다.

## 핵심 혁신

1. **힘 인식 평가 지표 도입**: 처음으로 힘 계층화와 가중 오차를 결합하여 33/66 백분위수로 힘 구간을 나누고 고힘 구간에 더 높은 가중치(0.5)를 부여함으로써 평가 결과가 강한 힘 상호작용 하에서 정책의 성능 저하 정도를 직접 반영합니다. 이 설계는 단순한 작업 성공률이나 운동학적 오차보다 물리적 상호작용의 본질적 도전을 더 잘刻画합니다.

2. **외력 재생 프로토콜**: 기록된 실측 상호작용 힘을 재현 가능한 평가 입력으로 사용하고, 힘 계수로 외력 적용 여부를 제어하여 "외력 있음"과 "외력 없음" 두 설정의 대조 평가를 구현합니다. 이 설계는 동일한 힘 조건에서 정책 간 비교를 가능하게 하여 서로 다른 시연 간 힘 차이로 인한 혼동을 제거합니다.

3. **진단 지표와 주요 지표의 분리**: 강건성 비율 ρ와 전력 오버헤드 η는 FATS 공식에 포함되지 않고 독립적인 진단 차원으로 사용됩니다. 이는 단일 지표가 특정 힘 구간에서 정책의 결함을 가리는 것을 방지합니다. 예를 들어 TWIST2의 높은 강건성 비율은 실제로 큰 저힘 기준 오차를 반영하는 것이지 진정한 강한 힘 강건성을 의미하지 않습니다.

## 실험 및 결과

실험에서는 4가지 전신 제어 정책(Thor2, TWIST2, GMT, SONIC)을 6개 하위 작업에서 비교했으며, 각 정책은 외력 있음과 없음 두 설정으로 평가했습니다.

| 지표 | Thor2 | TWIST2 | GMT | SONIC |
|------|-------|--------|-----|-------|
| FATS(외력) | 81.71 | 73.78 | 71.06 | 70.04 |
| Survival | 1.000 | 0.941 | 0.916 | 0.957 |
| Low KP (mm) | 27.8 | 37.5 | 37.8 | 43.9 |
| High KP (mm) | 33.8 | 40.7 | 42.4 | 54.1 |
| Robustness ρ | 0.812 | 0.908 | 0.888 | 0.816 |
| Power η | 1.27 | 1.23 | 1.37 | 1.22 |

핵심 발견:
- Thor2는 전체 6개 하위 작업에서 1위를 차지했으며, 평균 FATS가 가장 높고(81.71) 생존율이 거의 완벽합니다(1.000).
- push_chair는 벤치마크에서 가장 도전적인 작업으로, TWIST2, GMT, SONIC의 생존율이 0.73–0.81로 떨어지며 지속적인 수평 힘이 균형을 직접 위협합니다.
- 외력 없음 설정에서는 모든 정책의 생존율이 1.0에 가깝고, Thor2 FATS는 84.31, 최저 키포인트 오차는 26.1 mm로 성능 차이는 주로 상반신 추적 정밀도에서 발생합니다.

## 경계 및 한계

논문은 데이터셋 규모가 제한적임을 명시적으로 인정합니다. 각 작업당 원시 시연 시퀀스 60개, 총 360개로, 포괄하는 작업 유형과 힘 조건이 상대적으로 제한적입니다. 힘 계층화 임계값(33/66 백분위수)과 FATS 공식의 유효성은 체계적인 실험을 통해 충분히 검증되지 않았습니다. 벤치마크는 현재 시뮬레이션 환경에서만 평가되었으며 물리적 로봇 검증은 수행되지 않아 실제 적용 가능성과 시뮬레이션 결과와의 일관성은 아직 확인이 필요합니다. 또한 평가는 4가지 정책만을 대상으로 하여 더 많은 휴머노이드 로봇 본체와 제어 시스템으로 확장되지 않았습니다.

## 공학적 시사점

ThorArena를 재현하거나 사용할 때 먼저 힘 재생 프로토콜의 정확성을 확인해야 합니다. 센서 좌표계에서 월드 좌표계로의 변환 체인은 논문 설명을 엄격히 따라야 하며, 그렇지 않으면 외력 적용 위치와 방향에 편차가 발생합니다. 둘째, FATS 공식의 σ 매개변수(0.15 m)는 점수 민감도에 큰 영향을 미치므로 다른 로봇 본체에서는 재보정이 필요할 수 있습니다. 가장 함정에 빠지기 쉬운 지점은 힘 계층화 임계값 계산입니다. 각 데이터셋 내 총 가해진 손 힘 분포를 기반으로 33/66 백분위수를 계산해야 하며, 전역 고정 임계값을 사용해서는 안 됩니다. 하류 팀에게는 평가 전에 먼저 외력 없음 설정을 기준선으로 실행하여 정책의 추적 정밀도가 기준에 도달했는지 확인한 후 외력을 도입하여 힘 강건성 요인을 분리할 것을 권장합니다. 진단 지표(ρ 및 η)는 절대 오차와 함께 종합적으로 해석해야 단일 지표에 오도되지 않습니다.
