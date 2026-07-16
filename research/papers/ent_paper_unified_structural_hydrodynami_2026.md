---
$id: ent_paper_unified_structural_hydrodynami_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Unified Structural-Hydrodynamic Modeling of Underwater Underactuated Mechanisms and Soft Robots
  zh: Unified Structural-Hydrodynamic Modeling of Underwater Underactuated Mechanisms and Soft Robots
  ko: Unified Structural-Hydrodynamic Modeling of Underwater Underactuated Mechanisms and Soft Robots
summary:
  en: 'arXiv:2603.07939v2 Announce Type: replace Abstract: Underwater robots are widely deployed for ocean exploration and
    manipulation. Underactuated mechanisms are advantageous in aquatic environments because reducing actuator count lowers
    motor-leakage risk while introducing inherent mechanical compliance. However, accurate modeling of underwater underactuated
    and soft robotic systems remains challenging, as it requires identifying high-dimensional structural and hydrodynamic
    parameters. In this work, we propose a trajectory-driven global optimization framework for unified structural-hydrodynamic
    modeling of underwater multibody systems. Inspired by the Covariance Matrix Adaptation Evolution Strategy (CMA-ES), the
    proposed approach simultaneously identifies coupled elastic, damping, and distributed hydrodynamic parameters through
    trajectory-level matching between simulated and experimental motion. This enables high-fidelity reproduction of underactuated
    mechanisms and compliant soft robotic systems in underwater environments, using as little as a single video recording.
    We first validate the framework on a link-by-link underactuated multibody mechanism, demonstrating accurate identification
    of distributed hydrodynamic coefficients, with normalized end-effector position error below 5% across multiple trajectories,
    initial conditions, and both active-passive and fully passive configurations. The modeling strategy is further validated
    on an asymmetric octopus-inspired soft arm, confirming its effectiveness for compliant soft robotic systems. Finally,
    eight identified arms are assembled into a swimming octopus robot, where the unified parameter set enables realistic whole-body
    behavior without additional retuning. These results demonstrate the scalability and transferability of the proposed structural-hydrodynamic
    modeling framework across underwater underactuated and soft robotic systems.'
  zh: 'arXiv:2603.07939v2 Announce Type: replace Abstract: Underwater robots are widely deployed for ocean exploration and
    manipulation. Underactuated mechanisms are advantageous in aquatic environments because reducing actuator count lowers
    motor-leakage risk while introducing inherent mechanical compliance. However, accurate modeling of underwater underactuated
    and soft robotic systems remains challenging, as it requires identifying high-dimensional structural and hydrodynamic
    parameters. In this work, we propose a trajectory-driven global optimization framework for unified structural-hydrodynamic
    modeling of underwater multibody systems. Inspired by the Covariance Matrix Adaptation Evolution Strategy (CMA-ES), the
    proposed approach simultaneously identifies coupled elastic, damping, and distributed hydrodynamic parameters through
    trajectory-level matching between simulated and experimental motion. This enables high-fidelity reproduction of underactuated
    mechanisms and compliant soft robotic systems in underwater environments, using as little as a single video recording.
    We first validate the framework on a link-by-link underactuated multibody mechanism, demonstrating accurate identification
    of distributed hydrodynamic coefficients, with normalized end-effector position error below 5% across multiple trajectories,
    initial conditions, and both active-passive and fully passive configurations. The modeling strategy is further validated
    on an asymmetric octopus-inspired soft arm, confirming its effectiveness for compliant soft robotic systems. Finally,
    eight identified arms are assembled into a swimming octopus robot, where the unified parameter set enables realistic whole-body
    behavior without additional retuning. These results demonstrate the scalability and transferability of the proposed structural-hydrodynamic
    modeling framework across underwater underactuated and soft robotic systems.'
  ko: 'arXiv:2603.07939v2 Announce Type: replace Abstract: Underwater robots are widely deployed for ocean exploration and
    manipulation. Underactuated mechanisms are advantageous in aquatic environments because reducing actuator count lowers
    motor-leakage risk while introducing inherent mechanical compliance. However, accurate modeling of underwater underactuated
    and soft robotic systems remains challenging, as it requires identifying high-dimensional structural and hydrodynamic
    parameters. In this work, we propose a trajectory-driven global optimization framework for unified structural-hydrodynamic
    modeling of underwater multibody systems. Inspired by the Covariance Matrix Adaptation Evolution Strategy (CMA-ES), the
    proposed approach simultaneously identifies coupled elastic, damping, and distributed hydrodynamic parameters through
    trajectory-level matching between simulated and experimental motion. This enables high-fidelity reproduction of underactuated
    mechanisms and compliant soft robotic systems in underwater environments, using as little as a single video recording.
    We first validate the framework on a link-by-link underactuated multibody mechanism, demonstrating accurate identification
    of distributed hydrodynamic coefficients, with normalized end-effector position error below 5% across multiple trajectories,
    initial conditions, and both active-passive and fully passive configurations. The modeling strategy is further validated
    on an asymmetric octopus-inspired soft arm, confirming its effectiveness for compliant soft robotic systems. Finally,
    eight identified arms are assembled into a swimming octopus robot, where the unified parameter set enables realistic whole-body
    behavior without additional retuning. These results demonstrate the scalability and transferability of the proposed structural-hydrodynamic
    modeling framework across underwater underactuated and soft robotic systems.'
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
- unified_structural_hydrodynami
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.07939v2.
sources:
- id: src_001
  type: paper
  title: Unified Structural-Hydrodynamic Modeling of Underwater Underactuated Mechanisms and Soft Robots
  url: https://arxiv.org/abs/2603.07939
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Underwater robots are widely deployed for ocean exploration and manipulation. Underactuated mechanisms are advantageous in aquatic environments because reducing actuator count lowers motor-leakage risk while introducing inherent mechanical compliance. However, accurate modeling of underwater underactuated and soft robotic systems remains challenging, as it requires identifying high-dimensional structural and hydrodynamic parameters. In this work, we propose a trajectory-driven global optimization framework for unified structural-hydrodynamic modeling of underwater multibody systems. Inspired by the Covariance Matrix Adaptation Evolution Strategy (CMA-ES), the proposed approach simultaneously identifies coupled elastic, damping, and distributed hydrodynamic parameters through trajectory-level matching between simulated and experimental motion. This enables high-fidelity reproduction of underactuated mechanisms and compliant soft robotic systems in underwater environments, using as little as a single video recording. We first validate the framework on a link-by-link underactuated multibody mechanism, demonstrating accurate identification of distributed hydrodynamic coefficients, with normalized end-effector position error below 5% across multiple trajectories, initial conditions, and both active-passive and fully passive configurations. The modeling strategy is further validated on an asymmetric octopus-inspired soft arm, confirming its effectiveness for compliant soft robotic systems. Finally, eight identified arms are assembled into a swimming octopus robot, where the unified parameter set enables realistic whole-body behavior without additional retuning. These results demonstrate the scalability and transferability of the proposed structural-hydrodynamic modeling framework across underwater underactuated and soft robotic systems.

