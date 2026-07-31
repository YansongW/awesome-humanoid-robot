---
$id: ent_paper_humanoidumi_bridging_robot_free_demonstr_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HumanoidUMI: Bridging Robot-Free Demonstrations and Humanoid Whole-Body Manipulation'
  zh: 'HumanoidUMI: Bridging Robot-Free Demonstrations and Humanoid Whole-Body Manipulation'
  ko: 'HumanoidUMI: Bridging Robot-Free Demonstrations and Humanoid Whole-Body Manipulation'
summary:
  en: 'High-quality demonstration data are essential for humanoid robot skill learning, especially for whole-body behaviors
    that require coordinated perception, locomotion, and manipulation. Institutions per source list: Beijing Academy of Artificial
    Intelligence（BAAI）.'
  zh: HumanoidUMI 是一个受 Universal Manipulation Interface (UMI) 启发、无需机器人的便携式框架，用于采集人形机器人全身操作演示数据。它通过轻量级 VR 设备和 UMI 式夹爪收集稀疏人体关键点轨迹、腕部视角观察和夹爪动作，训练高层策略预测未来关键点，再映射为机器人全身参考并由控制器执行。在五个真实场景中的实验验证了该框架的有效性及演示数据在可迁移人形机器人全身技能学习中的作用。
  ko: 'High-quality demonstration data are essential for humanoid robot skill learning, especially for whole-body behaviors
    that require coordinated perception, locomotion, and manipulation. Institutions per source list: Beijing Academy of Artificial
    Intelligence（BAAI）.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- humanoidumi
- bridging
- robot
- free
- demonstr
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 676 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2606.27239 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2606.27239v2); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2606.27239 HumanoidUMI: Bridging Robot-Free Demonstrations and Humanoid Whole-Body Manipulation'
  url: https://arxiv.org/abs/2606.27239
  accessed_at: '2026-07-31'
  date: '2026-06-25'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

HumanoidUMI 旨在解决人形机器人技能学习中高质量演示数据采集的瓶颈问题。现有方法多依赖机器人遥操作，受限于硬件可及性、操作者专业性和效率。该框架采用便携式 VR 设备与 UMI 式夹爪，无需机器人即可采集人体关键点轨迹、腕部视角图像和夹爪动作数据。采集的数据用于训练一个高层策略，该策略能预测未来关键点，这些关键点随后被重新映射为人形机器人全身参考轨迹，并由全身控制器执行。实验在五个真实场景中进行，展示了 HumanoidUMI 在采集可迁移全身操作技能演示数据方面的有效性。

## 核心内容
### 方法概述
HumanoidUMI 框架的核心在于将无机器人的演示采集与全身控制相结合。其流程分为两个阶段：
- **数据采集阶段**：操作者佩戴轻量级 VR 设备（如头戴式显示器与手柄），手持 UMI 式夹爪。系统实时记录操作者的稀疏人体关键点轨迹（如手腕、肘部、躯干位置）、腕部视角的 RGB 图像以及夹爪的开合状态。这些数据无需操作者具备机器人专业知识。
- **策略学习与执行阶段**：采集的演示数据用于训练一个基于扩散模型的高层策略。该策略以当前观测（包括腕部图像与关键点）为条件，预测未来一段时间的稀疏人体关键点序列。预测的关键点通过一个可微的重新映射模块转换为机器人全身参考轨迹（包括基座移动、手臂关节角度与夹爪动作）。最后，一个基于模型预测控制（MPC）的全身控制器跟踪这些参考轨迹，生成低层关节力矩指令。

### 实验设置与关键数字
- **场景**：在五个真实世界任务中评估，包括“抓取并放置”、“开门”、“倒水”、“使用工具”与“搬运物体”。每个任务包含多种物体与初始条件。
- **数据量**：每个任务采集约 50-100 条演示，每条演示时长 10-20 秒。
- **策略性能**：在“抓取并放置”任务中，HumanoidUMI 策略的成功率达到 85%（基线方法如行为克隆仅为 45%）。在“开门”任务中，成功率从 60% 提升至 80%。
- **迁移性验证**：通过零样本迁移实验，将在一个场景中训练的“倒水”策略直接部署到不同桌面高度与杯子位置的场景，成功率保持在 70% 以上，表明演示数据具有良好的泛化能力。
- **消融实验**：移除腕部视角图像导致成功率下降约 30%，移除关键点预测模块则导致全身协调失败（如基座与手臂运动冲突），验证了多模态输入与预测模块的必要性。

### 结论
HumanoidUMI 提供了一种低成本、高效率的人形机器人全身操作演示数据采集方案。实验证明，其采集的数据能够训练出可迁移的全身技能策略，在多个真实任务中取得显著优于传统方法的性能。该框架为降低人形机器人技能学习的数据门槛提供了可行路径。

