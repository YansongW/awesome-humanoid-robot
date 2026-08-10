---
$id: ent_paper_guided_action_flow_q_guided_in_2092
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Guided Action Flow: Q-Guided Inference for Flow-Matching Vision-Language-Action Policies'
  zh: 'Guided Action Flow: Q-Guided Inference for Flow-Matching Vision-Language-Action Policies'
  ko: 'Guided Action Flow: Q-Guided Inference for Flow-Matching Vision-Language-Action Policies'
summary:
  en: 'arXiv:2607.02092v2 Announce Type: replace Abstract: Flow-matching vision-language-action policies generate robot action
    chunks through an iterative transport process, creating an opportunity for test-time guidance without retraining the base
    policy. We study this opportunity in Guided Action Flow, an inference-time framework that keeps a pretrained SmolVLA policy
    frozen and uses a learned action-chunk critic to guide its reverse-time flow sampler. The critic is trained from real
    success and failure rollouts, can condition on task-description features from the frozen SmolVLA language pathway, and
    is used only through action gradients during sampling. We evaluate the approach on LIBERO manipulation tasks. A single-task
    critic improves success from 68.0% to 82.0% on one seed window and from 82.0% to 86.0% on another. A multi-family task-description
    critic improves validation success from 46.0% to 56.0%, while the locked held-out test gain is positive but modest, from
    65.0% to 67.5%. These results support the feasibility of Q-guided inference for frozen flow-matching VLA policies, while
    showing that critic generalization and uncertainty-aware guidance remain the central bottlenecks.'
  zh: Guided Action Flow 是一种面向流匹配视觉-语言-动作策略的推理时引导框架，由研究者提出。其核心贡献在于：保持预训练 SmolVLA 策略冻结，通过一个从真实成功/失败轨迹中学习的动作块评判器，在反向流采样过程中提供梯度引导。在
    LIBERO 操作任务上，单任务评判器将成功率从 68.0% 提升至 82.0%，多任务评判器在验证集上从 46.0% 提升至 56.0%。
  ko: 'arXiv:2607.02092v2 Announce Type: replace Abstract: Flow-matching vision-language-action policies generate robot action
    chunks through an iterative transport process, creating an opportunity for test-time guidance without retraining the base
    policy. We study this opportunity in Guided Action Flow, an inference-time framework that keeps a pretrained SmolVLA policy
    frozen and uses a learned action-chunk critic to guide its reverse-time flow sampler. The critic is trained from real
    success and failure rollouts, can condition on task-description features from the frozen SmolVLA language pathway, and
    is used only through action gradients during sampling. We evaluate the approach on LIBERO manipulation tasks. A single-task
    critic improves success from 68.0% to 82.0% on one seed window and from 82.0% to 86.0% on another. A multi-family task-description
    critic improves validation success from 46.0% to 56.0%, while the locked held-out test gain is positive but modest, from
    65.0% to 67.5%. These results support the feasibility of Q-guided inference for frozen flow-matching VLA policies, while
    showing that critic generalization and uncertainty-aware guidance remain the central bottlenecks.'
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
- guided_action_flow
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.02092v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (856 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Guided Action Flow: Q-Guided Inference for Flow-Matching Vision-Language-Action Policies (arXiv)'
  url: https://arxiv.org/abs/2607.02092
  date: '2092'
  accessed_at: '2026-07-08'
---
## 概述
Guided Action Flow 是一种无需重新训练基础策略的推理时引导方法，专门针对流匹配视觉-语言-动作策略设计。该方法保持预训练的 SmolVLA 策略完全冻结，仅通过一个额外学习的动作块评判器来指导反向流采样过程。该评判器从真实的成功和失败轨迹中训练，能够利用 SmolVLA 语言通路中的任务描述特征，并在采样过程中仅通过动作梯度发挥作用。在 LIBERO 操作任务上的实验表明，单任务评判器能显著提升成功率，而多任务评判器在验证集上也有明显改善，但在测试集上的提升较为有限。

## 核心内容
### 方法概述
Guided Action Flow 的核心思想是在流匹配视觉-语言-动作策略的推理阶段引入引导机制，而无需修改或重新训练基础策略。具体而言：
- **基础策略**：使用预训练的 SmolVLA 策略，该策略通过流匹配过程生成机器人动作块。
- **评判器**：学习一个动作块评判器，该评判器从真实的成功和失败轨迹中训练，能够利用 SmolVLA 语言通路中的任务描述特征。
- **引导机制**：在反向流采样过程中，评判器通过动作梯度提供引导，从而优化生成的动作块。

### 实验设置
- **任务**：在 LIBERO 操作任务上进行评估。
- **评判器类型**：
  - **单任务评判器**：针对特定任务训练，在单个种子窗口上将成功率从 68.0% 提升至 82.0%，在另一个种子窗口上从 82.0% 提升至 86.0%。
  - **多任务评判器**：基于多家族任务描述特征训练，在验证集上将成功率从 46.0% 提升至 56.0%，在测试集上从 65.0% 提升至 67.5%。

### 关键结论
- **可行性验证**：实验结果表明，Q 引导推理对于冻结的流匹配 VLA 策略是可行的，能够在不重新训练基础策略的情况下提升性能。
- **主要瓶颈**：评判器的泛化能力和不确定性感知引导仍然是当前方法的核心限制，导致多任务场景下的测试集提升较为有限。

## Overview
Flow-matching vision-language-action policies generate robot action chunks through an iterative transport process, creating an opportunity for test-time guidance without retraining the base policy. We study this opportunity in Guided Action Flow, an inference-time framework that keeps a pretrained SmolVLA policy frozen and uses a learned action-chunk critic to guide its reverse-time flow sampler. The critic is trained from real success and failure rollouts, can condition on task-description features from the frozen SmolVLA language pathway, and is used only through action gradients during sampling. We evaluate the approach on LIBERO manipulation tasks. A single-task critic improves success from 68.0% to 82.0% on one seed window and from 82.0% to 86.0% on another. A multi-family task-description critic improves validation success from 46.0% to 56.0%, while the locked held-out test gain is positive but modest, from 65.0% to 67.5%. These results support the feasibility of Q-guided inference for frozen flow-matching VLA policies, while showing that critic generalization and uncertainty-aware guidance remain the central bottlenecks.

## 参考
- http://arxiv.org/abs/2607.02092v2

## 개요
Guided Action Flow는 재훈련 없이 기반 정책을 안내하는 추론 시점(inference-time) 유도 방법으로, 플로우 매칭(flow matching) 기반의 시각-언어-행동(VLA) 정책을 위해 특별히 설계되었습니다. 이 방법은 사전 훈련된 SmolVLA 정책을 완전히 동결(frozen) 상태로 유지하면서, 추가로 학습된 액션 블록 평가자(critic)만을 통해 역방향 플로우 샘플링 과정을 안내합니다. 이 평가자는 실제 성공 및 실패 궤적에서 훈련되며, SmolVLA 언어 경로의 작업 설명 특징을 활용하고, 샘플링 과정에서 오직 액션 그라디언트만을 통해 작동합니다. LIBERO 조작 작업에서의 실험 결과, 단일 작업 평가자는 성공률을 크게 향상시켰으며, 다중 작업 평가자는 검증 세트에서도 뚜렷한 개선을 보였지만 테스트 세트에서는 개선 폭이 제한적이었습니다.

## 핵심 내용
### 방법 개요
Guided Action Flow의 핵심 아이디어는 플로우 매칭 기반의 시각-언어-행동 정책의 추론 단계에 유도 메커니즘을 도입하되, 기반 정책을 수정하거나 재훈련하지 않는 것입니다. 구체적으로:
- **기반 정책**: 사전 훈련된 SmolVLA 정책을 사용하며, 이 정책은 플로우 매칭 과정을 통해 로봇 액션 블록을 생성합니다.
- **평가자**: 실제 성공 및 실패 궤적에서 훈련된 액션 블록 평가자를 학습하며, SmolVLA 언어 경로의 작업 설명 특징을 활용할 수 있습니다.
- **유도 메커니즘**: 역방향 플로우 샘플링 과정에서 평가자가 액션 그라디언트를 통해 유도를 제공하여 생성된 액션 블록을 최적화합니다.

### 실험 설정
- **작업**: LIBERO 조작 작업에서 평가를 수행합니다.
- **평가자 유형**:
  - **단일 작업 평가자**: 특정 작업에 대해 훈련되며, 한 시드 창에서 성공률을 68.0%에서 82.0%로, 다른 시드 창에서는 82.0%에서 86.0%로 향상시킵니다.
  - **다중 작업 평가자**: 다중 패밀리 작업 설명 특징을 기반으로 훈련되며, 검증 세트에서 성공률을 46.0%에서 56.0%로, 테스트 세트에서는 65.0%에서 67.5%로 향상시킵니다.

### 핵심 결론
- **타당성 검증**: 실험 결과는 Q-유도 추론이 동결된 플로우 매칭 VLA 정책에 대해 실행 가능하며, 기반 정책을 재훈련하지 않고도 성능을 향상시킬 수 있음을 보여줍니다.
- **주요 병목**: 평가자의 일반화 능력과 불확실성 인지 유도는 여전히 현재 방법의 핵심 제한 사항으로, 다중 작업 시나리오에서 테스트 세트 개선 폭이 제한적입니다.
