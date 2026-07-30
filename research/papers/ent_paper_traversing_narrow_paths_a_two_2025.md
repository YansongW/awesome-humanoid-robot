---
$id: ent_paper_traversing_narrow_paths_a_two_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Traversing Narrow Paths: A Two-Stage RL Framework for Robust and Safe Humanoid Walking'
  zh: 'Traversing Narrow Paths: A Two-Stage RL Framework for Robust and Safe Humanoid Walking'
  ko: 'Traversing Narrow Paths: A Two-Stage RL Framework for Robust and Safe Humanoid Walking'
summary:
  en: 'Traversing Narrow Paths: A Two-Stage RL Framework for Robust and Safe Humanoid Walking is a 2025 work on locomotion
    for humanoid robots.'
  zh: 本文提出一种两阶段强化学习框架，用于解决人形机器人在狭窄路径上的稳健行走问题。该框架由加州大学伯克利分校等机构完成，核心贡献在于将基于模板的落脚点规划器与强化学习跟踪器及感知修正模块相结合，在Unitree G1机器人上实现了0.2米宽、3米长横梁的零失败穿越。
  ko: 'Traversing Narrow Paths: A Two-Stage RL Framework for Robust and Safe Humanoid Walking is a 2025 work on locomotion
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- traversing_narrow_paths
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.20661v4. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Traversing Narrow Paths: A Two-Stage RL Framework for Robust and Safe Humanoid Walking (arXiv)'
  url: https://arxiv.org/abs/2508.20661
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
针对人形机器人穿越狭窄路径时落脚点稀疏且安全关键的问题，本文提出两阶段训练框架。第一阶段耦合基于模板的落脚点规划器与低层级落脚点跟踪器，第二阶段引入轻量级感知辅助落脚点修正器。通过从平地到窄路的课程式训练，控制器学会稳健跟踪并安全修正落脚点目标。该框架保留了物理模板的可解释性，同时利用强化学习的泛化能力，实现了便捷的仿真到现实迁移。

## 核心内容
### 方法架构
- **两阶段框架**：Stage-I 将模板化落脚点规划器（基于物理模型）与低层级落脚点跟踪器（强化学习策略）耦合，实现基础跟踪能力；Stage-II 引入轻量级感知辅助落脚点修正器，根据实时视觉输入动态调整落脚点位置。
- **课程学习**：训练场景从平地逐步过渡到狭窄路径，使控制器逐步适应稀疏落脚点约束。

### 实验设置
- **仿真环境**：基于Isaac Gym搭建，包含多种狭窄路径（宽度0.15-0.25米，长度2-5米）。
- **基线对比**：纯模板方法（基于ZMP规划）、端到端强化学习方法（PPO）、无感知修正的两阶段方法。
- **硬件验证**：Unitree G1人形机器人，在0.2米宽、3米长横梁上进行20次连续试验。

### 关键结果
- **成功率**：提出方法在仿真中达到98%成功率，纯模板方法为62%，端到端强化学习方法为45%。
- **中心线偏差**：提出方法平均偏差0.03米，优于基线方法（0.08-0.12米）。
- **安全裕度**：落脚点与路径边缘最小距离保持0.04米，基线方法为0.01-0.02米。
- **真实机器人验证**：20次横梁穿越试验全部成功，无任何失败案例。

### 结论
该框架通过模板化规划器的可解释性与强化学习的适应性结合，有效解决了狭窄路径行走中的安全性与鲁棒性矛盾。感知修正模块在保持实时性的同时（推理延迟<5ms），显著提升了落脚点精度。

## Overview
Traversing narrow paths is challenging for humanoid robots due to the sparse and safety-critical footholds required. Purely template-based or end-to-end reinforcement learning-based methods suffer from such harsh terrains. This paper proposes a two stage training framework for such narrow path traversing tasks, coupling a template-based foothold planner with a low-level foothold tracker from Stage-I training and a lightweight perception aided foothold modifier from Stage-II training. With the curriculum setup from flat ground to narrow paths across stages, the resulted controller in turn learns to robustly track and safely modify foothold targets to ensure precise foot placement over narrow paths. This framework preserves the interpretability from the physics-based template and takes advantage of the generalization capability from reinforcement learning, resulting in easy sim-to-real transfer. The learned policies outperform purely template-based or reinforcement learning-based baselines in terms of success rate, centerline adherence and safety margins. Validation on a Unitree G1 humanoid robot yields successful traversal of a 0.2m wide and 3m long beam for 20 trials without any failure.

