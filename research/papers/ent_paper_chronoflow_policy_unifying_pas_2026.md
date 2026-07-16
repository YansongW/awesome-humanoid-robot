---
$id: ent_paper_chronoflow_policy_unifying_pas_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ChronoFlow-Policy: Unifying Past-Current-Future Interaction Flow in Visuomotor Policy Learning'
  zh: 'ChronoFlow-Policy: Unifying Past-Current-Future Interaction Flow in Visuomotor Policy Learning'
  ko: 'ChronoFlow-Policy: Unifying Past-Current-Future Interaction Flow in Visuomotor Policy Learning'
summary:
  en: 'arXiv:2606.31493v1 Announce Type: new Abstract: Visual signals play a crucial role in policy learning by enabling models
    to capture object motion and interaction dynamics. Just as humans reason about actions using both past experience and
    anticipated outcomes, effective policies should integrate past interactions with future predictions. However, existing
    visuomotor policies typically model either historical context or future dynamics in isolation, lacking a unified temporal
    representation of interaction dynamics. In this work, we introduce \textbf{ChronoFlow}, a temporally unified representation
    that captures \textbf{past, current, and future} interaction dynamics through sparse 3D keypoints of both objects and
    the gripper. Based on this representation, we propose \textbf{ChronoFlow-Policy}, a diffusion-based visuomotor policy
    that jointly learns ChronoFlow and action sequences through a co-training objective. Experiments on 14 simulated tasks
    and 5 real-world manipulation tasks demonstrate that ChronoFlow-Policy consistently outperforms strong diffusion-policy
    baselines and improves robustness in long-horizon and non-Markovian manipulation scenarios.'
  zh: 'arXiv:2606.31493v1 Announce Type: new Abstract: Visual signals play a crucial role in policy learning by enabling models
    to capture object motion and interaction dynamics. Just as humans reason about actions using both past experience and
    anticipated outcomes, effective policies should integrate past interactions with future predictions. However, existing
    visuomotor policies typically model either historical context or future dynamics in isolation, lacking a unified temporal
    representation of interaction dynamics. In this work, we introduce \textbf{ChronoFlow}, a temporally unified representation
    that captures \textbf{past, current, and future} interaction dynamics through sparse 3D keypoints of both objects and
    the gripper. Based on this representation, we propose \textbf{ChronoFlow-Policy}, a diffusion-based visuomotor policy
    that jointly learns ChronoFlow and action sequences through a co-training objective. Experiments on 14 simulated tasks
    and 5 real-world manipulation tasks demonstrate that ChronoFlow-Policy consistently outperforms strong diffusion-policy
    baselines and improves robustness in long-horizon and non-Markovian manipulation scenarios.'
  ko: 'arXiv:2606.31493v1 Announce Type: new Abstract: Visual signals play a crucial role in policy learning by enabling models
    to capture object motion and interaction dynamics. Just as humans reason about actions using both past experience and
    anticipated outcomes, effective policies should integrate past interactions with future predictions. However, existing
    visuomotor policies typically model either historical context or future dynamics in isolation, lacking a unified temporal
    representation of interaction dynamics. In this work, we introduce \textbf{ChronoFlow}, a temporally unified representation
    that captures \textbf{past, current, and future} interaction dynamics through sparse 3D keypoints of both objects and
    the gripper. Based on this representation, we propose \textbf{ChronoFlow-Policy}, a diffusion-based visuomotor policy
    that jointly learns ChronoFlow and action sequences through a co-training objective. Experiments on 14 simulated tasks
    and 5 real-world manipulation tasks demonstrate that ChronoFlow-Policy consistently outperforms strong diffusion-policy
    baselines and improves robustness in long-horizon and non-Markovian manipulation scenarios.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- chronoflow_policy
- humanoid
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31493v2.
sources:
- id: src_001
  type: paper
  title: 'ChronoFlow-Policy: Unifying Past-Current-Future Interaction Flow in Visuomotor Policy Learning'
  url: https://arxiv.org/abs/2606.31493
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Visual signals play a crucial role in policy learning by enabling models to capture object motion and interaction dynamics. Just as humans reason about actions using both past experience and anticipated outcomes, effective policies should integrate past interactions with future predictions. However, existing visuomotor policies typically model either historical context or future dynamics in isolation, lacking a unified temporal representation of interaction dynamics. In this work, we introduce ChronoFlow, a temporally unified representation that captures past, current, and future interaction dynamics through sparse 3D keypoints of both objects and the gripper. Based on this representation, we propose ChronoFlow-Policy, a diffusion-based visuomotor policy that jointly learns ChronoFlow and action sequences through a co-training objective. Experiments on 14 simulated tasks and 5 real-world manipulation tasks demonstrate that ChronoFlow-Policy consistently outperforms strong diffusion-policy baselines and improves robustness in long-horizon and non-Markovian manipulation scenarios. Our project page is available at https://the-kamisato-sii.github.io/ChronoFlow-Policy-project-page/.

