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
  zh: 'arXiv:2607.02092v2 Announce Type: replace Abstract: Flow-matching vision-language-action policies generate robot action
    chunks through an iterative transport process, creating an opportunity for test-time guidance without retraining the base
    policy. We study this opportunity in Guided Action Flow, an inference-time framework that keeps a pretrained SmolVLA policy
    frozen and uses a learned action-chunk critic to guide its reverse-time flow sampler. The critic is trained from real
    success and failure rollouts, can condition on task-description features from the frozen SmolVLA language pathway, and
    is used only through action gradients during sampling. We evaluate the approach on LIBERO manipulation tasks. A single-task
    critic improves success from 68.0% to 82.0% on one seed window and from 82.0% to 86.0% on another. A multi-family task-description
    critic improves validation success from 46.0% to 56.0%, while the locked held-out test gain is positive but modest, from
    65.0% to 67.5%. These results support the feasibility of Q-guided inference for frozen flow-matching VLA policies, while
    showing that critic generalization and uncertainty-aware guidance remain the central bottlenecks.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.02092v2.
sources:
- id: src_001
  type: paper
  title: 'Guided Action Flow: Q-Guided Inference for Flow-Matching Vision-Language-Action Policies (arXiv)'
  url: https://arxiv.org/abs/2607.02092
  date: '2092'
  accessed_at: '2026-07-08'
---
## 概述
Flow-matching vision-language-action policies generate robot action chunks through an iterative transport process, creating an opportunity for test-time guidance without retraining the base policy. We study this opportunity in Guided Action Flow, an inference-time framework that keeps a pretrained SmolVLA policy frozen and uses a learned action-chunk critic to guide its reverse-time flow sampler. The critic is trained from real success and failure rollouts, can condition on task-description features from the frozen SmolVLA language pathway, and is used only through action gradients during sampling. We evaluate the approach on LIBERO manipulation tasks. A single-task critic improves success from 68.0% to 82.0% on one seed window and from 82.0% to 86.0% on another. A multi-family task-description critic improves validation success from 46.0% to 56.0%, while the locked held-out test gain is positive but modest, from 65.0% to 67.5%. These results support the feasibility of Q-guided inference for frozen flow-matching VLA policies, while showing that critic generalization and uncertainty-aware guidance remain the central bottlenecks.

## 核心内容
Flow-matching vision-language-action policies generate robot action chunks through an iterative transport process, creating an opportunity for test-time guidance without retraining the base policy. We study this opportunity in Guided Action Flow, an inference-time framework that keeps a pretrained SmolVLA policy frozen and uses a learned action-chunk critic to guide its reverse-time flow sampler. The critic is trained from real success and failure rollouts, can condition on task-description features from the frozen SmolVLA language pathway, and is used only through action gradients during sampling. We evaluate the approach on LIBERO manipulation tasks. A single-task critic improves success from 68.0% to 82.0% on one seed window and from 82.0% to 86.0% on another. A multi-family task-description critic improves validation success from 46.0% to 56.0%, while the locked held-out test gain is positive but modest, from 65.0% to 67.5%. These results support the feasibility of Q-guided inference for frozen flow-matching VLA policies, while showing that critic generalization and uncertainty-aware guidance remain the central bottlenecks.

## 参考
- http://arxiv.org/abs/2607.02092v2

## Overview
Flow-matching vision-language-action policies generate robot action chunks through an iterative transport process, creating an opportunity for test-time guidance without retraining the base policy. We study this opportunity in Guided Action Flow, an inference-time framework that keeps a pretrained SmolVLA policy frozen and uses a learned action-chunk critic to guide its reverse-time flow sampler. The critic is trained from real success and failure rollouts, can condition on task-description features from the frozen SmolVLA language pathway, and is used only through action gradients during sampling. We evaluate the approach on LIBERO manipulation tasks. A single-task critic improves success from 68.0% to 82.0% on one seed window and from 82.0% to 86.0% on another. A multi-family task-description critic improves validation success from 46.0% to 56.0%, while the locked held-out test gain is positive but modest, from 65.0% to 67.5%. These results support the feasibility of Q-guided inference for frozen flow-matching VLA policies, while showing that critic generalization and uncertainty-aware guidance remain the central bottlenecks.

