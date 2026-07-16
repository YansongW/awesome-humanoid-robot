---
$id: ent_paper_kimera_an_open_source_library_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Kimera: an Open-Source Library for Real-Time Metric-Semantic Localization and Mapping'
  zh: 'Kimera: an Open-Source Library for Real-Time Metric-Semantic Localization and Mapping'
  ko: 'Kimera: an Open-Source Library for Real-Time Metric-Semantic Localization and Mapping'
summary:
  en: 'Kimera: an Open-Source Library for Real-Time Metric-Semantic Localization and Mapping is a 2026 work on state estimation
    for humanoid robots.'
  zh: 'Kimera: an Open-Source Library for Real-Time Metric-Semantic Localization and Mapping is a 2026 work on state estimation
    for humanoid robots.'
  ko: 'Kimera: an Open-Source Library for Real-Time Metric-Semantic Localization and Mapping is a 2026 work on state estimation
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
- kimera
- slam
- state_estimation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1910.02490v3.
sources:
- id: src_001
  type: website
  title: 'Kimera: an Open-Source Library for Real-Time Metric-Semantic Localization and Mapping project page'
  url: https://github.com/MIT-SPARK/Kimera
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
We provide an open-source C++ library for real-time metric-semantic visual-inertial Simultaneous Localization And Mapping (SLAM). The library goes beyond existing visual and visual-inertial SLAM libraries (e.g., ORB-SLAM, VINS- Mono, OKVIS, ROVIO) by enabling mesh reconstruction and semantic labeling in 3D. Kimera is designed with modularity in mind and has four key components: a visual-inertial odometry (VIO) module for fast and accurate state estimation, a robust pose graph optimizer for global trajectory estimation, a lightweight 3D mesher module for fast mesh reconstruction, and a dense 3D metric-semantic reconstruction module. The modules can be run in isolation or in combination, hence Kimera can easily fall back to a state-of-the-art VIO or a full SLAM system. Kimera runs in real-time on a CPU and produces a 3D metric-semantic mesh from semantically labeled images, which can be obtained by modern deep learning methods. We hope that the flexibility, computational efficiency, robustness, and accuracy afforded by Kimera will build a solid basis for future metric-semantic SLAM and perception research, and will allow researchers across multiple areas (e.g., VIO, SLAM, 3D reconstruction, segmentation) to benchmark and prototype their own efforts without having to start from scratch.

## 核心内容
We provide an open-source C++ library for real-time metric-semantic visual-inertial Simultaneous Localization And Mapping (SLAM). The library goes beyond existing visual and visual-inertial SLAM libraries (e.g., ORB-SLAM, VINS- Mono, OKVIS, ROVIO) by enabling mesh reconstruction and semantic labeling in 3D. Kimera is designed with modularity in mind and has four key components: a visual-inertial odometry (VIO) module for fast and accurate state estimation, a robust pose graph optimizer for global trajectory estimation, a lightweight 3D mesher module for fast mesh reconstruction, and a dense 3D metric-semantic reconstruction module. The modules can be run in isolation or in combination, hence Kimera can easily fall back to a state-of-the-art VIO or a full SLAM system. Kimera runs in real-time on a CPU and produces a 3D metric-semantic mesh from semantically labeled images, which can be obtained by modern deep learning methods. We hope that the flexibility, computational efficiency, robustness, and accuracy afforded by Kimera will build a solid basis for future metric-semantic SLAM and perception research, and will allow researchers across multiple areas (e.g., VIO, SLAM, 3D reconstruction, segmentation) to benchmark and prototype their own efforts without having to start from scratch.

## 参考
- http://arxiv.org/abs/1910.02490v3

## Overview
We provide an open-source C++ library for real-time metric-semantic visual-inertial Simultaneous Localization And Mapping (SLAM). The library goes beyond existing visual and visual-inertial SLAM libraries (e.g., ORB-SLAM, VINS-Mono, OKVIS, ROVIO) by enabling mesh reconstruction and semantic labeling in 3D. Kimera is designed with modularity in mind and has four key components: a visual-inertial odometry (VIO) module for fast and accurate state estimation, a robust pose graph optimizer for global trajectory estimation, a lightweight 3D mesher module for fast mesh reconstruction, and a dense 3D metric-semantic reconstruction module. The modules can be run in isolation or in combination, hence Kimera can easily fall back to a state-of-the-art VIO or a full SLAM system. Kimera runs in real-time on a CPU and produces a 3D metric-semantic mesh from semantically labeled images, which can be obtained by modern deep learning methods. We hope that the flexibility, computational efficiency, robustness, and accuracy afforded by Kimera will build a solid basis for future metric-semantic SLAM and perception research, and will allow researchers across multiple areas (e.g., VIO, SLAM, 3D reconstruction, segmentation) to benchmark and prototype their own efforts without having to start from scratch.

