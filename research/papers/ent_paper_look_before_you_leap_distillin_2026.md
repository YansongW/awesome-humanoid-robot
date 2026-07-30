---
$id: ent_paper_look_before_you_leap_distillin_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Look Before You Leap: Distilling Tree Search into Action Evaluation for Frozen VLA Models'
  zh: 'Look Before You Leap: Distilling Tree Search into Action Evaluation for Frozen VLA Models'
  ko: 'Look Before You Leap: Distilling Tree Search into Action Evaluation for Frozen VLA Models'
summary:
  en: 'arXiv:2607.03751v1 Announce Type: new Abstract: Vision-Language-Action (VLA) models acquire broad embodied capabilities
    through large-scale pretraining, yet their generalization remains far more fragile than that of LLMs and VLMs. The prevailing
    remedy, post-training via supervised fine-tuning or reinforcement learning, improves task-specific performance but narrows
    the generalist capability that makes pretraining valuable. We identify a key bottleneck: VLA failures stem not only from
    action generation but also from action evaluation. A diagnostic pass@k study confirms that frozen VLAs already contain
    competent behaviors in their output distribution, with overall success rates rising from 33% at pass@1 to 92% at pass@32.
    Inspired by this, we propose SVA (Search, Value, and Act), a simple framework that equips frozen VLA policies with long-term
    consequence awareness. SVA first uses Monte-Carlo tree search in simulation to fully explore the VLA''s output distribution
    and collect diverse trajectories annotated with empirical returns; this knowledge is then distilled into a lightweight
    Q-value model that predicts the expected consequence of candidate actions; at deployment, the frozen VLA proposes multiple
    candidates and the evaluator selects the one with the highest uncertainty-regularized Q-value, requiring no simulator
    access. By decoupling action proposal from consequence evaluation, SVA preserves the generalization capacity of the VLA
    backbone while substantially improving task success rates. Experiments across embodied benchmarks show that SVA consistently
    improves generalization on unseen tasks and exhibits strong test-time scaling behavior. Strikingly, SVA enables a 9B VLA
    to outperform a 27B VLA by 7 points at 27% lower inference latency, suggesting that scaling test-time evaluation is more
    cost-effective than scaling model size.'
  zh: 本文提出SVA框架，通过将蒙特卡洛树搜索的探索结果蒸馏为轻量级Q值模型，为冻结的VLA模型赋予行动后果评估能力。该方法在保持基础模型泛化能力的同时，显著提升任务成功率，使9B参数VLA模型以27%更低推理延迟超越27B模型7个百分点。
  ko: 'arXiv:2607.03751v1 Announce Type: new Abstract: Vision-Language-Action (VLA) models acquire broad embodied capabilities
    through large-scale pretraining, yet their generalization remains far more fragile than that of LLMs and VLMs. The prevailing
    remedy, post-training via supervised fine-tuning or reinforcement learning, improves task-specific performance but narrows
    the generalist capability that makes pretraining valuable. We identify a key bottleneck: VLA failures stem not only from
    action generation but also from action evaluation. A diagnostic pass@k study confirms that frozen VLAs already contain
    competent behaviors in their output distribution, with overall success rates rising from 33% at pass@1 to 92% at pass@32.
    Inspired by this, we propose SVA (Search, Value, and Act), a simple framework that equips frozen VLA policies with long-term
    consequence awareness. SVA first uses Monte-Carlo tree search in simulation to fully explore the VLA''s output distribution
    and collect diverse trajectories annotated with empirical returns; this knowledge is then distilled into a lightweight
    Q-value model that predicts the expected consequence of candidate actions; at deployment, the frozen VLA proposes multiple
    candidates and the evaluator selects the one with the highest uncertainty-regularized Q-value, requiring no simulator
    access. By decoupling action proposal from consequence evaluation, SVA preserves the generalization capacity of the VLA
    backbone while substantially improving task success rates. Experiments across embodied benchmarks show that SVA consistently
    improves generalization on unseen tasks and exhibits strong test-time scaling behavior. Strikingly, SVA enables a 9B VLA
    to outperform a 27B VLA by 7 points at 27% lower inference latency, suggesting that scaling test-time evaluation is more
    cost-effective than scaling model size.'
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
- look_before_you_leap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03751v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Look Before You Leap: Distilling Tree Search into Action Evaluation for Frozen VLA Models (arXiv)'
  url: https://arxiv.org/abs/2607.03751
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
研究团队发现VLA模型失败的关键瓶颈不仅在于动作生成，更在于动作评估能力缺失。通过pass@k诊断实验证实，冻结的VLA模型输出分布中已包含足够多的有效行为，pass@32成功率可达92%。基于此发现提出的SVA框架，先在仿真环境中用蒙特卡洛树搜索充分探索VLA输出分布并收集带经验回报的轨迹数据，再将这些知识蒸馏为轻量级Q值模型用于评估候选动作。部署时冻结的VLA生成多个候选动作，由评估器选择不确定性正则化Q值最高的动作，整个过程无需访问仿真器。

