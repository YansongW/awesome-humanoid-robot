---
$id: ent_paper_hord_robust_humanoid_control_v_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HoRD: Robust Humanoid Control via History-Conditioned Reinforcement Learning and Online Distillation'
  zh: 'HoRD: Robust Humanoid Control via History-Conditioned Reinforcement Learning and Online Distillation'
  ko: 'HoRD: Robust Humanoid Control via History-Conditioned Reinforcement Learning and Online Distillation'
summary:
  en: 'HoRD: Robust Humanoid Control via History-Conditioned Reinforcement Learning and Online Distillation is a 2026 work
    on locomotion for humanoid robots.'
  zh: 'HoRD: Robust Humanoid Control via History-Conditioned Reinforcement Learning and Online Distillation is a 2026 work
    on locomotion for humanoid robots.'
  ko: 'HoRD: Robust Humanoid Control via History-Conditioned Reinforcement Learning and Online Distillation is a 2026 work
    on locomotion for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- hord
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.04412v3.
sources:
- id: src_001
  type: paper
  title: 'HoRD: Robust Humanoid Control via History-Conditioned Reinforcement Learning and Online Distillation (arXiv)'
  url: https://arxiv.org/abs/2602.04412
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots can suffer significant performance drops under small changes in dynamics, task specifications, or environment setup. We propose HoRD, a two-stage learning framework for robust humanoid control under domain shift. First, we train a high-performance teacher policy via history-conditioned reinforcement learning, where the policy infers latent dynamics context from recent state--action trajectories to adapt online to diverse randomized dynamics. Second, we perform online distillation to transfer the teacher's robust control capabilities into a transformer-based student policy that operates on sparse root-relative 3D joint keypoint trajectories. By combining history-conditioned adaptation with online distillation, HoRD enables a single policy to adapt zero-shot to unseen domains without per-domain retraining. Extensive experiments show HoRD outperforms strong baselines in robustness and transfer, especially under unseen domains and external perturbations. Code and project page are available at https://tonywang-0517.github.io/hord/.

## 核心内容
Humanoid robots can suffer significant performance drops under small changes in dynamics, task specifications, or environment setup. We propose HoRD, a two-stage learning framework for robust humanoid control under domain shift. First, we train a high-performance teacher policy via history-conditioned reinforcement learning, where the policy infers latent dynamics context from recent state--action trajectories to adapt online to diverse randomized dynamics. Second, we perform online distillation to transfer the teacher's robust control capabilities into a transformer-based student policy that operates on sparse root-relative 3D joint keypoint trajectories. By combining history-conditioned adaptation with online distillation, HoRD enables a single policy to adapt zero-shot to unseen domains without per-domain retraining. Extensive experiments show HoRD outperforms strong baselines in robustness and transfer, especially under unseen domains and external perturbations. Code and project page are available at https://tonywang-0517.github.io/hord/.

## 参考
- http://arxiv.org/abs/2602.04412v3

## Overview
Humanoid robots can suffer significant performance drops under small changes in dynamics, task specifications, or environment setup. We propose HoRD, a two-stage learning framework for robust humanoid control under domain shift. First, we train a high-performance teacher policy via history-conditioned reinforcement learning, where the policy infers latent dynamics context from recent state-action trajectories to adapt online to diverse randomized dynamics. Second, we perform online distillation to transfer the teacher's robust control capabilities into a transformer-based student policy that operates on sparse root-relative 3D joint keypoint trajectories. By combining history-conditioned adaptation with online distillation, HoRD enables a single policy to adapt zero-shot to unseen domains without per-domain retraining. Extensive experiments show HoRD outperforms strong baselines in robustness and transfer, especially under unseen domains and external perturbations. Code and project page are available at https://tonywang-0517.github.io/hord/.

## Content
Humanoid robots can suffer significant performance drops under small changes in dynamics, task specifications, or environment setup. We propose HoRD, a two-stage learning framework for robust humanoid control under domain shift. First, we train a high-performance teacher policy via history-conditioned reinforcement learning, where the policy infers latent dynamics context from recent state-action trajectories to adapt online to diverse randomized dynamics. Second, we perform online distillation to transfer the teacher's robust control capabilities into a transformer-based student policy that operates on sparse root-relative 3D joint keypoint trajectories. By combining history-conditioned adaptation with online distillation, HoRD enables a single policy to adapt zero-shot to unseen domains without per-domain retraining. Extensive experiments show HoRD outperforms strong baselines in robustness and transfer, especially under unseen domains and external perturbations. Code and project page are available at https://tonywang-0517.github.io/hord/.

## 개요
휴머노이드 로봇은 역학, 작업 사양 또는 환경 설정의 작은 변화에도 성능이 크게 저하될 수 있습니다. 본 논문에서는 도메인 변화에 강건한 휴머노이드 제어를 위한 2단계 학습 프레임워크인 HoRD를 제안합니다. 첫째, 과거 조건 기반 강화 학습을 통해 고성능 교사 정책을 훈련합니다. 이 정책은 최근 상태-행동 궤적으로부터 잠재 역학 맥락을 추론하여 다양한 무작위 역학에 온라인으로 적응합니다. 둘째, 온라인 증류를 수행하여 교사의 강건한 제어 능력을 희소한 루트 상대 3D 관절 키포인트 궤적으로 작동하는 트랜스포머 기반 학생 정책으로 전이합니다. 과거 조건 기반 적응과 온라인 증류를 결합함으로써, HoRD는 단일 정책이 도메인별 재훈련 없이 제로샷으로 보이지 않는 도메인에 적응할 수 있게 합니다. 광범위한 실험을 통해 HoRD가 강건성 및 전이 측면에서 강력한 기준선을 능가하며, 특히 보이지 않는 도메인과 외부 교란 하에서 우수함을 보여줍니다. 코드와 프로젝트 페이지는 https://tonywang-0517.github.io/hord/에서 확인할 수 있습니다.

## 핵심 내용
휴머노이드 로봇은 역학, 작업 사양 또는 환경 설정의 작은 변화에도 성능이 크게 저하될 수 있습니다. 본 논문에서는 도메인 변화에 강건한 휴머노이드 제어를 위한 2단계 학습 프레임워크인 HoRD를 제안합니다. 첫째, 과거 조건 기반 강화 학습을 통해 고성능 교사 정책을 훈련합니다. 이 정책은 최근 상태-행동 궤적으로부터 잠재 역학 맥락을 추론하여 다양한 무작위 역학에 온라인으로 적응합니다. 둘째, 온라인 증류를 수행하여 교사의 강건한 제어 능력을 희소한 루트 상대 3D 관절 키포인트 궤적으로 작동하는 트랜스포머 기반 학생 정책으로 전이합니다. 과거 조건 기반 적응과 온라인 증류를 결합함으로써, HoRD는 단일 정책이 도메인별 재훈련 없이 제로샷으로 보이지 않는 도메인에 적응할 수 있게 합니다. 광범위한 실험을 통해 HoRD가 강건성 및 전이 측면에서 강력한 기준선을 능가하며, 특히 보이지 않는 도메인과 외부 교란 하에서 우수함을 보여줍니다. 코드와 프로젝트 페이지는 https://tonywang-0517.github.io/hord/에서 확인할 수 있습니다.
