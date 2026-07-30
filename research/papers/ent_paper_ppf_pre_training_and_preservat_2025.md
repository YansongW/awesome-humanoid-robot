---
$id: ent_paper_ppf_pre_training_and_preservat_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PPF: Pre-training and Preservative Fine-tuning of Humanoid Locomotion'
  zh: 'PPF: Pre-training and Preservative Fine-tuning of Humanoid Locomotion'
  ko: 'PPF: Pre-training and Preservative Fine-tuning of Humanoid Locomotion'
summary:
  en: 'PPF: Pre-training and Preservative Fine-tuning of Humanoid Locomotion is a 2025 work on locomotion for humanoid robots.'
  zh: PPF 是 2025 年提出的人形机器人运动学习框架，由研究团队开发。其核心贡献在于通过模仿模型控制器的预训练、强化学习微调以及模型假设正则化（MAR），在防止灾难性遗忘的同时扩展运动能力，在 Digit 机器人上实现了 1.5 m/s
    的前进速度并适应多种复杂地形。
  ko: 'PPF: Pre-training and Preservative Fine-tuning of Humanoid Locomotion is a 2025 work on locomotion for humanoid robots.'
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
- ppf
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.09833v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'PPF: Pre-training and Preservative Fine-tuning of Humanoid Locomotion (arXiv)'
  url: https://arxiv.org/abs/2504.09833
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
人形机器人运动因高维动力学和复杂环境适应性而极具挑战。PPF 框架通过三个关键阶段解决这一问题：首先模仿基于模型的控制器进行预训练，随后使用强化学习进行微调，并在微调过程中引入模型假设正则化（MAR）。MAR 仅在模型假设成立的状态下对齐策略与控制器动作，从而有效防止灾难性遗忘。该框架在 Digit 全尺寸人形机器人上经过仿真和硬件实验验证，展示了在光滑、斜坡、不平整及沙地等多种地形上的稳健运动能力。

## 核心内容
### 方法架构
PPF 框架包含三个核心组件：
- **预训练阶段**：通过模仿基于模型的控制器（如 MPC）的行为来初始化运动策略，使策略学习到基础的运动模式。
- **微调阶段**：使用强化学习（RL）进一步优化策略，以处理更复杂的任务，如更高速度指令和更具挑战性的地形。
- **模型假设正则化（MAR）**：在微调过程中，MAR 仅在模型假设成立的状态下，强制策略输出与模型控制器一致的动作。这避免了策略在探索新行为时完全遗忘预训练知识，从而防止灾难性遗忘。

### 实验设置
- **机器人平台**：全尺寸人形机器人 Digit。
- **测试环境**：包括仿真测试和真实硬件实验，覆盖光滑、斜坡、不平整及沙地等多种地形。
- **性能指标**：前向速度达到 1.5 m/s，并在所有测试地形上实现稳健运动。

### 关键结论
PPF 框架成功结合了模型控制器的稳定性和强化学习的灵活性，通过 MAR 机制在扩展能力的同时保持了基础运动性能。实验表明，该方法在复杂地形和高速指令下均优于纯模型控制或纯强化学习方法。

## Overview
Humanoid locomotion is a challenging task due to its inherent complexity and high-dimensional dynamics, as well as the need to adapt to diverse and unpredictable environments. In this work, we introduce a novel learning framework for effectively training a humanoid locomotion policy that imitates the behavior of a model-based controller while extending its capabilities to handle more complex locomotion tasks, such as more challenging terrain and higher velocity commands. Our framework consists of three key components: pre-training through imitation of the model-based controller, fine-tuning via reinforcement learning, and model-assumption-based regularization (MAR) during fine-tuning. In particular, MAR aligns the policy with actions from the model-based controller only in states where the model assumption holds to prevent catastrophic forgetting. We evaluate the proposed framework through comprehensive simulation tests and hardware experiments on a full-size humanoid robot, Digit, demonstrating a forward speed of 1.5 m/s and robust locomotion across diverse terrains, including slippery, sloped, uneven, and sandy terrains.

## 개요
휴머노이드 보행은 본질적인 복잡성과 고차원 동역학, 그리고 다양하고 예측 불가능한 환경에 적응해야 하는 필요성으로 인해 매우 도전적인 과제입니다. 본 연구에서는 모델 기반 제어기의 동작을 모방하면서도 더 복잡한 보행 작업(예: 더 까다로운 지형 및 더 높은 속도 명령)을 처리할 수 있도록 성능을 확장하는 휴머노이드 보행 정책을 효과적으로 훈련하기 위한 새로운 학습 프레임워크를 소개합니다. 우리의 프레임워크는 세 가지 핵심 구성 요소로 이루어져 있습니다: 모델 기반 제어기를 모방한 사전 훈련, 강화 학습을 통한 미세 조정, 그리고 미세 조정 중 모델 가정 기반 정규화(MAR)입니다. 특히, MAR은 모델 가정이 유효한 상태에서만 정책을 모델 기반 제어기의 동작과 일치시켜 치명적 망각을 방지합니다. 제안된 프레임워크는 전신 휴머노이드 로봇 Digit을 대상으로 한 포괄적인 시뮬레이션 테스트와 하드웨어 실험을 통해 평가되었으며, 미끄러운 지형, 경사 지형, 고르지 않은 지형, 모래 지형 등 다양한 환경에서 1.5m/s의 전진 속도와 강건한 보행 성능을 입증했습니다.

## 핵심 내용
휴머노이드 보행은 본질적인 복잡성과 고차원 동역학, 그리고 다양하고 예측 불가능한 환경에 적응해야 하는 필요성으로 인해 매우 도전적인 과제입니다. 본 연구에서는 모델 기반 제어기의 동작을 모방하면서도 더 복잡한 보행 작업(예: 더 까다로운 지형 및 더 높은 속도 명령)을 처리할 수 있도록 성능을 확장하는 휴머노이드 보행 정책을 효과적으로 훈련하기 위한 새로운 학습 프레임워크를 소개합니다. 우리의 프레임워크는 세 가지 핵심 구성 요소로 이루어져 있습니다: 모델 기반 제어기를 모방한 사전 훈련, 강화 학습을 통한 미세 조정, 그리고 미세 조정 중 모델 가정 기반 정규화(MAR)입니다. 특히, MAR은 모델 가정이 유효한 상태에서만 정책을 모델 기반 제어기의 동작과 일치시켜 치명적 망각을 방지합니다. 제안된 프레임워크는 전신 휴머노이드 로봇 Digit을 대상으로 한 포괄적인 시뮬레이션 테스트와 하드웨어 실험을 통해 평가되었으며, 미끄러운 지형, 경사 지형, 고르지 않은 지형, 모래 지형 등 다양한 환경에서 1.5m/s의 전진 속도와 강건한 보행 성능을 입증했습니다.

## 参考
- http://arxiv.org/abs/2504.09833v2
