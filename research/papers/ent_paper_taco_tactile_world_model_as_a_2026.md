---
$id: ent_paper_taco_tactile_world_model_as_a_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TACO: TActile World Model as a Self-COrrector forScalable VLA Post-Training'
  zh: 'TACO: TActile World Model as a Self-COrrector forScalable VLA Post-Training'
  ko: 'TACO: TActile World Model as a Self-COrrector forScalable VLA Post-Training'
summary:
  en: 'arXiv:2607.02840v1 Announce Type: new Abstract: Vision-Language-Action (VLA) models have shown promising generalization
    in robotic manipulation, but they still struggle with contact-rich tasks, where minor contact perturbations can cause
    unrecoverable failures that are hard to detect from vision alone. Since these failures are localized rather than task-level
    semantic errors, tactile-aware corrective post-training offers an efficient way to improve recovery. However, scaling
    such supervision through human intervention is costly. Recent works have explored world models to synthesize imagined
    rollouts for policy improvement, but vision-only world models may produce visually plausible yet contact-inconsistent
    trajectories. We therefore introduce TACO, a tactile-aware world-model-driven framework for scalable VLA post-training
    in contact-rich manipulation. Given real robot rollouts, TACO follows a Recognize-Imagine-Label loop with a tactile-aware
    world model: a unified progress-action model recognizes failure-adjacent states using progress estimates, a visuo-tactile
    generation model imagines local correction segments, and the progress-action model labels them with executable corrective
    actions. To incorporate tactile corrective supervision into VLA post-training, TACO combines knowledge-insulated tactile
    adaptation with advantage-conditioned training, enabling the policy to learn from imagined corrections without degrading
    pretrained visual-language priors. These components enable TACO to convert real-world failures into imagined visuo-tactile
    corrections for iterative VLA post-training. Experiments on real-world contact-rich manipulation tasks show that TACO
    achieves 44% absolute success rate improvement over the base policy and 32% over the policy without knowledge-insulated
    tactile adaptation.'
  zh: TACO 是一个由触觉感知的世界模型驱动的框架，用于对视觉-语言-动作（VLA）模型进行可扩展的后训练，以提升其在接触密集型操作任务中的表现。该框架通过“识别-想象-标注”循环，将真实世界的失败转化为想象的视觉-触觉修正，并结合知识隔离的触觉适应与优势条件训练，实现了44%的绝对成功率提升。
  ko: 'arXiv:2607.02840v1 Announce Type: new Abstract: Vision-Language-Action (VLA) models have shown promising generalization
    in robotic manipulation, but they still struggle with contact-rich tasks, where minor contact perturbations can cause
    unrecoverable failures that are hard to detect from vision alone. Since these failures are localized rather than task-level
    semantic errors, tactile-aware corrective post-training offers an efficient way to improve recovery. However, scaling
    such supervision through human intervention is costly. Recent works have explored world models to synthesize imagined
    rollouts for policy improvement, but vision-only world models may produce visually plausible yet contact-inconsistent
    trajectories. We therefore introduce TACO, a tactile-aware world-model-driven framework for scalable VLA post-training
    in contact-rich manipulation. Given real robot rollouts, TACO follows a Recognize-Imagine-Label loop with a tactile-aware
    world model: a unified progress-action model recognizes failure-adjacent states using progress estimates, a visuo-tactile
    generation model imagines local correction segments, and the progress-action model labels them with executable corrective
    actions. To incorporate tactile corrective supervision into VLA post-training, TACO combines knowledge-insulated tactile
    adaptation with advantage-conditioned training, enabling the policy to learn from imagined corrections without degrading
    pretrained visual-language priors. These components enable TACO to convert real-world failures into imagined visuo-tactile
    corrections for iterative VLA post-training. Experiments on real-world contact-rich manipulation tasks show that TACO
    achieves 44% absolute success rate improvement over the base policy and 32% over the policy without knowledge-insulated
    tactile adaptation.'
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
- taco
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.02840v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1056 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'TACO: TActile World Model as a Self-COrrector forScalable VLA Post-Training (arXiv)'
  url: https://arxiv.org/abs/2607.02840
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
TACO 针对 VLA 模型在接触密集型任务中因微小接触扰动导致的不可恢复失败问题，提出了一种基于触觉感知世界模型的后训练方法。该框架首先利用统一的进度-动作模型识别接近失败的状态，然后通过视觉-触觉生成模型想象局部修正片段，最后用进度-动作模型为这些片段标注可执行的修正动作。为了将触觉修正监督融入 VLA 后训练，TACO 采用了知识隔离的触觉适应与优势条件训练相结合的策略，确保策略能从想象的修正中学习而不破坏预训练的视觉-语言先验知识。在真实世界的接触密集型操作实验中，TACO 相比基础策略取得了44%的绝对成功率提升，相比未使用知识隔离触觉适应的策略提升了32%。

