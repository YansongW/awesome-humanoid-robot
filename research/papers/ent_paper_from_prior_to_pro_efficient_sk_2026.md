---
$id: ent_paper_from_prior_to_pro_efficient_sk_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'From Prior to Pro: Efficient Skill Mastery via Distribution Contractive RL Finetuning'
  zh: 'From Prior to Pro: Efficient Skill Mastery via Distribution Contractive RL Finetuning'
  ko: 'From Prior to Pro: Efficient Skill Mastery via Distribution Contractive RL Finetuning'
summary:
  en: 'arXiv:2603.10263v2 Announce Type: replace Abstract: We introduce Distribution Contractive Reinforcement Learning (DICE-RL),
    a framework that uses reinforcement learning (RL) as a "distribution contraction" operator to refine pretrained generative
    robot policies. DICE-RL turns a pretrained behavior prior into a high-performing "pro" policy by amplifying high-success
    behaviors from online feedback. We pretrain a diffusion- or flow-based policy for broad behavioral coverage, then finetune
    it with a stable, sample-efficient residual off-policy RL framework that combines selective behavior regularization with
    value-guided action selection. Extensive experiments and analyses show that DICE-RL reliably improves performance with
    strong stability and sample efficiency. It enables mastery of complex long-horizon manipulation skills directly from high-dimensional
    pixel inputs, both in simulation and on a real robot. Project website: https://zhanyisun.github.io/dice.rl.2026/.'
  zh: DICE-RL 是由研究团队提出的机器人策略微调框架，将强化学习作为“分布收缩”算子，把预训练的生成式行为先验转化为高性能“专家”策略。其核心贡献在于结合选择性行为正则化与价值引导动作选择，实现了稳定且样本高效的残差离策略微调，在仿真和真实机器人上均能直接从高维像素输入掌握复杂长时程操作技能。
  ko: 'arXiv:2603.10263v2 Announce Type: replace Abstract: We introduce Distribution Contractive Reinforcement Learning (DICE-RL),
    a framework that uses reinforcement learning (RL) as a "distribution contraction" operator to refine pretrained generative
    robot policies. DICE-RL turns a pretrained behavior prior into a high-performing "pro" policy by amplifying high-success
    behaviors from online feedback. We pretrain a diffusion- or flow-based policy for broad behavioral coverage, then finetune
    it with a stable, sample-efficient residual off-policy RL framework that combines selective behavior regularization with
    value-guided action selection. Extensive experiments and analyses show that DICE-RL reliably improves performance with
    strong stability and sample efficiency. It enables mastery of complex long-horizon manipulation skills directly from high-dimensional
    pixel inputs, both in simulation and on a real robot. Project website: https://zhanyisun.github.io/dice.rl.2026/.'
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
- from_prior_to_pro
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.10263v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (890 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'From Prior to Pro: Efficient Skill Mastery via Distribution Contractive RL Finetuning (arXiv)'
  url: https://arxiv.org/abs/2603.10263
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述
DICE-RL 框架的核心思想是将强化学习视为一种“分布收缩”操作，用于精炼预训练的生成式机器人策略。它首先基于扩散或流模型预训练一个具有广泛行为覆盖的策略，然后通过一个稳定且样本高效的残差离策略微调框架进行优化。该框架巧妙融合了选择性行为正则化与价值引导动作选择，能够从在线反馈中放大高成功行为。大量实验与分析表明，DICE-RL 在提升性能的同时保持了出色的稳定性和样本效率，成功实现了在仿真和真实机器人上直接从高维像素输入掌握复杂长时程操作技能。

## 核心内容
### 方法概述
DICE-RL 将强化学习重新定义为一种“分布收缩”算子，其目标是将预训练的行为先验（prior）精炼为高性能的专家策略（pro）。该框架通过从在线交互反馈中放大高成功行为来实现这一转变。

### 架构与训练流程
1.  **预训练阶段**：首先基于扩散模型（diffusion model）或流模型（flow model）预训练一个策略，使其具备广泛的行为覆盖能力。
2.  **微调阶段**：采用一个稳定且样本高效的残差离策略强化学习框架进行微调。该框架包含两个关键组件：
    -   **选择性行为正则化**：在微调过程中有选择地约束策略，防止其偏离预训练先验中的有效行为模式。
    -   **价值引导动作选择**：利用价值函数指导动作选择，优先采纳预期回报更高的动作。

### 实验设置与关键结果
-   **任务与输入**：实验涉及复杂的、长时程的操作技能，策略直接基于高维像素输入（pixel inputs）进行决策。
-   **性能表现**：DICE-RL 在仿真环境和真实机器人上均能可靠地提升任务性能，展现出强大的稳定性和样本效率。
-   **关键优势**：相比传统方法，DICE-RL 能够更高效地掌握复杂技能，且无需大量在线交互数据即可实现性能提升。

### 结论
DICE-RL 提供了一种将预训练生成式策略转化为高性能专家策略的有效途径，通过分布收缩的视角统一了预训练与强化学习微调过程，为机器人技能学习提供了稳定且高效的解决方案。

## Overview
We introduce Distribution Contractive Reinforcement Learning (DICE-RL), a framework that uses reinforcement learning (RL) as a "distribution contraction" operator to refine pretrained generative robot policies. DICE-RL turns a pretrained behavior prior into a high-performing "pro" policy by amplifying high-success behaviors from online feedback. We pretrain a diffusion- or flow-based policy for broad behavioral coverage, then finetune it with a stable, sample-efficient residual off-policy RL framework that combines selective behavior regularization with value-guided action selection. Extensive experiments and analyses show that DICE-RL reliably improves performance with strong stability and sample efficiency. It enables mastery of complex long-horizon manipulation skills directly from high-dimensional pixel inputs, both in simulation and on a real robot. Project website: https://zhanyisun.github.io/dice.rl.2026/.

## 参考
- http://arxiv.org/abs/2603.10263v2

## 개요
DICE-RL 프레임워크의 핵심 아이디어는 강화 학습을 일종의 "분포 수축" 연산으로 간주하여 사전 훈련된 생성형 로봇 정책을 정제하는 것입니다. 먼저 확산 모델 또는 흐름 모델 기반으로 광범위한 행동 커버리지를 가진 정책을 사전 훈련한 다음, 안정적이고 샘플 효율적인 잔여 오프-정책 미세 조정 프레임워크를 통해 최적화합니다. 이 프레임워크는 선택적 행동 정규화와 가치 기반 행동 선택을 교묘하게 융합하여 온라인 피드백에서 높은 성공 행동을 증폭시킬 수 있습니다. 광범위한 실험과 분석을 통해 DICE-RL이 성능을 향상시키면서도 뛰어난 안정성과 샘플 효율성을 유지하며, 시뮬레이션 및 실제 로봇에서 고차원 픽셀 입력을 직접 처리하여 복잡한 장기간 조작 기술을 습득하는 데 성공했음을 보여줍니다.

## 핵심 내용
### 방법 개요
DICE-RL은 강화 학습을 "분포 수축" 연산자로 재정의하며, 그 목표는 사전 훈련된 행동 사전(prior)을 고성능 전문가 정책(pro)으로 정제하는 것입니다. 이 프레임워크는 온라인 상호작용 피드백에서 높은 성공 행동을 증폭시켜 이러한 전환을 실현합니다.

### 아키텍처 및 훈련 절차
1.  **사전 훈련 단계**: 먼저 확산 모델(diffusion model) 또는 흐름 모델(flow model) 기반으로 광범위한 행동 커버리지를 가진 정책을 사전 훈련합니다.
2.  **미세 조정 단계**: 안정적이고 샘플 효율적인 잔여 오프-정책 강화 학습 프레임워크를 사용하여 미세 조정합니다. 이 프레임워크는 두 가지 핵심 구성 요소를 포함합니다:
    -   **선택적 행동 정규화**: 미세 조정 과정에서 정책을 선택적으로 제약하여 사전 훈련된 사전의 유효한 행동 패턴에서 벗어나는 것을 방지합니다.
    -   **가치 기반 행동 선택**: 가치 함수를 사용하여 행동 선택을 안내하고, 기대 보상이 더 높은 행동을 우선적으로 채택합니다.

### 실험 설정 및 주요 결과
-   **작업 및 입력**: 실험은 복잡하고 장기간 지속되는 조작 기술을 포함하며, 정책은 고차원 픽셀 입력(pixel inputs)을 기반으로 직접 결정을 내립니다.
-   **성능**: DICE-RL은 시뮬레이션 환경과 실제 로봇 모두에서 작업 성능을 안정적으로 향상시키며, 강력한 안정성과 샘플 효율성을 보여줍니다.
-   **주요 장점**: 기존 방법에 비해 DICE-RL은 복잡한 기술을 더 효율적으로 습득할 수 있으며, 많은 온라인 상호작용 데이터 없이도 성능 향상을 달성할 수 있습니다.

### 결론
DICE-RL은 사전 훈련된 생성형 정책을 고성능 전문가 정책으로 전환하는 효과적인 방법을 제공하며, 분포 수축 관점을 통해 사전 훈련과 강화 학습 미세 조정 과정을 통합하여 로봇 기술 학습을 위한 안정적이고 효율적인 솔루션을 제공합니다.
