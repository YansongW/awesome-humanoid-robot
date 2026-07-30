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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.26406v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
강화 학습(RL)은 강건한 로봇 조작 정책을 생성하는 데 널리 사용되지만, 시각-언어-행동(VLA) 모델을 RL로 미세 조정하는 것은 부정확한 가치 추정과 중간 단계에서의 희소한 지도 학습으로 인해 불안정할 수 있습니다. 반면, 모방 학습(IL)은 훈련이 쉽지만 오프라인 특성으로 인해 성능이 낮은 경우가 많습니다. 본 논문에서는 간단하면서도 효과적인 사후 훈련 방법인 Hi-ORS를 제안하며, 이는 거절 샘플링을 활용하여 훈련 안정성과 높은 강건성을 동시에 달성합니다. Hi-ORS는 온라인 미세 조정 중 음의 보상을 받은 샘플을 필터링하여 가치 추정을 안정화하고, 보상 가중 지도 훈련 목표를 채택하여 밀집된 중간 단계 지도 학습을 제공합니다. 체계적인 연구를 위해, 유연한 온라인 인간-루프 수정을 지원하는 비동기 추론-훈련 프레임워크를 개발하며, 이는 오류 복구 행동 학습을 위한 명시적 지침 역할을 합니다. 세 가지 실제 작업과 두 가지 구현체에서 Hi-ORS는 pi-base 정책을 미세 조정하여 단 1.5시간의 실제 훈련으로 접촉이 많은 조작을 마스터하며, 효과성과 효율성 모두에서 RL 및 IL 기준선을 크게 능가합니다. 특히, 미세 조정된 정책은 복잡한 오류 복구 행동을 안정적으로 실행하여 더 나은 성능을 달성함으로써 강력한 테스트 시간 확장성을 보여줍니다.

## 핵심 내용
강화 학습(RL)은 강건한 로봇 조작 정책을 생성하는 데 널리 사용되지만, 시각-언어-행동(VLA) 모델을 RL로 미세 조정하는 것은 부정확한 가치 추정과 중간 단계에서의 희소한 지도 학습으로 인해 불안정할 수 있습니다. 반면, 모방 학습(IL)은 훈련이 쉽지만 오프라인 특성으로 인해 성능이 낮은 경우가 많습니다. 본 논문에서는 간단하면서도 효과적인 사후 훈련 방법인 Hi-ORS를 제안하며, 이는 거절 샘플링을 활용하여 훈련 안정성과 높은 강건성을 동시에 달성합니다. Hi-ORS는 온라인 미세 조정 중 음의 보상을 받은 샘플을 필터링하여 가치 추정을 안정화하고, 보상 가중 지도 훈련 목표를 채택하여 밀집된 중간 단계 지도 학습을 제공합니다. 체계적인 연구를 위해, 유연한 온라인 인간-루프 수정을 지원하는 비동기 추론-훈련 프레임워크를 개발하며, 이는 오류 복구 행동 학습을 위한 명시적 지침 역할을 합니다. 세 가지 실제 작업과 두 가지 구현체에서 Hi-ORS는 pi-base 정책을 미세 조정하여 단 1.5시간의 실제 훈련으로 접촉이 많은 조작을 마스터하며, 효과성과 효율성 모두에서 RL 및 IL 기준선을 크게 능가합니다. 특히, 미세 조정된 정책은 복잡한 오류 복구 행동을 안정적으로 실행하여 더 나은 성능을 달성함으로써 강력한 테스트 시간 확장성을 보여줍니다.

## 参考
- http://arxiv.org/abs/2510.26406v1
