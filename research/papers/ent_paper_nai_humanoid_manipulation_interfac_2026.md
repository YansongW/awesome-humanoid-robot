---
$id: ent_paper_nai_humanoid_manipulation_interfac_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Humanoid Manipulation Interface (HuMI): Humanoid Whole-Body Manipulation from Robot-Free Demonstrations'
  zh: 人形机器人操作接口（HuMI）：无需机器人演示的全身操作
  ko: '휴머노이드 조작 인터페이스(HuMI): 로봇 없는 시연으로부터의 전신 조작'
summary:
  en: HuMI is a portable, robot-free data-collection and hierarchical-learning framework that translates human whole-body
    manipulation demonstrations into autonomous humanoid skills. Using handheld sensorized grippers and wearable trackers,
    it trains a high-level Diffusion Policy to predict keypoint trajectories and a low-level RL whole-body controller to execute
    them, achieving 3× teleoperation throughput and 70% success in unseen environments on a Unitree G1.
  zh: HuMI 是一个便携式、无需机器人的数据采集与分层学习框架，能将人类全身操作演示转化为自主人形机器人技能。它通过手持传感器夹爪和可穿戴追踪器采集数据，训练高层 Diffusion Policy 预测关键点轨迹，再由低层强化学习全身控制器执行，在
    Unitree G1 上实现 3 倍遥操作吞吐量和 70% 的未见环境成功率。
  ko: HuMI는 휴대용 로봇 불필요 데이터 수집 및 계층적 학습 프레임워크로, 인간의 전신 조작 시연을 자율 휴머노이드 조작 기술로 변환한다. 손에 든 센서화된 그리퍼와 웨어러블 추적기만으로 고차원 확산 정책이 키포인트
    궤적을 예측하고, 저차원 강화학습 전신 제어기가 이를 실행하여 Unitree G1에서 원격조작 대비 3배의 데이터 수집 처리량과 보지 않은 환경에서 70% 성공률을 달성했다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 09_data_datasets
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- humanoid_whole_body_manipulation
- robot_free_demonstration
- diffusion_policy
- whole_body_rl_controller
- adaptive_end_effector_tracking
- variable_speed_augmentation
- loco_manipulation
- bimanual_manipulation
- imitation_learning
- unitree_g1
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.06643v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations'
  url: https://arxiv.org/abs/2602.06643
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
当前人形机器人全身操作主要依赖遥操作或视觉 sim-to-real 强化学习，受限于硬件物流和复杂的奖励工程，导致自主技能有限且仅适用于受控环境。HuMI 通过便携硬件捕获丰富的人类全身运动，无需机器人即可采集数据，并利用分层学习流水线将人类动作转化为灵巧可行的人形技能。在五项全身任务（跪姿、蹲姿、抛掷、行走、双臂操作）的实验中，HuMI 的数据采集效率比遥操作提升 3 倍，在未见环境中达到 70% 的成功率。

## 核心内容
### 方法概述
HuMI 的核心创新在于将数据采集与机器人本体解耦，通过便携硬件（手持传感器夹爪 + 可穿戴追踪器）记录人类演示的全身运动。这些数据驱动一个分层学习流水线：
- **高层策略**：使用 Diffusion Policy 从人类演示中学习预测关键点轨迹（如手部、躯干、脚部位置），作为任务规划层。
- **低层控制器**：基于强化学习的全身控制器，将高层预测的关键点轨迹映射为机器人关节指令，确保动作的物理可行性与稳定性。

### 实验设置
- **机器人平台**：Unitree G1 人形机器人。
- **任务集**：五项全身操作任务，涵盖动态（抛掷）、静态（跪姿、蹲姿）、移动（行走）及双臂协作场景。
- **对比基线**：传统遥操作数据采集方法。
- **评估指标**：数据采集吞吐量（单位时间采集的有效演示数）与未见环境任务成功率。

### 关键结果
- **数据效率**：HuMI 的数据采集吞吐量是遥操作的 3 倍，得益于无需机器人硬件即可并行采集人类演示。
- **泛化能力**：在未见环境（如不同物体位置、地面条件）中，任务成功率达到 70%，显著优于依赖固定场景的基线方法。
- **技能多样性**：成功学习五种不同动力学特性的全身技能，验证了框架对复杂操作任务的通用性。

### 结论
HuMI 通过机器人无关的数据采集与分层学习，解决了人形机器人全身操作中数据稀缺与泛化性差的瓶颈。其便携硬件设计降低了部署门槛，而分层架构平衡了任务规划与运动控制，为真实世界人形机器人技能学习提供了可扩展方案。

