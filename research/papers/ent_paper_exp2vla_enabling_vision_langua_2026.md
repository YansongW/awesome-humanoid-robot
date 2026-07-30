---
$id: ent_paper_exp2vla_enabling_vision_langua_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Exp2VLA: Enabling Vision-Language-Action for Drone Navigation from Expert Demonstrations'
  zh: 'Exp2VLA: Enabling Vision-Language-Action for Drone Navigation from Expert Demonstrations'
  ko: 'Exp2VLA: Enabling Vision-Language-Action for Drone Navigation from Expert Demonstrations'
summary:
  en: 'arXiv:2607.03146v1 Announce Type: new Abstract: Vision-language-action (VLA) models open a new path toward intuitive
    robot control by directly linking perception, language, and action in a single end-to-end framework. Yet for UAVs, practical
    adoption remains difficult because existing solutions are either computationally heavy or insufficiently capable in complex
    environments. In this work, we propose a practical expert-distillation pipeline (Exp2VLA) for language-conditioned drone
    navigation. The core idea is to distill expert behavior, obtained from reinforcement learning, teleoperation, or other
    controllers, into training data that can be used to fine-tune compact VLA models. This allows existing control strategies
    to be transferred into a unified language-guided navigation model, reducing manual system integration and lowering the
    barrier for deploying new robot behaviors. Experiments in both sim-to-sim and simulation-in-the-loop settings across multi-object
    scenes show that the fine-tuned models can handle varied semantic commands and generalize to unseen target compositions.
    The proposed framework demonstrates how expert-policy distillation can help mechatronic systems move from specialized
    control modules toward more flexible and reusable robot intelligence.'
  zh: Exp2VLA 提出了一种专家蒸馏流水线，用于语言指令驱动的无人机导航。该方法将强化学习、遥操作等专家行为蒸馏为训练数据，微调紧凑的VLA模型，实现统一语言引导的导航控制。实验在多种场景下验证了模型对语义命令的泛化能力。
  ko: 'arXiv:2607.03146v1 Announce Type: new Abstract: Vision-language-action (VLA) models open a new path toward intuitive
    robot control by directly linking perception, language, and action in a single end-to-end framework. Yet for UAVs, practical
    adoption remains difficult because existing solutions are either computationally heavy or insufficiently capable in complex
    environments. In this work, we propose a practical expert-distillation pipeline (Exp2VLA) for language-conditioned drone
    navigation. The core idea is to distill expert behavior, obtained from reinforcement learning, teleoperation, or other
    controllers, into training data that can be used to fine-tune compact VLA models. This allows existing control strategies
    to be transferred into a unified language-guided navigation model, reducing manual system integration and lowering the
    barrier for deploying new robot behaviors. Experiments in both sim-to-sim and simulation-in-the-loop settings across multi-object
    scenes show that the fine-tuned models can handle varied semantic commands and generalize to unseen target compositions.
    The proposed framework demonstrates how expert-policy distillation can help mechatronic systems move from specialized
    control modules toward more flexible and reusable robot intelligence.'
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
- robotics
- exp2vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03146v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Exp2VLA: Enabling Vision-Language-Action for Drone Navigation from Expert Demonstrations (arXiv)'
  url: https://arxiv.org/abs/2607.03146
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Exp2VLA 的核心创新在于将专家策略蒸馏与VLA模型微调相结合，解决了现有无人机导航方案计算负担重或复杂环境适应性不足的问题。通过将强化学习、遥操作等不同来源的专家行为转化为训练数据，该方法能够将多种控制策略统一到单一的语言引导导航模型中，显著降低了系统集成难度和新行为部署门槛。在sim-to-sim和simulation-in-the-loop两种实验设置下，微调后的模型成功处理了多样化的语义命令，并能泛化到未见过的目标组合场景。

## 核心内容
### 方法概述
Exp2VLA 提出了一种实用的专家蒸馏流水线，旨在将专家行为转化为可用于微调紧凑型VLA模型的训练数据。专家行为可来自强化学习、遥操作或其他控制器。

### 核心架构
- **专家蒸馏**：核心思想是将现有控制策略（如强化学习策略、遥操作轨迹）蒸馏为训练数据，用于微调紧凑的VLA模型。
- **统一导航模型**：通过蒸馏，将多种控制策略统一到一个语言引导的导航模型中，减少手动系统集成，降低部署新机器人行为的门槛。

### 实验设置
- **实验环境**：在sim-to-sim和simulation-in-the-loop两种设置下进行，场景包含多目标物体。
- **评估指标**：模型处理多样化语义命令的能力，以及对未见目标组合的泛化能力。

