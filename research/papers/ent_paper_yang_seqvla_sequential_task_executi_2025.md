---
$id: ent_paper_yang_seqvla_sequential_task_executi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SeqVLA: Sequential Task Execution for Long-Horizon Manipulation with Completion-Aware Vision-Language-Action Model'
  zh: SeqVLA
  ko: 'SeqVLA: Sequential Task Execution for Long-Horizon Manipulation with Completion-Aware Vision-Language-Action Model'
summary:
  en: 'SeqVLA: Sequential Task Execution for Long-Horizon Manipulation with Completion-Aware Vision-Language-Action Model
    (SeqVLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by Drexel University, Virginia
    Tech.'
  zh: 'SeqVLA: Sequential Task Execution for Long-Horizon Manipulation with Completion-Aware Vision-Language-Action Model
    (SeqVLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by Drexel University, Virginia
    Tech.'
  ko: 'SeqVLA: Sequential Task Execution for Long-Horizon Manipulation with Completion-Aware Vision-Language-Action Model
    (SeqVLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by Drexel University, Virginia
    Tech.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- seqvla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.14138v1.
sources:
- id: src_001
  type: paper
  title: 'SeqVLA: Sequential Task Execution for Long-Horizon Manipulation with Completion-Aware Vision-Language-Action Model
    (arXiv)'
  url: https://arxiv.org/abs/2509.14138
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: SeqVLA source
  url: https://doi.org/10.48550/arXiv.2509.14138
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Long-horizon robotic manipulation tasks require executing multiple interdependent subtasks in strict sequence, where errors in detecting subtask completion can cascade into downstream failures. Existing Vision-Language-Action (VLA) models such as $π_0$ excel at continuous low-level control but lack an internal signal for identifying when a subtask has finished, making them brittle in sequential settings. We propose SeqVLA, a completion-aware extension of $π_0$ that augments the base architecture with a lightweight detection head perceiving whether the current subtask is complete. This dual-head design enables SeqVLA not only to generate manipulation actions but also to autonomously trigger transitions between subtasks. We investigate four finetuning strategies that vary in how the action and detection heads are optimized (joint vs. sequential finetuning) and how pretrained knowledge is preserved (full finetuning vs. frozen backbone). Experiments are performed on two multi-stage tasks: salad packing with seven distinct subtasks and candy packing with four distinct subtasks. Results show that SeqVLA significantly outperforms the baseline $π_0$ and other strong baselines in overall success rate. In particular, joint finetuning with an unfrozen backbone yields the most decisive and statistically reliable completion predictions, eliminating sequence-related failures and enabling robust long-horizon execution. Our results highlight the importance of coupling action generation with subtask-aware detection for scalable sequential manipulation.

## 核心内容
Long-horizon robotic manipulation tasks require executing multiple interdependent subtasks in strict sequence, where errors in detecting subtask completion can cascade into downstream failures. Existing Vision-Language-Action (VLA) models such as $π_0$ excel at continuous low-level control but lack an internal signal for identifying when a subtask has finished, making them brittle in sequential settings. We propose SeqVLA, a completion-aware extension of $π_0$ that augments the base architecture with a lightweight detection head perceiving whether the current subtask is complete. This dual-head design enables SeqVLA not only to generate manipulation actions but also to autonomously trigger transitions between subtasks. We investigate four finetuning strategies that vary in how the action and detection heads are optimized (joint vs. sequential finetuning) and how pretrained knowledge is preserved (full finetuning vs. frozen backbone). Experiments are performed on two multi-stage tasks: salad packing with seven distinct subtasks and candy packing with four distinct subtasks. Results show that SeqVLA significantly outperforms the baseline $π_0$ and other strong baselines in overall success rate. In particular, joint finetuning with an unfrozen backbone yields the most decisive and statistically reliable completion predictions, eliminating sequence-related failures and enabling robust long-horizon execution. Our results highlight the importance of coupling action generation with subtask-aware detection for scalable sequential manipulation.

## 参考
- http://arxiv.org/abs/2509.14138v1

## Overview
Long-horizon robotic manipulation tasks require executing multiple interdependent subtasks in strict sequence, where errors in detecting subtask completion can cascade into downstream failures. Existing Vision-Language-Action (VLA) models such as $π_0$ excel at continuous low-level control but lack an internal signal for identifying when a subtask has finished, making them brittle in sequential settings. We propose SeqVLA, a completion-aware extension of $π_0$ that augments the base architecture with a lightweight detection head perceiving whether the current subtask is complete. This dual-head design enables SeqVLA not only to generate manipulation actions but also to autonomously trigger transitions between subtasks. We investigate four finetuning strategies that vary in how the action and detection heads are optimized (joint vs. sequential finetuning) and how pretrained knowledge is preserved (full finetuning vs. frozen backbone). Experiments are performed on two multi-stage tasks: salad packing with seven distinct subtasks and candy packing with four distinct subtasks. Results show that SeqVLA significantly outperforms the baseline $π_0$ and other strong baselines in overall success rate. In particular, joint finetuning with an unfrozen backbone yields the most decisive and statistically reliable completion predictions, eliminating sequence-related failures and enabling robust long-horizon execution. Our results highlight the importance of coupling action generation with subtask-aware detection for scalable sequential manipulation.

## Content
Long-horizon robotic manipulation tasks require executing multiple interdependent subtasks in strict sequence, where errors in detecting subtask completion can cascade into downstream failures. Existing Vision-Language-Action (VLA) models such as $π_0$ excel at continuous low-level control but lack an internal signal for identifying when a subtask has finished, making them brittle in sequential settings. We propose SeqVLA, a completion-aware extension of $π_0$ that augments the base architecture with a lightweight detection head perceiving whether the current subtask is complete. This dual-head design enables SeqVLA not only to generate manipulation actions but also to autonomously trigger transitions between subtasks. We investigate four finetuning strategies that vary in how the action and detection heads are optimized (joint vs. sequential finetuning) and how pretrained knowledge is preserved (full finetuning vs. frozen backbone). Experiments are performed on two multi-stage tasks: salad packing with seven distinct subtasks and candy packing with four distinct subtasks. Results show that SeqVLA significantly outperforms the baseline $π_0$ and other strong baselines in overall success rate. In particular, joint finetuning with an unfrozen backbone yields the most decisive and statistically reliable completion predictions, eliminating sequence-related failures and enabling robust long-horizon execution. Our results highlight the importance of coupling action generation with subtask-aware detection for scalable sequential manipulation.

## 개요
장기간 로봇 조작 작업은 여러 상호 의존적인 하위 작업을 엄격한 순서로 실행해야 하며, 하위 작업 완료 감지 오류가 하위 작업 실패로 이어질 수 있습니다. 기존의 Vision-Language-Action (VLA) 모델(예: $π_0$)은 연속적인 저수준 제어에 뛰어나지만, 하위 작업이 완료되었는지 식별하는 내부 신호가 없어 순차적 환경에서 취약합니다. 우리는 SeqVLA를 제안합니다. 이는 $π_0$의 완료 인식 확장판으로, 기본 아키텍처에 현재 하위 작업 완료 여부를 감지하는 경량 탐지 헤드를 추가합니다. 이 이중 헤드 설계를 통해 SeqVLA는 조작 동작을 생성할 뿐만 아니라 하위 작업 간 전환을 자율적으로 트리거할 수 있습니다. 우리는 동작 헤드와 탐지 헤드의 최적화 방식(공동 vs. 순차적 파인튜닝)과 사전 학습 지식 보존 방식(전체 파인튜닝 vs. 고정 백본)이 다른 네 가지 파인튜닝 전략을 조사합니다. 실험은 7개의 개별 하위 작업으로 구성된 샐러드 포장과 4개의 개별 하위 작업으로 구성된 사탕 포장이라는 두 가지 다단계 작업에서 수행됩니다. 결과는 SeqVLA가 전체 성공률에서 기준 모델 $π_0$ 및 다른 강력한 기준 모델을 크게 능가함을 보여줍니다. 특히, 고정되지 않은 백본을 사용한 공동 파인튜닝은 가장 결정적이고 통계적으로 신뢰할 수 있는 완료 예측을 제공하여 순서 관련 실패를 제거하고 강력한 장기 실행을 가능하게 합니다. 우리의 결과는 확장 가능한 순차적 조작을 위해 동작 생성과 하위 작업 인식 탐지를 결합하는 것의 중요성을 강조합니다.

## 핵심 내용
장기간 로봇 조작 작업은 여러 상호 의존적인 하위 작업을 엄격한 순서로 실행해야 하며, 하위 작업 완료 감지 오류가 하위 작업 실패로 이어질 수 있습니다. 기존의 Vision-Language-Action (VLA) 모델(예: $π_0$)은 연속적인 저수준 제어에 뛰어나지만, 하위 작업이 완료되었는지 식별하는 내부 신호가 없어 순차적 환경에서 취약합니다. 우리는 SeqVLA를 제안합니다. 이는 $π_0$의 완료 인식 확장판으로, 기본 아키텍처에 현재 하위 작업 완료 여부를 감지하는 경량 탐지 헤드를 추가합니다. 이 이중 헤드 설계를 통해 SeqVLA는 조작 동작을 생성할 뿐만 아니라 하위 작업 간 전환을 자율적으로 트리거할 수 있습니다. 우리는 동작 헤드와 탐지 헤드의 최적화 방식(공동 vs. 순차적 파인튜닝)과 사전 학습 지식 보존 방식(전체 파인튜닝 vs. 고정 백본)이 다른 네 가지 파인튜닝 전략을 조사합니다. 실험은 7개의 개별 하위 작업으로 구성된 샐러드 포장과 4개의 개별 하위 작업으로 구성된 사탕 포장이라는 두 가지 다단계 작업에서 수행됩니다. 결과는 SeqVLA가 전체 성공률에서 기준 모델 $π_0$ 및 다른 강력한 기준 모델을 크게 능가함을 보여줍니다. 특히, 고정되지 않은 백본을 사용한 공동 파인튜닝은 가장 결정적이고 통계적으로 신뢰할 수 있는 완료 예측을 제공하여 순서 관련 실패를 제거하고 강력한 장기 실행을 가능하게 합니다. 우리의 결과는 확장 가능한 순차적 조작을 위해 동작 생성과 하위 작업 인식 탐지를 결합하는 것의 중요성을 강조합니다.
