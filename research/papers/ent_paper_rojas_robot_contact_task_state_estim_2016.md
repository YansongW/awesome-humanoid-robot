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
  en: This paper converts 3D Cartesian end-effector trajectories into high-level action
    grammars through Frenet-frame segmentation and Direct Curve Coding, then uses
    linear SVMs to classify robot behaviors and verify task output, achieving 86%
    task-output verification and 72% behavior-monitoring accuracy on snap-assembly
    tasks in simulation and on a real HIRO-NX dual-arm humanoid robot.
  zh: 本文通过Frenet标架分割与直接曲线编码将三维笛卡尔末端轨迹转换为高层动作语法，并使用线性SVM对机器人行为分类和任务输出验证，在仿真与真实HIRO-NX双臂人形机器人上的卡扣装配任务中分别取得86%的任务输出验证准确率和72%的行为监控平均准确率。
  ko: 본 논문은 Frenet 프레임 분할과 Direct Curve Coding을 통해 3D 데카르트 엔드이펙터 궤적을 고수준 액션 문법으로 변환한
    뒤 선형 SVM으로 로봇 행동을 분류하고 작업 결과를 검증하여, 시뮬레이션과 실제 HIRO-NX 이팔 인간형 로봇의 스냅 조립 작업에서 작업
    결과 검증 86%, 행동 모니터링 평균 72%의 정확도를 달성하였다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the arXiv full text (arXiv:1609.04946v1); requires human
    review before final verification.
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

## Overview

Contact tasks are commonly implemented by empirically tuning force thresholds that trigger state transitions in finite-state machines or Markov chains. This threshold-based design is brittle: unexpected disturbances or model errors can cause false-positive transitions, leading to task failures. To address this, Rojas, Huang, and Harada propose a high-level state-estimation pipeline that reasons over 3D Cartesian trajectories instead of raw force signals. The pipeline segments end-effector position curves, encodes them as discrete action grammars, and classifies the resulting strings to monitor robot behaviors and verify the final task output.

The method consists of three stages: segmentation, encoding, and classification. Segmentation uses Frenet frames (FF) or accumulated Frenet frames (AFF) to capture local direction changes and motion "texture" along a 3D curve. The segmented frames are then converted into a string of canonical motion directions via Direct Curve Coding (DCC), producing an action grammar. Because grammar strings can differ in length, the authors align feature vectors by either truncating to the shortest string or resampling to a common length. A linear support vector machine is finally trained on these feature vectors to classify individual behaviors and overall task success or failure.

The system is evaluated on a snap-assembly task involving male and female 4-snap cantilever camera parts. Experiments are run both in the OpenHRP 3.0 simulator and on a real HIRO-NX 6-DoF dual-arm anthropomorphic robot. Three datasets are considered: successful assembly in simulation (A), controlled failed assembly in simulation (B), and successful assembly with the real robot (C). The best configuration (FF with linear SVC and cut-off alignment) reports 86% average task-output verification accuracy and 72% average behavior-monitoring accuracy across the combined datasets, with real-robot success assemblies reaching up to 100% task-output accuracy.

## Key Contributions

- Introduces a pipeline that converts 3D Cartesian position trajectories into high-level action grammars for robot contact-task state estimation.
- Evaluates both Frenet frame (FF) and accumulated Frenet frame (AFF) segmentation, combined with Direct Curve Coding, for behavior and task-output classification.
- Reports 86% average task-output verification accuracy and 72% average behavior-monitoring accuracy on snap-assembly tasks, with near-perfect accuracy on successful real-robot assemblies.
- Demonstrates the approach in both the OpenHRP 3.0 simulation environment and on the real HIRO-NX dual-arm humanoid robot.

## Relevance to Humanoid Robotics

The work is directly relevant to humanoid robotics because it validates process monitoring and failure detection on a real dual-arm humanoid robot. The HIRO-NX platform executes a representative industrial assembly task—snap fitting of cantilever camera parts—where robust state estimation can prevent false-positive state transitions and enable failure correction.

By turning low-level position data into interpretable high-level behavior descriptions, the method supports deliberation in high-level planning, programming by demonstration, and human-robot interaction. Reliable assembly monitoring is a prerequisite for deploying humanoids in mass-production or industrial-integration settings where autonomous error recovery is required.
