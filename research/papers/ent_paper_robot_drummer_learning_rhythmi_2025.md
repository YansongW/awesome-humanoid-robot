---
$id: ent_paper_robot_drummer_learning_rhythmi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Robot Drummer: Learning Rhythmic Skills for Humanoid Drumming'
  zh: 'Robot Drummer: Learning Rhythmic Skills for Humanoid Drumming'
  ko: 'Robot Drummer: Learning Rhythmic Skills for Humanoid Drumming'
summary:
  en: 'Robot Drummer: Learning Rhythmic Skills for Humanoid Drumming is a 2025 work on manipulation for humanoid robots.'
  zh: Robot Drummer 是 2025 年提出的一项人形机器人操作研究，旨在让机器人学会富有表现力且高精度的鼓乐演奏。其核心贡献在于将鼓谱转化为节奏接触链，并通过强化学习并行训练分段策略，使机器人能够完成长达数分钟的复杂多肢体协调任务。
  ko: 'Robot Drummer: Learning Rhythmic Skills for Humanoid Drumming is a 2025 work on manipulation for humanoid robots.'
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
- manipulation
- robot_drummer
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.11498v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Robot Drummer: Learning Rhythmic Skills for Humanoid Drumming (arXiv)'
  url: https://arxiv.org/abs/2507.11498
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
人形机器人在灵巧性、平衡与运动方面取得了显著进展，但在音乐表演等表达性领域的应用仍属空白。鼓乐演奏对机器人提出了独特挑战，包括毫秒级的时间精度、快速接触以及多肢体协调。为此，研究者将鼓谱转化为节奏接触链，并将每首乐曲分解为固定长度的片段，通过强化学习并行训练单一策略。在超过三十首摇滚、金属和爵士乐歌曲上的实验表明，Robot Drummer 能够稳定获得高 F1 分数，并展现出交叉臂击打、自适应鼓棒分配等类人策略。

## 核心内容
### 方法
- **问题建模**：将人形机器人鼓乐演奏形式化为按顺序完成定时接触的任务。
- **节奏接触链**：将鼓谱转化为一系列带时间戳的接触事件，作为策略学习的输入。
- **分段训练**：为应对音乐表演的长时域特性，将每首乐曲分解为固定长度的片段，并针对所有片段并行训练一个统一的策略。

### 实验设置
- **机器人平台**：采用人形机器人平台，具体型号未在正文中说明。
- **训练方法**：使用强化学习进行策略训练。
- **测试曲目**：涵盖超过三十首流行摇滚、金属和爵士乐歌曲。

### 关键结果
- **性能指标**：在所有测试曲目上均获得高 F1 分数，表明击打精度和节奏准确性优异。
- **涌现行为**：机器人学会了交叉臂击打和自适应鼓棒分配等类人策略，这些行为并非显式编程，而是通过强化学习自然涌现。

### 结论
该工作展示了强化学习在将人形机器人引入创意音乐表演领域的潜力，为机器人学习复杂、长时域、多肢体协调任务提供了有效框架。项目页面：robotdrummer.github.io

## Overview
Humanoid robots have seen remarkable advances in dexterity, balance, and locomotion, yet their role in expressive domains such as music performance remains largely unexplored. Musical tasks, like drumming, present unique challenges, including split-second timing, rapid contacts, and multi-limb coordination over performances lasting minutes. In this paper, we introduce Robot Drummer, a humanoid capable of expressive, high-precision drumming across a diverse repertoire of songs. We formulate humanoid drumming as sequential fulfillment of timed contacts and transform drum scores into a Rhythmic Contact Chain. To handle the long-horizon nature of musical performance, we decompose each piece into fixed-length segments and train a single policy across all segments in parallel using reinforcement learning. Through extensive experiments on over thirty popular rock, metal, and jazz tracks, our results demonstrate that Robot Drummer consistently achieves high F1 scores. The learned behaviors exhibit emergent human-like drumming strategies, such as cross-arm strikes, and adaptive stick assignments, demonstrating the potential of reinforcement learning to bring humanoid robots into the domain of creative musical performance. Project page: robotdrummer.github.io

## 개요
휴머노이드 로봇은 손재주, 균형, 보행에서 놀라운 발전을 이루었지만, 음악 연주와 같은 표현적 영역에서의 역할은 아직 거의 탐구되지 않았습니다. 드럼 연주와 같은 음악적 작업은 순간적인 타이밍, 빠른 접촉, 수 분간 지속되는 연주에서의 다중 사지 협응 등 독특한 도전 과제를 제시합니다. 본 논문에서는 다양한 노래 레퍼토리에 걸쳐 표현력이 뛰어나고 정밀도 높은 드럼 연주가 가능한 휴머노이드 로봇, Robot Drummer를 소개합니다. 우리는 휴머노이드 드럼 연주를 시간 제약이 있는 접촉의 순차적 수행으로 정식화하고, 드럼 악보를 리듬 접촉 체인(Rhythmic Contact Chain)으로 변환합니다. 음악 연주의 장기적 특성을 처리하기 위해 각 곡을 고정 길이 세그먼트로 분해하고, 강화 학습을 사용하여 모든 세그먼트에 걸쳐 단일 정책을 병렬로 훈련합니다. 30개 이상의 인기 있는 록, 메탈, 재즈 트랙에 대한 광범위한 실험을 통해 Robot Drummer가 일관되게 높은 F1 점수를 달성함을 입증했습니다. 학습된 행동은 교차 팔 스트라이크, 적응형 스틱 할당과 같은 인간과 유사한 드럼 연주 전략을 나타내며, 강화 학습이 휴머노이드 로봇을 창의적인 음악 연주 영역으로 이끌 가능성을 보여줍니다. 프로젝트 페이지: robotdrummer.github.io

## 핵심 내용
휴머노이드 로봇은 손재주, 균형, 보행에서 놀라운 발전을 이루었지만, 음악 연주와 같은 표현적 영역에서의 역할은 아직 거의 탐구되지 않았습니다. 드럼 연주와 같은 음악적 작업은 순간적인 타이밍, 빠른 접촉, 수 분간 지속되는 연주에서의 다중 사지 협응 등 독특한 도전 과제를 제시합니다. 본 논문에서는 다양한 노래 레퍼토리에 걸쳐 표현력이 뛰어나고 정밀도 높은 드럼 연주가 가능한 휴머노이드 로봇, Robot Drummer를 소개합니다. 우리는 휴머노이드 드럼 연주를 시간 제약이 있는 접촉의 순차적 수행으로 정식화하고, 드럼 악보를 리듬 접촉 체인(Rhythmic Contact Chain)으로 변환합니다. 음악 연주의 장기적 특성을 처리하기 위해 각 곡을 고정 길이 세그먼트로 분해하고, 강화 학습을 사용하여 모든 세그먼트에 걸쳐 단일 정책을 병렬로 훈련합니다. 30개 이상의 인기 있는 록, 메탈, 재즈 트랙에 대한 광범위한 실험을 통해 Robot Drummer가 일관되게 높은 F1 점수를 달성함을 입증했습니다. 학습된 행동은 교차 팔 스트라이크, 적응형 스틱 할당과 같은 인간과 유사한 드럼 연주 전략을 나타내며, 강화 학습이 휴머노이드 로봇을 창의적인 음악 연주 영역으로 이끌 가능성을 보여줍니다. 프로젝트 페이지: robotdrummer.github.io

## 参考
- http://arxiv.org/abs/2507.11498v2
