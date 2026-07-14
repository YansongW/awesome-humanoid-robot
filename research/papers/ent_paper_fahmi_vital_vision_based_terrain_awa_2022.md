---
$id: ent_paper_fahmi_vital_vision_based_terrain_awa_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ViTAL: Vision-Based Terrain-Aware Locomotion for Legged Robots'
  zh: ViTAL：基于视觉的地形感知腿式机器人运动方法
  ko: 'ViTAL: 시각 기반 지형 인식 다리 로봇 보행 기법'
summary:
  en: ViTAL proposes an online vision-based locomotion planning strategy that jointly plans body poses and footholds for legged
    robots using shared terrain-aware skills, validated on the HyQ and HyQReal quadruped robots.
  zh: ViTAL 提出了一种在线视觉驱动的运动规划策略，利用共享的地形感知技能同时为腿式机器人规划身体姿态和落足点，并在 HyQ 与 HyQReal 四足机器人上进行了验证。
  ko: ViTAL은 공유된 지형 인식 능력을 바탕으로 다리 로봇의 몸 자세와 발판을 동시에 온라인으로 계획하는 시각 기반 보행 계획 전략을 제안하고 HyQ 및 HyQReal 사족 로봇으로 검증하였다.
domains:
- 07_ai_models_algorithms
- 06_design_engineering
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- terrain_aware_locomotion
- vision_based_foothold_selection
- pose_adaptation
- locomotion_planning
- legged_robots
- quadruped
- humanoid_transferable
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2212.01246v1.
sources:
- id: src_001
  type: paper
  title: 'ViTAL: Vision-Based Terrain-Aware Locomotion for Legged Robots'
  url: https://arxiv.org/abs/2212.01246
  date: '2022'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
This work is on vision-based planning strategies for legged robots that separate locomotion planning into foothold selection and pose adaptation. Current pose adaptation strategies optimize the robot's body pose relative to given footholds. If these footholds are not reached, the robot may end up in a state with no reachable safe footholds. Therefore, we present a Vision-Based Terrain-Aware Locomotion (ViTAL) strategy that consists of novel pose adaptation and foothold selection algorithms. ViTAL introduces a different paradigm in pose adaptation that does not optimize the body pose relative to given footholds, but the body pose that maximizes the chances of the legs in reaching safe footholds. ViTAL plans footholds and poses based on skills that characterize the robot's capabilities and its terrain-awareness. We use the 90 kg HyQ and 140 kg HyQReal quadruped robots to validate ViTAL, and show that they are able to climb various obstacles including stairs, gaps, and rough terrains at different speeds and gaits. We compare ViTAL with a baseline strategy that selects the robot pose based on given selected footholds, and show that ViTAL outperforms the baseline.

## 核心内容
This work is on vision-based planning strategies for legged robots that separate locomotion planning into foothold selection and pose adaptation. Current pose adaptation strategies optimize the robot's body pose relative to given footholds. If these footholds are not reached, the robot may end up in a state with no reachable safe footholds. Therefore, we present a Vision-Based Terrain-Aware Locomotion (ViTAL) strategy that consists of novel pose adaptation and foothold selection algorithms. ViTAL introduces a different paradigm in pose adaptation that does not optimize the body pose relative to given footholds, but the body pose that maximizes the chances of the legs in reaching safe footholds. ViTAL plans footholds and poses based on skills that characterize the robot's capabilities and its terrain-awareness. We use the 90 kg HyQ and 140 kg HyQReal quadruped robots to validate ViTAL, and show that they are able to climb various obstacles including stairs, gaps, and rough terrains at different speeds and gaits. We compare ViTAL with a baseline strategy that selects the robot pose based on given selected footholds, and show that ViTAL outperforms the baseline.

## 参考
- http://arxiv.org/abs/2212.01246v1

