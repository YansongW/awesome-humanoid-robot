---
$id: ent_paper_orb_slam3_an_accurate_open_sou_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multi-Map SLAM'
  zh: 'ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multi-Map SLAM'
  ko: 'ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multi-Map SLAM'
summary:
  en: 'ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multi-Map SLAM is a 2026 work on state estimation
    for humanoid robots.'
  zh: 'ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multi-Map SLAM is a 2026 work on state estimation
    for humanoid robots.'
  ko: 'ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multi-Map SLAM is a 2026 work on state estimation
    for humanoid robots.'
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
- orb_slam3
- slam
- state_estimation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2007.11898v2.
sources:
- id: src_001
  type: website
  title: 'ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multi-Map SLAM project page'
  url: https://github.com/UZ-SLAMLab/ORB_SLAM3
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
This paper presents ORB-SLAM3, the first system able to perform visual, visual-inertial and multi-map SLAM with monocular, stereo and RGB-D cameras, using pin-hole and fisheye lens models. The first main novelty is a feature-based tightly-integrated visual-inertial SLAM system that fully relies on Maximum-a-Posteriori (MAP) estimation, even during the IMU initialization phase. The result is a system that operates robustly in real-time, in small and large, indoor and outdoor environments, and is 2 to 5 times more accurate than previous approaches. The second main novelty is a multiple map system that relies on a new place recognition method with improved recall. Thanks to it, ORB-SLAM3 is able to survive to long periods of poor visual information: when it gets lost, it starts a new map that will be seamlessly merged with previous maps when revisiting mapped areas. Compared with visual odometry systems that only use information from the last few seconds, ORB-SLAM3 is the first system able to reuse in all the algorithm stages all previous information. This allows to include in bundle adjustment co-visible keyframes, that provide high parallax observations boosting accuracy, even if they are widely separated in time or if they come from a previous mapping session. Our experiments show that, in all sensor configurations, ORB-SLAM3 is as robust as the best systems available in the literature, and significantly more accurate. Notably, our stereo-inertial SLAM achieves an average accuracy of 3.6 cm on the EuRoC drone and 9 mm under quick hand-held motions in the room of TUM-VI dataset, a setting representative of AR/VR scenarios. For the benefit of the community we make public the source code.

## 核心内容
This paper presents ORB-SLAM3, the first system able to perform visual, visual-inertial and multi-map SLAM with monocular, stereo and RGB-D cameras, using pin-hole and fisheye lens models. The first main novelty is a feature-based tightly-integrated visual-inertial SLAM system that fully relies on Maximum-a-Posteriori (MAP) estimation, even during the IMU initialization phase. The result is a system that operates robustly in real-time, in small and large, indoor and outdoor environments, and is 2 to 5 times more accurate than previous approaches. The second main novelty is a multiple map system that relies on a new place recognition method with improved recall. Thanks to it, ORB-SLAM3 is able to survive to long periods of poor visual information: when it gets lost, it starts a new map that will be seamlessly merged with previous maps when revisiting mapped areas. Compared with visual odometry systems that only use information from the last few seconds, ORB-SLAM3 is the first system able to reuse in all the algorithm stages all previous information. This allows to include in bundle adjustment co-visible keyframes, that provide high parallax observations boosting accuracy, even if they are widely separated in time or if they come from a previous mapping session. Our experiments show that, in all sensor configurations, ORB-SLAM3 is as robust as the best systems available in the literature, and significantly more accurate. Notably, our stereo-inertial SLAM achieves an average accuracy of 3.6 cm on the EuRoC drone and 9 mm under quick hand-held motions in the room of TUM-VI dataset, a setting representative of AR/VR scenarios. For the benefit of the community we make public the source code.

## 参考
- http://arxiv.org/abs/2007.11898v2

## Overview
This paper presents ORB-SLAM3, the first system able to perform visual, visual-inertial and multi-map SLAM with monocular, stereo and RGB-D cameras, using pin-hole and fisheye lens models. The first main novelty is a feature-based tightly-integrated visual-inertial SLAM system that fully relies on Maximum-a-Posteriori (MAP) estimation, even during the IMU initialization phase. The result is a system that operates robustly in real-time, in small and large, indoor and outdoor environments, and is 2 to 5 times more accurate than previous approaches. The second main novelty is a multiple map system that relies on a new place recognition method with improved recall. Thanks to it, ORB-SLAM3 is able to survive to long periods of poor visual information: when it gets lost, it starts a new map that will be seamlessly merged with previous maps when revisiting mapped areas. Compared with visual odometry systems that only use information from the last few seconds, ORB-SLAM3 is the first system able to reuse in all the algorithm stages all previous information. This allows to include in bundle adjustment co-visible keyframes, that provide high parallax observations boosting accuracy, even if they are widely separated in time or if they come from a previous mapping session. Our experiments show that, in all sensor configurations, ORB-SLAM3 is as robust as the best systems available in the literature, and significantly more accurate. Notably, our stereo-inertial SLAM achieves an average accuracy of 3.6 cm on the EuRoC drone and 9 mm under quick hand-held motions in the room of TUM-VI dataset, a setting representative of AR/VR scenarios. For the benefit of the community we make public the source code.

