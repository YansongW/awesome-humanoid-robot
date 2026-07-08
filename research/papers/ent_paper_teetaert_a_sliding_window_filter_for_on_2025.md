---
$id: ent_paper_teetaert_a_sliding_window_filter_for_on_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Sliding-Window Filter for Online Continuous-Time Continuum Robot State Estimation
  zh: 用于在线连续时间连续体机器人状态估计的滑动窗口滤波器
  ko: 온라인 연속시간 연속체 로봇 상태 추정을 위한 슬라이딩 윈도우 필터
summary:
  en: This paper proposes a continuous-time sliding-window filter for probabilistic
    online state estimation of continuum robots, using factor-graph marginalization
    and Gauss-Newton optimization to achieve faster-than-real-time accuracy comparable
    to batch smoothers on a tendon-driven continuum robot.
  zh: 本文提出了一种用于连续体机器人概率在线状态估计的连续时间滑动窗口滤波器，利用因子图边缘化和高斯-牛顿优化，在肌腱驱动连续体机器人上实现了比实时更快且接近批量平滑器精度的估计。
  ko: 본 논문은 인대 구동 연속체 로봇에서 실시간보다 빠르고 배치 스무더에 필적하는 정확도를 달성하기 위해 요인 그래프 주변화와 가우스-뉴턴
    최적화를 활용한 연속시간 슬라이딩 윈도우 필터를 제안한다.
domains:
- 07_ai_models_algorithms
- 06_design_engineering
- 02_components
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- state_estimation
- continuum_robot
- sliding_window_filter
- factor_graph
- tendon_driven_robot
- online_estimation
- gauss_newton
- marginalization
- uncertainty_quantification
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from provided metadata; full paper text was not independently
    read. Human review is required before marking verified.
sources:
- id: src_001
  type: paper
  title: A Sliding-Window Filter for Online Continuous-Time Continuum Robot State
    Estimation
  url: https://arxiv.org/abs/2510.26623
  date: '2025'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

Continuum robots (CRs) introduce unique state-estimation challenges because their flexible, continuously deformable bodies require methods that balance accuracy and computational efficiency. Existing recursive filters for CRs run at measurement rate and are computationally cheap but less accurate, while batch smoothers are accurate but not suited to online operation. Prior sliding-window approaches for CRs were limited to discrete-time approximations and lacked stochastic representations, and existing continuous-time estimators were restricted to offline use. This paper closes that gap by presenting the first stochastic, continuous-time sliding-window filter specifically designed for continuum robots.

The proposed method formulates the estimation problem as a factor graph over a fixed temporal window of continuous-time states. Old states are marginalized out in information form using the Schur complement, yielding marginalization factors that preserve information from outside the window while keeping the active state size bounded. The maximum-a-posteriori (MAP) problem is solved with iterative Gauss-Newton linearization, enabling the filter to run faster than real time on commodity hardware.

The approach is validated on a real tendon-driven continuum robot using asynchronous tip-pose measurements from electromagnetic sensors and gyroscope measurements from units mounted at the midpoint and tip. Ground-truth comparisons against a Vicon motion-capture system show that even small window sizes of approximately 0.1 s substantially improve accuracy over a pure recursive filter while remaining real-time capable.

## Key Contributions

- First probabilistic sliding-window filter specifically designed for continuous-time continuum-robot state estimation.
- Enables online operation of continuous-time estimation at faster-than-real-time speeds with accuracy comparable to batch methods.
- Formulates marginalization factors that preserve information from outside the active window while maintaining a bounded state size.
- Validates the approach on a real tendon-driven continuum robot with asynchronous tip-pose and gyroscope measurements.
- Demonstrates that even small window sizes (≈0.1 s) substantially improve accuracy over a pure filter while remaining real-time capable.

## Relevance to Humanoid Robotics

Humanoid robots increasingly rely on soft or compliant joints, continuum-style limbs, cable-driven actuation, and other flexible structures to improve safety and dexterity. Accurate, uncertainty-aware, online state estimation for these flexible subsystems is essential for closed-loop control, contact reasoning, and robust behavior in unstructured environments. The continuous-time sliding-window formulation developed in this paper is directly relevant because it provides stochastic state estimates at speeds compatible with real-time humanoid control, bridging the gap between fast recursive filters and accurate batch smoothers. Its validation on a real tendon-driven continuum robot further demonstrates that the method can handle the kinds of compliant, cable-driven structures that are becoming common in advanced humanoid designs.
