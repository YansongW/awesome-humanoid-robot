---
$id: ent_paper_polysim_bridging_the_sim_to_re_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PolySim: Bridging the Sim-to-Real Gap for Humanoid Control via Multi-Simulator Dynamics Randomization'
  zh: 'PolySim: Bridging the Sim-to-Real Gap for Humanoid Control via Multi-Simulator Dynamics Randomization'
  ko: 'PolySim: Bridging the Sim-to-Real Gap for Humanoid Control via Multi-Simulator Dynamics Randomization'
summary:
  en: 'PolySim: Bridging the Sim-to-Real Gap for Humanoid Control via Multi-Simulator Dynamics Randomization is a 2025 work
    on sim-to-real for humanoid robots.'
  zh: 'PolySim: Bridging the Sim-to-Real Gap for Humanoid Control via Multi-Simulator Dynamics Randomization is a 2025 work
    on sim-to-real for humanoid robots.'
  ko: 'PolySim: Bridging the Sim-to-Real Gap for Humanoid Control via Multi-Simulator Dynamics Randomization is a 2025 work
    on sim-to-real for humanoid robots.'
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
- polysim
- sim_to_real
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.01708v3.
sources:
- id: src_001
  type: paper
  title: 'PolySim: Bridging the Sim-to-Real Gap for Humanoid Control via Multi-Simulator Dynamics Randomization (arXiv)'
  url: https://arxiv.org/abs/2510.01708
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid whole-body control (WBC) policies trained in simulation often suffer from the sim-to-real gap, which fundamentally arises from simulator inductive bias, the inherent assumptions and limitations of any single simulator. These biases lead to nontrivial discrepancies both across simulators and between simulation and the real world. To mitigate the effect of simulator inductive bias, the key idea is to train policies jointly across multiple simulators, encouraging the learned controller to capture dynamics that generalize beyond any single simulator's assumptions. We thus introduce PolySim, a WBC training platform that integrates multiple heterogeneous simulators. PolySim can launch parallel environments from different engines simultaneously within a single training run, thereby realizing dynamics-level domain randomization. Theoretically, we show that PolySim yields a tighter upper bound on simulator inductive bias than single-simulator training. In experiments, PolySim substantially reduces motion-tracking error in sim-to-sim evaluations; for example, on MuJoCo, it improves execution success by 52.8 over an IsaacSim baseline. PolySim further enables zero-shot deployment on a real Unitree G1 without additional fine-tuning, showing effective transfer from simulation to the real world. We will release the PolySim code upon acceptance of this work.

## 核心内容
Humanoid whole-body control (WBC) policies trained in simulation often suffer from the sim-to-real gap, which fundamentally arises from simulator inductive bias, the inherent assumptions and limitations of any single simulator. These biases lead to nontrivial discrepancies both across simulators and between simulation and the real world. To mitigate the effect of simulator inductive bias, the key idea is to train policies jointly across multiple simulators, encouraging the learned controller to capture dynamics that generalize beyond any single simulator's assumptions. We thus introduce PolySim, a WBC training platform that integrates multiple heterogeneous simulators. PolySim can launch parallel environments from different engines simultaneously within a single training run, thereby realizing dynamics-level domain randomization. Theoretically, we show that PolySim yields a tighter upper bound on simulator inductive bias than single-simulator training. In experiments, PolySim substantially reduces motion-tracking error in sim-to-sim evaluations; for example, on MuJoCo, it improves execution success by 52.8 over an IsaacSim baseline. PolySim further enables zero-shot deployment on a real Unitree G1 without additional fine-tuning, showing effective transfer from simulation to the real world. We will release the PolySim code upon acceptance of this work.

## 参考
- http://arxiv.org/abs/2510.01708v3

## Overview
Humanoid whole-body control (WBC) policies trained in simulation often suffer from the sim-to-real gap, which fundamentally arises from simulator inductive bias, the inherent assumptions and limitations of any single simulator. These biases lead to nontrivial discrepancies both across simulators and between simulation and the real world. To mitigate the effect of simulator inductive bias, the key idea is to train policies jointly across multiple simulators, encouraging the learned controller to capture dynamics that generalize beyond any single simulator's assumptions. We thus introduce PolySim, a WBC training platform that integrates multiple heterogeneous simulators. PolySim can launch parallel environments from different engines simultaneously within a single training run, thereby realizing dynamics-level domain randomization. Theoretically, we show that PolySim yields a tighter upper bound on simulator inductive bias than single-simulator training. In experiments, PolySim substantially reduces motion-tracking error in sim-to-sim evaluations; for example, on MuJoCo, it improves execution success by 52.8 over an IsaacSim baseline. PolySim further enables zero-shot deployment on a real Unitree G1 without additional fine-tuning, showing effective transfer from simulation to the real world. We will release the PolySim code upon acceptance of this work.

