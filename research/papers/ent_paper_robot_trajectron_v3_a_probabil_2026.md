---
$id: ent_paper_robot_trajectron_v3_a_probabil_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Robot Trajectron V3: A Probabilistic Shared Control Framework for SE(3) Manipulation'
  zh: 'Robot Trajectron V3: A Probabilistic Shared Control Framework for SE(3) Manipulation'
  ko: 'Robot Trajectron V3: A Probabilistic Shared Control Framework for SE(3) Manipulation'
summary:
  en: 'arXiv:2607.09315v1 Announce Type: new Abstract: We aim to address the challenge of teleoperating robotic arms for high-degree-of-freedom
    (high-DoF) manipulation tasks, which is cognitively demanding and error-prone, particularly when relying on low-bandwidth
    interfaces. We propose Robot Trajectron V3 (RT-V3), a probabilistic shared control framework designed for $SE(3)$ grasping
    tasks. RT-V3 formulates shared control as Bayesian inference by learning a prior over user intent and combining it with
    real-time user commands to estimate the posterior intent distribution. The prior models user intent as a distribution
    over future trajectories conditioned on past robot dynamics and visual scene context. The intent prior is parameterized
    by a transformer-based conditional generative model that reasons over point clouds and candidate grasp poses, together
    with a factorized translation-rotation representation that improves learning efficiency in high-dimensional action spaces.
    During execution, RT-V3 continuously estimates the posterior distribution over future trajectories by combining the learned
    intent prior with a user-command likelihood derived from the observed control input, enabling continuous intent refinement
    and shared assistance. Comprehensive experiments demonstrate that RT-V3 achieves high accuracy in trajectory prediction
    and competitive performance in reactive planning. Furthermore, real-world user studies indicate that RT-V3 significantly
    outperforms baseline methods in terms of success rate and efficiency, while substantially reducing the user''s physical
    and mental workload.'
  zh: 'arXiv:2607.09315v1 Announce Type: new Abstract: We aim to address the challenge of teleoperating robotic arms for high-degree-of-freedom
    (high-DoF) manipulation tasks, which is cognitively demanding and error-prone, particularly when relying on low-bandwidth
    interfaces. We propose Robot Trajectron V3 (RT-V3), a probabilistic shared control framework designed for $SE(3)$ grasping
    tasks. RT-V3 formulates shared control as Bayesian inference by learning a prior over user intent and combining it with
    real-time user commands to estimate the posterior intent distribution. The prior models user intent as a distribution
    over future trajectories conditioned on past robot dynamics and visual scene context. The intent prior is parameterized
    by a transformer-based conditional generative model that reasons over point clouds and candidate grasp poses, together
    with a factorized translation-rotation representation that improves learning efficiency in high-dimensional action spaces.
    During execution, RT-V3 continuously estimates the posterior distribution over future trajectories by combining the learned
    intent prior with a user-command likelihood derived from the observed control input, enabling continuous intent refinement
    and shared assistance. Comprehensive experiments demonstrate that RT-V3 achieves high accuracy in trajectory prediction
    and competitive performance in reactive planning. Furthermore, real-world user studies indicate that RT-V3 significantly
    outperforms baseline methods in terms of success rate and efficiency, while substantially reducing the user''s physical
    and mental workload.'
  ko: 'arXiv:2607.09315v1 Announce Type: new Abstract: We aim to address the challenge of teleoperating robotic arms for high-degree-of-freedom
    (high-DoF) manipulation tasks, which is cognitively demanding and error-prone, particularly when relying on low-bandwidth
    interfaces. We propose Robot Trajectron V3 (RT-V3), a probabilistic shared control framework designed for $SE(3)$ grasping
    tasks. RT-V3 formulates shared control as Bayesian inference by learning a prior over user intent and combining it with
    real-time user commands to estimate the posterior intent distribution. The prior models user intent as a distribution
    over future trajectories conditioned on past robot dynamics and visual scene context. The intent prior is parameterized
    by a transformer-based conditional generative model that reasons over point clouds and candidate grasp poses, together
    with a factorized translation-rotation representation that improves learning efficiency in high-dimensional action spaces.
    During execution, RT-V3 continuously estimates the posterior distribution over future trajectories by combining the learned
    intent prior with a user-command likelihood derived from the observed control input, enabling continuous intent refinement
    and shared assistance. Comprehensive experiments demonstrate that RT-V3 achieves high accuracy in trajectory prediction
    and competitive performance in reactive planning. Furthermore, real-world user studies indicate that RT-V3 significantly
    outperforms baseline methods in terms of success rate and efficiency, while substantially reducing the user''s physical
    and mental workload.'
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
- robotics
- robot_trajectron_v3
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.09315v1.
sources:
- id: src_001
  type: paper
  title: 'Robot Trajectron V3: A Probabilistic Shared Control Framework for SE(3) Manipulation (arXiv)'
  url: https://arxiv.org/abs/2607.09315
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
We aim to address the challenge of teleoperating robotic arms for high-degree-of-freedom (high-DoF) manipulation tasks, which is cognitively demanding and error-prone, particularly when relying on low-bandwidth interfaces. We propose Robot Trajectron V3 (RT-V3), a probabilistic shared control framework designed for $SE(3)$ grasping tasks. RT-V3 formulates shared control as Bayesian inference by learning a prior over user intent and combining it with real-time user commands to estimate the posterior intent distribution. The prior models user intent as a distribution over future trajectories conditioned on past robot dynamics and visual scene context. The intent prior is parameterized by a transformer-based conditional generative model that reasons over point clouds and candidate grasp poses, together with a factorized translation-rotation representation that improves learning efficiency in high-dimensional action spaces. During execution, RT-V3 continuously estimates the posterior distribution over future trajectories by combining the learned intent prior with a user-command likelihood derived from the observed control input, enabling continuous intent refinement and shared assistance. Comprehensive experiments demonstrate that RT-V3 achieves high accuracy in trajectory prediction and competitive performance in reactive planning. Furthermore, real-world user studies indicate that RT-V3 significantly outperforms baseline methods in terms of success rate and efficiency, while substantially reducing the user's physical and mental workload.

