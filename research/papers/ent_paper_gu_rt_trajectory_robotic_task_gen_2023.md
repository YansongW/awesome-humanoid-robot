---
$id: ent_paper_gu_rt_trajectory_robotic_task_gen_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches'
  zh: RT-Trajectory
  ko: 'RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches'
summary:
  en: 'RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches (RT-Trajectory), is a 2023 generalized
    vision-language-action model for robotic manipulation, introduced by Google DeepMind, University of California San Diego,
    Stanford University, Intrinsic, and published at ICLR 2023.'
  zh: RT-Trajectory 是 Google DeepMind 等机构于 2023 年提出的通用视觉-语言-动作模型，通过粗糙轨迹草图实现机器人操作任务泛化。其核心贡献在于将任务表示为轨迹草图，使策略能执行训练数据中未见过的新任务，并在真实世界任务中优于语言条件与目标条件策略。
  ko: 'RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches (RT-Trajectory), is a 2023 generalized
    vision-language-action model for robotic manipulation, introduced by Google DeepMind, University of California San Diego,
    Stanford University, Intrinsic, and published at ICLR 2023.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- robotic_manipulation
- rt_trajectory
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2311.01977v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (939 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: RT-Trajectory source
  url: https://openreview.net/forum?id=F1TKzG8LJO
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
RT-Trajectory 针对机器人学习中的任务泛化难题，提出以粗糙轨迹草图作为策略条件。这种草图在细节上足以表达低层运动引导，同时保持粗糙性以允许策略结合视觉观察灵活解读。轨迹草图可通过人类输入（如手绘或视频）或自动方法（如图像生成或路径点生成）指定，为与机器人策略交互提供了实用接口。大规模真实世界实验表明，在相同训练数据下，RT-Trajectory 能执行比语言条件与目标条件策略更广泛的任务。

## 核心内容
### 方法
- **核心思想**：将任务表示为粗糙轨迹草图，而非精确轨迹。草图在运动引导与视觉上下文解读间取得平衡，使策略能泛化到新任务（如从 pick-and-place 泛化到 folding）。
- **条件机制**：策略以轨迹草图作为输入条件，结合当前视觉观察生成动作。草图不要求精确坐标，仅提供大致运动路径。
- **交互接口**：轨迹草图可通过多种方式生成：
  - 人类输入：手绘草图或演示视频。
  - 自动方法：利用现代图像生成模型（如扩散模型）或路径点生成算法。

### 实验设置
- **任务范围**：涵盖多种真实世界机器人操作任务，包括 pick-and-place、folding、rearrangement 等。
- **对比基线**：语言条件策略（如 RT-2）与目标条件策略（如 goal-conditioned policies）。
- **训练数据**：所有策略使用相同的训练数据集，确保公平比较。

### 关键结果
- RT-Trajectory 在未见任务上的成功率显著高于基线。例如，在 folding 任务中，语言条件策略因缺乏任务描述而失败，而 RT-Trajectory 通过轨迹草图成功执行。
- 轨迹草图的有效性在于其粗糙性：过于精确的轨迹会限制策略的适应性，而过于模糊则无法提供足够引导。
- 自动生成的轨迹草图（如通过图像生成模型）与人类输入效果相当，表明该方法可扩展至大规模应用。

### 结论
RT-Trajectory 通过轨迹草图实现了机器人任务泛化的突破，为策略交互提供了灵活接口，并在真实世界实验中验证了其有效性。未来工作可探索更复杂的草图生成方法及多任务联合训练。

## Overview
Generalization remains one of the most important desiderata for robust robot learning systems. While recently proposed approaches show promise in generalization to novel objects, semantic concepts, or visual distribution shifts, generalization to new tasks remains challenging. For example, a language-conditioned policy trained on pick-and-place tasks will not be able to generalize to a folding task, even if the arm trajectory of folding is similar to pick-and-place. Our key insight is that this kind of generalization becomes feasible if we represent the task through rough trajectory sketches. We propose a policy conditioning method using such rough trajectory sketches, which we call RT-Trajectory, that is practical, easy to specify, and allows the policy to effectively perform new tasks that would otherwise be challenging to perform. We find that trajectory sketches strike a balance between being detailed enough to express low-level motion-centric guidance while being coarse enough to allow the learned policy to interpret the trajectory sketch in the context of situational visual observations. In addition, we show how trajectory sketches can provide a useful interface to communicate with robotic policies: they can be specified through simple human inputs like drawings or videos, or through automated methods such as modern image-generating or waypoint-generating methods. We evaluate RT-Trajectory at scale on a variety of real-world robotic tasks, and find that RT-Trajectory is able to perform a wider range of tasks compared to language-conditioned and goal-conditioned policies, when provided the same training data.

## 参考
- http://arxiv.org/abs/2311.01977v2

## 개요
RT-Trajectory는 로봇 학습에서의 작업 일반화 문제를 해결하기 위해, 대략적인 궤적 스케치를 정책 조건으로 제안합니다. 이러한 스케치는 저수준 동작 안내를 표현하기에 충분한 세부 정보를 포함하면서도, 정책이 시각적 관찰과 결합하여 유연하게 해석할 수 있도록 대략적인 특성을 유지합니다. 궤적 스케치는 인간 입력(예: 손그림 또는 비디오) 또는 자동 방법(예: 이미지 생성 또는 경유점 생성)을 통해 지정될 수 있으며, 로봇 정책과의 상호작용을 위한 실용적인 인터페이스를 제공합니다. 대규모 실제 세계 실험에서, RT-Trajectory는 동일한 훈련 데이터를 사용할 때 언어 조건 및 목표 조건 정책보다 더 넓은 범위의 작업을 수행할 수 있음을 보여줍니다.

## 핵심 내용
### 방법
- **핵심 아이디어**: 작업을 정확한 궤적이 아닌 대략적인 궤적 스케치로 표현합니다. 스케치는 동작 안내와 시각적 맥락 해석 사이의 균형을 유지하여, 정책이 새로운 작업(예: pick-and-place에서 folding으로의 일반화)으로 확장될 수 있게 합니다.
- **조건 메커니즘**: 정책은 궤적 스케치를 입력 조건으로 사용하며, 현재 시각적 관찰과 결합하여 동작을 생성합니다. 스케치는 정확한 좌표를 요구하지 않으며, 대략적인 이동 경로만 제공합니다.
- **상호작용 인터페이스**: 궤적 스케치는 다양한 방식으로 생성될 수 있습니다:
  - 인간 입력: 손그림 스케치 또는 데모 비디오.
  - 자동 방법: 현대 이미지 생성 모델(예: 확산 모델) 또는 경유점 생성 알고리즘 활용.

### 실험 설정
- **작업 범위**: pick-and-place, folding, rearrangement 등 다양한 실제 세계 로봇 조작 작업을 포함합니다.
- **비교 기준선**: 언어 조건 정책(예: RT-2) 및 목표 조건 정책(예: goal-conditioned policies).
- **훈련 데이터**: 모든 정책은 동일한 훈련 데이터 세트를 사용하여 공정한 비교를 보장합니다.

### 주요 결과
- RT-Trajectory는 보지 못한 작업에서 기준선보다 훨씬 높은 성공률을 보여줍니다. 예를 들어, folding 작업에서 언어 조건 정책은 작업 설명 부족으로 실패하지만, RT-Trajectory는 궤적 스케치를 통해 성공적으로 수행합니다.
- 궤적 스케치의 효과는 대략적인 특성에 있습니다: 너무 정확한 궤적은 정책의 적응성을 제한하고, 너무 모호하면 충분한 안내를 제공하지 못합니다.
- 자동 생성된 궤적 스케치(예: 이미지 생성 모델을 통한)는 인간 입력과 유사한 성능을 보여, 이 방법이 대규모 응용으로 확장될 수 있음을 시사합니다.

### 결론
RT-Trajectory는 궤적 스케치를 통해 로봇 작업 일반화의 돌파구를 마련하고, 정책 상호작용을 위한 유연한 인터페이스를 제공하며, 실제 세계 실험에서 그 효과를 검증했습니다. 향후 연구는 더 복잡한 스케치 생성 방법 및 다중 작업 공동 훈련을 탐구할 수 있습니다.
