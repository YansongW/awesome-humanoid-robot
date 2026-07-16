---
$id: ent_paper_3d_hamster_bridging_planning_a_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: '3D HAMSTER: Bridging Planning and Control in Hierarchical Vision Language Action Models through 3D Trajectory Guidance'
  zh: '3D HAMSTER: Bridging Planning and Control in Hierarchical Vision Language Action Models through 3D Trajectory Guidance'
  ko: '3D HAMSTER: Bridging Planning and Control in Hierarchical Vision Language Action Models through 3D Trajectory Guidance'
summary:
  en: 'arXiv:2606.31329v1 Announce Type: new Abstract: Hierarchical Vision-Language-Action (VLA) models decouple high-level
    planning from low-level control to improve generalization in robot manipulation. Recent work in this paradigm uses 2D
    end-effector trajectories predicted by a Vision-Language Model (VLM) as explicit guidance for a downstream policy. However,
    state-of-the-art low-level policies operate in 3D metric space on point clouds, and feeding them 2D guidance that lacks
    depth forces each waypoint to be assigned the depth of whatever scene surface lies beneath it, producing geometrically
    distorted trajectories. We propose 3D HAMSTER, a hierarchical framework that closes this gap by having the planner directly
    output metrically reliable 3D trajectories. We augment a VLM with a dedicated depth encoder and a dense depth reconstruction
    objective to predict 3D waypoint sequences, which are directly integrated into a pointcloudbased low-level policy. Across
    3D trajectory prediction, simulation, and real-world manipulation, 3D HAMSTER consistently outperforms proprietary VLMs
    and 2D-guided baselines, with the largest gains under appearance-altering shifts and unseen language, spatial, and visual
    conditions. The project page is available at https://davian-robotics.github.io/3D_HAMSTER/.'
  zh: 'arXiv:2606.31329v1 Announce Type: new Abstract: Hierarchical Vision-Language-Action (VLA) models decouple high-level
    planning from low-level control to improve generalization in robot manipulation. Recent work in this paradigm uses 2D
    end-effector trajectories predicted by a Vision-Language Model (VLM) as explicit guidance for a downstream policy. However,
    state-of-the-art low-level policies operate in 3D metric space on point clouds, and feeding them 2D guidance that lacks
    depth forces each waypoint to be assigned the depth of whatever scene surface lies beneath it, producing geometrically
    distorted trajectories. We propose 3D HAMSTER, a hierarchical framework that closes this gap by having the planner directly
    output metrically reliable 3D trajectories. We augment a VLM with a dedicated depth encoder and a dense depth reconstruction
    objective to predict 3D waypoint sequences, which are directly integrated into a pointcloudbased low-level policy. Across
    3D trajectory prediction, simulation, and real-world manipulation, 3D HAMSTER consistently outperforms proprietary VLMs
    and 2D-guided baselines, with the largest gains under appearance-altering shifts and unseen language, spatial, and visual
    conditions. The project page is available at https://davian-robotics.github.io/3D_HAMSTER/.'
  ko: 'arXiv:2606.31329v1 Announce Type: new Abstract: Hierarchical Vision-Language-Action (VLA) models decouple high-level
    planning from low-level control to improve generalization in robot manipulation. Recent work in this paradigm uses 2D
    end-effector trajectories predicted by a Vision-Language Model (VLM) as explicit guidance for a downstream policy. However,
    state-of-the-art low-level policies operate in 3D metric space on point clouds, and feeding them 2D guidance that lacks
    depth forces each waypoint to be assigned the depth of whatever scene surface lies beneath it, producing geometrically
    distorted trajectories. We propose 3D HAMSTER, a hierarchical framework that closes this gap by having the planner directly
    output metrically reliable 3D trajectories. We augment a VLM with a dedicated depth encoder and a dense depth reconstruction
    objective to predict 3D waypoint sequences, which are directly integrated into a pointcloudbased low-level policy. Across
    3D trajectory prediction, simulation, and real-world manipulation, 3D HAMSTER consistently outperforms proprietary VLMs
    and 2D-guided baselines, with the largest gains under appearance-altering shifts and unseen language, spatial, and visual
    conditions. The project page is available at https://davian-robotics.github.io/3D_HAMSTER/.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- 3d_hamster
