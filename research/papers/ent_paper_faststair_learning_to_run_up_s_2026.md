---
$id: ent_paper_faststair_learning_to_run_up_s_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FastStair: Learning to Run Up Stairs with Humanoid Robots'
  zh: 'FastStair: Learning to Run Up Stairs with Humanoid Robots'
  ko: 'FastStair: Learning to Run Up Stairs with Humanoid Robots'
summary:
  en: 'FastStair: Learning to Run Up Stairs with Humanoid Robots is a 2026 work on locomotion for humanoid robots.'
  zh: 'FastStair: Learning to Run Up Stairs with Humanoid Robots is a 2026 work on locomotion for humanoid robots.'
  ko: 'FastStair: Learning to Run Up Stairs with Humanoid Robots is a 2026 work on locomotion for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- faststair
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.10365v1.
sources:
- id: src_001
  type: paper
  title: 'FastStair: Learning to Run Up Stairs with Humanoid Robots (arXiv)'
  url: https://arxiv.org/abs/2601.10365
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Running up stairs is effortless for humans but remains extremely challenging for humanoid robots due to the simultaneous requirements of high agility and strict stability. Model-free reinforcement learning (RL) can generate dynamic locomotion, yet implicit stability rewards and heavy reliance on task-specific reward shaping tend to result in unsafe behaviors, especially on stairs; conversely, model-based foothold planners encode contact feasibility and stability structure, but enforcing their hard constraints often induces conservative motion that limits speed. We present FastStair, a planner-guided, multi-stage learning framework that reconciles these complementary strengths to achieve fast and stable stair ascent. FastStair integrates a parallel model-based foothold planner into the RL training loop to bias exploration toward dynamically feasible contacts and to pretrain a safety-focused base policy. To mitigate planner-induced conservatism and the discrepancy between low- and high-speed action distributions, the base policy was fine-tuned into speed-specialized experts and then integrated via Low-Rank Adaptation (LoRA) to enable smooth operation across the full commanded-speed range. We deploy the resulting controller on the Oli humanoid robot, achieving stable stair ascent at commanded speeds up to 1.65 m/s and traversing a 33-step spiral staircase (17 cm rise per step) in 12 s, demonstrating robust high-speed performance on long staircases. Notably, the proposed approach served as the champion solution in the Canton Tower Robot Run Up Competition.

## 核心内容
Running up stairs is effortless for humans but remains extremely challenging for humanoid robots due to the simultaneous requirements of high agility and strict stability. Model-free reinforcement learning (RL) can generate dynamic locomotion, yet implicit stability rewards and heavy reliance on task-specific reward shaping tend to result in unsafe behaviors, especially on stairs; conversely, model-based foothold planners encode contact feasibility and stability structure, but enforcing their hard constraints often induces conservative motion that limits speed. We present FastStair, a planner-guided, multi-stage learning framework that reconciles these complementary strengths to achieve fast and stable stair ascent. FastStair integrates a parallel model-based foothold planner into the RL training loop to bias exploration toward dynamically feasible contacts and to pretrain a safety-focused base policy. To mitigate planner-induced conservatism and the discrepancy between low- and high-speed action distributions, the base policy was fine-tuned into speed-specialized experts and then integrated via Low-Rank Adaptation (LoRA) to enable smooth operation across the full commanded-speed range. We deploy the resulting controller on the Oli humanoid robot, achieving stable stair ascent at commanded speeds up to 1.65 m/s and traversing a 33-step spiral staircase (17 cm rise per step) in 12 s, demonstrating robust high-speed performance on long staircases. Notably, the proposed approach served as the champion solution in the Canton Tower Robot Run Up Competition.

## 参考
- http://arxiv.org/abs/2601.10365v1

## Overview
Running up stairs is effortless for humans but remains extremely challenging for humanoid robots due to the simultaneous requirements of high agility and strict stability. Model-free reinforcement learning (RL) can generate dynamic locomotion, yet implicit stability rewards and heavy reliance on task-specific reward shaping tend to result in unsafe behaviors, especially on stairs; conversely, model-based foothold planners encode contact feasibility and stability structure, but enforcing their hard constraints often induces conservative motion that limits speed. We present FastStair, a planner-guided, multi-stage learning framework that reconciles these complementary strengths to achieve fast and stable stair ascent. FastStair integrates a parallel model-based foothold planner into the RL training loop to bias exploration toward dynamically feasible contacts and to pretrain a safety-focused base policy. To mitigate planner-induced conservatism and the discrepancy between low- and high-speed action distributions, the base policy was fine-tuned into speed-specialized experts and then integrated via Low-Rank Adaptation (LoRA) to enable smooth operation across the full commanded-speed range. We deploy the resulting controller on the Oli humanoid robot, achieving stable stair ascent at commanded speeds up to 1.65 m/s and traversing a 33-step spiral staircase (17 cm rise per step) in 12 s, demonstrating robust high-speed performance on long staircases. Notably, the proposed approach served as the champion solution in the Canton Tower Robot Run Up Competition.

