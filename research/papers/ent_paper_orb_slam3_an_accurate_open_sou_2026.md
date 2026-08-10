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
  zh: ORB-SLAM3 是首个支持单目、双目、RGB-D 相机及针孔与鱼眼模型的视觉、视觉-惯性及多地图 SLAM 系统。其核心贡献在于基于最大后验估计的紧耦合视觉-惯性 SLAM 与创新的多地图融合机制，在 EuRoC 数据集上达到
    3.6 cm 精度，在 TUM-VI 数据集上达到 9 mm 精度，显著优于此前方法。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2007.11898v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (619 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: 'ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multi-Map SLAM project page'
  url: https://github.com/UZ-SLAMLab/ORB_SLAM3
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
该工作由 2026 年发布，面向人形机器人状态估计。系统首次在 IMU 初始化阶段即完全依赖 MAP 估计，实现实时鲁棒运行，精度较此前方法提升 2 至 5 倍。多地图系统通过改进的回环检测方法，能在视觉信息长期退化时创建新地图，并在重访区域时无缝合并，从而在算法全阶段复用历史信息，包括时间跨度大或来自先前建图会话的共视关键帧。

## 核心内容
### 方法架构
- **传感器支持**：单目、双目、RGB-D 相机，兼容针孔与鱼眼镜头模型。
- **视觉-惯性 SLAM**：基于特征点的紧耦合系统，IMU 初始化阶段即采用 MAP 估计，而非传统分步初始化。
- **多地图系统**：通过改进的回环检测方法（提升召回率），在跟踪丢失时自动创建新地图，重访已建图区域时无缝合并。

### 实验设置与关键数字
- **精度对比**：在所有传感器配置下，精度较此前方法提升 2 至 5 倍。
- **EuRoC 数据集**：双目-惯性 SLAM 平均精度达 3.6 cm（无人机场景）。
- **TUM-VI 数据集**：快速手持运动下精度达 9 mm（AR/VR 典型场景）。
- **鲁棒性**：与文献中最佳系统相当，且显著更准确。

### 结论
ORB-SLAM3 是首个能在算法全阶段复用历史信息的 SLAM 系统，包括时间分离或来自先前建图会话的共视关键帧，从而在高视差观测中提升精度。源代码已开源供社区使用。

## Overview
This paper presents ORB-SLAM3, the first system able to perform visual, visual-inertial and multi-map SLAM with monocular, stereo and RGB-D cameras, using pin-hole and fisheye lens models. The first main novelty is a feature-based tightly-integrated visual-inertial SLAM system that fully relies on Maximum-a-Posteriori (MAP) estimation, even during the IMU initialization phase. The result is a system that operates robustly in real-time, in small and large, indoor and outdoor environments, and is 2 to 5 times more accurate than previous approaches. The second main novelty is a multiple map system that relies on a new place recognition method with improved recall. Thanks to it, ORB-SLAM3 is able to survive to long periods of poor visual information: when it gets lost, it starts a new map that will be seamlessly merged with previous maps when revisiting mapped areas. Compared with visual odometry systems that only use information from the last few seconds, ORB-SLAM3 is the first system able to reuse in all the algorithm stages all previous information. This allows to include in bundle adjustment co-visible keyframes, that provide high parallax observations boosting accuracy, even if they are widely separated in time or if they come from a previous mapping session. Our experiments show that, in all sensor configurations, ORB-SLAM3 is as robust as the best systems available in the literature, and significantly more accurate. Notably, our stereo-inertial SLAM achieves an average accuracy of 3.6 cm on the EuRoC drone and 9 mm under quick hand-held motions in the room of TUM-VI dataset, a setting representative of AR/VR scenarios. For the benefit of the community we make public the source code.

## 参考
- http://arxiv.org/abs/2007.11898v2

## 개요
이 연구는 2026년에 발표되었으며, 휴머노이드 로봇 상태 추정을 대상으로 한다. 이 시스템은 처음으로 IMU 초기화 단계에서 완전히 MAP 추정에 의존하여 실시간으로 강건하게 동작하며, 정확도가 기존 방법보다 2~5배 향상되었다. 다중 맵 시스템은 개선된 루프 폐쇄 감지 방법을 통해 시각 정보가 장기간 저하되는 상황에서도 새 맵을 생성하고, 재방문 영역에서는 매끄럽게 병합하여 알고리즘 전 단계에서 과거 정보를 재사용한다. 여기에는 시간 간격이 크거나 이전 매핑 세션에서 얻은 공동 관측 키프레임도 포함된다.

## 핵심 내용
### 방법 아키텍처
- **센서 지원**: 단안, 스테레오, RGB-D 카메라를 지원하며, 핀홀 및 어안 렌즈 모델과 호환된다.
- **시각-관성 SLAM**: 특징점 기반의 긴밀하게 결합된 시스템으로, IMU 초기화 단계에서 전통적인 단계별 초기화 대신 MAP 추정을 사용한다.
- **다중 맵 시스템**: 개선된 루프 폐쇄 감지 방법(재현율 향상)을 통해 추적 손실 시 자동으로 새 맵을 생성하고, 이미 매핑된 영역을 재방문할 때 매끄럽게 병합한다.

### 실험 설정 및 주요 수치
- **정확도 비교**: 모든 센서 구성에서 기존 방법보다 정확도가 2~5배 향상되었다.
- **EuRoC 데이터셋**: 스테레오-관성 SLAM 평균 정확도 3.6 cm (드론 시나리오).
- **TUM-VI 데이터셋**: 빠른 손 동작에서 정확도 9 mm (AR/VR 일반 시나리오).
- **강건성**: 문헌의 최고 시스템과 동등하며, 현저히 더 정확하다.

### 결론
ORB-SLAM3는 알고리즘 전 단계에서 과거 정보를 재사용할 수 있는 최초의 SLAM 시스템으로, 시간적으로 분리되거나 이전 매핑 세션에서 얻은 공동 관측 키프레임을 포함하여 높은 시차 관측에서 정확도를 향상시킨다. 소스 코드는 커뮤니티 사용을 위해 오픈소스로 공개되었다.
