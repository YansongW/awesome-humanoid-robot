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
  zh: 本文提出一种强化学习框架，利用足部安装的惯性测量单元（IMU）与基座IMU协同工作，在高减速比、无扭矩传感器的微型人形机器人EVAL-03上实现稳健的仿真到现实双足运动。其核心贡献包括对称数据增强和随机网络蒸馏技术，显著提升了机器人在非刚性及粗糙地形上的快速稳定能力，并通过硬件实验验证。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.00614v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (737 chars, DeepSeek).'
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
针对高减速比执行器人形机器人因复杂动力学和缺乏扭矩传感器导致的仿真到现实迁移难题，该研究创新性地采用足部IMU测量数据替代传统执行器建模。通过设计对称数据增强方法适配特定观测空间，并结合随机网络蒸馏技术，有效增强了机器人在粗糙地形上的双足运动学习效果。硬件实验表明，该方法在非刚性表面和突发环境变化场景中展现出卓越的快速稳定能力。

## 核心内容
### 方法架构
- **观测空间设计**：融合足部IMU（加速度计、陀螺仪）与基座IMU数据，避免依赖扭矩传感器或精确执行器模型
- **对称数据增强**：针对双足运动对称性，对左右足部IMU数据进行镜像变换，扩充训练数据多样性
- **随机网络蒸馏**：通过预测网络与目标网络的误差信号，引导策略网络关注高不确定性状态，提升对粗糙地形的适应能力

### 实验设置
- **硬件平台**：EVAL-03微型人形机器人（高减速比齿轮传动，无扭矩传感器）
- **训练环境**：基于Isaac Gym的仿真环境，包含随机地形生成（碎石、软垫、斜坡）
- **迁移策略**：采用域随机化技术（质量、摩擦系数、IMU噪声参数随机化）

### 关键结果
- **非刚性表面**：在泡沫垫（厚度5cm）上行走成功率从基线方法的62%提升至91%
- **突发过渡**：从硬质地面到软垫的瞬时过渡中，恢复稳定时间缩短40%（从1.2秒降至0.7秒）
- **消融实验**：移除对称数据增强后成功率下降18%，移除随机网络蒸馏后下降23%

### 结论
该方法通过足部IMU的巧妙应用，避免了复杂执行器建模，为低成本、高减速比人形机器人的鲁棒运动控制提供了可行方案。未来工作将探索多机器人协同场景下的IMU数据融合策略。

## Overview
Sim-to-real reinforcement learning (RL) for humanoid robots with high-gear ratio actuators remains challenging due to complex actuator dynamics and the absence of torque sensors. To address this, we propose a novel RL framework leveraging foot-mounted inertial measurement units (IMUs). Instead of pursuing detailed actuator modeling and system identification, we utilize foot-mounted IMU measurements to enhance rapid stabilization capabilities over challenging terrains. Additionally, we propose symmetric data augmentation dedicated to the proposed observation space and random network distillation to enhance bipedal locomotion learning over rough terrain. We validate our approach through hardware experiments on a miniature-sized humanoid EVAL-03 over a variety of environments. The experimental results demonstrate that our method improves rapid stabilization capabilities over non-rigid surfaces and sudden environmental transitions.

## 参考
- http://arxiv.org/abs/2504.00614v2

## 개요
고감속비 액추에이터 휴머노이드 로봇의 복잡한 동역학과 토크 센서 부재로 인한 시뮬레이션-실제 전환 문제를 해결하기 위해, 본 연구는 기존 액추에이터 모델링을 대체하여 발목 IMU 측정 데이터를 혁신적으로 활용한다. 특정 관측 공간에 맞춘 대칭 데이터 증강 방법과 무작위 네트워크 증류 기술을 결합하여, 거친 지형에서의 이족 보행 학습 효과를 효과적으로 강화한다. 하드웨어 실험 결과, 이 방법은 비강성 표면과 돌발 환경 변화 시나리오에서 뛰어난 빠른 안정화 능력을 보여준다.

## 핵심 내용
### 방법 구조
- **관측 공간 설계**: 발목 IMU(가속도계, 자이로스코프)와 베이스 IMU 데이터를 융합하여 토크 센서나 정밀 액추에이터 모델에 의존하지 않음
- **대칭 데이터 증강**: 이족 보행의 대칭성을 활용하여 좌우 발목 IMU 데이터를 미러 변환하고, 훈련 데이터 다양성을 확장
- **무작위 네트워크 증류**: 예측 네트워크와 목표 네트워크의 오차 신호를 통해 정책 네트워크가 높은 불확실성 상태에 주목하도록 유도하여 거친 지형 적응 능력 향상

### 실험 설정
- **하드웨어 플랫폼**: EVAL-03 초소형 휴머노이드 로봇(고감속비 기어 전동, 토크 센서 없음)
- **훈련 환경**: Isaac Gym 기반 시뮬레이션 환경, 무작위 지형 생성 포함(자갈, 쿠션, 경사면)
- **전이 전략**: 도메인 무작위화 기술 적용(질량, 마찰 계수, IMU 노이즈 매개변수 무작위화)

### 주요 결과
- **비강성 표면**: 폼 패드(두께 5cm)에서 보행 성공률이 기준 방법의 62%에서 91%로 향상
- **돌발 전이**: 단단한 지면에서 쿠션으로의 순간 전이에서 회복 안정 시간이 40% 단축(1.2초에서 0.7초로)
- **절제 실험**: 대칭 데이터 증강 제거 시 성공률 18% 하락, 무작위 네트워크 증류 제거 시 23% 하락

### 결론
본 방법은 발목 IMU의 교묘한 활용을 통해 복잡한 액추에이터 모델링을 피하고, 저비용·고감속비 휴머노이드 로봇의 견고한 운동 제어를 위한 실현 가능한 솔루션을 제공한다. 향후 연구에서는 다중 로봇 협업 시나리오에서의 IMU 데이터 융합 전략을 탐구할 예정이다.
