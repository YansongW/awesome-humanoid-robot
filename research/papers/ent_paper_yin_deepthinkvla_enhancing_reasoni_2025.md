---
$id: ent_paper_yin_deepthinkvla_enhancing_reasoni_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DeepThinkVLA: Enhancing Reasoning Capability of Vision-Language-Action Models'
  zh: DeepThinkVLA
  ko: 'DeepThinkVLA: Enhancing Reasoning Capability of Vision-Language-Action Models'
summary:
  en: 'DeepThinkVLA: Enhancing Reasoning Capability of Vision-Language-Action Models (DeepThinkVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Wechat AI, Tencent Inc..'
  zh: DeepThinkVLA 是腾讯微信 AI 团队于 2025 年提出的视觉-语言-动作模型，旨在增强机器人操作中的推理能力。其核心贡献在于通过系统实验诊断出 CoT 推理在 VLA 中有效的两个必要条件：解码对齐与因果对齐，并据此设计混合注意力解码器与两阶段训练流程。在
    LIBERO 基准上达到 97.0% 成功率，在 RoboTwin 2.0 上超出最强基线 21.7 个百分点。
  ko: 'DeepThinkVLA: Enhancing Reasoning Capability of Vision-Language-Action Models (DeepThinkVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Wechat AI, Tencent Inc..'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- deepthinkvla
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.15669v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'DeepThinkVLA: Enhancing Reasoning Capability of Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2511.15669
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DeepThinkVLA source
  url: https://doi.org/10.48550/arXiv.2511.15669
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有 CoT-VLA 系统报告的效果增益有限且不一致，但此前没有工作严格诊断 CoT 何时及为何能帮助机器人行动。通过系统实验，作者识别出 CoT 在 VLA 中有效的两个必要条件：解码对齐要求 CoT 与动作采用模态适配的生成机制，将两者强制通过单一自回归解码器会降低性能 4.2 个百分点；因果对齐要求 CoT 通过基于结果的优化与任务成功建立因果联系，否则在分布偏移下监督式 CoT 与无推理基线表现几乎相同（性能下降 32.0 pp vs 31.6 pp）。基于这些发现构建的 DeepThinkVLA 采用混合注意力解码器（语言用因果注意力，动作用双向注意力并行解码）满足条件 1，通过两阶段 SFT-then-RL 流程满足条件 2，在多个基准上取得领先性能。

## 核心内容
### 方法架构
DeepThinkVLA 的核心设计围绕两个必要条件展开：
- **混合注意力解码器**：将语言因果注意力与动作双向注意力结合，实现 CoT 推理与并行动作解码的模态适配生成。具体而言，语言 token 使用标准因果掩码，动作 token 使用双向注意力，使得动作解码可以并行进行。
- **两阶段训练流程**：先进行监督微调（SFT）建立基础推理-动作链，再通过强化学习（RL）以稀疏任务成功奖励对齐完整的推理-动作链，确保 CoT 与任务成功的因果联系。

### 实验设置与关键结果
- **LIBERO 基准**：DeepThinkVLA 达到 97.0% 成功率，显著优于基线。
- **LIBERO-Plus 鲁棒性测试**：达到 79.0% 鲁棒性，对比 π₀-FAST 的 61.6%。
- **RoboTwin 2.0**：达到 59.3% 成功率，超出最强基线 21.7 个百分点。
- **消融实验**：单一自回归解码器导致性能下降 4.2 个百分点；无因果对齐时，分布偏移下性能下降 32.0 pp，与无推理基线的 31.6 pp 几乎相同。
- **真实机器人实验**：验证了方法在实际操作中的有效性。

### 结论
DeepThinkVLA 通过系统诊断 CoT 在 VLA 中的有效条件，提出混合注意力解码器与两阶段训练流程，在多个基准上取得显著性能提升，并验证了实际应用效果。代码已开源。

