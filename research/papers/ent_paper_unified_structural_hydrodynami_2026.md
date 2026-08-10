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
  zh: 本文提出一种基于轨迹驱动的全局优化框架，用于水下欠驱动机构与软体机器人的统一结构-水动力学建模。该方法受CMA-ES启发，通过仿真与实验运动轨迹匹配，同时识别弹性、阻尼及分布式水动力学参数，仅需单段视频即可实现高保真复现。在连杆欠驱动机构与章鱼仿生软体臂上验证，末端位置误差低于5%，并成功扩展至八臂游泳章鱼机器人。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.07939v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (709 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Unified Structural-Hydrodynamic Modeling of Underwater Underactuated Mechanisms and Soft Robots
  url: https://arxiv.org/abs/2603.07939
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
水下机器人广泛用于海洋探索与操作，欠驱动机构因减少致动器数量而降低电机泄漏风险并引入机械柔顺性，但其建模面临高维结构和水动力学参数识别的挑战。本文提出一种轨迹驱动的全局优化框架，受CMA-ES启发，通过仿真与实验运动轨迹的匹配，同时识别耦合的弹性、阻尼及分布式水动力学参数。该方法仅需单段视频即可高保真复现水下欠驱动机构与柔顺软体系统。在连杆欠驱动机构上验证，末端位置归一化误差低于5%，并在非对称章鱼仿生软体臂上确认有效性。最终，将八个识别后的臂组装成游泳章鱼机器人，统一参数集无需额外调整即可实现逼真的全身行为。

## 核心内容
### 方法
- 提出一种**轨迹驱动的全局优化框架**，用于水下多体系统的统一结构-水动力学建模。
- 受**Covariance Matrix Adaptation Evolution Strategy (CMA-ES)** 启发，通过仿真与实验运动轨迹的匹配，同时识别耦合的弹性、阻尼及分布式水动力学参数。
- 仅需**单段视频记录**即可实现高保真复现，适用于欠驱动机构与柔顺软体系统。

### 实验设置与验证
- **连杆欠驱动机构**：逐连杆验证，准确识别分布式水动力学系数，在多种轨迹、初始条件及主动-被动与完全被动配置下，**末端位置归一化误差低于5%**。
- **非对称章鱼仿生软体臂**：进一步验证框架对柔顺软体系统的有效性。
- **八臂游泳章鱼机器人**：将八个识别后的臂组装，**统一参数集无需额外调整**即可实现逼真的全身行为。

### 结论
- 结果表明，该框架具有**可扩展性与可迁移性**，可适用于水下欠驱动机构与软体机器人系统。

## Overview
Underwater robots are widely deployed for ocean exploration and manipulation. Underactuated mechanisms are advantageous in aquatic environments because reducing actuator count lowers motor-leakage risk while introducing inherent mechanical compliance. However, accurate modeling of underwater underactuated and soft robotic systems remains challenging, as it requires identifying high-dimensional structural and hydrodynamic parameters. In this work, we propose a trajectory-driven global optimization framework for unified structural-hydrodynamic modeling of underwater multibody systems. Inspired by the Covariance Matrix Adaptation Evolution Strategy (CMA-ES), the proposed approach simultaneously identifies coupled elastic, damping, and distributed hydrodynamic parameters through trajectory-level matching between simulated and experimental motion. This enables high-fidelity reproduction of underactuated mechanisms and compliant soft robotic systems in underwater environments, using as little as a single video recording. We first validate the framework on a link-by-link underactuated multibody mechanism, demonstrating accurate identification of distributed hydrodynamic coefficients, with normalized end-effector position error below 5% across multiple trajectories, initial conditions, and both active-passive and fully passive configurations. The modeling strategy is further validated on an asymmetric octopus-inspired soft arm, confirming its effectiveness for compliant soft robotic systems. Finally, eight identified arms are assembled into a swimming octopus robot, where the unified parameter set enables realistic whole-body behavior without additional retuning. These results demonstrate the scalability and transferability of the proposed structural-hydrodynamic modeling framework across underwater underactuated and soft robotic systems.

## 参考
- http://arxiv.org/abs/2603.07939v2

## 개요
수중 로봇은 해양 탐사와 작업에 널리 사용되며, 부족구동 메커니즘은 액추에이터 수를 줄여 모터 누출 위험을 낮추고 기계적 유연성을 도입하지만, 모델링 과정에서 고차원 구조와 수력학적 매개변수 식별의 어려움이 있습니다. 본 논문은 CMA-ES에서 영감을 받은 궤적 기반 전역 최적화 프레임워크를 제안하며, 시뮬레이션과 실험 운동 궤적의 일치를 통해 결합된 탄성, 감쇠 및 분산 수력학적 매개변수를 동시에 식별합니다. 이 방법은 단일 비디오 세그먼트만으로 수중 부족구동 메커니즘과 유연 소프트 시스템을 고충실도로 재현할 수 있습니다. 링크 부족구동 메커니즘에서 검증되었으며, 끝단 위치 정규화 오차가 5% 미만이고, 비대칭 문어 생체모방 소프트 암에서도 유효성을 확인했습니다. 마지막으로, 식별된 8개의 암을 조립하여 수영하는 문어 로봇을 구성했으며, 통합 매개변수 세트는 추가 조정 없이도 사실적인 전신 동작을 구현합니다.

## 핵심 내용
### 방법
- 수중 다물체 시스템의 통합 구조-수력학적 모델링을 위한 **궤적 기반 전역 최적화 프레임워크**를 제안합니다.
- **Covariance Matrix Adaptation Evolution Strategy (CMA-ES)** 에서 영감을 받아, 시뮬레이션과 실험 운동 궤적의 일치를 통해 결합된 탄성, 감쇠 및 분산 수력학적 매개변수를 동시에 식별합니다.
- **단일 비디오 기록**만으로 고충실도 재현이 가능하며, 부족구동 메커니즘과 유연 소프트 시스템에 적용 가능합니다.

### 실험 설정 및 검증
- **링크 부족구동 메커니즘**: 링크별로 검증하여 분산 수력학적 계수를 정확히 식별했으며, 다양한 궤적, 초기 조건 및 능동-수동 및 완전 수동 구성에서 **끝단 위치 정규화 오차가 5% 미만**입니다.
- **비대칭 문어 생체모방 소프트 암**: 프레임워크의 유연 소프트 시스템에 대한 유효성을 추가로 검증합니다.
- **8개 암 수영 문어 로봇**: 식별된 8개의 암을 조립하여 **통합 매개변수 세트는 추가 조정 없이** 사실적인 전신 동작을 구현합니다.

### 결론
- 결과는 이 프레임워크가 **확장성과 전이성**을 가지며, 수중 부족구동 메커니즘과 소프트 로봇 시스템에 적용될 수 있음을 보여줍니다.
