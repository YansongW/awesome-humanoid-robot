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
  en: This paper proposes a particle-filter-based GNSS localization method that detects and excludes non-line-of-sight multipath
    signals by analyzing pseudorange residuals, and validates the approach through real-world urban-canyon experiments.
  zh: 本文提出了一种基于粒子滤波的GNSS定位方法，通过分析伪距残差检测并排除非视距多路径信号，并在真实城市峡谷环境中验证了该方法。
  ko: 본 논문은 유사거리 잔차를 분석하여 비시각 다중경로 신호를 검출하고 제외하는 입자 필터 기반 GNSS 위치 추정 방법을 제안하고 실제 도심 환경에서 검증하였다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2401.08054v1.
sources:
- id: src_001
  type: paper
  title: Mobile Robot Localization with GNSS Multipath Detection using Pseudorange Residuals
  url: https://arxiv.org/abs/2401.08054
  date: '2019'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
This paper proposes a novel positioning technique suitable for use in mobile robots in urban environments in which large global navigation satellite system (GNSS) positioning errors occur because of multipath signals. During GNSS positioning, the GNSS satellites that are obstructed by buildings emit reflection and diffraction signals, which are called non-line-of-sight (NLOS) multipath signals. These multipath signals cause major positioning errors. The key concept considered in this paper is the estimation of a user's position using the likelihood of the position hypotheses computed from the GNSS pseudoranges, consisting only of LOS signals based on the analysis of the pseudorange residuals. To determine the NLOS GNSS signals from the pseudorange residuals at the user's position, it is necessary to accurately determine the position before the computation of the pseudorange residuals. This problem is solved using a particle filter. We propose a likelihood estimation method using the Mahalanobis distance between the hypotheses of the user's position computed from only the LOS pseudoranges and the particles. To confirm the effectiveness of the proposed technique, a positioning test was performed in a real-world urban environment. The results demonstrated that the proposed method is effective for accurately estimating the user's position in urban canyons.

## 核心内容
This paper proposes a novel positioning technique suitable for use in mobile robots in urban environments in which large global navigation satellite system (GNSS) positioning errors occur because of multipath signals. During GNSS positioning, the GNSS satellites that are obstructed by buildings emit reflection and diffraction signals, which are called non-line-of-sight (NLOS) multipath signals. These multipath signals cause major positioning errors. The key concept considered in this paper is the estimation of a user's position using the likelihood of the position hypotheses computed from the GNSS pseudoranges, consisting only of LOS signals based on the analysis of the pseudorange residuals. To determine the NLOS GNSS signals from the pseudorange residuals at the user's position, it is necessary to accurately determine the position before the computation of the pseudorange residuals. This problem is solved using a particle filter. We propose a likelihood estimation method using the Mahalanobis distance between the hypotheses of the user's position computed from only the LOS pseudoranges and the particles. To confirm the effectiveness of the proposed technique, a positioning test was performed in a real-world urban environment. The results demonstrated that the proposed method is effective for accurately estimating the user's position in urban canyons.

## 参考
- http://arxiv.org/abs/2401.08054v1

