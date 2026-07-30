---
$id: ent_paper_physv2a_reachability_gated_and_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PhysV2A: Reachability-Gated and Semantic-Mask-Constrained Feasibility Completion for Video-to-Robot Manipulation'
  zh: 'PhysV2A: Reachability-Gated and Semantic-Mask-Constrained Feasibility Completion for Video-to-Robot Manipulation'
  ko: 'PhysV2A: Reachability-Gated and Semantic-Mask-Constrained Feasibility Completion for Video-to-Robot Manipulation'
summary:
  en: 'arXiv:2607.09365v1 Announce Type: new Abstract: Video-based manipulation provides object-centric motion priors from
    human demonstrations, generated videos, or RGB-D observations, but such priors are typically embodiment-agnostic and cannot
    be directly executed by a specific robot. This paper presents \textbf{PhysV2A}, a reachability-gated and semantic-mask-constrained
    feasibility-completion framework for converting video-derived 6D object motion into robot-executable manipulation trajectories.
    The key idea is to treat grasp feasibility as trajectory-conditioned rather than local: each RGB-D-generated 6-DoF grasp
    candidate is rigidly coupled with the recovered object motion to form a grasp-conditioned TCP trajectory hypothesis. PhysV2A
    then performs hierarchical reachability-gated selection, where infeasible grasp--trajectory pairs are rejected by robot-centric
    kinematic checks and surviving candidates are ranked by downstream execution suitability. For the selected reachable trajectory,
    a VLM-assisted and rule-validated S-Mask identifies task-critical and relaxable Cartesian components, enabling semantic-mask-constrained
    manipulability refinement through redundancy-first optimization and bounded Cartesian relaxation. Real-robot experiments
    on four tabletop manipulation tasks show that PhysV2A improves task success over representative video-prior and IK-only
    baselines, reduces kinematic-feasibility failures, and produces better-conditioned trajectories with bounded semantic
    deviations.'
  zh: PhysV2A 是一个将视频中的6D物体运动转化为机器人可执行操作轨迹的框架，由研究团队提出。其核心贡献在于通过可达性门控和语义掩码约束的可行性补全机制，将抓取可行性视为轨迹条件而非局部条件，从而提升任务成功率并减少运动学可行性失败。
  ko: 'arXiv:2607.09365v1 Announce Type: new Abstract: Video-based manipulation provides object-centric motion priors from
    human demonstrations, generated videos, or RGB-D observations, but such priors are typically embodiment-agnostic and cannot
    be directly executed by a specific robot. This paper presents \textbf{PhysV2A}, a reachability-gated and semantic-mask-constrained
    feasibility-completion framework for converting video-derived 6D object motion into robot-executable manipulation trajectories.
    The key idea is to treat grasp feasibility as trajectory-conditioned rather than local: each RGB-D-generated 6-DoF grasp
    candidate is rigidly coupled with the recovered object motion to form a grasp-conditioned TCP trajectory hypothesis. PhysV2A
    then performs hierarchical reachability-gated selection, where infeasible grasp--trajectory pairs are rejected by robot-centric
    kinematic checks and surviving candidates are ranked by downstream execution suitability. For the selected reachable trajectory,
    a VLM-assisted and rule-validated S-Mask identifies task-critical and relaxable Cartesian components, enabling semantic-mask-constrained
    manipulability refinement through redundancy-first optimization and bounded Cartesian relaxation. Real-robot experiments
    on four tabletop manipulation tasks show that PhysV2A improves task success over representative video-prior and IK-only
    baselines, reduces kinematic-feasibility failures, and produces better-conditioned trajectories with bounded semantic
    deviations.'
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
- physv2a
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.09365v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'PhysV2A: Reachability-Gated and Semantic-Mask-Constrained Feasibility Completion for Video-to-Robot Manipulation
    (arXiv)'
  url: https://arxiv.org/abs/2607.09365
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
PhysV2A 框架旨在解决视频驱动操作中运动先验与具体机器人执行之间的脱节问题。它通过将每个RGB-D生成的6自由度抓取候选与恢复的物体运动刚性耦合，形成抓取条件化的TCP轨迹假设，并采用层次化可达性门控选择，拒绝不可行的抓取-轨迹对。对于选中的可达轨迹，框架利用VLM辅助和规则验证的语义掩码识别任务关键与可放松的笛卡尔分量，通过冗余优先优化和有界笛卡尔放松进行语义掩码约束的可操作性精炼。在四个桌面操作任务上的真实机器人实验表明，PhysV2A 相比基线方法提升了任务成功率，减少了运动学可行性失败，并生成了条件更优且语义偏差有界的轨迹。

