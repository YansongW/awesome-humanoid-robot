---
$id: ent_paper_spark_a_toolbox_for_safe_human_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SPARK: A Toolbox for Safe Humanoid Autonomy and Teleoperation'
  zh: 'SPARK: A Toolbox for Safe Humanoid Autonomy and Teleoperation'
  ko: 'SPARK: A Toolbox for Safe Humanoid Autonomy and Teleoperation'
summary:
  en: 'SPARK: A Toolbox for Safe Humanoid Autonomy and Teleoperation is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  zh: 'SPARK: A Toolbox for Safe Humanoid Autonomy and Teleoperation is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  ko: 'SPARK: A Toolbox for Safe Humanoid Autonomy and Teleoperation is a 2025 work on loco-manipulation and whole-body-control
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
- loco_manipulation
- spark
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.03132v3.
sources:
- id: src_001
  type: paper
  title: 'SPARK: A Toolbox for Safe Humanoid Autonomy and Teleoperation (arXiv)'
  url: https://arxiv.org/abs/2502.03132
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'SPARK: A Toolbox for Safe Humanoid Autonomy and Teleoperation project page'
  url: https://intelligent-control-lab.github.io/spark/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
This paper introduces the Safe Protective and Assistive Robot Kit (SPARK), a comprehensive benchmark designed to ensure safety in humanoid autonomy and teleoperation. Humanoid robots pose significant safety risks due to their physical capabilities of interacting with complex environments. The physical structures of humanoid robots further add complexity to the design of general safety solutions. To facilitate safe deployment of complex robot systems, SPARK can be used as a toolbox that comes with state-of-the-art safe control algorithms in a modular and composable robot control framework. Users can easily configure safety criteria and sensitivity levels to optimize the balance between safety and performance. To accelerate humanoid safety research and development, SPARK provides simulation benchmarks that compare safety approaches in a variety of environments, tasks, and robot models. Furthermore, SPARK allows quick deployment of synthesized safe controllers on real robots. For hardware deployment, SPARK supports Apple Vision Pro (AVP) or a Motion Capture System as external sensors, while offering interfaces for seamless integration with alternative hardware setups at the same time. This paper demonstrates SPARK's capability with both simulation experiments and case studies with a Unitree G1 humanoid robot. Leveraging these advantages of SPARK, users and researchers can significantly improve the safety of their humanoid systems as well as accelerate relevant research. The open source code is available at: https://github.com/intelligent-control-lab/spark.

## 核心内容
This paper introduces the Safe Protective and Assistive Robot Kit (SPARK), a comprehensive benchmark designed to ensure safety in humanoid autonomy and teleoperation. Humanoid robots pose significant safety risks due to their physical capabilities of interacting with complex environments. The physical structures of humanoid robots further add complexity to the design of general safety solutions. To facilitate safe deployment of complex robot systems, SPARK can be used as a toolbox that comes with state-of-the-art safe control algorithms in a modular and composable robot control framework. Users can easily configure safety criteria and sensitivity levels to optimize the balance between safety and performance. To accelerate humanoid safety research and development, SPARK provides simulation benchmarks that compare safety approaches in a variety of environments, tasks, and robot models. Furthermore, SPARK allows quick deployment of synthesized safe controllers on real robots. For hardware deployment, SPARK supports Apple Vision Pro (AVP) or a Motion Capture System as external sensors, while offering interfaces for seamless integration with alternative hardware setups at the same time. This paper demonstrates SPARK's capability with both simulation experiments and case studies with a Unitree G1 humanoid robot. Leveraging these advantages of SPARK, users and researchers can significantly improve the safety of their humanoid systems as well as accelerate relevant research. The open source code is available at: https://github.com/intelligent-control-lab/spark.

## 参考
- http://arxiv.org/abs/2502.03132v3

## Overview
This paper introduces the Safe Protective and Assistive Robot Kit (SPARK), a comprehensive benchmark designed to ensure safety in humanoid autonomy and teleoperation. Humanoid robots pose significant safety risks due to their physical capabilities of interacting with complex environments. The physical structures of humanoid robots further add complexity to the design of general safety solutions. To facilitate safe deployment of complex robot systems, SPARK can be used as a toolbox that comes with state-of-the-art safe control algorithms in a modular and composable robot control framework. Users can easily configure safety criteria and sensitivity levels to optimize the balance between safety and performance. To accelerate humanoid safety research and development, SPARK provides simulation benchmarks that compare safety approaches in a variety of environments, tasks, and robot models. Furthermore, SPARK allows quick deployment of synthesized safe controllers on real robots. For hardware deployment, SPARK supports Apple Vision Pro (AVP) or a Motion Capture System as external sensors, while offering interfaces for seamless integration with alternative hardware setups at the same time. This paper demonstrates SPARK's capability with both simulation experiments and case studies with a Unitree G1 humanoid robot. Leveraging these advantages of SPARK, users and researchers can significantly improve the safety of their humanoid systems as well as accelerate relevant research. The open source code is available at: https://github.com/intelligent-control-lab/spark.

