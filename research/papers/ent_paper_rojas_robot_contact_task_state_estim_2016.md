---
$id: ent_paper_rojas_robot_contact_task_state_estim_2016
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Robot Contact Task State Estimation via Position-based Action Grammars
  zh: 基于位置的动作语法用于机器人接触任务状态估计
  ko: 위치 기반 액션 문법을 활용한 로봇 접촉 작업 상태 추정
summary:
  en: This paper converts 3D Cartesian end-effector trajectories into high-level action grammars through Frenet-frame segmentation
    and Direct Curve Coding, then uses linear SVMs to classify robot behaviors and verify task output, achieving 86% task-output
    verification and 72% behavior-monitoring accuracy on snap-assembly tasks in simulation and on a real HIRO-NX dual-arm
    humanoid robot.
  zh: 本文通过Frenet标架分割与直接曲线编码将三维笛卡尔末端轨迹转换为高层动作语法，并使用线性SVM对机器人行为分类和任务输出验证，在仿真与真实HIRO-NX双臂人形机器人上的卡扣装配任务中分别取得86%的任务输出验证准确率和72%的行为监控平均准确率。
  ko: 본 논문은 Frenet 프레임 분할과 Direct Curve Coding을 통해 3D 데카르트 엔드이펙터 궤적을 고수준 액션 문법으로 변환한 뒤 선형 SVM으로 로봇 행동을 분류하고 작업 결과를 검증하여, 시뮬레이션과
    실제 HIRO-NX 이팔 인간형 로봇의 스냅 조립 작업에서 작업 결과 검증 86%, 행동 모니터링 평균 72%의 정확도를 달성하였다.
domains:
- 04_assembly_integration_testing
- 07_ai_models_algorithms
- 03_manufacturing_processes
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- contact_task
- state_estimation
- action_grammar
- frenet_frame
- direct_curve_coding
- accumulated_frenet_frames
- linear_svm
- snap_assembly
- failure_detection
- process_monitoring
- dual_arm_humanoid
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1609.04946v1.
sources:
- id: src_001
  type: paper
  title: Robot Contact Task State Estimation via Position-based Action Grammars
  url: https://arxiv.org/abs/1609.04946
  date: '2016'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Uncertainty is a major difficulty in endowing robots with autonomy. Robots often fail due to unexpected events. In robot contact tasks are often design to empirically look for force thresholds to define state transitions in a Markov chain or finite state machines. Such design is prone to failure in unstructured environments, when due to external disturbances or erroneous models, such thresholds are met, and lead to state transitions that are false-positives. The focus of this paper is to perform high-level state estimation of robot behaviors and task output for robot contact tasks. Our approach encodes raw low-level 3D cartesian trajectories and converts them into a high level (HL) action grammars. Cartesian trajectories can be segmented and encoded in a way that their dynamic properties, or "texture" are preserved. Once an action grammar is generated, a classifier is trained to detect current behaviors and ultimately the task output. The system executed HL state estimation for task output verification with an accuracy of 86%, and behavior monitoring with an average accuracy of: 72%. The significance of the work is the transformation of difficult-to-use raw low-level data to HL data that enables robust behavior and task monitoring. Monitoring is useful for failure correction or other deliberation in high-level planning, programming by demonstration, and human-robot interaction to name a few.

## 核心内容
Uncertainty is a major difficulty in endowing robots with autonomy. Robots often fail due to unexpected events. In robot contact tasks are often design to empirically look for force thresholds to define state transitions in a Markov chain or finite state machines. Such design is prone to failure in unstructured environments, when due to external disturbances or erroneous models, such thresholds are met, and lead to state transitions that are false-positives. The focus of this paper is to perform high-level state estimation of robot behaviors and task output for robot contact tasks. Our approach encodes raw low-level 3D cartesian trajectories and converts them into a high level (HL) action grammars. Cartesian trajectories can be segmented and encoded in a way that their dynamic properties, or "texture" are preserved. Once an action grammar is generated, a classifier is trained to detect current behaviors and ultimately the task output. The system executed HL state estimation for task output verification with an accuracy of 86%, and behavior monitoring with an average accuracy of: 72%. The significance of the work is the transformation of difficult-to-use raw low-level data to HL data that enables robust behavior and task monitoring. Monitoring is useful for failure correction or other deliberation in high-level planning, programming by demonstration, and human-robot interaction to name a few.

## 参考
- http://arxiv.org/abs/1609.04946v1

