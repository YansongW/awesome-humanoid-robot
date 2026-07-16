---
$id: ent_paper_torne_reconciling_reality_through_si_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Reconciling Reality through Simulation: A Real-to-Sim-to-Real Approach for Robust Manipulation'
  zh: 通过仿真调和现实：面向稳健操作的实到仿再到实方法
  ko: '시뮬레이션을 통한 현실 조화: 견고한 조작을 위한 Real-to-Sim-to-Real 접근법'
summary:
  en: RialTo builds on-the-fly digital-twin simulations from real-world scans and transfers real-world demonstrations into
    simulation via a novel inverse-distillation procedure, then uses reinforcement learning to robustify imitation-learning
    policies with minimal human supervision.
  zh: RialTo 从真实世界扫描即时构建数字孪生仿真环境，通过一种新颖的逆蒸馏过程将真实世界演示迁移到仿真中，并利用强化学习在最小人类监督下增强模仿学习策略的鲁棒性。
  ko: RialTo는 실제 세계 스캔에서 즉석에서 디지털 트윈 시뮬레이션을 구축하고, 새로운 역증류 절차를 통해 실제 세계 시연을 시뮬레이션으로 전달한 다음, 최소한의 인간 감독으로 모방 학습 정책을 강화하기 위해
    강화 학습을 사용합니다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- digital_twin
- real_to_sim_to_real
- sim_to_real
- inverse_distillation
- imitation_learning
- reinforcement_learning
- visuomotor_policy
- robust_manipulation
- isaac_sim
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.03949v3.
sources:
- id: src_001
  type: paper
  title: 'Reconciling Reality through Simulation: A Real-to-Sim-to-Real Approach for Robust Manipulation'
  url: https://arxiv.org/abs/2403.03949
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Imitation learning methods need significant human supervision to learn policies robust to changes in object poses, physical disturbances, and visual distractors. Reinforcement learning, on the other hand, can explore the environment autonomously to learn robust behaviors but may require impractical amounts of unsafe real-world data collection. To learn performant, robust policies without the burden of unsafe real-world data collection or extensive human supervision, we propose RialTo, a system for robustifying real-world imitation learning policies via reinforcement learning in "digital twin" simulation environments constructed on the fly from small amounts of real-world data. To enable this real-to-sim-to-real pipeline, RialTo proposes an easy-to-use interface for quickly scanning and constructing digital twins of real-world environments. We also introduce a novel "inverse distillation" procedure for bringing real-world demonstrations into simulated environments for efficient fine-tuning, with minimal human intervention and engineering required. We evaluate RialTo across a variety of robotic manipulation problems in the real world, such as robustly stacking dishes on a rack, placing books on a shelf, and six other tasks. RialTo increases (over 67%) in policy robustness without requiring extensive human data collection. Project website and videos at https://real-to-sim-to-real.github.io/RialTo/

## 核心内容
Imitation learning methods need significant human supervision to learn policies robust to changes in object poses, physical disturbances, and visual distractors. Reinforcement learning, on the other hand, can explore the environment autonomously to learn robust behaviors but may require impractical amounts of unsafe real-world data collection. To learn performant, robust policies without the burden of unsafe real-world data collection or extensive human supervision, we propose RialTo, a system for robustifying real-world imitation learning policies via reinforcement learning in "digital twin" simulation environments constructed on the fly from small amounts of real-world data. To enable this real-to-sim-to-real pipeline, RialTo proposes an easy-to-use interface for quickly scanning and constructing digital twins of real-world environments. We also introduce a novel "inverse distillation" procedure for bringing real-world demonstrations into simulated environments for efficient fine-tuning, with minimal human intervention and engineering required. We evaluate RialTo across a variety of robotic manipulation problems in the real world, such as robustly stacking dishes on a rack, placing books on a shelf, and six other tasks. RialTo increases (over 67%) in policy robustness without requiring extensive human data collection. Project website and videos at https://real-to-sim-to-real.github.io/RialTo/

## 参考
- http://arxiv.org/abs/2403.03949v3

## Overview
Imitation learning methods need significant human supervision to learn policies robust to changes in object poses, physical disturbances, and visual distractors. Reinforcement learning, on the other hand, can explore the environment autonomously to learn robust behaviors but may require impractical amounts of unsafe real-world data collection. To learn performant, robust policies without the burden of unsafe real-world data collection or extensive human supervision, we propose RialTo, a system for robustifying real-world imitation learning policies via reinforcement learning in "digital twin" simulation environments constructed on the fly from small amounts of real-world data. To enable this real-to-sim-to-real pipeline, RialTo proposes an easy-to-use interface for quickly scanning and constructing digital twins of real-world environments. We also introduce a novel "inverse distillation" procedure for bringing real-world demonstrations into simulated environments for efficient fine-tuning, with minimal human intervention and engineering required. We evaluate RialTo across a variety of robotic manipulation problems in the real world, such as robustly stacking dishes on a rack, placing books on a shelf, and six other tasks. RialTo increases (over 67%) in policy robustness without requiring extensive human data collection. Project website and videos at https://real-to-sim-to-real.github.io/RialTo/

