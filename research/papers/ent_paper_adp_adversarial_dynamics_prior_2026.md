---
$id: ent_paper_adp_adversarial_dynamics_prior_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ADP: Adversarial Dynamics Priors for Physically Grounded Humanoid Locomotion'
  zh: 'ADP: Adversarial Dynamics Priors for Physically Grounded Humanoid Locomotion'
  ko: 'ADP: Adversarial Dynamics Priors for Physically Grounded Humanoid Locomotion'
summary:
  en: 'arXiv:2607.03454v1 Announce Type: new Abstract: In this paper, we propose Adversarial Dynamics Priors (ADP) for perturbation-resilient
    humanoid locomotion control. Existing motion prior-based methods induce natural motion styles by imitating kinematic motion
    features, but they do not directly regularize dynamics features, such as CoM motion, centroidal momentum, contact forces,
    and contact states. To address this limitation, we replace kinematic motion-style feature with selected dynamics features
    extracted from locomotion trajectories as the target of adversarial regularization.To this end, we use trajectory optimization
    to construct a reference dataset and train a discriminator to evaluate whether policy-induced temporal windows are consistent
    with the resulting reference distribution.Without explicit motion tracking, ADP encourages policy rollouts to remain close
    to the reference support, even after perturbations. Experimental results show that, compared with AMP, the strongest baseline
    in our evaluation, ADP improves the $80\%$-success impulse threshold ($J_{80}$) by $16.7\%$, while reducing direction-averaged
    recovery time and velocity tracking error by $47.9\%$ and $35.4\%$, respectively.'
  zh: 'arXiv:2607.03454v1 Announce Type: new Abstract: In this paper, we propose Adversarial Dynamics Priors (ADP) for perturbation-resilient
    humanoid locomotion control. Existing motion prior-based methods induce natural motion styles by imitating kinematic motion
    features, but they do not directly regularize dynamics features, such as CoM motion, centroidal momentum, contact forces,
    and contact states. To address this limitation, we replace kinematic motion-style feature with selected dynamics features
    extracted from locomotion trajectories as the target of adversarial regularization.To this end, we use trajectory optimization
    to construct a reference dataset and train a discriminator to evaluate whether policy-induced temporal windows are consistent
    with the resulting reference distribution.Without explicit motion tracking, ADP encourages policy rollouts to remain close
    to the reference support, even after perturbations. Experimental results show that, compared with AMP, the strongest baseline
    in our evaluation, ADP improves the $80\%$-success impulse threshold ($J_{80}$) by $16.7\%$, while reducing direction-averaged
    recovery time and velocity tracking error by $47.9\%$ and $35.4\%$, respectively.'
  ko: 'arXiv:2607.03454v1 Announce Type: new Abstract: In this paper, we propose Adversarial Dynamics Priors (ADP) for perturbation-resilient
    humanoid locomotion control. Existing motion prior-based methods induce natural motion styles by imitating kinematic motion
    features, but they do not directly regularize dynamics features, such as CoM motion, centroidal momentum, contact forces,
    and contact states. To address this limitation, we replace kinematic motion-style feature with selected dynamics features
    extracted from locomotion trajectories as the target of adversarial regularization.To this end, we use trajectory optimization
    to construct a reference dataset and train a discriminator to evaluate whether policy-induced temporal windows are consistent
    with the resulting reference distribution.Without explicit motion tracking, ADP encourages policy rollouts to remain close
    to the reference support, even after perturbations. Experimental results show that, compared with AMP, the strongest baseline
    in our evaluation, ADP improves the $80\%$-success impulse threshold ($J_{80}$) by $16.7\%$, while reducing direction-averaged
    recovery time and velocity tracking error by $47.9\%$ and $35.4\%$, respectively.'
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
- adp
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03454v1.
sources:
- id: src_001
  type: paper
  title: 'ADP: Adversarial Dynamics Priors for Physically Grounded Humanoid Locomotion (arXiv)'
  url: https://arxiv.org/abs/2607.03454
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
In this paper, we propose Adversarial Dynamics Priors (ADP) for perturbation-resilient humanoid locomotion control. Existing motion prior-based methods induce natural motion styles by imitating kinematic motion features, but they do not directly regularize dynamics features, such as CoM motion, centroidal momentum, contact forces, and contact states. To address this limitation, we replace kinematic motion-style feature with selected dynamics features extracted from locomotion trajectories as the target of adversarial regularization.To this end, we use trajectory optimization to construct a reference dataset and train a discriminator to evaluate whether policy-induced temporal windows are consistent with the resulting reference distribution.Without explicit motion tracking, ADP encourages policy rollouts to remain close to the reference support, even after perturbations. Experimental results show that, compared with AMP, the strongest baseline in our evaluation, ADP improves the $80\%$-success impulse threshold ($J_{80}$) by $16.7\%$, while reducing direction-averaged recovery time and velocity tracking error by $47.9\%$ and $35.4\%$, respectively.

