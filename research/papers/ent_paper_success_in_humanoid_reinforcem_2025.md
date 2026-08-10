---
$id: ent_paper_success_in_humanoid_reinforcem_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Success in Humanoid Reinforcement Learning under Partial Observation
  zh: Success in Humanoid Reinforcement Learning under Partial Observation
  ko: Success in Humanoid Reinforcement Learning under Partial Observation
summary:
  en: Success in Humanoid Reinforcement Learning under Partial Observation is a 2025 work on locomotion for humanoid robots.
  zh: 这是2025年关于人形机器人部分观测下强化学习的研究。该工作首次在Gymnasium Humanoid-v4基准环境中实现了基于不完整状态信息的稳定策略训练。核心贡献是提出了一种新型历史编码器，使策略在仅使用原始状态三分之一到三分之二的情况下，达到了与全状态访问相当的性能。
  ko: Success in Humanoid Reinforcement Learning under Partial Observation is a 2025 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- success_in_humanoid_reinforcem
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.18883v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (788 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Success in Humanoid Reinforcement Learning under Partial Observation (arXiv)
  url: https://arxiv.org/abs/2507.18883
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该研究针对人形机器人运动控制中部分可观测性带来的挑战，在Gymnasium Humanoid-v4环境中实现了突破性进展。传统强化学习方法在此高维任务中难以处理不完整状态信息，而该工作通过设计并行处理固定长度历史观测序列的编码器，成功解决了这一难题。实验表明，学习到的策略不仅性能与全状态方法持平，还能适应机器人本体属性变化（如肢体质量差异）。研究团队认为，该编码器能够从近期观测中重建关键上下文信息，从而支撑鲁棒决策。

## 核心内容
### 研究背景
强化学习在机器人控制中应用广泛，但部分可观测性下的策略学习仍是重大挑战，尤其在人形机器人运动这类高维任务中。此前，在Gymnasium Humanoid-v4基准环境中，尚无工作能基于不完整状态信息实现稳定训练。该环境的目标是让机器人尽可能快向前行走而不摔倒，奖励函数包含保持直立和前进的激励，并对过度动作和外部接触力施加惩罚。

### 核心方法
- **历史编码器**：创新性地设计了一种并行处理固定长度历史观测序列的编码器，将其集成到标准无模型强化学习算法中。
- **状态压缩**：仅使用原始状态的三分之一到三分之二，即可实现与全状态访问基线相当的性能。
- **适应性验证**：策略展现出对机器人本体属性的鲁棒性，例如能适应不同肢体质量的配置变化。

### 实验设置与结果
- **环境**：Gymnasium Humanoid-v4
- **性能对比**：在部分观测条件下，策略性能与当前全状态最优结果（state-of-the-art）持平
- **关键发现**：研究假设该编码器通过从近期观测中重构关键上下文信息，使决策过程具备鲁棒性

### 结论
该工作首次证明了在Humanoid-v4环境中基于部分观测进行强化学习的可行性，为高维机器人控制任务中处理不完整状态信息提供了有效方案。

## Overview
Reinforcement learning has been widely applied to robotic control, but effective policy learning under partial observability remains a major challenge, especially in high-dimensional tasks like humanoid locomotion. To date, no prior work has demonstrated stable training of humanoid policies with incomplete state information in the benchmark Gymnasium Humanoid-v4 environment. The objective in this environment is to walk forward as fast as possible without falling, with rewards provided for staying upright and moving forward, and penalties incurred for excessive actions and external contact forces. This research presents the first successful instance of learning under partial observability in this environment. The learned policy achieves performance comparable to state-of-the-art results with full state access, despite using only one-third to two-thirds of the original states. Moreover, the policy exhibits adaptability to robot properties, such as variations in body part masses. The key to this success is a novel history encoder that processes a fixed-length sequence of past observations in parallel. Integrated into a standard model-free algorithm, the encoder enables performance on par with fully observed baselines. We hypothesize that it reconstructs essential contextual information from recent observations, thereby enabling robust decision-making.

## 参考
- http://arxiv.org/abs/2507.18883v1

## 개요
이 연구는 휴머노이드 로봇 운동 제어에서 부분 관측 가능성이 제기하는 도전 과제를 Gymnasium Humanoid-v4 환경에서 획기적으로 해결했습니다. 전통적인 강화 학습 방법은 이러한 고차원 작업에서 불완전한 상태 정보를 처리하기 어려운 반면, 이 작업은 고정 길이의 과거 관측 시퀀스를 병렬로 처리하는 인코더를 설계하여 이 문제를 성공적으로 해결했습니다. 실험 결과, 학습된 정책은 전체 상태 방법과 성능이 동등할 뿐만 아니라 로봇 본체 속성 변화(예: 팔다리 질량 차이)에도 적응할 수 있음을 보여줍니다. 연구팀은 이 인코더가 최근 관측에서 핵심 컨텍스트 정보를 재구성하여 강건한 의사 결정을 지원할 수 있다고 판단합니다.

## 핵심 내용
### 연구 배경
강화 학습은 로봇 제어에 널리 적용되지만, 부분 관측 가능성 하에서의 정책 학습은 특히 휴머노이드 로봇 운동과 같은 고차원 작업에서 여전히 중요한 도전 과제입니다. 이전에는 Gymnasium Humanoid-v4 벤치마크 환경에서 불완전한 상태 정보를 기반으로 안정적인 훈련을 달성한 작업이 없었습니다. 이 환경의 목표는 로봇이 넘어지지 않고 가능한 한 빨리 앞으로 걷는 것이며, 보상 함수는 직립 유지와 전진에 대한 인센티브를 포함하고 과도한 동작과 외부 접촉 힘에 대해 패널티를 부과합니다.

### 핵심 방법
- **히스토리 인코더**: 고정 길이의 과거 관측 시퀀스를 병렬로 처리하는 인코더를 혁신적으로 설계하여 표준 모델 프리 강화 학습 알고리즘에 통합했습니다.
- **상태 압축**: 원래 상태의 1/3에서 2/3만 사용하여 전체 상태 접근 기준선과 동등한 성능을 달성했습니다.
- **적응성 검증**: 정책은 로봇 본체 속성에 대한 강건성을 보여주며, 예를 들어 다양한 팔다리 질량 구성 변화에 적응할 수 있습니다.

### 실험 설정 및 결과
- **환경**: Gymnasium Humanoid-v4
- **성능 비교**: 부분 관측 조건에서 정책 성능은 현재 전체 상태 최적 결과(state-of-the-art)와 동등합니다.
- **주요 발견**: 연구는 이 인코더가 최근 관측에서 핵심 컨텍스트 정보를 재구성하여 의사 결정 과정을 강건하게 만든다고 가정합니다.

### 결론
이 작업은 Humanoid-v4 환경에서 부분 관측을 기반으로 한 강화 학습의 가능성을 처음으로 입증했으며, 고차원 로봇 제어 작업에서 불완전한 상태 정보를 처리하는 효과적인 솔루션을 제공합니다.
