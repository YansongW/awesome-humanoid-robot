---
$id: ent_paper_nian_control_your_robot_a_unified_s_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Control Your Robot: A Unified System for Robot Control and Policy Deployment'
  zh: Control Your Robot
  ko: 'Control Your Robot: A Unified System for Robot Control and Policy Deployment'
summary:
  en: 'Control Your Robot: A Unified System for Robot Control and Policy Deployment (Control Your Robot), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by ScaleLab, Shanghai Jiao Tong University, University
    of Shanghai for Science and Technology, Lumina Group.'
  zh: Control Your Robot 是 2025 年由 ScaleLab、上海交通大学、上海理工大学及 Lumina Group 联合提出的大型视觉-语言-动作模型系统，用于机器人操作。其核心贡献在于通过模块化设计与统一 API，实现了跨平台机器人控制与策略部署的标准化工作流，并支持遥操作与轨迹回放的双模式控制。
  ko: 'Control Your Robot: A Unified System for Robot Control and Policy Deployment (Control Your Robot), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by ScaleLab, Shanghai Jiao Tong University, University
    of Shanghai for Science and Technology, Lumina Group.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- control_your_robot
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.23823v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (706 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Control Your Robot: A Unified System for Robot Control and Policy Deployment (arXiv)'
  url: https://arxiv.org/abs/2509.23823
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Control Your Robot source
  url: https://doi.org/10.48550/arXiv.2509.23823
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该框架旨在解决跨平台机器人控制中因硬件接口、数据格式与控制范式差异导致的工具链碎片化与部署缓慢问题。Control Your Robot 采用标准化工作流，包含模块化设计、统一 API 及闭环架构，支持灵活的机器人注册、遥操作与轨迹回放双模式控制，以及从多模态数据采集到推理的无缝集成。在单臂与双臂系统上的实验表明，该系统能实现高效低延迟的数据采集，并有效支持基于模仿学习与视觉-语言-动作模型的策略学习。

## 核心内容
### 方法
Control Your Robot 是一个模块化通用框架，通过以下设计统一数据采集与策略部署：
- **标准化工作流**：采用模块化设计、统一 API 与闭环架构，减少工具链碎片化。
- **双模式控制**：支持遥操作与轨迹回放，便于灵活操作。
- **多模态集成**：从多模态数据采集到推理实现无缝衔接。

### 架构
- **机器人注册**：支持灵活注册不同平台机器人。
- **闭环架构**：确保控制与策略部署的实时反馈与调整。

### 实验设置
- **系统测试**：在单臂与双臂机器人系统上进行实验。
- **数据采集**：评估了数据采集的效率与延迟。
- **策略学习**：使用模仿学习与视觉-语言-动作模型进行策略训练。

### 关键数字
- **低延迟**：数据采集实现高效低延迟。
- **策略匹配度**：基于 Control Your Robot 采集数据训练的策略与专家演示高度匹配。

### 结论
Control Your Robot 框架使机器人学习具备跨平台的可扩展性与可复现性，为机器人控制与策略部署提供了统一解决方案。

## Overview
Cross-platform robot control remains difficult because hardware interfaces, data formats, and control paradigms vary widely, which fragments toolchains and slows deployment. To address this, we present Control Your Robot, a modular, general-purpose framework that unifies data collection and policy deployment across diverse platforms. The system reduces fragmentation through a standardized workflow with modular design, unified APIs, and a closed-loop architecture. It supports flexible robot registration, dual-mode control with teleoperation and trajectory playback, and seamless integration from multimodal data acquisition to inference. Experiments on single-arm and dual-arm systems show efficient, low-latency data collection and effective support for policy learning with imitation learning and vision-language-action models. Policies trained on data gathered by Control Your Robot match expert demonstrations closely, indicating that the framework enables scalable and reproducible robot learning across platforms.

## 参考
- http://arxiv.org/abs/2509.23823v2

## 개요
이 프레임워크는 크로스 플랫폼 로봇 제어에서 하드웨어 인터페이스, 데이터 형식 및 제어 패러다임의 차이로 인해 발생하는 도구 체인 파편화와 배포 지연 문제를 해결하는 것을 목표로 합니다. Control Your Robot은 모듈식 설계, 통합 API 및 폐쇄 루프 아키텍처를 포함한 표준화된 워크플로우를 채택하여, 유연한 로봇 등록, 원격 조작 및 궤적 재생의 이중 모드 제어, 그리고 다중 모달 데이터 수집에서 추론까지의 원활한 통합을 지원합니다. 단일 암 및 이중 암 시스템에서의 실험은 이 시스템이 효율적이고 낮은 지연 시간의 데이터 수집을 달성하고, 모방 학습 및 비전-언어-행동 모델 기반의 정책 학습을 효과적으로 지원함을 보여줍니다.

## 핵심 내용
### 방법
Control Your Robot은 모듈식 범용 프레임워크로, 다음 설계를 통해 데이터 수집과 정책 배포를 통합합니다:
- **표준화된 워크플로우**: 모듈식 설계, 통합 API 및 폐쇄 루프 아키텍처를 채택하여 도구 체인 파편화를 줄입니다.
- **이중 모드 제어**: 원격 조작과 궤적 재생을 지원하여 유연한 운영을 가능하게 합니다.
- **다중 모달 통합**: 다중 모달 데이터 수집에서 추론까지 원활한 연결을 구현합니다.

### 아키텍처
- **로봇 등록**: 다양한 플랫폼의 로봇을 유연하게 등록할 수 있도록 지원합니다.
- **폐쇄 루프 아키텍처**: 제어 및 정책 배포의 실시간 피드백과 조정을 보장합니다.

### 실험 설정
- **시스템 테스트**: 단일 암 및 이중 암 로봇 시스템에서 실험을 수행합니다.
- **데이터 수집**: 데이터 수집의 효율성과 지연 시간을 평가합니다.
- **정책 학습**: 모방 학습 및 비전-언어-행동 모델을 사용하여 정책을 훈련합니다.

### 주요 수치
- **낮은 지연 시간**: 데이터 수집에서 효율적이고 낮은 지연 시간을 구현합니다.
- **정책 일치도**: Control Your Robot으로 수집된 데이터로 훈련된 정책은 전문가 시연과 높은 일치도를 보입니다.

### 결론
Control Your Robot 프레임워크는 로봇 학습에 크로스 플랫폼 확장성과 재현성을 제공하여, 로봇 제어 및 정책 배포를 위한 통합 솔루션을 제시합니다.
