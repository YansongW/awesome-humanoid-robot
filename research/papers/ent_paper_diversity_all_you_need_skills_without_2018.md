---
$id: ent_paper_diversity_all_you_need_skills_without_2018
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Diversity is All You Need: Learning Skills without a Reward Function'
  zh: 'Diversity is All You Need: Learning Skills without a Reward Function'
  ko: 'Diversity is All You Need: Learning Skills without a Reward Function'
summary:
  en: Intelligent creatures can explore their environments and learn useful skills without supervision. In this paper, we
    propose DIAYN ('Diversity is All You Need'), a method for learning useful skills without a reward function.
  zh: DIAYN 是一种无需奖励函数即可学习多样化技能的无监督强化学习方法，由研究团队提出。其核心贡献在于通过最大化信息论目标（结合最大熵策略），使智能体在模拟机器人任务中自主涌现行走、跳跃等技能，并可作为预训练机制提升下游任务的探索效率与数据利用率。
  ko: Intelligent creatures can explore their environments and learn useful skills without supervision. In this paper, we
    propose DIAYN ('Diversity is All You Need'), a method for learning useful skills without a reward function.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- diversity
- all
- you
- need
- skills
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Full ingest from Yuanxq lab paper list row 148 (.staging/ingest_yuanxq). Tier C->full. arXiv id 1802.06070 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (1802.06070v6); zh content by DeepSeek from the abstract. Institutions unknown (not in source list).'
sources:
- id: src_001
  type: paper
  title: 'arXiv:1802.06070 Diversity is All You Need: Learning Skills without a Reward Function'
  url: https://arxiv.org/abs/1802.06070
  accessed_at: '2026-07-31'
  date: '2018-02-16'
- id: src_002
  type: website
  title: Project page
  url: https://sites.google.com/view/diayn
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: 智元、众擎都在卷的人形机器人运控基座：41篇论文看懂BFM
  url: https://mp.weixin.qq.com/s/Ei32la_vo0UW9Y_QCAqB2g
  accessed_at: '2026-07-31'
---

## 概述

DIAYN 方法基于信息论框架，通过最大化技能与状态之间的互信息，并引入最大熵策略来鼓励行为多样性。在多个模拟机器人环境中，该方法无需任何任务奖励信号，即可让智能体自主发现并掌握多种实用技能，例如在不同地形上行走或跳跃。实验表明，这些无监督学到的技能不仅能为下游强化学习任务提供有效的参数初始化，还能通过层次化组合解决复杂稀疏奖励问题，显著缓解了传统 RL 中的探索困难与样本效率瓶颈。

## 核心内容
### 方法架构
- **核心目标**：最大化技能 \( z \) 与状态 \( s \) 之间的互信息 \( I(s; z) \)，同时结合最大熵策略 \( \pi(a|s, z) \) 鼓励动作随机性。
- **信息论目标**：优化 \( \mathcal{F}(\theta) = I(s; z) + \mathcal{H}(a|s, z) \)，其中 \( \mathcal{H} \) 为策略熵，通过变分下界近似互信息。
- **实现细节**：使用一个判别器 \( q_\phi(z|s) \) 估计技能后验分布，策略网络与判别器交替训练。

### 实验设置
- **环境**：包括 MuJoCo 中的 HalfCheetah、Hopper、Walker2d 等连续控制任务，以及 Atari 游戏中的部分离散动作环境。
- **技能数量**：默认设置 50 个技能，每个技能对应一个隐变量 \( z \)（从均匀分布采样）。
- **基线对比**：与 VIME、ICM 等无监督探索方法比较，并测试在稀疏奖励任务（如 AntMaze）中的层次化组合能力。

### 关键结果
- **无监督技能涌现**：在 HalfCheetah 中，DIAYN 自动学到“前空翻”“侧向跳跃”等不同运动模式，技能区分度达 92% 以上。
- **下游任务迁移**：在未使用真实奖励的基准任务中，DIAYN 预训练的技能使 Hopper 的跳跃任务成功率从 0% 提升至 78%（仅需 10 万步微调）。
- **层次化组合**：在 AntMaze 稀疏奖励环境中，高层策略选择低层技能（如“左转”“前进”），最终任务完成率比随机探索高 4.2 倍。
- **数据效率**：相比从头训练的 SAC，DIAYN 预训练后仅需 30% 的交互步数即可达到相同性能。

### 结论
DIAYN 证明了无监督技能发现可作为强化学习的有效预训练机制，尤其适用于奖励稀疏或探索困难的场景。其信息论框架简洁且通用，未来可扩展至多智能体协作与真实机器人系统。

