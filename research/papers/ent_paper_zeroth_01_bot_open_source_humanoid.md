---
$id: ent_paper_zeroth_01_bot_open_source_humanoid
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: '[Zeroth Bot](https://github.com/zeroth-robotics/zeroth-bot)'
  zh: '[Zeroth Bot](https://github.com/zeroth-robotics/zeroth-bot)'
  ko: '[Zeroth Bot](https://github.com/zeroth-robotics/zeroth-bot)'
summary:
  en: "<div align=\"center\" style=\"text-align: center;\">\n\n  <h1>Zeroth-01 Bot</h1>\
    \ \n\n<p> Super hackable, affordable, and end-to-end (sim2real, RL) 3D-printed\
    \ open-source humanoid robot platform."
  zh: Zeroth-01 Bot 是一个完全开源、高度可定制且价格亲民（物料清单起价 350 美元）的 3D 打印人形机器人平台，由开源社区构建。其核心贡献在于提供了端到端的
    sim2real 与强化学习训练能力，并集成了机器人操作系统 KOS-ZBot 和 RL 训练环境 K-Sim Gym ZBot，支持从基础运动到视觉、语音的完整功能。
  ko: "<div align=\"center\" style=\"text-align: center;\">\n\n  <h1>Zeroth-01 Bot</h1>\
    \ \n\n<p> Super hackable, affordable, and end-to-end (sim2real, RL) 3D-printed\
    \ open-source humanoid robot platform."
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- zeroth
- bot
- https
- github
- com
- project_page_sourced
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: Full ingest from Yuanxq lab paper list row 671 (.staging/ingest_yuanxq).
    Tier B->page. Content compiled by DeepSeek from the fetched project page (https://raw.githubusercontent.com/zeroth-robotics/zeroth-bot/HEAD/README.md).
    Institutions unknown. [2026-07-31] id renamed from ent_paper_zeroth_bot_https_github_com_zeroth
    (non-compliant slug) by ingest_yuanxq id-fix.
sources:
- id: src_001
  type: website
  title: Project page
  url: https://github.com/zeroth-robotics/zeroth-bot
  accessed_at: '2026-07-31'
- id: src_002
  type: website
  title: Project page (fetched)
  url: https://raw.githubusercontent.com/zeroth-robotics/zeroth-bot/HEAD/README.md
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---


## 概述

Zeroth-01 Bot 是一个由开源社区开发的人形机器人平台，旨在通过 3D 打印和低成本物料（起价 350 美元）降低人形机器人研发门槛。该项目完全开源，涵盖硬件、SDK 和仿真环境，并提供了机器人操作系统 KOS-ZBot 和强化学习训练框架 K-Sim Gym ZBot。KOS-ZBot 负责底层硬件驱动（如 Feetech 舵机控制、IMU 接口）和高级 Python API，而 K-Sim Gym ZBot 则支持 GPU 加速的全身控制 RL 训练，并实现了从仿真到真实机器人的策略部署。目前处于公开测试阶段，计划于 2025 年 6 月发布稳定版 V1.0。

## 核心内容
### 项目状态
Zeroth-01 Bot 目前处于公开测试阶段，支持基础运动、视觉和语音功能，但可能存在破坏性变更。稳定版 V1.0 计划于 2025 年 6 月发布。

### 核心组件

#### KOS-ZBot - 操作系统
KOS-ZBot 提供机器人操作系统和硬件抽象层，包含以下关键模块：
- **硬件驱动**：支持 Feetech 舵机控制、IMU 接口和致动器管理。
- **Python API**：通过 `kos_zbot` 包提供高级控制接口，便于开发者使用 Python 进行开发。
- **实时控制**：实现低延迟的舵机通信和传感器数据处理。
- **CLI 工具**：提供机器人校准、诊断和系统配置的命令行工具。

#### K-Sim Gym ZBot - 强化学习训练
K-Sim Gym ZBot 提供强化学习训练管道，核心特性包括：
- **训练管道**：基于 GPU 加速的 RL 算法，支持全身控制训练，涵盖行走和人类动作模仿。
- **Sim-to-real**：通过系统辨识（SysID）校准致动器，并预加载 MJCF 和 URDF 模型，实现仿真到现实的迁移。
- **模型部署**：训练好的策略可直接通过 KOS 导出到真实机器人上运行。

### 构建指南
请参考官方文档 [https://docs.kscale.dev/docs/zeroth-01](https://docs.kscale.dev/docs/zeroth-01) 中的“Getting Started”部分。

### 如何开始开发
Zeroth Bot 由开源社区开发，欢迎在 GitHub 上提交 Pull Request 或 Issue。加入社区 Discord 或查阅文档以获取更多支持。

### 许可证
本项目采用 MIT 许可证。

## 参考
- https://github.com/zeroth-robotics/zeroth-bot
- https://raw.githubusercontent.com/zeroth-robotics/zeroth-bot/HEAD/README.md
- https://github.com/ImChong/Robotics_Notebooks

## Overview

Zeroth-01 Bot is a humanoid robot platform developed by the open-source community, designed to lower the barrier to humanoid robot research and development through 3D printing and low-cost materials (starting at $350). The project is fully open-source, covering hardware, SDK, and simulation environments, and provides the robot operating system KOS-ZBot and the reinforcement learning training framework K-Sim Gym ZBot. KOS-ZBot handles low-level hardware drivers (such as Feetech servo control, IMU interfaces) and a high-level Python API, while K-Sim Gym ZBot supports GPU-accelerated whole-body control RL training and implements policy deployment from simulation to real robots. It is currently in public beta, with a stable version V1.0 planned for release in June 2025.

## Content
### Project Status
Zeroth-01 Bot is currently in public beta, supporting basic locomotion, vision, and speech functions, but may include breaking changes. The stable version V1.0 is planned for release in June 2025.

### Core Components

#### KOS-ZBot - Operating System
KOS-ZBot provides the robot operating system and hardware abstraction layer, including the following key modules:
- **Hardware Drivers**: Supports Feetech servo control, IMU interfaces, and actuator management.
- **Python API**: Provides high-level control interfaces through the `kos_zbot` package, facilitating development in Python for developers.
- **Real-time Control**: Implements low-latency servo communication and sensor data processing.
- **CLI Tools**: Provides command-line tools for robot calibration, diagnostics, and system configuration.

#### K-Sim Gym ZBot - Reinforcement Learning Training
K-Sim Gym ZBot provides a reinforcement learning training pipeline, with core features including:
- **Training Pipeline**: Based on GPU-accelerated RL algorithms, supports whole-body control training, covering walking and human motion imitation.
- **Sim-to-real**: Calibrates actuators through system identification (SysID) and preloads MJCF and URDF models to achieve simulation-to-reality transfer.
- **Model Deployment**: Trained policies can be directly exported to real robots via KOS for execution.

### Build Guide
Please refer to the "Getting Started" section in the official documentation at [https://docs.kscale.dev/docs/zeroth-01](https://docs.kscale.dev/docs/zeroth-01).

### How to Start Developing
Zeroth Bot is developed by the open-source community, and Pull Requests or Issues on GitHub are welcome. Join the community Discord or consult the documentation for further support.

### License
This project is licensed under the MIT License.

## 개요

Zeroth-01 Bot은 오픈소스 커뮤니티에서 개발한 휴머노이드 로봇 플랫폼으로, 3D 프린팅과 저비용 부품(최저 350달러)을 통해 휴머노이드 로봇 개발의 진입 장벽을 낮추는 것을 목표로 합니다. 이 프로젝트는 완전히 오픈소스이며, 하드웨어, SDK, 시뮬레이션 환경을 포함하고 있으며, 로봇 운영 체제 KOS-ZBot과 강화 학습 훈련 프레임워크 K-Sim Gym ZBot을 제공합니다. KOS-ZBot은 하드웨어 드라이버(예: Feetech 서보 제어, IMU 인터페이스)와 고급 Python API를 담당하고, K-Sim Gym ZBot은 GPU 가속 전신 제어 RL 훈련을 지원하며, 시뮬레이션에서 실제 로봇으로의 정책 배포를 구현합니다. 현재 공개 베타 단계에 있으며, 2025년 6월 안정 버전 V1.0 출시를 계획하고 있습니다.

## 핵심 내용
### 프로젝트 상태
Zeroth-01 Bot은 현재 공개 베타 단계로, 기본 운동, 시각, 음성 기능을 지원하지만 파괴적 변경이 있을 수 있습니다. 안정 버전 V1.0은 2025년 6월 출시 예정입니다.

### 핵심 구성 요소

#### KOS-ZBot - 운영 체제
KOS-ZBot은 로봇 운영 체제와 하드웨어 추상화 계층을 제공하며, 다음과 같은 핵심 모듈을 포함합니다:
- **하드웨어 드라이버**: Feetech 서보 제어, IMU 인터페이스 및 액추에이터 관리를 지원합니다.
- **Python API**: `kos_zbot` 패키지를 통해 고급 제어 인터페이스를 제공하여 개발자가 Python으로 쉽게 개발할 수 있습니다.
- **실시간 제어**: 저지연 서보 통신 및 센서 데이터 처리를 구현합니다.
- **CLI 도구**: 로봇 보정, 진단 및 시스템 구성을 위한 명령줄 도구를 제공합니다.

#### K-Sim Gym ZBot - 강화 학습 훈련
K-Sim Gym ZBot은 강화 학습 훈련 파이프라인을 제공하며, 핵심 기능은 다음과 같습니다:
- **훈련 파이프라인**: GPU 가속 RL 알고리즘 기반으로, 걷기 및 인간 동작 모방을 포함한 전신 제어 훈련을 지원합니다.
- **Sim-to-real**: 시스템 식별(SysID)을 통해 액추에이터를 보정하고, MJCF 및 URDF 모델을 사전 로드하여 시뮬레이션에서 실제 환경으로의 전이를 구현합니다.
- **모델 배포**: 훈련된 정책은 KOS를 통해 직접 내보내져 실제 로봇에서 실행할 수 있습니다.

### 빌드 가이드
공식 문서 [https://docs.kscale.dev/docs/zeroth-01](https://docs.kscale.dev/docs/zeroth-01)의 "Getting Started" 섹션을 참조하세요.

### 개발 시작 방법
Zeroth Bot은 오픈소스 커뮤니티에서 개발되며, GitHub에서 Pull Request 또는 Issue를 제출하는 것을 환영합니다. 커뮤니티 Discord에 참여하거나 문서를 확인하여 더 많은 지원을 받을 수 있습니다.

### 라이선스
이 프로젝트는 MIT 라이선스를 사용합니다.
