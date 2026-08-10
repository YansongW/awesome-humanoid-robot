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
  zh: CORAL-AUV 提出了一种结合计算流体动力学（CFD）与强化学习（RL）的方法，用于自主水下航行器（AUV）的精细控制。该研究首次在六自由度AUV上成功部署零样本RL策略，通过训练基于CFD数据的替代阻力模型（SDMs）实现快速推理。实验表明，相比传统简化物理控制器，该方法能耗降低31%，航点间穿越速度提升11%，误差减少19%。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.09557v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (826 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'CORAL-AUV: CFD Oriented Reinforcement Learning for Autonomous Underwater Vehicles (arXiv)'
  url: https://arxiv.org/abs/2607.09557
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
传统AUV控制方法劳动密集且对配置或环境变化缺乏鲁棒性，而强化学习虽能通过域随机化（DR）处理部署参数变化，却受限于仿真对真实物理（尤其是阻力模型）的建模能力。计算流体动力学虽能提供高保真阻力模型，但因计算开销难以直接融入RL框架。为此，本文提出训练基于CFD数据的替代阻力模型（SDMs），使其在RL管线中实现快速推理。该零样本策略在六自由度AUV上成功部署，在受控水池和实地环境中均经过验证，展现出更优的零样本迁移预测能力和对奖励函数设计的鲁棒性。

## 核心内容
### 方法架构
- **核心思路**：利用计算流体动力学（CFD）生成高保真阻力数据，训练替代阻力模型（SDMs）作为快速推理代理，替代传统简化物理模型嵌入强化学习（RL）管线。
- **策略训练**：在六自由度（6-DOF）AUV上，基于SDMs进行策略训练，实现零样本（zero-shot）部署，无需在真实环境中微调。

### 实验设置
- **对比基线**：采用基于简化物理模型的控制器作为对比。
- **评估环境**：在受控水池（controlled tank）和实地（field）环境中进行广泛测试，涵盖航点导航任务。
- **域随机化（DR）测试**：在参数扰动条件下评估策略迁移能力。

### 关键结果
- **性能提升**：相比简化物理控制器，SDM-based RL控制器在航点间穿越时能耗降低31%，速度提升11%，路径误差减少19%。
- **零样本迁移**：SDM策略能更准确地预测零样本迁移效果，且对奖励函数设计（reward shaping）的鲁棒性更强。
- **域随机化表现**：在参数扰动任务中，基于CFD的策略是唯一成功迁移的控制器，而其他控制器均失败。

### 结论
本文首次证明，通过训练CFD数据的替代模型，可在RL框架中高效利用高保真阻力物理，显著提升AUV控制器的能效、速度和精度，同时增强对部署条件变化的鲁棒性。

## Overview
Fine grain control and positioning of autonomous underwater vehicles (AUVs) is critical for sampling, maintenance, and survey applications. Traditional control methods for AUVs are labor intensive and are not robust to changes in the vehicle configuration or environmental conditions. Reinforcement learning (RL) promises rapid controller development while handling a range of deployment parameters via domain randomization (DR). However, DR is still limited by the capacity of the underlying simulation to model real physics. In particular, drag physics are difficult to model and are a large contributor to sim-to-real gaps. Meanwhile, computational fluid dynamics (CFD) provides high fidelity drag models but is challenging to leverage within reinforcement learning frameworks due to its computational overhead. Thus, in this paper we exploit the idea of training surrogate approximations of CFD models of a given vehicle, enabling fast inference within RL pipelines. We are the first to successfully deploy a zero-shot RL policy on a 6-DOF AUV in which policy training is performed on surrogate drag models (SDMs) trained on CFD data. We find 31% lower energy usage compared to a controller using simplified physics while traversing between waypoints 11% faster with 19% less error. Our SDM based RL controller better predicts zero-shot transfer and is more robust across reward shaping design choices. When using DR to complete a task with perturbed parameters, we find that the CFD policy is the only controller that successfully transfers. The policies are evaluated in a controlled tank environment and in the field providing extensive testing of the policies' capabilities.

## 参考
- http://arxiv.org/abs/2607.09557v1

## 개요
전통적인 AUV 제어 방법은 노동 집약적이며 구성이나 환경 변화에 대한 견고성이 부족합니다. 반면 강화 학습은 도메인 무작위화(DR)를 통해 배포 매개변수 변화를 처리할 수 있지만, 시뮬레이션이 실제 물리(특히 항력 모델)를 모델링하는 능력에 제한을 받습니다. 계산 유체 역학은 고충실도 항력 모델을 제공할 수 있지만, 계산 비용 때문에 RL 프레임워크에 직접 통합하기 어렵습니다. 이를 위해 본 논문은 CFD 데이터 기반의 대체 항력 모델(SDMs)을 훈련하여 RL 파이프라인에서 빠른 추론을 가능하게 하는 방법을 제안합니다. 이 제로샷 정책은 6자유도 AUV에서 성공적으로 배포되었으며, 통제된 수조와 현장 환경 모두에서 검증되어 더 우수한 제로샷 전이 예측 능력과 보상 함수 설계에 대한 견고성을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
- **핵심 아이디어**: 계산 유체 역학(CFD)을 활용해 고충실도 항력 데이터를 생성하고, 대체 항력 모델(SDMs)을 빠른 추론 에이전트로 훈련하여 기존의 단순화된 물리 모델을 대체해 강화 학습(RL) 파이프라인에 통합합니다.
- **정책 훈련**: 6자유도(6-DOF) AUV에서 SDMs 기반 정책 훈련을 수행하여, 실제 환경에서의 미세 조정 없이 제로샷(zero-shot) 배포를 구현합니다.

### 실험 설정
- **비교 기준선**: 단순화된 물리 모델 기반 제어기를 비교 기준으로 사용합니다.
- **평가 환경**: 통제된 수조(controlled tank) 및 현장(field) 환경에서 웨이포인트 내비게이션 작업을 포함한 광범위한 테스트를 수행합니다.
- **도메인 무작위화(DR) 테스트**: 매개변수 교란 조건에서 정책 전이 능력을 평가합니다.

### 주요 결과
- **성능 향상**: 단순화된 물리 제어기와 비교해 SDM 기반 RL 제어기는 웨이포인트 간 이동 시 에너지 소비를 31% 절감하고, 속도를 11% 향상시키며, 경로 오차를 19% 줄였습니다.
- **제로샷 전이**: SDM 정책은 제로샷 전이 효과를 더 정확하게 예측하며, 보상 함수 설계(reward shaping)에 대한 견고성이 더 강합니다.
- **도메인 무작위화 성능**: 매개변수 교란 작업에서 CFD 기반 정책은 유일하게 성공적으로 전이된 제어기였으며, 다른 제어기는 모두 실패했습니다.

### 결론
본 논문은 CFD 데이터의 대체 모델을 훈련함으로써 RL 프레임워크에서 고충실도 항력 물리를 효율적으로 활용할 수 있음을 처음으로 입증했으며, AUV 제어기의 에너지 효율, 속도 및 정밀도를 크게 향상시키고 배포 조건 변화에 대한 견고성을 강화했습니다.
