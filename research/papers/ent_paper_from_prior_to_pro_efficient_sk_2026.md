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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.10263v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
우리는 분포 수축 강화 학습(DICE-RL)을 소개합니다. 이 프레임워크는 강화 학습(RL)을 "분포 수축" 연산자로 사용하여 사전 훈련된 생성 로봇 정책을 개선합니다. DICE-RL은 온라인 피드백에서 성공률이 높은 행동을 증폭시켜 사전 훈련된 행동 사전을 고성능 "프로" 정책으로 전환합니다. 우리는 확산 기반 또는 흐름 기반 정책을 사전 훈련하여 광범위한 행동 범위를 확보한 후, 선택적 행동 정규화와 가치 기반 행동 선택을 결합한 안정적이고 샘플 효율적인 잔차 오프-정책 RL 프레임워크로 미세 조정합니다. 광범위한 실험과 분석을 통해 DICE-RL이 강력한 안정성과 샘플 효율성으로 성능을 안정적으로 향상시킴을 보여줍니다. 이는 시뮬레이션과 실제 로봇 모두에서 고차원 픽셀 입력으로부터 직접 복잡한 장기 조작 기술을 습득할 수 있게 합니다. 프로젝트 웹사이트: https://zhanyisun.github.io/dice.rl.2026/.

## 핵심 내용
우리는 분포 수축 강화 학습(DICE-RL)을 소개합니다. 이 프레임워크는 강화 학습(RL)을 "분포 수축" 연산자로 사용하여 사전 훈련된 생성 로봇 정책을 개선합니다. DICE-RL은 온라인 피드백에서 성공률이 높은 행동을 증폭시켜 사전 훈련된 행동 사전을 고성능 "프로" 정책으로 전환합니다. 우리는 확산 기반 또는 흐름 기반 정책을 사전 훈련하여 광범위한 행동 범위를 확보한 후, 선택적 행동 정규화와 가치 기반 행동 선택을 결합한 안정적이고 샘플 효율적인 잔차 오프-정책 RL 프레임워크로 미세 조정합니다. 광범위한 실험과 분석을 통해 DICE-RL이 강력한 안정성과 샘플 효율성으로 성능을 안정적으로 향상시킴을 보여줍니다. 이는 시뮬레이션과 실제 로봇 모두에서 고차원 픽셀 입력으로부터 직접 복잡한 장기 조작 기술을 습득할 수 있게 합니다. 프로젝트 웹사이트: https://zhanyisun.github.io/dice.rl.2026/.

## 参考
- http://arxiv.org/abs/2603.10263v2
