---
$id: ent_paper_sampling_based_system_identifi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Sampling-Based System Identification with Active Exploration for Legged Robot Sim2Real Learning
  zh: Sampling-Based System Identification with Active Exploration for Legged Robot Sim2Real Learning
  ko: Sampling-Based System Identification with Active Exploration for Legged Robot Sim2Real Learning
summary:
  en: Sampling-Based System Identification with Active Exploration for Legged Robot Sim2Real Learning is a 2025 work on sim-to-real
    for humanoid robots.
  zh: Sampling-Based System Identification with Active Exploration for Legged Robot Sim2Real Learning is a 2025 work on sim-to-real
    for humanoid robots.
  ko: Sampling-Based System Identification with Active Exploration for Legged Robot Sim2Real Learning is a 2025 work on sim-to-real
    for humanoid robots.
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
- sampling_based_system_identifi
- sim_to_real
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.14266v1.
sources:
- id: src_001
  type: paper
  title: Sampling-Based System Identification with Active Exploration for Legged Robot Sim2Real Learning (arXiv)
  url: https://arxiv.org/abs/2505.14266
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Sim-to-real discrepancies hinder learning-based policies from achieving high-precision tasks in the real world. While Domain Randomization (DR) is commonly used to bridge this gap, it often relies on heuristics and can lead to overly conservative policies with degrading performance when not properly tuned. System Identification (Sys-ID) offers a targeted approach, but standard techniques rely on differentiable dynamics and/or direct torque measurement, assumptions that rarely hold for contact-rich legged systems. To this end, we present SPI-Active (Sampling-based Parameter Identification with Active Exploration), a two-stage framework that estimates physical parameters of legged robots to minimize the sim-to-real gap. SPI-Active robustly identifies key physical parameters through massive parallel sampling, minimizing state prediction errors between simulated and real-world trajectories. To further improve the informativeness of collected data, we introduce an active exploration strategy that maximizes the Fisher Information of the collected real-world trajectories via optimizing the input commands of an exploration policy. This targeted exploration leads to accurate identification and better generalization across diverse tasks. Experiments demonstrate that SPI-Active enables precise sim-to-real transfer of learned policies to the real world, outperforming baselines by 42-63% in various locomotion tasks.

## 核心内容
Sim-to-real discrepancies hinder learning-based policies from achieving high-precision tasks in the real world. While Domain Randomization (DR) is commonly used to bridge this gap, it often relies on heuristics and can lead to overly conservative policies with degrading performance when not properly tuned. System Identification (Sys-ID) offers a targeted approach, but standard techniques rely on differentiable dynamics and/or direct torque measurement, assumptions that rarely hold for contact-rich legged systems. To this end, we present SPI-Active (Sampling-based Parameter Identification with Active Exploration), a two-stage framework that estimates physical parameters of legged robots to minimize the sim-to-real gap. SPI-Active robustly identifies key physical parameters through massive parallel sampling, minimizing state prediction errors between simulated and real-world trajectories. To further improve the informativeness of collected data, we introduce an active exploration strategy that maximizes the Fisher Information of the collected real-world trajectories via optimizing the input commands of an exploration policy. This targeted exploration leads to accurate identification and better generalization across diverse tasks. Experiments demonstrate that SPI-Active enables precise sim-to-real transfer of learned policies to the real world, outperforming baselines by 42-63% in various locomotion tasks.

## 参考
- http://arxiv.org/abs/2505.14266v1

## Overview
Sim-to-real discrepancies hinder learning-based policies from achieving high-precision tasks in the real world. While Domain Randomization (DR) is commonly used to bridge this gap, it often relies on heuristics and can lead to overly conservative policies with degrading performance when not properly tuned. System Identification (Sys-ID) offers a targeted approach, but standard techniques rely on differentiable dynamics and/or direct torque measurement, assumptions that rarely hold for contact-rich legged systems. To this end, we present SPI-Active (Sampling-based Parameter Identification with Active Exploration), a two-stage framework that estimates physical parameters of legged robots to minimize the sim-to-real gap. SPI-Active robustly identifies key physical parameters through massive parallel sampling, minimizing state prediction errors between simulated and real-world trajectories. To further improve the informativeness of collected data, we introduce an active exploration strategy that maximizes the Fisher Information of the collected real-world trajectories via optimizing the input commands of an exploration policy. This targeted exploration leads to accurate identification and better generalization across diverse tasks. Experiments demonstrate that SPI-Active enables precise sim-to-real transfer of learned policies to the real world, outperforming baselines by 42-63% in various locomotion tasks.