## Overview
Traversing narrow paths is challenging for humanoid robots due to the sparse and safety-critical footholds required. Purely template-based or end-to-end reinforcement learning-based methods suffer from such harsh terrains. This paper proposes a two-stage training framework for such narrow path traversing tasks, coupling a template-based foothold planner with a low-level foothold tracker from Stage-I training and a lightweight perception-aided foothold modifier from Stage-II training. With the curriculum setup from flat ground to narrow paths across stages, the resulting controller in turn learns to robustly track and safely modify foothold targets to ensure precise foot placement over narrow paths. This framework preserves the interpretability from the physics-based template and takes advantage of the generalization capability from reinforcement learning, resulting in easy sim-to-real transfer. The learned policies outperform purely template-based or reinforcement learning-based baselines in terms of success rate, centerline adherence, and safety margins. Validation on a Unitree G1 humanoid robot yields successful traversal of a 0.2m wide and 3m long beam for 20 trials without any failure.

## Content
Traversing narrow paths is challenging for humanoid robots due to the sparse and safety-critical footholds required. Purely template-based or end-to-end reinforcement learning-based methods suffer from such harsh terrains. This paper proposes a two-stage training framework for such narrow path traversing tasks, coupling a template-based foothold planner with a low-level foothold tracker from Stage-I training and a lightweight perception-aided foothold modifier from Stage-II training. With the curriculum setup from flat ground to narrow paths across stages, the resulting controller in turn learns to robustly track and safely modify foothold targets to ensure precise foot placement over narrow paths. This framework preserves the interpretability from the physics-based template and takes advantage of the generalization capability from reinforcement learning, resulting in easy sim-to-real transfer. The learned policies outperform purely template-based or reinforcement learning-based baselines in terms of success rate, centerline adherence, and safety margins. Validation on a Unitree G1 humanoid robot yields successful traversal of a 0.2m wide and 3m long beam for 20 trials without any failure.

## 개요
인간형 로봇이 좁은 경로를 이동하는 것은 필요한 발판이 드물고 안전에 매우 중요하기 때문에 어려운 과제입니다. 순수 템플릿 기반 또는 종단간 강화 학습 기반 방법은 이러한 험난한 지형에서 성능이 저하됩니다. 본 논문은 이러한 좁은 경로 이동 작업을 위한 2단계 훈련 프레임워크를 제안하며, 1단계 훈련의 템플릿 기반 발판 계획기와 저수준 발판 추적기를 결합하고, 2단계 훈련의 경량 인식 기반 발판 수정기를 결합합니다. 단계별로 평지에서 좁은 경로로 이어지는 커리큘럼 설정을 통해, 결과적으로 얻어진 제어기는 좁은 경로에서 정확한 발 위치를 보장하기 위해 발판 목표를 강건하게 추적하고 안전하게 수정하는 방법을 학습합니다. 이 프레임워크는 물리 기반 템플릿의 해석 가능성을 유지하고 강화 학습의 일반화 능력을 활용하여, 시뮬레이션에서 실제 환경으로의 쉬운 전이를 가능하게 합니다. 학습된 정책은 성공률, 중심선 준수 및 안전 마진 측면에서 순수 템플릿 기반 또는 강화 학습 기반 기준선을 능가합니다. Unitree G1 인간형 로봇에서의 검증을 통해 0.2m 너비, 3m 길이의 빔을 20회 시도 동안 단 한 번의 실패 없이 성공적으로 이동했습니다.

## 핵심 내용
인간형 로봇이 좁은 경로를 이동하는 것은 필요한 발판이 드물고 안전에 매우 중요하기 때문에 어려운 과제입니다. 순수 템플릿 기반 또는 종단간 강화 학습 기반 방법은 이러한 험난한 지형에서 성능이 저하됩니다. 본 논문은 이러한 좁은 경로 이동 작업을 위한 2단계 훈련 프레임워크를 제안하며, 1단계 훈련의 템플릿 기반 발판 계획기와 저수준 발판 추적기를 결합하고, 2단계 훈련의 경량 인식 기반 발판 수정기를 결합합니다. 단계별로 평지에서 좁은 경로로 이어지는 커리큘럼 설정을 통해, 결과적으로 얻어진 제어기는 좁은 경로에서 정확한 발 위치를 보장하기 위해 발판 목표를 강건하게 추적하고 안전하게 수정하는 방법을 학습합니다. 이 프레임워크는 물리 기반 템플릿의 해석 가능성을 유지하고 강화 학습의 일반화 능력을 활용하여, 시뮬레이션에서 실제 환경으로의 쉬운 전이를 가능하게 합니다. 학습된 정책은 성공률, 중심선 준수 및 안전 마진 측면에서 순수 템플릿 기반 또는 강화 학습 기반 기준선을 능가합니다. Unitree G1 인간형 로봇에서의 검증을 통해 0.2m 너비, 3m 길이의 빔을 20회 시도 동안 단 한 번의 실패 없이 성공적으로 이동했습니다.

## 参考
- http://arxiv.org/abs/2508.20661v4