## 核心内容
### 核心问题
- VLA模型通过大规模预训练获得广泛具身能力，但其泛化性远弱于LLM和VLM
- 现有后训练方法（监督微调/强化学习）虽提升任务性能，却削弱了预训练带来的通用能力

### 关键发现
- pass@k诊断实验显示：冻结VLA在pass@1时成功率仅33%，但pass@32时提升至92%
- 证明VLA输出分布中已包含足够多的有效行为，失败主因是缺乏有效的动作评估机制

### SVA框架架构
1. **搜索阶段（Search）**：在仿真环境中使用蒙特卡洛树搜索（MCTS）充分探索冻结VLA的输出分布，收集多样化轨迹并标注经验回报
2. **蒸馏阶段（Value）**：将搜索知识蒸馏为轻量级Q值模型，用于预测候选动作的预期后果
3. **部署阶段（Act）**：冻结VLA生成多个候选动作，评估器选择不确定性正则化Q值最高的动作，无需访问仿真器

### 实验设置与结果
- 在多个具身基准测试中，SVA持续提升未见任务的泛化能力，并展现强测试时扩展行为
- 关键对比：9B参数VLA模型配合SVA，以27%更低推理延迟，在性能上超越27B参数VLA模型7个百分点
- 结论：扩展测试时评估比扩展模型规模更具成本效益

## Overview
Vision-Language-Action (VLA) models acquire broad embodied capabilities through large-scale pretraining, yet their generalization remains far more fragile than that of LLMs and VLMs. The prevailing remedy, post-training via supervised fine-tuning or reinforcement learning, improves task-specific performance but narrows the generalist capability that makes pretraining valuable. We identify a key bottleneck: VLA failures stem not only from action generation but also from action evaluation. A diagnostic pass@k study confirms that frozen VLAs already contain competent behaviors in their output distribution, with overall success rates rising from 33% at pass@1 to 92% at pass@32. Inspired by this, we propose SVA (Search, Value, and Act), a simple framework that equips frozen VLA policies with long-term consequence awareness. SVA first uses Monte-Carlo tree search in simulation to fully explore the VLA's output distribution and collect diverse trajectories annotated with empirical returns; this knowledge is then distilled into a lightweight Q-value model that predicts the expected consequence of candidate actions; at deployment, the frozen VLA proposes multiple candidates and the evaluator selects the one with the highest uncertainty-regularized Q-value, requiring no simulator access. By decoupling action proposal from consequence evaluation, SVA preserves the generalization capacity of the VLA backbone while substantially improving task success rates. Experiments across embodied benchmarks show that SVA consistently improves generalization on unseen tasks and exhibits strong test-time scaling behavior. Strikingly, SVA enables a 9B VLA to outperform a 27B VLA by 7 points at 27% lower inference latency, suggesting that scaling test-time evaluation is more cost-effective than scaling model size.

