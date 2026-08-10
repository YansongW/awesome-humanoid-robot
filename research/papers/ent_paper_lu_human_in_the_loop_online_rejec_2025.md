---
$id: ent_paper_lu_human_in_the_loop_online_rejec_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Human-in-the-loop Online Rejection Sampling for Robotic Manipulation
  zh: Hi-ORS
  ko: Human-in-the-loop Online Rejection Sampling for Robotic Manipulation
summary:
  en: Human-in-the-loop Online Rejection Sampling for Robotic Manipulation (Hi-ORS), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua Shenzhen International Graduate School, Tencent Robotics X.
  zh: Hi-ORS 是清华大学深圳国际研究生院与腾讯 Robotics X 于 2025 年提出的一种面向机器人操作的大规模视觉-语言-动作模型后训练方法。其核心贡献在于通过在线拒绝采样过滤负奖励样本，并结合奖励加权监督训练，在仅 1.5
    小时真实世界训练内显著提升策略的鲁棒性与效率。
  ko: Human-in-the-loop Online Rejection Sampling for Robotic Manipulation (Hi-ORS), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua Shenzhen International Graduate School, Tencent Robotics X.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- hi_ors
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.26406v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (715 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Human-in-the-loop Online Rejection Sampling for Robotic Manipulation (arXiv)
  url: https://arxiv.org/abs/2510.26406
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Hi-ORS source
  url: https://doi.org/10.48550/arXiv.2510.26406
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Hi-ORS 针对强化学习微调 VLA 模型时价值估计不准确与中间步骤监督稀疏的问题，以及模仿学习离线训练性能不足的缺陷，提出了一种结合拒绝采样与奖励加权监督的在线后训练方法。该方法通过异步推理-训练框架支持人类在线纠错，为学习错误恢复行为提供显式指导。在三个真实世界任务和两种机器人形态上的实验表明，Hi-ORS 微调的 pi-base 策略在接触密集型操作中表现优异，其效果与效率均大幅超越强化学习与模仿学习基线。

## 核心内容
### 方法架构
- **核心机制**：Hi-ORS 采用在线拒绝采样，在微调过程中过滤掉负奖励样本，从而稳定价值估计；同时使用奖励加权监督训练目标，为中间步骤提供密集监督信号。
- **异步框架**：开发了异步推理-训练框架，支持灵活的人类在线纠错，这些纠错作为显式指导，帮助策略学习错误恢复行为。

### 实验设置
- **任务与形态**：在三个真实世界任务（接触密集型操作）和两种机器人形态（具体未在正文中详述）上评估。
- **基线对比**：与强化学习（RL）和模仿学习（IL）基线进行对比。
- **训练效率**：仅需 1.5 小时真实世界训练即可完成微调。

### 关键结果
- **性能优势**：Hi-ORS 微调的 pi-base 策略在有效性和效率上均大幅超越 RL 和 IL 基线。
- **可扩展性**：微调后的策略展现出强大的测试时可扩展性，能够可靠地执行复杂错误恢复行为，从而获得更优性能。

### 结论
Hi-ORS 通过结合拒绝采样与人类在线纠错，解决了 VLA 模型微调中的稳定性与监督稀疏问题，为机器人操作提供了一种高效且鲁棒的后训练方案。

## Overview
Reinforcement learning (RL) is widely used to produce robust robotic manipulation policies, but fine-tuning vision-language-action (VLA) models with RL can be unstable due to inaccurate value estimates and sparse supervision at intermediate steps. In contrast, imitation learning (IL) is easy to train but often underperforms due to its offline nature. In this paper, we propose Hi-ORS, a simple yet effective post-training method that utilizes rejection sampling to achieve both training stability and high robustness. Hi-ORS stabilizes value estimation by filtering out negatively rewarded samples during online fine-tuning, and adopts a reward-weighted supervised training objective to provide dense intermediate-step supervision. For systematic study, we develop an asynchronous inference-training framework that supports flexible online human-in-the-loop corrections, which serve as explicit guidance for learning error-recovery behaviors. Across three real-world tasks and two embodiments, Hi-ORS fine-tunes a pi-base policy to master contact-rich manipulation in just 1.5 hours of real-world training, outperforming RL and IL baselines by a substantial margin in both effectiveness and efficiency. Notably, the fine-tuned policy exhibits strong test-time scalability by reliably executing complex error-recovery behaviors to achieve better performance.

## 参考
- http://arxiv.org/abs/2510.26406v1

## 개요
Hi-ORS는 강화 학습으로 VLA 모델을 미세 조정할 때 발생하는 가치 추정의 부정확성과 중간 단계 감독의 희소성 문제, 그리고 모방 학습의 오프라인 훈련 성능 부족 문제를 해결하기 위해, 거부 샘플링과 보상 가중 감독을 결합한 온라인 사후 훈련 방법을 제안한다. 이 방법은 비동기 추론-훈련 프레임워크를 통해 인간의 온라인 오류 수정을 지원하며, 오류 복구 동작 학습에 명시적 지침을 제공한다. 세 가지 실제 세계 작업과 두 가지 로봇 형태에 대한 실험에서 Hi-ORS로 미세 조정된 pi-base 정책은 접촉 집약적 조작에서 우수한 성능을 보였으며, 그 효과와 효율성 모두 강화 학습 및 모방 학습 기준선을 크게 능가했다.

## 핵심 내용
### 방법 아키텍처
- **핵심 메커니즘**: Hi-ORS는 온라인 거부 샘플링을 사용하여 미세 조정 과정에서 부정적 보상 샘플을 걸러내 가치 추정을 안정화하고, 동시에 보상 가중 감독 훈련 목표를 사용하여 중간 단계에 밀집 감독 신호를 제공한다.
- **비동기 프레임워크**: 유연한 인간 온라인 오류 수정을 지원하는 비동기 추론-훈련 프레임워크를 개발했으며, 이러한 수정은 명시적 지침으로 작용하여 정책이 오류 복구 동작을 학습하도록 돕는다.

### 실험 설정
- **작업 및 형태**: 세 가지 실제 세계 작업(접촉 집약적 조작)과 두 가지 로봇 형태(본문에서 구체적으로 상세히 설명되지 않음)에서 평가했다.
- **기준선 비교**: 강화 학습(RL) 및 모방 학습(IL) 기준선과 비교했다.
- **훈련 효율성**: 실제 세계 훈련 1.5시간만으로 미세 조정을 완료할 수 있다.

### 주요 결과
- **성능 우위**: Hi-ORS로 미세 조정된 pi-base 정책은 유효성과 효율성 모두에서 RL 및 IL 기준선을 크게 능가했다.
- **확장성**: 미세 조정된 정책은 강력한 테스트 시 확장성을 보여주며, 복잡한 오류 복구 동작을 안정적으로 실행하여 더 나은 성능을 얻을 수 있다.

### 결론
Hi-ORS는 거부 샘플링과 인간의 온라인 오류 수정을 결합하여 VLA 모델 미세 조정에서의 안정성 및 감독 희소성 문제를 해결하며, 로봇 조작을 위한 효율적이고 견고한 사후 훈련 솔루션을 제공한다.
