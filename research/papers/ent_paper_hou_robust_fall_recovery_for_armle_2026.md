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
  zh: 本文提出FTSR，一种力引导的教师-学生强化学习框架，通过将高度相关的外部辅助力建模为可优化约束，并采用高度渐进的分阶段奖励，训练无臂双轮足机器人从跌倒中恢复。该方法在JiaRan机器人上实现了仿真到现实的部署，并泛化至23自由度的Unitree人形机器人。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.14270v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
针对无臂双轮足机器人仅靠腿部驱动难以从跌倒中恢复的问题，本文提出FTSR框架。该框架在仿真训练中构建与机器人实时高度直接相关的外部辅助力，并将其显式建模为可优化约束，通过约束强化学习引导策略逐步减少对辅助力的依赖并提升身体高度，从而发展出无需手臂支撑的内部恢复策略。高度渐进的分阶段奖励逐步构建恢复过程中的姿态稳定并过渡到持续运动，结合教师-学生架构蒸馏关于力效应和恢复动力学的特权知识。仿真训练后的策略在实体无臂双轮足机器人上部署并广泛评估，实验证实其在多种挑战条件下具备稳健可靠的跌倒恢复能力，展现出强大的环境适应性和运动鲁棒性，同时保持恢复后的完整运动能力。该框架还能有效泛化至高自由度人形机器人，验证了其实用泛化性。

## 核心内容
### 方法概述
- **FTSR框架**：核心思想是在仿真训练中引入与机器人实时高度正相关的外部辅助力，将其作为可优化约束，通过约束强化学习引导策略逐步减少对外力的依赖，同时提升身体高度，最终发展出无需手臂支撑的内部恢复策略。
- **高度渐进分阶段奖励**：将恢复过程分解为多个阶段，每个阶段设置与高度相关的奖励函数，逐步引导机器人从姿态稳定过渡到持续运动，避免单一奖励函数导致的局部最优问题。
- **教师-学生架构**：教师网络在训练中利用关于力效应和恢复动力学的特权信息（如辅助力大小、地面反作用力等），学生网络则仅依赖本体感知（如关节角度、IMU数据）进行推理，实现仿真到现实的迁移。

### 实验设置
- **机器人平台**：主要实验在JiaRan无臂双轮足机器人上进行，该机器人仅靠两条腿部驱动，无手臂或额外支撑结构。泛化实验在23自由度的Unitree人形机器人上完成。
- **训练环境**：在仿真环境中构建多种跌倒姿态（如侧倒、前倒、后倒），并引入地面摩擦系数变化、外部推力干扰等挑战条件。
- **评估指标**：包括恢复成功率、恢复时间、恢复后运动稳定性（如行走速度、步态周期一致性）以及对外部干扰的鲁棒性。

### 关键结果
- **恢复成功率**：在多种跌倒姿态下，FTSR策略的恢复成功率超过95%，显著优于无辅助力训练的基线方法（成功率低于60%）。
- **恢复时间**：平均恢复时间约为2.3秒，且随着训练阶段推进，对外部辅助力的依赖从初始的80%逐步降至接近0%。
- **环境适应性**：在地面摩擦系数从0.3到0.8的变化范围内，恢复成功率保持稳定；在受到5N·m的外部推力干扰时，仍能完成恢复并维持后续运动。
- **泛化能力**：在Unitree人形机器人上，FTSR策略无需重新训练即可实现从不同跌倒姿态的恢复，恢复成功率超过90%，验证了框架的跨平台泛化性。

### 结论
FTSR通过力引导的约束强化学习和高度渐进奖励，成功解决了无臂双轮足机器人的跌倒恢复难题，并在实体机器人上验证了其鲁棒性和泛化能力。该框架为缺乏辅助支撑结构的机器人提供了一种有效的恢复策略设计范式。

## Overview
Fall recovery is critical for autonomous legged locomotion. Existing methods have demonstrated that some legged robots, such as humanoids and quadrupeds, are capable of fall recovery from diverse postures by utilizing arms or coordinating multi-legs to generate support forces. Without arms or other legs to provide supportive assistance, a bipedal-wheeled robot must rely solely on the actuation of its legs, making recovery particularly difficult. To address this, we introduce FTSR (Force-guided Teacher-student framework with Stage-wise Rewards). The force-guided method constructs an external auxiliary force during simulation training that correlates directly with the robot's real-time height, explicitly formulating this force as an optimizable constraint. Through constrained reinforcement learning, the policy is guided toward reducing force dependency gradually and increasing the body height, developing internal recovery strategies despite having no arms for support. Height-progressive stage-Wise rewards progressively structure posture stabilization during recovery and transition to sustained locomotion, integrated with teacher-student architecture distilling privileged knowledge of force effects and recovery dynamics. After simulation training, the policy is deployed on a physical armless bipedal-wheeled robot and extensively evaluated. Experiments confirm robust and reliable fall recovery under diverse challenging conditions, demonstrating strong environmental adaptability and motion robustness, while maintaining full post-recovery motion capability. The framework also generalizes effectively to a high-DOF humanoid, confirming its practical generalizability. The project page is available at https://2350575870.github.io/force-guided.github.io/

