---
$id: ent_paper_vigor_visual_goal_in_context_i_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VIGOR: Visual Goal-In-Context Inference for Unified Humanoid Fall Safety'
  zh: 'VIGOR: Visual Goal-In-Context Inference for Unified Humanoid Fall Safety'
  ko: 'VIGOR: Visual Goal-In-Context Inference for Unified Humanoid Fall Safety'
summary:
  en: 'VIGOR: Visual Goal-In-Context Inference for Unified Humanoid Fall Safety is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  zh: 'VIGOR: Visual Goal-In-Context Inference for Unified Humanoid Fall Safety is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  ko: 'VIGOR: Visual Goal-In-Context Inference for Unified Humanoid Fall Safety is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.'
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
- vigor
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.16511v2.
sources:
- id: src_001
  type: paper
  title: 'VIGOR: Visual Goal-In-Context Inference for Unified Humanoid Fall Safety (arXiv)'
  url: https://arxiv.org/abs/2602.16511
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Reliable fall recovery is critical for humanoids operating in cluttered environments. Unlike quadrupeds or wheeled robots, humanoids experience high-energy impacts, complex whole-body contact, and large viewpoint changes during a fall, making recovery essential for continued operation. Existing methods fragment fall safety into separate problems such as fall avoidance, impact mitigation, and stand-up recovery, or rely on end-to-end policies trained without vision through reinforcement learning or imitation learning, often on flat terrain. At a deeper level, fall safety is treated as monolithic data complexity, coupling pose, dynamics, and terrain and requiring exhaustive coverage, limiting scalability and generalization. We present a unified fall safety approach that spans all phases of fall recovery. It builds on two insights: 1) Natural human fall and recovery poses are highly constrained and transferable from flat to complex terrain through alignment, and 2) Fast whole-body reactions require integrated perceptual-motor representations. We train a privileged teacher using sparse human demonstrations on flat terrain and simulated complex terrains, and distill it into a deployable student that relies only on egocentric depth and proprioception. The student learns how to react by matching the teacher's goal-in-context latent representation, which combines the next target pose with the local terrain, rather than separately encoding what it must perceive and how it must act. Results in simulation and on a real Unitree G1 humanoid demonstrate robust, zero-shot fall safety across diverse non-flat environments without real-world fine-tuning. The project page is available at https://vigor2026.github.io/

## 核心内容
Reliable fall recovery is critical for humanoids operating in cluttered environments. Unlike quadrupeds or wheeled robots, humanoids experience high-energy impacts, complex whole-body contact, and large viewpoint changes during a fall, making recovery essential for continued operation. Existing methods fragment fall safety into separate problems such as fall avoidance, impact mitigation, and stand-up recovery, or rely on end-to-end policies trained without vision through reinforcement learning or imitation learning, often on flat terrain. At a deeper level, fall safety is treated as monolithic data complexity, coupling pose, dynamics, and terrain and requiring exhaustive coverage, limiting scalability and generalization. We present a unified fall safety approach that spans all phases of fall recovery. It builds on two insights: 1) Natural human fall and recovery poses are highly constrained and transferable from flat to complex terrain through alignment, and 2) Fast whole-body reactions require integrated perceptual-motor representations. We train a privileged teacher using sparse human demonstrations on flat terrain and simulated complex terrains, and distill it into a deployable student that relies only on egocentric depth and proprioception. The student learns how to react by matching the teacher's goal-in-context latent representation, which combines the next target pose with the local terrain, rather than separately encoding what it must perceive and how it must act. Results in simulation and on a real Unitree G1 humanoid demonstrate robust, zero-shot fall safety across diverse non-flat environments without real-world fine-tuning. The project page is available at https://vigor2026.github.io/

## 参考
- http://arxiv.org/abs/2602.16511v2

## Overview
Reliable fall recovery is critical for humanoids operating in cluttered environments. Unlike quadrupeds or wheeled robots, humanoids experience high-energy impacts, complex whole-body contact, and large viewpoint changes during a fall, making recovery essential for continued operation. Existing methods fragment fall safety into separate problems such as fall avoidance, impact mitigation, and stand-up recovery, or rely on end-to-end policies trained without vision through reinforcement learning or imitation learning, often on flat terrain. At a deeper level, fall safety is treated as monolithic data complexity, coupling pose, dynamics, and terrain and requiring exhaustive coverage, limiting scalability and generalization. We present a unified fall safety approach that spans all phases of fall recovery. It builds on two insights: 1) Natural human fall and recovery poses are highly constrained and transferable from flat to complex terrain through alignment, and 2) Fast whole-body reactions require integrated perceptual-motor representations. We train a privileged teacher using sparse human demonstrations on flat terrain and simulated complex terrains, and distill it into a deployable student that relies only on egocentric depth and proprioception. The student learns how to react by matching the teacher's goal-in-context latent representation, which combines the next target pose with the local terrain, rather than separately encoding what it must perceive and how it must act. Results in simulation and on a real Unitree G1 humanoid demonstrate robust, zero-shot fall safety across diverse non-flat environments without real-world fine-tuning. The project page is available at https://vigor2026.github.io/