## Content
Flow-matching vision-language-action policies generate robot action chunks through an iterative transport process, creating an opportunity for test-time guidance without retraining the base policy. We study this opportunity in Guided Action Flow, an inference-time framework that keeps a pretrained SmolVLA policy frozen and uses a learned action-chunk critic to guide its reverse-time flow sampler. The critic is trained from real success and failure rollouts, can condition on task-description features from the frozen SmolVLA language pathway, and is used only through action gradients during sampling. We evaluate the approach on LIBERO manipulation tasks. A single-task critic improves success from 68.0% to 82.0% on one seed window and from 82.0% to 86.0% on another. A multi-family task-description critic improves validation success from 46.0% to 56.0%, while the locked held-out test gain is positive but modest, from 65.0% to 67.5%. These results support the feasibility of Q-guided inference for frozen flow-matching VLA policies, while showing that critic generalization and uncertainty-aware guidance remain the central bottlenecks.

## 개요
Flow-matching vision-language-action 정책은 반복적인 전송 과정을 통해 로봇의 행동 청크를 생성하며, 이는 기본 정책을 재훈련하지 않고도 테스트 시점에서의 안내(guidance)를 가능하게 하는 기회를 제공합니다. 우리는 Guided Action Flow에서 이러한 기회를 연구합니다. 이는 사전 훈련된 SmolVLA 정책을 고정(frozen) 상태로 유지하고, 학습된 행동 청크 비평가(critic)를 사용하여 역방향 시간 흐름 샘플러를 안내하는 추론 시점 프레임워크입니다. 비평가는 실제 성공 및 실패 롤아웃 데이터로 훈련되며, 고정된 SmolVLA 언어 경로의 작업 설명 특징을 조건으로 사용할 수 있고, 샘플링 중 행동 그래디언트를 통해서만 활용됩니다. 우리는 이 접근법을 LIBERO 조작 작업에서 평가했습니다. 단일 작업 비평가는 한 시드 윈도우에서 성공률을 68.0%에서 82.0%로, 다른 시드에서는 82.0%에서 86.0%로 향상시켰습니다. 다중 패밀리 작업 설명 비평가는 검증 성공률을 46.0%에서 56.0%로 개선했으며, 고정된 홀드아웃 테스트 성능 향상은 긍정적이지만 미미하여 65.0%에서 67.5%로 증가했습니다. 이러한 결과는 고정된 flow-matching VLA 정책에 대한 Q-안내 추론의 실현 가능성을 지지하는 동시에, 비평가의 일반화와 불확실성 인식 안내가 여전히 주요 병목 현상임을 보여줍니다.

## 핵심 내용
Flow-matching vision-language-action 정책은 반복적인 전송 과정을 통해 로봇의 행동 청크를 생성하며, 이는 기본 정책을 재훈련하지 않고도 테스트 시점에서의 안내(guidance)를 가능하게 하는 기회를 제공합니다. 우리는 Guided Action Flow에서 이러한 기회를 연구합니다. 이는 사전 훈련된 SmolVLA 정책을 고정(frozen) 상태로 유지하고, 학습된 행동 청크 비평가(critic)를 사용하여 역방향 시간 흐름 샘플러를 안내하는 추론 시점 프레임워크입니다. 비평가는 실제 성공 및 실패 롤아웃 데이터로 훈련되며, 고정된 SmolVLA 언어 경로의 작업 설명 특징을 조건으로 사용할 수 있고, 샘플링 중 행동 그래디언트를 통해서만 활용됩니다. 우리는 이 접근법을 LIBERO 조작 작업에서 평가했습니다. 단일 작업 비평가는 한 시드 윈도우에서 성공률을 68.0%에서 82.0%로, 다른 시드에서는 82.0%에서 86.0%로 향상시켰습니다. 다중 패밀리 작업 설명 비평가는 검증 성공률을 46.0%에서 56.0%로 개선했으며, 고정된 홀드아웃 테스트 성능 향상은 긍정적이지만 미미하여 65.0%에서 67.5%로 증가했습니다. 이러한 결과는 고정된 flow-matching VLA 정책에 대한 Q-안내 추론의 실현 가능성을 지지하는 동시에, 비평가의 일반화와 불확실성 인식 안내가 여전히 주요 병목 현상임을 보여줍니다.