## 核心内容
### 方法概述
TACO 的核心是一个触觉感知的世界模型，它通过“Recognize-Imagine-Label”循环来处理真实机器人 rollout 数据：
- **Recognize（识别）**：使用统一的进度-动作模型，基于进度估计来识别接近失败的状态。
- **Imagine（想象）**：利用视觉-触觉生成模型，为识别出的失败状态想象局部的修正轨迹片段。
- **Label（标注）**：再次使用进度-动作模型，为想象的修正片段标注可执行的修正动作。

### 后训练策略
为了将触觉修正监督有效整合到 VLA 后训练中，TACO 引入了两种关键技术：
- **知识隔离的触觉适应（Knowledge-Insulated Tactile Adaptation）**：在训练过程中隔离触觉相关参数，避免对预训练的视觉-语言先验知识造成退化。
- **优势条件训练（Advantage-Conditioned Training）**：基于优势函数对想象的修正进行加权训练，使策略优先学习高价值的修正行为。

### 实验设置与结果
- **任务**：真实世界中的接触密集型操作任务。
- **基线对比**：TACO 与基础 VLA 策略以及未使用知识隔离触觉适应的变体进行对比。
- **关键数字**：
  - 相比基础策略，TACO 实现了 **44% 的绝对成功率提升**。
  - 相比未使用知识隔离触觉适应的策略，TACO 实现了 **32% 的绝对成功率提升**。

### 结论
TACO 通过触觉感知的世界模型，将真实世界的失败转化为可扩展的想象修正数据，有效提升了 VLA 模型在接触密集型任务中的鲁棒性。其知识隔离的触觉适应机制确保了后训练过程不会损害模型的视觉-语言先验能力。

## Overview
Vision-Language-Action (VLA) models have shown promising generalization in robotic manipulation, but they still struggle with contact-rich tasks, where minor contact perturbations can cause unrecoverable failures that are hard to detect from vision alone. Since these failures are localized rather than task-level semantic errors, tactile-aware corrective post-training offers an efficient way to improve recovery. However, scaling such supervision through human intervention is costly. Recent works have explored world models to synthesize imagined rollouts for policy improvement, but vision-only world models may produce visually plausible yet contact-inconsistent trajectories. We therefore introduce TACO, a tactile-aware world-model-driven framework for scalable VLA post-training in contact-rich manipulation. Given real robot rollouts, TACO follows a Recognize-Imagine-Label loop with a tactile-aware world model: a unified progress-action model recognizes failure-adjacent states using progress estimates, a visuo-tactile generation model imagines local correction segments, and the progress-action model labels them with executable corrective actions. To incorporate tactile corrective supervision into VLA post-training, TACO combines knowledge-insulated tactile adaptation with advantage-conditioned training, enabling the policy to learn from imagined corrections without degrading pretrained visual-language priors. These components enable TACO to convert real-world failures into imagined visuo-tactile corrections for iterative VLA post-training. Experiments on real-world contact-rich manipulation tasks show that TACO achieves 44% absolute success rate improvement over the base policy and 32% over the policy without knowledge-insulated tactile adaptation.