### 关键结果
- 微调后的VLA模型能够成功处理多种语义命令，并在未见过的目标组合场景中展现出良好的泛化能力。
- 实验表明，专家策略蒸馏能够帮助机电系统从专用控制模块向更灵活、可复用的机器人智能转变。

## Overview
Vision-language-action (VLA) models open a new path toward intuitive robot control by directly linking perception, language, and action in a single end-to-end framework. Yet for UAVs, practical adoption remains difficult because existing solutions are either computationally heavy or insufficiently capable in complex environments. In this work, we propose a practical expert-distillation pipeline (Exp2VLA) for language-conditioned drone navigation. The core idea is to distill expert behavior, obtained from reinforcement learning, teleoperation, or other controllers, into training data that can be used to fine-tune compact VLA models. This allows existing control strategies to be transferred into a unified language-guided navigation model, reducing manual system integration and lowering the barrier for deploying new robot behaviors. Experiments in both sim-to-sim and simulation-in-the-loop settings across multi-object scenes show that the fine-tuned models can handle varied semantic commands and generalize to unseen target compositions. The proposed framework demonstrates how expert-policy distillation can help mechatronic systems move from specialized control modules toward more flexible and reusable robot intelligence.

## 개요
Vision-language-action (VLA) 모델은 인식, 언어, 행동을 단일 엔드투엔드 프레임워크로 직접 연결하여 직관적인 로봇 제어를 위한 새로운 경로를 열어줍니다. 그러나 UAV의 경우, 기존 솔루션이 계산적으로 무겁거나 복잡한 환경에서 충분한 성능을 발휘하지 못하기 때문에 실제 적용이 여전히 어렵습니다. 본 연구에서는 언어 조건 기반 드론 항법을 위한 실용적인 전문가 증류 파이프라인(Exp2VLA)을 제안합니다. 핵심 아이디어는 강화 학습, 원격 조작 또는 기타 컨트롤러에서 얻은 전문가 행동을 증류하여 소형 VLA 모델을 미세 조정하는 데 사용할 수 있는 훈련 데이터로 변환하는 것입니다. 이를 통해 기존 제어 전략을 통합된 언어 기반 항법 모델로 전환하여 수동 시스템 통합을 줄이고 새로운 로봇 행동 배포 장벽을 낮출 수 있습니다. 다중 객체 장면에서 시뮬레이션 간 및 시뮬레이션 인더루프 설정 모두에서 수행된 실험은 미세 조정된 모델이 다양한 의미 명령을 처리하고 보지 못한 대상 구성을 일반화할 수 있음을 보여줍니다. 제안된 프레임워크는 전문가 정책 증류가 메카트로닉스 시스템이 특수 제어 모듈에서 더 유연하고 재사용 가능한 로봇 지능으로 전환하는 데 어떻게 도움이 될 수 있는지 보여줍니다.

## 핵심 내용
Vision-language-action (VLA) 모델은 인식, 언어, 행동을 단일 엔드투엔드 프레임워크로 직접 연결하여 직관적인 로봇 제어를 위한 새로운 경로를 열어줍니다. 그러나 UAV의 경우, 기존 솔루션이 계산적으로 무겁거나 복잡한 환경에서 충분한 성능을 발휘하지 못하기 때문에 실제 적용이 여전히 어렵습니다. 본 연구에서는 언어 조건 기반 드론 항법을 위한 실용적인 전문가 증류 파이프라인(Exp2VLA)을 제안합니다. 핵심 아이디어는 강화 학습, 원격 조작 또는 기타 컨트롤러에서 얻은 전문가 행동을 증류하여 소형 VLA 모델을 미세 조정하는 데 사용할 수 있는 훈련 데이터로 변환하는 것입니다. 이를 통해 기존 제어 전략을 통합된 언어 기반 항법 모델로 전환하여 수동 시스템 통합을 줄이고 새로운 로봇 행동 배포 장벽을 낮출 수 있습니다. 다중 객체 장면에서 시뮬레이션 간 및 시뮬레이션 인더루프 설정 모두에서 수행된 실험은 미세 조정된 모델이 다양한 의미 명령을 처리하고 보지 못한 대상 구성을 일반화할 수 있음을 보여줍니다. 제안된 프레임워크는 전문가 정책 증류가 메카트로닉스 시스템이 특수 제어 모듈에서 더 유연하고 재사용 가능한 로봇 지능으로 전환하는 데 어떻게 도움이 될 수 있는지 보여줍니다.

## 参考
- http://arxiv.org/abs/2607.03146v1
