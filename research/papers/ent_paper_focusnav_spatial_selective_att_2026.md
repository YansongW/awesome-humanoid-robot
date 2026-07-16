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
  zh: 'FocusNav: Spatial Selective Attention with Waypoint Guidance for Humanoid Local Navigation is a 2026 work on navigation
    for humanoid robots.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.12790v1.
sources:
- id: src_001
  type: paper
  title: 'FocusNav: Spatial Selective Attention with Waypoint Guidance for Humanoid Local Navigation (arXiv)'
  url: https://arxiv.org/abs/2601.12790
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Robust local navigation in unstructured and dynamic environments remains a significant challenge for humanoid robots, requiring a delicate balance between long-range navigation targets and immediate motion stability. In this paper, we propose FocusNav, a spatial selective attention framework that adaptively modulates the robot's perceptual field based on navigational intent and real-time stability. FocusNav features a Waypoint-Guided Spatial Cross-Attention (WGSCA) mechanism that anchors environmental feature aggregation to a sequence of predicted collision-free waypoints, ensuring task-relevant perception along the planned trajectory. To enhance robustness in complex terrains, the Stability-Aware Selective Gating (SASG) module autonomously truncates distal information when detecting instability, compelling the policy to prioritize immediate foothold safety. Extensive experiments on the Unitree G1 humanoid robot demonstrate that FocusNav significantly improves navigation success rates in challenging scenarios, outperforming baselines in both collision avoidance and motion stability, achieving robust navigation in dynamic and complex environments.

## 核心内容
Robust local navigation in unstructured and dynamic environments remains a significant challenge for humanoid robots, requiring a delicate balance between long-range navigation targets and immediate motion stability. In this paper, we propose FocusNav, a spatial selective attention framework that adaptively modulates the robot's perceptual field based on navigational intent and real-time stability. FocusNav features a Waypoint-Guided Spatial Cross-Attention (WGSCA) mechanism that anchors environmental feature aggregation to a sequence of predicted collision-free waypoints, ensuring task-relevant perception along the planned trajectory. To enhance robustness in complex terrains, the Stability-Aware Selective Gating (SASG) module autonomously truncates distal information when detecting instability, compelling the policy to prioritize immediate foothold safety. Extensive experiments on the Unitree G1 humanoid robot demonstrate that FocusNav significantly improves navigation success rates in challenging scenarios, outperforming baselines in both collision avoidance and motion stability, achieving robust navigation in dynamic and complex environments.

## 参考
- http://arxiv.org/abs/2601.12790v1

## Overview
Robust local navigation in unstructured and dynamic environments remains a significant challenge for humanoid robots, requiring a delicate balance between long-range navigation targets and immediate motion stability. In this paper, we propose FocusNav, a spatial selective attention framework that adaptively modulates the robot's perceptual field based on navigational intent and real-time stability. FocusNav features a Waypoint-Guided Spatial Cross-Attention (WGSCA) mechanism that anchors environmental feature aggregation to a sequence of predicted collision-free waypoints, ensuring task-relevant perception along the planned trajectory. To enhance robustness in complex terrains, the Stability-Aware Selective Gating (SASG) module autonomously truncates distal information when detecting instability, compelling the policy to prioritize immediate foothold safety. Extensive experiments on the Unitree G1 humanoid robot demonstrate that FocusNav significantly improves navigation success rates in challenging scenarios, outperforming baselines in both collision avoidance and motion stability, achieving robust navigation in dynamic and complex environments.

## Content
Robust local navigation in unstructured and dynamic environments remains a significant challenge for humanoid robots, requiring a delicate balance between long-range navigation targets and immediate motion stability. In this paper, we propose FocusNav, a spatial selective attention framework that adaptively modulates the robot's perceptual field based on navigational intent and real-time stability. FocusNav features a Waypoint-Guided Spatial Cross-Attention (WGSCA) mechanism that anchors environmental feature aggregation to a sequence of predicted collision-free waypoints, ensuring task-relevant perception along the planned trajectory. To enhance robustness in complex terrains, the Stability-Aware Selective Gating (SASG) module autonomously truncates distal information when detecting instability, compelling the policy to prioritize immediate foothold safety. Extensive experiments on the Unitree G1 humanoid robot demonstrate that FocusNav significantly improves navigation success rates in challenging scenarios, outperforming baselines in both collision avoidance and motion stability, achieving robust navigation in dynamic and complex environments.

## 개요
비정형적이고 동적인 환경에서의 강건한 로컬 내비게이션은 인간형 로봇에게 여전히 중요한 도전 과제로, 장거리 내비게이션 목표와 즉각적인 운동 안정성 사이의 섬세한 균형이 요구됩니다. 본 논문에서는 내비게이션 의도와 실시간 안정성에 기반하여 로봇의 지각 영역을 적응적으로 조절하는 공간 선택적 주의 메커니즘인 FocusNav를 제안합니다. FocusNav는 Waypoint-Guided Spatial Cross-Attention (WGSCA) 메커니즘을 특징으로 하며, 예측된 충돌 없는 웨이포인트 시퀀스에 환경 특징 집계를 고정시켜 계획된 궤적을 따라 작업 관련 지각을 보장합니다. 복잡한 지형에서의 강건성을 향상시키기 위해 Stability-Aware Selective Gating (SASG) 모듈은 불안정성이 감지될 때 원거리 정보를 자율적으로 차단하여 정책이 즉각적인 발판 안전을 우선시하도록 강제합니다. Unitree G1 인간형 로봇을 대상으로 한 광범위한 실험을 통해 FocusNav가 도전적인 시나리오에서 내비게이션 성공률을 크게 향상시키며, 충돌 회피와 운동 안정성 모두에서 기준선을 능가하여 동적이고 복잡한 환경에서 강건한 내비게이션을 달성함을 입증했습니다.

## 핵심 내용
비정형적이고 동적인 환경에서의 강건한 로컬 내비게이션은 인간형 로봇에게 여전히 중요한 도전 과제로, 장거리 내비게이션 목표와 즉각적인 운동 안정성 사이의 섬세한 균형이 요구됩니다. 본 논문에서는 내비게이션 의도와 실시간 안정성에 기반하여 로봇의 지각 영역을 적응적으로 조절하는 공간 선택적 주의 메커니즘인 FocusNav를 제안합니다. FocusNav는 Waypoint-Guided Spatial Cross-Attention (WGSCA) 메커니즘을 특징으로 하며, 예측된 충돌 없는 웨이포인트 시퀀스에 환경 특징 집계를 고정시켜 계획된 궤적을 따라 작업 관련 지각을 보장합니다. 복잡한 지형에서의 강건성을 향상시키기 위해 Stability-Aware Selective Gating (SASG) 모듈은 불안정성이 감지될 때 원거리 정보를 자율적으로 차단하여 정책이 즉각적인 발판 안전을 우선시하도록 강제합니다. Unitree G1 인간형 로봇을 대상으로 한 광범위한 실험을 통해 FocusNav가 도전적인 시나리오에서 내비게이션 성공률을 크게 향상시키며, 충돌 회피와 운동 안정성 모두에서 기준선을 능가하여 동적이고 복잡한 환경에서 강건한 내비게이션을 달성함을 입증했습니다.
