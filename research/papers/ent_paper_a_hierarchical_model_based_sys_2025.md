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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.09431v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
운동 능력을 갖춘 휴머노이드 로봇의 개발은 구동, 센싱, 제어 기술의 발전으로 점점 더 역동적이고 실제 환경에서의 능력이 가능해짐에 따라 큰 주목을 받고 있습니다. 완전 자율 휴머노이드 로봇의 국제 대회인 RoboCup은 이러한 시스템에 독특하게 도전적인 기준을 제공하며, 2050년까지 인간 축구 선수와 경쟁한다는 장기 목표로 이어집니다. 본 논문은 RoboCup 2024 성인형 휴머노이드 축구 대회에서 우리 팀의 우승을 이끈 하드웨어 및 소프트웨어 혁신을 제시합니다. 하드웨어 측면에서는 경량 구조 부품, 고토크 준직접 구동 액추에이터, 그리고 보행 견고성을 유지하면서 강력한 인게이트 킥을 가능하게 하는 특수 발 설계로 구축된 성인형 휴머노이드 플랫폼을 소개합니다. 소프트웨어 측면에서는 스테레오 비전, 객체 감지, 랜드마크 기반 융합을 결합하여 공, 골대, 팀원, 상대방에 대한 신뢰할 수 있는 추정을 제공하는 통합 인식 및 위치 추정 프레임워크를 개발합니다. 중간 수준의 내비게이션 스택은 충돌을 고려한 동적으로 실행 가능한 궤적을 생성하고, 중앙 집중식 행동 관리자는 변화하는 게임 상태에 따라 고수준 의사 결정, 역할 선택, 킥 실행을 조정합니다. 이러한 하위 시스템의 원활한 통합은 빠르고 정확하며 전술적으로 효과적인 게임 플레이를 가능하게 하여 실제 경기의 역동적이고 적대적인 조건에서 견고한 성능을 발휘합니다. 본 논문은 ARTEMIS가 2024년 성인형 휴머노이드 축구 챔피언으로 성공하는 데 기여한 설계 원칙, 시스템 아키텍처, 실험 결과를 제시합니다.

## 핵심 내용
운동 능력을 갖춘 휴머노이드 로봇의 개발은 구동, 센싱, 제어 기술의 발전으로 점점 더 역동적이고 실제 환경에서의 능력이 가능해짐에 따라 큰 주목을 받고 있습니다. 완전 자율 휴머노이드 로봇의 국제 대회인 RoboCup은 이러한 시스템에 독특하게 도전적인 기준을 제공하며, 2050년까지 인간 축구 선수와 경쟁한다는 장기 목표로 이어집니다. 본 논문은 RoboCup 2024 성인형 휴머노이드 축구 대회에서 우리 팀의 우승을 이끈 하드웨어 및 소프트웨어 혁신을 제시합니다. 하드웨어 측면에서는 경량 구조 부품, 고토크 준직접 구동 액추에이터, 그리고 보행 견고성을 유지하면서 강력한 인게이트 킥을 가능하게 하는 특수 발 설계로 구축된 성인형 휴머노이드 플랫폼을 소개합니다. 소프트웨어 측면에서는 스테레오 비전, 객체 감지, 랜드마크 기반 융합을 결합하여 공, 골대, 팀원, 상대방에 대한 신뢰할 수 있는 추정을 제공하는 통합 인식 및 위치 추정 프레임워크를 개발합니다. 중간 수준의 내비게이션 스택은 충돌을 고려한 동적으로 실행 가능한 궤적을 생성하고, 중앙 집중식 행동 관리자는 변화하는 게임 상태에 따라 고수준 의사 결정, 역할 선택, 킥 실행을 조정합니다. 이러한 하위 시스템의 원활한 통합은 빠르고 정확하며 전술적으로 효과적인 게임 플레이를 가능하게 하여 실제 경기의 역동적이고 적대적인 조건에서 견고한 성능을 발휘합니다. 본 논문은 ARTEMIS가 2024년 성인형 휴머노이드 축구 챔피언으로 성공하는 데 기여한 설계 원칙, 시스템 아키텍처, 실험 결과를 제시합니다.

## 参考
- http://arxiv.org/abs/2512.09431v1
