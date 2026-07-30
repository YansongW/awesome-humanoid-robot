---
$id: ent_paper_apex_learning_adaptive_high_pl_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'APEX: Learning Adaptive High-Platform Traversal for Humanoid Robots'
  zh: 'APEX: Learning Adaptive High-Platform Traversal for Humanoid Robots'
  ko: 'APEX: Learning Adaptive High-Platform Traversal for Humanoid Robots'
summary:
  en: 'APEX: Learning Adaptive High-Platform Traversal for Humanoid Robots is a 2026 work on locomotion for humanoid robots.'
  zh: APEX 是2026年提出的人形机器人自适应高平台穿越系统，由研究团队开发。其核心贡献在于通过强化学习实现基于攀爬的0.8米高平台（约114%腿长）零样本穿越，并设计了棘轮进度奖励机制与多技能蒸馏策略。
  ko: 'APEX: Learning Adaptive High-Platform Traversal for Humanoid Robots is a 2026 work on locomotion for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- apex
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.11143v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'APEX: Learning Adaptive High-Platform Traversal for Humanoid Robots (arXiv)'
  url: https://arxiv.org/abs/2602.11143
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'APEX: Learning Adaptive High-Platform Traversal for Humanoid Robots project page'
  url: https://apex-humanoid.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
现有深度强化学习训练的人形机器人虽能稳健穿越不平坦地面，但面对超过腿长的高平台时，常收敛到高冲击、扭矩受限且不安全的跳跃式解决方案。APEX 系统通过组合攀爬、行走、爬行、站立、躺卧等六种地形条件行为，实现了感知驱动的攀爬式高平台穿越。其核心创新是通用棘轮进度奖励，通过追踪最佳任务进度并惩罚无效步骤，在强安全正则化下实现高效探索。系统采用 LiDAR 全身控制策略，并通过训练时模拟建图伪影、部署时滤波修复的双重策略缩小仿真到现实的感知差距。最终将所有技能蒸馏为单一策略，实现基于局部几何与指令的自主行为选择与切换。

## 核心内容
### 方法架构
- **行为组合**：系统包含六种可组合行为：垂直边缘的 climb-up（攀爬）与 climb-down（攀下）、平台上的 walking（行走）与 crawling（爬行）、以及 posture reconfiguration（姿态重构）的 stand-up（站立）与 lie-down（躺卧）。
- **棘轮进度奖励**：核心奖励函数追踪当前最佳任务进度，对未改进步骤施加惩罚，提供密集且无速度的监督信号，在强安全约束下实现高效探索。
- **感知策略**：基于 LiDAR 的全身控制策略，采用双重 sim-to-real 策略：训练时模拟建图伪影，部署时对高程图进行滤波与修复。

### 实验设置
- **硬件平台**：29 自由度 Unitree G1 人形机器人
- **任务目标**：零样本穿越 0.8 米高平台（约 114% 腿长）
- **训练框架**：深度强化学习，所有六种技能蒸馏为单一策略

### 关键结果
- **穿越能力**：成功实现 0.8 米高平台的零样本仿真到现实穿越，平台高度为机器人腿长的 114%
- **鲁棒性**：对平台高度变化与初始姿态差异具有自适应能力
- **行为切换**：多技能间实现平滑稳定的自主转换，基于局部几何特征与指令选择行为

### 结论
APEX 通过棘轮进度奖励与多技能蒸馏策略，突破了人形机器人高平台穿越的瓶颈，避免了传统跳跃式方案的高冲击与扭矩限制问题，为复杂地形下的全身运动控制提供了新范式。

## Overview
Humanoid locomotion has advanced rapidly with deep reinforcement learning (DRL), enabling robust feet-based traversal over uneven terrain. Yet platforms beyond leg length remain largely out of reach because current RL training paradigms often converge to jumping-like solutions that are high-impact, torque-limited, and unsafe for real-world deployment. To address this gap, we propose APEX, a system for perceptive, climbing-based high-platform traversal that composes terrain-conditioned behaviors: climb-up and climb-down at vertical edges, walking or crawling on the platform, and stand-up and lie-down for posture reconfiguration. Central to our approach is a generalized ratchet progress reward for learning contact-rich, goal-reaching maneuvers. It tracks the best-so-far task progress and penalizes non-improving steps, providing dense yet velocity-free supervision that enables efficient exploration under strong safety regularization. Based on this formulation, we train LiDAR-based full-body maneuver policies and reduce the sim-to-real perception gap through a dual strategy: modeling mapping artifacts during training and applying filtering and inpainting to elevation maps during deployment. Finally, we distill all six skills into a single policy that autonomously selects behaviors and transitions based on local geometry and commands. Experiments on a 29-DoF Unitree G1 humanoid demonstrate zero-shot sim-to-real traversal of 0.8 meter platforms (approximately 114% of leg length), with robust adaptation to platform height and initial pose, as well as smooth and stable multi-skill transitions.

