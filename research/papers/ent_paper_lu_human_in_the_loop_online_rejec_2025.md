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
  zh: Human-in-the-loop Online Rejection Sampling for Robotic Manipulation (Hi-ORS), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua Shenzhen International Graduate School, Tencent Robotics X.
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.26406v1.
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
Reinforcement learning (RL) is widely used to produce robust robotic manipulation policies, but fine-tuning vision-language-action (VLA) models with RL can be unstable due to inaccurate value estimates and sparse supervision at intermediate steps. In contrast, imitation learning (IL) is easy to train but often underperforms due to its offline nature. In this paper, we propose Hi-ORS, a simple yet effective post-training method that utilizes rejection sampling to achieve both training stability and high robustness. Hi-ORS stabilizes value estimation by filtering out negatively rewarded samples during online fine-tuning, and adopts a reward-weighted supervised training objective to provide dense intermediate-step supervision. For systematic study, we develop an asynchronous inference-training framework that supports flexible online human-in-the-loop corrections, which serve as explicit guidance for learning error-recovery behaviors. Across three real-world tasks and two embodiments, Hi-ORS fine-tunes a pi-base policy to master contact-rich manipulation in just 1.5 hours of real-world training, outperforming RL and IL baselines by a substantial margin in both effectiveness and efficiency. Notably, the fine-tuned policy exhibits strong test-time scalability by reliably executing complex error-recovery behaviors to achieve better performance.

## 核心内容
Reinforcement learning (RL) is widely used to produce robust robotic manipulation policies, but fine-tuning vision-language-action (VLA) models with RL can be unstable due to inaccurate value estimates and sparse supervision at intermediate steps. In contrast, imitation learning (IL) is easy to train but often underperforms due to its offline nature. In this paper, we propose Hi-ORS, a simple yet effective post-training method that utilizes rejection sampling to achieve both training stability and high robustness. Hi-ORS stabilizes value estimation by filtering out negatively rewarded samples during online fine-tuning, and adopts a reward-weighted supervised training objective to provide dense intermediate-step supervision. For systematic study, we develop an asynchronous inference-training framework that supports flexible online human-in-the-loop corrections, which serve as explicit guidance for learning error-recovery behaviors. Across three real-world tasks and two embodiments, Hi-ORS fine-tunes a pi-base policy to master contact-rich manipulation in just 1.5 hours of real-world training, outperforming RL and IL baselines by a substantial margin in both effectiveness and efficiency. Notably, the fine-tuned policy exhibits strong test-time scalability by reliably executing complex error-recovery behaviors to achieve better performance.

## 参考
- http://arxiv.org/abs/2510.26406v1

## Overview
Reinforcement learning (RL) is widely used to produce robust robotic manipulation policies, but fine-tuning vision-language-action (VLA) models with RL can be unstable due to inaccurate value estimates and sparse supervision at intermediate steps. In contrast, imitation learning (IL) is easy to train but often underperforms due to its offline nature. In this paper, we propose Hi-ORS, a simple yet effective post-training method that utilizes rejection sampling to achieve both training stability and high robustness. Hi-ORS stabilizes value estimation by filtering out negatively rewarded samples during online fine-tuning, and adopts a reward-weighted supervised training objective to provide dense intermediate-step supervision. For systematic study, we develop an asynchronous inference-training framework that supports flexible online human-in-the-loop corrections, which serve as explicit guidance for learning error-recovery behaviors. Across three real-world tasks and two embodiments, Hi-ORS fine-tunes a pi-base policy to master contact-rich manipulation in just 1.5 hours of real-world training, outperforming RL and IL baselines by a substantial margin in both effectiveness and efficiency. Notably, the fine-tuned policy exhibits strong test-time scalability by reliably executing complex error-recovery behaviors to achieve better performance.

