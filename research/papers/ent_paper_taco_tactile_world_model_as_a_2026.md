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
  zh: 'arXiv:2607.02840v1 Announce Type: new Abstract: Vision-Language-Action (VLA) models have shown promising generalization
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.02840v1.
sources:
- id: src_001
  type: paper
  title: 'TACO: TActile World Model as a Self-COrrector forScalable VLA Post-Training (arXiv)'
  url: https://arxiv.org/abs/2607.02840
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Vision-Language-Action (VLA) models have shown promising generalization in robotic manipulation, but they still struggle with contact-rich tasks, where minor contact perturbations can cause unrecoverable failures that are hard to detect from vision alone. Since these failures are localized rather than task-level semantic errors, tactile-aware corrective post-training offers an efficient way to improve recovery. However, scaling such supervision through human intervention is costly. Recent works have explored world models to synthesize imagined rollouts for policy improvement, but vision-only world models may produce visually plausible yet contact-inconsistent trajectories. We therefore introduce TACO, a tactile-aware world-model-driven framework for scalable VLA post-training in contact-rich manipulation. Given real robot rollouts, TACO follows a Recognize-Imagine-Label loop with a tactile-aware world model: a unified progress-action model recognizes failure-adjacent states using progress estimates, a visuo-tactile generation model imagines local correction segments, and the progress-action model labels them with executable corrective actions. To incorporate tactile corrective supervision into VLA post-training, TACO combines knowledge-insulated tactile adaptation with advantage-conditioned training, enabling the policy to learn from imagined corrections without degrading pretrained visual-language priors. These components enable TACO to convert real-world failures into imagined visuo-tactile corrections for iterative VLA post-training. Experiments on real-world contact-rich manipulation tasks show that TACO achieves 44% absolute success rate improvement over the base policy and 32% over the policy without knowledge-insulated tactile adaptation.

## 核心内容
Vision-Language-Action (VLA) models have shown promising generalization in robotic manipulation, but they still struggle with contact-rich tasks, where minor contact perturbations can cause unrecoverable failures that are hard to detect from vision alone. Since these failures are localized rather than task-level semantic errors, tactile-aware corrective post-training offers an efficient way to improve recovery. However, scaling such supervision through human intervention is costly. Recent works have explored world models to synthesize imagined rollouts for policy improvement, but vision-only world models may produce visually plausible yet contact-inconsistent trajectories. We therefore introduce TACO, a tactile-aware world-model-driven framework for scalable VLA post-training in contact-rich manipulation. Given real robot rollouts, TACO follows a Recognize-Imagine-Label loop with a tactile-aware world model: a unified progress-action model recognizes failure-adjacent states using progress estimates, a visuo-tactile generation model imagines local correction segments, and the progress-action model labels them with executable corrective actions. To incorporate tactile corrective supervision into VLA post-training, TACO combines knowledge-insulated tactile adaptation with advantage-conditioned training, enabling the policy to learn from imagined corrections without degrading pretrained visual-language priors. These components enable TACO to convert real-world failures into imagined visuo-tactile corrections for iterative VLA post-training. Experiments on real-world contact-rich manipulation tasks show that TACO achieves 44% absolute success rate improvement over the base policy and 32% over the policy without knowledge-insulated tactile adaptation.

## 参考
- http://arxiv.org/abs/2607.02840v1

## Overview
Vision-Language-Action (VLA) models have shown promising generalization in robotic manipulation, but they still struggle with contact-rich tasks, where minor contact perturbations can cause unrecoverable failures that are hard to detect from vision alone. Since these failures are localized rather than task-level semantic errors, tactile-aware corrective post-training offers an efficient way to improve recovery. However, scaling such supervision through human intervention is costly. Recent works have explored world models to synthesize imagined rollouts for policy improvement, but vision-only world models may produce visually plausible yet contact-inconsistent trajectories. We therefore introduce TACO, a tactile-aware world-model-driven framework for scalable VLA post-training in contact-rich manipulation. Given real robot rollouts, TACO follows a Recognize-Imagine-Label loop with a tactile-aware world model: a unified progress-action model recognizes failure-adjacent states using progress estimates, a visuo-tactile generation model imagines local correction segments, and the progress-action model labels them with executable corrective actions. To incorporate tactile corrective supervision into VLA post-training, TACO combines knowledge-insulated tactile adaptation with advantage-conditioned training, enabling the policy to learn from imagined corrections without degrading pretrained visual-language priors. These components enable TACO to convert real-world failures into imagined visuo-tactile corrections for iterative VLA post-training. Experiments on real-world contact-rich manipulation tasks show that TACO achieves 44% absolute success rate improvement over the base policy and 32% over the policy without knowledge-insulated tactile adaptation.

