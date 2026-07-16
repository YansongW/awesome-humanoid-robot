---
$id: ent_paper_warp_rl_reshaping_base_policy_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Warp RL: Reshaping Base Policy Distributions for Dynamics Adaptation'
  zh: 'Warp RL: Reshaping Base Policy Distributions for Dynamics Adaptation'
  ko: 'Warp RL: Reshaping Base Policy Distributions for Dynamics Adaptation'
summary:
  en: 'arXiv:2606.31043v1 Announce Type: cross Abstract: Residual reinforcement learning adapts a pretrained robot policy
    by learning an additive correction to its actions. While effective when adaptation amounts to shifting the base policy''s
    action distribution, additive corrections cannot change the distribution''s shape, scale, or state-dependent geometry
    -- limitations we formalize as wrong variance, miscalibrated confidence, and non-uniform correction. We show that these
    matter under dynamics shift: when the base distribution is geometrically mismatched to the shifted system, residual correction
    can underperform even the unadapted policy. We propose \textbf{Warp RL}, a policy adaptation method that replaces additive
    residuals with an invertible, state-conditioned transformation of the base policy''s action distribution. Instantiated
    with monotonic rational-quadratic spline flows [arXiv:0706.1234v1], Warp RL preserves identity initialization, strictly
    generalizes additive residual correction, and exposes a structured adaptation space suitable for both policy-gradient
    and gradient-free optimization. Across a variety of ManiSkill3 manipulation tasks with controlled dynamics shifts, Warp
    RL matches residual correction when translation is sufficient and substantially outperforms it when adaptation requires
    distributional reshaping. We further demonstrate that warping can replace additive correction in an off-policy sim-to-real
    pipeline, achieving comparable success rate with 30% faster task completion on a real-robot peg-insertion task.'
  zh: 'arXiv:2606.31043v1 Announce Type: cross Abstract: Residual reinforcement learning adapts a pretrained robot policy
    by learning an additive correction to its actions. While effective when adaptation amounts to shifting the base policy''s
    action distribution, additive corrections cannot change the distribution''s shape, scale, or state-dependent geometry
    -- limitations we formalize as wrong variance, miscalibrated confidence, and non-uniform correction. We show that these
    matter under dynamics shift: when the base distribution is geometrically mismatched to the shifted system, residual correction
    can underperform even the unadapted policy. We propose \textbf{Warp RL}, a policy adaptation method that replaces additive
    residuals with an invertible, state-conditioned transformation of the base policy''s action distribution. Instantiated
    with monotonic rational-quadratic spline flows [arXiv:0706.1234v1], Warp RL preserves identity initialization, strictly
    generalizes additive residual correction, and exposes a structured adaptation space suitable for both policy-gradient
    and gradient-free optimization. Across a variety of ManiSkill3 manipulation tasks with controlled dynamics shifts, Warp
    RL matches residual correction when translation is sufficient and substantially outperforms it when adaptation requires
    distributional reshaping. We further demonstrate that warping can replace additive correction in an off-policy sim-to-real
    pipeline, achieving comparable success rate with 30% faster task completion on a real-robot peg-insertion task.'
  ko: 'arXiv:2606.31043v1 Announce Type: cross Abstract: Residual reinforcement learning adapts a pretrained robot policy
    by learning an additive correction to its actions. While effective when adaptation amounts to shifting the base policy''s
    action distribution, additive corrections cannot change the distribution''s shape, scale, or state-dependent geometry
    -- limitations we formalize as wrong variance, miscalibrated confidence, and non-uniform correction. We show that these
    matter under dynamics shift: when the base distribution is geometrically mismatched to the shifted system, residual correction
    can underperform even the unadapted policy. We propose \textbf{Warp RL}, a policy adaptation method that replaces additive
    residuals with an invertible, state-conditioned transformation of the base policy''s action distribution. Instantiated
    with monotonic rational-quadratic spline flows [arXiv:0706.1234v1], Warp RL preserves identity initialization, strictly
    generalizes additive residual correction, and exposes a structured adaptation space suitable for both policy-gradient
    and gradient-free optimization. Across a variety of ManiSkill3 manipulation tasks with controlled dynamics shifts, Warp
    RL matches residual correction when translation is sufficient and substantially outperforms it when adaptation requires
    distributional reshaping. We further demonstrate that warping can replace additive correction in an off-policy sim-to-real
    pipeline, achieving comparable success rate with 30% faster task completion on a real-robot peg-insertion task.'
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
- warp_rl
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31043v2.
sources:
- id: src_001
  type: paper
  title: 'Warp RL: Reshaping Base Policy Distributions for Dynamics Adaptation'
  url: https://arxiv.org/abs/2606.31043
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Residual reinforcement learning adapts a pretrained robot policy by learning an additive correction to its actions. While effective when adaptation amounts to shifting the base policy's action distribution, additive corrections cannot change the distribution's shape, scale, or state-dependent geometry -- limitations we formalize as wrong variance, miscalibrated confidence, and non-uniform correction. We show that these matter under dynamics shift: when the base distribution is geometrically mismatched to the shifted system, residual correction can underperform even the unadapted policy. We propose Warp RL, a policy adaptation method that replaces additive residuals with an invertible, state-conditioned transformation of the base policy's action distribution. Instantiated with monotonic rational-quadratic spline flows (arXiv:1906.04032), Warp RL preserves identity initialization, strictly generalizes additive residual correction, and exposes a structured adaptation space suitable for both policy-gradient and gradient-free optimization. Across a variety of ManiSkill3 manipulation tasks with controlled dynamics shifts, Warp RL matches residual correction when translation is sufficient and substantially outperforms it when adaptation requires distributional reshaping. We further demonstrate that warping can replace additive correction in an off-policy sim-to-real pipeline, achieving comparable success rate with 30% faster task completion on a real-robot peg-insertion task.

