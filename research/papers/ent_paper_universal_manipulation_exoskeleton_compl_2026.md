---
$id: ent_paper_universal_manipulation_exoskeleton_compl_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Universal Manipulation Exoskeleton: Learning Compliant Whole-body Policies with Real-time Torque Feedback'
  zh: 'Universal Manipulation Exoskeleton: Learning Compliant Whole-body Policies with Real-time Torque Feedback'
  ko: 'Universal Manipulation Exoskeleton: Learning Compliant Whole-body Policies with Real-time Torque Feedback'
summary:
  en: 'For robots to work safely in household environments, they need to be compliant and react to torque and force feedback
    during contact. However, the majority of existing data collection pipelines still lack the ability to capture force and
    torque data for learning active compliant policies. Institutions per source list: Ant Group、Stanford University.'
  zh: Universal Manipulation Exoskeleton (UME) 是一种低成本、轻量化的上肢外骨骼系统，由研究团队开发，用于通过实时触觉扭矩反馈实现遥操作。其核心贡献在于支持学习全身主动柔顺策略，在高度受限空间中完成移动操作、力控翻转等任务，并兼容多种机器人平台。
  ko: 'For robots to work safely in household environments, they need to be compliant and react to torque and force feedback
    during contact. However, the majority of existing data collection pipelines still lack the ability to capture force and
    torque data for learning active compliant policies. Institutions per source list: Ant Group、Stanford University.'
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
- universal
- manipulation
- exoskeleton
- compl
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 807 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2606.14218 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2606.14218v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2606.14218 Universal Manipulation Exoskeleton: Learning Compliant Whole-body Policies with Real-time Torque
    Feedback'
  url: https://arxiv.org/abs/2606.14218
  accessed_at: '2026-07-31'
  date: '2026-06-12'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

UME 通过透明扭矩反馈让操作者能在蒙眼状态下完成运动学约束物体的脱鞘操作，并利用嵌入式 IMU 支持移动操作遥操作。该系统采用通用重定向算法，可适配 7DoF OpenArm、7DoF Franka 和 6DoF X-ARM 等机器人。实验表明，基于 UME 学习的自主策略在长时移动操作、力介导箱体翻转、视觉遮挡箱体推挤及空间受限桌面操作等任务中均达到高成功率。

## 核心内容
### 系统架构
- **硬件设计**：UME 为上肢外骨骼，集成实时触觉扭矩反馈与关节扭矩信号记录，配备嵌入式 IMU 实现移动操作遥操作。系统强调低成本、轻量化与便携性。
- **通用重定向算法**：提出通用重定向算法，支持将人类操作映射到不同机器人平台，包括 7DoF OpenArm、7DoF Franka 和 6DoF X-ARM。

### 核心能力
- **透明扭矩反馈**：操作者可在蒙眼状态下完成运动学约束物体的脱鞘操作，验证了扭矩反馈的实时性与透明度。
- **全身主动柔顺策略学习**：通过遥操作采集全身关节配置与扭矩数据，训练机器人自主策略，使其在高度受限空间中实现主动柔顺行为。

### 实验设置与结果
- **任务类型**：涵盖长时移动操作、力介导箱体翻转、视觉遮挡箱体推挤及空间受限桌面操作。
- **关键性能**：学习到的自主策略在所有任务中均达到高成功率，尤其在力介导箱体翻转和视觉遮挡箱体推挤任务中表现突出，验证了扭矩反馈对主动柔顺策略的增强作用。

### 结论
UME 通过低成本硬件与通用重定向算法，为学习全身主动柔顺策略提供了有效数据采集方案，在复杂家庭环境中展现出高鲁棒性与泛化能力。

## Overview
For robots to work safely in household environments, they need to be compliant and react to torque and force feedback during contact. However, the majority of existing data collection pipelines still lack the ability to capture force and torque data for learning active compliant policies. In this paper, we present Universal Manipulation Exoskeleton (UME), an upper-limb exoskeleton that provides real-time haptic torque feedback while recording whole-arm configurations and joint torque signals for teleoperation. With transparent torque feedback, human operators can even unsheathe kinematically constrained objects while blindfolded. UME is low-cost, lightweight, and portable. Equipped with an embedded IMU, it enables teleoperation for mobile manipulation. With our proposed universal retargeting algorithm, UME can teleoperate a range of robots, including the 7DoF OpenArm, 7DoF Franka, and 6DoF X-ARM. We demonstrate that this combination of capabilities enables learning bimanual, whole-body, and active compliant policies that operate effectively in highly constrained spaces. The learned robust autonomous policies achieve high success rates across a variety of tasks, including long-horizon mobile manipulation, force-mediated box flipping, visually occluded box pushing, and space-constrained tabletop manipulation. Videos, code, and additional information can be found at https://ume-exo.github.io.

## 参考
- https://arxiv.org/abs/2606.14218
- https://github.com/ImChong/Robotics_Notebooks

## 개요

UME는 투명한 토크 피드백을 통해 조작자가 눈을 가린 상태에서도 운동학적 구속을 받는 물체의 탈피(脫鞘) 작업을 완료할 수 있게 하며, 내장형 IMU를 활용해 이동 조작 원격 조작을 지원합니다. 이 시스템은 범용 재배향 알고리즘을 채택하여 7DoF OpenArm, 7DoF Franka, 6DoF X-ARM 등의 로봇에 적용할 수 있습니다. 실험 결과, UME 기반으로 학습된 자율 정책은 장시간 이동 조작, 힘 매개 상자 뒤집기, 시각적 가림 상자 밀기, 공간 제약 데스크톱 조작 등의 작업에서 높은 성공률을 달성했습니다.

## 핵심 내용
### 시스템 아키텍처
- **하드웨어 설계**: UME는 상지 외골격으로, 실시간 촉각 토크 피드백과 관절 토크 신호 기록을 통합하며, 이동 조작 원격 조작을 위한 내장형 IMU를 갖추고 있습니다. 시스템은 저비용, 경량화, 휴대성을 강조합니다.
- **범용 재배향 알고리즘**: 인간의 조작을 다양한 로봇 플랫폼(7DoF OpenArm, 7DoF Franka, 6DoF X-ARM 포함)에 매핑할 수 있는 범용 재배향 알고리즘을 제안합니다.

### 핵심 역량
- **투명한 토크 피드백**: 조작자는 눈을 가린 상태에서도 운동학적 구속을 받는 물체의 탈피 작업을 완료할 수 있어, 토크 피드백의 실시간성과 투명성을 검증합니다.
- **전신 능동 순응 정책 학습**: 원격 조작을 통해 전신 관절 구성과 토크 데이터를 수집하여 로봇의 자율 정책을 훈련시키며, 고도로 제약된 공간에서 능동 순응 행동을 구현합니다.

### 실험 설정 및 결과
- **작업 유형**: 장시간 이동 조작, 힘 매개 상자 뒤집기, 시각적 가림 상자 밀기, 공간 제약 데스크톱 조작을 포함합니다.
- **주요 성능**: 학습된 자율 정책은 모든 작업에서 높은 성공률을 달성했으며, 특히 힘 매개 상자 뒤집기와 시각적 가림 상자 밀기 작업에서 두드러진 성과를 보여 토크 피드백이 능동 순응 정책을 강화함을 입증합니다.

### 결론
UME는 저비용 하드웨어와 범용 재배향 알고리즘을 통해 전신 능동 순응 정책 학습을 위한 효과적인 데이터 수집 방안을 제공하며, 복잡한 가정 환경에서 높은 견고성과 일반화 능력을 나타냅니다.
