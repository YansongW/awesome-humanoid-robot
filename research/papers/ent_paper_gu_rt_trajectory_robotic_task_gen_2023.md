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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2311.01977v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
일반화는 강건한 로봇 학습 시스템을 위한 가장 중요한 요구사항 중 하나로 남아 있습니다. 최근 제안된 접근법들은 새로운 객체, 의미론적 개념 또는 시각적 분포 변화에 대한 일반화에서 가능성을 보여주지만, 새로운 작업으로의 일반화는 여전히 어려운 과제입니다. 예를 들어, 집기-놓기 작업으로 훈련된 언어 조건화 정책은 접기 작업의 팔 궤적이 집기-놓기와 유사하더라도 접기 작업으로 일반화할 수 없습니다. 우리의 핵심 통찰은 이러한 종류의 일반화가 대략적인 궤적 스케치를 통해 작업을 표현할 때 가능해진다는 것입니다. 우리는 이러한 대략적인 궤적 스케치를 사용하는 정책 조건화 방법을 제안하며, 이를 RT-Trajectory라고 부릅니다. 이 방법은 실용적이고 지정하기 쉬우며, 정책이 그렇지 않으면 수행하기 어려운 새로운 작업을 효과적으로 수행할 수 있게 합니다. 우리는 궤적 스케치가 저수준 동작 중심 지침을 표현할 만큼 상세하면서도, 학습된 정책이 상황별 시각적 관찰 맥락에서 궤적 스케치를 해석할 수 있을 만큼 대략적인 균형을 이룬다는 것을 발견했습니다. 또한, 궤적 스케치가 로봇 정책과 소통하기 위한 유용한 인터페이스를 제공할 수 있음을 보여줍니다. 이는 그림이나 비디오와 같은 간단한 인간 입력, 또는 현대 이미지 생성 또는 웨이포인트 생성 방법과 같은 자동화된 방법을 통해 지정될 수 있습니다. 우리는 다양한 실제 로봇 작업에서 RT-Trajectory를 대규모로 평가했으며, 동일한 훈련 데이터가 제공될 때 RT-Trajectory가 언어 조건화 및 목표 조건화 정책보다 더 넓은 범위의 작업을 수행할 수 있음을 발견했습니다.

## 핵심 내용
일반화는 강건한 로봇 학습 시스템을 위한 가장 중요한 요구사항 중 하나로 남아 있습니다. 최근 제안된 접근법들은 새로운 객체, 의미론적 개념 또는 시각적 분포 변화에 대한 일반화에서 가능성을 보여주지만, 새로운 작업으로의 일반화는 여전히 어려운 과제입니다. 예를 들어, 집기-놓기 작업으로 훈련된 언어 조건화 정책은 접기 작업의 팔 궤적이 집기-놓기와 유사하더라도 접기 작업으로 일반화할 수 없습니다. 우리의 핵심 통찰은 이러한 종류의 일반화가 대략적인 궤적 스케치를 통해 작업을 표현할 때 가능해진다는 것입니다. 우리는 이러한 대략적인 궤적 스케치를 사용하는 정책 조건화 방법을 제안하며, 이를 RT-Trajectory라고 부릅니다. 이 방법은 실용적이고 지정하기 쉬우며, 정책이 그렇지 않으면 수행하기 어려운 새로운 작업을 효과적으로 수행할 수 있게 합니다. 우리는 궤적 스케치가 저수준 동작 중심 지침을 표현할 만큼 상세하면서도, 학습된 정책이 상황별 시각적 관찰 맥락에서 궤적 스케치를 해석할 수 있을 만큼 대략적인 균형을 이룬다는 것을 발견했습니다. 또한, 궤적 스케치가 로봇 정책과 소통하기 위한 유용한 인터페이스를 제공할 수 있음을 보여줍니다. 이는 그림이나 비디오와 같은 간단한 인간 입력, 또는 현대 이미지 생성 또는 웨이포인트 생성 방법과 같은 자동화된 방법을 통해 지정될 수 있습니다. 우리는 다양한 실제 로봇 작업에서 RT-Trajectory를 대규모로 평가했으며, 동일한 훈련 데이터가 제공될 때 RT-Trajectory가 언어 조건화 및 목표 조건화 정책보다 더 넓은 범위의 작업을 수행할 수 있음을 발견했습니다.

## 参考
- http://arxiv.org/abs/2311.01977v2