## 核心内容
Residual reinforcement learning adapts a pretrained robot policy by learning an additive correction to its actions. While effective when adaptation amounts to shifting the base policy's action distribution, additive corrections cannot change the distribution's shape, scale, or state-dependent geometry -- limitations we formalize as wrong variance, miscalibrated confidence, and non-uniform correction. We show that these matter under dynamics shift: when the base distribution is geometrically mismatched to the shifted system, residual correction can underperform even the unadapted policy. We propose Warp RL, a policy adaptation method that replaces additive residuals with an invertible, state-conditioned transformation of the base policy's action distribution. Instantiated with monotonic rational-quadratic spline flows (arXiv:1906.04032), Warp RL preserves identity initialization, strictly generalizes additive residual correction, and exposes a structured adaptation space suitable for both policy-gradient and gradient-free optimization. Across a variety of ManiSkill3 manipulation tasks with controlled dynamics shifts, Warp RL matches residual correction when translation is sufficient and substantially outperforms it when adaptation requires distributional reshaping. We further demonstrate that warping can replace additive correction in an off-policy sim-to-real pipeline, achieving comparable success rate with 30% faster task completion on a real-robot peg-insertion task.

## 参考
- http://arxiv.org/abs/2606.31043v2

## Overview
Residual reinforcement learning adapts a pretrained robot policy by learning an additive correction to its actions. While effective when adaptation amounts to shifting the base policy's action distribution, additive corrections cannot change the distribution's shape, scale, or state-dependent geometry -- limitations we formalize as wrong variance, miscalibrated confidence, and non-uniform correction. We show that these matter under dynamics shift: when the base distribution is geometrically mismatched to the shifted system, residual correction can underperform even the unadapted policy. We propose Warp RL, a policy adaptation method that replaces additive residuals with an invertible, state-conditioned transformation of the base policy's action distribution. Instantiated with monotonic rational-quadratic spline flows (arXiv:1906.04032), Warp RL preserves identity initialization, strictly generalizes additive residual correction, and exposes a structured adaptation space suitable for both policy-gradient and gradient-free optimization. Across a variety of ManiSkill3 manipulation tasks with controlled dynamics shifts, Warp RL matches residual correction when translation is sufficient and substantially outperforms it when adaptation requires distributional reshaping. We further demonstrate that warping can replace additive correction in an off-policy sim-to-real pipeline, achieving comparable success rate with 30% faster task completion on a real-robot peg-insertion task.

## Content
Residual reinforcement learning adapts a pretrained robot policy by learning an additive correction to its actions. While effective when adaptation amounts to shifting the base policy's action distribution, additive corrections cannot change the distribution's shape, scale, or state-dependent geometry -- limitations we formalize as wrong variance, miscalibrated confidence, and non-uniform correction. We show that these matter under dynamics shift: when the base distribution is geometrically mismatched to the shifted system, residual correction can underperform even the unadapted policy. We propose Warp RL, a policy adaptation method that replaces additive residuals with an invertible, state-conditioned transformation of the base policy's action distribution. Instantiated with monotonic rational-quadratic spline flows (arXiv:1906.04032), Warp RL preserves identity initialization, strictly generalizes additive residual correction, and exposes a structured adaptation space suitable for both policy-gradient and gradient-free optimization. Across a variety of ManiSkill3 manipulation tasks with controlled dynamics shifts, Warp RL matches residual correction when translation is sufficient and substantially outperforms it when adaptation requires distributional reshaping. We further demonstrate that warping can replace additive correction in an off-policy sim-to-real pipeline, achieving comparable success rate with 30% faster task completion on a real-robot peg-insertion task.

