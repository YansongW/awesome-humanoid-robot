---
$id: rel_ent_paper_ghansah_hierarchical_reduced_order_mod_2025_evaluates_on_ent_robot_system_unitree_g1
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: evaluates_on
source:
  id: ent_paper_ghansah_hierarchical_reduced_order_mod_2025
  name:
    en: Hierarchical Reduced-Order Model Predictive Control for Robust Locomotion on Humanoid Robots
    zh: 面向人形机器人稳健运动的层级化降阶模型预测控制
    ko: 인간형 로봇의 견고한 보행을 위한 계층적 차수 축소 모델 예측 제어
target:
  id: ent_robot_system_unitree_g1
  name:
    en: Unitree G1 humanoid robot
    ko: ''
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 02_components
description:
  en: Validates the hierarchical MPC framework through simulation and hardware experiments on the Unitree G1 humanoid robot.
  zh: 在Unitree G1人形机器人上通过仿真和硬件实验验证层级化MPC框架。
  ko: Unitree G1 인간형 로봇에서 시뮬레이션 및 하드웨어 실험을 통해 계층적 MPC 프레임워크를 검증한다.
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: 'Proposed by AI extraction. Source citation: Abstract: ''We validate the performance of our approach through simulation
    and hardware experiments on the Unitree G1 humanoid robot.'''
sources:
- id: src_001
  type: paper
  title: Hierarchical Reduced-Order Model Predictive Control for Robust Locomotion on Humanoid Robots
  url: https://arxiv.org/abs/2509.04722
  date: '2025'
  accessed_at: '2026-06-26'
---
