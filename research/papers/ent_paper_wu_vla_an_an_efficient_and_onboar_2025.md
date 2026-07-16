---
$id: ent_paper_wu_vla_an_an_efficient_and_onboar_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLA-AN: An Efficient and Onboard Vision-Language-Action Framework for Aerial Navigation in Complex Environments'
  zh: VLA-AN
  ko: 'VLA-AN: An Efficient and Onboard Vision-Language-Action Framework for Aerial Navigation in Complex Environments'
summary:
  en: 'VLA-AN: An Efficient and Onboard Vision-Language-Action Framework for Aerial Navigation in Complex Environments (VLA-AN),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Zhejiang University, Differential
    Robotics.'
  zh: 'VLA-AN: An Efficient and Onboard Vision-Language-Action Framework for Aerial Navigation in Complex Environments (VLA-AN),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Zhejiang University, Differential
    Robotics.'
  ko: 'VLA-AN: An Efficient and Onboard Vision-Language-Action Framework for Aerial Navigation in Complex Environments (VLA-AN),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Zhejiang University, Differential
    Robotics.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
- vla_an
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.15258v2.
sources:
- id: src_001
  type: paper
  title: 'VLA-AN: An Efficient and Onboard Vision-Language-Action Framework for Aerial Navigation in Complex Environments
    (arXiv)'
  url: https://arxiv.org/abs/2512.15258
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLA-AN source
  url: https://doi.org/10.48550/arXiv.2512.15258
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
This paper proposes VLA-AN, an efficient and onboard Vision-Language-Action (VLA) framework dedicated to autonomous drone navigation in complex environments. VLA-AN addresses four major limitations of existing large aerial navigation models: the data domain gap, insufficient temporal navigation with reasoning, safety issues with generative action policies, and onboard deployment constraints. First, we construct a high-fidelity dataset utilizing 3D Gaussian Splatting (3D-GS) to effectively bridge the domain gap. Second, we introduce a progressive three-stage training framework that sequentially reinforces scene comprehension, core flight skills, and complex navigation capabilities. Third, we design a lightweight, real-time action module coupled with geometric safety correction. This module ensures fast, collision-free, and stable command generation, mitigating the safety risks inherent in stochastic generative policies. Finally, through deep optimization of the onboard deployment pipeline, VLA-AN achieves a robust real-time 8.3x improvement in inference throughput on resource-constrained UAVs. Extensive experiments demonstrate that VLA-AN significantly improves spatial grounding, scene reasoning, and long-horizon navigation, achieving a maximum single-task success rate of 98.1%, and providing an efficient, practical solution for realizing full-chain closed-loop autonomy in lightweight aerial robots.

## 核心内容
This paper proposes VLA-AN, an efficient and onboard Vision-Language-Action (VLA) framework dedicated to autonomous drone navigation in complex environments. VLA-AN addresses four major limitations of existing large aerial navigation models: the data domain gap, insufficient temporal navigation with reasoning, safety issues with generative action policies, and onboard deployment constraints. First, we construct a high-fidelity dataset utilizing 3D Gaussian Splatting (3D-GS) to effectively bridge the domain gap. Second, we introduce a progressive three-stage training framework that sequentially reinforces scene comprehension, core flight skills, and complex navigation capabilities. Third, we design a lightweight, real-time action module coupled with geometric safety correction. This module ensures fast, collision-free, and stable command generation, mitigating the safety risks inherent in stochastic generative policies. Finally, through deep optimization of the onboard deployment pipeline, VLA-AN achieves a robust real-time 8.3x improvement in inference throughput on resource-constrained UAVs. Extensive experiments demonstrate that VLA-AN significantly improves spatial grounding, scene reasoning, and long-horizon navigation, achieving a maximum single-task success rate of 98.1%, and providing an efficient, practical solution for realizing full-chain closed-loop autonomy in lightweight aerial robots.

## 参考
- http://arxiv.org/abs/2512.15258v2

## Overview
This paper proposes VLA-AN, an efficient and onboard Vision-Language-Action (VLA) framework dedicated to autonomous drone navigation in complex environments. VLA-AN addresses four major limitations of existing large aerial navigation models: the data domain gap, insufficient temporal navigation with reasoning, safety issues with generative action policies, and onboard deployment constraints. First, we construct a high-fidelity dataset utilizing 3D Gaussian Splatting (3D-GS) to effectively bridge the domain gap. Second, we introduce a progressive three-stage training framework that sequentially reinforces scene comprehension, core flight skills, and complex navigation capabilities. Third, we design a lightweight, real-time action module coupled with geometric safety correction. This module ensures fast, collision-free, and stable command generation, mitigating the safety risks inherent in stochastic generative policies. Finally, through deep optimization of the onboard deployment pipeline, VLA-AN achieves a robust real-time 8.3x improvement in inference throughput on resource-constrained UAVs. Extensive experiments demonstrate that VLA-AN significantly improves spatial grounding, scene reasoning, and long-horizon navigation, achieving a maximum single-task success rate of 98.1%, and providing an efficient, practical solution for realizing full-chain closed-loop autonomy in lightweight aerial robots.

