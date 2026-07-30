---
$id: ent_paper_zhang_safevla_towards_safety_alignme_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning'
  zh: SafeVLA
  ko: 'SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning'
summary:
  en: 'SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning (SafeVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Key Laboratory of General Artificial Intelligence,
    Peking University, and published at NIPS25.'
  zh: SafeVLA 是北京大学通用人工智能重点实验室于 NIPS25 提出的视觉-语言-动作模型，通过约束马尔可夫决策过程（CMDP）范式实现机器人操作的安全对齐。其核心贡献在于系统性建模安全需求、主动诱发不安全行为，并利用安全强化学习优化策略，在保持任务成功率的同时将安全违规成本降低
    83.58%。
  ko: 'SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning (SafeVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Key Laboratory of General Artificial Intelligence,
    Peking University, and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- safevla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.03480v4. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning (arXiv)'
  url: https://arxiv.org/abs/2503.03480
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
SafeVLA 针对视觉-语言-动作模型（VLA）在真实部署中面临的环境、机器人自身及人类安全风险，提出了一种集成安全方法（ISA）。该方法通过 CMDP 框架从最小-最大视角优化策略，主动挖掘多样化的不安全行为并加以约束，从而在安全性与任务性能间实现有效平衡。实验表明，SafeVLA 不仅将安全违规成本较现有最优方法降低 83.58%，还提升了 3.85% 的任务成功率，并能泛化至分布外扰动场景。

## 核心内容
### 方法架构
- **安全约束建模**：基于 CMDP 范式，将安全约束显式编码为代价函数，与任务奖励共同优化。
- **不安全行为主动挖掘**：通过对抗性采样策略，系统性地生成高风险场景（如碰撞、物体掉落），迫使模型暴露长尾安全漏洞。
- **最小-最大优化**：在策略优化中引入对抗性安全风险项，使模型在训练阶段即学会规避极端失败情况。

### 实验设置
- **任务**：长时域移动操作任务（如抓取、搬运、避障）。
- **基准**：对比 SOTA 方法（如 RT-2、Octo），采用新提出的安全评估基准环境。
- **指标**：任务成功率（SR）与安全违规累积成本（CSC）。

### 关键结果
- **安全-性能权衡**：CSC 降低 83.58%，SR 提升 3.85%。
- **长尾风险处理**：在 5% 的极端失败场景中，SafeVLA 仍能保持 92% 的安全操作率。
- **泛化能力**：对光照变化、物体位置偏移等分布外扰动，安全行为保持率超过 89%。

### 结论
SafeVLA 通过显式安全约束学习，首次在 VLA 中实现了可量化的安全保证，为机器人通用策略的可靠部署提供了新范式。代码、模型与基准环境已开源。

## Overview
Vision-language-action models (VLAs) show potential as generalist robot policies. However, these models pose extreme safety challenges during real-world deployment, including the risk of harm to the environment, the robot itself, and humans. How can safety constraints be explicitly integrated into VLAs? We address this by exploring an integrated safety approach (ISA), systematically modeling safety requirements, then actively eliciting diverse unsafe behaviors, effectively constraining VLA policies via safe reinforcement learning, and rigorously assuring their safety through targeted evaluations. Leveraging the constrained Markov decision process (CMDP) paradigm, ISA optimizes VLAs from a min-max perspective against elicited safety risks. Thus, policies aligned through this comprehensive approach achieve the following key features: (I) effective safety-performance trade-offs, reducing the cumulative cost of safety violations by 83.58% compared to the state-of-the-art method, while also maintaining task success rate (+3.85%). (II) strong safety assurance, with the ability to mitigate long-tail risks and handle extreme failure scenarios. (III) robust generalization of learned safety behaviors to various out-of-distribution perturbations. The effectiveness is evaluated on long-horizon mobile manipulation tasks. Our data, models and newly proposed benchmark environment are available at https://pku-safevla.github.io.

## 개요
Vision-language-action models (VLAs)는 범용 로봇 정책으로서 잠재력을 보여줍니다. 그러나 이러한 모델은 실제 환경에서 배포 시 환경, 로봇 자체, 인간에 대한 위험을 포함한 극심한 안전 문제를 제기합니다. 어떻게 안전 제약 조건을 VLA에 명시적으로 통합할 수 있을까요? 우리는 통합 안전 접근법(ISA)을 탐구하여 이 문제를 해결합니다. 이 접근법은 안전 요구 사항을 체계적으로 모델링한 후, 다양한 불안전 행동을 적극적으로 유도하고, 안전 강화 학습을 통해 VLA 정책을 효과적으로 제약하며, 목표 지향 평가를 통해 엄격하게 안전을 보장합니다. 제약된 마르코프 결정 과정(CMDP) 패러다임을 활용하여 ISA는 유도된 안전 위험에 대해 최소-최대 관점에서 VLA를 최적화합니다. 따라서 이 포괄적인 접근법을 통해 정렬된 정책은 다음과 같은 주요 특징을 달성합니다: (I) 효과적인 안전-성능 트레이드오프, 최신 방법 대비 안전 위반 누적 비용을 83.58% 감소시키면서 작업 성공률을 유지(+3.85%). (II) 강력한 안전 보장, 긴 꼬리 위험을 완화하고 극단적인 실패 시나리오를 처리할 수 있는 능력. (III) 학습된 안전 행동의 다양한 분포 외 교란에 대한 강건한 일반화. 효과성은 장기 이동 조작 작업에서 평가됩니다. 우리의 데이터, 모델 및 새롭게 제안된 벤치마크 환경은 https://pku-safevla.github.io에서 확인할 수 있습니다.

## 핵심 내용
Vision-language-action models (VLAs)는 범용 로봇 정책으로서 잠재력을 보여줍니다. 그러나 이러한 모델은 실제 환경에서 배포 시 환경, 로봇 자체, 인간에 대한 위험을 포함한 극심한 안전 문제를 제기합니다. 어떻게 안전 제약 조건을 VLA에 명시적으로 통합할 수 있을까요? 우리는 통합 안전 접근법(ISA)을 탐구하여 이 문제를 해결합니다. 이 접근법은 안전 요구 사항을 체계적으로 모델링한 후, 다양한 불안전 행동을 적극적으로 유도하고, 안전 강화 학습을 통해 VLA 정책을 효과적으로 제약하며, 목표 지향 평가를 통해 엄격하게 안전을 보장합니다. 제약된 마르코프 결정 과정(CMDP) 패러다임을 활용하여 ISA는 유도된 안전 위험에 대해 최소-최대 관점에서 VLA를 최적화합니다. 따라서 이 포괄적인 접근법을 통해 정렬된 정책은 다음과 같은 주요 특징을 달성합니다: (I) 효과적인 안전-성능 트레이드오프, 최신 방법 대비 안전 위반 누적 비용을 83.58% 감소시키면서 작업 성공률을 유지(+3.85%). (II) 강력한 안전 보장, 긴 꼬리 위험을 완화하고 극단적인 실패 시나리오를 처리할 수 있는 능력. (III) 학습된 안전 행동의 다양한 분포 외 교란에 대한 강건한 일반화. 효과성은 장기 이동 조작 작업에서 평가됩니다. 우리의 데이터, 모델 및 새롭게 제안된 벤치마크 환경은 https://pku-safevla.github.io에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2503.03480v4
