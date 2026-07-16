---
$id: ent_paper_implicit_kinodynamic_motion_re_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning
  zh: Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning
  ko: Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning
summary:
  en: Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.
  zh: Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.
  ko: Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.
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
- implicit_kinodynamic_motion_re
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.15443v2.
sources:
- id: src_001
  type: paper
  title: Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning (arXiv)
  url: https://arxiv.org/abs/2509.15443
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Human-to-humanoid imitation learning presents a promising pathway to address the severe data scarcity bottleneck in robotics by utilizing abundant, large-scale human motion collections. However, scaling this paradigm requires addressing two key challenges. First, human motion data acquired from videos, motion capture systems, or generative models often contains spatial noise, jitter, and frame-level flickering, which can be amplified during retargeting and lead to unsafe or physically infeasible robot motions. Second, existing motion retargeting methods typically rely on frame-by-frame numerical optimization, making them too computationally expensive for large-scale dataset synthesis. To overcome these limitations, we introduce Implicit Kinodynamic Motion Retargeting (IKMR), a highly scalable, neural-based data transformation pipeline. IKMR leverages a skeleton-based graph convolutional dual autoencoder to map cross-structural human and humanoid kinematic configurations into a shared topological latent space. To guarantee the physical viability of the generated data, the framework incorporates a physics-informed refinement phase that utilizes simulated physical tracking feedback to learn a robust motion prior. This implicit formulation fundamentally resolves both challenges. By shifting the computational burden from online optimization to offline inference, IKMR achieves an unprecedented data conversion throughput exceeding 5000 frames per second. Furthermore, leveraging the learned motion prior, it functions as an intrinsic data curation mechanism and naturally filters out high-frequency noise and spatial jitters from source data, yielding smooth trajectories that ensure physical hardware safety. Extensive evaluations, including real-world whole-body control deployments on humanoid robot, confirm that IKMR bridges the gap between human motion and robotic data.

## 核心内容
Human-to-humanoid imitation learning presents a promising pathway to address the severe data scarcity bottleneck in robotics by utilizing abundant, large-scale human motion collections. However, scaling this paradigm requires addressing two key challenges. First, human motion data acquired from videos, motion capture systems, or generative models often contains spatial noise, jitter, and frame-level flickering, which can be amplified during retargeting and lead to unsafe or physically infeasible robot motions. Second, existing motion retargeting methods typically rely on frame-by-frame numerical optimization, making them too computationally expensive for large-scale dataset synthesis. To overcome these limitations, we introduce Implicit Kinodynamic Motion Retargeting (IKMR), a highly scalable, neural-based data transformation pipeline. IKMR leverages a skeleton-based graph convolutional dual autoencoder to map cross-structural human and humanoid kinematic configurations into a shared topological latent space. To guarantee the physical viability of the generated data, the framework incorporates a physics-informed refinement phase that utilizes simulated physical tracking feedback to learn a robust motion prior. This implicit formulation fundamentally resolves both challenges. By shifting the computational burden from online optimization to offline inference, IKMR achieves an unprecedented data conversion throughput exceeding 5000 frames per second. Furthermore, leveraging the learned motion prior, it functions as an intrinsic data curation mechanism and naturally filters out high-frequency noise and spatial jitters from source data, yielding smooth trajectories that ensure physical hardware safety. Extensive evaluations, including real-world whole-body control deployments on humanoid robot, confirm that IKMR bridges the gap between human motion and robotic data.

## 参考
- http://arxiv.org/abs/2509.15443v2

## Overview
Human-to-humanoid imitation learning presents a promising pathway to address the severe data scarcity bottleneck in robotics by utilizing abundant, large-scale human motion collections. However, scaling this paradigm requires addressing two key challenges. First, human motion data acquired from videos, motion capture systems, or generative models often contains spatial noise, jitter, and frame-level flickering, which can be amplified during retargeting and lead to unsafe or physically infeasible robot motions. Second, existing motion retargeting methods typically rely on frame-by-frame numerical optimization, making them too computationally expensive for large-scale dataset synthesis. To overcome these limitations, we introduce Implicit Kinodynamic Motion Retargeting (IKMR), a highly scalable, neural-based data transformation pipeline. IKMR leverages a skeleton-based graph convolutional dual autoencoder to map cross-structural human and humanoid kinematic configurations into a shared topological latent space. To guarantee the physical viability of the generated data, the framework incorporates a physics-informed refinement phase that utilizes simulated physical tracking feedback to learn a robust motion prior. This implicit formulation fundamentally resolves both challenges. By shifting the computational burden from online optimization to offline inference, IKMR achieves an unprecedented data conversion throughput exceeding 5000 frames per second. Furthermore, leveraging the learned motion prior, it functions as an intrinsic data curation mechanism and naturally filters out high-frequency noise and spatial jitters from source data, yielding smooth trajectories that ensure physical hardware safety. Extensive evaluations, including real-world whole-body control deployments on humanoid robot, confirm that IKMR bridges the gap between human motion and robotic data.

