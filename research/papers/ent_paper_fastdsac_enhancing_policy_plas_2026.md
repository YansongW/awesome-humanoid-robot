---
$id: ent_paper_fastdsac_enhancing_policy_plas_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FastDSAC: Enhancing Policy Plasticity via Constrained Exploration for Scalable Humanoid Locomotion'
  zh: 'FastDSAC: Enhancing Policy Plasticity via Constrained Exploration for Scalable Humanoid Locomotion'
  ko: 'FastDSAC: Enhancing Policy Plasticity via Constrained Exploration for Scalable Humanoid Locomotion'
summary:
  en: 'arXiv:2606.31691v1 Announce Type: new Abstract: Scalable reinforcement learning has popularized high-throughput sampling
    architectures, which significantly compresses the training time for off-policy methods in robotic locomotion. However,
    the rapid increase of data volume and update frequency undermines the stability of value-based methods and diminishes
    the plasticity of policy networks. To address these challenges, this work presents FastDSAC, a fast and high-performance
    variant of the Distributional Actor-Critic algorithm designed for parallel sampling scenarios. Specifically, we introduce
    a truncated Gaussian distribution to approximate the learned policy, which effectively excludes out-of-distribution actions
    that strain target value estimation while keeping necessary stochasticity for exploration. The proposed action constraint
    functions as an implicit regularization, which counteracts the plasticity loss typically caused by aggressive gradient
    updates. This preservation of network adaptability enhances sample efficiency, particularly in scenarios with a high update-to-data
    ratio, and accelerates the early training process. In contrast to prior fast reinforcement learning approaches that rely
    on discrete value distributions, our method utilizes a continuous Gaussian representation equipped with adaptive variance
    regulation, which improves value estimation accuracy by sampling confident and informative transitions. Extensive experiments
    on MuJoCo Playground and HumanoidBench demonstrate that FastDSAC not only stabilizes the overall training process but
    also achieves superior asymptotic performance and faster convergence compared to state-of-the-art baselines.'
  zh: 'arXiv:2606.31691v1 Announce Type: new Abstract: Scalable reinforcement learning has popularized high-throughput sampling
    architectures, which significantly compresses the training time for off-policy methods in robotic locomotion. However,
    the rapid increase of data volume and update frequency undermines the stability of value-based methods and diminishes
    the plasticity of policy networks. To address these challenges, this work presents FastDSAC, a fast and high-performance
    variant of the Distributional Actor-Critic algorithm designed for parallel sampling scenarios. Specifically, we introduce
    a truncated Gaussian distribution to approximate the learned policy, which effectively excludes out-of-distribution actions
    that strain target value estimation while keeping necessary stochasticity for exploration. The proposed action constraint
    functions as an implicit regularization, which counteracts the plasticity loss typically caused by aggressive gradient
    updates. This preservation of network adaptability enhances sample efficiency, particularly in scenarios with a high update-to-data
    ratio, and accelerates the early training process. In contrast to prior fast reinforcement learning approaches that rely
    on discrete value distributions, our method utilizes a continuous Gaussian representation equipped with adaptive variance
    regulation, which improves value estimation accuracy by sampling confident and informative transitions. Extensive experiments
    on MuJoCo Playground and HumanoidBench demonstrate that FastDSAC not only stabilizes the overall training process but
    also achieves superior asymptotic performance and faster convergence compared to state-of-the-art baselines.'
  ko: 'arXiv:2606.31691v1 Announce Type: new Abstract: Scalable reinforcement learning has popularized high-throughput sampling
    architectures, which significantly compresses the training time for off-policy methods in robotic locomotion. However,
    the rapid increase of data volume and update frequency undermines the stability of value-based methods and diminishes
    the plasticity of policy networks. To address these challenges, this work presents FastDSAC, a fast and high-performance
    variant of the Distributional Actor-Critic algorithm designed for parallel sampling scenarios. Specifically, we introduce
    a truncated Gaussian distribution to approximate the learned policy, which effectively excludes out-of-distribution actions
    that strain target value estimation while keeping necessary stochasticity for exploration. The proposed action constraint
    functions as an implicit regularization, which counteracts the plasticity loss typically caused by aggressive gradient
    updates. This preservation of network adaptability enhances sample efficiency, particularly in scenarios with a high update-to-data
    ratio, and accelerates the early training process. In contrast to prior fast reinforcement learning approaches that rely
    on discrete value distributions, our method utilizes a continuous Gaussian representation equipped with adaptive variance
    regulation, which improves value estimation accuracy by sampling confident and informative transitions. Extensive experiments
    on MuJoCo Playground and HumanoidBench demonstrate that FastDSAC not only stabilizes the overall training process but
    also achieves superior asymptotic performance and faster convergence compared to state-of-the-art baselines.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- fastdsac
