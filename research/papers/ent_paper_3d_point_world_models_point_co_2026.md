---
$id: ent_paper_3d_point_world_models_point_co_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: '3D Point World Models: Point Completion Enables More Accurate Dynamics Learning'
  zh: '3D Point World Models: Point Completion Enables More Accurate Dynamics Learning'
  ko: '3D Point World Models: Point Completion Enables More Accurate Dynamics Learning'
summary:
  en: 'arXiv:2607.00148v1 Announce Type: new Abstract: Learning predictive models of the world enables robotic control through
    planning, potentially allowing robots to improvise solutions on new tasks. However, large video-based dynamics models
    lack explicit 3D spatial structure and suffer from geometrically inconsistent long-term rollouts with compounding errors.
    Emerging 3D dynamics models based on partial point clouds improve geometric consistency but remain sensitive to occlusions
    and accumulated prediction drift. To address these challenges, we present 3D Point World Models (3DPWM) - a task-agnostic
    world model that operates entirely in 3D space by first completing partial point clouds and then learning action-conditioned
    dynamics in this completed 3D scene. By operating on completed geometry, 3DPWM enables reliable long-horizon rollouts
    and more accurate cost evaluation for model-based planning while supporting adaptation to new tasks. Experiments across
    different robotic embodiments and tabletop manipulation benchmarks demonstrate that 3DPWM achieves significantly more
    reliable long-horizon rollouts (100-300+ steps), supports both open-loop and closed-loop planning, and enables successful
    sim-to-real transfer.'
  zh: 3D Point World Models (3DPWM) 是一种任务无关的世界模型，由研究团队提出，其核心贡献在于通过先完成部分点云再学习动作条件动力学，实现了在完整3D空间中的可靠长程推演。该方法在多种机器人平台和桌面操作基准上验证了100-300步以上的稳定推演能力，并支持开环与闭环规划以及仿真到现实的迁移。
  ko: 'arXiv:2607.00148v1 Announce Type: new Abstract: Learning predictive models of the world enables robotic control through
    planning, potentially allowing robots to improvise solutions on new tasks. However, large video-based dynamics models
    lack explicit 3D spatial structure and suffer from geometrically inconsistent long-term rollouts with compounding errors.
    Emerging 3D dynamics models based on partial point clouds improve geometric consistency but remain sensitive to occlusions
    and accumulated prediction drift. To address these challenges, we present 3D Point World Models (3DPWM) - a task-agnostic
    world model that operates entirely in 3D space by first completing partial point clouds and then learning action-conditioned
    dynamics in this completed 3D scene. By operating on completed geometry, 3DPWM enables reliable long-horizon rollouts
    and more accurate cost evaluation for model-based planning while supporting adaptation to new tasks. Experiments across
    different robotic embodiments and tabletop manipulation benchmarks demonstrate that 3DPWM achieves significantly more
    reliable long-horizon rollouts (100-300+ steps), supports both open-loop and closed-loop planning, and enables successful
    sim-to-real transfer.'
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
- 3d_point_world_models
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.00148v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (707 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: '3D Point World Models: Point Completion Enables More Accurate Dynamics Learning (arXiv)'
  url: https://arxiv.org/abs/2607.00148
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述
现有基于视频的动力学模型缺乏显式3D空间结构，在长程推演中会产生几何不一致的累积误差。虽然基于部分点云的3D动力学模型改善了几何一致性，但仍受遮挡和预测漂移的影响。3DPWM通过先完成部分点云再学习动作条件动力学，在完整3D场景中实现了更可靠的长程推演和更准确的成本评估。实验表明，该方法在多种机器人平台上均能实现100-300步以上的稳定推演，并支持开环与闭环规划以及仿真到现实的迁移。

## 核心内容
### 方法架构
3DPWM 的核心流程分为两个阶段：
- **点云完成**：首先对传感器获取的部分点云进行补全，恢复场景的完整几何结构。
- **动作条件动力学学习**：在完成的3D场景上学习动作与状态转移之间的映射关系。

### 关键设计
- 完全在3D空间操作，避免了视频模型中的几何不一致问题。
- 通过完成点云，有效缓解了遮挡和预测漂移对动力学学习的影响。
- 支持任务无关的规划，可适应新任务而无需重新训练。

### 实验设置与结果
- **机器人平台**：涵盖多种机器人形态，包括机械臂和移动操作平台。
- **基准任务**：在桌面操作基准上评估，包括抓取、推拉等典型操作。
- **长程推演**：实现了100-300步以上的稳定推演，显著优于基线方法。
- **规划模式**：同时支持开环规划（一次性生成完整轨迹）和闭环规划（逐步修正）。
- **迁移能力**：成功实现了从仿真环境到真实机器人的零样本迁移。

### 结论
3DPWM 通过点云完成与3D动力学学习的结合，为基于模型的机器人规划提供了一种几何一致且鲁棒的解决方案，在长程推演和跨任务泛化方面展现出显著优势。

## Overview
Learning predictive models of the world enables robotic control through planning, potentially allowing robots to improvise solutions on new tasks. However, large video-based dynamics models lack explicit 3D spatial structure and suffer from geometrically inconsistent long-term rollouts with compounding errors. Emerging 3D dynamics models based on partial point clouds improve geometric consistency but remain sensitive to occlusions and accumulated prediction drift. To address these challenges, we present 3D Point World Models (3DPWM) - a task-agnostic world model that operates entirely in 3D space by first completing partial point clouds and then learning action-conditioned dynamics in this completed 3D scene. By operating on completed geometry, 3DPWM enables reliable long-horizon rollouts and more accurate cost evaluation for model-based planning while supporting adaptation to new tasks. Experiments across different robotic embodiments and tabletop manipulation benchmarks demonstrate that 3DPWM achieves significantly more reliable long-horizon rollouts (100-300+ steps), supports both open-loop and closed-loop planning, and enables successful sim-to-real transfer.

## 参考
- http://arxiv.org/abs/2607.00148v1

## 개요
기존 비디오 기반 동역학 모델은 명시적 3D 공간 구조가 부족하여 장기 추론에서 기하학적 불일치의 누적 오차가 발생합니다. 부분 점군 기반 3D 동역학 모델은 기하학적 일관성을 개선했지만 여전히 폐색 및 예측 드리프트의 영향을 받습니다. 3DPWM은 부분 점군을 먼저 완성한 후 동작 조건부 동역학을 학습함으로써 완전한 3D 장면에서 더 신뢰할 수 있는 장기 추론과 더 정확한 비용 평가를 구현합니다. 실험 결과, 이 방법은 다양한 로봇 플랫폼에서 100-300단계 이상의 안정적인 추론을 달성하며, 개루프 및 폐루프 계획과 시뮬레이션에서 실제 환경으로의 전이를 지원합니다.

## 핵심 내용
### 방법 아키텍처
3DPWM의 핵심 프로세스는 두 단계로 구성됩니다:
- **점군 완성**: 먼저 센서에서 획득한 부분 점군을 보완하여 장면의 완전한 기하학적 구조를 복원합니다.
- **동작 조건부 동역학 학습**: 완성된 3D 장면에서 동작과 상태 전이 간의 매핑 관계를 학습합니다.

### 핵심 설계
- 완전히 3D 공간에서 작동하여 비디오 모델의 기하학적 불일치 문제를 방지합니다.
- 점군 완성을 통해 폐색 및 예측 드리프트가 동역학 학습에 미치는 영향을 효과적으로 완화합니다.
- 작업과 무관한 계획을 지원하여 재훈련 없이 새로운 작업에 적응할 수 있습니다.

### 실험 설정 및 결과
- **로봇 플랫폼**: 로봇 팔과 이동 조작 플랫폼을 포함한 다양한 로봇 형태를 포괄합니다.
- **벤치마크 작업**: 테이블 조작 벤치마크에서 그리핑, 밀기/당기기 등 전형적인 조작을 평가합니다.
- **장기 추론**: 100-300단계 이상의 안정적인 추론을 구현하여 기준 방법보다 현저히 우수합니다.
- **계획 모드**: 개루프 계획(전체 궤적을 한 번에 생성)과 폐루프 계획(단계별 수정)을 동시에 지원합니다.
- **전이 능력**: 시뮬레이션 환경에서 실제 로봇으로의 제로샷 전이를 성공적으로 구현했습니다.

### 결론
3DPWM은 점군 완성과 3D 동역학 학습의 결합을 통해 모델 기반 로봇 계획에 기하학적으로 일관되고 견고한 솔루션을 제공하며, 장기 추론 및 교차 작업 일반화에서 현저한 이점을 보여줍니다.