## Content
Human-to-humanoid imitation learning presents a promising pathway to address the severe data scarcity bottleneck in robotics by utilizing abundant, large-scale human motion collections. However, scaling this paradigm requires addressing two key challenges. First, human motion data acquired from videos, motion capture systems, or generative models often contains spatial noise, jitter, and frame-level flickering, which can be amplified during retargeting and lead to unsafe or physically infeasible robot motions. Second, existing motion retargeting methods typically rely on frame-by-frame numerical optimization, making them too computationally expensive for large-scale dataset synthesis. To overcome these limitations, we introduce Implicit Kinodynamic Motion Retargeting (IKMR), a highly scalable, neural-based data transformation pipeline. IKMR leverages a skeleton-based graph convolutional dual autoencoder to map cross-structural human and humanoid kinematic configurations into a shared topological latent space. To guarantee the physical viability of the generated data, the framework incorporates a physics-informed refinement phase that utilizes simulated physical tracking feedback to learn a robust motion prior. This implicit formulation fundamentally resolves both challenges. By shifting the computational burden from online optimization to offline inference, IKMR achieves an unprecedented data conversion throughput exceeding 5000 frames per second. Furthermore, leveraging the learned motion prior, it functions as an intrinsic data curation mechanism and naturally filters out high-frequency noise and spatial jitters from source data, yielding smooth trajectories that ensure physical hardware safety. Extensive evaluations, including real-world whole-body control deployments on humanoid robot, confirm that IKMR bridges the gap between human motion and robotic data.

## 개요
인간-휴머노이드 모방 학습은 풍부하고 대규모의 인간 동작 데이터를 활용하여 로봇 공학에서 심각한 데이터 부족 병목 현상을 해결할 수 있는 유망한 접근 방식을 제시합니다. 그러나 이 패러다임을 확장하려면 두 가지 주요 과제를 해결해야 합니다. 첫째, 비디오, 모션 캡처 시스템 또는 생성 모델에서 획득한 인간 동작 데이터에는 종종 공간적 노이즈, 지터 및 프레임 수준의 깜빡임이 포함되어 있으며, 이는 리타겟팅 과정에서 증폭되어 안전하지 않거나 물리적으로 실행 불가능한 로봇 동작을 초래할 수 있습니다. 둘째, 기존의 동작 리타겟팅 방법은 일반적으로 프레임별 수치 최적화에 의존하기 때문에 대규모 데이터셋 합성에 계산 비용이 너무 많이 듭니다. 이러한 한계를 극복하기 위해 우리는 고도로 확장 가능한 신경망 기반 데이터 변환 파이프라인인 Implicit Kinodynamic Motion Retargeting (IKMR)을 소개합니다. IKMR은 골격 기반 그래프 컨볼루션 이중 오토인코더를 활용하여 교차 구조적 인간 및 휴머노이드 운동학적 구성을 공유 위상 잠재 공간에 매핑합니다. 생성된 데이터의 물리적 실행 가능성을 보장하기 위해 프레임워크는 시뮬레이션된 물리적 추적 피드백을 활용하여 강건한 동작 사전을 학습하는 물리 기반 정제 단계를 통합합니다. 이 암시적 공식은 두 가지 과제를 근본적으로 해결합니다. 계산 부담을 온라인 최적화에서 오프라인 추론으로 전환함으로써 IKMR은 초당 5000프레임을 초과하는 전례 없는 데이터 변환 처리량을 달성합니다. 또한, 학습된 동작 사전을 활용하여 내재적 데이터 큐레이션 메커니즘으로 기능하며 소스 데이터에서 고주파 노이즈와 공간적 지터를 자연스럽게 필터링하여 물리적 하드웨어 안전을 보장하는 부드러운 궤적을 생성합니다. 휴머노이드 로봇에 대한 실제 전신 제어 배치를 포함한 광범위한 평가를 통해 IKMR이 인간 동작과 로봇 데이터 간의 격차를 해소함을 확인했습니다.

## 핵심 내용
인간-휴머노이드 모방 학습은 풍부하고 대규모의 인간 동작 데이터를 활용하여 로봇 공학에서 심각한 데이터 부족 병목 현상을 해결할 수 있는 유망한 접근 방식을 제시합니다. 그러나 이 패러다임을 확장하려면 두 가지 주요 과제를 해결해야 합니다. 첫째, 비디오, 모션 캡처 시스템 또는 생성 모델에서 획득한 인간 동작 데이터에는 종종 공간적 노이즈, 지터 및 프레임 수준의 깜빡임이 포함되어 있으며, 이는 리타겟팅 과정에서 증폭되어 안전하지 않거나 물리적으로 실행 불가능한 로봇 동작을 초래할 수 있습니다. 둘째, 기존의 동작 리타겟팅 방법은 일반적으로 프레임별 수치 최적화에 의존하기 때문에 대규모 데이터셋 합성에 계산 비용이 너무 많이 듭니다. 이러한 한계를 극복하기 위해 우리는 고도로 확장 가능한 신경망 기반 데이터 변환 파이프라인인 Implicit Kinodynamic Motion Retargeting (IKMR)을 소개합니다. IKMR은 골격 기반 그래프 컨볼루션 이중 오토인코더를 활용하여 교차 구조적 인간 및 휴머노이드 운동학적 구성을 공유 위상 잠재 공간에 매핑합니다. 생성된 데이터의 물리적 실행 가능성을 보장하기 위해 프레임워크는 시뮬레이션된 물리적 추적 피드백을 활용하여 강건한 동작 사전을 학습하는 물리 기반 정제 단계를 통합합니다. 이 암시적 공식은 두 가지 과제를 근본적으로 해결합니다. 계산 부담을 온라인 최적화에서 오프라인 추론으로 전환함으로써 IKMR은 초당 5000프레임을 초과하는 전례 없는 데이터 변환 처리량을 달성합니다. 또한, 학습된 동작 사전을 활용하여 내재적 데이터 큐레이션 메커니즘으로 기능하며 소스 데이터에서 고주파 노이즈와 공간적 지터를 자연스럽게 필터링하여 물리적 하드웨어 안전을 보장하는 부드러운 궤적을 생성합니다. 휴머노이드 로봇에 대한 실제 전신 제어 배치를 포함한 광범위한 평가를 통해 IKMR이 인간 동작과 로봇 데이터 간의 격차를 해소함을 확인했습니다.