## Overview
Current approaches for humanoid whole-body manipulation, primarily relying on teleoperation or visual sim-to-real reinforcement learning, are hindered by hardware logistics and complex reward engineering. Consequently, demonstrated autonomous skills remain limited and are typically restricted to controlled environments. In this paper, we present the Humanoid Manipulation Interface (HuMI), a portable and efficient framework for learning diverse whole-body manipulation tasks across various environments. HuMI enables robot-free data collection by capturing rich whole-body motion using portable hardware. This data drives a hierarchical learning pipeline that translates human motions into dexterous and feasible humanoid skills. Extensive experiments across five whole-body tasks--including kneeling, squatting, tossing, walking, and bimanual manipulation--demonstrate that HuMI achieves a 3x increase in data collection efficiency compared to teleoperation and attains a 70% success rate in unseen environments.

## Overview
Current approaches for humanoid whole-body manipulation, primarily relying on teleoperation or visual sim-to-real reinforcement learning, are hindered by hardware logistics and complex reward engineering. Consequently, demonstrated autonomous skills remain limited and are typically restricted to controlled environments. In this paper, we present the Humanoid Manipulation Interface (HuMI), a portable and efficient framework for learning diverse whole-body manipulation tasks across various environments. HuMI enables robot-free data collection by capturing rich whole-body motion using portable hardware. This data drives a hierarchical learning pipeline that translates human motions into dexterous and feasible humanoid skills. Extensive experiments across five whole-body tasks—including kneeling, squatting, tossing, walking, and bimanual manipulation—demonstrate that HuMI achieves a 3x increase in data collection efficiency compared to teleoperation and attains a 70% success rate in unseen environments.

## Content
Current approaches for humanoid whole-body manipulation, primarily relying on teleoperation or visual sim-to-real reinforcement learning, are hindered by hardware logistics and complex reward engineering. Consequently, demonstrated autonomous skills remain limited and are typically restricted to controlled environments. In this paper, we present the Humanoid Manipulation Interface (HuMI), a portable and efficient framework for learning diverse whole-body manipulation tasks across various environments. HuMI enables robot-free data collection by capturing rich whole-body motion using portable hardware. This data drives a hierarchical learning pipeline that translates human motions into dexterous and feasible humanoid skills. Extensive experiments across five whole-body tasks—including kneeling, squatting, tossing, walking, and bimanual manipulation—demonstrate that HuMI achieves a 3x increase in data collection efficiency compared to teleoperation and attains a 70% success rate in unseen environments.

## 개요
휴머노이드 전신 조작을 위한 현재 접근 방식은 주로 원격 조작 또는 시각적 시뮬레이션-실제 강화 학습에 의존하며, 하드웨어 물류 및 복잡한 보상 엔지니어링으로 인해 제약을 받습니다. 결과적으로 입증된 자율 기술은 여전히 제한적이며 일반적으로 통제된 환경으로 한정됩니다. 본 논문에서는 다양한 환경에서 다양한 전신 조작 작업을 학습하기 위한 휴대용 및 효율적인 프레임워크인 HuMI(Humanoid Manipulation Interface)를 제시합니다. HuMI는 휴대용 하드웨어를 사용하여 풍부한 전신 움직임을 캡처함으로써 로봇 없이 데이터 수집을 가능하게 합니다. 이 데이터는 인간의 움직임을 능숙하고 실행 가능한 휴머노이드 기술로 변환하는 계층적 학습 파이프라인을 구동합니다. 무릎 꿇기, 쪼그려 앉기, 던지기, 걷기, 양손 조작을 포함한 다섯 가지 전신 작업에 걸친 광범위한 실험을 통해 HuMI는 원격 조작 대비 데이터 수집 효율성이 3배 향상되고, 보지 못한 환경에서 70%의 성공률을 달성함을 입증합니다.

## 핵심 내용
휴머노이드 전신 조작을 위한 현재 접근 방식은 주로 원격 조작 또는 시각적 시뮬레이션-실제 강화 학습에 의존하며, 하드웨어 물류 및 복잡한 보상 엔지니어링으로 인해 제약을 받습니다. 결과적으로 입증된 자율 기술은 여전히 제한적이며 일반적으로 통제된 환경으로 한정됩니다. 본 논문에서는 다양한 환경에서 다양한 전신 조작 작업을 학습하기 위한 휴대용 및 효율적인 프레임워크인 HuMI(Humanoid Manipulation Interface)를 제시합니다. HuMI는 휴대용 하드웨어를 사용하여 풍부한 전신 움직임을 캡처함으로써 로봇 없이 데이터 수집을 가능하게 합니다. 이 데이터는 인간의 움직임을 능숙하고 실행 가능한 휴머노이드 기술로 변환하는 계층적 학습 파이프라인을 구동합니다. 무릎 꿇기, 쪼그려 앉기, 던지기, 걷기, 양손 조작을 포함한 다섯 가지 전신 작업에 걸친 광범위한 실험을 통해 HuMI는 원격 조작 대비 데이터 수집 효율성이 3배 향상되고, 보지 못한 환경에서 70%의 성공률을 달성함을 입증합니다.

## 参考
- http://arxiv.org/abs/2602.06643v2
