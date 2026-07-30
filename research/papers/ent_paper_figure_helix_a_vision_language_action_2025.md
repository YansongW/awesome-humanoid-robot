---
$id: ent_paper_figure_helix_a_vision_language_action_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Helix: A vision-language-action model for generalist humanoid control'
  zh: Helix
  ko: 'Helix: A vision-language-action model for generalist humanoid control'
summary:
  en: 'Helix: A vision-language-action model for generalist humanoid control (Helix), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by FIGURE.'
  zh: Helix 是 FIGURE 公司于 2025 年提出的大型视觉-语言-动作模型，专为通用人形机器人操控设计。其核心贡献在于首次实现 VLA 模型对人形机器人全上半身（含手指）的高频连续控制，并首次支持双机器人协作完成未见物品的长时操控任务。
  ko: 'Helix: A vision-language-action model for generalist humanoid control (Helix), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by FIGURE.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- helix
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-15'
  confidence: medium
  notes: Summary backfilled by scripts/backfill_report_summaries.py from https://www.figure.ai/news/helix. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: website
  title: Helix source
  url: https://www.figure.ai/news/helix
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Helix 模型将感知、语言理解与学习控制统一于单一架构，旨在解决机器人领域的多项长期挑战。该模型实现了两项里程碑式突破：一是能够输出覆盖手腕、躯干、头部及每根手指的全上半身高频连续控制指令；二是首次让两个机器人同时运行同一 VLA 模型，协作完成从未见过物品的长时间操控任务。这些能力使 Helix 在通用人形机器人操控方面迈出了关键一步。

## 核心内容
### 模型定位与核心能力
Helix 是一个通用型 Vision-Language-Action (VLA) 模型，由 FIGURE 公司于 2025 年 2 月 20 日发布。它通过统一感知、语言理解与学习控制，旨在解决机器人操控中的泛化性与协调性问题。

### 关键技术突破
- **全上半身控制**：Helix 是首个能够输出高频连续控制信号，覆盖人形机器人整个上半身的 VLA 模型，控制范围包括手腕、躯干、头部以及每根独立手指。这使其能够执行精细的灵巧操作任务。
- **双机器人协作**：Helix 首次实现了同一 VLA 模型同时运行于两台机器人，使它们能够协作完成一项共享的长时操控任务，且任务中涉及的物品是机器人从未见过的。这验证了模型在零样本泛化与多智能体协调方面的能力。

### 实验设置与结论
虽然摘要与正文未提供具体的实验数据集、基准测试或量化数字，但 Helix 的发布强调了其在真实场景中的零样本泛化能力与多机器人协同效果。模型通过端到端学习，直接从视觉与语言输入映射到动作输出，跳过了传统机器人操控中繁琐的感知-规划-控制流水线。结论表明，Helix 为通用人形机器人的灵巧操控与协作任务提供了一种可行的统一框架。

## Overview
Figure was founded with the ambition to change the world. FIGURE 03 HELIX COMPANY NEWS CAREERS Helix: A Vision-Language-Action Model for Generalist Humanoid Control February 20, 2025 Introducing Helix We're introducing Helix, a generalist Vision-Language-Action (VLA) model that unifies perception, language understanding, and learned control to overcome multiple longstanding challenges in robotics. Helix is a series of firsts: Full-upper-body control : Helix is the first VLA to output high-rate continuous control of the entire humanoid upper body, including wrists, torso, head, and individual fingers. Multi-robot collaboration : Helix is the first VLA to operate simultaneously on two robots, enabling them to solve a shared, long-horizon manipulation task with items they have never seen before.

## 개요
Figure는 세상을 바꾸겠다는 포부로 설립되었습니다. FIGURE 03 HELIX COMPANY NEWS CAREERS Helix: A Vision-Language-Action Model for Generalist Humanoid Control 2025년 2월 20일 Helix 소개 저희는 Helix를 소개합니다. Helix는 지각, 언어 이해, 학습된 제어를 통합하여 로봇 공학의 여러 오랜 과제를 해결하는 범용 Vision-Language-Action(VLA) 모델입니다. Helix는 여러 최초의 기록을 세웠습니다: 전상체 제어 : Helix는 손목, 몸통, 머리, 개별 손가락을 포함한 휴머노이드 전상체의 고속 연속 제어를 출력하는 최초의 VLA입니다. 다중 로봇 협업 : Helix는 두 대의 로봇에서 동시에 작동하여, 이전에 본 적 없는 물체로 공유된 장기 조작 작업을 해결할 수 있는 최초의 VLA입니다.

## 핵심 내용
Figure는 세상을 바꾸겠다는 포부로 설립되었습니다. FIGURE 03 HELIX COMPANY NEWS CAREERS Helix: A Vision-Language-Action Model for Generalist Humanoid Control 2025년 2월 20일 Helix 소개 저희는 Helix를 소개합니다. Helix는 지각, 언어 이해, 학습된 제어를 통합하여 로봇 공학의 여러 오랜 과제를 해결하는 범용 Vision-Language-Action(VLA) 모델입니다. Helix는 여러 최초의 기록을 세웠습니다: 전상체 제어 : Helix는 손목, 몸통, 머리, 개별 손가락을 포함한 휴머노이드 전상체의 고속 연속 제어를 출력하는 최초의 VLA입니다. 다중 로봇 협업 : Helix는 두 대의 로봇에서 동시에 작동하여, 이전에 본 적 없는 물체로 공유된 장기 조작 작업을 해결할 수 있는 최초의 VLA입니다.

## 参考
- https://www.figure.ai/news/helix
