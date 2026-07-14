---
$id: ent_paper_yousefi_koma_surena_iv_towards_a_cost_effec_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SURENA IV: Towards A Cost-effective Full-size Humanoid Robot for Real-world Scenarios'
  zh: SURENA IV：面向真实场景的成本效益型全尺寸人形机器人
  ko: 'SURENA IV: 실제 환경을 위한 비용 효율적인 풀사이즈 휴머노이드 로봇'
summary:
  en: SURENA IV is a 43-DoF, 170 cm, 68 kg anthropomorphic humanoid developed at the University of Tehran using low-cost manufacturing;
    it uses a predictive foot sensor and online swing-foot adaptation to walk on bounded uneven terrain without force/torque
    sensors, and current-feedback hand control for manipulation tasks.
  zh: SURENA IV 是德黑兰大学开发的 43 自由度、170 cm、68 kg 拟人化人形机器人，采用低成本制造；它利用预测式足底传感器和在线摆动足自适应控制，在没有力/力矩传感器的情况下在有限不平坦地形行走，并通过电流反馈手部控制完成操作任务。
  ko: SURENA IV는 테헤란 대학에서 저비용 제조 방식으로 개발된 43자유도, 170 cm, 68 kg 의 인간형 휴머노이드 로봇으로, 예측형 발 센서와 온라인 스윙 발 적응 제어를 통해 힘/토크 센서 없이 제한된
    불규칙 지면을 보행하고 전류 피드백 손 제어로 조작 작업을 수행한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2108.13515v1.
sources:
- id: src_001
  type: paper
  title: 'SURENA IV: Towards A Cost-effective Full-size Humanoid Robot for Real-world Scenarios'
  url: https://arxiv.org/abs/2108.13515
  date: '2021'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
This paper describes the hardware, software framework, and experimental testing of SURENA IV humanoid robotics platform. SURENA IV has 43 degrees of freedom (DoFs), including seven DoFs for each arm, six DoFs for each hand, and six DoFs for each leg, with a height of 170 cm and a mass of 68 kg and morphological and mass properties similar to an average adult human. SURENA IV aims to realize a cost-effective and anthropomorphic humanoid robot for real-world scenarios. In this way, we demonstrate a locomotion framework based on a novel and inexpensive predictive foot sensor that enables walking with 7cm foot position error because of accumulative error of links and connections' deflection(that has been manufactured by the tools which are available in the Universities). Thanks to this sensor, the robot can walk on unknown obstacles without any force feedback, by online adaptation of foot height and orientation. Moreover, the arm and hand of the robot have been designed to grasp the objects with different stiffness and geometries that enable the robot to do drilling, visual servoing of a moving object, and writing his name on the white-board.

## 核心内容
This paper describes the hardware, software framework, and experimental testing of SURENA IV humanoid robotics platform. SURENA IV has 43 degrees of freedom (DoFs), including seven DoFs for each arm, six DoFs for each hand, and six DoFs for each leg, with a height of 170 cm and a mass of 68 kg and morphological and mass properties similar to an average adult human. SURENA IV aims to realize a cost-effective and anthropomorphic humanoid robot for real-world scenarios. In this way, we demonstrate a locomotion framework based on a novel and inexpensive predictive foot sensor that enables walking with 7cm foot position error because of accumulative error of links and connections' deflection(that has been manufactured by the tools which are available in the Universities). Thanks to this sensor, the robot can walk on unknown obstacles without any force feedback, by online adaptation of foot height and orientation. Moreover, the arm and hand of the robot have been designed to grasp the objects with different stiffness and geometries that enable the robot to do drilling, visual servoing of a moving object, and writing his name on the white-board.

## 参考
- http://arxiv.org/abs/2108.13515v1

