---
$id: ent_paper_suzuki_mobile_robot_localization_with_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Mobile Robot Localization with GNSS Multipath Detection using Pseudorange Residuals
  zh: 基于伪距残差的GNSS多路径检测移动机器人定位
  ko: 유사거리 잔차를 이용한 GNSS 다중경로 검출 기반 이동 로봇 위치 추정
summary:
  en: This paper proposes a particle-filter-based GNSS localization method that detects
    and excludes non-line-of-sight multipath signals by analyzing pseudorange residuals,
    and validates the approach through real-world urban-canyon experiments.
  zh: 本文提出了一种基于粒子滤波的GNSS定位方法，通过分析伪距残差检测并排除非视距多路径信号，并在真实城市峡谷环境中验证了该方法。
  ko: 본 논문은 유사거리 잔차를 분석하여 비시각 다중경로 신호를 검출하고 제외하는 입자 필터 기반 GNSS 위치 추정 방법을 제안하고 실제 도심
    환경에서 검증하였다.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- gnss_localization
- multipath_detection
- nlos_mitigation
- particle_filter
- urban_navigation
- outdoor_localization
- pseudorange_residuals
- mahalanobis_distance
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from the supplied abstract and metadata. Exact section/page
    citations, numerical results, and hardware details require verification against
    the full paper.; approved by autonomous review workflow.
sources:
- id: src_001
  type: paper
  title: Mobile Robot Localization with GNSS Multipath Detection using Pseudorange
    Residuals
  url: https://arxiv.org/abs/2401.08054
  date: '2019'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

In urban canyon environments, GNSS signals from satellites obstructed by buildings arrive as reflections and diffractions known as non-line-of-sight (NLOS) multipath signals. These NLOS signals introduce large pseudorange errors and can severely degrade the localization accuracy of mobile robots and vehicles that rely on GNSS.

The proposed method addresses this problem by identifying NLOS signals from the pseudorange residuals at the user's position. Because residual computation requires an accurate position estimate, the authors use a particle filter to maintain a distribution of position hypotheses. Each particle's likelihood is evaluated using the Mahalanobis distance between the particle and position hypotheses computed from subsets of pseudoranges that are classified as line-of-sight (LOS). A motion model based on GNSS Doppler velocity measurements supports kinematic robot and vehicle applications.

Experimental validation was conducted in a real-world urban environment. The results show that the proposed technique reduces horizontal RMS positioning error from 19.4 m to 1.08 m compared with conventional GNSS positioning, demonstrating effective NLOS mitigation in multipath-rich urban canyons.

## Key Contributions

- NLOS multipath detection from pseudorange residuals without requiring 3D maps or external sensors.
- Particle filter likelihood estimation using the Mahalanobis distance between particles and LOS-only GNSS solutions.
- Motion model based on GNSS Doppler velocity measurements for kinematic mobile robots and vehicles.
- Real-world urban-canyon validation showing horizontal RMS error reduction from 19.4 m to 1.08 m.

## Relevance to Humanoid Robotics

Reliable outdoor localization is a foundational capability for deploying humanoid robots in real-world urban settings. Humanoid platforms operating on sidewalks, crosswalks, or public spaces need accurate global position estimates despite multipath-rich environments. The NLOS detection and particle-filter localization method presented in this paper can serve as an enabling navigation component for outdoor humanoid autonomy, improving safety and robustness in urban canyons where conventional GNSS alone fails.
