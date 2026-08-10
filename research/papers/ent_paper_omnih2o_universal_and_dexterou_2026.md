---
$id: ent_paper_omnih2o_universal_and_dexterou_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning'
  zh: 把遥操作升级成通用身体接口
  ko: 'OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning'
summary:
  en: 'OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning is a knowledge node related
    to paper in the humanoid robot value chain.'
  zh: OmniH2O 是一个基于学习的全身人形机器人遥操作与自主控制系统，由研究团队开发。其核心贡献在于通过运动学姿态作为通用控制接口，支持 VR 头显、语音指令和 RGB 摄像头等多种人类控制方式，并实现了从遥操作演示学习或与 GPT-4
    等前沿模型集成的全自主能力。该系统在多种真实世界全身任务中展现了通用性与灵巧性，并发布了首个包含六种日常任务的人形机器人全身控制数据集 OmniH2O-6。
  ko: 'OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning is a knowledge node related
    to paper in the humanoid robot value chain.'
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- data_collection
- human_demonstration
- human_video
- interaction_fidelity
- motion_retargeting
- teleoperation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.08858v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (845 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning (arXiv)'
  url: https://arxiv.org/abs/2406.08858
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 把遥操作升级成通用身体接口 project page
  url: https://omni.human2humanoid.com/
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
OmniH2O 系统通过将人体运动学姿态作为通用控制接口，实现了人类对全尺寸人形机器人的多种控制方式，包括 VR 头显实时遥操作、语音指令和 RGB 摄像头视觉控制。该系统不仅支持实时遥操作，还能通过从遥操作演示中学习或与 GPT-4 等模型集成实现全自主运行。在真实世界任务中，OmniH2O 展示了执行多种运动、物体操作和人际交互的通用性与灵巧性。研究团队开发了基于强化学习的 sim-to-real 流水线，通过大规模人体运动数据集的重定向与增强、模仿特权教师策略的稀疏传感器输入策略学习，以及增强鲁棒性与稳定性的奖励设计，实现了从仿真到真实世界的有效迁移。此外，团队还发布了首个包含六种日常任务的人形机器人全身控制数据集 OmniH2O-6。

## 核心内容
### 系统架构
- **通用控制接口**：采用人体运动学姿态作为统一控制信号，支持三种输入方式：
  - VR 头显实时遥操作
  - 语音指令控制
  - RGB 摄像头视觉控制
- **自主能力**：通过两种途径实现：
  - 从遥操作演示数据中学习
  - 与 GPT-4 等前沿模型集成

### 核心方法
- **Sim-to-Real 流水线**：
  - 大规模人体运动数据集的重定向与增强
  - 通过模仿特权教师策略，学习基于稀疏传感器输入的真实世界可部署策略
  - 设计特定奖励函数以增强机器人鲁棒性与稳定性

### 实验设置与结果
- **任务范围**：在真实世界中执行多种全身任务，包括：
  - 多项体育运动（如打球）
  - 物体移动与操作
  - 人际交互
- **数据集**：发布首个全身控制数据集 OmniH2O-6，包含六种日常任务（如抓取、放置等）
- **技能学习**：成功从遥操作数据集中学习人形机器人全身技能

### 关键数字
- 支持三种控制方式（VR、语音、RGB 摄像头）
- 数据集包含六种日常任务
- 系统在多种真实世界任务中验证了通用性与灵巧性

## Overview
We present OmniH2O (Omni Human-to-Humanoid), a learning-based system for whole-body humanoid teleoperation and autonomy. Using kinematic pose as a universal control interface, OmniH2O enables various ways for a human to control a full-sized humanoid with dexterous hands, including using real-time teleoperation through VR headset, verbal instruction, and RGB camera. OmniH2O also enables full autonomy by learning from teleoperated demonstrations or integrating with frontier models such as GPT-4. OmniH2O demonstrates versatility and dexterity in various real-world whole-body tasks through teleoperation or autonomy, such as playing multiple sports, moving and manipulating objects, and interacting with humans. We develop an RL-based sim-to-real pipeline, which involves large-scale retargeting and augmentation of human motion datasets, learning a real-world deployable policy with sparse sensor input by imitating a privileged teacher policy, and reward designs to enhance robustness and stability. We release the first humanoid whole-body control dataset, OmniH2O-6, containing six everyday tasks, and demonstrate humanoid whole-body skill learning from teleoperated datasets.

## 参考
- http://arxiv.org/abs/2406.08858v1

## 개요
OmniH2O 시스템은 인체 운동학적 자세를 범용 제어 인터페이스로 사용하여, VR 헤드셋 실시간 원격 조작, 음성 명령, RGB 카메라 시각 제어를 포함한 다양한 방식으로 인간이 전신 휴머노이드 로봇을 제어할 수 있게 합니다. 이 시스템은 실시간 원격 조작을 지원할 뿐만 아니라, 원격 조작 시연 데이터 학습 또는 GPT-4와 같은 모델 통합을 통해 완전 자율 실행도 가능합니다. 실제 세계 작업에서 OmniH2O는 다양한 운동, 물체 조작 및 인간-로봇 상호작용을 수행하는 범용성과 기민함을 보여줍니다. 연구팀은 강화 학습 기반의 sim-to-real 파이프라인을 개발하여, 대규모 인체 운동 데이터셋의 리타게팅 및 증강, 특권 교사 정책을 모방하는 희소 센서 입력 정책 학습, 그리고 견고성과 안정성을 향상시키는 보상 설계를 통해 시뮬레이션에서 실제 세계로의 효과적인 전이를 구현했습니다. 또한, 팀은 여섯 가지 일상 작업을 포함한 최초의 휴머노이드 로봇 전신 제어 데이터셋인 OmniH2O-6을 공개했습니다.

## 핵심 내용
### 시스템 아키텍처
- **범용 제어 인터페이스**: 인체 운동학적 자세를 통합 제어 신호로 사용하며, 세 가지 입력 방식을 지원합니다:
  - VR 헤드셋 실시간 원격 조작
  - 음성 명령 제어
  - RGB 카메라 시각 제어
- **자율 능력**: 두 가지 경로를 통해 구현됩니다:
  - 원격 조작 시연 데이터 학습
  - GPT-4와 같은 최첨단 모델 통합

### 핵심 방법
- **Sim-to-Real 파이프라인**:
  - 대규모 인체 운동 데이터셋의 리타게팅 및 증강
  - 특권 교사 정책을 모방하여 희소 센서 입력 기반의 실제 세계 배포 가능 정책 학습
  - 로봇 견고성과 안정성을 강화하기 위한 특정 보상 함수 설계

### 실험 설정 및 결과
- **작업 범위**: 실제 세계에서 다양한 전신 작업을 수행하며, 다음을 포함합니다:
  - 여러 스포츠 활동 (예: 공 치기)
  - 물체 이동 및 조작
  - 인간-로봇 상호작용
- **데이터셋**: 여섯 가지 일상 작업(예: 잡기, 놓기 등)을 포함한 최초의 전신 제어 데이터셋 OmniH2O-6 공개
- **기술 학습**: 원격 조작 데이터셋에서 휴머노이드 로봇 전신 기술 학습에 성공

### 주요 수치
- 세 가지 제어 방식 지원 (VR, 음성, RGB 카메라)
- 데이터셋은 여섯 가지 일상 작업 포함
- 시스템은 다양한 실제 세계 작업에서 범용성과 기민함을 검증함
