---
$id: ent_paper_towards_versatile_humanoid_tab_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Towards Versatile Humanoid Table Tennis: Unified Reinforcement Learning with Prediction Augmentation'
  zh: 'Towards Versatile Humanoid Table Tennis: Unified Reinforcement Learning with Prediction Augmentation'
  ko: 'Towards Versatile Humanoid Table Tennis: Unified Reinforcement Learning with Prediction Augmentation'
summary:
  en: 'Towards Versatile Humanoid Table Tennis: Unified Reinforcement Learning with Prediction Augmentation is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
  zh: 'Towards Versatile Humanoid Table Tennis: Unified Reinforcement Learning with Prediction Augmentation is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
  ko: 'Towards Versatile Humanoid Table Tennis: Unified Reinforcement Learning with Prediction Augmentation is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
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
- loco_manipulation
- towards_versatile_humanoid_tab
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.21690v4.
sources:
- id: src_001
  type: paper
  title: 'Towards Versatile Humanoid Table Tennis: Unified Reinforcement Learning with Prediction Augmentation (arXiv)'
  url: https://arxiv.org/abs/2509.21690
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid table tennis (TT) demands rapid perception, proactive whole-body motion, and agile footwork under strict timing--capabilities that remain difficult for end-to-end control policies. We propose a reinforcement learning (RL) framework that maps ball-position observations directly to whole-body joint commands for both arm striking and leg locomotion, strengthened by predictive signals and dense, physics-guided rewards. A lightweight learned predictor, fed with recent ball positions, estimates future ball states and augments the policy's observations for proactive decision-making. During training, a physics-based predictor supplies precise future states to construct dense, informative rewards that lead to effective exploration. The resulting policy attains strong performance across varied serve ranges (hit rate$\geq$96% and success rate$\geq$92%) in simulations. Ablation studies confirm that both the learned predictor and the predictive reward design are critical for end-to-end learning. Deployed zero-shot on a physical Booster T1 humanoid with 23 revolute joints, the policy produces coordinated lateral and forward-backward footwork with accurate, fast returns, suggesting a practical path toward versatile, competitive humanoid TT. We have open-sourced our RL training code at: https://github.com/purdue-tracelab/TTRL-ICRA2026

## 核心内容
Humanoid table tennis (TT) demands rapid perception, proactive whole-body motion, and agile footwork under strict timing--capabilities that remain difficult for end-to-end control policies. We propose a reinforcement learning (RL) framework that maps ball-position observations directly to whole-body joint commands for both arm striking and leg locomotion, strengthened by predictive signals and dense, physics-guided rewards. A lightweight learned predictor, fed with recent ball positions, estimates future ball states and augments the policy's observations for proactive decision-making. During training, a physics-based predictor supplies precise future states to construct dense, informative rewards that lead to effective exploration. The resulting policy attains strong performance across varied serve ranges (hit rate$\geq$96% and success rate$\geq$92%) in simulations. Ablation studies confirm that both the learned predictor and the predictive reward design are critical for end-to-end learning. Deployed zero-shot on a physical Booster T1 humanoid with 23 revolute joints, the policy produces coordinated lateral and forward-backward footwork with accurate, fast returns, suggesting a practical path toward versatile, competitive humanoid TT. We have open-sourced our RL training code at: https://github.com/purdue-tracelab/TTRL-ICRA2026

## 参考
- http://arxiv.org/abs/2509.21690v4

## Overview
Humanoid table tennis (TT) demands rapid perception, proactive whole-body motion, and agile footwork under strict timing—capabilities that remain difficult for end-to-end control policies. We propose a reinforcement learning (RL) framework that maps ball-position observations directly to whole-body joint commands for both arm striking and leg locomotion, strengthened by predictive signals and dense, physics-guided rewards. A lightweight learned predictor, fed with recent ball positions, estimates future ball states and augments the policy's observations for proactive decision-making. During training, a physics-based predictor supplies precise future states to construct dense, informative rewards that lead to effective exploration. The resulting policy attains strong performance across varied serve ranges (hit rate\(\geq\)96% and success rate\(\geq\)92%) in simulations. Ablation studies confirm that both the learned predictor and the predictive reward design are critical for end-to-end learning. Deployed zero-shot on a physical Booster T1 humanoid with 23 revolute joints, the policy produces coordinated lateral and forward-backward footwork with accurate, fast returns, suggesting a practical path toward versatile, competitive humanoid TT. We have open-sourced our RL training code at: https://github.com/purdue-tracelab/TTRL-ICRA2026