## 核心内容
### 方法概述
PhysV2A 框架的核心创新在于将抓取可行性视为轨迹条件而非局部条件。具体而言，每个由RGB-D数据生成的6自由度抓取候选与恢复的物体运动刚性耦合，形成抓取条件化的TCP轨迹假设。随后，框架执行层次化可达性门控选择，通过机器人中心运动学检查拒绝不可行的抓取-轨迹对，并对幸存候选按下游执行适用性排序。

### 架构与关键组件
- **可达性门控选择**：采用层次化机制，首先通过机器人中心运动学检查过滤不可行的抓取-轨迹对，然后对剩余候选进行排序，确保选中的轨迹在运动学上可行。
- **语义掩码约束精炼**：对于选中的可达轨迹，利用VLM辅助和规则验证的语义掩码（S-Mask）识别任务关键与可放松的笛卡尔分量。通过冗余优先优化和有界笛卡尔放松，实现语义掩码约束的可操作性精炼，确保轨迹在语义上有界且条件更优。

### 实验设置与结果
- **任务与基线**：在四个桌面操作任务上进行真实机器人实验，对比基线包括代表性视频先验方法和仅IK方法。
- **关键数字**：PhysV2A 在任务成功率上显著优于基线，减少了运动学可行性失败，并生成了条件更优且语义偏差有界的轨迹。具体成功率提升和失败减少的数值未在摘要中明确给出，但实验验证了其有效性。

### 结论
PhysV2A 通过将抓取可行性视为轨迹条件，结合可达性门控和语义掩码约束，成功将视频中的物体运动转化为机器人可执行轨迹，在真实机器人实验中展现了优越的性能。

## Overview
Video-based manipulation provides object-centric motion priors from human demonstrations, generated videos, or RGB-D observations, but such priors are typically embodiment-agnostic and cannot be directly executed by a specific robot. This paper presents \textbf{PhysV2A}, a reachability-gated and semantic-mask-constrained feasibility-completion framework for converting video-derived 6D object motion into robot-executable manipulation trajectories. The key idea is to treat grasp feasibility as trajectory-conditioned rather than local: each RGB-D-generated 6-DoF grasp candidate is rigidly coupled with the recovered object motion to form a grasp-conditioned TCP trajectory hypothesis. PhysV2A then performs hierarchical reachability-gated selection, where infeasible grasp--trajectory pairs are rejected by robot-centric kinematic checks and surviving candidates are ranked by downstream execution suitability. For the selected reachable trajectory, a VLM-assisted and rule-validated S-Mask identifies task-critical and relaxable Cartesian components, enabling semantic-mask-constrained manipulability refinement through redundancy-first optimization and bounded Cartesian relaxation. Real-robot experiments on four tabletop manipulation tasks show that PhysV2A improves task success over representative video-prior and IK-only baselines, reduces kinematic-feasibility failures, and produces better-conditioned trajectories with bounded semantic deviations.

## Overview
Video-based manipulation provides object-centric motion priors from human demonstrations, generated videos, or RGB-D observations, but such priors are typically embodiment-agnostic and cannot be directly executed by a specific robot. This paper presents **PhysV2A**, a reachability-gated and semantic-mask-constrained feasibility-completion framework for converting video-derived 6D object motion into robot-executable manipulation trajectories. The key idea is to treat grasp feasibility as trajectory-conditioned rather than local: each RGB-D-generated 6-DoF grasp candidate is rigidly coupled with the recovered object motion to form a grasp-conditioned TCP trajectory hypothesis. PhysV2A then performs hierarchical reachability-gated selection, where infeasible grasp–trajectory pairs are rejected by robot-centric kinematic checks and surviving candidates are ranked by downstream execution suitability. For the selected reachable trajectory, a VLM-assisted and rule-validated S-Mask identifies task-critical and relaxable Cartesian components, enabling semantic-mask-constrained manipulability refinement through redundancy-first optimization and bounded Cartesian relaxation. Real-robot experiments on four tabletop manipulation tasks show that PhysV2A improves task success over representative video-prior and IK-only baselines, reduces kinematic-feasibility failures, and produces better-conditioned trajectories with bounded semantic deviations.