## 核心内容
Underwater robots are widely deployed for ocean exploration and manipulation. Underactuated mechanisms are advantageous in aquatic environments because reducing actuator count lowers motor-leakage risk while introducing inherent mechanical compliance. However, accurate modeling of underwater underactuated and soft robotic systems remains challenging, as it requires identifying high-dimensional structural and hydrodynamic parameters. In this work, we propose a trajectory-driven global optimization framework for unified structural-hydrodynamic modeling of underwater multibody systems. Inspired by the Covariance Matrix Adaptation Evolution Strategy (CMA-ES), the proposed approach simultaneously identifies coupled elastic, damping, and distributed hydrodynamic parameters through trajectory-level matching between simulated and experimental motion. This enables high-fidelity reproduction of underactuated mechanisms and compliant soft robotic systems in underwater environments, using as little as a single video recording. We first validate the framework on a link-by-link underactuated multibody mechanism, demonstrating accurate identification of distributed hydrodynamic coefficients, with normalized end-effector position error below 5% across multiple trajectories, initial conditions, and both active-passive and fully passive configurations. The modeling strategy is further validated on an asymmetric octopus-inspired soft arm, confirming its effectiveness for compliant soft robotic systems. Finally, eight identified arms are assembled into a swimming octopus robot, where the unified parameter set enables realistic whole-body behavior without additional retuning. These results demonstrate the scalability and transferability of the proposed structural-hydrodynamic modeling framework across underwater underactuated and soft robotic systems.

