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
  zh: 'arXiv:2607.09590v1 Announce Type: new Abstract: Precision industrial contact manipulation requires reliable robot policies
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.09590v1.
sources:
- id: src_001
  type: paper
  title: 'PAC-ACT: Post-training Actor-Critic for Action Chunking Transformers (arXiv)'
  url: https://arxiv.org/abs/2607.09590
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
Precision industrial contact manipulation requires reliable robot policies under pose perturbations and contact-force constraints. Vision-language-action models offer broad generalization but often introduce high inference latency and GPU-memory cost, while vision-action chunking policies are more suitable for real-time industrial control. However, these policies are usually trained by behavior cloning and suffer from distribution shift in contact-rich tasks. This paper proposes PAC-ACT, a reinforcement-learning post-training framework for pretrained Action Chunking Transformer policies. PAC-ACT reformulates policy optimization at the chunk level, constructs an ACT-transferred actor-critic architecture, and introduces a hybrid behavior-prior constraint to preserve the pretrained action distribution during online fine-tuning. Experiments on industrial precision-contact benchmarks show that PAC-ACT improves task success, contact stability, and force safety while retaining low latency and low GPU-memory usage. On the Contour task, PAC-ACT significantly reduces peak contact force and decreases the proportion of force readings above 60 N by 46 times. Sparse-reward ablations further show that the proposed behavior-prior constraint enables effective exploration under randomized initial poses.

## 核心内容
Precision industrial contact manipulation requires reliable robot policies under pose perturbations and contact-force constraints. Vision-language-action models offer broad generalization but often introduce high inference latency and GPU-memory cost, while vision-action chunking policies are more suitable for real-time industrial control. However, these policies are usually trained by behavior cloning and suffer from distribution shift in contact-rich tasks. This paper proposes PAC-ACT, a reinforcement-learning post-training framework for pretrained Action Chunking Transformer policies. PAC-ACT reformulates policy optimization at the chunk level, constructs an ACT-transferred actor-critic architecture, and introduces a hybrid behavior-prior constraint to preserve the pretrained action distribution during online fine-tuning. Experiments on industrial precision-contact benchmarks show that PAC-ACT improves task success, contact stability, and force safety while retaining low latency and low GPU-memory usage. On the Contour task, PAC-ACT significantly reduces peak contact force and decreases the proportion of force readings above 60 N by 46 times. Sparse-reward ablations further show that the proposed behavior-prior constraint enables effective exploration under randomized initial poses.

## 参考
- http://arxiv.org/abs/2607.09590v1

## Overview
Precision industrial contact manipulation requires reliable robot policies under pose perturbations and contact-force constraints. Vision-language-action models offer broad generalization but often introduce high inference latency and GPU-memory cost, while vision-action chunking policies are more suitable for real-time industrial control. However, these policies are usually trained by behavior cloning and suffer from distribution shift in contact-rich tasks. This paper proposes PAC-ACT, a reinforcement-learning post-training framework for pretrained Action Chunking Transformer policies. PAC-ACT reformulates policy optimization at the chunk level, constructs an ACT-transferred actor-critic architecture, and introduces a hybrid behavior-prior constraint to preserve the pretrained action distribution during online fine-tuning. Experiments on industrial precision-contact benchmarks show that PAC-ACT improves task success, contact stability, and force safety while retaining low latency and low GPU-memory usage. On the Contour task, PAC-ACT significantly reduces peak contact force and decreases the proportion of force readings above 60 N by 46 times. Sparse-reward ablations further show that the proposed behavior-prior constraint enables effective exploration under randomized initial poses.

