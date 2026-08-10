---
$id: ent_paper_focusnav_spatial_selective_att_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FocusNav: Spatial Selective Attention with Waypoint Guidance for Humanoid Local Navigation'
  zh: 'FocusNav: Spatial Selective Attention with Waypoint Guidance for Humanoid Local Navigation'
  ko: 'FocusNav: Spatial Selective Attention with Waypoint Guidance for Humanoid Local Navigation'
summary:
  en: 'FocusNav: Spatial Selective Attention with Waypoint Guidance for Humanoid Local Navigation is a 2026 work on navigation
    for humanoid robots.'
  zh: FocusNav 是 2026 年提出的一种用于人形机器人局部导航的空间选择性注意力框架。它通过 Waypoint-Guided Spatial Cross-Attention (WGSCA) 机制和 Stability-Aware
    Selective Gating (SASG) 模块，在复杂动态环境中平衡长程导航目标与即时运动稳定性。在 Unitree G1 人形机器人上的实验表明，该方法在避障和运动稳定性方面显著优于基线。
  ko: 'FocusNav: Spatial Selective Attention with Waypoint Guidance for Humanoid Local Navigation is a 2026 work on navigation
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- focusnav
- humanoid
- navigation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.12790v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1028 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'FocusNav: Spatial Selective Attention with Waypoint Guidance for Humanoid Local Navigation (arXiv)'
  url: https://arxiv.org/abs/2601.12790
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
FocusNav 的核心创新在于其空间选择性注意力机制，该机制根据导航意图和实时稳定性自适应地调整机器人的感知范围。具体而言，Waypoint-Guided Spatial Cross-Attention (WGSCA) 将环境特征聚合锚定到一系列预测的无碰撞航点上，确保沿规划轨迹的任务相关感知。同时，Stability-Aware Selective Gating (SASG) 模块在检测到不稳定时自动截断远端信息，迫使策略优先考虑即时立足点安全。在 Unitree G1 人形机器人上的大量实验验证了 FocusNav 在挑战性场景中的有效性，其导航成功率、避障能力和运动稳定性均优于现有基线方法。

## 核心内容
### 方法架构
FocusNav 框架包含两个核心模块：
- **Waypoint-Guided Spatial Cross-Attention (WGSCA)**：该机制将环境特征聚合过程与一系列预测的无碰撞航点对齐。通过交叉注意力操作，模型能够聚焦于沿规划轨迹的关键环境信息，确保感知与导航意图的一致性。
- **Stability-Aware Selective Gating (SASG)**：该模块实时监测机器人的运动稳定性。当检测到不稳定状态（如倾斜或震动）时，SASG 会自动截断对远端环境信息的处理，使策略优先关注即时立足点的安全性，从而增强在复杂地形中的鲁棒性。

### 实验设置
- **平台**：Unitree G1 人形机器人。
- **场景**：非结构化和动态环境，包含障碍物、地形变化和移动干扰。
- **基线**：与现有局部导航方法进行对比，评估指标包括导航成功率、碰撞率和运动稳定性。

### 关键结果
- FocusNav 在挑战性场景中显著提升了导航成功率，尤其在动态障碍物密集和地形崎岖的环境中表现突出。
- 与基线相比，FocusNav 在碰撞避免方面实现了更低的碰撞率，同时保持了更高的运动稳定性（如更小的身体倾斜幅度和更少的步态调整）。
- 消融实验证实，WGSCA 和 SASG 模块各自对性能提升有贡献，且两者结合效果最佳。

### 结论
FocusNav 通过空间选择性注意力机制有效解决了人形机器人在非结构化和动态环境中的局部导航难题。其航点引导和稳定性感知设计为平衡长程目标与即时安全提供了可行方案，在 Unitree G1 上的实验验证了其实际部署潜力。

