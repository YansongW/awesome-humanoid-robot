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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.11143v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (920 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2602.11143v2

## 개요
기존의 심층 강화 학습으로 훈련된 휴머노이드 로봇은 울퉁불퉁한 지형을 안정적으로 횡단할 수 있지만, 다리 길이를 초과하는 높은 플랫폼에 직면했을 때 종종 높은 충격, 토크 제한, 그리고 안전하지 않은 점프 방식의 해결책으로 수렴합니다. APEX 시스템은 등반, 보행, 기어가기, 서기, 눕기 등 여섯 가지 지형 조건 행동을 결합하여 인식 기반의 높은 플랫폼 등반 횡단을 구현합니다. 핵심 혁신은 범용 래칫 진행 보상으로, 최적의 작업 진행 상황을 추적하고 비효율적인 단계에 패널티를 부여하여 강력한 안전 정규화 하에서 효율적인 탐색을 가능하게 합니다. 시스템은 LiDAR 기반의 전신 제어 정책을 채택하고, 훈련 중 지도 작성 아티팩트를 시뮬레이션하고 배포 시 필터링으로 복구하는 이중 전략을 통해 시뮬레이션-실제 격차를 줄입니다. 최종적으로 모든 스킬을 단일 정책으로 증류하여 로컬 지오메트리와 명령에 기반한 자율적 행동 선택 및 전환을 구현합니다.

## 핵심 내용
### 방법 아키텍처
- **행동 조합**: 시스템은 여섯 가지 조합 가능한 행동을 포함합니다: 수직 가장자리의 climb-up(등반) 및 climb-down(하강), 플랫폼 위의 walking(보행) 및 crawling(기어가기), 그리고 자세 재구성의 stand-up(서기) 및 lie-down(눕기).
- **래칫 진행 보상**: 핵심 보상 함수는 현재 최적의 작업 진행 상황을 추적하고, 개선되지 않은 단계에 패널티를 부여하여 밀집되고 속도가 없는 감독 신호를 제공하며, 강력한 안전 제약 하에서 효율적인 탐색을 가능하게 합니다.
- **인식 정책**: LiDAR 기반의 전신 제어 정책으로, 이중 sim-to-real 전략을 채택합니다: 훈련 중 지도 작성 아티팩트를 시뮬레이션하고, 배포 시 고도 지도를 필터링 및 복구합니다.

### 실험 설정
- **하드웨어 플랫폼**: 29 자유도 Unitree G1 휴머노이드 로봇
- **작업 목표**: 0.8미터 높이 플랫폼(약 114% 다리 길이)의 제로샷 횡단
- **훈련 프레임워크**: 심층 강화 학습, 여섯 가지 스킬 모두 단일 정책으로 증류

### 주요 결과
- **횡단 능력**: 0.8미터 높이 플랫폼의 제로샷 시뮬레이션-실제 횡단 성공, 플랫폼 높이는 로봇 다리 길이의 114%
- **강건성**: 플랫폼 높이 변화와 초기 자세 차이에 대한 적응 능력 보유
- **행동 전환**: 로컬 지오메트리 특징과 명령에 기반한 행동 선택으로 다중 스킬 간 부드럽고 안정적인 자율 전환 구현

### 결론
APEX는 래칫 진행 보상과 다중 스킬 증류 전략을 통해 휴머노이드 로봇의 높은 플랫폼 횡단 병목 현상을 돌파하고, 기존 점프 방식의 높은 충격과 토크 제한 문제를 피하며, 복잡한 지형에서의 전신 운동 제어를 위한 새로운 패러다임을 제공합니다.