## Content
Reinforcement learning (RL) is widely used to produce robust robotic manipulation policies, but fine-tuning vision-language-action (VLA) models with RL can be unstable due to inaccurate value estimates and sparse supervision at intermediate steps. In contrast, imitation learning (IL) is easy to train but often underperforms due to its offline nature. In this paper, we propose Hi-ORS, a simple yet effective post-training method that utilizes rejection sampling to achieve both training stability and high robustness. Hi-ORS stabilizes value estimation by filtering out negatively rewarded samples during online fine-tuning, and adopts a reward-weighted supervised training objective to provide dense intermediate-step supervision. For systematic study, we develop an asynchronous inference-training framework that supports flexible online human-in-the-loop corrections, which serve as explicit guidance for learning error-recovery behaviors. Across three real-world tasks and two embodiments, Hi-ORS fine-tunes a pi-base policy to master contact-rich manipulation in just 1.5 hours of real-world training, outperforming RL and IL baselines by a substantial margin in both effectiveness and efficiency. Notably, the fine-tuned policy exhibits strong test-time scalability by reliably executing complex error-recovery behaviors to achieve better performance.

## 개요
강화 학습(RL)은 강건한 로봇 조작 정책을 생성하는 데 널리 사용되지만, 시각-언어-행동(VLA) 모델을 RL로 미세 조정하는 것은 부정확한 가치 추정과 중간 단계에서의 희소한 지도 학습으로 인해 불안정할 수 있습니다. 반면, 모방 학습(IL)은 훈련이 쉽지만 오프라인 특성으로 인해 성능이 낮은 경우가 많습니다. 본 논문에서는 간단하면서도 효과적인 사후 훈련 방법인 Hi-ORS를 제안하며, 이는 거절 샘플링을 활용하여 훈련 안정성과 높은 강건성을 동시에 달성합니다. Hi-ORS는 온라인 미세 조정 중 음의 보상을 받은 샘플을 필터링하여 가치 추정을 안정화하고, 보상 가중 지도 훈련 목표를 채택하여 밀집된 중간 단계 지도 학습을 제공합니다. 체계적인 연구를 위해, 유연한 온라인 인간-루프 수정을 지원하는 비동기 추론-훈련 프레임워크를 개발하며, 이는 오류 복구 행동 학습을 위한 명시적 지침 역할을 합니다. 세 가지 실제 작업과 두 가지 구현체에서 Hi-ORS는 pi-base 정책을 미세 조정하여 단 1.5시간의 실제 훈련으로 접촉이 많은 조작을 마스터하며, 효과성과 효율성 모두에서 RL 및 IL 기준선을 크게 능가합니다. 특히, 미세 조정된 정책은 복잡한 오류 복구 행동을 안정적으로 실행하여 더 나은 성능을 달성함으로써 강력한 테스트 시간 확장성을 보여줍니다.

## 핵심 내용
강화 학습(RL)은 강건한 로봇 조작 정책을 생성하는 데 널리 사용되지만, 시각-언어-행동(VLA) 모델을 RL로 미세 조정하는 것은 부정확한 가치 추정과 중간 단계에서의 희소한 지도 학습으로 인해 불안정할 수 있습니다. 반면, 모방 학습(IL)은 훈련이 쉽지만 오프라인 특성으로 인해 성능이 낮은 경우가 많습니다. 본 논문에서는 간단하면서도 효과적인 사후 훈련 방법인 Hi-ORS를 제안하며, 이는 거절 샘플링을 활용하여 훈련 안정성과 높은 강건성을 동시에 달성합니다. Hi-ORS는 온라인 미세 조정 중 음의 보상을 받은 샘플을 필터링하여 가치 추정을 안정화하고, 보상 가중 지도 훈련 목표를 채택하여 밀집된 중간 단계 지도 학습을 제공합니다. 체계적인 연구를 위해, 유연한 온라인 인간-루프 수정을 지원하는 비동기 추론-훈련 프레임워크를 개발하며, 이는 오류 복구 행동 학습을 위한 명시적 지침 역할을 합니다. 세 가지 실제 작업과 두 가지 구현체에서 Hi-ORS는 pi-base 정책을 미세 조정하여 단 1.5시간의 실제 훈련으로 접촉이 많은 조작을 마스터하며, 효과성과 효율성 모두에서 RL 및 IL 기준선을 크게 능가합니다. 특히, 미세 조정된 정책은 복잡한 오류 복구 행동을 안정적으로 실행하여 더 나은 성능을 달성함으로써 강력한 테스트 시간 확장성을 보여줍니다.