## Content
Sim-to-real discrepancies hinder learning-based policies from achieving high-precision tasks in the real world. While Domain Randomization (DR) is commonly used to bridge this gap, it often relies on heuristics and can lead to overly conservative policies with degrading performance when not properly tuned. System Identification (Sys-ID) offers a targeted approach, but standard techniques rely on differentiable dynamics and/or direct torque measurement, assumptions that rarely hold for contact-rich legged systems. To this end, we present SPI-Active (Sampling-based Parameter Identification with Active Exploration), a two-stage framework that estimates physical parameters of legged robots to minimize the sim-to-real gap. SPI-Active robustly identifies key physical parameters through massive parallel sampling, minimizing state prediction errors between simulated and real-world trajectories. To further improve the informativeness of collected data, we introduce an active exploration strategy that maximizes the Fisher Information of the collected real-world trajectories via optimizing the input commands of an exploration policy. This targeted exploration leads to accurate identification and better generalization across diverse tasks. Experiments demonstrate that SPI-Active enables precise sim-to-real transfer of learned policies to the real world, outperforming baselines by 42-63% in various locomotion tasks.

## 개요
Sim-to-real 불일치는 학습 기반 정책이 실제 세계에서 고정밀 작업을 수행하는 것을 방해합니다. 도메인 무작위화(DR)는 이러한 격차를 해소하기 위해 일반적으로 사용되지만, 종종 휴리스틱에 의존하며 적절히 조정되지 않으면 성능이 저하되는 지나치게 보수적인 정책으로 이어질 수 있습니다. 시스템 식별(Sys-ID)은 목표 지향적인 접근 방식을 제공하지만, 표준 기술은 미분 가능한 동역학 및/또는 직접 토크 측정에 의존하며, 이러한 가정은 접촉이 많은 보행 시스템에서는 거의 성립하지 않습니다. 이를 위해, 우리는 SPI-Active(능동 탐색을 통한 샘플링 기반 파라미터 식별)를 제시합니다. 이는 보행 로봇의 물리적 파라미터를 추정하여 sim-to-real 격차를 최소화하는 2단계 프레임워크입니다. SPI-Active는 대규모 병렬 샘플링을 통해 주요 물리적 파라미터를 강건하게 식별하며, 시뮬레이션과 실제 궤적 간의 상태 예측 오차를 최소화합니다. 수집된 데이터의 정보성을 더욱 향상시키기 위해, 우리는 탐색 정책의 입력 명령을 최적화하여 수집된 실제 궤적의 피셔 정보(Fisher Information)를 최대화하는 능동 탐색 전략을 도입합니다. 이 목표 지향적인 탐색은 정확한 식별과 다양한 작업에 걸친 더 나은 일반화를 가능하게 합니다. 실험 결과, SPI-Active는 학습된 정책의 실제 세계로의 정밀한 sim-to-real 전이를 가능하게 하며, 다양한 보행 작업에서 기준선 대비 42-63% 더 나은 성능을 보여줍니다.

## 핵심 내용
Sim-to-real 불일치는 학습 기반 정책이 실제 세계에서 고정밀 작업을 수행하는 것을 방해합니다. 도메인 무작위화(DR)는 이러한 격차를 해소하기 위해 일반적으로 사용되지만, 종종 휴리스틱에 의존하며 적절히 조정되지 않으면 성능이 저하되는 지나치게 보수적인 정책으로 이어질 수 있습니다. 시스템 식별(Sys-ID)은 목표 지향적인 접근 방식을 제공하지만, 표준 기술은 미분 가능한 동역학 및/또는 직접 토크 측정에 의존하며, 이러한 가정은 접촉이 많은 보행 시스템에서는 거의 성립하지 않습니다. 이를 위해, 우리는 SPI-Active(능동 탐색을 통한 샘플링 기반 파라미터 식별)를 제시합니다. 이는 보행 로봇의 물리적 파라미터를 추정하여 sim-to-real 격차를 최소화하는 2단계 프레임워크입니다. SPI-Active는 대규모 병렬 샘플링을 통해 주요 물리적 파라미터를 강건하게 식별하며, 시뮬레이션과 실제 궤적 간의 상태 예측 오차를 최소화합니다. 수집된 데이터의 정보성을 더욱 향상시키기 위해, 우리는 탐색 정책의 입력 명령을 최적화하여 수집된 실제 궤적의 피셔 정보(Fisher Information)를 최대화하는 능동 탐색 전략을 도입합니다. 이 목표 지향적인 탐색은 정확한 식별과 다양한 작업에 걸친 더 나은 일반화를 가능하게 합니다. 실험 결과, SPI-Active는 학습된 정책의 실제 세계로의 정밀한 sim-to-real 전이를 가능하게 하며, 다양한 보행 작업에서 기준선 대비 42-63% 더 나은 성능을 보여줍니다.
