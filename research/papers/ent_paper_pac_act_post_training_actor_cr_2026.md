---
$id: ent_paper_pac_act_post_training_actor_cr_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PAC-ACT: Post-training Actor-Critic for Action Chunking Transformers'
  zh: 'PAC-ACT: Post-training Actor-Critic for Action Chunking Transformers'
  ko: 'PAC-ACT: Post-training Actor-Critic for Action Chunking Transformers'
summary:
  en: 'arXiv:2607.09590v1 Announce Type: new Abstract: Precision industrial contact manipulation requires reliable robot policies
    under pose perturbations and contact-force constraints. Vision-language-action models offer broad generalization but often
    introduce high inference latency and GPU-memory cost, while vision-action chunking policies are more suitable for real-time
    industrial control. However, these policies are usually trained by behavior cloning and suffer from distribution shift
    in contact-rich tasks. This paper proposes PAC-ACT, a reinforcement-learning post-training framework for pretrained Action
    Chunking Transformer policies. PAC-ACT reformulates policy optimization at the chunk level, constructs an ACT-transferred
    actor-critic architecture, and introduces a hybrid behavior-prior constraint to preserve the pretrained action distribution
    during online fine-tuning. Experiments on industrial precision-contact benchmarks show that PAC-ACT improves task success,
    contact stability, and force safety while retaining low latency and low GPU-memory usage. On the Contour task, PAC-ACT
    significantly reduces peak contact force and decreases the proportion of force readings above 60 N by 46 times. Sparse-reward
    ablations further show that the proposed behavior-prior constraint enables effective exploration under randomized initial
    poses.'
  zh: PAC-ACT 是一个针对预训练 Action Chunking Transformer 策略的强化学习后训练框架，由研究团队提出。其核心贡献在于通过块级策略优化、ACT 迁移的 actor-critic 架构和混合行为先验约束，在保持低延迟和低
    GPU 内存占用的同时，显著提升了工业精密接触操作的成功率、接触稳定性和力安全性。
  ko: 'arXiv:2607.09590v1 Announce Type: new Abstract: Precision industrial contact manipulation requires reliable robot policies
    under pose perturbations and contact-force constraints. Vision-language-action models offer broad generalization but often
    introduce high inference latency and GPU-memory cost, while vision-action chunking policies are more suitable for real-time
    industrial control. However, these policies are usually trained by behavior cloning and suffer from distribution shift
    in contact-rich tasks. This paper proposes PAC-ACT, a reinforcement-learning post-training framework for pretrained Action
    Chunking Transformer policies. PAC-ACT reformulates policy optimization at the chunk level, constructs an ACT-transferred
    actor-critic architecture, and introduces a hybrid behavior-prior constraint to preserve the pretrained action distribution
    during online fine-tuning. Experiments on industrial precision-contact benchmarks show that PAC-ACT improves task success,
    contact stability, and force safety while retaining low latency and low GPU-memory usage. On the Contour task, PAC-ACT
    significantly reduces peak contact force and decreases the proportion of force readings above 60 N by 46 times. Sparse-reward
    ablations further show that the proposed behavior-prior constraint enables effective exploration under randomized initial
    poses.'
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
- pac_act
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.09590v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1021 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'PAC-ACT: Post-training Actor-Critic for Action Chunking Transformers (arXiv)'
  url: https://arxiv.org/abs/2607.09590
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
PAC-ACT 旨在解决预训练 Action Chunking Transformer 策略在接触密集型任务中因行为克隆训练导致的分布偏移问题。该框架将策略优化重新定义为块级别，构建了基于 ACT 迁移的 actor-critic 架构，并引入混合行为先验约束以在在线微调中保留预训练动作分布。在工业精密接触基准测试中，PAC-ACT 在保持低延迟和低 GPU 内存占用的前提下，提升了任务成功率、接触稳定性和力安全性。例如，在 Contour 任务中，PAC-ACT 将峰值接触力显著降低，并将超过 60 N 的力读数比例减少了 46 倍。

## 核心内容
### 方法
- **块级策略优化**：将预训练的 Action Chunking Transformer 策略的优化重新定义为块级别，以更好地适应接触操作中的时序动作依赖。
- **ACT 迁移的 actor-critic 架构**：基于 ACT 架构构建 actor-critic 网络，其中 actor 负责生成动作块，critic 评估状态-动作块的价值，从而支持强化学习训练。
- **混合行为先验约束**：引入一种混合约束，在在线微调过程中保留预训练的动作分布，防止策略在探索时偏离原始行为过远，从而缓解分布偏移问题。

### 实验设置
- **基准测试**：在工业精密接触操作基准上进行评估，包括 Contour 等任务。
- **对比基线**：与原始 ACT 策略及其他行为克隆方法进行对比。
- **评估指标**：任务成功率、接触稳定性（如峰值接触力）、力安全性（如超过 60 N 的力读数比例）、推理延迟和 GPU 内存占用。