## Overview
Does Chain-of-Thought (CoT) reasoning genuinely improve Vision-Language-Action (VLA) models, or does it merely add overhead? Existing CoT-VLA systems report limited and inconsistent gains, yet no prior work has rigorously diagnosed when and why CoT helps robots act. Through systematic experiments, we identify two necessary conditions that must be jointly satisfied for CoT to be effective in VLA: (1) Decoding Alignment -- CoT and actions must be generated with modality-appropriate mechanisms; forcing both through a single autoregressive decoder is not merely suboptimal but actively harmful, degrading performance by 4.2 percentage points; (2) Causal Alignment -- CoT must be causally linked to task success via outcome-based optimization; without it, supervised CoT is indistinguishable from no reasoning at all under distribution shift, exhibiting a 32.0\,pp performance drop nearly identical to the 31.6\,pp drop of a reasoning-free baseline. Guided by these findings, we build DeepThinkVLA: a hybrid-attention decoder satisfies Condition~1 by pairing causal attention for language with bidirectional attention for parallel action decoding, while a two-stage SFT-then-RL pipeline satisfies Condition~2 by aligning the full reasoning--action chain with sparse task-success rewards. DeepThinkVLA achieves 97.0\% success on LIBERO, 79.0\% robustness on LIBERO-Plus (vs.\ 61.6\% for $π_0$-FAST), and 59.3\% success on RoboTwin~2.0, exceeding the strongest baseline by 21.7 points. Furthermore, we validate the practical effectiveness of our approach through real-world robot experiments. Code available at https://github.com/OpenBMB/DeepThinkVLA

## Overview
Does Chain-of-Thought (CoT) reasoning genuinely improve Vision-Language-Action (VLA) models, or does it merely add overhead? Existing CoT-VLA systems report limited and inconsistent gains, yet no prior work has rigorously diagnosed when and why CoT helps robots act. Through systematic experiments, we identify two necessary conditions that must be jointly satisfied for CoT to be effective in VLA: (1) Decoding Alignment -- CoT and actions must be generated with modality-appropriate mechanisms; forcing both through a single autoregressive decoder is not merely suboptimal but actively harmful, degrading performance by 4.2 percentage points; (2) Causal Alignment -- CoT must be causally linked to task success via outcome-based optimization; without it, supervised CoT is indistinguishable from no reasoning at all under distribution shift, exhibiting a 32.0 pp performance drop nearly identical to the 31.6 pp drop of a reasoning-free baseline. Guided by these findings, we build DeepThinkVLA: a hybrid-attention decoder satisfies Condition 1 by pairing causal attention for language with bidirectional attention for parallel action decoding, while a two-stage SFT-then-RL pipeline satisfies Condition 2 by aligning the full reasoning--action chain with sparse task-success rewards. DeepThinkVLA achieves 97.0% success on LIBERO, 79.0% robustness on LIBERO-Plus (vs. 61.6% for $\pi_0$-FAST), and 59.3% success on RoboTwin 2.0, exceeding the strongest baseline by 21.7 points. Furthermore, we validate the practical effectiveness of our approach through real-world robot experiments. Code available at https://github.com/OpenBMB/DeepThinkVLA

## Content
Does Chain-of-Thought (CoT) reasoning genuinely improve Vision-Language-Action (VLA) models, or does it merely add overhead? Existing CoT-VLA systems report limited and inconsistent gains, yet no prior work has rigorously diagnosed when and why CoT helps robots act. Through systematic experiments, we identify two necessary conditions that must be jointly satisfied for CoT to be effective in VLA: (1) Decoding Alignment -- CoT and actions must be generated with modality-appropriate mechanisms; forcing both through a single autoregressive decoder is not merely suboptimal but actively harmful, degrading performance by 4.2 percentage points; (2) Causal Alignment -- CoT must be causally linked to task success via outcome-based optimization; without it, supervised CoT is indistinguishable from no reasoning at all under distribution shift, exhibiting a 32.0 pp performance drop nearly identical to the 31.6 pp drop of a reasoning-free baseline. Guided by these findings, we build DeepThinkVLA: a hybrid-attention decoder satisfies Condition 1 by pairing causal attention for language with bidirectional attention for parallel action decoding, while a two-stage SFT-then-RL pipeline satisfies Condition 2 by aligning the full reasoning--action chain with sparse task-success rewards. DeepThinkVLA achieves 97.0% success on LIBERO, 79.0% robustness on LIBERO-Plus (vs. 61.6% for $\pi_0$-FAST), and 59.3% success on RoboTwin 2.0, exceeding the strongest baseline by 21.7 points. Furthermore, we validate the practical effectiveness of our approach through real-world robot experiments. Code available at https://github.com/OpenBMB/DeepThinkVLA

