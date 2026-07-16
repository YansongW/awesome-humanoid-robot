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

## Overview
Fall recovery is critical for autonomous legged locomotion. Existing methods have demonstrated that some legged robots, such as humanoids and quadrupeds, are capable of fall recovery from diverse postures by utilizing arms or coordinating multi-legs to generate support forces. Without arms or other legs to provide supportive assistance, a bipedal-wheeled robot must rely solely on the actuation of its legs, making recovery particularly difficult. To address this, we introduce FTSR (Force-guided Teacher-student framework with Stage-wise Rewards). The force-guided method constructs an external auxiliary force during simulation training that correlates directly with the robot's real-time height, explicitly formulating this force as an optimizable constraint. Through constrained reinforcement learning, the policy is guided toward reducing force dependency gradually and increasing the body height, developing internal recovery strategies despite having no arms for support. Height-progressive stage-Wise rewards progressively structure posture stabilization during recovery and transition to sustained locomotion, integrated with teacher-student architecture distilling privileged knowledge of force effects and recovery dynamics. After simulation training, the policy is deployed on a physical armless bipedal-wheeled robot and extensively evaluated. Experiments confirm robust and reliable fall recovery under diverse challenging conditions, demonstrating strong environmental adaptability and motion robustness, while maintaining full post-recovery motion capability. The framework also generalizes effectively to a high-DOF humanoid, confirming its practical generalizability. The project page is available at https://2350575870.github.io/force-guided.github.io/

## Content
Fall recovery is critical for autonomous legged locomotion. Existing methods have demonstrated that some legged robots, such as humanoids and quadrupeds, are capable of fall recovery from diverse postures by utilizing arms or coordinating multi-legs to generate support forces. Without arms or other legs to provide supportive assistance, a bipedal-wheeled robot must rely solely on the actuation of its legs, making recovery particularly difficult. To address this, we introduce FTSR (Force-guided Teacher-student framework with Stage-wise Rewards). The force-guided method constructs an external auxiliary force during simulation training that correlates directly with the robot's real-time height, explicitly formulating this force as an optimizable constraint. Through constrained reinforcement learning, the policy is guided toward reducing force dependency gradually and increasing the body height, developing internal recovery strategies despite having no arms for support. Height-progressive stage-Wise rewards progressively structure posture stabilization during recovery and transition to sustained locomotion, integrated with teacher-student architecture distilling privileged knowledge of force effects and recovery dynamics. After simulation training, the policy is deployed on a physical armless bipedal-wheeled robot and extensively evaluated. Experiments confirm robust and reliable fall recovery under diverse challenging conditions, demonstrating strong environmental adaptability and motion robustness, while maintaining full post-recovery motion capability. The framework also generalizes effectively to a high-DOF humanoid, confirming its practical generalizability. The project page is available at https://2350575870.github.io/force-guided.github.io/

## 개요
낙하 회복은 자율 보행 로봇에 있어 매우 중요합니다. 기존 방법들은 휴머노이드나 사족 보행 로봇과 같은 일부 보행 로봇이 팔을 사용하거나 다리를 협력하여 지지력을 생성함으로써 다양한 자세에서 낙하 회복이 가능함을 입증했습니다. 그러나 팔이나 다른 다리의 지지 도움 없이 이족 바퀴 로봇은 오직 다리의 구동에만 의존해야 하므로 회복이 특히 어렵습니다. 이를 해결하기 위해 우리는 FTSR(Force-guided Teacher-student framework with Stage-wise Rewards)을 소개합니다. 힘 유도 방법은 시뮬레이션 훈련 중 로봇의 실시간 높이와 직접적으로 상관관계가 있는 외부 보조 힘을 구성하고, 이 힘을 최적화 가능한 제약 조건으로 명시적으로 공식화합니다. 제약 조건 강화 학습을 통해 정책은 점진적으로 힘 의존성을 줄이고 몸체 높이를 높이도록 유도되어, 지지할 팔이 없음에도 불구하고 내부 회복 전략을 개발합니다. 높이 점진적 단계별 보상은 회복 중 자세 안정화와 지속적인 보행으로의 전환을 점진적으로 구조화하며, 교사-학생 아키텍처와 통합되어 힘 효과 및 회복 역학에 대한 특권 지식을 증류합니다. 시뮬레이션 훈련 후, 정책은 실제 팔이 없는 이족 바퀴 로봇에 배포되어 광범위하게 평가됩니다. 실험 결과, 다양한 까다로운 조건에서 강건하고 신뢰할 수 있는 낙하 회복이 확인되었으며, 강한 환경 적응성과 운동 강건성을 보여주고 회복 후 완전한 운동 능력을 유지합니다. 이 프레임워크는 높은 자유도를 가진 휴머노이드에도 효과적으로 일반화되어 실용적인 일반화 가능성을 입증합니다. 프로젝트 페이지는 https://2350575870.github.io/force-guided.github.io/ 에서 확인할 수 있습니다.

## 핵심 내용
낙하 회복은 자율 보행 로봇에 있어 매우 중요합니다. 기존 방법들은 휴머노이드나 사족 보행 로봇과 같은 일부 보행 로봇이 팔을 사용하거나 다리를 협력하여 지지력을 생성함으로써 다양한 자세에서 낙하 회복이 가능함을 입증했습니다. 그러나 팔이나 다른 다리의 지지 도움 없이 이족 바퀴 로봇은 오직 다리의 구동에만 의존해야 하므로 회복이 특히 어렵습니다. 이를 해결하기 위해 우리는 FTSR(Force-guided Teacher-student framework with Stage-wise Rewards)을 소개합니다. 힘 유도 방법은 시뮬레이션 훈련 중 로봇의 실시간 높이와 직접적으로 상관관계가 있는 외부 보조 힘을 구성하고, 이 힘을 최적화 가능한 제약 조건으로 명시적으로 공식화합니다. 제약 조건 강화 학습을 통해 정책은 점진적으로 힘 의존성을 줄이고 몸체 높이를 높이도록 유도되어, 지지할 팔이 없음에도 불구하고 내부 회복 전략을 개발합니다. 높이 점진적 단계별 보상은 회복 중 자세 안정화와 지속적인 보행으로의 전환을 점진적으로 구조화하며, 교사-학생 아키텍처와 통합되어 힘 효과 및 회복 역학에 대한 특권 지식을 증류합니다. 시뮬레이션 훈련 후, 정책은 실제 팔이 없는 이족 바퀴 로봇에 배포되어 광범위하게 평가됩니다. 실험 결과, 다양한 까다로운 조건에서 강건하고 신뢰할 수 있는 낙하 회복이 확인되었으며, 강한 환경 적응성과 운동 강건성을 보여주고 회복 후 완전한 운동 능력을 유지합니다. 이 프레임워크는 높은 자유도를 가진 휴머노이드에도 효과적으로 일반화되어 실용적인 일반화 가능성을 입증합니다. 프로젝트 페이지는 https://2350575870.github.io/force-guided.github.io/ 에서 확인할 수 있습니다.
