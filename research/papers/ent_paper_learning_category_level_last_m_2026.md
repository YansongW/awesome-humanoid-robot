---
$id: ent_paper_learning_category_level_last_m_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Category-level Last-meter Navigation from RGB Demonstrations of a Single-instance
  zh: Learning Category-level Last-meter Navigation from RGB Demonstrations of a Single-instance
  ko: Learning Category-level Last-meter Navigation from RGB Demonstrations of a Single-instance
summary:
  en: 'arXiv:2512.11173v4 Announce Type: replace Abstract: Achieving precise positioning of the mobile manipulator''s base
    is essential for successful manipulation actions that follow. Most of the RGB-based navigation systems only guarantee
    coarse, meter-level accuracy, making them less suitable for the precise positioning phase of mobile manipulation. This
    gap prevents manipulation policies from operating within the distribution of their training demonstrations, resulting
    in frequent execution failures. We address this gap by introducing an object-centric imitation learning framework for
    last-meter navigation, enabling a quadruped mobile manipulator robot to achieve manipulation-ready positioning using only
    RGB observations from its onboard cameras. Our method conditions the navigation policy on three inputs: goal images, multi-view
    RGB observations from the onboard cameras, and a text prompt specifying the target object. A language-driven segmentation
    module and a spatial score-matrix decoder then supply explicit object grounding and relative pose reasoning. Using real-world
    data from a single object instance within a category, the system generalizes to unseen object instances across diverse
    environments with challenging lighting and background conditions. To comprehensively evaluate this, we introduce two metrics:
    an edge-alignment metric, which uses ground truth orientation, and an object-alignment metric, which evaluates how well
    the robot visually faces the target. Under these metrics, our policy achieves 74.58% success in edge-alignment and 89.42%
    success in object-alignment when positioning relative to unseen target objects. These results show that precise last-meter
    navigation can be achieved at a category-level without depth, LiDAR, or map priors, enabling a scalable pathway toward
    unified mobile manipulation. Project page: https://rpm-lab-umn.github.io/category-level-last-meter-nav/'
  zh: 本文提出一种面向物体中心的模仿学习框架，用于解决移动操作机器人的“最后一米”精确定位问题。该方法由RPM Lab团队开发，仅依靠RGB相机观测，无需深度、LiDAR或地图先验，即可实现类别级别的精确定位，在未见目标物体上达到74.58%的边缘对齐成功率和89.42%的物体对齐成功率。
  ko: 'arXiv:2512.11173v4 Announce Type: replace Abstract: Achieving precise positioning of the mobile manipulator''s base
    is essential for successful manipulation actions that follow. Most of the RGB-based navigation systems only guarantee
    coarse, meter-level accuracy, making them less suitable for the precise positioning phase of mobile manipulation. This
    gap prevents manipulation policies from operating within the distribution of their training demonstrations, resulting
    in frequent execution failures. We address this gap by introducing an object-centric imitation learning framework for
    last-meter navigation, enabling a quadruped mobile manipulator robot to achieve manipulation-ready positioning using only
    RGB observations from its onboard cameras. Our method conditions the navigation policy on three inputs: goal images, multi-view
    RGB observations from the onboard cameras, and a text prompt specifying the target object. A language-driven segmentation
    module and a spatial score-matrix decoder then supply explicit object grounding and relative pose reasoning. Using real-world
    data from a single object instance within a category, the system generalizes to unseen object instances across diverse
    environments with challenging lighting and background conditions. To comprehensively evaluate this, we introduce two metrics:
    an edge-alignment metric, which uses ground truth orientation, and an object-alignment metric, which evaluates how well
    the robot visually faces the target. Under these metrics, our policy achieves 74.58% success in edge-alignment and 89.42%
    success in object-alignment when positioning relative to unseen target objects. These results show that precise last-meter
    navigation can be achieved at a category-level without depth, LiDAR, or map priors, enabling a scalable pathway toward
    unified mobile manipulation. Project page: https://rpm-lab-umn.github.io/category-level-last-meter-nav/'
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
- learning_category_level_last_m
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.11173v4. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1029 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Learning Category-level Last-meter Navigation from RGB Demonstrations of a Single-instance (arXiv)
  url: https://arxiv.org/abs/2512.11173
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述
现有基于RGB的导航系统通常只能提供米级精度，无法满足移动操作中机械臂执行精确抓取前的定位需求。本文提出一种物体中心的模仿学习框架，使四足移动操作机器人仅通过机载多视角RGB图像和文本提示，即可实现操作就绪的精准定位。该方法利用语言驱动的分割模块和空间得分矩阵解码器，提供显式的物体定位和相对位姿推理，仅使用单个物体实例的真实数据训练，即可泛化到同一类别中未见过的物体实例，并在复杂光照和背景条件下保持鲁棒性。

