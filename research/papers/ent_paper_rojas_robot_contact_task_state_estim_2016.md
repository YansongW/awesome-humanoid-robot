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

## Overview
Uncertainty is a major difficulty in endowing robots with autonomy. Robots often fail due to unexpected events. In robot contact tasks, designs often empirically look for force thresholds to define state transitions in a Markov chain or finite state machines. Such designs are prone to failure in unstructured environments, where external disturbances or erroneous models cause these thresholds to be met, leading to false-positive state transitions. The focus of this paper is to perform high-level state estimation of robot behaviors and task output for robot contact tasks. Our approach encodes raw low-level 3D Cartesian trajectories and converts them into high-level (HL) action grammars. Cartesian trajectories can be segmented and encoded in a way that preserves their dynamic properties, or "texture." Once an action grammar is generated, a classifier is trained to detect current behaviors and ultimately the task output. The system executed HL state estimation for task output verification with an accuracy of 86%, and behavior monitoring with an average accuracy of 72%. The significance of the work lies in transforming difficult-to-use raw low-level data into HL data that enables robust behavior and task monitoring. Monitoring is useful for failure correction or other deliberation in high-level planning, programming by demonstration, and human-robot interaction, to name a few.

## Content
Uncertainty is a major difficulty in endowing robots with autonomy. Robots often fail due to unexpected events. In robot contact tasks, designs often empirically look for force thresholds to define state transitions in a Markov chain or finite state machines. Such designs are prone to failure in unstructured environments, where external disturbances or erroneous models cause these thresholds to be met, leading to false-positive state transitions. The focus of this paper is to perform high-level state estimation of robot behaviors and task output for robot contact tasks. Our approach encodes raw low-level 3D Cartesian trajectories and converts them into high-level (HL) action grammars. Cartesian trajectories can be segmented and encoded in a way that preserves their dynamic properties, or "texture." Once an action grammar is generated, a classifier is trained to detect current behaviors and ultimately the task output. The system executed HL state estimation for task output verification with an accuracy of 86%, and behavior monitoring with an average accuracy of 72%. The significance of the work lies in transforming difficult-to-use raw low-level data into HL data that enables robust behavior and task monitoring. Monitoring is useful for failure correction or other deliberation in high-level planning, programming by demonstration, and human-robot interaction, to name a few.

## 개요
불확실성은 로봇에 자율성을 부여하는 데 있어 주요한 어려움입니다. 로봇은 예상치 못한 사건으로 인해 종종 실패합니다. 로봇 접촉 작업에서는 마르코프 체인 또는 유한 상태 기계에서 상태 전이를 정의하기 위해 경험적으로 힘 임계값을 찾도록 설계되는 경우가 많습니다. 이러한 설계는 비구조화된 환경에서 외부 교란이나 오류 모델로 인해 해당 임계값이 충족되어 거짓 양성 상태 전이가 발생할 때 실패하기 쉽습니다. 본 논문의 초점은 로봇 접촉 작업에 대한 로봇 행동 및 작업 출력의 고수준 상태 추정을 수행하는 것입니다. 우리의 접근 방식은 원시 저수준 3D 직교 좌표 궤적을 인코딩하여 고수준(HL) 행동 문법으로 변환합니다. 직교 좌표 궤적은 동적 속성 또는 "질감"이 보존되는 방식으로 분할 및 인코딩될 수 있습니다. 행동 문법이 생성되면 분류기가 훈련되어 현재 행동과 궁극적으로 작업 출력을 감지합니다. 시스템은 작업 출력 검증을 위해 86%의 정확도로 HL 상태 추정을 실행했으며, 행동 모니터링의 평균 정확도는 72%였습니다. 이 연구의 의의는 사용하기 어려운 원시 저수준 데이터를 강력한 행동 및 작업 모니터링을 가능하게 하는 HL 데이터로 변환하는 데 있습니다. 모니터링은 고수준 계획, 시연을 통한 프로그래밍, 인간-로봇 상호작용 등에서 실패 수정 또는 기타 심의에 유용합니다.

## 핵심 내용
불확실성은 로봇에 자율성을 부여하는 데 있어 주요한 어려움입니다. 로봇은 예상치 못한 사건으로 인해 종종 실패합니다. 로봇 접촉 작업에서는 마르코프 체인 또는 유한 상태 기계에서 상태 전이를 정의하기 위해 경험적으로 힘 임계값을 찾도록 설계되는 경우가 많습니다. 이러한 설계는 비구조화된 환경에서 외부 교란이나 오류 모델로 인해 해당 임계값이 충족되어 거짓 양성 상태 전이가 발생할 때 실패하기 쉽습니다. 본 논문의 초점은 로봇 접촉 작업에 대한 로봇 행동 및 작업 출력의 고수준 상태 추정을 수행하는 것입니다. 우리의 접근 방식은 원시 저수준 3D 직교 좌표 궤적을 인코딩하여 고수준(HL) 행동 문법으로 변환합니다. 직교 좌표 궤적은 동적 속성 또는 "질감"이 보존되는 방식으로 분할 및 인코딩될 수 있습니다. 행동 문법이 생성되면 분류기가 훈련되어 현재 행동과 궁극적으로 작업 출력을 감지합니다. 시스템은 작업 출력 검증을 위해 86%의 정확도로 HL 상태 추정을 실행했으며, 행동 모니터링의 평균 정확도는 72%였습니다. 이 연구의 의의는 사용하기 어려운 원시 저수준 데이터를 강력한 행동 및 작업 모니터링을 가능하게 하는 HL 데이터로 변환하는 데 있습니다. 모니터링은 고수준 계획, 시연을 통한 프로그래밍, 인간-로봇 상호작용 등에서 실패 수정 또는 기타 심의에 유용합니다.