## 개요
Vision-Language-Action (VLA) 모델은 대규모 사전 학습을 통해 광범위한 임베디드 능력을 습득하지만, 그 일반화 능력은 LLM 및 VLM에 비해 훨씬 취약합니다. 현재 널리 사용되는 해결책인 지도 미세 조정 또는 강화 학습을 통한 사후 학습은 특정 작업 성능을 향상시키지만, 사전 학습의 가치를 만드는 일반화 능력을 좁힙니다. 우리는 핵심 병목 현상을 식별했습니다: VLA의 실패는 행동 생성뿐만 아니라 행동 평가에서도 비롯됩니다. 진단적 pass@k 연구는 고정된 VLA가 이미 출력 분포 내에서 유능한 행동을 포함하고 있음을 확인했으며, pass@1에서 33%였던 전체 성공률이 pass@32에서 92%로 상승했습니다. 이에 영감을 받아, 우리는 SVA (Search, Value, and Act)라는 간단한 프레임워크를 제안합니다. 이는 고정된 VLA 정책에 장기적 결과 인식을 부여합니다. SVA는 먼저 시뮬레이션에서 몬테카를로 트리 검색을 사용하여 VLA의 출력 분포를 완전히 탐색하고 경험적 수익으로 주석이 달린 다양한 궤적을 수집합니다. 이 지식은 이후 경량 Q-값 모델로 증류되어 후보 행동의 예상 결과를 예측합니다. 배포 시, 고정된 VLA는 여러 후보를 제안하고 평가자는 불확실성 정규화된 Q-값이 가장 높은 것을 선택하며, 시뮬레이터 접근이 필요하지 않습니다. 행동 제안을 결과 평가에서 분리함으로써, SVA는 VLA 백본의 일반화 능력을 유지하면서 작업 성공률을 크게 향상시킵니다. 임베디드 벤치마크를 통한 실험은 SVA가 보지 못한 작업에서 일관되게 일반화를 개선하고 강력한 테스트 시간 스케일링 동작을 보여줍니다. 놀랍게도, SVA는 9B VLA가 27% 낮은 추론 지연 시간으로 27B VLA보다 7포인트 더 나은 성능을 발휘하게 하여, 모델 크기를 확장하는 것보다 테스트 시간 평가를 확장하는 것이 더 비용 효율적임을 시사합니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 대규모 사전 학습을 통해 광범위한 임베디드 능력을 습득하지만, 그 일반화 능력은 LLM 및 VLM에 비해 훨씬 취약합니다. 현재 널리 사용되는 해결책인 지도 미세 조정 또는 강화 학습을 통한 사후 학습은 특정 작업 성능을 향상시키지만, 사전 학습의 가치를 만드는 일반화 능력을 좁힙니다. 우리는 핵심 병목 현상을 식별했습니다: VLA의 실패는 행동 생성뿐만 아니라 행동 평가에서도 비롯됩니다. 진단적 pass@k 연구는 고정된 VLA가 이미 출력 분포 내에서 유능한 행동을 포함하고 있음을 확인했으며, pass@1에서 33%였던 전체 성공률이 pass@32에서 92%로 상승했습니다. 이에 영감을 받아, 우리는 SVA (Search, Value, and Act)라는 간단한 프레임워크를 제안합니다. 이는 고정된 VLA 정책에 장기적 결과 인식을 부여합니다. SVA는 먼저 시뮬레이션에서 몬테카를로 트리 검색을 사용하여 VLA의 출력 분포를 완전히 탐색하고 경험적 수익으로 주석이 달린 다양한 궤적을 수집합니다. 이 지식은 이후 경량 Q-값 모델로 증류되어 후보 행동의 예상 결과를 예측합니다. 배포 시, 고정된 VLA는 여러 후보를 제안하고 평가자는 불확실성 정규화된 Q-값이 가장 높은 것을 선택하며, 시뮬레이터 접근이 필요하지 않습니다. 행동 제안을 결과 평가에서 분리함으로써, SVA는 VLA 백본의 일반화 능력을 유지하면서 작업 성공률을 크게 향상시킵니다. 임베디드 벤치마크를 통한 실험은 SVA가 보지 못한 작업에서 일관되게 일반화를 개선하고 강력한 테스트 시간 스케일링 동작을 보여줍니다. 놀랍게도, SVA는 9B VLA가 27% 낮은 추론 지연 시간으로 27B VLA보다 7포인트 더 나은 성능을 발휘하게 하여, 모델 크기를 확장하는 것보다 테스트 시간 평가를 확장하는 것이 더 비용 효율적임을 시사합니다.

## 参考
- http://arxiv.org/abs/2607.03751v1