## 核心内容
### 方法架构
- **输入条件**：导航策略接收三类输入——目标图像（goal images）、机载多视角RGB观测、指定目标物体的文本提示。
- **核心模块**：
  - **语言驱动分割模块**：根据文本提示对多视角RGB图像进行语义分割，提取目标物体的显式空间位置。
  - **空间得分矩阵解码器**：将分割后的特征映射为相对位姿得分，输出机器人相对于目标物体的精确朝向和距离信息。
- **训练数据**：仅使用同一类别中单个物体实例的真实世界演示数据（RGB图像），无需深度或点云标注。

### 实验设置
- **机器人平台**：四足移动操作机器人，搭载机载RGB相机。
- **评估指标**：
  - **边缘对齐指标（edge-alignment）**：使用真实朝向信息，评估机器人底座与目标物体边缘的精确对齐程度。
  - **物体对齐指标（object-alignment）**：评估机器人是否正对目标物体，即视觉朝向的准确性。
- **测试环境**：包含不同光照条件和复杂背景的多样化真实场景，目标物体为训练中未见过的同一类别实例。

### 关键结果
- 在未见目标物体上，边缘对齐成功率达到74.58%，物体对齐成功率达到89.42%。
- 该方法无需深度传感器、LiDAR或地图先验，仅依赖RGB视觉和文本提示，即可实现类别级别的最后一米精确定位。
- 实验表明，该框架为统一移动操作提供了一条可扩展的路径，使导航策略能够与后续操作策略的训练分布保持一致，减少执行失败。

### 结论
本文证明，通过物体中心的模仿学习，可以在无深度、无LiDAR、无地图先验的条件下实现类别级别的精确定位，为移动操作机器人的实际部署提供了低成本、高泛化性的解决方案。项目页面：https://rpm-lab-umn.github.io/category-level-last-meter-nav/

## Overview
Achieving precise positioning of the mobile manipulator's base is essential for successful manipulation actions that follow. Most of the RGB-based navigation systems only guarantee coarse, meter-level accuracy, making them less suitable for the precise positioning phase of mobile manipulation. This gap prevents manipulation policies from operating within the distribution of their training demonstrations, resulting in frequent execution failures. We address this gap by introducing an object-centric imitation learning framework for last-meter navigation, enabling a quadruped mobile manipulator robot to achieve manipulation-ready positioning using only RGB observations from its onboard cameras. Our method conditions the navigation policy on three inputs: goal images, multi-view RGB observations from the onboard cameras, and a text prompt specifying the target object. A language-driven segmentation module and a spatial score-matrix decoder then supply explicit object grounding and relative pose reasoning. Using real-world data from a single object instance within a category, the system generalizes to unseen object instances across diverse environments with challenging lighting and background conditions. To comprehensively evaluate this, we introduce two metrics: an edge-alignment metric, which uses ground truth orientation, and an object-alignment metric, which evaluates how well the robot visually faces the target. Under these metrics, our policy achieves 74.58% success in edge-alignment and 89.42% success in object-alignment when positioning relative to unseen target objects. These results show that precise last-meter navigation can be achieved at a category-level without depth, LiDAR, or map priors, enabling a scalable pathway toward unified mobile manipulation. Project page: https://rpm-lab-umn.github.io/category-level-last-meter-nav/

