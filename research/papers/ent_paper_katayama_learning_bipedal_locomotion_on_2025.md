---
$id: ent_paper_katayama_learning_bipedal_locomotion_on_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Bipedal Locomotion on Gear-Driven Humanoid Robot Using Foot-Mounted IMUs
  zh: 使用足部惯性测量单元在齿轮驱动人形机器人上学习双足行走
  ko: 발에 장착된 IMU를 활용한 기어 구동 인간형 로봇의 이족 보행 학습
summary:
  en: This paper proposes a reinforcement learning framework that uses foot-mounted inertial measurement units (IMUs) together
    with a base-mounted IMU to achieve robust sim-to-real bipedal locomotion on a high-gear-ratio, torque-sensorless miniature
    humanoid robot (EVAL-03). It introduces symmetric data augmentation and random network distillation to improve rapid stabilization
    over rough and non-rigid terrains, validated through hardware experiments.
  zh: 该论文提出了一种强化学习框架，通过足部惯性测量单元（IMU）与躯干IMU相结合，在采用高减速比执行器且无扭矩传感器的微型人形机器人EVAL-03上实现稳健的仿真到现实双足行走。论文引入了针对观测空间的对称数据增强和随机网络蒸馏技术，以提升在粗糙和非刚性地形上的快速稳定能力，并通过硬件实验进行了验证。
  ko: 본 논문은 발에 장착된 관성 측정 장치(IMU)와 기반 IMU를 함께 사용하여 고감속비 액추에이터와 토크 센서가 없는 소형 인간형 로봇 EVAL-03에서 시뮬레이션에서 현실로 이어지는 견고한 이족 보행을 달성하는
    강화학습 프레임워크를 제안한다. 거친 지형과 비강성 지형에서의 급격한 안정화 능력을 향상시키기 위해 대칭 데이터 증강과 랜덤 네트워크 증류를 도입하고 하드웨어 실험으로 검증하였다.
domains:
- 07_ai_models_algorithms
- 02_components
- 05_mass_production
- 11_applications_markets
layers:
- intelligence
- midstream
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
- system
tags:
- sim_to_real
- reinforcement_learning
- bipedal_locomotion
- foot_mounted_imu
- gear_driven_humanoid
- torque_sensorless
- blind_locomotion
- eval_03
- miniature_humanoid
- ppo
- isaac_gym
- legged_gym
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.00614v2.
sources:
- id: src_001
  type: paper
  title: Learning Bipedal Locomotion on Gear-Driven Humanoid Robot Using Foot-Mounted IMUs
  url: https://arxiv.org/abs/2504.00614
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Sim-to-real reinforcement learning (RL) for humanoid robots with high-gear ratio actuators remains challenging due to complex actuator dynamics and the absence of torque sensors. To address this, we propose a novel RL framework leveraging foot-mounted inertial measurement units (IMUs). Instead of pursuing detailed actuator modeling and system identification, we utilize foot-mounted IMU measurements to enhance rapid stabilization capabilities over challenging terrains. Additionally, we propose symmetric data augmentation dedicated to the proposed observation space and random network distillation to enhance bipedal locomotion learning over rough terrain. We validate our approach through hardware experiments on a miniature-sized humanoid EVAL-03 over a variety of environments. The experimental results demonstrate that our method improves rapid stabilization capabilities over non-rigid surfaces and sudden environmental transitions.

## 核心内容
Sim-to-real reinforcement learning (RL) for humanoid robots with high-gear ratio actuators remains challenging due to complex actuator dynamics and the absence of torque sensors. To address this, we propose a novel RL framework leveraging foot-mounted inertial measurement units (IMUs). Instead of pursuing detailed actuator modeling and system identification, we utilize foot-mounted IMU measurements to enhance rapid stabilization capabilities over challenging terrains. Additionally, we propose symmetric data augmentation dedicated to the proposed observation space and random network distillation to enhance bipedal locomotion learning over rough terrain. We validate our approach through hardware experiments on a miniature-sized humanoid EVAL-03 over a variety of environments. The experimental results demonstrate that our method improves rapid stabilization capabilities over non-rigid surfaces and sudden environmental transitions.

## 参考
- http://arxiv.org/abs/2504.00614v2