## 参考
- http://arxiv.org/abs/2607.02840v1

## 개요
TACO는 VLA 모델이 접촉 집약적 작업에서 미세한 접촉 교란으로 인해 발생하는 복구 불가능한 실패 문제를 해결하기 위해, 촉각 인식 세계 모델 기반의 사후 훈련 방법을 제안한다. 이 프레임워크는 먼저 통합된 진행-행동 모델을 사용하여 실패에 가까운 상태를 식별하고, 그 다음 시각-촉각 생성 모델을 통해 국소적 수정 궤적 조각을 상상하며, 마지막으로 진행-행동 모델을 사용하여 이러한 조각들에 실행 가능한 수정 행동을 주석한다. 촉각 수정 감독을 VLA 사후 훈련에 통합하기 위해, TACO는 지식 격리 촉각 적응과 이점 조건 훈련을 결합한 전략을 채택하여, 정책이 사전 훈련된 시각-언어 사전 지식을 손상시키지 않으면서 상상된 수정으로부터 학습할 수 있도록 보장한다. 실제 세계의 접촉 집약적 조작 실험에서, TACO는 기본 정책 대비 **44%의 절대 성공률 향상**을 달성했으며, 지식 격리 촉각 적응을 사용하지 않은 정책 대비 **32%의 성능 향상**을 보였다.

## 핵심 내용
### 방법 개요
TACO의 핵심은 촉각 인식 세계 모델로, "인식-상상-주석" 루프를 통해 실제 로봇 롤아웃 데이터를 처리한다:
- **인식(Recognize)**: 통합된 진행-행동 모델을 사용하여 진행 추정을 기반으로 실패에 가까운 상태를 식별한다.
- **상상(Imagine)**: 시각-촉각 생성 모델을 활용하여 식별된 실패 상태에 대한 국소적 수정 궤적 조각을 상상한다.
- **주석(Label)**: 진행-행동 모델을 다시 사용하여 상상된 수정 조각에 실행 가능한 수정 행동을 주석한다.

### 사후 훈련 전략
촉각 수정 감독을 VLA 사후 훈련에 효과적으로 통합하기 위해, TACO는 두 가지 핵심 기술을 도입한다:
- **지식 격리 촉각 적응(Knowledge-Insulated Tactile Adaptation)**: 훈련 과정에서 촉각 관련 매개변수를 격리하여 사전 훈련된 시각-언어 사전 지식의 퇴화를 방지한다.
- **이점 조건 훈련(Advantage-Conditioned Training)**: 이점 함수를 기반으로 상상된 수정에 가중치를 부여하여 훈련함으로써, 정책이 높은 가치의 수정 행동을 우선적으로 학습하도록 한다.

### 실험 설정 및 결과
- **작업**: 실제 세계에서의 접촉 집약적 조작 작업.
- **기준 비교**: TACO는 기본 VLA 정책 및 지식 격리 촉각 적응을 사용하지 않은 변형과 비교된다.
- **핵심 수치**:
  - 기본 정책 대비, TACO는 **44%의 절대 성공률 향상**을 달성했다.
  - 지식 격리 촉각 적응을 사용하지 않은 정책 대비, TACO는 **32%의 절대 성공률 향상**을 달성했다.

### 결론
TACO는 촉각 인식 세계 모델을 통해 실제 세계의 실패를 확장 가능한 상상 수정 데이터로 변환하여, 접촉 집약적 작업에서 VLA 모델의 견고성을 효과적으로 향상시킨다. 지식 격리 촉각 적응 메커니즘은 사후 훈련 과정이 모델의 시각-언어 사전 능력을 손상시키지 않도록 보장한다.
