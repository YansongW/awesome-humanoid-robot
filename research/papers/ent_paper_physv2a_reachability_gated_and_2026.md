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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.09365v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (912 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2607.09365v1

## 개요
PhysV2A 프레임워크는 비디오 기반 조작에서 운동 사전(motion prior)과 구체적인 로봇 실행 사이의 괴리를 해결하는 것을 목표로 한다. 이는 각 RGB-D 생성 6자유도 그랩 후보를 복원된 객체 운동과 강체적으로 결합하여 그랩 조건화된 TCP 궤적 가설을 형성하고, 계층적 도달 가능성 게이팅 선택을 통해 실행 불가능한 그랩-궤적 쌍을 거부한다. 선택된 도달 가능 궤적에 대해 프레임워크는 VLM 보조 및 규칙 검증된 의미 마스크를 활용하여 작업 핵심 및 완화 가능한 데카르트 성분을 식별하고, 중복 우선 최적화와 유계 데카르트 완화를 통해 의미 마스크 제약된 조작성 정제를 수행한다. 네 개의 데스크톱 조작 작업에 대한 실제 로봇 실험에서 PhysV2A는 기준 방법 대비 작업 성공률을 향상시키고, 운동학적 실행 가능성 실패를 줄였으며, 조건이 더 우수하고 의미 편차가 유계인 궤적을 생성했다.

## 핵심 내용
### 방법 개요
PhysV2A 프레임워크의 핵심 혁신은 그랩 실행 가능성을 로컬 조건이 아닌 궤적 조건으로 간주하는 것이다. 구체적으로, RGB-D 데이터로 생성된 각 6자유도 그랩 후보는 복원된 객체 운동과 강체적으로 결합되어 그랩 조건화된 TCP 궤적 가설을 형성한다. 이후 프레임워크는 계층적 도달 가능성 게이팅 선택을 수행하여 로봇 중심 운동학 검사를 통해 실행 불가능한 그랩-궤적 쌍을 거부하고, 생존한 후보를 하류 실행 적합성에 따라 정렬한다.

### 아키텍처 및 핵심 구성 요소
- **도달 가능성 게이팅 선택**: 계층적 메커니즘을 채택하여 먼저 로봇 중심 운동학 검사를 통해 실행 불가능한 그랩-궤적 쌍을 필터링한 후, 남은 후보를 정렬하여 선택된 궤적이 운동학적으로 실행 가능하도록 보장한다.
- **의미 마스크 제약 정제**: 선택된 도달 가능 궤적에 대해 VLM 보조 및 규칙 검증된 의미 마스크(S-Mask)를 활용하여 작업 핵심 및 완화 가능한 데카르트 성분을 식별한다. 중복 우선 최적화와 유계 데카르트 완화를 통해 의미 마스크 제약된 조작성 정제를 구현하여 궤적이 의미적으로 유계이고 조건이 더 우수하도록 보장한다.

### 실험 설정 및 결과
- **작업 및 기준**: 네 개의 데스크톱 조작 작업에 대한 실제 로봇 실험을 수행했으며, 기준에는 대표적인 비디오 사전 방법과 IK 전용 방법이 포함된다.
- **주요 수치**: PhysV2A는 작업 성공률에서 기준 대비 유의미하게 우수하며, 운동학적 실행 가능성 실패를 줄이고 조건이 더 우수하며 의미 편차가 유계인 궤적을 생성했다. 구체적인 성공률 향상 및 실패 감소 수치는 초록에 명시되지 않았지만, 실험을 통해 그 효과가 검증되었다.

### 결론
PhysV2A는 그랩 실행 가능성을 궤적 조건으로 간주하고 도달 가능성 게이팅과 의미 마스크 제약을 결합하여 비디오의 객체 운동을 로봇 실행 가능 궤적으로 성공적으로 변환했으며, 실제 로봇 실험에서 우수한 성능을 입증했다.