## Content
Humanoid whole-body control (WBC) policies trained in simulation often suffer from the sim-to-real gap, which fundamentally arises from simulator inductive bias, the inherent assumptions and limitations of any single simulator. These biases lead to nontrivial discrepancies both across simulators and between simulation and the real world. To mitigate the effect of simulator inductive bias, the key idea is to train policies jointly across multiple simulators, encouraging the learned controller to capture dynamics that generalize beyond any single simulator's assumptions. We thus introduce PolySim, a WBC training platform that integrates multiple heterogeneous simulators. PolySim can launch parallel environments from different engines simultaneously within a single training run, thereby realizing dynamics-level domain randomization. Theoretically, we show that PolySim yields a tighter upper bound on simulator inductive bias than single-simulator training. In experiments, PolySim substantially reduces motion-tracking error in sim-to-sim evaluations; for example, on MuJoCo, it improves execution success by 52.8 over an IsaacSim baseline. PolySim further enables zero-shot deployment on a real Unitree G1 without additional fine-tuning, showing effective transfer from simulation to the real world. We will release the PolySim code upon acceptance of this work.

## 개요
시뮬레이션에서 훈련된 휴머노이드 전신 제어(WBC) 정책은 종종 시뮬레이션-실제 간극(sim-to-real gap)으로 어려움을 겪으며, 이는 근본적으로 시뮬레이터 귀납적 편향(simulator inductive bias), 즉 단일 시뮬레이터의 내재적 가정과 한계에서 비롯됩니다. 이러한 편향은 시뮬레이터 간 및 시뮬레이션과 실제 세계 간에 상당한 차이를 초래합니다. 시뮬레이터 귀납적 편향의 영향을 완화하기 위한 핵심 아이디어는 여러 시뮬레이터에서 공동으로 정책을 훈련하여 학습된 제어기가 단일 시뮬레이터의 가정을 넘어 일반화되는 동역학을 포착하도록 하는 것입니다. 이에 우리는 여러 이기종 시뮬레이터를 통합하는 WBC 훈련 플랫폼인 PolySim을 소개합니다. PolySim은 단일 훈련 실행 내에서 서로 다른 엔진의 병렬 환경을 동시에 실행하여 동역학 수준의 도메인 무작위화를 실현합니다. 이론적으로, 우리는 PolySim이 단일 시뮬레이터 훈련보다 시뮬레이터 귀납적 편향에 대한 더 엄격한 상한을 제공함을 보여줍니다. 실험에서 PolySim은 시뮬레이션 간 평가에서 동작 추적 오류를 크게 줄입니다. 예를 들어, MuJoCo에서는 IsaacSim 기준선 대비 실행 성공률을 52.8% 향상시킵니다. PolySim은 추가 미세 조정 없이 실제 Unitree G1에서 제로샷 배포를 가능하게 하여 시뮬레이션에서 실제 세계로의 효과적인 전이를 보여줍니다. 본 연구가 채택되면 PolySim 코드를 공개할 예정입니다.

## 핵심 내용
시뮬레이션에서 훈련된 휴머노이드 전신 제어(WBC) 정책은 종종 시뮬레이션-실제 간극(sim-to-real gap)으로 어려움을 겪으며, 이는 근본적으로 시뮬레이터 귀납적 편향(simulator inductive bias), 즉 단일 시뮬레이터의 내재적 가정과 한계에서 비롯됩니다. 이러한 편향은 시뮬레이터 간 및 시뮬레이션과 실제 세계 간에 상당한 차이를 초래합니다. 시뮬레이터 귀납적 편향의 영향을 완화하기 위한 핵심 아이디어는 여러 시뮬레이터에서 공동으로 정책을 훈련하여 학습된 제어기가 단일 시뮬레이터의 가정을 넘어 일반화되는 동역학을 포착하도록 하는 것입니다. 이에 우리는 여러 이기종 시뮬레이터를 통합하는 WBC 훈련 플랫폼인 PolySim을 소개합니다. PolySim은 단일 훈련 실행 내에서 서로 다른 엔진의 병렬 환경을 동시에 실행하여 동역학 수준의 도메인 무작위화를 실현합니다. 이론적으로, 우리는 PolySim이 단일 시뮬레이터 훈련보다 시뮬레이터 귀납적 편향에 대한 더 엄격한 상한을 제공함을 보여줍니다. 실험에서 PolySim은 시뮬레이션 간 평가에서 동작 추적 오류를 크게 줄입니다. 예를 들어, MuJoCo에서는 IsaacSim 기준선 대비 실행 성공률을 52.8% 향상시킵니다. PolySim은 추가 미세 조정 없이 실제 Unitree G1에서 제로샷 배포를 가능하게 하여 시뮬레이션에서 실제 세계로의 효과적인 전이를 보여줍니다. 본 연구가 채택되면 PolySim 코드를 공개할 예정입니다.
