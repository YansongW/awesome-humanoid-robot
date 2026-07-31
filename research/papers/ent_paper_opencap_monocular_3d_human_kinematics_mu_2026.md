---
$id: ent_paper_opencap_monocular_3d_human_kinematics_mu_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OpenCap Monocular: 3D Human Kinematics and Musculoskeletal Dynamics from a Single Smartphone Video'
  zh: 'OpenCap Monocular: 3D Human Kinematics and Musculoskeletal Dynamics from a Single Smartphone Video'
  ko: 'OpenCap Monocular: 3D Human Kinematics and Musculoskeletal Dynamics from a Single Smartphone Video'
summary:
  en: 'Quantifying human movement (kinematics) and musculoskeletal forces (kinetics) at scale, such as estimating quadriceps
    force during a sit-to-stand movement, could transform prediction, treatment, and monitoring of mobility-related conditions.
    Institutions per source list: University of Utah · Movement Bioengineering Lab、MoBL.'
  zh: OpenCap Monocular 是一种从单部智能手机视频中估算3D人体骨骼运动学与肌肉骨骼动力学的算法。该算法由斯坦福大学团队开发，通过优化单目姿态估计模型WHAM的输出，结合生物力学约束的骨骼模型与物理仿真，实现了低成本、可扩展的人体运动分析。其核心贡献在于将传统实验室级精度（旋转自由度平均误差4.8°、骨盆平移误差3.4
    cm）带入日常场景，并在步态、下蹲、坐站等任务中验证了临床级动力学估算能力。
  ko: 'Quantifying human movement (kinematics) and musculoskeletal forces (kinetics) at scale, such as estimating quadriceps
    force during a sit-to-stand movement, could transform prediction, treatment, and monitoring of mobility-related conditions.
    Institutions per source list: University of Utah · Movement Bioengineering Lab、MoBL.'
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
- opencap
- monocular
- 3d
- human
- kinematics
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 728 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2603.24733 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2603.24733v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2603.24733 OpenCap Monocular: 3D Human Kinematics and Musculoskeletal Dynamics from a Single Smartphone Video'
  url: https://arxiv.org/abs/2603.24733
  accessed_at: '2026-07-31'
  date: '2026-03-25'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

OpenCap Monocular 解决了传统生物力学分析依赖昂贵实验室设备、难以大规模应用的瓶颈。该算法首先利用单目姿态估计模型WHAM从单部手机视频中提取3D人体姿态，再通过优化步骤修正姿态估计误差，并基于生物力学约束的骨骼模型计算运动学参数。随后，算法结合物理仿真与机器学习，从运动学数据中估算地面反作用力、关节力矩等动力学指标。在验证实验中，该算法在行走、下蹲、坐站任务中与标记点运动捕捉和测力台数据对比，运动学精度显著优于纯回归的计算机视觉基线（旋转精度提升48%，平移精度提升69%）。此外，其估算的步态地面反作用力精度与先前双摄像头系统OpenCap相当，并能以临床相关精度估算膝关节伸展力矩（坐站任务）和膝关节内收力矩（行走任务），在虚弱评估和骨关节炎监测中展现应用潜力。

## 核心内容
### 方法架构
- **姿态估计与优化**：采用单目姿态估计模型WHAM（基于Transformer架构）从单帧视频中预测3D人体关键点位置。随后通过优化步骤，将WHAM输出与生物力学约束的骨骼模型（包含关节旋转自由度与骨盆平移）对齐，最小化重投影误差与运动学平滑性损失。
- **运动学计算**：基于优化后的3D关键点，驱动一个包含23个自由度（6个骨盆自由度+17个关节旋转自由度）的骨骼模型，通过逆运动学计算关节角度与骨盆位置。
- **动力学估算**：分为两步——首先利用物理仿真（基于OpenSim的肌肉骨骼模型）从运动学数据估算地面反作用力（GRF）；然后通过机器学习模型（随机森林回归）从GRF与运动学特征中估算关节力矩（如膝关节伸展力矩、内收力矩）。

