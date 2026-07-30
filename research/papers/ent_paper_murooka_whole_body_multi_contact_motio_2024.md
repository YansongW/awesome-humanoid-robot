---
$id: ent_paper_murooka_whole_body_multi_contact_motio_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Whole-body Multi-contact Motion Control for Humanoid Robots Based on Distributed Tactile Sensors
  zh: 基于分布式触觉传感器的人形机器人全身多接触运动控制
  ko: 분산 촉각 센서 기반 휴머노이드 로봇의 전신 다중 접촉 동작 제어
summary:
  en: This paper presents a whole-body multi-contact control method that uses distributed tactile-sensor feedback to stabilize
    contacts on intermediate limb areas such as knees, elbows, forearms, and thighs, validated in simulation and on the RHP
    Kaleido humanoid.
  zh: 本文提出一种基于分布式触觉传感器的全身多接触控制方法，使RHP Kaleido人形机器人能在膝盖、肘部、前臂和大腿等中间肢体区域稳定接触。该方法通过可变形片状触觉传感器测量接触力，并扩展原有末端接触控制器，在仿真和实物实验中验证了抗干扰能力与复杂姿态稳定性。
  ko: 본 논문은 분산 촉각 센서 피드백을 사용하여 무릎, 팔꿈치, 전완부, 대퇴부와 같은 중간 사지 영역의 접촉을 안정화하는 전신 다중 접촉 제어 방법을 제시하고, 시뮬레이션과 RHP Kaleido 휴머노이드에서
    검증하였다.
domains:
- 07_ai_models_algorithms
- 02_components
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- multi_contact_control
- whole_body_control
- tactile_sensing
- distributed_tactile_sensors
- humanoid_motion_control
- centroidal_mpc
- model_predictive_control
- contact_polygon_estimation
- rhp_kaleido
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.19580v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Whole-body Multi-contact Motion Control for Humanoid Robots Based on Distributed Tactile Sensors
  url: https://arxiv.org/abs/2505.19580
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
为使人形机器人在狭窄环境中稳健工作，本文开发了涉及中间肢体区域（如膝盖、肘部）的全身多接触运动控制方法。通过在机器人肢体表面安装可变形片状分布式触觉传感器，在不显著改变外形的前提下测量接触力。研究将原有仅针对末端（手、脚）的多接触控制器扩展至中间区域，并融合力/力矩传感器与触觉传感器进行反馈控制。动力学仿真表明，触觉反馈能有效提升运动对干扰和环境误差的稳定性；实物实验中，RHP Kaleido人形机器人成功演示了前臂支撑前进和坐姿平衡等全身多接触动作。

## 核心内容
### 方法概述
- 核心挑战：人形机器人在狭窄环境中需利用膝盖、肘部、前臂、大腿等中间肢体区域进行多接触运动，而传统方法仅关注手、脚等末端接触。
- 传感器方案：采用可变形片状分布式触觉传感器，覆盖机器人肢体表面，可测量接触力且不显著改变机器人外形。
- 控制器扩展：基于原有末端多接触控制器，新增对中间区域接触的处理逻辑，并引入分布式触觉传感器的反馈信号。

### 实验设置
- 仿真验证：在动力学仿真环境中测试触觉反馈对运动稳定性的影响，重点评估抗干扰能力和环境误差补偿效果。
- 实物验证：使用全尺寸人形机器人RHP Kaleido进行演示，包括：
  - 前臂支撑前进：身体前倾时以前臂接触地面辅助支撑，完成跨步动作。
  - 坐姿平衡：以大腿接触支撑面，保持坐姿稳定。

### 关键结果
- 仿真中，触觉反馈显著提升了多接触运动对随机扰动和地形误差的鲁棒性。
- 实物实验中，RHP Kaleido成功执行了两种典型全身多接触动作，验证了方法的实际可行性。

### 结论
本文提出的分布式触觉传感器反馈控制方法，有效扩展了人形机器人的接触能力至中间肢体区域，为在狭窄环境中的稳健运动提供了可行方案。

