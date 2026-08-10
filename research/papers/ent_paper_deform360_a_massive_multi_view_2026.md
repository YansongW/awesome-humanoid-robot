---
$id: ent_paper_deform360_a_massive_multi_view_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Deform360: A Massive Multi-view Visuotactile Dataset for Deformable World Models'
  zh: 'Deform360: A Massive Multi-view Visuotactile Dataset for Deformable World Models'
  ko: 'Deform360: A Massive Multi-view Visuotactile Dataset for Deformable World Models'
summary:
  en: 'arXiv:2607.05390v1 Announce Type: new Abstract: Predicting object dynamics (i.e., world modeling) is a fundamental
    challenge for robotic manipulation, and modeling deformable objects presents a particularly difficult case due to their
    high-dimensional state spaces and complex material properties. While current world models approach this through two distinct
    paradigms: learning the dynamics over the 2D pixel space or more explicit 3D geometric space. A systematic understanding
    of their relative strengths and limitations remains elusive due to the lack of diverse, large-scale real-world data. To
    address this, we present Deform360, a large-scale visuotactile dataset featuring 198 daily-life objects, 1,980 interaction
    sequences, and over 215 hours of observations from 41 surround-view cameras and bimanual tactile grippers to capture both
    global motion and contact-induced local deformations. Leveraging a novel markerless visuotactile 3D tracking pipeline
    to extract dense geometry and motion, we systematically evaluate current state-of-the-art world models, comparing 2D video
    models against 3D particle models. Finally, we provide a preliminary demonstration indicating the real-world applicability
    of our dataset by performing robot planning tasks on deformable objects. Our analysis reveals key insights into the trade-offs
    between structural priors and scalability, providing a solid benchmark for future research in generalizable deformable
    object-centric world modeling. Project website: https://deform360.lhy.xyz'
  zh: Deform360 是一个大规模多视角视觉触觉数据集，由研究团队提出，用于推动可变形物体的世界模型研究。该数据集包含 198 个日常物体、1,980 次交互序列及超过 215 小时的观测数据，通过 41 个环绕相机和双手触觉夹爪捕获全局运动与接触变形，并利用无标记视觉触觉
    3D 追踪管线提取密集几何与运动信息。
  ko: 'arXiv:2607.05390v1 Announce Type: new Abstract: Predicting object dynamics (i.e., world modeling) is a fundamental
    challenge for robotic manipulation, and modeling deformable objects presents a particularly difficult case due to their
    high-dimensional state spaces and complex material properties. While current world models approach this through two distinct
    paradigms: learning the dynamics over the 2D pixel space or more explicit 3D geometric space. A systematic understanding
    of their relative strengths and limitations remains elusive due to the lack of diverse, large-scale real-world data. To
    address this, we present Deform360, a large-scale visuotactile dataset featuring 198 daily-life objects, 1,980 interaction
    sequences, and over 215 hours of observations from 41 surround-view cameras and bimanual tactile grippers to capture both
    global motion and contact-induced local deformations. Leveraging a novel markerless visuotactile 3D tracking pipeline
    to extract dense geometry and motion, we systematically evaluate current state-of-the-art world models, comparing 2D video
    models against 3D particle models. Finally, we provide a preliminary demonstration indicating the real-world applicability
    of our dataset by performing robot planning tasks on deformable objects. Our analysis reveals key insights into the trade-offs
    between structural priors and scalability, providing a solid benchmark for future research in generalizable deformable
    object-centric world modeling. Project website: https://deform360.lhy.xyz'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- deform360
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.05390v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (816 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Deform360: A Massive Multi-view Visuotactile Dataset for Deformable World Models (arXiv)'
  url: https://arxiv.org/abs/2607.05390
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Deform360 旨在解决可变形物体动力学预测中因缺乏大规模真实数据而难以系统比较 2D 像素空间与 3D 几何空间世界模型的问题。该数据集覆盖 198 个日常物体，包含 1,980 次交互序列，总观测时长超过 215 小时，由 41 个环绕相机和双手触觉夹爪同步采集，以捕捉全局运动与接触引起的局部变形。研究团队开发了一种新颖的无标记视觉触觉 3D 追踪管线，用于提取密集几何与运动数据，并基于此系统评估了当前最先进的 2D 视频模型与 3D 粒子模型。初步演示表明，该数据集可用于可变形物体的机器人规划任务，揭示了结构先验与可扩展性之间的权衡，为未来可泛化的可变形物体世界模型研究提供了坚实基准。

## 核心内容
### 数据集构成
- **规模**：包含 198 个日常物体，1,980 次交互序列，总观测时长超过 215 小时。
- **采集设备**：使用 41 个环绕相机和双手触觉夹爪，同步捕获全局运动与接触引起的局部变形。
- **追踪技术**：采用新颖的无标记视觉触觉 3D 追踪管线，从多模态数据中提取密集几何与运动信息。

### 实验设置与评估
- **模型对比**：系统评估了当前最先进的 2D 视频模型与 3D 粒子模型，比较两者在可变形物体动力学预测上的表现。
- **关键发现**：分析揭示了结构先验与可扩展性之间的权衡，2D 模型在像素空间上更易扩展，但 3D 模型在几何精度上更具优势。
- **应用验证**：通过可变形物体的机器人规划任务进行初步演示，验证了数据集在真实世界中的适用性。

### 结论与意义
Deform360 为可变形物体世界模型研究提供了大规模、多模态的真实数据基准，填补了现有数据集的空白。其系统评估结果有助于指导未来研究在结构先验与可扩展性之间做出合理选择，推动可泛化的物体中心世界模型的发展。项目网站：https://deform360.lhy.xyz

## Overview
Predicting object dynamics (i.e., world modeling) is a fundamental challenge for robotic manipulation, and modeling deformable objects presents a particularly difficult case due to their high-dimensional state spaces and complex material properties. While current world models approach this through two distinct paradigms: learning the dynamics over the 2D pixel space or more explicit 3D geometric space. A systematic understanding of their relative strengths and limitations remains elusive due to the lack of diverse, large-scale real-world data. To address this, we present Deform360, a large-scale visuotactile dataset featuring 198 daily-life objects, 1,980 interaction sequences, and over 215 hours of observations from 41 surround-view cameras and bimanual tactile grippers to capture both global motion and contact-induced local deformations. Leveraging a novel markerless visuotactile 3D tracking pipeline to extract dense geometry and motion, we systematically evaluate current state-of-the-art world models, comparing 2D video models against 3D particle models. Finally, we provide a preliminary demonstration indicating the real-world applicability of our dataset by performing robot planning tasks on deformable objects. Our analysis reveals key insights into the trade-offs between structural priors and scalability, providing a solid benchmark for future research in generalizable deformable object-centric world modeling. Project website: https://deform360.lhy.xyz

## 参考
- http://arxiv.org/abs/2607.05390v1

## 개요
Deform360은 변형 가능한 물체의 역학 예측에서 대규모 실제 데이터 부족으로 2D 픽셀 공간과 3D 기하 공간 세계 모델을 체계적으로 비교하기 어려운 문제를 해결하고자 합니다. 이 데이터셋은 198개의 일상 물체를 포함하며, 1,980회의 상호작용 시퀀스, 총 관측 시간 215시간 이상을 41개의环绕 카메라와 양손 촉각 그리퍼로 동기화 수집하여 전역 운동과 접촉으로 인한 국부 변형을 포착합니다. 연구팀은 조밀한 기하 및 운동 데이터를 추출하기 위한 새로운 무표지 시각-촉각 3D 추적 파이프라인을 개발했으며, 이를 기반으로 현재 최첨단 2D 비디오 모델과 3D 입자 모델을 체계적으로 평가했습니다. 초기 데모는 이 데이터셋이 변형 가능한 물체의 로봇 계획 작업에 사용될 수 있음을 보여주며, 구조적 사전 지식과 확장성 간의 절충을 드러내어 향후 일반화 가능한 변형 가능한 물체 세계 모델 연구를 위한 견고한 벤치마크를 제공합니다.

## 핵심 내용
### 데이터셋 구성
- **규모**: 198개의 일상 물체, 1,980회의 상호작용 시퀀스, 총 관측 시간 215시간 이상 포함.
- **수집 장치**: 41개의环绕 카메라와 양손 촉각 그리퍼를 사용하여 전역 운동과 접촉으로 인한 국부 변형을 동기화 포착.
- **추적 기술**: 다중 모달 데이터에서 조밀한 기하 및 운동 정보를 추출하는 새로운 무표지 시각-촉각 3D 추적 파이프라인 채택.

### 실험 설정 및 평가
- **모델 비교**: 현재 최첨단 2D 비디오 모델과 3D 입자 모델을 체계적으로 평가하여 변형 가능한 물체 역학 예측 성능을 비교.
- **주요 발견**: 분석 결과 구조적 사전 지식과 확장성 간의 절충이 드러났으며, 2D 모델은 픽셀 공간에서 확장이 더 용이하지만 3D 모델은 기하 정밀도에서 더 유리함.
- **응용 검증**: 변형 가능한 물체의 로봇 계획 작업을 통한 초기 데모로 데이터셋의 실제 세계 적용 가능성을 검증.

### 결론 및 의의
Deform360은 변형 가능한 물체 세계 모델 연구를 위한 대규모 다중 모달 실제 데이터 벤치마크를 제공하며, 기존 데이터셋의 공백을 메웁니다. 체계적 평가 결과는 향후 연구가 구조적 사전 지식과 확장성 사이에서 합리적 선택을 하도록 안내하며, 일반화 가능한 객체 중심 세계 모델 개발을 촉진합니다. 프로젝트 웹사이트: https://deform360.lhy.xyz
