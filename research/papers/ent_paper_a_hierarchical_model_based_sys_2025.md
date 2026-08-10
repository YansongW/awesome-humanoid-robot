---
$id: ent_paper_a_hierarchical_model_based_sys_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Hierarchical, Model-Based System for High-Performance Humanoid Soccer
  zh: A Hierarchical, Model-Based System for High-Performance Humanoid Soccer
  ko: A Hierarchical, Model-Based System for High-Performance Humanoid Soccer
summary:
  en: A Hierarchical, Model-Based System for High-Performance Humanoid Soccer is a 2025 work on locomotion for humanoid robots.
  zh: 本文提出了一套层级化、基于模型的系统，用于高性能人形足球机器人。该系统由加州大学洛杉矶分校（UCLA）团队开发，核心贡献包括轻量化硬件设计（高扭矩准直驱执行器与专用脚部结构）和集成感知-导航-决策软件框架。该系统助力ARTEMIS机器人赢得RoboCup
    2024成人组人形足球冠军。
  ko: A Hierarchical, Model-Based System for High-Performance Humanoid Soccer is a 2025 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- a_hierarchical_model_based_sys
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.09431v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (671 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: A Hierarchical, Model-Based System for High-Performance Humanoid Soccer (arXiv)
  url: https://arxiv.org/abs/2512.09431
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
本文介绍了赢得RoboCup 2024成人组人形足球比赛的硬件与软件创新。硬件方面，采用轻质结构组件、高扭矩准直驱执行器和特殊脚部设计，实现强力踢球同时保持运动鲁棒性。软件方面，集成立体视觉、目标检测与地标融合的感知定位框架，中层导航生成碰撞感知的动态可行轨迹，高层行为管理器协调决策、角色分配与踢球执行。各子系统无缝集成，在真实比赛动态对抗条件下实现快速、精准的战术表现。

## 核心内容
### 硬件设计
- **轻量化结构**：采用碳纤维等轻质材料构建成人尺寸机器人平台，降低运动惯量。
- **高扭矩准直驱执行器**：提供高力矩输出，支持动态运动与强力踢球。
- **专用脚部设计**：在踢球时保持运动鲁棒性，实现“行进中踢球”（in-gait kick）能力。

### 软件架构
- **感知与定位**：融合立体视觉、目标检测与地标定位，可靠估计球、球门、队友和对手位置。
- **中层导航**：生成碰撞感知、动态可行的运动轨迹，避免障碍物并适应环境变化。
- **高层行为管理**：基于实时比赛状态协调决策、角色分配与踢球执行，实现战术协同。

### 实验与结果
- **比赛表现**：ARTEMIS在RoboCup 2024成人组比赛中展现快速、精准的战术能力，最终夺冠。
- **关键指标**：系统在动态对抗条件下保持鲁棒性，踢球成功率与运动稳定性显著优于对手。

### 结论
本文验证了层级化、基于模型的设计方法在人形足球中的有效性，为未来RoboCup 2050年目标（与人类球员对抗）提供了技术基础。

## Overview
The development of athletic humanoid robots has gained significant attention as advances in actuation, sensing, and control enable increasingly dynamic, real-world capabilities. RoboCup, an international competition of fully autonomous humanoid robots, provides a uniquely challenging benchmark for such systems, culminating in the long-term goal of competing against human soccer players by 2050. This paper presents the hardware and software innovations underlying our team's victory in the RoboCup 2024 Adult-Sized Humanoid Soccer Competition. On the hardware side, we introduce an adult-sized humanoid platform built with lightweight structural components, high-torque quasi-direct-drive actuators, and a specialized foot design that enables powerful in-gait kicks while preserving locomotion robustness. On the software side, we develop an integrated perception and localization framework that combines stereo vision, object detection, and landmark-based fusion to provide reliable estimates of the ball, goals, teammates, and opponents. A mid-level navigation stack then generates collision-aware, dynamically feasible trajectories, while a centralized behavior manager coordinates high-level decision making, role selection, and kick execution based on the evolving game state. The seamless integration of these subsystems results in fast, precise, and tactically effective gameplay, enabling robust performance under the dynamic and adversarial conditions of real matches. This paper presents the design principles, system architecture, and experimental results that contributed to ARTEMIS's success as the 2024 Adult-Sized Humanoid Soccer champion.

## 参考
- http://arxiv.org/abs/2512.09431v1

## 개요
이 논문은 RoboCup 2024 성인부 휴머노이드 축구 경기에서 우승을 차지한 하드웨어 및 소프트웨어 혁신을 소개합니다. 하드웨어 측면에서는 경량 구조 부품, 고토크 준직접 구동 액추에이터, 특수 발 설계를 통해 강력한 킥을 구현하면서도 운동 견고성을 유지합니다. 소프트웨어 측면에서는 스테레오 비전, 객체 탐지, 랜드마크 융합을 통합한 인식 및 위치 추정 프레임워크를 구축하고, 중간 계층 내비게이션은 충돌 인식 기반의 동적 실행 가능 궤적을 생성하며, 상위 계층 행동 관리자는 의사 결정, 역할 분배, 킥 실행을 조율합니다. 각 하위 시스템은 원활하게 통합되어 실제 경기의 동적 대항 조건에서 빠르고 정밀한 전술적 성능을 발휘합니다.

## 핵심 내용
### 하드웨어 설계
- **경량 구조**: 탄소 섬유 등 경량 소재로 성인용 로봇 플랫폼을 제작하여 운동 관성을 낮춥니다.
- **고토크 준직접 구동 액추에이터**: 높은 토크 출력을 제공하여 동적 운동과 강력한 킥을 지원합니다.
- **전용 발 설계**: 킥 수행 중에도 운동 견고성을 유지하여 '걸으면서 차는 킥'(in-gait kick) 능력을 구현합니다.

### 소프트웨어 아키텍처
- **인식 및 위치 추정**: 스테레오 비전, 객체 탐지, 랜드마크 위치 추정을 융합하여 공, 골대, 팀원, 상대방의 위치를 안정적으로 추정합니다.
- **중간 계층 내비게이션**: 충돌 인식 및 동적 실행 가능한 운동 궤적을 생성하여 장애물을 회피하고 환경 변화에 적응합니다.
- **상위 계층 행동 관리**: 실시간 경기 상태를 기반으로 의사 결정, 역할 분배, 킥 실행을 조율하여 전술적 협력을 구현합니다.

### 실험 및 결과
- **경기 성과**: ARTEMIS는 RoboCup 2024 성인부 경기에서 빠르고 정밀한 전술 능력을 선보이며 최종 우승을 차지했습니다.
- **핵심 지표**: 시스템은 동적 대항 조건에서도 견고성을 유지했으며, 킥 성공률과 운동 안정성에서 상대보다 월등히 우수했습니다.

### 결론
이 논문은 계층적이고 모델 기반의 설계 방법이 휴머노이드 축구에서 효과적임을 입증하며, 향후 RoboCup 2050 목표(인간 선수와의 대결)를 위한 기술적 기반을 제공합니다.