## Overview
To enable humanoid robots to work robustly in confined environments, multi-contact motion that makes contacts not only at extremities, such as hands and feet, but also at intermediate areas of the limbs, such as knees and elbows, is essential. We develop a method to realize such whole-body multi-contact motion involving contacts at intermediate areas by a humanoid robot. Deformable sheet-shaped distributed tactile sensors are mounted on the surface of the robot's limbs to measure the contact force without significantly changing the robot body shape. The multi-contact motion controller developed earlier, which is dedicated to contact at extremities, is extended to handle contact at intermediate areas, and the robot motion is stabilized by feedback control using not only force/torque sensors but also distributed tactile sensors. Through verification on dynamics simulations, we show that the developed tactile feedback improves the stability of whole-body multi-contact motion against disturbances and environmental errors. Furthermore, the life-sized humanoid RHP Kaleido demonstrates whole-body multi-contact motions, such as stepping forward while supporting the body with forearm contact and balancing in a sitting posture with thigh contacts.

## 개요
인간형 로봇이 협소한 환경에서도 강건하게 작업할 수 있도록 하기 위해서는 손과 발 같은 말단뿐만 아니라 무릎과 팔꿈치 같은 사지의 중간 부위에서도 접촉을 만드는 다중 접촉 동작이 필수적입니다. 본 연구에서는 인간형 로봇이 중간 부위에서의 접촉을 포함한 전신 다중 접촉 동작을 구현하는 방법을 개발합니다. 로봇 사지 표면에는 변형 가능한 시트 형태의 분포형 촉각 센서를 장착하여 로봇 형상을 크게 변경하지 않고 접촉력을 측정합니다. 기존에 개발된 말단 접촉 전용 다중 접촉 동작 제어기를 중간 부위 접촉을 처리할 수 있도록 확장하고, 힘/토크 센서뿐만 아니라 분포형 촉각 센서를 활용한 피드백 제어를 통해 로봇 동작을 안정화합니다. 동역학 시뮬레이션 검증을 통해 개발된 촉각 피드백이 외란 및 환경 오차에 대한 전신 다중 접촉 동작의 안정성을 향상시킴을 보여줍니다. 또한 실물 크기 인간형 로봇 RHP Kaleido는 팔뚝 접촉으로 몸을 지지하며 앞으로 나아가는 동작과 대퇴부 접촉으로 앉은 자세에서 균형을 유지하는 동작 등 전신 다중 접촉 동작을 시연합니다.

## 핵심 내용
인간형 로봇이 협소한 환경에서도 강건하게 작업할 수 있도록 하기 위해서는 손과 발 같은 말단뿐만 아니라 무릎과 팔꿈치 같은 사지의 중간 부위에서도 접촉을 만드는 다중 접촉 동작이 필수적입니다. 본 연구에서는 인간형 로봇이 중간 부위에서의 접촉을 포함한 전신 다중 접촉 동작을 구현하는 방법을 개발합니다. 로봇 사지 표면에는 변형 가능한 시트 형태의 분포형 촉각 센서를 장착하여 로봇 형상을 크게 변경하지 않고 접촉력을 측정합니다. 기존에 개발된 말단 접촉 전용 다중 접촉 동작 제어기를 중간 부위 접촉을 처리할 수 있도록 확장하고, 힘/토크 센서뿐만 아니라 분포형 촉각 센서를 활용한 피드백 제어를 통해 로봇 동작을 안정화합니다. 동역학 시뮬레이션 검증을 통해 개발된 촉각 피드백이 외란 및 환경 오차에 대한 전신 다중 접촉 동작의 안정성을 향상시킴을 보여줍니다. 또한 실물 크기 인간형 로봇 RHP Kaleido는 팔뚝 접촉으로 몸을 지지하며 앞으로 나아가는 동작과 대퇴부 접촉으로 앉은 자세에서 균형을 유지하는 동작 등 전신 다중 접촉 동작을 시연합니다.

## 参考
- http://arxiv.org/abs/2505.19580v1