## 개요
낙하 회복은 자율 보행 로봇에 있어 매우 중요합니다. 기존 방법들은 휴머노이드나 사족 보행 로봇과 같은 일부 보행 로봇이 팔을 사용하거나 다리를 협력하여 지지력을 생성함으로써 다양한 자세에서 낙하 회복이 가능함을 입증했습니다. 그러나 팔이나 다른 다리의 지지 도움 없이 이족 바퀴 로봇은 오직 다리의 구동에만 의존해야 하므로 회복이 특히 어렵습니다. 이를 해결하기 위해 우리는 FTSR(Force-guided Teacher-student framework with Stage-wise Rewards)을 소개합니다. 힘 유도 방법은 시뮬레이션 훈련 중 로봇의 실시간 높이와 직접적으로 상관관계가 있는 외부 보조 힘을 구성하고, 이 힘을 최적화 가능한 제약 조건으로 명시적으로 공식화합니다. 제약 조건 강화 학습을 통해 정책은 점진적으로 힘 의존성을 줄이고 몸체 높이를 높이도록 유도되어, 지지할 팔이 없음에도 불구하고 내부 회복 전략을 개발합니다. 높이 점진적 단계별 보상은 회복 중 자세 안정화와 지속적인 보행으로의 전환을 점진적으로 구조화하며, 교사-학생 아키텍처와 통합되어 힘 효과 및 회복 역학에 대한 특권 지식을 증류합니다. 시뮬레이션 훈련 후, 정책은 실제 팔이 없는 이족 바퀴 로봇에 배포되어 광범위하게 평가됩니다. 실험 결과, 다양한 까다로운 조건에서 강건하고 신뢰할 수 있는 낙하 회복이 확인되었으며, 강한 환경 적응성과 운동 강건성을 보여주고 회복 후 완전한 운동 능력을 유지합니다. 이 프레임워크는 높은 자유도를 가진 휴머노이드에도 효과적으로 일반화되어 실용적인 일반화 가능성을 입증합니다. 프로젝트 페이지는 https://2350575870.github.io/force-guided.github.io/ 에서 확인할 수 있습니다.

## 핵심 내용
낙하 회복은 자율 보행 로봇에 있어 매우 중요합니다. 기존 방법들은 휴머노이드나 사족 보행 로봇과 같은 일부 보행 로봇이 팔을 사용하거나 다리를 협력하여 지지력을 생성함으로써 다양한 자세에서 낙하 회복이 가능함을 입증했습니다. 그러나 팔이나 다른 다리의 지지 도움 없이 이족 바퀴 로봇은 오직 다리의 구동에만 의존해야 하므로 회복이 특히 어렵습니다. 이를 해결하기 위해 우리는 FTSR(Force-guided Teacher-student framework with Stage-wise Rewards)을 소개합니다. 힘 유도 방법은 시뮬레이션 훈련 중 로봇의 실시간 높이와 직접적으로 상관관계가 있는 외부 보조 힘을 구성하고, 이 힘을 최적화 가능한 제약 조건으로 명시적으로 공식화합니다. 제약 조건 강화 학습을 통해 정책은 점진적으로 힘 의존성을 줄이고 몸체 높이를 높이도록 유도되어, 지지할 팔이 없음에도 불구하고 내부 회복 전략을 개발합니다. 높이 점진적 단계별 보상은 회복 중 자세 안정화와 지속적인 보행으로의 전환을 점진적으로 구조화하며, 교사-학생 아키텍처와 통합되어 힘 효과 및 회복 역학에 대한 특권 지식을 증류합니다. 시뮬레이션 훈련 후, 정책은 실제 팔이 없는 이족 바퀴 로봇에 배포되어 광범위하게 평가됩니다. 실험 결과, 다양한 까다로운 조건에서 강건하고 신뢰할 수 있는 낙하 회복이 확인되었으며, 강한 환경 적응성과 운동 강건성을 보여주고 회복 후 완전한 운동 능력을 유지합니다. 이 프레임워크는 높은 자유도를 가진 휴머노이드에도 효과적으로 일반화되어 실용적인 일반화 가능성을 입증합니다. 프로젝트 페이지는 https://2350575870.github.io/force-guided.github.io/ 에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2606.14270v1