## Content
Running up stairs is effortless for humans but remains extremely challenging for humanoid robots due to the simultaneous requirements of high agility and strict stability. Model-free reinforcement learning (RL) can generate dynamic locomotion, yet implicit stability rewards and heavy reliance on task-specific reward shaping tend to result in unsafe behaviors, especially on stairs; conversely, model-based foothold planners encode contact feasibility and stability structure, but enforcing their hard constraints often induces conservative motion that limits speed. We present FastStair, a planner-guided, multi-stage learning framework that reconciles these complementary strengths to achieve fast and stable stair ascent. FastStair integrates a parallel model-based foothold planner into the RL training loop to bias exploration toward dynamically feasible contacts and to pretrain a safety-focused base policy. To mitigate planner-induced conservatism and the discrepancy between low- and high-speed action distributions, the base policy was fine-tuned into speed-specialized experts and then integrated via Low-Rank Adaptation (LoRA) to enable smooth operation across the full commanded-speed range. We deploy the resulting controller on the Oli humanoid robot, achieving stable stair ascent at commanded speeds up to 1.65 m/s and traversing a 33-step spiral staircase (17 cm rise per step) in 12 s, demonstrating robust high-speed performance on long staircases. Notably, the proposed approach served as the champion solution in the Canton Tower Robot Run Up Competition.

## 개요
계단을 빠르게 오르는 것은 인간에게는 쉬운 일이지만, 높은 민첩성과 엄격한 안정성을 동시에 요구하기 때문에 휴머노이드 로봇에게는 여전히 매우 어려운 과제입니다. 모델 프리 강화 학습(RL)은 동적인 움직임을 생성할 수 있지만, 암묵적인 안정성 보상과 과제별 보상 설계에 대한 과도한 의존성은 특히 계단에서 불안전한 행동을 초래하는 경향이 있습니다. 반대로, 모델 기반 발판 계획기는 접촉 가능성과 안정성 구조를 인코딩하지만, 엄격한 제약 조건을 강제하면 종종 속도를 제한하는 보수적인 움직임을 유발합니다. 우리는 이러한 상호 보완적인 강점을 조화시켜 빠르고 안정적인 계단 오르기를 달성하는 계획기 기반 다단계 학습 프레임워크인 FastStair를 제시합니다. FastStair는 병렬 모델 기반 발판 계획기를 RL 훈련 루프에 통합하여 동적으로 실현 가능한 접촉 방향으로 탐색을 유도하고 안전 중심의 기본 정책을 사전 훈련합니다. 계획기로 인한 보수성과 저속 및 고속 행동 분포 간의 차이를 완화하기 위해, 기본 정책을 속도별 전문가로 미세 조정한 후 Low-Rank Adaptation(LoRA)을 통해 통합하여 명령된 전체 속도 범위에서 원활한 작동을 가능하게 합니다. 우리는 결과 컨트롤러를 Oli 휴머노이드 로봇에 배포하여 명령 속도 최대 1.65m/s에서 안정적인 계단 오르기를 달성하고, 33계단의 나선형 계단(계단당 높이 17cm)을 12초 만에 통과하여 긴 계단에서의 강력한 고속 성능을 입증했습니다. 특히, 제안된 접근 방식은 Canton Tower Robot Run Up Competition에서 우승 솔루션으로 사용되었습니다.

## 핵심 내용
계단을 빠르게 오르는 것은 인간에게는 쉬운 일이지만, 높은 민첩성과 엄격한 안정성을 동시에 요구하기 때문에 휴머노이드 로봇에게는 여전히 매우 어려운 과제입니다. 모델 프리 강화 학습(RL)은 동적인 움직임을 생성할 수 있지만, 암묵적인 안정성 보상과 과제별 보상 설계에 대한 과도한 의존성은 특히 계단에서 불안전한 행동을 초래하는 경향이 있습니다. 반대로, 모델 기반 발판 계획기는 접촉 가능성과 안정성 구조를 인코딩하지만, 엄격한 제약 조건을 강제하면 종종 속도를 제한하는 보수적인 움직임을 유발합니다. 우리는 이러한 상호 보완적인 강점을 조화시켜 빠르고 안정적인 계단 오르기를 달성하는 계획기 기반 다단계 학습 프레임워크인 FastStair를 제시합니다. FastStair는 병렬 모델 기반 발판 계획기를 RL 훈련 루프에 통합하여 동적으로 실현 가능한 접촉 방향으로 탐색을 유도하고 안전 중심의 기본 정책을 사전 훈련합니다. 계획기로 인한 보수성과 저속 및 고속 행동 분포 간의 차이를 완화하기 위해, 기본 정책을 속도별 전문가로 미세 조정한 후 Low-Rank Adaptation(LoRA)을 통해 통합하여 명령된 전체 속도 범위에서 원활한 작동을 가능하게 합니다. 우리는 결과 컨트롤러를 Oli 휴머노이드 로봇에 배포하여 명령 속도 최대 1.65m/s에서 안정적인 계단 오르기를 달성하고, 33계단의 나선형 계단(계단당 높이 17cm)을 12초 만에 통과하여 긴 계단에서의 강력한 고속 성능을 입증했습니다. 특히, 제안된 접근 방식은 Canton Tower Robot Run Up Competition에서 우승 솔루션으로 사용되었습니다.
