---
$id: ent_paper_learning_humanoid_standing_up_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Humanoid Standing-up Control across Diverse Postures
  zh: Learning Humanoid Standing-up Control across Diverse Postures
  ko: Learning Humanoid Standing-up Control across Diverse Postures
summary:
  en: Learning Humanoid Standing-up Control across Diverse Postures is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.
  zh: Learning Humanoid Standing-up Control across Diverse Postures is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.
  ko: Learning Humanoid Standing-up Control across Diverse Postures is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.
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
- learning_humanoid_standing_up
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.08378v2.
sources:
- id: src_001
  type: paper
  title: Learning Humanoid Standing-up Control across Diverse Postures (arXiv)
  url: https://arxiv.org/abs/2502.08378
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Standing-up control is crucial for humanoid robots, with the potential for integration into current locomotion and loco-manipulation systems, such as fall recovery. Existing approaches are either limited to simulations that overlook hardware constraints or rely on predefined ground-specific motion trajectories, failing to enable standing up across postures in real-world scenes. To bridge this gap, we present HoST (Humanoid Standing-up Control), a reinforcement learning framework that learns standing-up control from scratch, enabling robust sim-to-real transfer across diverse postures. HoST effectively learns posture-adaptive motions by leveraging a multi-critic architecture and curriculum-based training on diverse simulated terrains. To ensure successful real-world deployment, we constrain the motion with smoothness regularization and implicit motion speed bound to alleviate oscillatory and violent motions on physical hardware, respectively. After simulation-based training, the learned control policies are directly deployed on the Unitree G1 humanoid robot. Our experimental results demonstrate that the controllers achieve smooth, stable, and robust standing-up motions across a wide range of laboratory and outdoor environments. Videos and code are available at https://taohuang13.github.io/humanoid-standingup.github.io/.

## 核心内容
Standing-up control is crucial for humanoid robots, with the potential for integration into current locomotion and loco-manipulation systems, such as fall recovery. Existing approaches are either limited to simulations that overlook hardware constraints or rely on predefined ground-specific motion trajectories, failing to enable standing up across postures in real-world scenes. To bridge this gap, we present HoST (Humanoid Standing-up Control), a reinforcement learning framework that learns standing-up control from scratch, enabling robust sim-to-real transfer across diverse postures. HoST effectively learns posture-adaptive motions by leveraging a multi-critic architecture and curriculum-based training on diverse simulated terrains. To ensure successful real-world deployment, we constrain the motion with smoothness regularization and implicit motion speed bound to alleviate oscillatory and violent motions on physical hardware, respectively. After simulation-based training, the learned control policies are directly deployed on the Unitree G1 humanoid robot. Our experimental results demonstrate that the controllers achieve smooth, stable, and robust standing-up motions across a wide range of laboratory and outdoor environments. Videos and code are available at https://taohuang13.github.io/humanoid-standingup.github.io/.

## 参考
- http://arxiv.org/abs/2502.08378v2

## Overview
Standing-up control is crucial for humanoid robots, with the potential for integration into current locomotion and loco-manipulation systems, such as fall recovery. Existing approaches are either limited to simulations that overlook hardware constraints or rely on predefined ground-specific motion trajectories, failing to enable standing up across postures in real-world scenes. To bridge this gap, we present HoST (Humanoid Standing-up Control), a reinforcement learning framework that learns standing-up control from scratch, enabling robust sim-to-real transfer across diverse postures. HoST effectively learns posture-adaptive motions by leveraging a multi-critic architecture and curriculum-based training on diverse simulated terrains. To ensure successful real-world deployment, we constrain the motion with smoothness regularization and implicit motion speed bound to alleviate oscillatory and violent motions on physical hardware, respectively. After simulation-based training, the learned control policies are directly deployed on the Unitree G1 humanoid robot. Our experimental results demonstrate that the controllers achieve smooth, stable, and robust standing-up motions across a wide range of laboratory and outdoor environments. Videos and code are available at https://taohuang13.github.io/humanoid-standingup.github.io/.

