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
  notes: 'Summary backfilled by scripts/backfill_report_summaries.py from https://www.figure.ai/news/helix. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10: ko
    body retranslated from zh deep-read (713 chars, DeepSeek).'
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

## 参考
- https://www.figure.ai/news/helix

## 개요
Helix 모델은 인식, 언어 이해 및 학습 제어를 단일 아키텍처로 통합하여 로봇 공학의 여러 장기적 과제를 해결하는 것을 목표로 합니다. 이 모델은 두 가지 이정표적 돌파구를 달성했습니다: 첫째, 손목, 몸통, 머리 및 각 손가락을 포함한 전신 상반부의 고주파 연속 제어 명령을 출력할 수 있으며, 둘째, 처음으로 두 로봇이 동시에 동일한 VLA 모델을 실행하여 본 적 없는 물체를 협력적으로 장시간 조작하는 작업을 완료합니다. 이러한 능력은 Helix를 범용 휴머노이드 로봇 조작 분야에서 핵심적인 진전으로 이끌었습니다.

## 핵심 내용
### 모델 포지셔닝 및 핵심 능력
Helix는 FIGURE 사가 2025년 2월 20일에 발표한 범용 Vision-Language-Action (VLA) 모델입니다. 이는 인식, 언어 이해 및 학습 제어를 통합하여 로봇 조작에서의 일반화 및 조정 문제를 해결하는 것을 목표로 합니다.

### 핵심 기술 돌파구
- **전신 상반부 제어**: Helix는 휴머노이드 로봇의 전체 상반부를 포함하는 고주파 연속 제어 신호를 출력할 수 있는 최초의 VLA 모델로, 제어 범위에는 손목, 몸통, 머리 및 각 개별 손가락이 포함됩니다. 이를 통해 정밀한 손재주 조작 작업을 수행할 수 있습니다.
- **이중 로봇 협력**: Helix는 처음으로 동일한 VLA 모델이 두 로봇에서 동시에 실행되도록 구현하여, 로봇들이 공유된 장시간 조작 작업을 협력적으로 완료할 수 있게 합니다. 이때 작업에 포함된 물체는 로봇이 본 적 없는 것입니다. 이는 모델의 제로샷 일반화 및 다중 에이전트 조정 능력을 검증합니다.

### 실험 설정 및 결론
요약 및 본문에서 구체적인 실험 데이터셋, 벤치마크 또는 정량적 수치를 제공하지는 않았지만, Helix의 발표는 실제 환경에서의 제로샷 일반화 능력과 다중 로봇 협력 효과를 강조합니다. 모델은 엔드투엔드 학습을 통해 시각 및 언어 입력에서 직접 동작 출력으로 매핑하며, 전통적인 로봇 조작의 번거로운 인식-계획-제어 파이프라인을 건너뜁니다. 결론은 Helix가 범용 휴머노이드 로봇의 손재주 조작 및 협력 작업을 위한 실행 가능한 통합 프레임워크를 제공한다는 것을 보여줍니다.