## 参考
- http://arxiv.org/abs/2603.07939v2

## Overview
Underwater robots are widely deployed for ocean exploration and manipulation. Underactuated mechanisms are advantageous in aquatic environments because reducing actuator count lowers motor-leakage risk while introducing inherent mechanical compliance. However, accurate modeling of underwater underactuated and soft robotic systems remains challenging, as it requires identifying high-dimensional structural and hydrodynamic parameters. In this work, we propose a trajectory-driven global optimization framework for unified structural-hydrodynamic modeling of underwater multibody systems. Inspired by the Covariance Matrix Adaptation Evolution Strategy (CMA-ES), the proposed approach simultaneously identifies coupled elastic, damping, and distributed hydrodynamic parameters through trajectory-level matching between simulated and experimental motion. This enables high-fidelity reproduction of underactuated mechanisms and compliant soft robotic systems in underwater environments, using as little as a single video recording. We first validate the framework on a link-by-link underactuated multibody mechanism, demonstrating accurate identification of distributed hydrodynamic coefficients, with normalized end-effector position error below 5% across multiple trajectories, initial conditions, and both active-passive and fully passive configurations. The modeling strategy is further validated on an asymmetric octopus-inspired soft arm, confirming its effectiveness for compliant soft robotic systems. Finally, eight identified arms are assembled into a swimming octopus robot, where the unified parameter set enables realistic whole-body behavior without additional retuning. These results demonstrate the scalability and transferability of the proposed structural-hydrodynamic modeling framework across underwater underactuated and soft robotic systems.

## Content
Underwater robots are widely deployed for ocean exploration and manipulation. Underactuated mechanisms are advantageous in aquatic environments because reducing actuator count lowers motor-leakage risk while introducing inherent mechanical compliance. However, accurate modeling of underwater underactuated and soft robotic systems remains challenging, as it requires identifying high-dimensional structural and hydrodynamic parameters. In this work, we propose a trajectory-driven global optimization framework for unified structural-hydrodynamic modeling of underwater multibody systems. Inspired by the Covariance Matrix Adaptation Evolution Strategy (CMA-ES), the proposed approach simultaneously identifies coupled elastic, damping, and distributed hydrodynamic parameters through trajectory-level matching between simulated and experimental motion. This enables high-fidelity reproduction of underactuated mechanisms and compliant soft robotic systems in underwater environments, using as little as a single video recording. We first validate the framework on a link-by-link underactuated multibody mechanism, demonstrating accurate identification of distributed hydrodynamic coefficients, with normalized end-effector position error below 5% across multiple trajectories, initial conditions, and both active-passive and fully passive configurations. The modeling strategy is further validated on an asymmetric octopus-inspired soft arm, confirming its effectiveness for compliant soft robotic systems. Finally, eight identified arms are assembled into a swimming octopus robot, where the unified parameter set enables realistic whole-body behavior without additional retuning. These results demonstrate the scalability and transferability of the proposed structural-hydrodynamic modeling framework across underwater underactuated and soft robotic systems.