## Content
Standing-up control is crucial for humanoid robots, with the potential for integration into current locomotion and loco-manipulation systems, such as fall recovery. Existing approaches are either limited to simulations that overlook hardware constraints or rely on predefined ground-specific motion trajectories, failing to enable standing up across postures in real-world scenes. To bridge this gap, we present HoST (Humanoid Standing-up Control), a reinforcement learning framework that learns standing-up control from scratch, enabling robust sim-to-real transfer across diverse postures. HoST effectively learns posture-adaptive motions by leveraging a multi-critic architecture and curriculum-based training on diverse simulated terrains. To ensure successful real-world deployment, we constrain the motion with smoothness regularization and implicit motion speed bound to alleviate oscillatory and violent motions on physical hardware, respectively. After simulation-based training, the learned control policies are directly deployed on the Unitree G1 humanoid robot. Our experimental results demonstrate that the controllers achieve smooth, stable, and robust standing-up motions across a wide range of laboratory and outdoor environments. Videos and code are available at https://taohuang13.github.io/humanoid-standingup.github.io/.

## 개요
휴머노이드 로봇의 기립 제어는 낙상 복구와 같은 현재의 보행 및 보행-조작 시스템에 통합될 가능성이 있어 매우 중요합니다. 기존 접근 방식은 하드웨어 제약을 간과한 시뮬레이션에 국한되거나, 미리 정의된 지면별 동작 궤적에 의존하여 실제 환경에서 다양한 자세로 기립하는 것을 실현하지 못합니다. 이러한 격차를 해소하기 위해, 우리는 HoST(Humanoid Standing-up Control)를 제시합니다. 이는 강화 학습 프레임워크로, 기립 제어를 처음부터 학습하여 다양한 자세에 걸쳐 강건한 시뮬-투-리얼 전이를 가능하게 합니다. HoST는 다중 비평가 아키텍처와 다양한 시뮬레이션 지형에서의 커리큘럼 기반 훈련을 활용하여 자세 적응형 동작을 효과적으로 학습합니다. 실제 환경 배포를 성공적으로 보장하기 위해, 우리는 동작에 평활화 정규화와 암시적 동작 속도 제한을 적용하여 각각 물리적 하드웨어에서의 진동 및 과격한 동작을 완화합니다. 시뮬레이션 기반 훈련 후, 학습된 제어 정책은 Unitree G1 휴머노이드 로봇에 직접 배포됩니다. 실험 결과는 컨트롤러가 다양한 실내 및 실외 환경에서 부드럽고 안정적이며 강건한 기립 동작을 달성함을 보여줍니다. 비디오와 코드는 https://taohuang13.github.io/humanoid-standingup.github.io/에서 확인할 수 있습니다.

## 핵심 내용
휴머노이드 로봇의 기립 제어는 낙상 복구와 같은 현재의 보행 및 보행-조작 시스템에 통합될 가능성이 있어 매우 중요합니다. 기존 접근 방식은 하드웨어 제약을 간과한 시뮬레이션에 국한되거나, 미리 정의된 지면별 동작 궤적에 의존하여 실제 환경에서 다양한 자세로 기립하는 것을 실현하지 못합니다. 이러한 격차를 해소하기 위해, 우리는 HoST(Humanoid Standing-up Control)를 제시합니다. 이는 강화 학습 프레임워크로, 기립 제어를 처음부터 학습하여 다양한 자세에 걸쳐 강건한 시뮬-투-리얼 전이를 가능하게 합니다. HoST는 다중 비평가 아키텍처와 다양한 시뮬레이션 지형에서의 커리큘럼 기반 훈련을 활용하여 자세 적응형 동작을 효과적으로 학습합니다. 실제 환경 배포를 성공적으로 보장하기 위해, 우리는 동작에 평활화 정규화와 암시적 동작 속도 제한을 적용하여 각각 물리적 하드웨어에서의 진동 및 과격한 동작을 완화합니다. 시뮬레이션 기반 훈련 후, 학습된 제어 정책은 Unitree G1 휴머노이드 로봇에 직접 배포됩니다. 실험 결과는 컨트롤러가 다양한 실내 및 실외 환경에서 부드럽고 안정적이며 강건한 기립 동작을 달성함을 보여줍니다. 비디오와 코드는 https://taohuang13.github.io/humanoid-standingup.github.io/에서 확인할 수 있습니다.
