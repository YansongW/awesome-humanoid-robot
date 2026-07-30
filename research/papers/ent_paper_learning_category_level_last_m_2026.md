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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.11173v4. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
이동 조작기의 베이스를 정밀하게 위치시키는 것은 이후의 성공적인 조작 동작에 필수적입니다. 대부분의 RGB 기반 내비게이션 시스템은 대략적인 미터 단위의 정확도만 보장하므로, 이동 조작의 정밀 위치 결정 단계에는 적합하지 않습니다. 이러한 격차로 인해 조작 정책이 훈련 시연의 분포 내에서 작동하지 못해 실행 실패가 빈번하게 발생합니다. 우리는 이러한 격차를 해소하기 위해 객체 중심 모방 학습 프레임워크를 최종 미터 내비게이션에 도입하여, 사족 이동 조작 로봇이 탑재 카메라의 RGB 관측만으로 조작 준비가 완료된 위치 결정을 달성할 수 있도록 합니다. 우리의 방법은 내비게이션 정책을 세 가지 입력(목표 이미지, 탑재 카메라의 다중 뷰 RGB 관측, 대상 객체를 지정하는 텍스트 프롬프트)에 조건화합니다. 언어 기반 분할 모듈과 공간 점수 행렬 디코더가 명시적 객체 근거 및 상대적 자세 추론을 제공합니다. 카테고리 내 단일 객체 인스턴스의 실제 데이터를 사용하여, 시스템은 까다로운 조명 및 배경 조건을 가진 다양한 환경에서 보지 못한 객체 인스턴스로 일반화됩니다. 이를 종합적으로 평가하기 위해, 우리는 두 가지 지표(지상 실측 방향을 사용하는 에지 정렬 지표와 로봇이 시각적으로 대상을 얼마나 잘 마주하는지 평가하는 객체 정렬 지표)를 도입합니다. 이 지표 하에서, 우리의 정책은 보지 못한 대상 객체에 대해 위치 결정 시 에지 정렬에서 74.58%, 객체 정렬에서 89.42%의 성공률을 달성합니다. 이러한 결과는 깊이, LiDAR 또는 지도 사전 정보 없이도 카테고리 수준에서 정밀한 최종 미터 내비게이션이 가능함을 보여주며, 통합 이동 조작을 위한 확장 가능한 경로를 제공합니다. 프로젝트 페이지: https://rpm-lab-umn.github.io/category-level-last-meter-nav/

## 핵심 내용
이동 조작기의 베이스를 정밀하게 위치시키는 것은 이후의 성공적인 조작 동작에 필수적입니다. 대부분의 RGB 기반 내비게이션 시스템은 대략적인 미터 단위의 정확도만 보장하므로, 이동 조작의 정밀 위치 결정 단계에는 적합하지 않습니다. 이러한 격차로 인해 조작 정책이 훈련 시연의 분포 내에서 작동하지 못해 실행 실패가 빈번하게 발생합니다. 우리는 이러한 격차를 해소하기 위해 객체 중심 모방 학습 프레임워크를 최종 미터 내비게이션에 도입하여, 사족 이동 조작 로봇이 탑재 카메라의 RGB 관측만으로 조작 준비가 완료된 위치 결정을 달성할 수 있도록 합니다. 우리의 방법은 내비게이션 정책을 세 가지 입력(목표 이미지, 탑재 카메라의 다중 뷰 RGB 관측, 대상 객체를 지정하는 텍스트 프롬프트)에 조건화합니다. 언어 기반 분할 모듈과 공간 점수 행렬 디코더가 명시적 객체 근거 및 상대적 자세 추론을 제공합니다. 카테고리 내 단일 객체 인스턴스의 실제 데이터를 사용하여, 시스템은 까다로운 조명 및 배경 조건을 가진 다양한 환경에서 보지 못한 객체 인스턴스로 일반화됩니다. 이를 종합적으로 평가하기 위해, 우리는 두 가지 지표(지상 실측 방향을 사용하는 에지 정렬 지표와 로봇이 시각적으로 대상을 얼마나 잘 마주하는지 평가하는 객체 정렬 지표)를 도입합니다. 이 지표 하에서, 우리의 정책은 보지 못한 대상 객체에 대해 위치 결정 시 에지 정렬에서 74.58%, 객체 정렬에서 89.42%의 성공률을 달성합니다. 이러한 결과는 깊이, LiDAR 또는 지도 사전 정보 없이도 카테고리 수준에서 정밀한 최종 미터 내비게이션이 가능함을 보여주며, 통합 이동 조작을 위한 확장 가능한 경로를 제공합니다. 프로젝트 페이지: https://rpm-lab-umn.github.io/category-level-last-meter-nav/

## 参考
- http://arxiv.org/abs/2512.11173v4
