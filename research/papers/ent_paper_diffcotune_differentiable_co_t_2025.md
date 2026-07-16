---
$id: ent_paper_diffcotune_differentiable_co_t_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DiffCoTune: Differentiable Co-Tuning for Cross-domain Robot Control'
  zh: 'DiffCoTune: Differentiable Co-Tuning for Cross-domain Robot Control'
  ko: 'DiffCoTune: Differentiable Co-Tuning for Cross-domain Robot Control'
summary:
  en: 'DiffCoTune: Differentiable Co-Tuning for Cross-domain Robot Control is a 2025 work on sim-to-real for humanoid robots.'
  zh: 'DiffCoTune: Differentiable Co-Tuning for Cross-domain Robot Control is a 2025 work on sim-to-real for humanoid robots.'
  ko: 'DiffCoTune: Differentiable Co-Tuning for Cross-domain Robot Control is a 2025 work on sim-to-real for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- diffcotune
- humanoid
- sim_to_real
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.24068v1.
sources:
- id: src_001
  type: paper
  title: 'DiffCoTune: Differentiable Co-Tuning for Cross-domain Robot Control (arXiv)'
  url: https://arxiv.org/abs/2505.24068
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The deployment of robot controllers is hindered by modeling discrepancies due to necessary simplifications for computational tractability or inaccuracies in data-generating simulators. Such discrepancies typically require ad-hoc tuning to meet the desired performance, thereby ensuring successful transfer to a target domain. We propose a framework for automated, gradient-based tuning to enhance performance in the deployment domain by leveraging differentiable simulators. Our method collects rollouts in an iterative manner to co-tune the simulator and controller parameters, enabling systematic transfer within a few trials in the deployment domain. Specifically, we formulate multi-step objectives for tuning and employ alternating optimization to effectively adapt the controller to the deployment domain. The scalability of our framework is demonstrated by co-tuning model-based and learning-based controllers of arbitrary complexity for tasks ranging from low-dimensional cart-pole stabilization to high-dimensional quadruped and biped tracking, showing performance improvements across different deployment domains.

## 核心内容
The deployment of robot controllers is hindered by modeling discrepancies due to necessary simplifications for computational tractability or inaccuracies in data-generating simulators. Such discrepancies typically require ad-hoc tuning to meet the desired performance, thereby ensuring successful transfer to a target domain. We propose a framework for automated, gradient-based tuning to enhance performance in the deployment domain by leveraging differentiable simulators. Our method collects rollouts in an iterative manner to co-tune the simulator and controller parameters, enabling systematic transfer within a few trials in the deployment domain. Specifically, we formulate multi-step objectives for tuning and employ alternating optimization to effectively adapt the controller to the deployment domain. The scalability of our framework is demonstrated by co-tuning model-based and learning-based controllers of arbitrary complexity for tasks ranging from low-dimensional cart-pole stabilization to high-dimensional quadruped and biped tracking, showing performance improvements across different deployment domains.

## 参考
- http://arxiv.org/abs/2505.24068v1

## Overview
The deployment of robot controllers is hindered by modeling discrepancies due to necessary simplifications for computational tractability or inaccuracies in data-generating simulators. Such discrepancies typically require ad-hoc tuning to meet the desired performance, thereby ensuring successful transfer to a target domain. We propose a framework for automated, gradient-based tuning to enhance performance in the deployment domain by leveraging differentiable simulators. Our method collects rollouts in an iterative manner to co-tune the simulator and controller parameters, enabling systematic transfer within a few trials in the deployment domain. Specifically, we formulate multi-step objectives for tuning and employ alternating optimization to effectively adapt the controller to the deployment domain. The scalability of our framework is demonstrated by co-tuning model-based and learning-based controllers of arbitrary complexity for tasks ranging from low-dimensional cart-pole stabilization to high-dimensional quadruped and biped tracking, showing performance improvements across different deployment domains.

## Content
The deployment of robot controllers is hindered by modeling discrepancies due to necessary simplifications for computational tractability or inaccuracies in data-generating simulators. Such discrepancies typically require ad-hoc tuning to meet the desired performance, thereby ensuring successful transfer to a target domain. We propose a framework for automated, gradient-based tuning to enhance performance in the deployment domain by leveraging differentiable simulators. Our method collects rollouts in an iterative manner to co-tune the simulator and controller parameters, enabling systematic transfer within a few trials in the deployment domain. Specifically, we formulate multi-step objectives for tuning and employ alternating optimization to effectively adapt the controller to the deployment domain. The scalability of our framework is demonstrated by co-tuning model-based and learning-based controllers of arbitrary complexity for tasks ranging from low-dimensional cart-pole stabilization to high-dimensional quadruped and biped tracking, showing performance improvements across different deployment domains.

## 개요
로봇 제어기의 배포는 계산 효율성을 위한 필연적인 단순화나 데이터 생성 시뮬레이터의 부정확성으로 인한 모델링 차이로 인해 어려움을 겪습니다. 이러한 차이는 일반적으로 원하는 성능을 달성하고 목표 도메인으로의 성공적인 전이를 보장하기 위해 임시 조정이 필요합니다. 본 논문에서는 미분 가능한 시뮬레이터를 활용하여 배포 도메인에서 성능을 향상시키기 위한 자동화된 그래디언트 기반 조정 프레임워크를 제안합니다. 우리의 방법은 반복적인 방식으로 롤아웃을 수집하여 시뮬레이터와 제어기 매개변수를 공동 조정함으로써 배포 도메인에서 몇 번의 시도 내에 체계적인 전이를 가능하게 합니다. 구체적으로, 조정을 위한 다단계 목표를 공식화하고 교대 최적화를 사용하여 제어기를 배포 도메인에 효과적으로 적응시킵니다. 우리 프레임워크의 확장성은 저차원 카트-폴 안정화부터 고차원 사족 및 이족 보행 추적에 이르기까지 다양한 작업에 대해 임의의 복잡성을 가진 모델 기반 및 학습 기반 제어기를 공동 조정함으로써 입증되며, 다양한 배포 도메인에서 성능 향상을 보여줍니다.

## 핵심 내용
로봇 제어기의 배포는 계산 효율성을 위한 필연적인 단순화나 데이터 생성 시뮬레이터의 부정확성으로 인한 모델링 차이로 인해 어려움을 겪습니다. 이러한 차이는 일반적으로 원하는 성능을 달성하고 목표 도메인으로의 성공적인 전이를 보장하기 위해 임시 조정이 필요합니다. 본 논문에서는 미분 가능한 시뮬레이터를 활용하여 배포 도메인에서 성능을 향상시키기 위한 자동화된 그래디언트 기반 조정 프레임워크를 제안합니다. 우리의 방법은 반복적인 방식으로 롤아웃을 수집하여 시뮬레이터와 제어기 매개변수를 공동 조정함으로써 배포 도메인에서 몇 번의 시도 내에 체계적인 전이를 가능하게 합니다. 구체적으로, 조정을 위한 다단계 목표를 공식화하고 교대 최적화를 사용하여 제어기를 배포 도메인에 효과적으로 적응시킵니다. 우리 프레임워크의 확장성은 저차원 카트-폴 안정화부터 고차원 사족 및 이족 보행 추적에 이르기까지 다양한 작업에 대해 임의의 복잡성을 가진 모델 기반 및 학습 기반 제어기를 공동 조정함으로써 입증되며, 다양한 배포 도메인에서 성능 향상을 보여줍니다.
