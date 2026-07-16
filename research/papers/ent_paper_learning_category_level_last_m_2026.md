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
  zh: 'arXiv:2512.11173v4 Announce Type: replace Abstract: Achieving precise positioning of the mobile manipulator''s base
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.11173v4.
sources:
- id: src_001
  type: paper
  title: Learning Category-level Last-meter Navigation from RGB Demonstrations of a Single-instance (arXiv)
  url: https://arxiv.org/abs/2512.11173
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述
Achieving precise positioning of the mobile manipulator's base is essential for successful manipulation actions that follow. Most of the RGB-based navigation systems only guarantee coarse, meter-level accuracy, making them less suitable for the precise positioning phase of mobile manipulation. This gap prevents manipulation policies from operating within the distribution of their training demonstrations, resulting in frequent execution failures. We address this gap by introducing an object-centric imitation learning framework for last-meter navigation, enabling a quadruped mobile manipulator robot to achieve manipulation-ready positioning using only RGB observations from its onboard cameras. Our method conditions the navigation policy on three inputs: goal images, multi-view RGB observations from the onboard cameras, and a text prompt specifying the target object. A language-driven segmentation module and a spatial score-matrix decoder then supply explicit object grounding and relative pose reasoning. Using real-world data from a single object instance within a category, the system generalizes to unseen object instances across diverse environments with challenging lighting and background conditions. To comprehensively evaluate this, we introduce two metrics: an edge-alignment metric, which uses ground truth orientation, and an object-alignment metric, which evaluates how well the robot visually faces the target. Under these metrics, our policy achieves 74.58% success in edge-alignment and 89.42% success in object-alignment when positioning relative to unseen target objects. These results show that precise last-meter navigation can be achieved at a category-level without depth, LiDAR, or map priors, enabling a scalable pathway toward unified mobile manipulation. Project page: https://rpm-lab-umn.github.io/category-level-last-meter-nav/

## 核心内容
Achieving precise positioning of the mobile manipulator's base is essential for successful manipulation actions that follow. Most of the RGB-based navigation systems only guarantee coarse, meter-level accuracy, making them less suitable for the precise positioning phase of mobile manipulation. This gap prevents manipulation policies from operating within the distribution of their training demonstrations, resulting in frequent execution failures. We address this gap by introducing an object-centric imitation learning framework for last-meter navigation, enabling a quadruped mobile manipulator robot to achieve manipulation-ready positioning using only RGB observations from its onboard cameras. Our method conditions the navigation policy on three inputs: goal images, multi-view RGB observations from the onboard cameras, and a text prompt specifying the target object. A language-driven segmentation module and a spatial score-matrix decoder then supply explicit object grounding and relative pose reasoning. Using real-world data from a single object instance within a category, the system generalizes to unseen object instances across diverse environments with challenging lighting and background conditions. To comprehensively evaluate this, we introduce two metrics: an edge-alignment metric, which uses ground truth orientation, and an object-alignment metric, which evaluates how well the robot visually faces the target. Under these metrics, our policy achieves 74.58% success in edge-alignment and 89.42% success in object-alignment when positioning relative to unseen target objects. These results show that precise last-meter navigation can be achieved at a category-level without depth, LiDAR, or map priors, enabling a scalable pathway toward unified mobile manipulation. Project page: https://rpm-lab-umn.github.io/category-level-last-meter-nav/

## 参考
- http://arxiv.org/abs/2512.11173v4

## Overview
Achieving precise positioning of the mobile manipulator's base is essential for successful manipulation actions that follow. Most of the RGB-based navigation systems only guarantee coarse, meter-level accuracy, making them less suitable for the precise positioning phase of mobile manipulation. This gap prevents manipulation policies from operating within the distribution of their training demonstrations, resulting in frequent execution failures. We address this gap by introducing an object-centric imitation learning framework for last-meter navigation, enabling a quadruped mobile manipulator robot to achieve manipulation-ready positioning using only RGB observations from its onboard cameras. Our method conditions the navigation policy on three inputs: goal images, multi-view RGB observations from the onboard cameras, and a text prompt specifying the target object. A language-driven segmentation module and a spatial score-matrix decoder then supply explicit object grounding and relative pose reasoning. Using real-world data from a single object instance within a category, the system generalizes to unseen object instances across diverse environments with challenging lighting and background conditions. To comprehensively evaluate this, we introduce two metrics: an edge-alignment metric, which uses ground truth orientation, and an object-alignment metric, which evaluates how well the robot visually faces the target. Under these metrics, our policy achieves 74.58% success in edge-alignment and 89.42% success in object-alignment when positioning relative to unseen target objects. These results show that precise last-meter navigation can be achieved at a category-level without depth, LiDAR, or map priors, enabling a scalable pathway toward unified mobile manipulation. Project page: https://rpm-lab-umn.github.io/category-level-last-meter-nav/

