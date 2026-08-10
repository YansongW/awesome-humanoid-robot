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
  zh: 本文提出一种基于粒子滤波的GNSS定位方法，通过分析伪距残差检测并排除非视距多径信号，以提升城市峡谷环境中移动机器人的定位精度。该方法由研究团队通过真实城市环境实验验证，核心贡献在于利用马氏距离计算似然估计，有效解决了多径干扰下的定位难题。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2401.08054v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (580 chars, DeepSeek).'
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
针对城市环境中建筑物遮挡导致的GNSS多径信号（即非视距NLOS信号）引发的大幅定位误差，本文提出一种新型定位技术。核心思路是通过分析伪距残差，仅使用视距LOS信号计算用户位置假设的似然值，从而排除NLOS信号干扰。为解决伪距残差计算前需先确定位置的矛盾，研究引入粒子滤波器，并采用马氏距离衡量仅由LOS伪距计算的位置假设与粒子之间的差异。真实城市峡谷环境中的定位实验表明，该方法能显著提升移动机器人在复杂城市场景下的定位准确性。

## 核心内容
### 方法架构
- 采用粒子滤波器作为核心框架，每个粒子代表一个位置假设。
- 通过分析GNSS伪距残差，识别并排除非视距NLOS多径信号。
- 提出基于马氏距离的似然估计方法，计算仅由LOS伪距推导的位置假设与粒子之间的相似度。

### 实验设置
- 在真实城市峡谷环境中进行定位测试，该环境存在大量建筑物遮挡，易产生多径信号。
- 对比传统GNSS定位方法，验证新技术的有效性。

### 关键结果
- 实验证明，该方法能有效抑制NLOS信号造成的定位误差，在城市峡谷中实现更精确的位置估计。
- 通过排除多径信号，定位精度显著优于未处理多径干扰的常规方法。

### 结论
本文提出的基于伪距残差分析与粒子滤波的GNSS定位方法，为移动机器人在复杂城市环境中的可靠导航提供了有效解决方案。

## Overview
This paper proposes a novel positioning technique suitable for use in mobile robots in urban environments in which large global navigation satellite system (GNSS) positioning errors occur because of multipath signals. During GNSS positioning, the GNSS satellites that are obstructed by buildings emit reflection and diffraction signals, which are called non-line-of-sight (NLOS) multipath signals. These multipath signals cause major positioning errors. The key concept considered in this paper is the estimation of a user's position using the likelihood of the position hypotheses computed from the GNSS pseudoranges, consisting only of LOS signals based on the analysis of the pseudorange residuals. To determine the NLOS GNSS signals from the pseudorange residuals at the user's position, it is necessary to accurately determine the position before the computation of the pseudorange residuals. This problem is solved using a particle filter. We propose a likelihood estimation method using the Mahalanobis distance between the hypotheses of the user's position computed from only the LOS pseudoranges and the particles. To confirm the effectiveness of the proposed technique, a positioning test was performed in a real-world urban environment. The results demonstrated that the proposed method is effective for accurately estimating the user's position in urban canyons.

## 参考
- http://arxiv.org/abs/2401.08054v1

## 개요
도시 환경에서 건물에 의한 차폐로 발생하는 GNSS 다중경로 신호(즉, 비가시거리 NLOS 신호)로 인한 큰 위치 오차를 해결하기 위해, 본 논문은 새로운 측위 기술을 제안한다. 핵심 아이디어는 의사거리 잔차를 분석하여 가시거리 LOS 신호만을 사용해 사용자 위치 가설의 우도 값을 계산함으로써 NLOS 신호 간섭을 배제하는 것이다. 의사거리 잔차 계산 전에 위치를 먼저 결정해야 하는 모순을 해결하기 위해, 연구는 입자 필터를 도입하고 마할라노비스 거리를 사용하여 LOS 의사거리만으로 계산된 위치 가설과 입자 간의 차이를 측정한다. 실제 도시 협곡 환경에서의 측위 실험은 이 방법이 복잡한 도시 환경에서 이동 로봇의 측위 정확도를 크게 향상시킬 수 있음을 보여준다.

## 핵심 내용
### 방법 구조
- 입자 필터를 핵심 프레임워크로 사용하며, 각 입자는 위치 가설을 나타낸다.
- GNSS 의사거리 잔차를 분석하여 비가시거리 NLOS 다중경로 신호를 식별하고 배제한다.
- 마할라노비스 거리 기반의 우도 추정 방법을 제안하여, LOS 의사거리만으로 도출된 위치 가설과 입자 간의 유사도를 계산한다.

### 실험 설정
- 다수의 건물 차폐로 다중경로 신호가 발생하기 쉬운 실제 도시 협곡 환경에서 측위 테스트를 수행한다.
- 기존 GNSS 측위 방법과 비교하여 새 기술의 유효성을 검증한다.

### 주요 결과
- 실험 결과, 이 방법이 NLOS 신호로 인한 측위 오차를 효과적으로 억제하여 도시 협곡에서 더 정확한 위치 추정을 달성함을 입증한다.
- 다중경로 신호를 배제함으로써, 측위 정확도는 다중경로 간섭을 처리하지 않은 일반 방법보다 크게 우수하다.

### 결론
본 논문에서 제안한 의사거리 잔차 분석과 입자 필터 기반의 GNSS 측위 방법은 복잡한 도시 환경에서 이동 로봇의 신뢰할 수 있는 내비게이션을 위한 효과적인 솔루션을 제공한다.
