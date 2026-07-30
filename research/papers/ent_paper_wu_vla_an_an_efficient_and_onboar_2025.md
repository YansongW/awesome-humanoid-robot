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
  zh: VLA-AN 是浙江大学与 Differential Robotics 于 2025 年提出的高效机载视觉-语言-动作框架，专为复杂环境下的自主无人机导航设计。其核心贡献包括：利用 3D Gaussian Splatting 构建高保真数据集以弥合域差距，设计渐进式三阶段训练框架，以及轻量级实时动作模块配合几何安全校正，最终在资源受限的无人机上实现推理吞吐量
    8.3 倍提升，单任务成功率最高达 98.1%。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.15258v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
VLA-AN 针对现有大型空中导航模型在数据域差距、时序导航推理不足、生成式动作策略的安全隐患以及机载部署限制等四大问题，提出了一套完整的解决方案。该框架首先通过 3D Gaussian Splatting 技术构建高保真数据集，有效弥合了仿真与真实环境间的域差距。其次，采用渐进式三阶段训练流程，依次强化场景理解、核心飞行技能与复杂导航能力。最后，设计轻量级实时动作模块并耦合几何安全校正机制，确保指令生成快速、无碰撞且稳定，从而缓解随机生成策略固有的安全风险。通过深度优化机载部署管线，VLA-AN 在资源受限的无人机上实现了推理吞吐量 8.3 倍的稳健提升。

## 核心内容
### 方法架构
VLA-AN 框架包含三个核心组件：
- **高保真数据集构建**：采用 3D Gaussian Splatting (3D-GS) 技术生成逼真的场景数据，有效缩小仿真与真实环境之间的域差距。
- **渐进式三阶段训练框架**：
  1. 第一阶段：强化场景理解能力。
  2. 第二阶段：巩固核心飞行技能。
  3. 第三阶段：提升复杂导航能力。
- **轻量级实时动作模块**：该模块与几何安全校正机制耦合，确保生成的动作指令快速、无碰撞且稳定，从而规避随机生成策略（如扩散模型）可能带来的安全风险。

### 实验设置与关键结果
- **部署优化**：通过深度优化机载部署管线，VLA-AN 在资源受限的无人机上实现了推理吞吐量 8.3 倍的提升。
- **性能表现**：在多项实验中，VLA-AN 显著提升了空间定位、场景推理与长程导航能力，单任务最高成功率达到 98.1%。
- **结论**：该框架为轻量级空中机器人实现全链路闭环自主提供了高效、实用的解决方案。

## Overview
This paper proposes VLA-AN, an efficient and onboard Vision-Language-Action (VLA) framework dedicated to autonomous drone navigation in complex environments. VLA-AN addresses four major limitations of existing large aerial navigation models: the data domain gap, insufficient temporal navigation with reasoning, safety issues with generative action policies, and onboard deployment constraints. First, we construct a high-fidelity dataset utilizing 3D Gaussian Splatting (3D-GS) to effectively bridge the domain gap. Second, we introduce a progressive three-stage training framework that sequentially reinforces scene comprehension, core flight skills, and complex navigation capabilities. Third, we design a lightweight, real-time action module coupled with geometric safety correction. This module ensures fast, collision-free, and stable command generation, mitigating the safety risks inherent in stochastic generative policies. Finally, through deep optimization of the onboard deployment pipeline, VLA-AN achieves a robust real-time 8.3x improvement in inference throughput on resource-constrained UAVs. Extensive experiments demonstrate that VLA-AN significantly improves spatial grounding, scene reasoning, and long-horizon navigation, achieving a maximum single-task success rate of 98.1%, and providing an efficient, practical solution for realizing full-chain closed-loop autonomy in lightweight aerial robots.

## 개요
본 논문은 복잡한 환경에서 자율 드론 항법을 위한 효율적이고 온보드 방식의 VLA-AN(Vision-Language-Action) 프레임워크를 제안합니다. VLA-AN은 기존 대규모 항공 항법 모델의 네 가지 주요 한계, 즉 데이터 도메인 격차, 추론이 부족한 시간적 항법, 생성적 행동 정책의 안전 문제, 온보드 배포 제약을 해결합니다. 첫째, 3D Gaussian Splatting(3D-GS)을 활용한 고충실도 데이터셋을 구축하여 도메인 격차를 효과적으로 줄입니다. 둘째, 장면 이해, 핵심 비행 기술, 복잡한 항법 능력을 순차적으로 강화하는 점진적 3단계 훈련 프레임워크를 도입합니다. 셋째, 기하학적 안전 보정이 결합된 경량 실시간 행동 모듈을 설계합니다. 이 모듈은 빠르고 충돌 없이 안정적인 명령 생성을 보장하여 확률적 생성 정책에 내재된 안전 위험을 완화합니다. 마지막으로, 온보드 배포 파이프라인의 심층 최적화를 통해 VLA-AN은 자원이 제한된 UAV에서 추론 처리량을 8.3배 향상시킵니다. 광범위한 실험 결과, VLA-AN은 공간 기반, 장면 추론, 장기 항법을 크게 개선하여 최대 단일 작업 성공률 98.1%를 달성하며, 경량 항공 로봇의 전체 체인 폐쇄 루프 자율성을 실현하기 위한 효율적이고 실용적인 솔루션을 제공합니다.

## 핵심 내용
본 논문은 복잡한 환경에서 자율 드론 항법을 위한 효율적이고 온보드 방식의 VLA-AN(Vision-Language-Action) 프레임워크를 제안합니다. VLA-AN은 기존 대규모 항공 항법 모델의 네 가지 주요 한계, 즉 데이터 도메인 격차, 추론이 부족한 시간적 항법, 생성적 행동 정책의 안전 문제, 온보드 배포 제약을 해결합니다. 첫째, 3D Gaussian Splatting(3D-GS)을 활용한 고충실도 데이터셋을 구축하여 도메인 격차를 효과적으로 줄입니다. 둘째, 장면 이해, 핵심 비행 기술, 복잡한 항법 능력을 순차적으로 강화하는 점진적 3단계 훈련 프레임워크를 도입합니다. 셋째, 기하학적 안전 보정이 결합된 경량 실시간 행동 모듈을 설계합니다. 이 모듈은 빠르고 충돌 없이 안정적인 명령 생성을 보장하여 확률적 생성 정책에 내재된 안전 위험을 완화합니다. 마지막으로, 온보드 배포 파이프라인의 심층 최적화를 통해 VLA-AN은 자원이 제한된 UAV에서 추론 처리량을 8.3배 향상시킵니다. 광범위한 실험 결과, VLA-AN은 공간 기반, 장면 추론, 장기 항법을 크게 개선하여 최대 단일 작업 성공률 98.1%를 달성하며, 경량 항공 로봇의 전체 체인 폐쇄 루프 자율성을 실현하기 위한 효율적이고 실용적인 솔루션을 제공합니다.

## 参考
- http://arxiv.org/abs/2512.15258v2
