---
$id: ent_paper_towards_bridging_the_gap_syste_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Towards bridging the gap: Systematic sim-to-real transfer for diverse legged robots'
  zh: 'Towards bridging the gap: Systematic sim-to-real transfer for diverse legged robots'
  ko: 'Towards bridging the gap: Systematic sim-to-real transfer for diverse legged robots'
summary:
  en: 'Towards bridging the gap: Systematic sim-to-real transfer for diverse legged robots is a 2025 work on sim-to-real for
    humanoid robots.'
  zh: 'Towards bridging the gap: Systematic sim-to-real transfer for diverse legged robots is a 2025 work on sim-to-real for
    humanoid robots.'
  ko: 'Towards bridging the gap: Systematic sim-to-real transfer for diverse legged robots is a 2025 work on sim-to-real for
    humanoid robots.'
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
- sim_to_real
- towards_bridging_the_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.06342v1.
sources:
- id: src_001
  type: paper
  title: 'Towards bridging the gap: Systematic sim-to-real transfer for diverse legged robots (arXiv)'
  url: https://arxiv.org/abs/2509.06342
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Legged robots must achieve both robust locomotion and energy efficiency to be practical in real-world environments. Yet controllers trained in simulation often fail to transfer reliably, and most existing approaches neglect actuator-specific energy losses or depend on complex, hand-tuned reward formulations. We propose a framework that integrates sim-to-real reinforcement learning with a physics-grounded energy model for permanent magnet synchronous motors. The framework requires a minimal parameter set to capture the simulation-to-reality gap and employs a compact four-term reward with a first-principle-based energetic loss formulation that balances electrical and mechanical dissipation. We evaluate and validate the approach through a bottom-up dynamic parameter identification study, spanning actuators, full-robot in-air trajectories and on-ground locomotion. The framework is tested on three primary platforms and deployed on ten additional robots, demonstrating reliable policy transfer without randomization of dynamic parameters. Our method improves energetic efficiency over state-of-the-art methods, achieving a 32 percent reduction in the full Cost of Transport of ANYmal (value 1.27). All code, models, and datasets will be released.

## 核心内容
Legged robots must achieve both robust locomotion and energy efficiency to be practical in real-world environments. Yet controllers trained in simulation often fail to transfer reliably, and most existing approaches neglect actuator-specific energy losses or depend on complex, hand-tuned reward formulations. We propose a framework that integrates sim-to-real reinforcement learning with a physics-grounded energy model for permanent magnet synchronous motors. The framework requires a minimal parameter set to capture the simulation-to-reality gap and employs a compact four-term reward with a first-principle-based energetic loss formulation that balances electrical and mechanical dissipation. We evaluate and validate the approach through a bottom-up dynamic parameter identification study, spanning actuators, full-robot in-air trajectories and on-ground locomotion. The framework is tested on three primary platforms and deployed on ten additional robots, demonstrating reliable policy transfer without randomization of dynamic parameters. Our method improves energetic efficiency over state-of-the-art methods, achieving a 32 percent reduction in the full Cost of Transport of ANYmal (value 1.27). All code, models, and datasets will be released.

## 参考
- http://arxiv.org/abs/2509.06342v1

## Overview
Legged robots must achieve both robust locomotion and energy efficiency to be practical in real-world environments. Yet controllers trained in simulation often fail to transfer reliably, and most existing approaches neglect actuator-specific energy losses or depend on complex, hand-tuned reward formulations. We propose a framework that integrates sim-to-real reinforcement learning with a physics-grounded energy model for permanent magnet synchronous motors. The framework requires a minimal parameter set to capture the simulation-to-reality gap and employs a compact four-term reward with a first-principle-based energetic loss formulation that balances electrical and mechanical dissipation. We evaluate and validate the approach through a bottom-up dynamic parameter identification study, spanning actuators, full-robot in-air trajectories and on-ground locomotion. The framework is tested on three primary platforms and deployed on ten additional robots, demonstrating reliable policy transfer without randomization of dynamic parameters. Our method improves energetic efficiency over state-of-the-art methods, achieving a 32 percent reduction in the full Cost of Transport of ANYmal (value 1.27). All code, models, and datasets will be released.

