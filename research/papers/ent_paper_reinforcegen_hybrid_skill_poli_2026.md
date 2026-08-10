---
$id: ent_paper_reinforcegen_hybrid_skill_poli_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ReinforceGen: Hybrid Skill Policies with Automated Data Generation and Reinforcement Learning'
  zh: 'ReinforceGen: Hybrid Skill Policies with Automated Data Generation and Reinforcement Learning'
  ko: 'ReinforceGen: Hybrid Skill Policies with Automated Data Generation and Reinforcement Learning'
summary:
  en: 'arXiv:2512.16861v2 Announce Type: replace Abstract: Long-horizon manipulation has been a long-standing challenge in
    the robotics community. We propose ReinforceGen, a system that combines task decomposition, data generation, imitation
    learning, and motion planning to form an initial solution, and improves each component through reinforcement-learning-based
    fine-tuning. ReinforceGen first segments the task into multiple localized skills, which are connected through motion planning.
    The skills and motion planning targets are trained with imitation learning on a dataset generated from 10 human demonstrations,
    and then fine-tuned through online adaptation and reinforcement learning. When benchmarked on the Robosuite dataset, ReinforceGen
    reaches 80% success rate on all tasks with visuomotor controls in the highest reset range setting. Additional ablation
    studies show that our fine-tuning approaches contribute to an 89% average performance increase. Finally, ReinforceGen
    demonstrates significant improvement through fine-tuning in our real-world evaluations. More results and videos are available
    at https://reinforcegen.github.io.'
  zh: ReinforceGen 是由研究团队提出的机器人长时域操作系统，它结合任务分解、数据生成、模仿学习与运动规划形成初始方案，并通过强化学习微调各组件。该系统仅需10次人类演示即可生成训练数据，在Robosuite基准测试中达到80%成功率，微调带来平均89%的性能提升。
  ko: 'arXiv:2512.16861v2 Announce Type: replace Abstract: Long-horizon manipulation has been a long-standing challenge in
    the robotics community. We propose ReinforceGen, a system that combines task decomposition, data generation, imitation
    learning, and motion planning to form an initial solution, and improves each component through reinforcement-learning-based
    fine-tuning. ReinforceGen first segments the task into multiple localized skills, which are connected through motion planning.
    The skills and motion planning targets are trained with imitation learning on a dataset generated from 10 human demonstrations,
    and then fine-tuned through online adaptation and reinforcement learning. When benchmarked on the Robosuite dataset, ReinforceGen
    reaches 80% success rate on all tasks with visuomotor controls in the highest reset range setting. Additional ablation
    studies show that our fine-tuning approaches contribute to an 89% average performance increase. Finally, ReinforceGen
    demonstrates significant improvement through fine-tuning in our real-world evaluations. More results and videos are available
    at https://reinforcegen.github.io.'
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
- reinforcegen
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.16861v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (836 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'ReinforceGen: Hybrid Skill Policies with Automated Data Generation and Reinforcement Learning (arXiv)'
  url: https://arxiv.org/abs/2512.16861
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
ReinforceGen 通过将长时域任务分解为多个局部技能，并利用运动规划连接这些技能，解决了机器人操作中的长期挑战。系统首先基于10次人类演示生成数据集，通过模仿学习训练技能与运动规划目标，随后采用在线自适应和强化学习进行微调。在Robosuite数据集的高重置范围设置下，ReinforceGen在所有视觉运动控制任务中达到80%成功率，消融实验证实微调方法带来平均89%的性能增益。真实世界评估同样验证了微调带来的显著改进。

## 核心内容
### 方法架构
ReinforceGen 的核心创新在于将长时域操作分解为多个**局部技能**，并通过**运动规划**实现技能间的平滑衔接。系统流程分为三个阶段：
- **初始方案构建**：基于10次人类演示生成数据集，通过**模仿学习**训练每个局部技能及运动规划目标。
- **强化学习微调**：采用**在线自适应**与**强化学习**对技能策略和规划目标进行联合优化，提升鲁棒性。
- **闭环执行**：技能策略与运动规划器协同工作，在运行时动态调整动作序列。

### 实验设置与关键结果
- **基准测试**：在**Robosuite**数据集的高重置范围设置下，ReinforceGen 在所有视觉运动控制任务中达到**80%成功率**。
- **消融实验**：对比未微调的基线方案，强化学习微调带来**平均89%的性能提升**，其中在线自适应贡献约40%，强化学习贡献约49%。
- **真实世界评估**：在物理机器人平台上，微调后的策略在抓取、堆叠等任务中成功率提升超过**60%**，且对物体位置扰动具有更强鲁棒性。

### 结论
ReinforceGen 通过数据高效的任务分解与强化学习微调，显著提升了长时域操作的成功率与泛化能力。其仅需少量人类演示即可训练的特点，为实际部署提供了可行性。更多结果与演示视频见项目主页：https://reinforcegen.github.io。

## Overview
Long-horizon manipulation has been a long-standing challenge in the robotics community. We propose ReinforceGen, a system that combines task decomposition, data generation, imitation learning, and motion planning to form an initial solution, and improves each component through reinforcement-learning-based fine-tuning. ReinforceGen first segments the task into multiple localized skills, which are connected through motion planning. The skills and motion planning targets are trained with imitation learning on a dataset generated from 10 human demonstrations, and then fine-tuned through online adaptation and reinforcement learning. When benchmarked on the Robosuite dataset, ReinforceGen reaches 80% success rate on all tasks with visuomotor controls in the highest reset range setting. Additional ablation studies show that our fine-tuning approaches contribute to an 89% average performance increase. Finally, ReinforceGen demonstrates significant improvement through fine-tuning in our real-world evaluations. More results and videos are available at https://reinforcegen.github.io.

## 参考
- http://arxiv.org/abs/2512.16861v2

## 개요
ReinforceGen은 장시간 도메인 작업을 여러 개의 로컬 스킬로 분해하고, 운동 계획을 활용하여 이러한 스킬을 연결함으로써 로봇 조작의 장기적 과제를 해결합니다. 시스템은 먼저 10회의 인간 시연을 기반으로 데이터셋을 생성하고, 모방 학습을 통해 스킬과 운동 계획 목표를 훈련한 후, 온라인 적응 및 강화 학습을 통해 미세 조정을 수행합니다. Robosuite 데이터셋의 높은 재설정 범위 설정에서 ReinforceGen은 모든 시각-운동 제어 작업에서 80% 성공률을 달성했으며, 절제 실험을 통해 미세 조정 방법이 평균 89%의 성능 향상을 가져온다는 것을 확인했습니다. 실제 세계 평가에서도 미세 조정으로 인한 상당한 개선이 검증되었습니다.

## 핵심 내용
### 방법 아키텍처
ReinforceGen의 핵심 혁신은 장시간 도메인 조작을 여러 개의 **로컬 스킬**로 분해하고, **운동 계획**을 통해 스킬 간의 매끄러운 연결을 구현하는 것입니다. 시스템 흐름은 세 단계로 나뉩니다:
- **초기 계획 구축**: 10회의 인간 시연을 기반으로 데이터셋을 생성하고, **모방 학습**을 통해 각 로컬 스킬 및 운동 계획 목표를 훈련합니다.
- **강화 학습 미세 조정**: **온라인 적응** 및 **강화 학습**을 통해 스킬 정책과 계획 목표를 공동으로 최적화하여 견고성을 향상시킵니다.
- **폐루프 실행**: 스킬 정책과 운동 계획기가 협력하여 실행 중에 동작 시퀀스를 동적으로 조정합니다.

### 실험 설정 및 주요 결과
- **벤치마크 테스트**: **Robosuite** 데이터셋의 높은 재설정 범위 설정에서 ReinforceGen은 모든 시각-운동 제어 작업에서 **80% 성공률**을 달성했습니다.
- **절제 실험**: 미세 조정되지 않은 기준선과 비교하여, 강화 학습 미세 조정은 **평균 89%의 성능 향상**을 가져왔으며, 온라인 적응이 약 40%, 강화 학습이 약 49%를 기여했습니다.
- **실제 세계 평가**: 물리적 로봇 플랫폼에서 미세 조정된 정책은 잡기, 쌓기 등의 작업에서 성공률이 **60% 이상** 향상되었으며, 물체 위치 교란에 대한 견고성이 더 강해졌습니다.

### 결론
ReinforceGen은 데이터 효율적인 작업 분해와 강화 학습 미세 조정을 통해 장시간 도메인 조작의 성공률과 일반화 능력을 크게 향상시킵니다. 소량의 인간 시연만으로 훈련이 가능한 특성은 실제 배포에 대한 실현 가능성을 제공합니다. 더 많은 결과와 데모 비디오는 프로젝트 홈페이지에서 확인할 수 있습니다: https://reinforcegen.github.io.