## Content
We provide an open-source C++ library for real-time metric-semantic visual-inertial Simultaneous Localization And Mapping (SLAM). The library goes beyond existing visual and visual-inertial SLAM libraries (e.g., ORB-SLAM, VINS-Mono, OKVIS, ROVIO) by enabling mesh reconstruction and semantic labeling in 3D. Kimera is designed with modularity in mind and has four key components: a visual-inertial odometry (VIO) module for fast and accurate state estimation, a robust pose graph optimizer for global trajectory estimation, a lightweight 3D mesher module for fast mesh reconstruction, and a dense 3D metric-semantic reconstruction module. The modules can be run in isolation or in combination, hence Kimera can easily fall back to a state-of-the-art VIO or a full SLAM system. Kimera runs in real-time on a CPU and produces a 3D metric-semantic mesh from semantically labeled images, which can be obtained by modern deep learning methods. We hope that the flexibility, computational efficiency, robustness, and accuracy afforded by Kimera will build a solid basis for future metric-semantic SLAM and perception research, and will allow researchers across multiple areas (e.g., VIO, SLAM, 3D reconstruction, segmentation) to benchmark and prototype their own efforts without having to start from scratch.

## 개요
우리는 실시간 메트릭-시맨틱 시각-관성 동시 위치 추정 및 매핑(SLAM)을 위한 오픈소스 C++ 라이브러리를 제공합니다. 이 라이브러리는 기존의 시각 및 시각-관성 SLAM 라이브러리(예: ORB-SLAM, VINS-Mono, OKVIS, ROVIO)를 넘어 3D 메시 재구성 및 시맨틱 레이블링을 가능하게 합니다. Kimera는 모듈성을 염두에 두고 설계되었으며, 네 가지 핵심 구성 요소로 이루어져 있습니다: 빠르고 정확한 상태 추정을 위한 시각-관성 오도메트리(VIO) 모듈, 전역 궤적 추정을 위한 강건한 포즈 그래프 최적화기, 빠른 메시 재구성을 위한 경량 3D 메셔 모듈, 그리고 밀집 3D 메트릭-시맨틱 재구성 모듈입니다. 이 모듈들은 개별적으로 또는 조합하여 실행될 수 있으므로, Kimera는 최첨단 VIO 또는 전체 SLAM 시스템으로 쉽게 전환할 수 있습니다. Kimera는 CPU에서 실시간으로 실행되며, 현대 딥러닝 방법으로 얻을 수 있는 시맨틱 레이블링된 이미지로부터 3D 메트릭-시맨틱 메시를 생성합니다. 우리는 Kimera가 제공하는 유연성, 계산 효율성, 강건성 및 정확성이 미래의 메트릭-시맨틱 SLAM 및 인식 연구를 위한 견고한 기반을 구축하고, 여러 분야(예: VIO, SLAM, 3D 재구성, 세그멘테이션)의 연구자들이 처음부터 시작하지 않고도 자신의 작업을 벤치마킹하고 프로토타입을 만들 수 있게 해주기를 바랍니다.

## 핵심 내용
우리는 실시간 메트릭-시맨틱 시각-관성 동시 위치 추정 및 매핑(SLAM)을 위한 오픈소스 C++ 라이브러리를 제공합니다. 이 라이브러리는 기존의 시각 및 시각-관성 SLAM 라이브러리(예: ORB-SLAM, VINS-Mono, OKVIS, ROVIO)를 넘어 3D 메시 재구성 및 시맨틱 레이블링을 가능하게 합니다. Kimera는 모듈성을 염두에 두고 설계되었으며, 네 가지 핵심 구성 요소로 이루어져 있습니다: 빠르고 정확한 상태 추정을 위한 시각-관성 오도메트리(VIO) 모듈, 전역 궤적 추정을 위한 강건한 포즈 그래프 최적화기, 빠른 메시 재구성을 위한 경량 3D 메셔 모듈, 그리고 밀집 3D 메트릭-시맨틱 재구성 모듈입니다. 이 모듈들은 개별적으로 또는 조합하여 실행될 수 있으므로, Kimera는 최첨단 VIO 또는 전체 SLAM 시스템으로 쉽게 전환할 수 있습니다. Kimera는 CPU에서 실시간으로 실행되며, 현대 딥러닝 방법으로 얻을 수 있는 시맨틱 레이블링된 이미지로부터 3D 메트릭-시맨틱 메시를 생성합니다. 우리는 Kimera가 제공하는 유연성, 계산 효율성, 강건성 및 정확성이 미래의 메트릭-시맨틱 SLAM 및 인식 연구를 위한 견고한 기반을 구축하고, 여러 분야(예: VIO, SLAM, 3D 재구성, 세그멘테이션)의 연구자들이 처음부터 시작하지 않고도 자신의 작업을 벤치마킹하고 프로토타입을 만들 수 있게 해주기를 바랍니다.
