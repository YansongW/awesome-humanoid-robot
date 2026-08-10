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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03751v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (763 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2607.03751v1

## 개요
연구팀은 VLA 모델 실패의 핵심 병목이 동작 생성뿐만 아니라 동작 평가 능력의 결여에 있음을 발견했다. pass@k 진단 실험을 통해 동결된 VLA 모델의 출력 분포에 이미 충분히 많은 유효 행동이 포함되어 있으며, pass@32 성공률이 92%에 달함을 확인했다. 이 발견을 바탕으로 제안된 SVA 프레임워크는 먼저 시뮬레이션 환경에서 몬테카를로 트리 탐색을 사용해 VLA 출력 분포를 충분히 탐색하고 경험적 보상이 포함된 궤적 데이터를 수집한 다음, 이러한 지식을 경량 Q-값 모델로 증류하여 후보 동작을 평가하는 데 사용한다. 배포 시 동결된 VLA가 여러 후보 동작을 생성하고, 평가기가 불확실성 정규화 Q-값이 가장 높은 동작을 선택하며, 전체 과정에서 시뮬레이터에 접근할 필요가 없다.

## 핵심 내용
### 핵심 문제
- VLA 모델은 대규모 사전 학습을 통해 광범위한 구현 능력을 얻지만, 그 일반화 성능은 LLM 및 VLM보다 훨씬 약하다
- 기존 후학습 방법(지도 미세 조정/강화 학습)은 작업 성능을 향상시키지만 사전 학습에서 얻은 일반 능력을 약화시킨다

### 핵심 발견
- pass@k 진단 실험 결과: 동결 VLA는 pass@1에서 성공률이 33%에 불과하지만, pass@32에서는 92%로 향상된다
- VLA 출력 분포에 이미 충분히 많은 유효 행동이 포함되어 있으며, 실패의 주요 원인은 효과적인 동작 평가 메커니즘의 부재임을 입증

### SVA 프레임워크 구조
1. **탐색 단계(Search)**: 시뮬레이션 환경에서 몬테카를로 트리 탐색(MCTS)을 사용해 동결 VLA의 출력 분포를 충분히 탐색하고, 다양한 궤적을 수집하며 경험적 보상을 주석 처리
2. **증류 단계(Value)**: 탐색 지식을 경량 Q-값 모델로 증류하여 후보 동작의 예상 결과를 예측
3. **배포 단계(Act)**: 동결 VLA가 여러 후보 동작을 생성하고, 평가기가 불확실성 정규화 Q-값이 가장 높은 동작을 선택하며, 시뮬레이터 접근 불필요

### 실험 설정 및 결과
- 여러 구현 벤치마크에서 SVA는 미지 작업에 대한 일반화 능력을 지속적으로 향상시키고 강력한 테스트 시 확장 동작을 보여준다
- 핵심 비교: 9B 파라미터 VLA 모델에 SVA를 적용하면 27% 더 낮은 추론 지연 시간으로 27B 파라미터 VLA 모델을 성능에서 7% 포인트 능가
- 결론: 모델 규모 확장보다 테스트 시 평가 확장이 더 비용 효율적이다