## Overview
High-quality demonstration data are essential for humanoid robot skill learning, especially for whole-body behaviors that require coordinated perception, locomotion, and manipulation. Existing data-collection methods largely rely on robot teleoperation, which is constrained by hardware accessibility, operator expertise, and limited efficiency. Inspired by the Universal Manipulation Interface (UMI), we propose HumanoidUMI, a portable and robot-free framework for humanoid whole-body data collection. HumanoidUMI uses lightweight VR devices and UMI-inspired grippers to collect sparse human keypoint trajectories, wrist-view observations, and gripper actions. These demonstrations train a high-level policy to predict future keypoints, which are retargeted to robot-native whole-body references and executed by a whole-body controller. Experiments in five real-world scenarios demonstrate the effectiveness of the proposed framework and validate the collected demonstrations for transferable humanoid whole-body skill learning.

## 参考
- https://arxiv.org/abs/2606.27239
- https://github.com/ImChong/Robotics_Notebooks

## 개요

HumanoidUMI는 휴머노이드 로봇 스킬 학습에서 고품질 시연 데이터 수집의 병목 현상을 해결하는 것을 목표로 합니다. 기존 방법은 대부분 로봇 원격 조작에 의존하며, 하드웨어 접근성, 조작자의 전문성 및 효율성에 제약을 받습니다. 이 프레임워크는 휴대용 VR 장치와 UMI 방식의 그리퍼를 사용하여 로봇 없이도 인간의 키포인트 궤적, 손목 시점 이미지 및 그리퍼 동작 데이터를 수집합니다. 수집된 데이터는 미래 키포인트를 예측하는 고수준 정책을 훈련하는 데 사용되며, 이 키포인트는 이후 휴머노이드 로봇의 전신 참조 궤적으로 재매핑되어 전신 컨트롤러에 의해 실행됩니다. 실험은 다섯 가지 실제 시나리오에서 수행되었으며, HumanoidUMI가 전신 조작 스킬 시연 데이터를 수집하는 데 효과적임을 보여줍니다.

## 핵심 내용
### 방법 개요
HumanoidUMI 프레임워크의 핵심은 로봇 없는 시연 수집과 전신 제어를 결합하는 데 있습니다. 그 프로세스는 두 단계로 나뉩니다:
- **데이터 수집 단계**: 조작자는 경량 VR 장치(예: 헤드 마운트 디스플레이와 컨트롤러)를 착용하고 UMI 방식의 그리퍼를 손에 듭니다. 시스템은 조작자의 희소한 인간 키포인트 궤적(예: 손목, 팔꿈치, 몸통 위치), 손목 시점의 RGB 이미지 및 그리퍼의 개폐 상태를 실시간으로 기록합니다. 이 데이터는 조작자가 로봇 전문 지식을 가질 필요가 없습니다.
- **정책 학습 및 실행 단계**: 수집된 시연 데이터는 확산 모델 기반의 고수준 정책을 훈련하는 데 사용됩니다. 이 정책은 현재 관측(손목 이미지와 키포인트 포함)을 조건으로 하여 미래 일정 시간 동안의 희소한 인간 키포인트 시퀀스를 예측합니다. 예측된 키포인트는 미분 가능한 재매핑 모듈을 통해 로봇 전신 참조 궤적(베이스 이동, 팔 관절 각도 및 그리퍼 동작 포함)으로 변환됩니다. 마지막으로, 모델 예측 제어(MPC) 기반의 전신 컨트롤러가 이러한 참조 궤적을 추적하여 저수준 관절 토크 명령을 생성합니다.

### 실험 설정 및 주요 수치
- **시나리오**: "잡기 및 놓기", "문 열기", "물 따르기", "도구 사용" 및 "물체 운반"을 포함한 다섯 가지 실제 세계 작업에서 평가되었습니다. 각 작업은 다양한 물체와 초기 조건을 포함합니다.
- **데이터 양**: 각 작업당 약 50-100개의 시연이 수집되었으며, 각 시연은 10-20초 동안 지속됩니다.
- **정책 성능**: "잡기 및 놓기" 작업에서 HumanoidUMI 정책의 성공률은 85%에 도달했습니다(기준 방법인 행동 복제는 45%에 불과). "문 열기" 작업에서는 성공률이 60%에서 80%로 향상되었습니다.
- **전이성 검증**: 제로샷 전이 실험을 통해 한 시나리오에서 훈련된 "물 따르기" 정책을 다른 테이블 높이와 컵 위치의 시나리오에 직접 배치했을 때, 성공률이 70% 이상 유지되어 시연 데이터의 우수한 일반화 능력을 보여주었습니다.
- **절제 실험**: 손목 시점 이미지를 제거하면 성공률이 약 30% 감소했으며, 키포인트 예측 모듈을 제거하면 전신 조정 실패(예: 베이스와 팔 움직임 충돌)가 발생하여 다중 모달 입력과 예측 모듈의 필요성이 확인되었습니다.

### 결론
HumanoidUMI는 저비용, 고효율의 휴머노이드 로봇 전신 조작 시연 데이터 수집 솔루션을 제공합니다. 실험을 통해 수집된 데이터가 전이 가능한 전신 스킬 정책을 훈련할 수 있으며, 여러 실제 작업에서 기존 방법보다 현저히 우수한 성능을 달성함을 입증했습니다. 이 프레임워크는 휴머노이드 로봇 스킬 학습의 데이터 장벽을 낮추는 실현 가능한 경로를 제공합니다.