## Content
Reliable fall recovery is critical for humanoids operating in cluttered environments. Unlike quadrupeds or wheeled robots, humanoids experience high-energy impacts, complex whole-body contact, and large viewpoint changes during a fall, making recovery essential for continued operation. Existing methods fragment fall safety into separate problems such as fall avoidance, impact mitigation, and stand-up recovery, or rely on end-to-end policies trained without vision through reinforcement learning or imitation learning, often on flat terrain. At a deeper level, fall safety is treated as monolithic data complexity, coupling pose, dynamics, and terrain and requiring exhaustive coverage, limiting scalability and generalization. We present a unified fall safety approach that spans all phases of fall recovery. It builds on two insights: 1) Natural human fall and recovery poses are highly constrained and transferable from flat to complex terrain through alignment, and 2) Fast whole-body reactions require integrated perceptual-motor representations. We train a privileged teacher using sparse human demonstrations on flat terrain and simulated complex terrains, and distill it into a deployable student that relies only on egocentric depth and proprioception. The student learns how to react by matching the teacher's goal-in-context latent representation, which combines the next target pose with the local terrain, rather than separately encoding what it must perceive and how it must act. Results in simulation and on a real Unitree G1 humanoid demonstrate robust, zero-shot fall safety across diverse non-flat environments without real-world fine-tuning. The project page is available at https://vigor2026.github.io/

## 개요
혼잡한 환경에서 작동하는 휴머노이드에게 신뢰할 수 있는 낙상 회복은 매우 중요합니다. 사족 보행 로봇이나 바퀴 달린 로봇과 달리, 휴머노이드는 낙상 중에 고에너지 충격, 복잡한 전신 접촉, 큰 시점 변화를 겪기 때문에 지속적인 작동을 위해 회복이 필수적입니다. 기존 방법들은 낙상 안전을 낙상 회피, 충격 완화, 기립 회복과 같은 개별 문제로 분할하거나, 평평한 지형에서 강화 학습이나 모방 학습을 통해 시각 없이 훈련된 종단간 정책에 의존합니다. 더 깊은 수준에서 보면, 낙상 안전은 자세, 동역학, 지형을 결합하고 완전한 커버리지를 요구하는 모놀리식 데이터 복잡성으로 취급되어 확장성과 일반화를 제한합니다. 우리는 낙상 회복의 모든 단계를 포괄하는 통합된 낙상 안전 접근법을 제시합니다. 이는 두 가지 통찰에 기반합니다: 1) 자연스러운 인간의 낙상 및 회복 자세는 매우 제한적이며 정렬을 통해 평평한 지형에서 복잡한 지형으로 전이 가능하고, 2) 빠른 전신 반응에는 통합된 지각-운동 표현이 필요합니다. 우리는 평평한 지형에서의 희소한 인간 시연과 시뮬레이션된 복잡한 지형을 사용하여 특권 교사를 훈련시키고, 이를 자기중심적 깊이와 고유수용감각에만 의존하는 배치 가능한 학생으로 증류합니다. 학생은 무엇을 인지해야 하고 어떻게 행동해야 하는지를 별도로 인코딩하는 대신, 다음 목표 자세와 로컬 지형을 결합한 교사의 맥락 내 목표 잠재 표현을 일치시킴으로써 반응하는 방법을 학습합니다. 시뮬레이션과 실제 Unitree G1 휴머노이드에서의 결과는 실제 환경 미세 조정 없이 다양한 비평평 환경에서 강력한 제로샷 낙상 안전을 입증합니다. 프로젝트 페이지는 https://vigor2026.github.io/ 에서 확인할 수 있습니다.

## 핵심 내용
혼잡한 환경에서 작동하는 휴머노이드에게 신뢰할 수 있는 낙상 회복은 매우 중요합니다. 사족 보행 로봇이나 바퀴 달린 로봇과 달리, 휴머노이드는 낙상 중에 고에너지 충격, 복잡한 전신 접촉, 큰 시점 변화를 겪기 때문에 지속적인 작동을 위해 회복이 필수적입니다. 기존 방법들은 낙상 안전을 낙상 회피, 충격 완화, 기립 회복과 같은 개별 문제로 분할하거나, 평평한 지형에서 강화 학습이나 모방 학습을 통해 시각 없이 훈련된 종단간 정책에 의존합니다. 더 깊은 수준에서 보면, 낙상 안전은 자세, 동역학, 지형을 결합하고 완전한 커버리지를 요구하는 모놀리식 데이터 복잡성으로 취급되어 확장성과 일반화를 제한합니다. 우리는 낙상 회복의 모든 단계를 포괄하는 통합된 낙상 안전 접근법을 제시합니다. 이는 두 가지 통찰에 기반합니다: 1) 자연스러운 인간의 낙상 및 회복 자세는 매우 제한적이며 정렬을 통해 평평한 지형에서 복잡한 지형으로 전이 가능하고, 2) 빠른 전신 반응에는 통합된 지각-운동 표현이 필요합니다. 우리는 평평한 지형에서의 희소한 인간 시연과 시뮬레이션된 복잡한 지형을 사용하여 특권 교사를 훈련시키고, 이를 자기중심적 깊이와 고유수용감각에만 의존하는 배치 가능한 학생으로 증류합니다. 학생은 무엇을 인지해야 하고 어떻게 행동해야 하는지를 별도로 인코딩하는 대신, 다음 목표 자세와 로컬 지형을 결합한 교사의 맥락 내 목표 잠재 표현을 일치시킴으로써 반응하는 방법을 학습합니다. 시뮬레이션과 실제 Unitree G1 휴머노이드에서의 결과는 실제 환경 미세 조정 없이 다양한 비평평 환경에서 강력한 제로샷 낙상 안전을 입증합니다. 프로젝트 페이지는 https://vigor2026.github.io/ 에서 확인할 수 있습니다.