## Content
Legged robots must achieve both robust locomotion and energy efficiency to be practical in real-world environments. Yet controllers trained in simulation often fail to transfer reliably, and most existing approaches neglect actuator-specific energy losses or depend on complex, hand-tuned reward formulations. We propose a framework that integrates sim-to-real reinforcement learning with a physics-grounded energy model for permanent magnet synchronous motors. The framework requires a minimal parameter set to capture the simulation-to-reality gap and employs a compact four-term reward with a first-principle-based energetic loss formulation that balances electrical and mechanical dissipation. We evaluate and validate the approach through a bottom-up dynamic parameter identification study, spanning actuators, full-robot in-air trajectories and on-ground locomotion. The framework is tested on three primary platforms and deployed on ten additional robots, demonstrating reliable policy transfer without randomization of dynamic parameters. Our method improves energetic efficiency over state-of-the-art methods, achieving a 32 percent reduction in the full Cost of Transport of ANYmal (value 1.27). All code, models, and datasets will be released.

## 개요  
다리 로봇이 실제 환경에서 실용적으로 사용되기 위해서는 강건한 보행과 에너지 효율성을 동시에 달성해야 합니다. 그러나 시뮬레이션에서 훈련된 제어기는 종종 신뢰성 있게 전이되지 못하며, 대부분의 기존 접근법은 액추에이터 특정 에너지 손실을 무시하거나 복잡하고 수동으로 조정된 보상 함수에 의존합니다. 본 논문에서는 시뮬레이션-실제 강화 학습과 영구자석 동기 모터에 대한 물리 기반 에너지 모델을 통합하는 프레임워크를 제안합니다. 이 프레임워크는 시뮬레이션-실제 간극을 포착하기 위해 최소한의 매개변수 집합을 필요로 하며, 전기적 및 기계적 소산을 균형 있게 조정하는 제1원리 기반 에너지 손실 공식을 포함한 간결한 4항 보상을 사용합니다. 우리는 액추에이터, 전체 로봇의 공중 궤적 및 지상 보행을 포괄하는 하향식 동적 매개변수 식별 연구를 통해 접근법을 평가하고 검증합니다. 이 프레임워크는 세 가지 주요 플랫폼에서 테스트되고 추가로 10대의 로봇에 배포되어, 동적 매개변수의 무작위화 없이 신뢰성 있는 정책 전이를 입증합니다. 우리의 방법은 최첨단 방법보다 에너지 효율성을 개선하여 ANYmal의 전체 운송 비용을 32% 감소시킵니다(값 1.27). 모든 코드, 모델 및 데이터셋은 공개될 예정입니다.

## 핵심 내용  
다리 로봇이 실제 환경에서 실용적으로 사용되기 위해서는 강건한 보행과 에너지 효율성을 동시에 달성해야 합니다. 그러나 시뮬레이션에서 훈련된 제어기는 종종 신뢰성 있게 전이되지 못하며, 대부분의 기존 접근법은 액추에이터 특정 에너지 손실을 무시하거나 복잡하고 수동으로 조정된 보상 함수에 의존합니다. 본 논문에서는 시뮬레이션-실제 강화 학습과 영구자석 동기 모터에 대한 물리 기반 에너지 모델을 통합하는 프레임워크를 제안합니다. 이 프레임워크는 시뮬레이션-실제 간극을 포착하기 위해 최소한의 매개변수 집합을 필요로 하며, 전기적 및 기계적 소산을 균형 있게 조정하는 제1원리 기반 에너지 손실 공식을 포함한 간결한 4항 보상을 사용합니다. 우리는 액추에이터, 전체 로봇의 공중 궤적 및 지상 보행을 포괄하는 하향식 동적 매개변수 식별 연구를 통해 접근법을 평가하고 검증합니다. 이 프레임워크는 세 가지 주요 플랫폼에서 테스트되고 추가로 10대의 로봇에 배포되어, 동적 매개변수의 무작위화 없이 신뢰성 있는 정책 전이를 입증합니다. 우리의 방법은 최첨단 방법보다 에너지 효율성을 개선하여 ANYmal의 전체 운송 비용을 32% 감소시킵니다(값 1.27). 모든 코드, 모델 및 데이터셋은 공개될 예정입니다.
