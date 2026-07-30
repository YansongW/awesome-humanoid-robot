---
$id: ent_paper_sim_to_real_learning_for_human_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Sim-to-Real Learning for Humanoid Box Loco-Manipulation
  zh: Sim-to-Real Learning for Humanoid Box Loco-Manipulation
  ko: Sim-to-Real Learning for Humanoid Box Loco-Manipulation
summary:
  en: Sim-to-Real Learning for Humanoid Box Loco-Manipulation is a 2023 work on loco-manipulation and whole-body-control for
    humanoid robots.
  zh: 本文提出一种基于强化学习的 sim-to-real 方法，用于双足人形机器人 Digit 的箱子搬运与全身协调控制。核心贡献在于设计奖励函数以平衡抓取、平衡与步态质量，并成功将学习技能迁移至真实机器人，实现不同尺寸、重量和初始位置箱子的跨桌搬运。
  ko: Sim-to-Real Learning for Humanoid Box Loco-Manipulation is a 2023 work on loco-manipulation and whole-body-control for
    humanoid robots.
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
- loco_manipulation
- sim_to_real_learning_for_human
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2310.03191v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Sim-to-Real Learning for Humanoid Box Loco-Manipulation (arXiv)
  url: https://arxiv.org/abs/2310.03191
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
这项工作针对人形机器人搬运箱子时需全身协调以应对不同重量、位置和朝向的挑战，提出基于 sim-to-real 的强化学习方案。研究者为 Digit 机器人训练了通用的箱子拾取与携带技能，奖励函数兼顾与箱子的交互、平衡维持及步态质量。通过组合这些技能，系统能完成将多种规格箱子从一张桌子移至另一张桌子的完整任务。除仿真定量结果外，该方法还成功实现了向真实 Digit 机器人的迁移。

## 核心内容
### 方法概述
- 采用 sim-to-real 强化学习框架，在仿真环境中训练 Digit 机器人的箱子搬运技能。
- 奖励函数设计包含三方面：与箱子的期望交互（如抓取稳定性）、平衡维持（防止摔倒）以及步态质量（自然行走）。

### 技能组合与任务
- 将拾取与携带技能整合为完整搬运系统，目标是将箱子从一张桌子移动到另一张桌子。
- 测试场景涵盖多种箱子尺寸、重量（未明确具体数值）及初始配置（位置、朝向）。

### 实验与迁移
- 在仿真中进行了定量评估，验证技能在不同条件下的有效性。
- 成功实现 sim-to-real 迁移：将仿真训练的策略直接部署到真实 Digit 机器人上，完成实际搬运任务。

## Overview
In this work we propose a learning-based approach to box loco-manipulation for a humanoid robot. This is a particularly challenging problem due to the need for whole-body coordination in order to lift boxes of varying weight, position, and orientation while maintaining balance. To address this challenge, we present a sim-to-real reinforcement learning approach for training general box pickup and carrying skills for the bipedal robot Digit. Our reward functions are designed to produce the desired interactions with the box while also valuing balance and gait quality. We combine the learned skills into a full system for box loco-manipulation to achieve the task of moving boxes from one table to another with a variety of sizes, weights, and initial configurations. In addition to quantitative simulation results, we demonstrate successful sim-to-real transfer on the humanoid r

## 개요
본 연구에서는 휴머노이드 로봇의 박스 이동 조작을 위한 학습 기반 접근법을 제안합니다. 이는 다양한 무게, 위치, 방향의 박스를 들어 올리면서 균형을 유지하기 위해 전신 협응이 필요하다는 점에서 특히 어려운 문제입니다. 이러한 과제를 해결하기 위해, 우리는 이족 보행 로봇 Digit을 위한 일반적인 박스 집기 및 운반 기술을 훈련하는 시뮬레이션-실제 강화 학습 접근법을 제시합니다. 보상 함수는 박스와의 원하는 상호작용을 유도하면서 균형과 보행 품질을 중시하도록 설계되었습니다. 학습된 기술을 결합하여 다양한 크기, 무게, 초기 구성의 박스를 한 테이블에서 다른 테이블로 옮기는 작업을 수행하는 완전한 박스 이동 조작 시스템을 구축합니다. 정량적 시뮬레이션 결과 외에도, 휴머노이드 로봇에서 성공적인 시뮬레이션-실제 전이를 시연합니다.

## 핵심 내용
본 연구에서는 휴머노이드 로봇의 박스 이동 조작을 위한 학습 기반 접근법을 제안합니다. 이는 다양한 무게, 위치, 방향의 박스를 들어 올리면서 균형을 유지하기 위해 전신 협응이 필요하다는 점에서 특히 어려운 문제입니다. 이러한 과제를 해결하기 위해, 우리는 이족 보행 로봇 Digit을 위한 일반적인 박스 집기 및 운반 기술을 훈련하는 시뮬레이션-실제 강화 학습 접근법을 제시합니다. 보상 함수는 박스와의 원하는 상호작용을 유도하면서 균형과 보행 품질을 중시하도록 설계되었습니다. 학습된 기술을 결합하여 다양한 크기, 무게, 초기 구성의 박스를 한 테이블에서 다른 테이블로 옮기는 작업을 수행하는 완전한 박스 이동 조작 시스템을 구축합니다. 정량적 시뮬레이션 결과 외에도, 휴머노이드 로봇에서 성공적인 시뮬레이션-실제 전이를 시연합니다.

## 参考
- http://arxiv.org/abs/2310.03191v1
