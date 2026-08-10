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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2310.03191v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (514 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2310.03191v1

## 개요
이 연구는 휴머노이드 로봇이 상자를 운반할 때 다양한 무게, 위치, 방향에 대응하기 위해 전신 협응이 필요하다는 문제를 해결하기 위해, sim-to-real 기반 강화 학습 방안을 제안한다. 연구진은 Digit 로봇을 위해 범용 상자 집기 및 운반 기술을 훈련시켰으며, 보상 함수는 상자와의 상호작용, 균형 유지, 보행 품질을 모두 고려한다. 이러한 기술을 조합함으로써, 시스템은 다양한 규격의 상자를 한 테이블에서 다른 테이블로 옮기는 전체 작업을 완료할 수 있다. 시뮬레이션의 정량적 결과 외에도, 이 방법은 실제 Digit 로봇으로의 전이에도 성공했다.

## 핵심 내용
### 방법 개요
- sim-to-real 강화 학습 프레임워크를 채택하여, 시뮬레이션 환경에서 Digit 로봇의 상자 운반 기술을 훈련한다.
- 보상 함수 설계는 세 가지 측면을 포함한다: 상자와의 기대 상호작용(예: 파지 안정성), 균형 유지(넘어짐 방지), 보행 품질(자연스러운 걷기).

### 기술 조합 및 작업
- 집기 및 운반 기술을 통합하여 완전한 운반 시스템으로 구성하며, 목표는 상자를 한 테이블에서 다른 테이블로 옮기는 것이다.
- 테스트 시나리오는 다양한 상자 크기, 무게(구체적 수치는 명시되지 않음) 및 초기 구성(위치, 방향)을 포함한다.

### 실험 및 전이
- 시뮬레이션에서 정량적 평가를 수행하여 다양한 조건에서 기술의 유효성을 검증한다.
- sim-to-real 전이에 성공: 시뮬레이션에서 훈련된 정책을 실제 Digit 로봇에 직접 배포하여 실제 운반 작업을 완료한다.