- humanoid
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31329v2.
sources:
- id: src_001
  type: paper
  title: '3D HAMSTER: Bridging Planning and Control in Hierarchical Vision Language Action Models through 3D Trajectory Guidance'
  url: https://arxiv.org/abs/2606.31329
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Hierarchical Vision-Language-Action (VLA) models decouple high-level planning from low-level control to improve generalization in robot manipulation. Recent work in this paradigm uses 2D end-effector trajectories predicted by a Vision-Language Model (VLM) as explicit guidance for a downstream policy. However, state-of-the-art low-level policies operate in 3D metric space on point clouds, and feeding them 2D guidance that lacks depth forces each waypoint to be assigned the depth of whatever scene surface lies beneath it, producing geometrically distorted trajectories. We propose 3D HAMSTER, a hierarchical framework that closes this gap by having the planner directly output metrically reliable 3D trajectories. We augment a VLM with a dedicated depth encoder and a dense depth reconstruction objective to predict 3D waypoint sequences, which are directly integrated into a pointcloudbased low-level policy. Across 3D trajectory prediction, simulation, and real-world manipulation, 3D HAMSTER consistently outperforms proprietary VLMs and 2D-guided baselines, with the largest gains under appearance-altering shifts and unseen language, spatial, and visual conditions. The project page is available at https://davian-robotics.github.io/3D_HAMSTER/.

## 核心内容
Hierarchical Vision-Language-Action (VLA) models decouple high-level planning from low-level control to improve generalization in robot manipulation. Recent work in this paradigm uses 2D end-effector trajectories predicted by a Vision-Language Model (VLM) as explicit guidance for a downstream policy. However, state-of-the-art low-level policies operate in 3D metric space on point clouds, and feeding them 2D guidance that lacks depth forces each waypoint to be assigned the depth of whatever scene surface lies beneath it, producing geometrically distorted trajectories. We propose 3D HAMSTER, a hierarchical framework that closes this gap by having the planner directly output metrically reliable 3D trajectories. We augment a VLM with a dedicated depth encoder and a dense depth reconstruction objective to predict 3D waypoint sequences, which are directly integrated into a pointcloudbased low-level policy. Across 3D trajectory prediction, simulation, and real-world manipulation, 3D HAMSTER consistently outperforms proprietary VLMs and 2D-guided baselines, with the largest gains under appearance-altering shifts and unseen language, spatial, and visual conditions. The project page is available at https://davian-robotics.github.io/3D_HAMSTER/.

## 参考
- http://arxiv.org/abs/2606.31329v2

## Overview
Hierarchical Vision-Language-Action (VLA) models decouple high-level planning from low-level control to improve generalization in robot manipulation. Recent work in this paradigm uses 2D end-effector trajectories predicted by a Vision-Language Model (VLM) as explicit guidance for a downstream policy. However, state-of-the-art low-level policies operate in 3D metric space on point clouds, and feeding them 2D guidance that lacks depth forces each waypoint to be assigned the depth of whatever scene surface lies beneath it, producing geometrically distorted trajectories. We propose 3D HAMSTER, a hierarchical framework that closes this gap by having the planner directly output metrically reliable 3D trajectories. We augment a VLM with a dedicated depth encoder and a dense depth reconstruction objective to predict 3D waypoint sequences, which are directly integrated into a pointcloud-based low-level policy. Across 3D trajectory prediction, simulation, and real-world manipulation, 3D HAMSTER consistently outperforms proprietary VLMs and 2D-guided baselines, with the largest gains under appearance-altering shifts and unseen language, spatial, and visual conditions. The project page is available at https://davian-robotics.github.io/3D_HAMSTER/.

