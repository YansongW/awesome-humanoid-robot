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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.12790v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
비정형적이고 동적인 환경에서의 강건한 로컬 내비게이션은 인간형 로봇에게 여전히 중요한 도전 과제로, 장거리 내비게이션 목표와 즉각적인 운동 안정성 사이의 섬세한 균형이 요구됩니다. 본 논문에서는 내비게이션 의도와 실시간 안정성에 기반하여 로봇의 지각 영역을 적응적으로 조절하는 공간 선택적 주의 메커니즘인 FocusNav를 제안합니다. FocusNav는 Waypoint-Guided Spatial Cross-Attention (WGSCA) 메커니즘을 특징으로 하며, 예측된 충돌 없는 웨이포인트 시퀀스에 환경 특징 집계를 고정시켜 계획된 궤적을 따라 작업 관련 지각을 보장합니다. 복잡한 지형에서의 강건성을 향상시키기 위해 Stability-Aware Selective Gating (SASG) 모듈은 불안정성이 감지될 때 원거리 정보를 자율적으로 차단하여 정책이 즉각적인 발판 안전을 우선시하도록 강제합니다. Unitree G1 인간형 로봇을 대상으로 한 광범위한 실험을 통해 FocusNav가 도전적인 시나리오에서 내비게이션 성공률을 크게 향상시키며, 충돌 회피와 운동 안정성 모두에서 기준선을 능가하여 동적이고 복잡한 환경에서 강건한 내비게이션을 달성함을 입증했습니다.

## 핵심 내용
비정형적이고 동적인 환경에서의 강건한 로컬 내비게이션은 인간형 로봇에게 여전히 중요한 도전 과제로, 장거리 내비게이션 목표와 즉각적인 운동 안정성 사이의 섬세한 균형이 요구됩니다. 본 논문에서는 내비게이션 의도와 실시간 안정성에 기반하여 로봇의 지각 영역을 적응적으로 조절하는 공간 선택적 주의 메커니즘인 FocusNav를 제안합니다. FocusNav는 Waypoint-Guided Spatial Cross-Attention (WGSCA) 메커니즘을 특징으로 하며, 예측된 충돌 없는 웨이포인트 시퀀스에 환경 특징 집계를 고정시켜 계획된 궤적을 따라 작업 관련 지각을 보장합니다. 복잡한 지형에서의 강건성을 향상시키기 위해 Stability-Aware Selective Gating (SASG) 모듈은 불안정성이 감지될 때 원거리 정보를 자율적으로 차단하여 정책이 즉각적인 발판 안전을 우선시하도록 강제합니다. Unitree G1 인간형 로봇을 대상으로 한 광범위한 실험을 통해 FocusNav가 도전적인 시나리오에서 내비게이션 성공률을 크게 향상시키며, 충돌 회피와 운동 안정성 모두에서 기준선을 능가하여 동적이고 복잡한 환경에서 강건한 내비게이션을 달성함을 입증했습니다.

## 参考
- http://arxiv.org/abs/2601.12790v1