## Content
Video-based manipulation provides object-centric motion priors from human demonstrations, generated videos, or RGB-D observations, but such priors are typically embodiment-agnostic and cannot be directly executed by a specific robot. This paper presents **PhysV2A**, a reachability-gated and semantic-mask-constrained feasibility-completion framework for converting video-derived 6D object motion into robot-executable manipulation trajectories. The key idea is to treat grasp feasibility as trajectory-conditioned rather than local: each RGB-D-generated 6-DoF grasp candidate is rigidly coupled with the recovered object motion to form a grasp-conditioned TCP trajectory hypothesis. PhysV2A then performs hierarchical reachability-gated selection, where infeasible grasp–trajectory pairs are rejected by robot-centric kinematic checks and surviving candidates are ranked by downstream execution suitability. For the selected reachable trajectory, a VLM-assisted and rule-validated S-Mask identifies task-critical and relaxable Cartesian components, enabling semantic-mask-constrained manipulability refinement through redundancy-first optimization and bounded Cartesian relaxation. Real-robot experiments on four tabletop manipulation tasks show that PhysV2A improves task success over representative video-prior and IK-only baselines, reduces kinematic-feasibility failures, and produces better-conditioned trajectories with bounded semantic deviations.

## 개요
비디오 기반 조작은 인간 시연, 생성된 비디오 또는 RGB-D 관측을 통해 객체 중심의 운동 사전 정보를 제공하지만, 이러한 사전 정보는 일반적으로 구현 방식에 구애받지 않으며 특정 로봇이 직접 실행할 수 없습니다. 본 논문은 비디오에서 추출된 6D 객체 운동을 로봇이 실행 가능한 조작 궤적으로 변환하기 위한 **PhysV2A**라는 도달 가능성 게이트 및 의미 마스크 제약 기반 실행 가능성 완성 프레임워크를 제시합니다. 핵심 아이디어는 파지 가능성을 국소적이 아닌 궤적 조건부로 처리하는 것입니다. RGB-D로 생성된 각 6-DoF 파지 후보는 복원된 객체 운동과 강체적으로 결합되어 파지 조건부 TCP 궤적 가설을 형성합니다. 그런 다음 PhysV2A는 계층적 도달 가능성 게이트 선택을 수행하여, 실행 불가능한 파지-궤적 쌍을 로봇 중심의 운동학적 검사를 통해 거부하고, 생존한 후보를 하위 실행 적합성에 따라 순위를 매깁니다. 선택된 도달 가능 궤적에 대해 VLM 지원 및 규칙 검증된 S-마스크가 작업에 중요한 카르테시안 구성 요소와 완화 가능한 구성 요소를 식별하여, 중복성 우선 최적화와 제한된 카르테시안 완화를 통해 의미 마스크 제약 기반 조작성 개선을 가능하게 합니다. 네 가지 탁상 조작 작업에 대한 실제 로봇 실험에서 PhysV2A는 대표적인 비디오 사전 및 IK 전용 기준선보다 작업 성공률을 향상시키고, 운동학적 실행 가능성 실패를 줄이며, 제한된 의미 편차를 가진 더 나은 조건의 궤적을 생성함을 보여줍니다.

## 핵심 내용
비디오 기반 조작은 인간 시연, 생성된 비디오 또는 RGB-D 관측을 통해 객체 중심의 운동 사전 정보를 제공하지만, 이러한 사전 정보는 일반적으로 구현 방식에 구애받지 않으며 특정 로봇이 직접 실행할 수 없습니다. 본 논문은 비디오에서 추출된 6D 객체 운동을 로봇이 실행 가능한 조작 궤적으로 변환하기 위한 **PhysV2A**라는 도달 가능성 게이트 및 의미 마스크 제약 기반 실행 가능성 완성 프레임워크를 제시합니다. 핵심 아이디어는 파지 가능성을 국소적이 아닌 궤적 조건부로 처리하는 것입니다. RGB-D로 생성된 각 6-DoF 파지 후보는 복원된 객체 운동과 강체적으로 결합되어 파지 조건부 TCP 궤적 가설을 형성합니다. 그런 다음 PhysV2A는 계층적 도달 가능성 게이트 선택을 수행하여, 실행 불가능한 파지-궤적 쌍을 로봇 중심의 운동학적 검사를 통해 거부하고, 생존한 후보를 하위 실행 적합성에 따라 순위를 매깁니다. 선택된 도달 가능 궤적에 대해 VLM 지원 및 규칙 검증된 S-마스크가 작업에 중요한 카르테시안 구성 요소와 완화 가능한 구성 요소를 식별하여, 중복성 우선 최적화와 제한된 카르테시안 완화를 통해 의미 마스크 제약 기반 조작성 개선을 가능하게 합니다. 네 가지 탁상 조작 작업에 대한 실제 로봇 실험에서 PhysV2A는 대표적인 비디오 사전 및 IK 전용 기준선보다 작업 성공률을 향상시키고, 운동학적 실행 가능성 실패를 줄이며, 제한된 의미 편차를 가진 더 나은 조건의 궤적을 생성함을 보여줍니다.

## 参考
- http://arxiv.org/abs/2607.09365v1