## Content
This paper introduces the Safe Protective and Assistive Robot Kit (SPARK), a comprehensive benchmark designed to ensure safety in humanoid autonomy and teleoperation. Humanoid robots pose significant safety risks due to their physical capabilities of interacting with complex environments. The physical structures of humanoid robots further add complexity to the design of general safety solutions. To facilitate safe deployment of complex robot systems, SPARK can be used as a toolbox that comes with state-of-the-art safe control algorithms in a modular and composable robot control framework. Users can easily configure safety criteria and sensitivity levels to optimize the balance between safety and performance. To accelerate humanoid safety research and development, SPARK provides simulation benchmarks that compare safety approaches in a variety of environments, tasks, and robot models. Furthermore, SPARK allows quick deployment of synthesized safe controllers on real robots. For hardware deployment, SPARK supports Apple Vision Pro (AVP) or a Motion Capture System as external sensors, while offering interfaces for seamless integration with alternative hardware setups at the same time. This paper demonstrates SPARK's capability with both simulation experiments and case studies with a Unitree G1 humanoid robot. Leveraging these advantages of SPARK, users and researchers can significantly improve the safety of their humanoid systems as well as accelerate relevant research. The open source code is available at: https://github.com/intelligent-control-lab/spark.

## 개요
본 논문에서는 휴머노이드 자율 및 원격 조작의 안전성을 보장하기 위해 설계된 포괄적인 벤치마크인 SPARK(Safe Protective and Assistive Robot Kit)를 소개합니다. 휴머노이드 로봇은 복잡한 환경과 상호작용하는 물리적 능력으로 인해 상당한 안전 위험을 초래합니다. 휴머노이드 로봇의 물리적 구조는 일반적인 안전 솔루션 설계에 추가적인 복잡성을 더합니다. 복잡한 로봇 시스템의 안전한 배치를 촉진하기 위해 SPARK는 모듈식 및 구성 가능한 로봇 제어 프레임워크 내에서 최첨단 안전 제어 알고리즘을 제공하는 툴박스로 사용될 수 있습니다. 사용자는 안전 기준과 민감도 수준을 쉽게 구성하여 안전과 성능 간의 균형을 최적화할 수 있습니다. 휴머노이드 안전 연구 및 개발을 가속화하기 위해 SPARK는 다양한 환경, 작업 및 로봇 모델에서 안전 접근 방식을 비교하는 시뮬레이션 벤치마크를 제공합니다. 또한 SPARK는 합성된 안전 컨트롤러를 실제 로봇에 신속하게 배치할 수 있도록 합니다. 하드웨어 배치를 위해 SPARK는 Apple Vision Pro(AVP) 또는 모션 캡처 시스템을 외부 센서로 지원하며, 동시에 대체 하드웨어 설정과의 원활한 통합을 위한 인터페이스를 제공합니다. 본 논문은 Unitree G1 휴머노이드 로봇을 사용한 시뮬레이션 실험과 사례 연구를 통해 SPARK의 성능을 입증합니다. SPARK의 이러한 장점을 활용하여 사용자와 연구자는 휴머노이드 시스템의 안전성을 크게 향상시키고 관련 연구를 가속화할 수 있습니다. 오픈 소스 코드는 다음에서 확인할 수 있습니다: https://github.com/intelligent-control-lab/spark.

## 핵심 내용
본 논문에서는 휴머노이드 자율 및 원격 조작의 안전성을 보장하기 위해 설계된 포괄적인 벤치마크인 SPARK(Safe Protective and Assistive Robot Kit)를 소개합니다. 휴머노이드 로봇은 복잡한 환경과 상호작용하는 물리적 능력으로 인해 상당한 안전 위험을 초래합니다. 휴머노이드 로봇의 물리적 구조는 일반적인 안전 솔루션 설계에 추가적인 복잡성을 더합니다. 복잡한 로봇 시스템의 안전한 배치를 촉진하기 위해 SPARK는 모듈식 및 구성 가능한 로봇 제어 프레임워크 내에서 최첨단 안전 제어 알고리즘을 제공하는 툴박스로 사용될 수 있습니다. 사용자는 안전 기준과 민감도 수준을 쉽게 구성하여 안전과 성능 간의 균형을 최적화할 수 있습니다. 휴머노이드 안전 연구 및 개발을 가속화하기 위해 SPARK는 다양한 환경, 작업 및 로봇 모델에서 안전 접근 방식을 비교하는 시뮬레이션 벤치마크를 제공합니다. 또한 SPARK는 합성된 안전 컨트롤러를 실제 로봇에 신속하게 배치할 수 있도록 합니다. 하드웨어 배치를 위해 SPARK는 Apple Vision Pro(AVP) 또는 모션 캡처 시스템을 외부 센서로 지원하며, 동시에 대체 하드웨어 설정과의 원활한 통합을 위한 인터페이스를 제공합니다. 본 논문은 Unitree G1 휴머노이드 로봇을 사용한 시뮬레이션 실험과 사례 연구를 통해 SPARK의 성능을 입증합니다. SPARK의 이러한 장점을 활용하여 사용자와 연구자는 휴머노이드 시스템의 안전성을 크게 향상시키고 관련 연구를 가속화할 수 있습니다. 오픈 소스 코드는 다음에서 확인할 수 있습니다: https://github.com/intelligent-control-lab/spark.