## 개요
인간형 로봇의 보행은 심층 강화 학습(DRL)의 발전으로 급속히 진보하여, 거친 지형에서도 견고한 발 기반 이동이 가능해졌습니다. 그러나 다리 길이를 초과하는 플랫폼은 여전히 도달하기 어려운데, 이는 현재의 RL 훈련 패러다임이 충격이 크고 토크 제한이 있으며 실제 환경 배포에 안전하지 않은 점프형 해결책으로 수렴하는 경향이 있기 때문입니다. 이러한 격차를 해소하기 위해, 우리는 APEX를 제안합니다. 이는 지형 조건에 따른 행동(수직 모서리에서의 올라가기와 내려오기, 플랫폼 위 걷기 또는 기어가기, 자세 재구성을 위한 일어서기와 눕기)을 구성하는 인지 기반 등반형 고플랫폼 이동 시스템입니다. 우리 접근법의 핵심은 접촉이 풍부하고 목표 도달 기동을 학습하기 위한 일반화된 래칫 진행 보상입니다. 이는 지금까지의 최고 작업 진행 상황을 추적하고 개선되지 않는 단계에 패널티를 부여하여, 강력한 안전 정규화 하에서 효율적인 탐색을 가능하게 하는 밀집하면서도 속도가 없는 감독을 제공합니다. 이 공식에 기반하여, 우리는 LiDAR 기반 전신 기동 정책을 훈련하고, 훈련 중 매핑 아티팩트를 모델링하고 배포 중 고도 맵에 필터링 및 인페인팅을 적용하는 이중 전략을 통해 시뮬레이션-실제 인식 격차를 줄입니다. 마지막으로, 우리는 여섯 가지 기술을 모두 단일 정책으로 증류하여, 로컬 지오메트리와 명령에 따라 자율적으로 행동과 전환을 선택합니다. 29자유도 Unitree G1 인간형 로봇 실험을 통해, 0.8미터 플랫폼(다리 길이의 약 114%)에 대한 제로샷 시뮬레이션-실제 이동, 플랫폼 높이와 초기 자세에 대한 견고한 적응, 그리고 부드럽고 안정적인 다중 기술 전환을 입증했습니다.

## 핵심 내용
인간형 로봇의 보행은 심층 강화 학습(DRL)의 발전으로 급속히 진보하여, 거친 지형에서도 견고한 발 기반 이동이 가능해졌습니다. 그러나 다리 길이를 초과하는 플랫폼은 여전히 도달하기 어려운데, 이는 현재의 RL 훈련 패러다임이 충격이 크고 토크 제한이 있으며 실제 환경 배포에 안전하지 않은 점프형 해결책으로 수렴하는 경향이 있기 때문입니다. 이러한 격차를 해소하기 위해, 우리는 APEX를 제안합니다. 이는 지형 조건에 따른 행동(수직 모서리에서의 올라가기와 내려오기, 플랫폼 위 걷기 또는 기어가기, 자세 재구성을 위한 일어서기와 눕기)을 구성하는 인지 기반 등반형 고플랫폼 이동 시스템입니다. 우리 접근법의 핵심은 접촉이 풍부하고 목표 도달 기동을 학습하기 위한 일반화된 래칫 진행 보상입니다. 이는 지금까지의 최고 작업 진행 상황을 추적하고 개선되지 않는 단계에 패널티를 부과하여, 강력한 안전 정규화 하에서 효율적인 탐색을 가능하게 하는 밀집하면서도 속도가 없는 감독을 제공합니다. 이 공식에 기반하여, 우리는 LiDAR 기반 전신 기동 정책을 훈련하고, 훈련 중 매핑 아티팩트를 모델링하고 배포 중 고도 맵에 필터링 및 인페인팅을 적용하는 이중 전략을 통해 시뮬레이션-실제 인식 격차를 줄입니다. 마지막으로, 우리는 여섯 가지 기술을 모두 단일 정책으로 증류하여, 로컬 지오메트리와 명령에 따라 자율적으로 행동과 전환을 선택합니다. 29자유도 Unitree G1 인간형 로봇 실험을 통해, 0.8미터 플랫폼(다리 길이의 약 114%)에 대한 제로샷 시뮬레이션-실제 이동, 플랫폼 높이와 초기 자세에 대한 견고한 적응, 그리고 부드럽고 안정적인 다중 기술 전환을 입증했습니다.

## 参考
- http://arxiv.org/abs/2602.11143v2