## 개요
수중 로봇은 해양 탐사 및 조작을 위해 널리 사용됩니다. 저구동 메커니즘은 수중 환경에서 유리한데, 이는 액추에이터 수를 줄이면 모터 누출 위험을 낮추면서도 고유한 기계적 순응성을 도입하기 때문입니다. 그러나 수중 저구동 및 소프트 로봇 시스템의 정확한 모델링은 고차원의 구조적 및 유체역학적 매개변수를 식별해야 하므로 여전히 어려운 과제입니다. 본 연구에서는 수중 다물체 시스템의 통합 구조-유체역학 모델링을 위한 궤적 기반 전역 최적화 프레임워크를 제안합니다. 공분산 행렬 적응 진화 전략(CMA-ES)에서 영감을 받은 이 접근법은 시뮬레이션과 실험 운동 간의 궤적 수준 정합을 통해 결합된 탄성, 감쇠 및 분산 유체역학 매개변수를 동시에 식별합니다. 이를 통해 단일 비디오 녹화만으로도 수중 환경에서 저구동 메커니즘과 순응형 소프트 로봇 시스템의 고충실도 재현이 가능합니다. 먼저 링크별 저구동 다물체 메커니즘에서 프레임워크를 검증하여 분산 유체역학 계수의 정확한 식별을 입증했으며, 여러 궤적, 초기 조건, 능동-수동 및 완전 수동 구성에서 정규화된 말단 효과기 위치 오차가 5% 미만임을 확인했습니다. 모델링 전략은 비대칭 문어 모방 소프트 암에서 추가로 검증되어 순응형 소프트 로봇 시스템에 대한 효과성을 확인했습니다. 마지막으로, 식별된 8개의 암이 수영하는 문어 로봇에 조립되었으며, 통합 매개변수 세트가 추가 조정 없이 현실적인 전신 동작을 가능하게 했습니다. 이러한 결과는 제안된 구조-유체역학 모델링 프레임워크가 수중 저구동 및 소프트 로봇 시스템 전반에 걸쳐 확장성과 전이성을 가짐을 보여줍니다.

## 핵심 내용
수중 로봇은 해양 탐사 및 조작을 위해 널리 사용됩니다. 저구동 메커니즘은 수중 환경에서 유리한데, 이는 액추에이터 수를 줄이면 모터 누출 위험을 낮추면서도 고유한 기계적 순응성을 도입하기 때문입니다. 그러나 수중 저구동 및 소프트 로봇 시스템의 정확한 모델링은 고차원의 구조적 및 유체역학적 매개변수를 식별해야 하므로 여전히 어려운 과제입니다. 본 연구에서는 수중 다물체 시스템의 통합 구조-유체역학 모델링을 위한 궤적 기반 전역 최적화 프레임워크를 제안합니다. 공분산 행렬 적응 진화 전략(CMA-ES)에서 영감을 받은 이 접근법은 시뮬레이션과 실험 운동 간의 궤적 수준 정합을 통해 결합된 탄성, 감쇠 및 분산 유체역학 매개변수를 동시에 식별합니다. 이를 통해 단일 비디오 녹화만으로도 수중 환경에서 저구동 메커니즘과 순응형 소프트 로봇 시스템의 고충실도 재현이 가능합니다. 먼저 링크별 저구동 다물체 메커니즘에서 프레임워크를 검증하여 분산 유체역학 계수의 정확한 식별을 입증했으며, 여러 궤적, 초기 조건, 능동-수동 및 완전 수동 구성에서 정규화된 말단 효과기 위치 오차가 5% 미만임을 확인했습니다. 모델링 전략은 비대칭 문어 모방 소프트 암에서 추가로 검증되어 순응형 소프트 로봇 시스템에 대한 효과성을 확인했습니다. 마지막으로, 식별된 8개의 암이 수영하는 문어 로봇에 조립되었으며, 통합 매개변수 세트가 추가 조정 없이 현실적인 전신 동작을 가능하게 했습니다. 이러한 결과는 제안된 구조-유체역학 모델링 프레임워크가 수중 저구동 및 소프트 로봇 시스템 전반에 걸쳐 확장성과 전이성을 가짐을 보여줍니다.