## Content
Imitation learning methods need significant human supervision to learn policies robust to changes in object poses, physical disturbances, and visual distractors. Reinforcement learning, on the other hand, can explore the environment autonomously to learn robust behaviors but may require impractical amounts of unsafe real-world data collection. To learn performant, robust policies without the burden of unsafe real-world data collection or extensive human supervision, we propose RialTo, a system for robustifying real-world imitation learning policies via reinforcement learning in "digital twin" simulation environments constructed on the fly from small amounts of real-world data. To enable this real-to-sim-to-real pipeline, RialTo proposes an easy-to-use interface for quickly scanning and constructing digital twins of real-world environments. We also introduce a novel "inverse distillation" procedure for bringing real-world demonstrations into simulated environments for efficient fine-tuning, with minimal human intervention and engineering required. We evaluate RialTo across a variety of robotic manipulation problems in the real world, such as robustly stacking dishes on a rack, placing books on a shelf, and six other tasks. RialTo increases (over 67%) in policy robustness without requiring extensive human data collection. Project website and videos at https://real-to-sim-to-real.github.io/RialTo/

## 개요
모방 학습 방법은 객체 자세 변화, 물리적 교란, 시각적 방해 요소에 강건한 정책을 학습하기 위해 상당한 인간의 감독이 필요합니다. 반면, 강화 학습은 환경을 자율적으로 탐색하여 강건한 행동을 학습할 수 있지만, 비현실적인 양의 안전하지 않은 실제 데이터 수집이 필요할 수 있습니다. 안전하지 않은 실제 데이터 수집이나 광범위한 인간 감독의 부담 없이 성능이 뛰어나고 강건한 정책을 학습하기 위해, 우리는 소량의 실제 데이터로 즉시 구축된 "디지털 트윈" 시뮬레이션 환경에서 강화 학습을 통해 실제 모방 학습 정책을 강건화하는 시스템인 RialTo를 제안합니다. 이 실제-시뮬레이션-실제 파이프라인을 가능하게 하기 위해, RialTo는 실제 환경의 디지털 트윈을 빠르게 스캔하고 구축할 수 있는 사용하기 쉬운 인터페이스를 제안합니다. 또한, 최소한의 인간 개입과 엔지니어링으로 실제 시연을 시뮬레이션 환경으로 가져와 효율적인 미세 조정을 수행하는 새로운 "역증류" 절차를 소개합니다. 우리는 접시를 선반에 강건하게 쌓기, 책을 책장에 놓기 등 여섯 가지 추가 작업을 포함한 다양한 실제 로봇 조작 문제에서 RialTo를 평가합니다. RialTo는 광범위한 인간 데이터 수집 없이 정책 강건성을 67% 이상 향상시킵니다. 프로젝트 웹사이트 및 비디오: https://real-to-sim-to-real.github.io/RialTo/

## 핵심 내용
모방 학습 방법은 객체 자세 변화, 물리적 교란, 시각적 방해 요소에 강건한 정책을 학습하기 위해 상당한 인간의 감독이 필요합니다. 반면, 강화 학습은 환경을 자율적으로 탐색하여 강건한 행동을 학습할 수 있지만, 비현실적인 양의 안전하지 않은 실제 데이터 수집이 필요할 수 있습니다. 안전하지 않은 실제 데이터 수집이나 광범위한 인간 감독의 부담 없이 성능이 뛰어나고 강건한 정책을 학습하기 위해, 우리는 소량의 실제 데이터로 즉시 구축된 "디지털 트윈" 시뮬레이션 환경에서 강화 학습을 통해 실제 모방 학습 정책을 강건화하는 시스템인 RialTo를 제안합니다. 이 실제-시뮬레이션-실제 파이프라인을 가능하게 하기 위해, RialTo는 실제 환경의 디지털 트윈을 빠르게 스캔하고 구축할 수 있는 사용하기 쉬운 인터페이스를 제안합니다. 또한, 최소한의 인간 개입과 엔지니어링으로 실제 시연을 시뮬레이션 환경으로 가져와 효율적인 미세 조정을 수행하는 새로운 "역증류" 절차를 소개합니다. 우리는 접시를 선반에 강건하게 쌓기, 책을 책장에 놓기 등 여섯 가지 추가 작업을 포함한 다양한 실제 로봇 조작 문제에서 RialTo를 평가합니다. RialTo는 광범위한 인간 데이터 수집 없이 정책 강건성을 67% 이상 향상시킵니다. 프로젝트 웹사이트 및 비디오: https://real-to-sim-to-real.github.io/RialTo/
