---
$id: ent_paper_yousefi_koma_surena_iv_towards_a_cost_effec_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SURENA IV: Towards A Cost-effective Full-size Humanoid Robot for Real-world
    Scenarios'
  zh: SURENA IV：面向真实场景的成本效益型全尺寸人形机器人
  ko: 'SURENA IV: 실제 환경을 위한 비용 효율적인 풀사이즈 휴머노이드 로봇'
summary:
  en: SURENA IV is a 43-DoF, 170 cm, 68 kg anthropomorphic humanoid developed at the
    University of Tehran using low-cost manufacturing; it uses a predictive foot sensor
    and online swing-foot adaptation to walk on bounded uneven terrain without force/torque
    sensors, and current-feedback hand control for manipulation tasks.
  zh: SURENA IV 是德黑兰大学开发的 43 自由度、170 cm、68 kg 拟人化人形机器人，采用低成本制造；它利用预测式足底传感器和在线摆动足自适应控制，在没有力/力矩传感器的情况下在有限不平坦地形行走，并通过电流反馈手部控制完成操作任务。
  ko: SURENA IV는 테헤란 대학에서 저비용 제조 방식으로 개발된 43자유도, 170 cm, 68 kg 의 인간형 휴머노이드 로봇으로, 예측형
    발 센서와 온라인 스윙 발 적응 제어를 통해 힘/토크 센서 없이 제한된 불규칙 지면을 보행하고 전류 피드백 손 제어로 조작 작업을 수행한다.
domains:
- 05_mass_production
- 06_design_engineering
- 03_manufacturing_processes
- 02_components
layers:
- midstream
- upstream
functional_roles:
- knowledge
- system
- intelligence
tags:
- surena_iv
- full_size_humanoid
- cost_effective_humanoid
- predictive_foot_sensor
- swing_foot_adaptation
- bipedal_locomotion
- anthropomorphic_hand
- current_feedback_grasping
- encoder_based_sensing
- university_manufacturing
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from arXiv full text; hardware specifications, method equations,
    and cited robots/companies are directly traceable to the paper, but total unit
    cost and some component model details are not explicitly stated.
sources:
- id: src_001
  type: paper
  title: 'SURENA IV: Towards A Cost-effective Full-size Humanoid Robot for Real-world
    Scenarios'
  url: https://arxiv.org/abs/2108.13515
  date: '2021'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---

## Overview

SURENA IV is a full-size, 43-DoF humanoid robot developed at the University of Tehran's Center of Advanced Systems and Technologies (CAST). It stands 170 cm tall, weighs 68 kg, and is intended to be a cost-effective, anthropomorphic platform for real-world tasks. The mechanical design uses magnesium alloy AZ91 for the leg structures, aluminum alloy and carbon-fiber composite for the arms, and custom compact actuator modules built around BLDC brushless motors and Harmonic-Drive gears with incremental and absolute encoders. The electronics architecture combines an Intel Core i7 main computer with an NVIDIA GTX 1060 GPU and a Xilinx Zynq-7020 FPGA board that communicates with motor drivers over CAN at a 200 Hz control loop, together with an IMU and a RealSense camera.

The locomotion system is built around a predictive foot sensor and online swing-foot adaptation to compensate for large foot-trajectory errors caused by link deflections and joint clearances in low-cost manufacturing. Four rotary contact sensors on each foot, each connected to an encoder, report the distance of the foot corners to the ground up to about 1.5 cm before contact. A cumulative controller adjusts ankle pitch and roll trajectories and replans the swing-foot height polynomial when the sensor detects an earlier-than-expected ground approach, thereby avoiding severe collisions and enabling autonomous walking over 1 cm obstacles and 3° slopes without force/torque sensors. For manipulation, the 6-DoF anthropomorphic hands use current feedback from PQ12 linear finger actuators to grasp objects of varying stiffness and geometry, supporting tasks such as drilling, visual servoing of a moving bottle, and writing on a whiteboard.

## Key Contributions

- Design of SURENA IV, a 43-DoF, 170 cm, 68 kg anthropomorphic humanoid robot built with low-cost manufacturing.
- A novel inexpensive predictive foot sensor using rotary encoders to estimate ground distance before contact.
- Online swing-foot height and orientation adaptation enabling walking despite approximately 7 cm foot-position error from link deflections and joint clearances.
- Autonomous walking over bounded uneven terrain (1 cm obstacles, 3° slopes) without force/torque feedback.
- Anthropomorphic hand and arm design using current feedback to grasp objects of varying stiffness and geometry.

## Relevance to Humanoid Robotics

The paper directly addresses the cost barrier that limits mass production and widespread deployment of humanoid robots. By demonstrating that a full-size humanoid built with university-level manufacturing can locomote and manipulate without expensive force/torque sensors, it provides a design and control reference for low-cost, real-world humanoid systems. The predictive foot-sensing and adaptive-control ideas are transferable to other platforms that must tolerate mechanical imperfections while retaining safe and robust locomotion.