## 核心内容
In this paper, we propose Adversarial Dynamics Priors (ADP) for perturbation-resilient humanoid locomotion control. Existing motion prior-based methods induce natural motion styles by imitating kinematic motion features, but they do not directly regularize dynamics features, such as CoM motion, centroidal momentum, contact forces, and contact states. To address this limitation, we replace kinematic motion-style feature with selected dynamics features extracted from locomotion trajectories as the target of adversarial regularization.To this end, we use trajectory optimization to construct a reference dataset and train a discriminator to evaluate whether policy-induced temporal windows are consistent with the resulting reference distribution.Without explicit motion tracking, ADP encourages policy rollouts to remain close to the reference support, even after perturbations. Experimental results show that, compared with AMP, the strongest baseline in our evaluation, ADP improves the $80\%$-success impulse threshold ($J_{80}$) by $16.7\%$, while reducing direction-averaged recovery time and velocity tracking error by $47.9\%$ and $35.4\%$, respectively.

## 参考
- http://arxiv.org/abs/2607.03454v1

## Overview
In this paper, we propose Adversarial Dynamics Priors (ADP) for perturbation-resilient humanoid locomotion control. Existing motion prior-based methods induce natural motion styles by imitating kinematic motion features, but they do not directly regularize dynamics features, such as CoM motion, centroidal momentum, contact forces, and contact states. To address this limitation, we replace kinematic motion-style features with selected dynamics features extracted from locomotion trajectories as the target of adversarial regularization. To this end, we use trajectory optimization to construct a reference dataset and train a discriminator to evaluate whether policy-induced temporal windows are consistent with the resulting reference distribution. Without explicit motion tracking, ADP encourages policy rollouts to remain close to the reference support, even after perturbations. Experimental results show that, compared with AMP, the strongest baseline in our evaluation, ADP improves the $80\%$-success impulse threshold ($J_{80}$) by $16.7\%$, while reducing direction-averaged recovery time and velocity tracking error by $47.9\%$ and $35.4\%$, respectively.

## Content
In this paper, we propose Adversarial Dynamics Priors (ADP) for perturbation-resilient humanoid locomotion control. Existing motion prior-based methods induce natural motion styles by imitating kinematic motion features, but they do not directly regularize dynamics features, such as CoM motion, centroidal momentum, contact forces, and contact states. To address this limitation, we replace kinematic motion-style features with selected dynamics features extracted from locomotion trajectories as the target of adversarial regularization. To this end, we use trajectory optimization to construct a reference dataset and train a discriminator to evaluate whether policy-induced temporal windows are consistent with the resulting reference distribution. Without explicit motion tracking, ADP encourages policy rollouts to remain close to the reference support, even after perturbations. Experimental results show that, compared with AMP, the strongest baseline in our evaluation, ADP improves the $80\%$-success impulse threshold ($J_{80}$) by $16.7\%$, while reducing direction-averaged recovery time and velocity tracking error by $47.9\%$ and $35.4\%$, respectively.

## 개요
본 논문에서는 외란에 강건한 휴머노이드 보행 제어를 위한 적대적 동역학 사전(ADP)을 제안합니다. 기존의 동작 사전 기반 방법은 운동학적 동작 특징을 모방하여 자연스러운 동작 스타일을 유도하지만, CoM 운동, 중심 운동량, 접촉력 및 접촉 상태와 같은 동역학 특징을 직접적으로 정규화하지는 않습니다. 이러한 한계를 해결하기 위해, 우리는 운동학적 동작 스타일 특징을 보행 궤적에서 추출한 선택된 동역학 특징으로 대체하여 적대적 정규화의 대상으로 삼습니다. 이를 위해 궤적 최적화를 사용하여 참조 데이터셋을 구축하고, 정책이 유도하는 시간 창이 결과 참조 분포와 일관성이 있는지 평가하는 판별기를 훈련합니다. 명시적인 동작 추적 없이도 ADP는 정책 롤아웃이 외란 이후에도 참조 지지 영역에 가깝게 유지되도록 장려합니다. 실험 결과, 평가에서 가장 강력한 기준선인 AMP와 비교하여 ADP는 $80\%$ 성공 임펄스 임계값($J_{80}$)을 $16.7\%$ 향상시키고, 방향 평균 회복 시간과 속도 추적 오차를 각각 $47.9\%$ 및 $35.4\%$ 감소시킵니다.

## 핵심 내용
본 논문에서는 외란에 강건한 휴머노이드 보행 제어를 위한 적대적 동역학 사전(ADP)을 제안합니다. 기존의 동작 사전 기반 방법은 운동학적 동작 특징을 모방하여 자연스러운 동작 스타일을 유도하지만, CoM 운동, 중심 운동량, 접촉력 및 접촉 상태와 같은 동역학 특징을 직접적으로 정규화하지는 않습니다. 이러한 한계를 해결하기 위해, 우리는 운동학적 동작 스타일 특징을 보행 궤적에서 추출한 선택된 동역학 특징으로 대체하여 적대적 정규화의 대상으로 삼습니다. 이를 위해 궤적 최적화를 사용하여 참조 데이터셋을 구축하고, 정책이 유도하는 시간 창이 결과 참조 분포와 일관성이 있는지 평가하는 판별기를 훈련합니다. 명시적인 동작 추적 없이도 ADP는 정책 롤아웃이 외란 이후에도 참조 지지 영역에 가깝게 유지되도록 장려합니다. 실험 결과, 평가에서 가장 강력한 기준선인 AMP와 비교하여 ADP는 $80\%$ 성공 임펄스 임계값($J_{80}$)을 $16.7\%$ 향상시키고, 방향 평균 회복 시간과 속도 추적 오차를 각각 $47.9\%$ 및 $35.4\%$ 감소시킵니다.