## Content
This paper presents ORB-SLAM3, the first system able to perform visual, visual-inertial and multi-map SLAM with monocular, stereo and RGB-D cameras, using pin-hole and fisheye lens models. The first main novelty is a feature-based tightly-integrated visual-inertial SLAM system that fully relies on Maximum-a-Posteriori (MAP) estimation, even during the IMU initialization phase. The result is a system that operates robustly in real-time, in small and large, indoor and outdoor environments, and is 2 to 5 times more accurate than previous approaches. The second main novelty is a multiple map system that relies on a new place recognition method with improved recall. Thanks to it, ORB-SLAM3 is able to survive to long periods of poor visual information: when it gets lost, it starts a new map that will be seamlessly merged with previous maps when revisiting mapped areas. Compared with visual odometry systems that only use information from the last few seconds, ORB-SLAM3 is the first system able to reuse in all the algorithm stages all previous information. This allows to include in bundle adjustment co-visible keyframes, that provide high parallax observations boosting accuracy, even if they are widely separated in time or if they come from a previous mapping session. Our experiments show that, in all sensor configurations, ORB-SLAM3 is as robust as the best systems available in the literature, and significantly more accurate. Notably, our stereo-inertial SLAM achieves an average accuracy of 3.6 cm on the EuRoC drone and 9 mm under quick hand-held motions in the room of TUM-VI dataset, a setting representative of AR/VR scenarios. For the benefit of the community we make public the source code.

## 개요
본 논문은 핀홀 및 어안 렌즈 모델을 사용하여 단안, 스테레오 및 RGB-D 카메라로 비주얼, 비주얼-관성 및 다중 맵 SLAM을 수행할 수 있는 최초의 시스템인 ORB-SLAM3를 제시합니다. 첫 번째 주요 혁신은 IMU 초기화 단계에서도 완전히 최대 사후 확률(MAP) 추정에 의존하는 특징 기반의 긴밀하게 통합된 비주얼-관성 SLAM 시스템입니다. 그 결과, 실시간으로 소규모 및 대규모, 실내 및 실외 환경에서 강건하게 작동하며, 이전 접근 방식보다 2~5배 더 정확한 시스템이 탄생했습니다. 두 번째 주요 혁신은 개선된 재현율을 가진 새로운 위치 인식 방법에 의존하는 다중 맵 시스템입니다. 이를 통해 ORB-SLAM3는 시각 정보가 부족한 긴 기간을 견딜 수 있습니다: 길을 잃으면 새로운 맵을 시작하고, 매핑된 영역을 재방문할 때 이전 맵과 원활하게 병합됩니다. 지난 몇 초의 정보만 사용하는 시각적 오도메트리 시스템과 비교하여, ORB-SLAM3는 모든 알고리즘 단계에서 모든 이전 정보를 재사용할 수 있는 최초의 시스템입니다. 이를 통해 번들 조정에 공동 가시 키프레임을 포함할 수 있으며, 이는 시간적으로 크게 떨어져 있거나 이전 매핑 세션에서 온 경우에도 높은 시차 관측을 제공하여 정확도를 향상시킵니다. 우리의 실험은 모든 센서 구성에서 ORB-SLAM3가 문헌에서 사용 가능한 최고의 시스템만큼 강건하며, 훨씬 더 정확함을 보여줍니다. 특히, 우리의 스테레오-관성 SLAM은 AR/VR 시나리오를 대표하는 설정인 TUM-VI 데이터셋의 방에서 EuRoC 드론에서 평균 정확도 3.6cm, 빠른 손 동작에서 9mm를 달성합니다. 커뮤니티의 이익을 위해 소스 코드를 공개합니다.

## 핵심 내용
본 논문은 핀홀 및 어안 렌즈 모델을 사용하여 단안, 스테레오 및 RGB-D 카메라로 비주얼, 비주얼-관성 및 다중 맵 SLAM을 수행할 수 있는 최초의 시스템인 ORB-SLAM3를 제시합니다. 첫 번째 주요 혁신은 IMU 초기화 단계에서도 완전히 최대 사후 확률(MAP) 추정에 의존하는 특징 기반의 긴밀하게 통합된 비주얼-관성 SLAM 시스템입니다. 그 결과, 실시간으로 소규모 및 대규모, 실내 및 실외 환경에서 강건하게 작동하며, 이전 접근 방식보다 2~5배 더 정확한 시스템이 탄생했습니다. 두 번째 주요 혁신은 개선된 재현율을 가진 새로운 위치 인식 방법에 의존하는 다중 맵 시스템입니다. 이를 통해 ORB-SLAM3는 시각 정보가 부족한 긴 기간을 견딜 수 있습니다: 길을 잃으면 새로운 맵을 시작하고, 매핑된 영역을 재방문할 때 이전 맵과 원활하게 병합됩니다. 지난 몇 초의 정보만 사용하는 시각적 오도메트리 시스템과 비교하여, ORB-SLAM3는 모든 알고리즘 단계에서 모든 이전 정보를 재사용할 수 있는 최초의 시스템입니다. 이를 통해 번들 조정에 공동 가시 키프레임을 포함할 수 있으며, 이는 시간적으로 크게 떨어져 있거나 이전 매핑 세션에서 온 경우에도 높은 시차 관측을 제공하여 정확도를 향상시킵니다. 우리의 실험은 모든 센서 구성에서 ORB-SLAM3가 문헌에서 사용 가능한 최고의 시스템만큼 강건하며, 훨씬 더 정확함을 보여줍니다. 특히, 우리의 스테레오-관성 SLAM은 AR/VR 시나리오를 대표하는 설정인 TUM-VI 데이터셋의 방에서 EuRoC 드론에서 평균 정확도 3.6cm, 빠른 손 동작에서 9mm를 달성합니다. 커뮤니티의 이익을 위해 소스 코드를 공개합니다.