## 参考
- http://arxiv.org/abs/2512.11173v4

## 개요
기존 RGB 기반 내비게이션 시스템은 일반적으로 미터 단위 정밀도만 제공하여, 이동 조작에서 로봇 팔이 정밀한 파지를 수행하기 전의 위치 파악 요구를 충족할 수 없습니다. 본 논문은 객체 중심의 모방 학습 프레임워크를 제안하여, 네 발 달린 이동 조작 로봇이 온보드 다중 시점 RGB 이미지와 텍스트 프롬프트만으로 조작 준비가 된 정밀 위치 파악을 달성할 수 있게 합니다. 이 방법은 언어 기반 분할 모듈과 공간 점수 행렬 디코더를 활용하여 명시적인 객체 위치 파악과 상대 자세 추론을 제공하며, 단일 객체 인스턴스의 실제 데이터만으로 훈련하여 동일 범주 내에서 보지 못한 객체 인스턴스로 일반화할 수 있고, 복잡한 조명 및 배경 조건에서도 견고성을 유지합니다.

## 핵심 내용
### 방법 아키텍처
- **입력 조건**: 내비게이션 정책은 세 가지 입력을 수신합니다——목표 이미지(goal images), 온보드 다중 시점 RGB 관측, 지정된 목표 객체를 나타내는 텍스트 프롬프트.
- **핵심 모듈**:
  - **언어 기반 분할 모듈**: 텍스트 프롬프트에 따라 다중 시점 RGB 이미지를 의미론적으로 분할하여 목표 객체의 명시적 공간 위치를 추출합니다.
  - **공간 점수 행렬 디코더**: 분할된 특징을 상대 자세 점수로 매핑하여 로봇이 목표 객체에 대한 정밀한 방향과 거리 정보를 출력합니다.
- **훈련 데이터**: 동일 범주 내 단일 객체 인스턴스의 실제 세계 시연 데이터(RGB 이미지)만 사용하며, 깊이 또는 포인트 클라우드 주석이 필요 없습니다.

### 실험 설정
- **로봇 플랫폼**: 네 발 달린 이동 조작 로봇, 온보드 RGB 카메라 탑재.
- **평가 지표**:
  - **가장자리 정렬 지표(edge-alignment)**: 실제 방향 정보를 사용하여 로봇 베이스와 목표 객체 가장자리의 정밀한 정렬 정도를 평가합니다.
  - **객체 정렬 지표(object-alignment)**: 로봇이 목표 객체를 정면으로 바라보는지, 즉 시각적 방향의 정확성을 평가합니다.
- **테스트 환경**: 다양한 조명 조건과 복잡한 배경을 포함한 다양한 실제 장면, 목표 객체는 훈련에서 보지 못한 동일 범주 인스턴스입니다.

### 주요 결과
- 보지 못한 목표 객체에서 가장자리 정렬 성공률은 74.58%, 객체 정렬 성공률은 89.42%에 도달했습니다.
- 이 방법은 깊이 센서, LiDAR 또는 지도 사전 정보 없이 RGB 비전과 텍스트 프롬프트만으로 범주 수준의 마지막 1미터 정밀 위치 파악을 달성할 수 있습니다.
- 실험은 이 프레임워크가 통합 이동 조작을 위한 확장 가능한 경로를 제공하여, 내비게이션 정책이 후속 조작 정책의 훈련 분포와 일관성을 유지하고 실행 실패를 줄일 수 있음을 보여줍니다.

### 결론
본 논문은 객체 중심의 모방 학습을 통해 깊이, LiDAR, 지도 사전 정보 없이 범주 수준의 정밀 위치 파악을 달성할 수 있음을 증명하며, 이동 조작 로봇의 실제 배치를 위한 저비용, 높은 일반화 솔루션을 제공합니다. 프로젝트 페이지: https://rpm-lab-umn.github.io/category-level-last-meter-nav/
