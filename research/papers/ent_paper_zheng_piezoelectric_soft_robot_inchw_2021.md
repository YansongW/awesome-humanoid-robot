---
$id: ent_paper_zheng_piezoelectric_soft_robot_inchw_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Piezoelectric Soft Robot Inchworm Motion by Tuning Ground Friction through Robot Shape: Quasi-Static Modeling and Experimental
    Validation'
  zh: 通过机器人形状调节地面摩擦的压电软体机器人尺蠖运动：准静态建模与实验验证
  ko: '로봇 형상을 통한 지면 마찰 튜닝을 이용한 압전 소프트 로봇 인치웜 운동: 준정적 모델링 및 실험적 검증'
summary:
  en: Zheng et al. present a sub-millimeter-thick soft robot driven by five coordinated piezoelectric actuators on a steel
    foil substrate, using shape-controlled ground friction to achieve bidirectional inchworm crawling, and validate a gravity-inclusive
    Euler-Bernoulli quasi-static model against experiments.
  zh: Zheng 等人展示了一种厚度不足 0.5 毫米的软体机器人，该机器人在钢箔基底上集成五个压电执行器，通过形状控制地面摩擦实现双向尺蠖爬行，并验证了包含重力的欧拉-伯努利准静态模型。
  ko: Zheng 등은 강박 기판 위에 5개의 압전 액추에이터를 조화롭게 구동하는 수백 마이크로미터 두께의 소프트 로봇을 제안하고, 형상에 의한 지면 마찰 제어로 양방향 인치웜 이동을 구현하며 중력을 포함한 Euler-Bernoulli
    준정적 모델을 실험으로 검증하였다.
domains:
- 02_components
- 06_design_engineering
- 03_manufacturing_processes
layers:
- midstream
- upstream
functional_roles:
- knowledge
tags:
- piezoelectric_actuator
- pzt
- soft_robot
- inchworm_locomotion
- friction_tuning
- thin_film
- quasi_static_modeling
- ground_contact_modeling
- steel_foil
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2111.00944v2.
sources:
- id: src_001
  type: paper
  title: 'Piezoelectric Soft Robot Inchworm Motion by Tuning Ground Friction through Robot Shape: Quasi-Static Modeling and
    Experimental Validation'
  url: https://arxiv.org/abs/2111.00944
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Electrically-driven soft robots based on piezoelectric actuators may enable compact form factors and maneuverability in complex environments. In most prior work, piezoelectric actuators are used to control a single degree of freedom. In this work, the coordinated activation of five independent piezoelectric actuators, attached to a common metal foil, is used to implement inchworm-inspired crawling motion in a robot that is less than 0.5 mm thick. The motion is based on the control of its friction to the ground through the robot's shape, in which one end of the robot (depending on its shape) is anchored to the ground by static friction, while the rest of its body expands or contracts. A complete analytical model of the robot shape, which includes gravity, is developed to quantify the robot shape, friction, and displacement. After validation of the model by experiments, the robot's five actuators are collectively sequenced for inchworm-like forward and backward motion.

## 核心内容
Electrically-driven soft robots based on piezoelectric actuators may enable compact form factors and maneuverability in complex environments. In most prior work, piezoelectric actuators are used to control a single degree of freedom. In this work, the coordinated activation of five independent piezoelectric actuators, attached to a common metal foil, is used to implement inchworm-inspired crawling motion in a robot that is less than 0.5 mm thick. The motion is based on the control of its friction to the ground through the robot's shape, in which one end of the robot (depending on its shape) is anchored to the ground by static friction, while the rest of its body expands or contracts. A complete analytical model of the robot shape, which includes gravity, is developed to quantify the robot shape, friction, and displacement. After validation of the model by experiments, the robot's five actuators are collectively sequenced for inchworm-like forward and backward motion.

## 参考
- http://arxiv.org/abs/2111.00944v2

