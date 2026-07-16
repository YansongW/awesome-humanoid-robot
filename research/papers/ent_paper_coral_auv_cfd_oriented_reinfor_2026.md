---
$id: ent_paper_coral_auv_cfd_oriented_reinfor_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CORAL-AUV: CFD Oriented Reinforcement Learning for Autonomous Underwater Vehicles'
  zh: 'CORAL-AUV: CFD Oriented Reinforcement Learning for Autonomous Underwater Vehicles'
  ko: 'CORAL-AUV: CFD Oriented Reinforcement Learning for Autonomous Underwater Vehicles'
summary:
  en: 'arXiv:2607.09557v1 Announce Type: new Abstract: Fine grain control and positioning of autonomous underwater vehicles
    (AUVs) is critical for sampling, maintenance, and survey applications. Traditional control methods for AUVs are labor
    intensive and are not robust to changes in the vehicle configuration or environmental conditions. Reinforcement learning
    (RL) promises rapid controller development while handling a range of deployment parameters via domain randomization (DR).
    However, DR is still limited by the capacity of the underlying simulation to model real physics. In particular, drag physics
    are difficult to model and are a large contributor to sim-to-real gaps. Meanwhile, computational fluid dynamics (CFD)
    provides high fidelity drag models but is challenging to leverage within reinforcement learning frameworks due to its
    computational overhead. Thus, in this paper we exploit the idea of training surrogate approximations of CFD models of
    a given vehicle, enabling fast inference within RL pipelines. We are the first to successfully deploy a zero-shot RL policy
    on a 6-DOF AUV in which policy training is performed on surrogate drag models (SDMs) trained on CFD data. We find 31%
    lower energy usage compared to a controller using simplified physics while traversing between waypoints 11% faster with
    19% less error. Our SDM based RL controller better predicts zero-shot transfer and is more robust across reward shaping
    design choices. When using DR to complete a task with perturbed parameters, we find that the CFD policy is the only controller
    that successfully transfers. The policies are evaluated in a controlled tank environment and in the field providing extensive
    testing of the policies'' capabilities.'
  zh: 'arXiv:2607.09557v1 Announce Type: new Abstract: Fine grain control and positioning of autonomous underwater vehicles
    (AUVs) is critical for sampling, maintenance, and survey applications. Traditional control methods for AUVs are labor
    intensive and are not robust to changes in the vehicle configuration or environmental conditions. Reinforcement learning
    (RL) promises rapid controller development while handling a range of deployment parameters via domain randomization (DR).
    However, DR is still limited by the capacity of the underlying simulation to model real physics. In particular, drag physics
    are difficult to model and are a large contributor to sim-to-real gaps. Meanwhile, computational fluid dynamics (CFD)
    provides high fidelity drag models but is challenging to leverage within reinforcement learning frameworks due to its
    computational overhead. Thus, in this paper we exploit the idea of training surrogate approximations of CFD models of
    a given vehicle, enabling fast inference within RL pipelines. We are the first to successfully deploy a zero-shot RL policy
    on a 6-DOF AUV in which policy training is performed on surrogate drag models (SDMs) trained on CFD data. We find 31%
    lower energy usage compared to a controller using simplified physics while traversing between waypoints 11% faster with
    19% less error. Our SDM based RL controller better predicts zero-shot transfer and is more robust across reward shaping
    design choices. When using DR to complete a task with perturbed parameters, we find that the CFD policy is the only controller
    that successfully transfers. The policies are evaluated in a controlled tank environment and in the field providing extensive
    testing of the policies'' capabilities.'
  ko: 'arXiv:2607.09557v1 Announce Type: new Abstract: Fine grain control and positioning of autonomous underwater vehicles
    (AUVs) is critical for sampling, maintenance, and survey applications. Traditional control methods for AUVs are labor
    intensive and are not robust to changes in the vehicle configuration or environmental conditions. Reinforcement learning
    (RL) promises rapid controller development while handling a range of deployment parameters via domain randomization (DR).
    However, DR is still limited by the capacity of the underlying simulation to model real physics. In particular, drag physics
    are difficult to model and are a large contributor to sim-to-real gaps. Meanwhile, computational fluid dynamics (CFD)
    provides high fidelity drag models but is challenging to leverage within reinforcement learning frameworks due to its
    computational overhead. Thus, in this paper we exploit the idea of training surrogate approximations of CFD models of
    a given vehicle, enabling fast inference within RL pipelines. We are the first to successfully deploy a zero-shot RL policy
    on a 6-DOF AUV in which policy training is performed on surrogate drag models (SDMs) trained on CFD data. We find 31%
    lower energy usage compared to a controller using simplified physics while traversing between waypoints 11% faster with
    19% less error. Our SDM based RL controller better predicts zero-shot transfer and is more robust across reward shaping
    design choices. When using DR to complete a task with perturbed parameters, we find that the CFD policy is the only controller
    that successfully transfers. The policies are evaluated in a controlled tank environment and in the field providing extensive
    testing of the policies'' capabilities.'
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
- coral_auv
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.09557v1.
sources:
- id: src_001
  type: paper
  title: 'CORAL-AUV: CFD Oriented Reinforcement Learning for Autonomous Underwater Vehicles (arXiv)'
  url: https://arxiv.org/abs/2607.09557
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
Fine grain control and positioning of autonomous underwater vehicles (AUVs) is critical for sampling, maintenance, and survey applications. Traditional control methods for AUVs are labor intensive and are not robust to changes in the vehicle configuration or environmental conditions. Reinforcement learning (RL) promises rapid controller development while handling a range of deployment parameters via domain randomization (DR). However, DR is still limited by the capacity of the underlying simulation to model real physics. In particular, drag physics are difficult to model and are a large contributor to sim-to-real gaps. Meanwhile, computational fluid dynamics (CFD) provides high fidelity drag models but is challenging to leverage within reinforcement learning frameworks due to its computational overhead. Thus, in this paper we exploit the idea of training surrogate approximations of CFD models of a given vehicle, enabling fast inference within RL pipelines. We are the first to successfully deploy a zero-shot RL policy on a 6-DOF AUV in which policy training is performed on surrogate drag models (SDMs) trained on CFD data. We find 31% lower energy usage compared to a controller using simplified physics while traversing between waypoints 11% faster with 19% less error. Our SDM based RL controller better predicts zero-shot transfer and is more robust across reward shaping design choices. When using DR to complete a task with perturbed parameters, we find that the CFD policy is the only controller that successfully transfers. The policies are evaluated in a controlled tank environment and in the field providing extensive testing of the policies' capabilities.

