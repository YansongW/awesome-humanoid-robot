---
$id: ent_paper_closd_closing_the_loop_between_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CLoSD: Closing the Loop between Simulation and Diffusion for multi-task character control'
  zh: 'CLoSD: Closing the Loop between Simulation and Diffusion for multi-task character control'
  ko: 'CLoSD: Closing the Loop between Simulation and Diffusion for multi-task character control'
summary:
  en: 'CLoSD: Closing the Loop between Simulation and Diffusion for multi-task character control is a 2024 work on physics-based
    character animation for humanoid robots.'
  zh: CLoSD 是 2024 年提出的一种结合运动扩散模型与强化学习的物理仿真角色控制方法。其核心贡献在于利用扩散模型作为在线通用规划器，为鲁棒的强化学习控制器提供实时运动计划，从而在多种任务（如导航、击打物体、坐下与起立）中实现文本驱动的多任务角色控制。
  ko: 'CLoSD: Closing the Loop between Simulation and Diffusion for multi-task character control is a 2024 work on physics-based
    character animation for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- closd
- humanoid
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.03441v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (639 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'CLoSD: Closing the Loop between Simulation and Diffusion for multi-task character control (arXiv)'
  url: https://arxiv.org/abs/2410.03441
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'CLoSD: Closing the Loop between Simulation and Diffusion for multi-task character control project page'
  url: https://guytevet.github.io/CLoSD-page/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
CLoSD 通过闭环交互将扩散规划器（DiP）与跟踪控制器相结合。DiP 是一种快速自回归扩散模型，能够根据文本提示和目标位置生成运动计划；控制器则是一个简单且鲁棒的运动模仿器，持续接收 DiP 的计划并反馈环境信息。该方法能够无缝执行一系列不同任务，包括导航到目标位置、按文本提示用手或脚击打物体、坐下以及起立。

## 核心内容
### 方法架构
CLoSD 由两个核心模块构成：
- **扩散规划器（DiP）**：一种快速响应的自回归扩散模型，受文本提示和目标位置控制，负责生成运动计划。
- **跟踪控制器**：一个简单且鲁棒的运动模仿器，持续接收 DiP 的运动计划，并根据环境反馈进行调整。

### 闭环交互
两个模块之间维持闭环交互：DiP 作为通用规划器，为控制器提供实时运动计划；控制器则向 DiP 反馈环境状态，确保运动计划的物理合理性。

### 实验设置与关键数字
- **任务多样性**：CLoSD 能够无缝执行导航、击打物体（手或脚）、坐下、起立等多种任务。
- **控制方式**：所有任务均通过文本提示驱动，无需手动切换策略。
- **性能表现**：实验表明，CLoSD 在物理仿真环境中实现了高鲁棒性和任务完成率。

### 结论
CLoSD 成功结合了运动扩散模型的多样性与强化学习的物理合理性，为多任务角色控制提供了一种高效且灵活的解决方案。项目页面：https://guytevet.github.io/CLoSD-page/

## Overview
Motion diffusion models and Reinforcement Learning (RL) based control for physics-based simulations have complementary strengths for human motion generation. The former is capable of generating a wide variety of motions, adhering to intuitive control such as text, while the latter offers physically plausible motion and direct interaction with the environment. In this work, we present a method that combines their respective strengths. CLoSD is a text-driven RL physics-based controller, guided by diffusion generation for various tasks. Our key insight is that motion diffusion can serve as an on-the-fly universal planner for a robust RL controller. To this end, CLoSD maintains a closed-loop interaction between two modules -- a Diffusion Planner (DiP), and a tracking controller. DiP is a fast-responding autoregressive diffusion model, controlled by textual prompts and target locations, and the controller is a simple and robust motion imitator that continuously receives motion plans from DiP and provides feedback from the environment. CLoSD is capable of seamlessly performing a sequence of different tasks, including navigation to a goal location, striking an object with a hand or foot as specified in a text prompt, sitting down, and getting up. https://guytevet.github.io/CLoSD-page/

## 参考
- http://arxiv.org/abs/2410.03441v1

## 개요
CLoSD는 폐쇄 루프 상호작용을 통해 확산 플래너(DiP)와 추적 컨트롤러를 결합합니다. DiP는 텍스트 프롬프트와 목표 위치에 따라 운동 계획을 생성하는 빠른 자기회귀 확산 모델이며, 컨트롤러는 DiP의 계획을 지속적으로 수신하고 환경 정보를 피드백하는 간단하고 견고한 운동 모방기입니다. 이 방법은 목표 위치로 내비게이션, 텍스트 프롬프트에 따라 손이나 발로 물체를 타격, 앉기, 일어서기 등 일련의 다양한 작업을 원활하게 수행할 수 있습니다.

## 핵심 내용
### 방법 아키텍처
CLoSD는 두 가지 핵심 모듈로 구성됩니다:
- **확산 플래너(DiP)**: 텍스트 프롬프트와 목표 위치에 의해 제어되는 빠른 응답 자기회귀 확산 모델로, 운동 계획 생성을 담당합니다.
- **추적 컨트롤러**: DiP의 운동 계획을 지속적으로 수신하고 환경 피드백에 따라 조정하는 간단하고 견고한 운동 모방기입니다.

### 폐쇄 루프 상호작용
두 모듈 간에는 폐쇄 루프 상호작용이 유지됩니다: DiP는 범용 플래너로서 컨트롤러에 실시간 운동 계획을 제공하며, 컨트롤러는 환경 상태를 DiP에 피드백하여 운동 계획의 물리적 타당성을 보장합니다.

### 실험 설정 및 핵심 수치
- **작업 다양성**: CLoSD는 내비게이션, 물체 타격(손 또는 발), 앉기, 일어서기 등 다양한 작업을 원활하게 수행할 수 있습니다.
- **제어 방식**: 모든 작업은 텍스트 프롬프트로 구동되며, 수동으로 전략을 전환할 필요가 없습니다.
- **성능 표현**: 실험에 따르면 CLoSD는 물리 시뮬레이션 환경에서 높은 견고성과 작업 완료율을 달성했습니다.

### 결론
CLoSD는 운동 확산 모델의 다양성과 강화 학습의 물리적 타당성을 성공적으로 결합하여, 다중 작업 캐릭터 제어를 위한 효율적이고 유연한 솔루션을 제공합니다. 프로젝트 페이지: https://guytevet.github.io/CLoSD-page/