## 개요
잔차 강화 학습(Residual reinforcement learning)은 사전 훈련된 로봇 정책의 행동에 대한 가산적 보정(additive correction)을 학습하여 이를 적응시킵니다. 적응이 기본 정책의 행동 분포를 이동시키는 것에 해당할 때 효과적이지만, 가산적 보정은 분포의 형태, 척도 또는 상태 의존적 기하학을 변경할 수 없습니다. 이는 잘못된 분산(wrong variance), 잘못 보정된 신뢰도(miscalibrated confidence), 비균일 보정(non-uniform correction)으로 공식화하는 한계입니다. 우리는 이러한 한계가 동역학 변화(dynamics shift) 하에서 중요함을 보여줍니다: 기본 분포가 변화된 시스템과 기하학적으로 일치하지 않을 때, 잔차 보정은 적응되지 않은 정책보다도 성능이 떨어질 수 있습니다. 우리는 Warp RL을 제안합니다. 이는 가산적 잔차를 기본 정책의 행동 분포에 대한 가역적이고 상태 조건화된 변환으로 대체하는 정책 적응 방법입니다. 단조 유리-2차 스플라인 흐름(arXiv:1906.04032)으로 구현된 Warp RL은 항등 초기화(identity initialization)를 유지하고, 가산적 잔차 보정을 엄격히 일반화하며, 정책 경사 및 경사 없는 최적화 모두에 적합한 구조화된 적응 공간을 제공합니다. 제어된 동역학 변화를 가진 다양한 ManiSkill3 조작 작업에서 Warp RL은 이동(translation)만으로 충분할 때 잔차 보정과 동등한 성능을 보이고, 적응에 분포 재형성(distributional reshaping)이 필요할 때는 이를 크게 능가합니다. 또한, 오프-정책 시뮬레이션-실제(sim-to-real) 파이프라인에서 워핑(warping)이 가산적 보정을 대체할 수 있음을 입증하여, 실제 로봇 페그 삽입 작업에서 30% 더 빠른 작업 완료와 함께 유사한 성공률을 달성합니다.

## 핵심 내용
잔차 강화 학습은 사전 훈련된 로봇 정책의 행동에 대한 가산적 보정을 학습하여 이를 적응시킵니다. 적응이 기본 정책의 행동 분포를 이동시키는 것에 해당할 때 효과적이지만, 가산적 보정은 분포의 형태, 척도 또는 상태 의존적 기하학을 변경할 수 없습니다. 이는 잘못된 분산, 잘못 보정된 신뢰도, 비균일 보정으로 공식화하는 한계입니다. 우리는 이러한 한계가 동역학 변화 하에서 중요함을 보여줍니다: 기본 분포가 변화된 시스템과 기하학적으로 일치하지 않을 때, 잔차 보정은 적응되지 않은 정책보다도 성능이 떨어질 수 있습니다. 우리는 Warp RL을 제안합니다. 이는 가산적 잔차를 기본 정책의 행동 분포에 대한 가역적이고 상태 조건화된 변환으로 대체하는 정책 적응 방법입니다. 단조 유리-2차 스플라인 흐름(arXiv:1906.04032)으로 구현된 Warp RL은 항등 초기화를 유지하고, 가산적 잔차 보정을 엄격히 일반화하며, 정책 경사 및 경사 없는 최적화 모두에 적합한 구조화된 적응 공간을 제공합니다. 제어된 동역학 변화를 가진 다양한 ManiSkill3 조작 작업에서 Warp RL은 이동만으로 충분할 때 잔차 보정과 동등한 성능을 보이고, 적응에 분포 재형성이 필요할 때는 이를 크게 능가합니다. 또한, 오프-정책 시뮬레이션-실제 파이프라인에서 워핑이 가산적 보정을 대체할 수 있음을 입증하여, 실제 로봇 페그 삽입 작업에서 30% 더 빠른 작업 완료와 함께 유사한 성공률을 달성합니다.
