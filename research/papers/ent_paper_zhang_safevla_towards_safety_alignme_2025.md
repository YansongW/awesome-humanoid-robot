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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.03480v4. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (744 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2503.03480v4

## 개요
SafeVLA는 시각-언어-행동 모델(VLA)이 실제 배포에서 직면하는 환경, 로봇 자체 및 인간의 안전 위험에 대해 통합 안전 방법(ISA)을 제안합니다. 이 방법은 CMDP 프레임워크를 통해 최소-최대 관점에서 정책을 최적화하고, 다양한 불안전 행동을 능동적으로 발굴하여 제약함으로써 안전성과 작업 성능 간의 효과적인 균형을 달성합니다. 실험 결과, SafeVLA는 기존 최적 방법 대비 안전 위반 비용을 83.58% 낮추고 작업 성공률을 3.85% 향상시킬 뿐만 아니라 분포 외 교란 시나리오에도 일반화할 수 있습니다.

## 핵심 내용
### 방법 아키텍처
- **안전 제약 모델링**: CMDP 패러다임을 기반으로 안전 제약을 비용 함수로 명시적으로 인코딩하고 작업 보상과 함께 최적화합니다.
- **불안전 행동 능동 발굴**: 적대적 샘플링 전략을 통해 고위험 시나리오(예: 충돌, 물체 낙하)를 체계적으로 생성하여 모델이 긴 꼬리 안전 취약점을 노출하도록 강제합니다.
- **최소-최대 최적화**: 정책 최적화에 적대적 안전 위험 항목을 도입하여 모델이 훈련 단계에서 극단적 실패 상황을 회피하는 법을 학습하게 합니다.

### 실험 설정
- **작업**: 장시간 이동 조작 작업(예: 잡기, 운반, 장애물 회피).
- **기준**: SOTA 방법(예: RT-2, Octo)과 비교하며, 새로 제안된 안전 평가 기준 환경을 사용합니다.
- **지표**: 작업 성공률(SR) 및 안전 위반 누적 비용(CSC).

### 주요 결과
- **안전-성능 균형**: CSC 83.58% 감소, SR 3.85% 향상.
- **긴 꼬리 위험 처리**: 5%의 극단적 실패 시나리오에서 SafeVLA는 여전히 92%의 안전 운영률을 유지합니다.
- **일반화 능력**: 조명 변화, 물체 위치 이동 등의 분포 외 교란에 대해 안전 행동 유지율이 89%를 초과합니다.

### 결론
SafeVLA는 명시적 안전 제약 학습을 통해 VLA에서 처음으로 정량화 가능한 안전 보장을 구현하여 로봇 일반 정책의 신뢰할 수 있는 배포를 위한 새로운 패러다임을 제공합니다. 코드, 모델 및 기준 환경이 오픈소스로 공개되었습니다.
