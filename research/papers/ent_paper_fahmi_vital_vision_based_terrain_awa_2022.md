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
  zh: ViTAL 提出了一种基于视觉的在线运动规划策略，通过共享地形感知技能联合规划四足机器人的身体姿态与落脚点。该方法在 HyQ 和 HyQReal 机器人上验证，能攀爬楼梯、跨越间隙及粗糙地形，性能优于传统基线方法。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2212.01246v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (703 chars, DeepSeek).'
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
现有方法将运动规划分为落脚点选择与姿态适应两步，但若落脚点不可达，机器人可能陷入无安全支撑的状态。ViTAL 创新性地将姿态适应从“优化给定落脚点下的身体位姿”转变为“最大化腿部到达安全落脚点概率的身体位姿”。该方法基于机器人能力与地形感知技能联合规划落脚点与姿态，在 90 kg 的 HyQ 和 140 kg 的 HyQReal 四足机器人上验证，成功实现不同速度与步态下的楼梯、间隙及粗糙地形攀爬。

## 核心内容
### 方法架构
ViTAL 的核心是**联合规划**身体姿态与落脚点，而非传统顺序规划。其关键创新在于：
- **姿态适应新范式**：不优化给定落脚点下的身体位姿，而是寻找能最大化腿部到达安全落脚点概率的身体位姿。
- **技能驱动规划**：基于表征机器人能力与地形感知的“技能”（skills）进行规划，确保规划结果符合机器人运动学与动力学约束。

### 实验设置
- **机器人平台**：90 kg 的 HyQ 与 140 kg 的 HyQReal 四足机器人。
- **测试地形**：楼梯、间隙（gaps）、粗糙地形（rough terrains）。
- **对比基线**：传统方法——先选择落脚点，再基于这些落脚点优化身体姿态。

### 关键结果
- ViTAL 在多种地形上均能成功攀爬，而基线方法在复杂地形（如大间隙或高台阶）中因落脚点不可达导致失败。
- 不同速度与步态下，ViTAL 均保持稳定，验证了其鲁棒性。

### 结论
ViTAL 通过将姿态适应与落脚点选择联合优化，并引入地形感知技能，显著提升了四足机器人在复杂非结构化地形上的通过能力。

## Overview
This work is on vision-based planning strategies for legged robots that separate locomotion planning into foothold selection and pose adaptation. Current pose adaptation strategies optimize the robot's body pose relative to given footholds. If these footholds are not reached, the robot may end up in a state with no reachable safe footholds. Therefore, we present a Vision-Based Terrain-Aware Locomotion (ViTAL) strategy that consists of novel pose adaptation and foothold selection algorithms. ViTAL introduces a different paradigm in pose adaptation that does not optimize the body pose relative to given footholds, but the body pose that maximizes the chances of the legs in reaching safe footholds. ViTAL plans footholds and poses based on skills that characterize the robot's capabilities and its terrain-awareness. We use the 90 kg HyQ and 140 kg HyQReal quadruped robots to validate ViTAL, and show that they are able to climb various obstacles including stairs, gaps, and rough terrains at different speeds and gaits. We compare ViTAL with a baseline strategy that selects the robot pose based on given selected footholds, and show that ViTAL outperforms the baseline.

## 参考
- http://arxiv.org/abs/2212.01246v1

## 개요
기존 방법은 운동 계획을 착지점 선택과 자세 적응의 두 단계로 나누지만, 착지점에 도달할 수 없는 경우 로봇이 안전한 지지 상태를 확보하지 못할 수 있다. ViTAL은 자세 적응을 "주어진 착지점에서의 신체 자세 최적화"에서 "다리가 안전한 착지점에 도달할 확률을 최대화하는 신체 자세"로 혁신적으로 전환한다. 이 방법은 로봇의 능력과 지형 인식 기술을 기반으로 착지점과 자세를 공동 계획하며, 90kg의 HyQ와 140kg의 HyQReal 네 발 달린 로봇에서 검증되어 다양한 속도와 보행에서 계단, 틈, 거친 지형 등반에 성공했다.

## 핵심 내용
### 방법 구조
ViTAL의 핵심은 전통적인 순차 계획이 아닌 신체 자세와 착지점의 **공동 계획**이다. 주요 혁신은 다음과 같다:
- **자세 적응의 새로운 패러다임**: 주어진 착지점에서의 신체 자세를 최적화하지 않고, 다리가 안전한 착지점에 도달할 확률을 최대화하는 신체 자세를 찾는다.
- **기술 기반 계획**: 로봇의 능력과 지형 인식을 나타내는 "기술"(skills)을 기반으로 계획하여, 계획 결과가 로봇의 운동학 및 동역학 제약을 준수하도록 보장한다.

### 실험 설정
- **로봇 플랫폼**: 90kg의 HyQ와 140kg의 HyQReal 네 발 달린 로봇.
- **테스트 지형**: 계단, 틈(gaps), 거친 지형(rough terrains).
- **비교 기준선**: 전통적인 방법—먼저 착지점을 선택한 후, 해당 착지점을 기반으로 신체 자세를 최적화.

### 주요 결과
- ViTAL은 다양한 지형에서 성공적으로 등반했지만, 기준선 방법은 복잡한 지형(예: 큰 틈이나 높은 계단)에서 착지점에 도달할 수 없어 실패했다.
- 다양한 속도와 보행에서 ViTAL은 안정성을 유지하여 견고성을 검증했다.

### 결론
ViTAL은 자세 적응과 착지점 선택을 공동 최적화하고 지형 인식 기술을 도입함으로써, 네 발 달린 로봇의 복잡한 비구조적 지형 통과 능력을 크게 향상시켰다.
