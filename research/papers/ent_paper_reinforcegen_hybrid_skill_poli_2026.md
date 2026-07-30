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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.16861v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
장기간 조작(Long-horizon manipulation)은 로보틱스 커뮤니티에서 오랜 도전 과제였습니다. 우리는 작업 분해, 데이터 생성, 모방 학습 및 모션 플래닝을 결합하여 초기 솔루션을 형성하고, 강화 학습 기반의 미세 조정을 통해 각 구성 요소를 개선하는 시스템인 ReinforceGen을 제안합니다. ReinforceGen은 먼저 작업을 여러 개의 지역화된 스킬로 분할하고, 이를 모션 플래닝을 통해 연결합니다. 스킬과 모션 플래닝 목표는 10개의 인간 시연에서 생성된 데이터셋을 사용한 모방 학습으로 훈련된 후, 온라인 적응 및 강화 학습을 통해 미세 조정됩니다. Robosuite 데이터셋에서 벤치마킹했을 때, ReinforceGen은 가장 높은 리셋 범위 설정에서 시각-운동 제어(visuomotor controls)를 사용한 모든 작업에서 80%의 성공률을 달성했습니다. 추가 절제 연구(ablation studies)에 따르면, 우리의 미세 조정 접근 방식은 평균 성능을 89% 향상시키는 데 기여합니다. 마지막으로, ReinforceGen은 실제 환경 평가에서 미세 조정을 통해 상당한 개선을 보여줍니다. 더 많은 결과와 비디오는 https://reinforcegen.github.io에서 확인할 수 있습니다.

## 핵심 내용
장기간 조작(Long-horizon manipulation)은 로보틱스 커뮤니티에서 오랜 도전 과제였습니다. 우리는 작업 분해, 데이터 생성, 모방 학습 및 모션 플래닝을 결합하여 초기 솔루션을 형성하고, 강화 학습 기반의 미세 조정을 통해 각 구성 요소를 개선하는 시스템인 ReinforceGen을 제안합니다. ReinforceGen은 먼저 작업을 여러 개의 지역화된 스킬로 분할하고, 이를 모션 플래닝을 통해 연결합니다. 스킬과 모션 플래닝 목표는 10개의 인간 시연에서 생성된 데이터셋을 사용한 모방 학습으로 훈련된 후, 온라인 적응 및 강화 학습을 통해 미세 조정됩니다. Robosuite 데이터셋에서 벤치마킹했을 때, ReinforceGen은 가장 높은 리셋 범위 설정에서 시각-운동 제어(visuomotor controls)를 사용한 모든 작업에서 80%의 성공률을 달성했습니다. 추가 절제 연구(ablation studies)에 따르면, 우리의 미세 조정 접근 방식은 평균 성능을 89% 향상시키는 데 기여합니다. 마지막으로, ReinforceGen은 실제 환경 평가에서 미세 조정을 통해 상당한 개선을 보여줍니다. 더 많은 결과와 비디오는 https://reinforcegen.github.io에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2512.16861v2