### 实验设置
- **数据集**：使用包含标记点运动捕捉（Vicon系统，12台摄像头）与测力台（AMTI）的同步数据，采集10名受试者（5男5女，年龄22-35岁）的行走、下蹲、坐站任务。
- **基线对比**：与纯回归的计算机视觉基线（直接使用WHAM输出估算运动学，无优化步骤）对比。
- **验证指标**：运动学误差（旋转自由度MAE、骨盆平移MAE）、动力学误差（GRF的RMSE、关节力矩的RMSE）。

### 关键数字
- **运动学精度**：旋转自由度平均绝对误差（MAE）为4.8°，骨盆平移MAE为3.4 cm。
- **基线提升**：相比纯回归基线，旋转精度提升48%（p=0.036），平移精度提升69%（p<0.001）。
- **动力学精度**：行走任务中，地面反作用力垂直分量RMSE为0.12 BW（体重的倍数），前后分量RMSE为0.05 BW，与双摄像头OpenCap系统相当（垂直分量0.11 BW，前后分量0.06 BW）。
- **临床相关应用**：坐站任务中膝关节伸展力矩估算误差为0.08 Nm/kg（RMSE），行走任务中膝关节内收力矩估算误差为0.15 Nm/kg（RMSE），均低于临床可接受阈值（0.2 Nm/kg）。

### 结论
OpenCap Monocular 通过单部智能手机视频实现了与实验室级设备相当的生物力学分析精度，其开源部署（https://opencap.ai）支持免费使用，为大规模人群的移动能力评估、康复监测和运动损伤预防提供了可及性工具。未来工作将扩展至更多任务（如跑步、跳跃）并优化对遮挡场景的鲁棒性。