## 核心内容
We aim to address the challenge of teleoperating robotic arms for high-degree-of-freedom (high-DoF) manipulation tasks, which is cognitively demanding and error-prone, particularly when relying on low-bandwidth interfaces. We propose Robot Trajectron V3 (RT-V3), a probabilistic shared control framework designed for $SE(3)$ grasping tasks. RT-V3 formulates shared control as Bayesian inference by learning a prior over user intent and combining it with real-time user commands to estimate the posterior intent distribution. The prior models user intent as a distribution over future trajectories conditioned on past robot dynamics and visual scene context. The intent prior is parameterized by a transformer-based conditional generative model that reasons over point clouds and candidate grasp poses, together with a factorized translation-rotation representation that improves learning efficiency in high-dimensional action spaces. During execution, RT-V3 continuously estimates the posterior distribution over future trajectories by combining the learned intent prior with a user-command likelihood derived from the observed control input, enabling continuous intent refinement and shared assistance. Comprehensive experiments demonstrate that RT-V3 achieves high accuracy in trajectory prediction and competitive performance in reactive planning. Furthermore, real-world user studies indicate that RT-V3 significantly outperforms baseline methods in terms of success rate and efficiency, while substantially reducing the user's physical and mental workload.

## 参考
- http://arxiv.org/abs/2607.09315v1

## Overview
We aim to address the challenge of teleoperating robotic arms for high-degree-of-freedom (high-DoF) manipulation tasks, which is cognitively demanding and error-prone, particularly when relying on low-bandwidth interfaces. We propose Robot Trajectron V3 (RT-V3), a probabilistic shared control framework designed for $SE(3)$ grasping tasks. RT-V3 formulates shared control as Bayesian inference by learning a prior over user intent and combining it with real-time user commands to estimate the posterior intent distribution. The prior models user intent as a distribution over future trajectories conditioned on past robot dynamics and visual scene context. The intent prior is parameterized by a transformer-based conditional generative model that reasons over point clouds and candidate grasp poses, together with a factorized translation-rotation representation that improves learning efficiency in high-dimensional action spaces. During execution, RT-V3 continuously estimates the posterior distribution over future trajectories by combining the learned intent prior with a user-command likelihood derived from the observed control input, enabling continuous intent refinement and shared assistance. Comprehensive experiments demonstrate that RT-V3 achieves high accuracy in trajectory prediction and competitive performance in reactive planning. Furthermore, real-world user studies indicate that RT-V3 significantly outperforms baseline methods in terms of success rate and efficiency, while substantially reducing the user's physical and mental workload.