## Content
Precision industrial contact manipulation requires reliable robot policies under pose perturbations and contact-force constraints. Vision-language-action models offer broad generalization but often introduce high inference latency and GPU-memory cost, while vision-action chunking policies are more suitable for real-time industrial control. However, these policies are usually trained by behavior cloning and suffer from distribution shift in contact-rich tasks. This paper proposes PAC-ACT, a reinforcement-learning post-training framework for pretrained Action Chunking Transformer policies. PAC-ACT reformulates policy optimization at the chunk level, constructs an ACT-transferred actor-critic architecture, and introduces a hybrid behavior-prior constraint to preserve the pretrained action distribution during online fine-tuning. Experiments on industrial precision-contact benchmarks show that PAC-ACT improves task success, contact stability, and force safety while retaining low latency and low GPU-memory usage. On the Contour task, PAC-ACT significantly reduces peak contact force and decreases the proportion of force readings above 60 N by 46 times. Sparse-reward ablations further show that the proposed behavior-prior constraint enables effective exploration under randomized initial poses.

## 개요
정밀 산업 접촉 조작은 자세 변동과 접촉력 제약 하에서 신뢰할 수 있는 로봇 정책을 필요로 합니다. 시각-언어-행동 모델은 광범위한 일반화를 제공하지만 종종 높은 추론 지연 시간과 GPU 메모리 비용을 초래하는 반면, 시각-행동 청킹 정책은 실시간 산업 제어에 더 적합합니다. 그러나 이러한 정책은 일반적으로 행동 복제로 훈련되며 접촉이 많은 작업에서 분포 변화를 겪습니다. 본 논문은 사전 훈련된 Action Chunking Transformer 정책을 위한 강화 학습 사후 훈련 프레임워크인 PAC-ACT를 제안합니다. PAC-ACT는 청크 수준에서 정책 최적화를 재구성하고, ACT 전이된 행위자-비평가 아키텍처를 구축하며, 온라인 미세 조정 중 사전 훈련된 행동 분포를 보존하기 위해 하이브리드 행동 사전 제약을 도입합니다. 산업 정밀 접촉 벤치마크에 대한 실험은 PAC-ACT가 낮은 지연 시간과 낮은 GPU 메모리 사용량을 유지하면서 작업 성공률, 접촉 안정성 및 힘 안전성을 향상시킴을 보여줍니다. Contour 작업에서 PAC-ACT는 최대 접촉력을 크게 줄이고 60 N 이상의 힘 판독 비율을 46배 감소시킵니다. 희소 보상 절제 실험은 제안된 행동 사전 제약이 무작위 초기 자세 하에서 효과적인 탐색을 가능하게 함을 추가로 보여줍니다.

## 핵심 내용
정밀 산업 접촉 조작은 자세 변동과 접촉력 제약 하에서 신뢰할 수 있는 로봇 정책을 필요로 합니다. 시각-언어-행동 모델은 광범위한 일반화를 제공하지만 종종 높은 추론 지연 시간과 GPU 메모리 비용을 초래하는 반면, 시각-행동 청킹 정책은 실시간 산업 제어에 더 적합합니다. 그러나 이러한 정책은 일반적으로 행동 복제로 훈련되며 접촉이 많은 작업에서 분포 변화를 겪습니다. 본 논문은 사전 훈련된 Action Chunking Transformer 정책을 위한 강화 학습 사후 훈련 프레임워크인 PAC-ACT를 제안합니다. PAC-ACT는 청크 수준에서 정책 최적화를 재구성하고, ACT 전이된 행위자-비평가 아키텍처를 구축하며, 온라인 미세 조정 중 사전 훈련된 행동 분포를 보존하기 위해 하이브리드 행동 사전 제약을 도입합니다. 산업 정밀 접촉 벤치마크에 대한 실험은 PAC-ACT가 낮은 지연 시간과 낮은 GPU 메모리 사용량을 유지하면서 작업 성공률, 접촉 안정성 및 힘 안전성을 향상시킴을 보여줍니다. Contour 작업에서 PAC-ACT는 최대 접촉력을 크게 줄이고 60 N 이상의 힘 판독 비율을 46배 감소시킵니다. 희소 보상 절제 실험은 제안된 행동 사전 제약이 무작위 초기 자세 하에서 효과적인 탐색을 가능하게 함을 추가로 보여줍니다.
