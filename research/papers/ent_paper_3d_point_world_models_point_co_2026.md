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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.00148v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
세계의 예측 모델을 학습하면 계획을 통한 로봇 제어가 가능해져, 로봇이 새로운 작업에 대한 해결책을 즉석에서 창출할 수 있습니다. 그러나 대규모 비디오 기반 동역학 모델은 명시적인 3D 공간 구조가 부족하고, 오차가 누적되어 기하학적으로 일관되지 않은 장기 롤아웃을 초래합니다. 부분 포인트 클라우드에 기반한 새로운 3D 동역학 모델은 기하학적 일관성을 개선하지만, 여전히 폐색과 누적된 예측 드리프트에 민감합니다. 이러한 문제를 해결하기 위해, 우리는 3D 포인트 월드 모델(3DPWM)을 제시합니다. 이는 작업에 구애받지 않는 세계 모델로, 먼저 부분 포인트 클라우드를 완성한 후 완성된 3D 장면에서 행동 조건 동역학을 학습함으로써 전적으로 3D 공간에서 작동합니다. 완성된 기하학을 기반으로 작동함으로써, 3DPWM은 신뢰할 수 있는 장기 롤아웃과 모델 기반 계획을 위한 더 정확한 비용 평가를 가능하게 하며, 새로운 작업에 대한 적응을 지원합니다. 다양한 로봇 형태와 테이블탑 조작 벤치마크에 걸친 실험은 3DPWM이 현저히 더 신뢰할 수 있는 장기 롤아웃(100-300+ 단계)을 달성하고, 개방 루프 및 폐쇄 루프 계획을 모두 지원하며, 성공적인 시뮬레이션-실제 전이를 가능하게 함을 보여줍니다.

## 핵심 내용
세계의 예측 모델을 학습하면 계획을 통한 로봇 제어가 가능해져, 로봇이 새로운 작업에 대한 해결책을 즉석에서 창출할 수 있습니다. 그러나 대규모 비디오 기반 동역학 모델은 명시적인 3D 공간 구조가 부족하고, 오차가 누적되어 기하학적으로 일관되지 않은 장기 롤아웃을 초래합니다. 부분 포인트 클라우드에 기반한 새로운 3D 동역학 모델은 기하학적 일관성을 개선하지만, 여전히 폐색과 누적된 예측 드리프트에 민감합니다. 이러한 문제를 해결하기 위해, 우리는 3D 포인트 월드 모델(3DPWM)을 제시합니다. 이는 작업에 구애받지 않는 세계 모델로, 먼저 부분 포인트 클라우드를 완성한 후 완성된 3D 장면에서 행동 조건 동역학을 학습함으로써 전적으로 3D 공간에서 작동합니다. 완성된 기하학을 기반으로 작동함으로써, 3DPWM은 신뢰할 수 있는 장기 롤아웃과 모델 기반 계획을 위한 더 정확한 비용 평가를 가능하게 하며, 새로운 작업에 대한 적응을 지원합니다. 다양한 로봇 형태와 테이블탑 조작 벤치마크에 걸친 실험은 3DPWM이 현저히 더 신뢰할 수 있는 장기 롤아웃(100-300+ 단계)을 달성하고, 개방 루프 및 폐쇄 루프 계획을 모두 지원하며, 성공적인 시뮬레이션-실제 전이를 가능하게 함을 보여줍니다.

## 参考
- http://arxiv.org/abs/2607.00148v1