## Content
Hierarchical Vision-Language-Action (VLA) models decouple high-level planning from low-level control to improve generalization in robot manipulation. Recent work in this paradigm uses 2D end-effector trajectories predicted by a Vision-Language Model (VLM) as explicit guidance for a downstream policy. However, state-of-the-art low-level policies operate in 3D metric space on point clouds, and feeding them 2D guidance that lacks depth forces each waypoint to be assigned the depth of whatever scene surface lies beneath it, producing geometrically distorted trajectories. We propose 3D HAMSTER, a hierarchical framework that closes this gap by having the planner directly output metrically reliable 3D trajectories. We augment a VLM with a dedicated depth encoder and a dense depth reconstruction objective to predict 3D waypoint sequences, which are directly integrated into a pointcloud-based low-level policy. Across 3D trajectory prediction, simulation, and real-world manipulation, 3D HAMSTER consistently outperforms proprietary VLMs and 2D-guided baselines, with the largest gains under appearance-altering shifts and unseen language, spatial, and visual conditions. The project page is available at https://davian-robotics.github.io/3D_HAMSTER/.

## 개요
계층적 비전-언어-행동(VLA) 모델은 고수준 계획과 저수준 제어를 분리하여 로봇 조작의 일반화 성능을 향상시킵니다. 이 패러다임의 최근 연구는 비전-언어 모델(VLM)이 예측한 2D 엔드 이펙터 궤적을 하위 정책의 명시적 지침으로 사용합니다. 그러나 최첨단 저수준 정책은 포인트 클라우드 상의 3D 미터법 공간에서 작동하며, 깊이 정보가 없는 2D 지침을 입력하면 각 웨이포인트가 그 아래에 있는 장면 표면의 깊이를 할당받아 기하학적으로 왜곡된 궤적이 생성됩니다. 우리는 계획기가 직접 미터법적으로 신뢰할 수 있는 3D 궤적을 출력하도록 하여 이 격차를 해소하는 계층적 프레임워크인 3D HAMSTER를 제안합니다. 우리는 전용 깊이 인코더와 조밀한 깊이 재구성 목표를 통해 VLM을 확장하여 3D 웨이포인트 시퀀스를 예측하고, 이를 포인트 클라우드 기반 저수준 정책에 직접 통합합니다. 3D 궤적 예측, 시뮬레이션 및 실제 로봇 조작 실험에서 3D HAMSTER는 독점 VLM 및 2D 지침 기반 기준선을 일관되게 능가하며, 특히 외관 변화, 새로운 언어, 공간 및 시각 조건에서 가장 큰 성능 향상을 보입니다. 프로젝트 페이지는 https://davian-robotics.github.io/3D_HAMSTER/에서 확인할 수 있습니다.

## 핵심 내용
계층적 비전-언어-행동(VLA) 모델은 고수준 계획과 저수준 제어를 분리하여 로봇 조작의 일반화 성능을 향상시킵니다. 이 패러다임의 최근 연구는 비전-언어 모델(VLM)이 예측한 2D 엔드 이펙터 궤적을 하위 정책의 명시적 지침으로 사용합니다. 그러나 최첨단 저수준 정책은 포인트 클라우드 상의 3D 미터법 공간에서 작동하며, 깊이 정보가 없는 2D 지침을 입력하면 각 웨이포인트가 그 아래에 있는 장면 표면의 깊이를 할당받아 기하학적으로 왜곡된 궤적이 생성됩니다. 우리는 계획기가 직접 미터법적으로 신뢰할 수 있는 3D 궤적을 출력하도록 하여 이 격차를 해소하는 계층적 프레임워크인 3D HAMSTER를 제안합니다. 우리는 전용 깊이 인코더와 조밀한 깊이 재구성 목표를 통해 VLM을 확장하여 3D 웨이포인트 시퀀스를 예측하고, 이를 포인트 클라우드 기반 저수준 정책에 직접 통합합니다. 3D 궤적 예측, 시뮬레이션 및 실제 로봇 조작 실험에서 3D HAMSTER는 독점 VLM 및 2D 지침 기반 기준선을 일관되게 능가하며, 특히 외관 변화, 새로운 언어, 공간 및 시각 조건에서 가장 큰 성능 향상을 보입니다. 프로젝트 페이지는 https://davian-robotics.github.io/3D_HAMSTER/에서 확인할 수 있습니다.