## 核心内容
Fine grain control and positioning of autonomous underwater vehicles (AUVs) is critical for sampling, maintenance, and survey applications. Traditional control methods for AUVs are labor intensive and are not robust to changes in the vehicle configuration or environmental conditions. Reinforcement learning (RL) promises rapid controller development while handling a range of deployment parameters via domain randomization (DR). However, DR is still limited by the capacity of the underlying simulation to model real physics. In particular, drag physics are difficult to model and are a large contributor to sim-to-real gaps. Meanwhile, computational fluid dynamics (CFD) provides high fidelity drag models but is challenging to leverage within reinforcement learning frameworks due to its computational overhead. Thus, in this paper we exploit the idea of training surrogate approximations of CFD models of a given vehicle, enabling fast inference within RL pipelines. We are the first to successfully deploy a zero-shot RL policy on a 6-DOF AUV in which policy training is performed on surrogate drag models (SDMs) trained on CFD data. We find 31% lower energy usage compared to a controller using simplified physics while traversing between waypoints 11% faster with 19% less error. Our SDM based RL controller better predicts zero-shot transfer and is more robust across reward shaping design choices. When using DR to complete a task with perturbed parameters, we find that the CFD policy is the only controller that successfully transfers. The policies are evaluated in a controlled tank environment and in the field providing extensive testing of the policies' capabilities.

## 参考
- http://arxiv.org/abs/2607.09557v1

## Overview
Fine grain control and positioning of autonomous underwater vehicles (AUVs) is critical for sampling, maintenance, and survey applications. Traditional control methods for AUVs are labor intensive and are not robust to changes in the vehicle configuration or environmental conditions. Reinforcement learning (RL) promises rapid controller development while handling a range of deployment parameters via domain randomization (DR). However, DR is still limited by the capacity of the underlying simulation to model real physics. In particular, drag physics are difficult to model and are a large contributor to sim-to-real gaps. Meanwhile, computational fluid dynamics (CFD) provides high fidelity drag models but is challenging to leverage within reinforcement learning frameworks due to its computational overhead. Thus, in this paper we exploit the idea of training surrogate approximations of CFD models of a given vehicle, enabling fast inference within RL pipelines. We are the first to successfully deploy a zero-shot RL policy on a 6-DOF AUV in which policy training is performed on surrogate drag models (SDMs) trained on CFD data. We find 31% lower energy usage compared to a controller using simplified physics while traversing between waypoints 11% faster with 19% less error. Our SDM based RL controller better predicts zero-shot transfer and is more robust across reward shaping design choices. When using DR to complete a task with perturbed parameters, we find that the CFD policy is the only controller that successfully transfers. The policies are evaluated in a controlled tank environment and in the field providing extensive testing of the policies' capabilities.