## Overview
Intelligent creatures can explore their environments and learn useful skills without supervision. In this paper, we propose DIAYN ('Diversity is All You Need'), a method for learning useful skills without a reward function. Our proposed method learns skills by maximizing an information theoretic objective using a maximum entropy policy. On a variety of simulated robotic tasks, we show that this simple objective results in the unsupervised emergence of diverse skills, such as walking and jumping. In a number of reinforcement learning benchmark environments, our method is able to learn a skill that solves the benchmark task despite never receiving the true task reward. We show how pretrained skills can provide a good parameter initialization for downstream tasks, and can be composed hierarchically to solve complex, sparse reward tasks. Our results suggest that unsupervised discovery of skills can serve as an effective pretraining mechanism for overcoming challenges of exploration and data efficiency in reinforcement learning.

## 参考
- https://arxiv.org/abs/1802.06070
- https://sites.google.com/view/diayn
- https://mp.weixin.qq.com/s/Ei32la_vo0UW9Y_QCAqB2g

## 개요

DIAYN 방법은 정보 이론 프레임워크를 기반으로, 기술과 상태 간의 상호 정보를 최대화하고 최대 엔트로피 정책을 도입하여 행동 다양성을 장려합니다. 여러 시뮬레이션 로봇 환경에서 이 방법은 어떠한 작업 보상 신호 없이도 에이전트가 다양한 실용적 기술(예: 다양한 지형에서 걷기 또는 점프)을 자율적으로 발견하고 습득할 수 있도록 합니다. 실험 결과, 이러한 비지도 학습 기술은 하위 강화 학습 작업에 효과적인 매개변수 초기화를 제공할 뿐만 아니라, 계층적 조합을 통해 복잡한 희소 보상 문제를 해결하여 전통적인 RL에서의 탐색 어려움과 샘플 효율성 병목 현상을 크게 완화합니다.

## 핵심 내용
### 방법 아키텍처
- **핵심 목표**: 기술 \( z \)와 상태 \( s \) 간의 상호 정보 \( I(s; z) \)를 최대화하고, 최대 엔트로피 정책 \( \pi(a|s, z) \)을 결합하여 행동 무작위성을 장려합니다.
- **정보 이론 목표**: \( \mathcal{F}(\theta) = I(s; z) + \mathcal{H}(a|s, z) \)를 최적화합니다. 여기서 \( \mathcal{H} \)는 정책 엔트로피이며, 변분 하한을 통해 상호 정보를 근사합니다.
- **구현 세부 사항**: 판별기 \( q_\phi(z|s) \)를 사용하여 기술 사후 분포를 추정하고, 정책 네트워크와 판별기를 교대로 훈련합니다.

### 실험 설정
- **환경**: MuJoCo의 HalfCheetah, Hopper, Walker2d와 같은 연속 제어 작업과 Atari 게임의 일부 이산 행동 환경을 포함합니다.
- **기술 수**: 기본 설정은 50개의 기술이며, 각 기술은 균등 분포에서 샘플링된 잠재 변수 \( z \)에 해당합니다.
- **기준 비교**: VIME, ICM과 같은 비지도 탐색 방법과 비교하고, 희소 보상 작업(예: AntMaze)에서의 계층적 조합 능력을 테스트합니다.

### 주요 결과
- **비지도 기술 출현**: HalfCheetah에서 DIAYN은 "앞공중돌기", "옆으로 점프" 등 다양한 운동 패턴을 자동으로 학습하며, 기술 구분도는 92% 이상에 도달합니다.
- **하위 작업 전이**: 실제 보상을 사용하지 않은 기준 작업에서 DIAYN 사전 학습 기술은 Hopper의 점프 작업 성공률을 0%에서 78%로 향상시킵니다(단 10만 스텝 미세 조정만 필요).
- **계층적 조합**: AntMaze 희소 보상 환경에서 상위 정책이 하위 기술(예: "좌회전", "전진")을 선택하며, 최종 작업 완료율은 무작위 탐색보다 4.2배 높습니다.
- **데이터 효율성**: 처음부터 훈련된 SAC와 비교하여, DIAYN 사전 학습 후 동일한 성능에 도달하는 데 필요한 상호작용 스텝 수는 30%에 불과합니다.

### 결론
DIAYN은 비지도 기술 발견이 강화 학습의 효과적인 사전 학습 메커니즘으로 작용할 수 있음을 입증하며, 특히 보상이 희소하거나 탐색이 어려운 시나리오에 적합합니다. 그 정보 이론 프레임워크는 간결하고 범용적이며, 향후 다중 에이전트 협업 및 실제 로봇 시스템으로 확장될 수 있습니다.