## Content
Vision-Language-Action (VLA) models have shown promising generalization in robotic manipulation, but they still struggle with contact-rich tasks, where minor contact perturbations can cause unrecoverable failures that are hard to detect from vision alone. Since these failures are localized rather than task-level semantic errors, tactile-aware corrective post-training offers an efficient way to improve recovery. However, scaling such supervision through human intervention is costly. Recent works have explored world models to synthesize imagined rollouts for policy improvement, but vision-only world models may produce visually plausible yet contact-inconsistent trajectories. We therefore introduce TACO, a tactile-aware world-model-driven framework for scalable VLA post-training in contact-rich manipulation. Given real robot rollouts, TACO follows a Recognize-Imagine-Label loop with a tactile-aware world model: a unified progress-action model recognizes failure-adjacent states using progress estimates, a visuo-tactile generation model imagines local correction segments, and the progress-action model labels them with executable corrective actions. To incorporate tactile corrective supervision into VLA post-training, TACO combines knowledge-insulated tactile adaptation with advantage-conditioned training, enabling the policy to learn from imagined corrections without degrading pretrained visual-language priors. These components enable TACO to convert real-world failures into imagined visuo-tactile corrections for iterative VLA post-training. Experiments on real-world contact-rich manipulation tasks show that TACO achieves 44% absolute success rate improvement over the base policy and 32% over the policy without knowledge-insulated tactile adaptation.

## 개요
Vision-Language-Action (VLA) 모델은 로봇 조작에서 유망한 일반화 성능을 보여주었지만, 접촉이 많은 작업에서는 여전히 어려움을 겪습니다. 이러한 작업에서는 미세한 접촉 교란이 시각 정보만으로는 감지하기 어려운 복구 불가능한 실패를 초래할 수 있습니다. 이러한 실패는 작업 수준의 의미론적 오류가 아닌 국소적이므로, 촉각 인식 교정 사후 훈련은 복구를 개선하는 효율적인 방법을 제공합니다. 그러나 인간의 개입을 통해 이러한 감독을 확장하는 것은 비용이 많이 듭니다. 최근 연구에서는 정책 개선을 위해 상상된 롤아웃을 합성하는 세계 모델을 탐구했지만, 시각 전용 세계 모델은 시각적으로는 그럴듯하지만 접촉이 일관되지 않은 궤적을 생성할 수 있습니다. 따라서 우리는 접촉이 많은 조작에서 확장 가능한 VLA 사후 훈련을 위한 촉각 인식 세계 모델 기반 프레임워크인 TACO를 소개합니다. 실제 로봇 롤아웃이 주어지면, TACO는 촉각 인식 세계 모델을 사용하여 Recognize-Imagine-Label 루프를 따릅니다: 통합된 진행-행동 모델이 진행 추정을 통해 실패에 인접한 상태를 인식하고, 시각-촉각 생성 모델이 국소 교정 세그먼트를 상상하며, 진행-행동 모델이 이를 실행 가능한 교정 행동으로 레이블링합니다. 촉각 교정 감독을 VLA 사후 훈련에 통합하기 위해, TACO는 지식 절연 촉각 적응과 이점 조건화 훈련을 결합하여, 정책이 사전 훈련된 시각-언어 사전 지식을 저하시키지 않으면서 상상된 교정으로부터 학습할 수 있도록 합니다. 이러한 구성 요소는 TACO가 실제 세계의 실패를 반복적인 VLA 사후 훈련을 위한 상상된 시각-촉각 교정으로 변환할 수 있게 합니다. 실제 접촉이 많은 조작 작업에 대한 실험에서 TACO는 기본 정책 대비 44%의 절대 성공률 향상과 지식 절연 촉각 적응이 없는 정책 대비 32%의 향상을 달성했습니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 로봇 조작에서 유망한 일반화 성능을 보여주었지만, 접촉이 많은 작업에서는 여전히 어려움을 겪습니다. 이러한 작업에서는 미세한 접촉 교란이 시각 정보만으로는 감지하기 어려운 복구 불가능한 실패를 초래할 수 있습니다. 이러한 실패는 작업 수준의 의미론적 오류가 아닌 국소적이므로, 촉각 인식 교정 사후 훈련은 복구를 개선하는 효율적인 방법을 제공합니다. 그러나 인간의 개입을 통해 이러한 감독을 확장하는 것은 비용이 많이 듭니다. 최근 연구에서는 정책 개선을 위해 상상된 롤아웃을 합성하는 세계 모델을 탐구했지만, 시각 전용 세계 모델은 시각적으로는 그럴듯하지만 접촉이 일관되지 않은 궤적을 생성할 수 있습니다. 따라서 우리는 접촉이 많은 조작에서 확장 가능한 VLA 사후 훈련을 위한 촉각 인식 세계 모델 기반 프레임워크인 TACO를 소개합니다. 실제 로봇 롤아웃이 주어지면, TACO는 촉각 인식 세계 모델을 사용하여 Recognize-Imagine-Label 루프를 따릅니다: 통합된 진행-행동 모델이 진행 추정을 통해 실패에 인접한 상태를 인식하고, 시각-촉각 생성 모델이 국소 교정 세그먼트를 상상하며, 진행-행동 모델이 이를 실행 가능한 교정 행동으로 레이블링합니다. 촉각 교정 감독을 VLA 사후 훈련에 통합하기 위해, TACO는 지식 절연 촉각 적응과 이점 조건화 훈련을 결합하여, 정책이 사전 훈련된 시각-언어 사전 지식을 저하시키지 않으면서 상상된 교정으로부터 학습할 수 있도록 합니다. 이러한 구성 요소는 TACO가 실제 세계의 실패를 반복적인 VLA 사후 훈련을 위한 상상된 시각-촉각 교정으로 변환할 수 있게 합니다. 실제 접촉이 많은 조작 작업에 대한 실험에서 TACO는 기본 정책 대비 44%의 절대 성공률 향상과 지식 절연 촉각 적응이 없는 정책 대비 32%의 향상을 달성했습니다.
