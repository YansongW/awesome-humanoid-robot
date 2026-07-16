---
$id: ent_paper_sim_to_real_of_humanoid_locomo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Sim-to-Real of Humanoid Locomotion Policies via Joint Torque Space Perturbation Injection
  zh: Sim-to-Real of Humanoid Locomotion Policies via Joint Torque Space Perturbation Injection
  ko: Sim-to-Real of Humanoid Locomotion Policies via Joint Torque Space Perturbation Injection
summary:
  en: Sim-to-Real of Humanoid Locomotion Policies via Joint Torque Space Perturbation Injection is a 2025 work on sim-to-real
    for humanoid robots.
  zh: Sim-to-Real of Humanoid Locomotion Policies via Joint Torque Space Perturbation Injection is a 2025 work on sim-to-real
    for humanoid robots.
  ko: Sim-to-Real of Humanoid Locomotion Policies via Joint Torque Space Perturbation Injection is a 2025 work on sim-to-real
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
- sim_to_real
- sim_to_real_of_humanoid_locomo
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.06585v2.
sources:
- id: src_001
  type: paper
  title: Sim-to-Real of Humanoid Locomotion Policies via Joint Torque Space Perturbation Injection (arXiv)
  url: https://arxiv.org/abs/2504.06585
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
This paper proposes a novel alternative to existing sim-to-real methods for training control policies with simulated experiences. Prior sim-to-real methods for legged robots mostly rely on the domain randomization approach, where a fixed finite set of simulation parameters is randomized during training. Instead, our method adds state-dependent perturbations to the input joint torque used for forward simulation during the training phase. These state-dependent perturbations are designed to simulate a broader range of reality gaps than those captured by randomizing a fixed set of simulation parameters. Experimental results show that our method enables humanoid locomotion policies that achieve greater robustness against complex reality gaps unseen in the training domain.

## 核心内容
This paper proposes a novel alternative to existing sim-to-real methods for training control policies with simulated experiences. Prior sim-to-real methods for legged robots mostly rely on the domain randomization approach, where a fixed finite set of simulation parameters is randomized during training. Instead, our method adds state-dependent perturbations to the input joint torque used for forward simulation during the training phase. These state-dependent perturbations are designed to simulate a broader range of reality gaps than those captured by randomizing a fixed set of simulation parameters. Experimental results show that our method enables humanoid locomotion policies that achieve greater robustness against complex reality gaps unseen in the training domain.

## 参考
- http://arxiv.org/abs/2504.06585v2

## Overview
This paper proposes a novel alternative to existing sim-to-real methods for training control policies with simulated experiences. Prior sim-to-real methods for legged robots mostly rely on the domain randomization approach, where a fixed finite set of simulation parameters is randomized during training. Instead, our method adds state-dependent perturbations to the input joint torque used for forward simulation during the training phase. These state-dependent perturbations are designed to simulate a broader range of reality gaps than those captured by randomizing a fixed set of simulation parameters. Experimental results show that our method enables humanoid locomotion policies that achieve greater robustness against complex reality gaps unseen in the training domain.

## Content
This paper proposes a novel alternative to existing sim-to-real methods for training control policies with simulated experiences. Prior sim-to-real methods for legged robots mostly rely on the domain randomization approach, where a fixed finite set of simulation parameters is randomized during training. Instead, our method adds state-dependent perturbations to the input joint torque used for forward simulation during the training phase. These state-dependent perturbations are designed to simulate a broader range of reality gaps than those captured by randomizing a fixed set of simulation parameters. Experimental results show that our method enables humanoid locomotion policies that achieve greater robustness against complex reality gaps unseen in the training domain.

## 개요
본 논문은 시뮬레이션 경험을 활용한 제어 정책 훈련을 위한 기존 sim-to-real 방법에 대한 새로운 대안을 제안합니다. 보행 로봇을 위한 기존 sim-to-real 방법은 대부분 도메인 무작위화 접근법에 의존하며, 여기서 고정된 유한한 시뮬레이션 매개변수 집합이 훈련 중에 무작위화됩니다. 대신, 본 방법은 훈련 단계에서 순방향 시뮬레이션에 사용되는 입력 관절 토크에 상태 의존적 섭동을 추가합니다. 이러한 상태 의존적 섭동은 고정된 시뮬레이션 매개변수 집합을 무작위화하여 포착되는 것보다 더 넓은 범위의 현실 격차를 시뮬레이션하도록 설계되었습니다. 실험 결과는 본 방법이 훈련 도메인에서 보지 못한 복잡한 현실 격차에 대해 더 큰 견고성을 달성하는 인간형 보행 정책을 가능하게 함을 보여줍니다.

## 핵심 내용
본 논문은 시뮬레이션 경험을 활용한 제어 정책 훈련을 위한 기존 sim-to-real 방법에 대한 새로운 대안을 제안합니다. 보행 로봇을 위한 기존 sim-to-real 방법은 대부분 도메인 무작위화 접근법에 의존하며, 여기서 고정된 유한한 시뮬레이션 매개변수 집합이 훈련 중에 무작위화됩니다. 대신, 본 방법은 훈련 단계에서 순방향 시뮬레이션에 사용되는 입력 관절 토크에 상태 의존적 섭동을 추가합니다. 이러한 상태 의존적 섭동은 고정된 시뮬레이션 매개변수 집합을 무작위화하여 포착되는 것보다 더 넓은 범위의 현실 격차를 시뮬레이션하도록 설계되었습니다. 실험 결과는 본 방법이 훈련 도메인에서 보지 못한 복잡한 현실 격차에 대해 더 큰 견고성을 달성하는 인간형 보행 정책을 가능하게 함을 보여줍니다.