## Content
We aim to address the challenge of teleoperating robotic arms for high-degree-of-freedom (high-DoF) manipulation tasks, which is cognitively demanding and error-prone, particularly when relying on low-bandwidth interfaces. We propose Robot Trajectron V3 (RT-V3), a probabilistic shared control framework designed for $SE(3)$ grasping tasks. RT-V3 formulates shared control as Bayesian inference by learning a prior over user intent and combining it with real-time user commands to estimate the posterior intent distribution. The prior models user intent as a distribution over future trajectories conditioned on past robot dynamics and visual scene context. The intent prior is parameterized by a transformer-based conditional generative model that reasons over point clouds and candidate grasp poses, together with a factorized translation-rotation representation that improves learning efficiency in high-dimensional action spaces. During execution, RT-V3 continuously estimates the posterior distribution over future trajectories by combining the learned intent prior with a user-command likelihood derived from the observed control input, enabling continuous intent refinement and shared assistance. Comprehensive experiments demonstrate that RT-V3 achieves high accuracy in trajectory prediction and competitive performance in reactive planning. Furthermore, real-world user studies indicate that RT-V3 significantly outperforms baseline methods in terms of success rate and efficiency, while substantially reducing the user's physical and mental workload.

## 개요
본 연구는 고자유도(high-DoF) 조작 작업을 위한 로봇 팔 원격 조작의 과제를 해결하는 것을 목표로 합니다. 이러한 작업은 인지적 부담이 크고 오류가 발생하기 쉬우며, 특히 저대역폭 인터페이스에 의존할 때 더욱 두드러집니다. 우리는 $SE(3)$ 파지 작업을 위해 설계된 확률적 공유 제어 프레임워크인 Robot Trajectron V3 (RT-V3)를 제안합니다. RT-V3는 사용자 의도에 대한 사전 분포를 학습하고 이를 실시간 사용자 명령과 결합하여 사후 의도 분포를 추정함으로써 공유 제어를 베이지안 추론으로 공식화합니다. 사전 분포는 과거 로봇 동역학 및 시각적 장면 맥락에 조건화된 미래 궤적에 대한 분포로 사용자 의도를 모델링합니다. 의도 사전 분포는 포인트 클라우드와 후보 파지 자세를 추론하는 트랜스포머 기반 조건부 생성 모델과 고차원 행동 공간에서 학습 효율성을 향상시키는 분해된 병진-회전 표현에 의해 매개변수화됩니다. 실행 중에 RT-V3는 학습된 의도 사전 분포와 관찰된 제어 입력에서 파생된 사용자 명령 가능도를 결합하여 미래 궤적에 대한 사후 분포를 지속적으로 추정함으로써, 지속적인 의도 개선과 공유 지원을 가능하게 합니다. 포괄적인 실험을 통해 RT-V3가 궤적 예측에서 높은 정확도를 달성하고 반응적 계획에서 경쟁력 있는 성능을 보임을 입증했습니다. 또한 실제 사용자 연구에서 RT-V3는 성공률과 효율성 측면에서 기준 방법을 크게 능가하며, 사용자의 신체적 및 정신적 작업 부하를 현저히 감소시키는 것으로 나타났습니다.

## 핵심 내용
본 연구는 고자유도(high-DoF) 조작 작업을 위한 로봇 팔 원격 조작의 과제를 해결하는 것을 목표로 합니다. 이러한 작업은 인지적 부담이 크고 오류가 발생하기 쉬우며, 특히 저대역폭 인터페이스에 의존할 때 더욱 두드러집니다. 우리는 $SE(3)$ 파지 작업을 위해 설계된 확률적 공유 제어 프레임워크인 Robot Trajectron V3 (RT-V3)를 제안합니다. RT-V3는 사용자 의도에 대한 사전 분포를 학습하고 이를 실시간 사용자 명령과 결합하여 사후 의도 분포를 추정함으로써 공유 제어를 베이지안 추론으로 공식화합니다. 사전 분포는 과거 로봇 동역학 및 시각적 장면 맥락에 조건화된 미래 궤적에 대한 분포로 사용자 의도를 모델링합니다. 의도 사전 분포는 포인트 클라우드와 후보 파지 자세를 추론하는 트랜스포머 기반 조건부 생성 모델과 고차원 행동 공간에서 학습 효율성을 향상시키는 분해된 병진-회전 표현에 의해 매개변수화됩니다. 실행 중에 RT-V3는 학습된 의도 사전 분포와 관찰된 제어 입력에서 파생된 사용자 명령 가능도를 결합하여 미래 궤적에 대한 사후 분포를 지속적으로 추정함으로써, 지속적인 의도 개선과 공유 지원을 가능하게 합니다. 포괄적인 실험을 통해 RT-V3가 궤적 예측에서 높은 정확도를 달성하고 반응적 계획에서 경쟁력 있는 성능을 보임을 입증했습니다. 또한 실제 사용자 연구에서 RT-V3는 성공률과 효율성 측면에서 기준 방법을 크게 능가하며, 사용자의 신체적 및 정신적 작업 부하를 현저히 감소시키는 것으로 나타났습니다.
