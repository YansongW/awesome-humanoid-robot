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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.09833v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (683 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2504.09833v2

## 개요
휴머노이드 로봇 운동은 고차원 동역학과 복잡한 환경 적응성으로 인해 매우 도전적입니다. PPF 프레임워크는 세 가지 핵심 단계를 통해 이 문제를 해결합니다: 먼저 모델 기반 컨트롤러를 모방하여 사전 학습을 수행하고, 이후 강화 학습을 사용하여 미세 조정하며, 미세 조정 과정에서 모델 가정 정규화(MAR)를 도입합니다. MAR은 모델 가정이 성립하는 상태에서만 정책과 컨트롤러의 행동을 정렬하여 재앙적 망각을 효과적으로 방지합니다. 이 프레임워크는 Digit 전신 휴머노이드 로봇에서 시뮬레이션 및 하드웨어 실험을 통해 검증되었으며, 평지, 경사로, 울퉁불퉁한 지형 및 모래 지형 등 다양한 지형에서 견고한 운동 능력을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
PPF 프레임워크는 세 가지 핵심 구성 요소를 포함합니다:
- **사전 학습 단계**: 모델 기반 컨트롤러(예: MPC)의 행동을 모방하여 운동 정책을 초기화함으로써, 정책이 기본적인 운동 패턴을 학습하게 합니다.
- **미세 조정 단계**: 강화 학습(RL)을 사용하여 정책을 추가로 최적화하고, 더 높은 속도 명령 및 더 도전적인 지형과 같은 복잡한 작업을 처리합니다.
- **모델 가정 정규화(MAR)**: 미세 조정 과정에서 MAR은 모델 가정이 성립하는 상태에서만 정책 출력을 모델 컨트롤러의 행동과 일치하도록 강제합니다. 이는 정책이 새로운 행동을 탐색할 때 사전 학습 지식을 완전히 망각하는 것을 방지하여 재앙적 망각을 예방합니다.

### 실험 설정
- **로봇 플랫폼**: 전신 휴머노이드 로봇 Digit.
- **테스트 환경**: 시뮬레이션 테스트 및 실제 하드웨어 실험을 포함하며, 평지, 경사로, 울퉁불퉁한 지형 및 모래 지형 등 다양한 지형을 다룹니다.
- **성능 지표**: 전방 속도 1.5 m/s에 도달하며, 모든 테스트 지형에서 견고한 운동을 구현합니다.

### 핵심 결론
PPF 프레임워크는 모델 컨트롤러의 안정성과 강화 학습의 유연성을 성공적으로 결합했으며, MAR 메커니즘을 통해 능력을 확장하면서도 기본 운동 성능을 유지합니다. 실험 결과, 이 방법은 복잡한 지형과 고속 명령에서 순수 모델 제어 또는 순수 강화 학습 방법보다 우수함을 보여줍니다.
