---
$id: ent_paper_hou_robust_fall_recovery_for_armle_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Robust Fall Recovery for Armless Bipedal-Wheeled Robots via Force-Guided Learning
  zh: 基于力引导学习的无臂双轮足机器人鲁棒跌倒恢复
  ko: 힘-유도 학습을 통한 무팔 이족-바퀴 로봇의 강건한 낙상 복귀
summary:
  en: This paper proposes FTSR, a force-guided teacher-student reinforcement-learning framework that formulates height-correlated
    external auxiliary forces as optimizable constraints and uses height-progressive stage-wise rewards to train armless bipedal-wheeled
    robots to recover from falls, with sim-to-real deployment on the JiaRan robot and generalization to a 23-DOF Unitree humanoid.
  zh: 本文提出FTSR框架，将高度相关的外部辅助力构建为可优化约束，并采用高度递进的分阶段奖励训练无臂双轮足机器人实现跌倒恢复，在JiaRan机器人上完成仿真到现实部署，并泛化至23自由度Unitree人形机器人。
  ko: 본 논문은 높이에 연동된 외부 보조력을 최적화 가능한 제약으로 공식화하고 높이 기반 단계적 보상을 사용하여 무팔 이족-바퀴 로봇의 낙상 복귀를 학습하는 FTSR 프레임워크를 제안하며, JiaRan 로봇에 대한
    시뮬레이션-현실 전개 및 23-DOF Unitree 휴머노이드로의 일반화를 보여준다.
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
tags:
- fall_recovery
- reinforcement_learning
- force_guided_learning
- teacher_student_distillation
- constrained_rl
- bipedal_wheeled_robot
- sim_to_real
- jiaran_robot
- unitree_humanoid
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.14270v1.
sources:
- id: src_001
  type: paper
  title: Robust Fall Recovery for Armless Bipedal-Wheeled Robots via Force-Guided Learning
  url: https://arxiv.org/abs/2606.14270
  date: '2026'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Fall recovery is critical for autonomous legged locomotion. Existing methods have demonstrated that some legged robots, such as humanoids and quadrupeds, are capable of fall recovery from diverse postures by utilizing arms or coordinating multi-legs to generate support forces. Without arms or other legs to provide supportive assistance, a bipedal-wheeled robot must rely solely on the actuation of its legs, making recovery particularly difficult. To address this, we introduce FTSR (Force-guided Teacher-student framework with Stage-wise Rewards). The force-guided method constructs an external auxiliary force during simulation training that correlates directly with the robot's real-time height, explicitly formulating this force as an optimizable constraint. Through constrained reinforcement learning, the policy is guided toward reducing force dependency gradually and increasing the body height, developing internal recovery strategies despite having no arms for support. Height-progressive stage-Wise rewards progressively structure posture stabilization during recovery and transition to sustained locomotion, integrated with teacher-student architecture distilling privileged knowledge of force effects and recovery dynamics. After simulation training, the policy is deployed on a physical armless bipedal-wheeled robot and extensively evaluated. Experiments confirm robust and reliable fall recovery under diverse challenging conditions, demonstrating strong environmental adaptability and motion robustness, while maintaining full post-recovery motion capability. The framework also generalizes effectively to a high-DOF humanoid, confirming its practical generalizability. The project page is available at https://2350575870.github.io/force-guided.github.io/

## 核心内容
Fall recovery is critical for autonomous legged locomotion. Existing methods have demonstrated that some legged robots, such as humanoids and quadrupeds, are capable of fall recovery from diverse postures by utilizing arms or coordinating multi-legs to generate support forces. Without arms or other legs to provide supportive assistance, a bipedal-wheeled robot must rely solely on the actuation of its legs, making recovery particularly difficult. To address this, we introduce FTSR (Force-guided Teacher-student framework with Stage-wise Rewards). The force-guided method constructs an external auxiliary force during simulation training that correlates directly with the robot's real-time height, explicitly formulating this force as an optimizable constraint. Through constrained reinforcement learning, the policy is guided toward reducing force dependency gradually and increasing the body height, developing internal recovery strategies despite having no arms for support. Height-progressive stage-Wise rewards progressively structure posture stabilization during recovery and transition to sustained locomotion, integrated with teacher-student architecture distilling privileged knowledge of force effects and recovery dynamics. After simulation training, the policy is deployed on a physical armless bipedal-wheeled robot and extensively evaluated. Experiments confirm robust and reliable fall recovery under diverse challenging conditions, demonstrating strong environmental adaptability and motion robustness, while maintaining full post-recovery motion capability. The framework also generalizes effectively to a high-DOF humanoid, confirming its practical generalizability. The project page is available at https://2350575870.github.io/force-guided.github.io/

## 参考
- http://arxiv.org/abs/2606.14270v1