## 개요
Chain-of-Thought(CoT) 추론이 Vision-Language-Action(VLA) 모델을 실제로 개선하는가, 아니면 단순히 오버헤드를 추가하는가? 기존 CoT-VLA 시스템은 제한적이고 일관되지 않은 성능 향상을 보고하지만, CoT가 로봇의 행동에 언제, 왜 도움이 되는지 엄격하게 진단한 선행 연구는 없습니다. 체계적인 실험을 통해, 우리는 CoT가 VLA에서 효과적이기 위해 함께 충족되어야 하는 두 가지 필수 조건을 식별했습니다: (1) 디코딩 정렬(Decoding Alignment) -- CoT와 행동은 모달리티에 적합한 메커니즘으로 생성되어야 합니다. 둘을 단일 자기회귀 디코더로 강제하는 것은 단순히 차선책이 아니라 적극적으로 해로우며, 성능을 4.2% 포인트 저하시킵니다; (2) 인과적 정렬(Causal Alignment) -- CoT는 결과 기반 최적화를 통해 작업 성공과 인과적으로 연결되어야 합니다. 그렇지 않으면, 분포 변화 하에서 지도 학습된 CoT는 추론이 전혀 없는 것과 구별할 수 없으며, 추론 없는 기준선의 31.6% 포인트 하락과 거의 동일한 32.0% 포인트 성능 하락을 보입니다. 이러한 발견에 따라, 우리는 DeepThinkVLA를 구축했습니다: 하이브리드 어텐션 디코더는 언어에 대한 인과적 어텐션과 병렬 행동 디코딩을 위한 양방향 어텐션을 결합하여 조건 1을 충족시키고, 2단계 SFT 후 RL 파이프라인은 전체 추론-행동 체인을 희소 작업 성공 보상과 정렬시켜 조건 2를 충족시킵니다. DeepThinkVLA는 LIBERO에서 97.0% 성공률, LIBERO-Plus에서 79.0% 견고성($π_0$-FAST의 61.6% 대비), RoboTwin 2.0에서 59.3% 성공률을 달성하여 가장 강력한 기준선을 21.7% 포인트 초과합니다. 또한, 실제 로봇 실험을 통해 우리 접근 방식의 실용적 효과를 검증합니다. 코드는 https://github.com/OpenBMB/DeepThinkVLA 에서 확인할 수 있습니다.

## 핵심 내용
Chain-of-Thought(CoT) 추론이 Vision-Language-Action(VLA) 모델을 실제로 개선하는가, 아니면 단순히 오버헤드를 추가하는가? 기존 CoT-VLA 시스템은 제한적이고 일관되지 않은 성능 향상을 보고하지만, CoT가 로봇의 행동에 언제, 왜 도움이 되는지 엄격하게 진단한 선행 연구는 없습니다. 체계적인 실험을 통해, 우리는 CoT가 VLA에서 효과적이기 위해 함께 충족되어야 하는 두 가지 필수 조건을 식별했습니다: (1) 디코딩 정렬(Decoding Alignment) -- CoT와 행동은 모달리티에 적합한 메커니즘으로 생성되어야 합니다. 둘을 단일 자기회귀 디코더로 강제하는 것은 단순히 차선책이 아니라 적극적으로 해로우며, 성능을 4.2% 포인트 저하시킵니다; (2) 인과적 정렬(Causal Alignment) -- CoT는 결과 기반 최적화를 통해 작업 성공과 인과적으로 연결되어야 합니다. 그렇지 않으면, 분포 변화 하에서 지도 학습된 CoT는 추론이 전혀 없는 것과 구별할 수 없으며, 추론 없는 기준선의 31.6% 포인트 하락과 거의 동일한 32.0% 포인트 성능 하락을 보입니다. 이러한 발견에 따라, 우리는 DeepThinkVLA를 구축했습니다: 하이브리드 어텐션 디코더는 언어에 대한 인과적 어텐션과 병렬 행동 디코딩을 위한 양방향 어텐션을 결합하여 조건 1을 충족시키고, 2단계 SFT 후 RL 파이프라인은 전체 추론-행동 체인을 희소 작업 성공 보상과 정렬시켜 조건 2를 충족시킵니다. DeepThinkVLA는 LIBERO에서 97.0% 성공률, LIBERO-Plus에서 79.0% 견고성($π_0$-FAST의 61.6% 대비), RoboTwin 2.0에서 59.3% 성공률을 달성하여 가장 강력한 기준선을 21.7% 포인트 초과합니다. 또한, 실제 로봇 실험을 통해 우리 접근 방식의 실용적 효과를 검증합니다. 코드는 https://github.com/OpenBMB/DeepThinkVLA 에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2511.15669v2