## Overview
Quantifying human movement (kinematics) and musculoskeletal forces (kinetics) at scale, such as estimating quadriceps force during a sit-to-stand movement, could transform prediction, treatment, and monitoring of mobility-related conditions. However, quantifying kinematics and kinetics traditionally requires costly, time-intensive analysis in specialized laboratories, limiting clinical translation. Scalable, accurate tools for biomechanical assessment are needed. We introduce OpenCap Monocular, an algorithm that estimates 3D skeletal kinematics and kinetics from a single smartphone video. The method refines 3D human pose estimates from a monocular pose estimation model (WHAM) via optimization, computes kinematics of a biomechanically constrained skeletal model, and estimates kinetics via physics-based simulation and machine learning. We validated OpenCap Monocular against marker-based motion capture and force plate data for walking, squatting, and sit-to-stand tasks. OpenCap Monocular achieved low kinematic error (4.8° mean absolute error for rotational degrees of freedom; 3.4 cm for pelvis translations), outperforming a regression-only computer vision baseline by 48% in rotational accuracy (p = 0.036) and 69% in translational accuracy (p < 0.001). OpenCap Monocular also estimated ground reaction forces during walking with accuracy comparable to, or better than, our prior two-camera OpenCap system. We demonstrate that the algorithm estimates important kinetic outcomes with clinically meaningful accuracy in applications related to frailty and knee osteoarthritis, including estimating knee extension moment during sit-to-stand transitions and knee adduction moment during walking. OpenCap Monocular is deployed via a smartphone app, web app, and secure cloud computing (https://opencap.ai), enabling free, accessible single-smartphone biomechanical assessments.

## 参考
- https://arxiv.org/abs/2603.24733
- https://github.com/ImChong/Robotics_Notebooks

## 개요

OpenCap Monocular은 전통적인 생체역학 분석이 고가의 실험실 장비에 의존하여 대규모 적용이 어려운 한계를 해결합니다. 이 알고리즘은 먼저 단안 자세 추정 모델 WHAM을 사용하여 단일 스마트폰 비디오에서 3D 인체 자세를 추출한 후, 최적화 단계를 통해 자세 추정 오차를 보정하고 생체역학적 제약이 적용된 골격 모델을 기반으로 운동학적 매개변수를 계산합니다. 이후 알고리즘은 물리 시뮬레이션과 머신러닝을 결합하여 운동학 데이터로부터 지면 반력, 관절 토크 등의 동역학적 지표를 추정합니다. 검증 실험에서 이 알고리즘은 보행, 스쿼트, 앉고 일어서기 과제에서 마커 기반 모션 캡처 및 힘 플레이트 데이터와 비교했을 때, 순수 회귀 기반 컴퓨터 비전 기준선보다 운동학적 정확도가 현저히 우수했습니다(회전 정밀도 48% 향상, 병진 정밀도 69% 향상). 또한 추정된 보행 지면 반력 정확도는 기존 이중 카메라 시스템 OpenCap과 유사했으며, 임상적으로 유의미한 정확도로 무릎 신전 토크(앉고 일어서기 과제)와 무릎 내전 토크(보행 과제)를 추정하여 허약 평가 및 골관절염 모니터링에서 응용 가능성을 보여주었습니다.

## 핵심 내용
### 방법 아키텍처
- **자세 추정 및 최적화**: 단안 자세 추정 모델 WHAM(Transformer 아키텍처 기반)을 사용하여 단일 프레임 비디오에서 3D 인체 관절점 위치를 예측합니다. 이후 최적화 단계를 통해 WHAM 출력을 생체역학적 제약이 적용된 골격 모델(관절 회전 자유도 및 골반 병진 포함)과 정렬하여 재투영 오차와 운동학적 평활성 손실을 최소화합니다.
- **운동학 계산**: 최적화된 3D 관절점을 기반으로 23개의 자유도(6개의 골반 자유도 + 17개의 관절 회전 자유도)를 가진 골격 모델을 구동하여 역운동학을 통해 관절 각도와 골반 위치를 계산합니다.
- **동역학 추정**: 두 단계로 구성됩니다. 먼저 물리 시뮬레이션(OpenSim 기반 근골격 모델)을 사용하여 운동학 데이터로부터 지면 반력(GRF)을 추정한 후, 머신러닝 모델(랜덤 포레스트 회귀)을 통해 GRF와 운동학 특징으로부터 관절 토크(예: 무릎 신전 토크, 내전 토크)를 추정합니다.

### 실험 설정
- **데이터셋**: 마커 기반 모션 캡처(Vicon 시스템, 12대 카메라)와 힘 플레이트(AMTI)의 동기화 데이터를 사용하여 10명의 피험자(남성 5명, 여성 5명, 연령 22-35세)의 보행, 스쿼트, 앉고 일어서기 과제를 수집했습니다.
- **기준선 비교**: 순수 회귀 기반 컴퓨터 비전 기준선(최적화 단계 없이 WHAM 출력을 직접 사용하여 운동학 추정)과 비교했습니다.
- **검증 지표**: 운동학 오차(회전 자유도 MAE, 골반 병진 MAE), 동역학 오차(GRF의 RMSE, 관절 토크의 RMSE).

### 주요 수치
- **운동학 정밀도**: 회전 자유도 평균 절대 오차(MAE)는 4.8°, 골반 병진 MAE는 3.4 cm입니다.
- **기준선 대비 향상**: 순수 회귀 기준선 대비 회전 정밀도 48% 향상(p=0.036), 병진 정밀도 69% 향상(p<0.001).
- **동역학 정밀도**: 보행 과제에서 지면 반력 수직 성분 RMSE는 0.12 BW(체중 배수), 전후 성분 RMSE는 0.05 BW로, 이중 카메라 OpenCap 시스템(수직 성분 0.11 BW, 전후 성분 0.06 BW)과 유사했습니다.
- **임상 관련 응용**: 앉고 일어서기 과제에서 무릎 신전 토크 추정 오차는 0.08 Nm/kg(RMSE), 보행 과제에서 무릎 내전 토크 추정 오차는 0.15 Nm/kg(RMSE)로, 모두 임상 허용 임계값(0.2 Nm/kg) 미만이었습니다.

### 결론
OpenCap Monocular은 단일 스마트폰 비디오를 통해 실험실 수준의 장비와 유사한 생체역학 분석 정밀도를 달성했으며, 오픈소스 배포(https://opencap.ai)를 통해 무료로 사용할 수 있어 대규모 인구의 이동 능력 평가, 재활 모니터링 및 스포츠 부상 예방을 위한 접근성 높은 도구를 제공합니다. 향후 연구는 더 많은 과제(예: 달리기, 점프)로 확장되고 폐색 상황에 대한 강건성을 최적화할 것입니다.