## Content
Humanoid table tennis (TT) demands rapid perception, proactive whole-body motion, and agile footwork under strict timing—capabilities that remain difficult for end-to-end control policies. We propose a reinforcement learning (RL) framework that maps ball-position observations directly to whole-body joint commands for both arm striking and leg locomotion, strengthened by predictive signals and dense, physics-guided rewards. A lightweight learned predictor, fed with recent ball positions, estimates future ball states and augments the policy's observations for proactive decision-making. During training, a physics-based predictor supplies precise future states to construct dense, informative rewards that lead to effective exploration. The resulting policy attains strong performance across varied serve ranges (hit rate\(\geq\)96% and success rate\(\geq\)92%) in simulations. Ablation studies confirm that both the learned predictor and the predictive reward design are critical for end-to-end learning. Deployed zero-shot on a physical Booster T1 humanoid with 23 revolute joints, the policy produces coordinated lateral and forward-backward footwork with accurate, fast returns, suggesting a practical path toward versatile, competitive humanoid TT. We have open-sourced our RL training code at: https://github.com/purdue-tracelab/TTRL-ICRA2026

## 개요
휴머노이드 탁구(TT)는 엄격한 타이밍 하에서 빠른 인지, 능동적인 전신 동작, 민첩한 풋워크를 요구하며, 이는 엔드투엔드 제어 정책으로는 여전히 달성하기 어려운 능력입니다. 본 연구에서는 공 위치 관측값을 팔 스트라이킹과 다리 로코모션을 위한 전신 관절 명령에 직접 매핑하는 강화 학습(RL) 프레임워크를 제안하며, 예측 신호와 조밀한 물리 기반 보상으로 강화되었습니다. 최근 공 위치를 입력으로 받는 경량 학습 예측기가 미래 공 상태를 추정하여 정책의 관측값을 보강함으로써 능동적인 의사 결정을 가능하게 합니다. 훈련 중에는 물리 기반 예측기가 정확한 미래 상태를 제공하여 조밀하고 유용한 보상을 구성함으로써 효과적인 탐색을 유도합니다. 결과 정책은 다양한 서브 범위(타격률 $\geq$96%, 성공률 $\geq$92%)에서 시뮬레이션 내 강력한 성능을 달성합니다. 절제 연구는 학습 예측기와 예측 보상 설계 모두 엔드투엔드 학습에 중요함을 확인합니다. 23개의 회전 관절을 가진 실제 Booster T1 휴머노이드에 제로샷으로 배포된 정책은 정확하고 빠른 리턴과 함께 조화로운 좌우 및 전후 풋워크를 생성하여, 다재다능하고 경쟁력 있는 휴머노이드 탁구를 위한 실용적인 경로를 제시합니다. RL 훈련 코드를 다음에서 오픈소스로 공개했습니다: https://github.com/purdue-tracelab/TTRL-ICRA2026

## 핵심 내용
휴머노이드 탁구(TT)는 엄격한 타이밍 하에서 빠른 인지, 능동적인 전신 동작, 민첩한 풋워크를 요구하며, 이는 엔드투엔드 제어 정책으로는 여전히 달성하기 어려운 능력입니다. 본 연구에서는 공 위치 관측값을 팔 스트라이킹과 다리 로코모션을 위한 전신 관절 명령에 직접 매핑하는 강화 학습(RL) 프레임워크를 제안하며, 예측 신호와 조밀한 물리 기반 보상으로 강화되었습니다. 최근 공 위치를 입력으로 받는 경량 학습 예측기가 미래 공 상태를 추정하여 정책의 관측값을 보강함으로써 능동적인 의사 결정을 가능하게 합니다. 훈련 중에는 물리 기반 예측기가 정확한 미래 상태를 제공하여 조밀하고 유용한 보상을 구성함으로써 효과적인 탐색을 유도합니다. 결과 정책은 다양한 서브 범위(타격률 $\geq$96%, 성공률 $\geq$92%)에서 시뮬레이션 내 강력한 성능을 달성합니다. 절제 연구는 학습 예측기와 예측 보상 설계 모두 엔드투엔드 학습에 중요함을 확인합니다. 23개의 회전 관절을 가진 실제 Booster T1 휴머노이드에 제로샷으로 배포된 정책은 정확하고 빠른 리턴과 함께 조화로운 좌우 및 전후 풋워크를 생성하여, 다재다능하고 경쟁력 있는 휴머노이드 탁구를 위한 실용적인 경로를 제시합니다. RL 훈련 코드를 다음에서 오픈소스로 공개했습니다: https://github.com/purdue-tracelab/TTRL-ICRA2026