## Content
This paper proposes VLA-AN, an efficient and onboard Vision-Language-Action (VLA) framework dedicated to autonomous drone navigation in complex environments. VLA-AN addresses four major limitations of existing large aerial navigation models: the data domain gap, insufficient temporal navigation with reasoning, safety issues with generative action policies, and onboard deployment constraints. First, we construct a high-fidelity dataset utilizing 3D Gaussian Splatting (3D-GS) to effectively bridge the domain gap. Second, we introduce a progressive three-stage training framework that sequentially reinforces scene comprehension, core flight skills, and complex navigation capabilities. Third, we design a lightweight, real-time action module coupled with geometric safety correction. This module ensures fast, collision-free, and stable command generation, mitigating the safety risks inherent in stochastic generative policies. Finally, through deep optimization of the onboard deployment pipeline, VLA-AN achieves a robust real-time 8.3x improvement in inference throughput on resource-constrained UAVs. Extensive experiments demonstrate that VLA-AN significantly improves spatial grounding, scene reasoning, and long-horizon navigation, achieving a maximum single-task success rate of 98.1%, and providing an efficient, practical solution for realizing full-chain closed-loop autonomy in lightweight aerial robots.

## 개요
본 논문은 복잡한 환경에서 자율 드론 항법을 위한 효율적이고 온보드 방식의 VLA-AN(Vision-Language-Action) 프레임워크를 제안합니다. VLA-AN은 기존 대규모 항공 항법 모델의 네 가지 주요 한계, 즉 데이터 도메인 격차, 추론이 부족한 시간적 항법, 생성적 행동 정책의 안전 문제, 온보드 배포 제약을 해결합니다. 첫째, 3D Gaussian Splatting(3D-GS)을 활용한 고충실도 데이터셋을 구축하여 도메인 격차를 효과적으로 줄입니다. 둘째, 장면 이해, 핵심 비행 기술, 복잡한 항법 능력을 순차적으로 강화하는 점진적 3단계 훈련 프레임워크를 도입합니다. 셋째, 기하학적 안전 보정이 결합된 경량 실시간 행동 모듈을 설계합니다. 이 모듈은 빠르고 충돌 없이 안정적인 명령 생성을 보장하여 확률적 생성 정책에 내재된 안전 위험을 완화합니다. 마지막으로, 온보드 배포 파이프라인의 심층 최적화를 통해 VLA-AN은 자원이 제한된 UAV에서 추론 처리량을 8.3배 향상시킵니다. 광범위한 실험 결과, VLA-AN은 공간 기반, 장면 추론, 장기 항법을 크게 개선하여 최대 단일 작업 성공률 98.1%를 달성하며, 경량 항공 로봇의 전체 체인 폐쇄 루프 자율성을 실현하기 위한 효율적이고 실용적인 솔루션을 제공합니다.

## 핵심 내용
본 논문은 복잡한 환경에서 자율 드론 항법을 위한 효율적이고 온보드 방식의 VLA-AN(Vision-Language-Action) 프레임워크를 제안합니다. VLA-AN은 기존 대규모 항공 항법 모델의 네 가지 주요 한계, 즉 데이터 도메인 격차, 추론이 부족한 시간적 항법, 생성적 행동 정책의 안전 문제, 온보드 배포 제약을 해결합니다. 첫째, 3D Gaussian Splatting(3D-GS)을 활용한 고충실도 데이터셋을 구축하여 도메인 격차를 효과적으로 줄입니다. 둘째, 장면 이해, 핵심 비행 기술, 복잡한 항법 능력을 순차적으로 강화하는 점진적 3단계 훈련 프레임워크를 도입합니다. 셋째, 기하학적 안전 보정이 결합된 경량 실시간 행동 모듈을 설계합니다. 이 모듈은 빠르고 충돌 없이 안정적인 명령 생성을 보장하여 확률적 생성 정책에 내재된 안전 위험을 완화합니다. 마지막으로, 온보드 배포 파이프라인의 심층 최적화를 통해 VLA-AN은 자원이 제한된 UAV에서 추론 처리량을 8.3배 향상시킵니다. 광범위한 실험 결과, VLA-AN은 공간 기반, 장면 추론, 장기 항법을 크게 개선하여 최대 단일 작업 성공률 98.1%를 달성하며, 경량 항공 로봇의 전체 체인 폐쇄 루프 자율성을 실현하기 위한 효율적이고 실용적인 솔루션을 제공합니다.