## Content
Achieving precise positioning of the mobile manipulator's base is essential for successful manipulation actions that follow. Most of the RGB-based navigation systems only guarantee coarse, meter-level accuracy, making them less suitable for the precise positioning phase of mobile manipulation. This gap prevents manipulation policies from operating within the distribution of their training demonstrations, resulting in frequent execution failures. We address this gap by introducing an object-centric imitation learning framework for last-meter navigation, enabling a quadruped mobile manipulator robot to achieve manipulation-ready positioning using only RGB observations from its onboard cameras. Our method conditions the navigation policy on three inputs: goal images, multi-view RGB observations from the onboard cameras, and a text prompt specifying the target object. A language-driven segmentation module and a spatial score-matrix decoder then supply explicit object grounding and relative pose reasoning. Using real-world data from a single object instance within a category, the system generalizes to unseen object instances across diverse environments with challenging lighting and background conditions. To comprehensively evaluate this, we introduce two metrics: an edge-alignment metric, which uses ground truth orientation, and an object-alignment metric, which evaluates how well the robot visually faces the target. Under these metrics, our policy achieves 74.58% success in edge-alignment and 89.42% success in object-alignment when positioning relative to unseen target objects. These results show that precise last-meter navigation can be achieved at a category-level without depth, LiDAR, or map priors, enabling a scalable pathway toward unified mobile manipulation. Project page: https://rpm-lab-umn.github.io/category-level-last-meter-nav/

## 개요
이동 조작기의 베이스를 정밀하게 위치시키는 것은 이후의 성공적인 조작 동작에 필수적입니다. 대부분의 RGB 기반 내비게이션 시스템은 대략적인 미터 단위의 정확도만 보장하므로, 이동 조작의 정밀 위치 결정 단계에는 적합하지 않습니다. 이러한 격차로 인해 조작 정책이 훈련 시연의 분포 내에서 작동하지 못해 실행 실패가 빈번하게 발생합니다. 우리는 이러한 격차를 해소하기 위해 객체 중심 모방 학습 프레임워크를 최종 미터 내비게이션에 도입하여, 사족 이동 조작 로봇이 탑재 카메라의 RGB 관측만으로 조작 준비가 완료된 위치 결정을 달성할 수 있도록 합니다. 우리의 방법은 내비게이션 정책을 세 가지 입력(목표 이미지, 탑재 카메라의 다중 뷰 RGB 관측, 대상 객체를 지정하는 텍스트 프롬프트)에 조건화합니다. 언어 기반 분할 모듈과 공간 점수 행렬 디코더가 명시적 객체 근거 및 상대적 자세 추론을 제공합니다. 카테고리 내 단일 객체 인스턴스의 실제 데이터를 사용하여, 시스템은 까다로운 조명 및 배경 조건을 가진 다양한 환경에서 보지 못한 객체 인스턴스로 일반화됩니다. 이를 종합적으로 평가하기 위해, 우리는 두 가지 지표(지상 실측 방향을 사용하는 에지 정렬 지표와 로봇이 시각적으로 대상을 얼마나 잘 마주하는지 평가하는 객체 정렬 지표)를 도입합니다. 이 지표 하에서, 우리의 정책은 보지 못한 대상 객체에 대해 위치 결정 시 에지 정렬에서 74.58%, 객체 정렬에서 89.42%의 성공률을 달성합니다. 이러한 결과는 깊이, LiDAR 또는 지도 사전 정보 없이도 카테고리 수준에서 정밀한 최종 미터 내비게이션이 가능함을 보여주며, 통합 이동 조작을 위한 확장 가능한 경로를 제공합니다. 프로젝트 페이지: https://rpm-lab-umn.github.io/category-level-last-meter-nav/

## 핵심 내용
이동 조작기의 베이스를 정밀하게 위치시키는 것은 이후의 성공적인 조작 동작에 필수적입니다. 대부분의 RGB 기반 내비게이션 시스템은 대략적인 미터 단위의 정확도만 보장하므로, 이동 조작의 정밀 위치 결정 단계에는 적합하지 않습니다. 이러한 격차로 인해 조작 정책이 훈련 시연의 분포 내에서 작동하지 못해 실행 실패가 빈번하게 발생합니다. 우리는 이러한 격차를 해소하기 위해 객체 중심 모방 학습 프레임워크를 최종 미터 내비게이션에 도입하여, 사족 이동 조작 로봇이 탑재 카메라의 RGB 관측만으로 조작 준비가 완료된 위치 결정을 달성할 수 있도록 합니다. 우리의 방법은 내비게이션 정책을 세 가지 입력(목표 이미지, 탑재 카메라의 다중 뷰 RGB 관측, 대상 객체를 지정하는 텍스트 프롬프트)에 조건화합니다. 언어 기반 분할 모듈과 공간 점수 행렬 디코더가 명시적 객체 근거 및 상대적 자세 추론을 제공합니다. 카테고리 내 단일 객체 인스턴스의 실제 데이터를 사용하여, 시스템은 까다로운 조명 및 배경 조건을 가진 다양한 환경에서 보지 못한 객체 인스턴스로 일반화됩니다. 이를 종합적으로 평가하기 위해, 우리는 두 가지 지표(지상 실측 방향을 사용하는 에지 정렬 지표와 로봇이 시각적으로 대상을 얼마나 잘 마주하는지 평가하는 객체 정렬 지표)를 도입합니다. 이 지표 하에서, 우리의 정책은 보지 못한 대상 객체에 대해 위치 결정 시 에지 정렬에서 74.58%, 객체 정렬에서 89.42%의 성공률을 달성합니다. 이러한 결과는 깊이, LiDAR 또는 지도 사전 정보 없이도 카테고리 수준에서 정밀한 최종 미터 내비게이션이 가능함을 보여주며, 통합 이동 조작을 위한 확장 가능한 경로를 제공합니다. 프로젝트 페이지: https://rpm-lab-umn.github.io/category-level-last-meter-nav/