- humanoid
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31691v1.
sources:
- id: src_001
  type: paper
  title: 'FastDSAC: Enhancing Policy Plasticity via Constrained Exploration for Scalable Humanoid Locomotion'
  url: https://arxiv.org/abs/2606.31691
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Scalable reinforcement learning has popularized high-throughput sampling architectures, which significantly compresses the training time for off-policy methods in robotic locomotion. However, the rapid increase of data volume and update frequency undermines the stability of value-based methods and diminishes the plasticity of policy networks. To address these challenges, this work presents FastDSAC, a fast and high-performance variant of the Distributional Actor-Critic algorithm designed for parallel sampling scenarios. Specifically, we introduce a truncated Gaussian distribution to approximate the learned policy, which effectively excludes out-of-distribution actions that strain target value estimation while keeping necessary stochasticity for exploration. The proposed action constraint functions as an implicit regularization, which counteracts the plasticity loss typically caused by aggressive gradient updates. This preservation of network adaptability enhances sample efficiency, particularly in scenarios with a high update-to-data ratio, and accelerates the early training process. In contrast to prior fast reinforcement learning approaches that rely on discrete value distributions, our method utilizes a continuous Gaussian representation equipped with adaptive variance regulation, which improves value estimation accuracy by sampling confident and informative transitions. Extensive experiments on MuJoCo Playground and HumanoidBench demonstrate that FastDSAC not only stabilizes the overall training process but also achieves superior asymptotic performance and faster convergence compared to state-of-the-art baselines.

## 核心内容
Scalable reinforcement learning has popularized high-throughput sampling architectures, which significantly compresses the training time for off-policy methods in robotic locomotion. However, the rapid increase of data volume and update frequency undermines the stability of value-based methods and diminishes the plasticity of policy networks. To address these challenges, this work presents FastDSAC, a fast and high-performance variant of the Distributional Actor-Critic algorithm designed for parallel sampling scenarios. Specifically, we introduce a truncated Gaussian distribution to approximate the learned policy, which effectively excludes out-of-distribution actions that strain target value estimation while keeping necessary stochasticity for exploration. The proposed action constraint functions as an implicit regularization, which counteracts the plasticity loss typically caused by aggressive gradient updates. This preservation of network adaptability enhances sample efficiency, particularly in scenarios with a high update-to-data ratio, and accelerates the early training process. In contrast to prior fast reinforcement learning approaches that rely on discrete value distributions, our method utilizes a continuous Gaussian representation equipped with adaptive variance regulation, which improves value estimation accuracy by sampling confident and informative transitions. Extensive experiments on MuJoCo Playground and HumanoidBench demonstrate that FastDSAC not only stabilizes the overall training process but also achieves superior asymptotic performance and faster convergence compared to state-of-the-art baselines.

## 参考
- http://arxiv.org/abs/2606.31691v1

## Overview
Scalable reinforcement learning has popularized high-throughput sampling architectures, which significantly compresses the training time for off-policy methods in robotic locomotion. However, the rapid increase of data volume and update frequency undermines the stability of value-based methods and diminishes the plasticity of policy networks. To address these challenges, this work presents FastDSAC, a fast and high-performance variant of the Distributional Actor-Critic algorithm designed for parallel sampling scenarios. Specifically, we introduce a truncated Gaussian distribution to approximate the learned policy, which effectively excludes out-of-distribution actions that strain target value estimation while keeping necessary stochasticity for exploration. The proposed action constraint functions as an implicit regularization, which counteracts the plasticity loss typically caused by aggressive gradient updates. This preservation of network adaptability enhances sample efficiency, particularly in scenarios with a high update-to-data ratio, and accelerates the early training process. In contrast to prior fast reinforcement learning approaches that rely on discrete value distributions, our method utilizes a continuous Gaussian representation equipped with adaptive variance regulation, which improves value estimation accuracy by sampling confident and informative transitions. Extensive experiments on MuJoCo Playground and HumanoidBench demonstrate that FastDSAC not only stabilizes the overall training process but also achieves superior asymptotic performance and faster convergence compared to state-of-the-art baselines.

