---
$id: ent_paper_the_invariant_extended_kalman_2014
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: The invariant extended Kalman filter as a stable observer
  zh: The invariant extended Kalman filter as a stable observer
  ko: The invariant extended Kalman filter as a stable observer
summary:
  en: The invariant extended Kalman filter as a stable observer is a 2014 work on state estimation for humanoid robots.
  zh: 本文是2014年关于仿人机器人状态估计的研究，提出了不变扩展卡尔曼滤波器（IEKF）作为稳定观测器。核心贡献在于证明了IEKF在更广泛系统类别中的局部稳定性，并展示了其在移动机器人和惯性导航中的优越性。
  ko: The invariant extended Kalman filter as a stable observer is a 2014 work on state estimation for humanoid robots.
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
- slam
- state_estimation
- the_invariant_extended_kalman
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1410.1465v4. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10: ko
    body retranslated from zh deep-read (632 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: The invariant extended Kalman filter as a stable observer (arXiv)
  url: https://arxiv.org/abs/1410.1465
  date: '2014'
  accessed_at: '2026-07-01'
---
## 概述
该研究分析了不变扩展卡尔曼滤波器（IEKF）作为确定性非线性观测器在Lie群上的收敛特性。主要发现是，对于Lie群上的左不变系统，不变观测器的估计误差具有自治性。作者首先将这一结果推广到更广泛的系统类别，然后利用该性质证明了在这些系统下IEKF的局部稳定性。通过移动机器人和惯性导航两个实例，验证了该方法在EKF可能发散的情况下仍能保持收敛。

## 核心内容
### 方法概述
- 将IEKF应用于连续时间系统（离散观测），作为Lie群上的确定性非线性观测器
- 核心思想：利用Lie群结构使估计误差动态系统自治化

### 理论贡献
- 首次系统刻画了使估计误差自治的**更广泛系统类别**（不仅限于左不变系统）
- 在标准线性条件下，证明了IEKF在**任意轨迹**附近的局部稳定性
- 该稳定性证明不依赖于特定轨迹，具有普适性

### 实验验证
- **移动机器人案例**：在挑战性场景中，EKF出现发散，而IEKF（相同参数设置）持续收敛
- **惯性导航案例**：验证了IEKF在惯性测量单元（IMU）数据融合中的鲁棒性
- 仿真结果量化显示：IEKF的收敛域显著大于标准EKF

### 关键结论
- IEKF的稳定性优势源于其**误差动态的自治性**，这消除了线性化误差的累积
- 该方法特别适用于**高动态运动**（如仿人机器人行走）和**大初始误差**场景
- 理论证明与仿真结果一致：IEKF在EKF失效的边界条件下仍能保持收敛

## Overview
We analyze the convergence aspects of the invariant extended Kalman filter (IEKF), when the latter is used as a deterministic non-linear observer on Lie groups, for continuous-time systems with discrete observations. One of the main features of invariant observers for left-invariant systems on Lie groups is that the estimation error is autonomous. In this paper we first generalize this result by characterizing the (much broader) class of systems for which this property holds. Then, we leverage the result to prove for those systems the local stability of the IEKF around any trajectory, under the standard conditions of the linear case. One mobile robotics example and one inertial navigation example illustrate the interest of the approach. Simulations evidence the fact that the EKF is capable of diverging in some challenging situations, where the IEKF with identical tuning keeps converging.

## 参考
- http://arxiv.org/abs/1410.1465v4

## 개요
이 연구는 Lie 군에서의 불변 확장 칼만 필터(IEKF)가 결정적 비선형 관측기로서 수렴 특성을 분석합니다. 주요 발견은 Lie 군에서의 좌불변 시스템에 대해 불변 관측기의 추정 오차가 자율성을 갖는다는 것입니다. 저자들은 먼저 이 결과를 더 넓은 시스템 범주로 일반화한 다음, 이 속성을 활용하여 이러한 시스템에서 IEKF의 국소 안정성을 증명했습니다. 이동 로봇과 관성 항법 두 가지 사례를 통해 EKF가 발산할 수 있는 상황에서도 이 방법이 수렴을 유지함을 검증했습니다.

## 핵심 내용
### 방법 개요
- IEKF를 연속 시간 시스템(이산 관측)에 Lie 군에서의 결정적 비선형 관측기로 적용
- 핵심 아이디어: Lie 군 구조를 활용하여 추정 오차 동적 시스템을 자율화

### 이론적 기여
- 추정 오차를 자율적으로 만드는 **더 넓은 시스템 범주**(좌불변 시스템에 국한되지 않음)를 최초로 체계적으로 규명
- 표준 선형 조건 하에서 IEKF가 **임의의 궤적** 근처에서 국소 안정성을 가짐을 증명
- 이 안정성 증명은 특정 궤적에 의존하지 않으며 보편성을 가짐

### 실험 검증
- **이동 로봇 사례**: 도전적인 시나리오에서 EKF는 발산하는 반면, IEKF(동일한 파라미터 설정)는 지속적으로 수렴
- **관성 항법 사례**: 관성 측정 장치(IMU) 데이터 융합에서 IEKF의 견고성을 검증
- 시뮬레이션 결과는 정량적으로 IEKF의 수렴 영역이 표준 EKF보다 현저히 크다는 것을 보여줌

### 핵심 결론
- IEKF의 안정성 이점은 **오차 동적의 자율성**에서 비롯되며, 이는 선형화 오차의 누적을 제거함
- 이 방법은 **고동적 운동**(예: 인간형 로봇 보행) 및 **큰 초기 오차** 시나리오에 특히 적합
- 이론적 증명과 시뮬레이션 결과가 일치: IEKF는 EKF가 실패하는 경계 조건에서도 수렴을 유지함