## 核心内容
Visual signals play a crucial role in policy learning by enabling models to capture object motion and interaction dynamics. Just as humans reason about actions using both past experience and anticipated outcomes, effective policies should integrate past interactions with future predictions. However, existing visuomotor policies typically model either historical context or future dynamics in isolation, lacking a unified temporal representation of interaction dynamics. In this work, we introduce ChronoFlow, a temporally unified representation that captures past, current, and future interaction dynamics through sparse 3D keypoints of both objects and the gripper. Based on this representation, we propose ChronoFlow-Policy, a diffusion-based visuomotor policy that jointly learns ChronoFlow and action sequences through a co-training objective. Experiments on 14 simulated tasks and 5 real-world manipulation tasks demonstrate that ChronoFlow-Policy consistently outperforms strong diffusion-policy baselines and improves robustness in long-horizon and non-Markovian manipulation scenarios. Our project page is available at https://the-kamisato-sii.github.io/ChronoFlow-Policy-project-page/.

## 参考
- http://arxiv.org/abs/2606.31493v2

## Overview
Visual signals play a crucial role in policy learning by enabling models to capture object motion and interaction dynamics. Just as humans reason about actions using both past experience and anticipated outcomes, effective policies should integrate past interactions with future predictions. However, existing visuomotor policies typically model either historical context or future dynamics in isolation, lacking a unified temporal representation of interaction dynamics. In this work, we introduce ChronoFlow, a temporally unified representation that captures past, current, and future interaction dynamics through sparse 3D keypoints of both objects and the gripper. Based on this representation, we propose ChronoFlow-Policy, a diffusion-based visuomotor policy that jointly learns ChronoFlow and action sequences through a co-training objective. Experiments on 14 simulated tasks and 5 real-world manipulation tasks demonstrate that ChronoFlow-Policy consistently outperforms strong diffusion-policy baselines and improves robustness in long-horizon and non-Markovian manipulation scenarios. Our project page is available at https://the-kamisato-sii.github.io/ChronoFlow-Policy-project-page/.

## Content
Visual signals play a crucial role in policy learning by enabling models to capture object motion and interaction dynamics. Just as humans reason about actions using both past experience and anticipated outcomes, effective policies should integrate past interactions with future predictions. However, existing visuomotor policies typically model either historical context or future dynamics in isolation, lacking a unified temporal representation of interaction dynamics. In this work, we introduce ChronoFlow, a temporally unified representation that captures past, current, and future interaction dynamics through sparse 3D keypoints of both objects and the gripper. Based on this representation, we propose ChronoFlow-Policy, a diffusion-based visuomotor policy that jointly learns ChronoFlow and action sequences through a co-training objective. Experiments on 14 simulated tasks and 5 real-world manipulation tasks demonstrate that ChronoFlow-Policy consistently outperforms strong diffusion-policy baselines and improves robustness in long-horizon and non-Markovian manipulation scenarios. Our project page is available at https://the-kamisato-sii.github.io/ChronoFlow-Policy-project-page/.

## 개요
시각 신호는 모델이 객체의 움직임과 상호작용 역학을 포착할 수 있게 함으로써 정책 학습에서 중요한 역할을 합니다. 인간이 과거 경험과 예상 결과를 모두 사용하여 행동을 추론하는 것처럼, 효과적인 정책은 과거 상호작용과 미래 예측을 통합해야 합니다. 그러나 기존의 시각운동 정책은 일반적으로 역사적 맥락이나 미래 역학을 개별적으로 모델링하여 상호작용 역학의 통일된 시간적 표현이 부족합니다. 본 연구에서는 객체와 그리퍼의 희소 3D 키포인트를 통해 과거, 현재, 미래의 상호작용 역학을 포착하는 시간적으로 통일된 표현인 ChronoFlow를 소개합니다. 이 표현을 기반으로, 공동 훈련 목표를 통해 ChronoFlow와 행동 시퀀스를 함께 학습하는 확산 기반 시각운동 정책인 ChronoFlow-Policy를 제안합니다. 14개의 시뮬레이션 작업과 5개의 실제 조작 작업에 대한 실험은 ChronoFlow-Policy가 강력한 확산 정책 기준선을 일관되게 능가하고, 장기 지평 및 비마르코프 조작 시나리오에서 견고성을 향상시킴을 보여줍니다. 프로젝트 페이지는 https://the-kamisato-sii.github.io/ChronoFlow-Policy-project-page/에서 확인할 수 있습니다.

## 핵심 내용
시각 신호는 모델이 객체의 움직임과 상호작용 역학을 포착할 수 있게 함으로써 정책 학습에서 중요한 역할을 합니다. 인간이 과거 경험과 예상 결과를 모두 사용하여 행동을 추론하는 것처럼, 효과적인 정책은 과거 상호작용과 미래 예측을 통합해야 합니다. 그러나 기존의 시각운동 정책은 일반적으로 역사적 맥락이나 미래 역학을 개별적으로 모델링하여 상호작용 역학의 통일된 시간적 표현이 부족합니다. 본 연구에서는 객체와 그리퍼의 희소 3D 키포인트를 통해 과거, 현재, 미래의 상호작용 역학을 포착하는 시간적으로 통일된 표현인 ChronoFlow를 소개합니다. 이 표현을 기반으로, 공동 훈련 목표를 통해 ChronoFlow와 행동 시퀀스를 함께 학습하는 확산 기반 시각운동 정책인 ChronoFlow-Policy를 제안합니다. 14개의 시뮬레이션 작업과 5개의 실제 조작 작업에 대한 실험은 ChronoFlow-Policy가 강력한 확산 정책 기준선을 일관되게 능가하고, 장기 지평 및 비마르코프 조작 시나리오에서 견고성을 향상시킴을 보여줍니다. 프로젝트 페이지는 https://the-kamisato-sii.github.io/ChronoFlow-Policy-project-page/에서 확인할 수 있습니다.