## Overview
Robust local navigation in unstructured and dynamic environments remains a significant challenge for humanoid robots, requiring a delicate balance between long-range navigation targets and immediate motion stability. In this paper, we propose FocusNav, a spatial selective attention framework that adaptively modulates the robot's perceptual field based on navigational intent and real-time stability. FocusNav features a Waypoint-Guided Spatial Cross-Attention (WGSCA) mechanism that anchors environmental feature aggregation to a sequence of predicted collision-free waypoints, ensuring task-relevant perception along the planned trajectory. To enhance robustness in complex terrains, the Stability-Aware Selective Gating (SASG) module autonomously truncates distal information when detecting instability, compelling the policy to prioritize immediate foothold safety. Extensive experiments on the Unitree G1 humanoid robot demonstrate that FocusNav significantly improves navigation success rates in challenging scenarios, outperforming baselines in both collision avoidance and motion stability, achieving robust navigation in dynamic and complex environments.

## 参考
- http://arxiv.org/abs/2601.12790v1

## 개요
FocusNav의 핵심 혁신은 공간 선택적 주의 메커니즘으로, 이 메커니즘은 내비게이션 의도와 실시간 안정성에 따라 로봇의 인식 범위를 적응적으로 조정합니다. 구체적으로, Waypoint-Guided Spatial Cross-Attention (WGSCA)은 환경 특징 집계를 일련의 예측된 충돌 없는 웨이포인트에 고정시켜 계획된 궤적을 따라 작업 관련 인식을 보장합니다. 동시에, Stability-Aware Selective Gating (SASG) 모듈은 불안정이 감지되면 원거리 정보를 자동으로 차단하여 정책이 즉각적인 발판 안전을 우선시하도록 강제합니다. Unitree G1 휴머노이드 로봇에서의 광범위한 실험은 도전적인 시나리오에서 FocusNav의 효과를 검증했으며, 내비게이션 성공률, 장애물 회피 능력 및 운동 안정성에서 기존 기준 방법보다 우수함을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
FocusNav 프레임워크는 두 가지 핵심 모듈을 포함합니다:
- **Waypoint-Guided Spatial Cross-Attention (WGSCA)**: 이 메커니즘은 환경 특징 집계 과정을 일련의 예측된 충돌 없는 웨이포인트와 정렬합니다. 교차 주의 연산을 통해 모델은 계획된 궤적을 따라 핵심 환경 정보에 집중할 수 있어 인식과 내비게이션 의도의 일관성을 보장합니다.
- **Stability-Aware Selective Gating (SASG)**: 이 모듈은 로봇의 운동 안정성을 실시간으로 모니터링합니다. 불안정 상태(예: 기울어짐 또는 진동)가 감지되면 SASG는 원거리 환경 정보 처리를 자동으로 차단하여 정책이 즉각적인 발판 안전에 우선적으로 집중하도록 하여 복잡한 지형에서의 견고성을 강화합니다.

### 실험 설정
- **플랫폼**: Unitree G1 휴머노이드 로봇.
- **시나리오**: 장애물, 지형 변화 및 이동 간섭을 포함한 비구조적 및 동적 환경.
- **기준**: 기존 로컬 내비게이션 방법과 비교했으며, 평가 지표는 내비게이션 성공률, 충돌률 및 운동 안정성을 포함합니다.

### 주요 결과
- FocusNav는 도전적인 시나리오에서 내비게이션 성공률을 크게 향상시켰으며, 특히 동적 장애물이 밀집되고 지형이 험준한 환경에서 두드러진 성과를 보였습니다.
- 기준과 비교하여 FocusNav는 충돌 회피에서 더 낮은 충돌률을 달성하면서도 더 높은 운동 안정성(예: 더 작은 몸 기울기 진폭 및 더 적은 보행 조정)을 유지했습니다.
- 절제 실험은 WGSCA와 SASG 모듈이 각각 성능 향상에 기여하며, 두 모듈을 결합했을 때 최상의 효과를 나타냄을 확인했습니다.

### 결론
FocusNav는 공간 선택적 주의 메커니즘을 통해 비구조적 및 동적 환경에서 휴머노이드 로봇의 로컬 내비게이션 문제를 효과적으로 해결합니다. 웨이포인트 안내 및 안정성 인식 설계는 장거리 목표와 즉각적인 안전 사이의 균형을 위한 실현 가능한 솔루션을 제공하며, Unitree G1에서의 실험은 실제 배포 가능성을 검증했습니다.