### 关键结果
- **性能提升**：PAC-ACT 在任务成功率和接触稳定性上均优于基线方法，同时保持了低延迟和低 GPU 内存占用。
- **力安全性**：在 Contour 任务中，PAC-ACT 将峰值接触力显著降低，并将超过 60 N 的力读数比例减少了 46 倍。
- **稀疏奖励消融实验**：在随机初始位姿下，混合行为先验约束使策略能够进行有效探索，进一步验证了其鲁棒性。

### 结论
PAC-ACT 通过强化学习后训练框架，有效提升了预训练 Action Chunking Transformer 策略在精密接触操作中的性能，同时避免了高推理延迟和 GPU 内存开销，适用于实时工业控制场景。

## Overview
Precision industrial contact manipulation requires reliable robot policies under pose perturbations and contact-force constraints. Vision-language-action models offer broad generalization but often introduce high inference latency and GPU-memory cost, while vision-action chunking policies are more suitable for real-time industrial control. However, these policies are usually trained by behavior cloning and suffer from distribution shift in contact-rich tasks. This paper proposes PAC-ACT, a reinforcement-learning post-training framework for pretrained Action Chunking Transformer policies. PAC-ACT reformulates policy optimization at the chunk level, constructs an ACT-transferred actor-critic architecture, and introduces a hybrid behavior-prior constraint to preserve the pretrained action distribution during online fine-tuning. Experiments on industrial precision-contact benchmarks show that PAC-ACT improves task success, contact stability, and force safety while retaining low latency and low GPU-memory usage. On the Contour task, PAC-ACT significantly reduces peak contact force and decreases the proportion of force readings above 60 N by 46 times. Sparse-reward ablations further show that the proposed behavior-prior constraint enables effective exploration under randomized initial poses.

## 参考
- http://arxiv.org/abs/2607.09590v1

## 개요
PAC-ACT는 사전 훈련된 Action Chunking Transformer 정책이 접촉 집약적 작업에서 행동 복제 훈련으로 인해 발생하는 분포 이동 문제를 해결하는 것을 목표로 합니다. 이 프레임워크는 정책 최적화를 블록 수준으로 재정의하고, ACT 전이 기반 actor-critic 아키텍처를 구축하며, 혼합 행동 사전 제약을 도입하여 온라인 미세 조정 중 사전 훈련된 행동 분포를 유지합니다. 산업용 정밀 접촉 벤치마크에서 PAC-ACT는 낮은 지연 시간과 낮은 GPU 메모리 사용량을 유지하면서 작업 성공률, 접촉 안정성 및 힘 안전성을 향상시킵니다. 예를 들어, Contour 작업에서 PAC-ACT는 최대 접촉 힘을 크게 줄이고 60 N을 초과하는 힘 판독 비율을 46배 감소시킵니다.

## 핵심 내용
### 방법
- **블록 수준 정책 최적화**: 사전 훈련된 Action Chunking Transformer 정책의 최적화를 블록 수준으로 재정의하여 접촉 조작의 시간적 행동 의존성에 더 잘 적응시킵니다.
- **ACT 전이 기반 actor-critic 아키텍처**: ACT 아키텍처를 기반으로 actor-critic 네트워크를 구축하며, actor는 행동 블록을 생성하고 critic은 상태-행동 블록의 가치를 평가하여 강화 학습 훈련을 지원합니다.
- **혼합 행동 사전 제약**: 온라인 미세 조정 중 사전 훈련된 행동 분포를 유지하는 혼합 제약을 도입하여 정책이 탐색 중 원래 행동에서 너무 멀리 벗어나는 것을 방지함으로써 분포 이동 문제를 완화합니다.

### 실험 설정
- **벤치마크**: Contour 등의 작업을 포함한 산업용 정밀 접촉 조작 벤치마크에서 평가합니다.
- **비교 기준선**: 원래 ACT 정책 및 기타 행동 복제 방법과 비교합니다.
- **평가 지표**: 작업 성공률, 접촉 안정성(예: 최대 접촉 힘), 힘 안전성(예: 60 N 초과 힘 판독 비율), 추론 지연 시간 및 GPU 메모리 사용량.

### 주요 결과
- **성능 향상**: PAC-ACT는 작업 성공률과 접촉 안정성에서 기준선 방법보다 우수하며, 낮은 지연 시간과 낮은 GPU 메모리 사용량을 유지합니다.
- **힘 안전성**: Contour 작업에서 PAC-ACT는 최대 접촉 힘을 크게 줄이고 60 N을 초과하는 힘 판독 비율을 46배 감소시킵니다.
- **희소 보상 제거 실험**: 무작위 초기 자세에서 혼합 행동 사전 제약은 정책이 효과적으로 탐색할 수 있게 하여 견고성을 추가로 검증합니다.

### 결론
PAC-ACT는 강화 학습 후 훈련 프레임워크를 통해 사전 훈련된 Action Chunking Transformer 정책의 정밀 접촉 조작 성능을 효과적으로 향상시키면서 높은 추론 지연 시간과 GPU 메모리 오버헤드를 피하여 실시간 산업 제어 시나리오에 적합합니다.