## Content
Scalable reinforcement learning has popularized high-throughput sampling architectures, which significantly compresses the training time for off-policy methods in robotic locomotion. However, the rapid increase of data volume and update frequency undermines the stability of value-based methods and diminishes the plasticity of policy networks. To address these challenges, this work presents FastDSAC, a fast and high-performance variant of the Distributional Actor-Critic algorithm designed for parallel sampling scenarios. Specifically, we introduce a truncated Gaussian distribution to approximate the learned policy, which effectively excludes out-of-distribution actions that strain target value estimation while keeping necessary stochasticity for exploration. The proposed action constraint functions as an implicit regularization, which counteracts the plasticity loss typically caused by aggressive gradient updates. This preservation of network adaptability enhances sample efficiency, particularly in scenarios with a high update-to-data ratio, and accelerates the early training process. In contrast to prior fast reinforcement learning approaches that rely on discrete value distributions, our method utilizes a continuous Gaussian representation equipped with adaptive variance regulation, which improves value estimation accuracy by sampling confident and informative transitions. Extensive experiments on MuJoCo Playground and HumanoidBench demonstrate that FastDSAC not only stabilizes the overall training process but also achieves superior asymptotic performance and faster convergence compared to state-of-the-art baselines.

## 개요
확장 가능한 강화 학습은 높은 처리량의 샘플링 아키텍처를 대중화하여 로봇 보행에서 오프-폴리시 방법의 훈련 시간을 크게 단축시켰습니다. 그러나 데이터 양과 업데이트 빈도의 급격한 증가는 가치 기반 방법의 안정성을 저하시키고 정책 네트워크의 가소성을 감소시킵니다. 이러한 문제를 해결하기 위해 본 연구는 병렬 샘플링 시나리오에 맞게 설계된 분포형 행위자-비평가 알고리즘의 빠르고 고성능 변형인 FastDSAC을 제시합니다. 구체적으로, 우리는 학습된 정책을 근사화하기 위해 절단된 가우시안 분포를 도입하여, 목표 가치 추정에 부담을 주는 분포 외 행동을 효과적으로 배제하면서 탐험에 필요한 확률성을 유지합니다. 제안된 행동 제약은 암묵적 정규화 역할을 하여, 공격적인 그래디언트 업데이트로 인해 일반적으로 발생하는 가소성 손실을 상쇄합니다. 이러한 네트워크 적응성의 보존은 특히 높은 업데이트-데이터 비율 시나리오에서 샘플 효율성을 향상시키고 초기 훈련 과정을 가속화합니다. 이산적 가치 분포에 의존하는 이전의 빠른 강화 학습 접근법과 달리, 우리의 방법은 적응형 분산 조절을 갖춘 연속 가우시안 표현을 활용하여 신뢰할 수 있고 정보가 풍부한 전이를 샘플링함으로써 가치 추정 정확도를 향상시킵니다. MuJoCo Playground 및 HumanoidBench에서의 광범위한 실험은 FastDSAC이 전체 훈련 과정을 안정화할 뿐만 아니라 최첨단 기준선과 비교하여 우수한 점근적 성능과 더 빠른 수렴을 달성함을 보여줍니다.

## 핵심 내용
확장 가능한 강화 학습은 높은 처리량의 샘플링 아키텍처를 대중화하여 로봇 보행에서 오프-폴리시 방법의 훈련 시간을 크게 단축시켰습니다. 그러나 데이터 양과 업데이트 빈도의 급격한 증가는 가치 기반 방법의 안정성을 저하시키고 정책 네트워크의 가소성을 감소시킵니다. 이러한 문제를 해결하기 위해 본 연구는 병렬 샘플링 시나리오에 맞게 설계된 분포형 행위자-비평가 알고리즘의 빠르고 고성능 변형인 FastDSAC을 제시합니다. 구체적으로, 우리는 학습된 정책을 근사화하기 위해 절단된 가우시안 분포를 도입하여, 목표 가치 추정에 부담을 주는 분포 외 행동을 효과적으로 배제하면서 탐험에 필요한 확률성을 유지합니다. 제안된 행동 제약은 암묵적 정규화 역할을 하여, 공격적인 그래디언트 업데이트로 인해 일반적으로 발생하는 가소성 손실을 상쇄합니다. 이러한 네트워크 적응성의 보존은 특히 높은 업데이트-데이터 비율 시나리오에서 샘플 효율성을 향상시키고 초기 훈련 과정을 가속화합니다. 이산적 가치 분포에 의존하는 이전의 빠른 강화 학습 접근법과 달리, 우리의 방법은 적응형 분산 조절을 갖춘 연속 가우시안 표현을 활용하여 신뢰할 수 있고 정보가 풍부한 전이를 샘플링함으로써 가치 추정 정확도를 향상시킵니다. MuJoCo Playground 및 HumanoidBench에서의 광범위한 실험은 FastDSAC이 전체 훈련 과정을 안정화할 뿐만 아니라 최첨단 기준선과 비교하여 우수한 점근적 성능과 더 빠른 수렴을 달성함을 보여줍니다.