## Content
Fine grain control and positioning of autonomous underwater vehicles (AUVs) is critical for sampling, maintenance, and survey applications. Traditional control methods for AUVs are labor intensive and are not robust to changes in the vehicle configuration or environmental conditions. Reinforcement learning (RL) promises rapid controller development while handling a range of deployment parameters via domain randomization (DR). However, DR is still limited by the capacity of the underlying simulation to model real physics. In particular, drag physics are difficult to model and are a large contributor to sim-to-real gaps. Meanwhile, computational fluid dynamics (CFD) provides high fidelity drag models but is challenging to leverage within reinforcement learning frameworks due to its computational overhead. Thus, in this paper we exploit the idea of training surrogate approximations of CFD models of a given vehicle, enabling fast inference within RL pipelines. We are the first to successfully deploy a zero-shot RL policy on a 6-DOF AUV in which policy training is performed on surrogate drag models (SDMs) trained on CFD data. We find 31% lower energy usage compared to a controller using simplified physics while traversing between waypoints 11% faster with 19% less error. Our SDM based RL controller better predicts zero-shot transfer and is more robust across reward shaping design choices. When using DR to complete a task with perturbed parameters, we find that the CFD policy is the only controller that successfully transfers. The policies are evaluated in a controlled tank environment and in the field providing extensive testing of the policies' capabilities.

## 개요
자율 수중 차량(AUV)의 미세 제어 및 위치 결정은 샘플링, 유지보수 및 조사 응용 분야에서 매우 중요합니다. AUV를 위한 전통적인 제어 방법은 노동 집약적이며 차량 구성이나 환경 조건의 변화에 강건하지 않습니다. 강화 학습(RL)은 도메인 무작위화(DR)를 통해 다양한 배치 매개변수를 처리하면서 빠른 제어기 개발을 약속합니다. 그러나 DR은 여전히 실제 물리 현상을 모델링하는 기반 시뮬레이션의 용량에 의해 제한됩니다. 특히 항력 물리 현상은 모델링하기 어렵고 시뮬레이션-실제 격차에 큰 기여를 합니다. 한편, 전산 유체 역학(CFD)은 높은 충실도의 항력 모델을 제공하지만 계산 오버헤드로 인해 강화 학습 프레임워크 내에서 활용하기 어렵습니다. 따라서 본 논문에서는 특정 차량의 CFD 모델에 대한 대리 근사 모델을 훈련하여 RL 파이프라인 내에서 빠른 추론을 가능하게 하는 아이디어를 활용합니다. 우리는 CFD 데이터로 훈련된 대리 항력 모델(SDM)에서 정책 훈련을 수행하는 6자유도 AUV에 제로샷 RL 정책을 성공적으로 배치한 최초의 사례입니다. 단순화된 물리 모델을 사용하는 제어기와 비교하여 웨이포인트 간 이동 시 31% 낮은 에너지 사용, 11% 더 빠른 이동, 19% 더 적은 오류를 발견했습니다. SDM 기반 RL 제어기는 제로샷 전이를 더 잘 예측하며 보상 형성 설계 선택 전반에 걸쳐 더 강건합니다. 교란된 매개변수로 작업을 완료하기 위해 DR을 사용할 때, CFD 정책만이 성공적으로 전이되는 유일한 제어기임을 확인했습니다. 정책은 제어된 탱크 환경과 현장에서 평가되어 정책의 능력에 대한 광범위한 테스트를 제공합니다.

## 핵심 내용
자율 수중 차량(AUV)의 미세 제어 및 위치 결정은 샘플링, 유지보수 및 조사 응용 분야에서 매우 중요합니다. AUV를 위한 전통적인 제어 방법은 노동 집약적이며 차량 구성이나 환경 조건의 변화에 강건하지 않습니다. 강화 학습(RL)은 도메인 무작위화(DR)를 통해 다양한 배치 매개변수를 처리하면서 빠른 제어기 개발을 약속합니다. 그러나 DR은 여전히 실제 물리 현상을 모델링하는 기반 시뮬레이션의 용량에 의해 제한됩니다. 특히 항력 물리 현상은 모델링하기 어렵고 시뮬레이션-실제 격차에 큰 기여를 합니다. 한편, 전산 유체 역학(CFD)은 높은 충실도의 항력 모델을 제공하지만 계산 오버헤드로 인해 강화 학습 프레임워크 내에서 활용하기 어렵습니다. 따라서 본 논문에서는 특정 차량의 CFD 모델에 대한 대리 근사 모델을 훈련하여 RL 파이프라인 내에서 빠른 추론을 가능하게 하는 아이디어를 활용합니다. 우리는 CFD 데이터로 훈련된 대리 항력 모델(SDM)에서 정책 훈련을 수행하는 6자유도 AUV에 제로샷 RL 정책을 성공적으로 배치한 최초의 사례입니다. 단순화된 물리 모델을 사용하는 제어기와 비교하여 웨이포인트 간 이동 시 31% 낮은 에너지 사용, 11% 더 빠른 이동, 19% 더 적은 오류를 발견했습니다. SDM 기반 RL 제어기는 제로샷 전이를 더 잘 예측하며 보상 형성 설계 선택 전반에 걸쳐 더 강건합니다. 교란된 매개변수로 작업을 완료하기 위해 DR을 사용할 때, CFD 정책만이 성공적으로 전이되는 유일한 제어기임을 확인했습니다. 정책은 제어된 탱크 환경과 현장에서 평가되어 정책의 능력에 대한 광범위한 테스트를 제공합니다.
