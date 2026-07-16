---
$id: ent_paper_wu_robomind_benchmark_on_multi_em_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation'
  zh: RoboMIND：机器人操作多具身智能规范数据基准
  ko: 'RoboMIND: 로봇 조작을 위한 다중 구현체 지능 표준 데이터 벤치마크'
summary:
  en: Introduces RoboMIND, a 107k-trajectory human-teleoperated manipulation dataset collected on a unified platform across
    four robot embodiments including the X-Humanoid Tien Kung, and benchmarks imitation-learning and Vision-Language-Action
    methods on it.
  zh: 提出 RoboMIND，一个在统一平台上通过人类遥操作采集的107k条操作轨迹数据集，涵盖包括X-Humanoid Tien Kung人形机器人在内的四种机器人具身，并在该数据集上对模仿学习和视觉-语言-动作方法进行基准测试。
  ko: X-Humanoid Tien Kung 휴머노이드 로봇을 포함한 4가지 로봇 embodiment에 걸쳐 통합 플랫폼에서 사람 원격 조작으로 수집한 107k 궤적 조작 데이터셋 RoboMIND를 소개하고, 이를
    이용해 모방 학습 및 비전-언어-행동 방법을 벤치마크함.
domains:
- 09_data_datasets
- 10_evaluation_benchmarks
- 07_ai_models_algorithms
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
- tool_equipment
tags:
- vla
- imitation_learning
- teleoperation
- multi_embodiment
- manipulation
- dataset
- benchmark
- humanoid
- digital_twin
- failure_reflection
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.13877v3.
sources:
- id: src_001
  type: paper
  title: 'RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation'
  url: https://arxiv.org/abs/2412.13877
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
In this paper, we introduce RoboMIND (Multi-embodiment Intelligence Normative Data for Robot Manipulation), a dataset containing 107k demonstration trajectories across 479 diverse tasks involving 96 object classes. RoboMIND is collected through human teleoperation and encompasses comprehensive robotic-related information, including multi-view observations, proprioceptive robot state information, and linguistic task descriptions. To ensure data consistency and reliability for imitation learning, RoboMIND is built on a unified data collection platform and a standardized protocol, covering four distinct robotic embodiments: the Franka Emika Panda, the UR5e, the AgileX dual-arm robot, and a humanoid robot with dual dexterous hands. Our dataset also includes 5k real-world failure demonstrations, each accompanied by detailed causes, enabling failure reflection and correction during policy learning. Additionally, we created a digital twin environment in the Isaac Sim simulator, replicating the real-world tasks and assets, which facilitates the low-cost collection of additional training data and enables efficient evaluation. To demonstrate the quality and diversity of our dataset, we conducted extensive experiments using various imitation learning methods for single-task settings and state-of-the-art Vision-Language-Action (VLA) models for multi-task scenarios. By leveraging RoboMIND, the VLA models achieved high manipulation success rates and demonstrated strong generalization capabilities. To the best of our knowledge, RoboMIND is the largest multi-embodiment teleoperation dataset collected on a unified platform, providing large-scale and high-quality robotic training data. Our project is at https://x-humanoid-robomind.github.io/.

## 核心内容
In this paper, we introduce RoboMIND (Multi-embodiment Intelligence Normative Data for Robot Manipulation), a dataset containing 107k demonstration trajectories across 479 diverse tasks involving 96 object classes. RoboMIND is collected through human teleoperation and encompasses comprehensive robotic-related information, including multi-view observations, proprioceptive robot state information, and linguistic task descriptions. To ensure data consistency and reliability for imitation learning, RoboMIND is built on a unified data collection platform and a standardized protocol, covering four distinct robotic embodiments: the Franka Emika Panda, the UR5e, the AgileX dual-arm robot, and a humanoid robot with dual dexterous hands. Our dataset also includes 5k real-world failure demonstrations, each accompanied by detailed causes, enabling failure reflection and correction during policy learning. Additionally, we created a digital twin environment in the Isaac Sim simulator, replicating the real-world tasks and assets, which facilitates the low-cost collection of additional training data and enables efficient evaluation. To demonstrate the quality and diversity of our dataset, we conducted extensive experiments using various imitation learning methods for single-task settings and state-of-the-art Vision-Language-Action (VLA) models for multi-task scenarios. By leveraging RoboMIND, the VLA models achieved high manipulation success rates and demonstrated strong generalization capabilities. To the best of our knowledge, RoboMIND is the largest multi-embodiment teleoperation dataset collected on a unified platform, providing large-scale and high-quality robotic training data. Our project is at https://x-humanoid-robomind.github.io/.

## 参考
- http://arxiv.org/abs/2412.13877v3

## Overview
In this paper, we introduce RoboMIND (Multi-embodiment Intelligence Normative Data for Robot Manipulation), a dataset containing 107k demonstration trajectories across 479 diverse tasks involving 96 object classes. RoboMIND is collected through human teleoperation and encompasses comprehensive robotic-related information, including multi-view observations, proprioceptive robot state information, and linguistic task descriptions. To ensure data consistency and reliability for imitation learning, RoboMIND is built on a unified data collection platform and a standardized protocol, covering four distinct robotic embodiments: the Franka Emika Panda, the UR5e, the AgileX dual-arm robot, and a humanoid robot with dual dexterous hands. Our dataset also includes 5k real-world failure demonstrations, each accompanied by detailed causes, enabling failure reflection and correction during policy learning. Additionally, we created a digital twin environment in the Isaac Sim simulator, replicating the real-world tasks and assets, which facilitates the low-cost collection of additional training data and enables efficient evaluation. To demonstrate the quality and diversity of our dataset, we conducted extensive experiments using various imitation learning methods for single-task settings and state-of-the-art Vision-Language-Action (VLA) models for multi-task scenarios. By leveraging RoboMIND, the VLA models achieved high manipulation success rates and demonstrated strong generalization capabilities. To the best of our knowledge, RoboMIND is the largest multi-embodiment teleoperation dataset collected on a unified platform, providing large-scale and high-quality robotic training data. Our project is at https://x-humanoid-robomind.github.io/.

## Content
In this paper, we introduce RoboMIND (Multi-embodiment Intelligence Normative Data for Robot Manipulation), a dataset containing 107k demonstration trajectories across 479 diverse tasks involving 96 object classes. RoboMIND is collected through human teleoperation and encompasses comprehensive robotic-related information, including multi-view observations, proprioceptive robot state information, and linguistic task descriptions. To ensure data consistency and reliability for imitation learning, RoboMIND is built on a unified data collection platform and a standardized protocol, covering four distinct robotic embodiments: the Franka Emika Panda, the UR5e, the AgileX dual-arm robot, and a humanoid robot with dual dexterous hands. Our dataset also includes 5k real-world failure demonstrations, each accompanied by detailed causes, enabling failure reflection and correction during policy learning. Additionally, we created a digital twin environment in the Isaac Sim simulator, replicating the real-world tasks and assets, which facilitates the low-cost collection of additional training data and enables efficient evaluation. To demonstrate the quality and diversity of our dataset, we conducted extensive experiments using various imitation learning methods for single-task settings and state-of-the-art Vision-Language-Action (VLA) models for multi-task scenarios. By leveraging RoboMIND, the VLA models achieved high manipulation success rates and demonstrated strong generalization capabilities. To the best of our knowledge, RoboMIND is the largest multi-embodiment teleoperation dataset collected on a unified platform, providing large-scale and high-quality robotic training data. Our project is at https://x-humanoid-robomind.github.io/.

## 개요
본 논문에서는 로봇 조작을 위한 다중 체현 지능 규범 데이터(RoboMIND)를 소개합니다. 이 데이터셋은 96개 객체 클래스를 포함한 479개의 다양한 작업에 걸쳐 107,000개의 시연 궤적을 포함합니다. RoboMIND는 인간 원격 조작을 통해 수집되었으며, 다중 시점 관찰, 고유 수용성 로봇 상태 정보, 언어적 작업 설명 등 포괄적인 로봇 관련 정보를 포함합니다. 모방 학습을 위한 데이터 일관성과 신뢰성을 보장하기 위해 RoboMIND는 통합 데이터 수집 플랫폼과 표준화된 프로토콜을 기반으로 구축되었으며, Franka Emika Panda, UR5e, AgileX 이중 팔 로봇, 이중 정교한 손을 가진 휴머노이드 로봇 등 네 가지 서로 다른 로봇 체현을 포함합니다. 또한 데이터셋에는 5,000개의 실제 세계 실패 시연이 포함되어 있으며, 각각 상세한 원인이 함께 제공되어 정책 학습 중 실패 반성 및 수정을 가능하게 합니다. 추가로 Isaac Sim 시뮬레이터에서 디지털 트윈 환경을 생성하여 실제 작업과 자산을 복제함으로써 추가 훈련 데이터의 저비용 수집을 용이하게 하고 효율적인 평가를 가능하게 합니다. 데이터셋의 품질과 다양성을 입증하기 위해 단일 작업 설정을 위한 다양한 모방 학습 방법과 다중 작업 시나리오를 위한 최첨단 Vision-Language-Action(VLA) 모델을 사용하여 광범위한 실험을 수행했습니다. RoboMIND를 활용함으로써 VLA 모델은 높은 조작 성공률을 달성하고 강력한 일반화 능력을 보여주었습니다. 우리가 아는 한, RoboMIND는 통합 플랫폼에서 수집된 가장 큰 다중 체현 원격 조작 데이터셋으로, 대규모 고품질 로봇 훈련 데이터를 제공합니다. 프로젝트는 https://x-humanoid-robomind.github.io/에서 확인할 수 있습니다.

## 핵심 내용
본 논문에서는 로봇 조작을 위한 다중 체현 지능 규범 데이터(RoboMIND)를 소개합니다. 이 데이터셋은 96개 객체 클래스를 포함한 479개의 다양한 작업에 걸쳐 107,000개의 시연 궤적을 포함합니다. RoboMIND는 인간 원격 조작을 통해 수집되었으며, 다중 시점 관찰, 고유 수용성 로봇 상태 정보, 언어적 작업 설명 등 포괄적인 로봇 관련 정보를 포함합니다. 모방 학습을 위한 데이터 일관성과 신뢰성을 보장하기 위해 RoboMIND는 통합 데이터 수집 플랫폼과 표준화된 프로토콜을 기반으로 구축되었으며, Franka Emika Panda, UR5e, AgileX 이중 팔 로봇, 이중 정교한 손을 가진 휴머노이드 로봇 등 네 가지 서로 다른 로봇 체현을 포함합니다. 또한 데이터셋에는 5,000개의 실제 세계 실패 시연이 포함되어 있으며, 각각 상세한 원인이 함께 제공되어 정책 학습 중 실패 반성 및 수정을 가능하게 합니다. 추가로 Isaac Sim 시뮬레이터에서 디지털 트윈 환경을 생성하여 실제 작업과 자산을 복제함으로써 추가 훈련 데이터의 저비용 수집을 용이하게 하고 효율적인 평가를 가능하게 합니다. 데이터셋의 품질과 다양성을 입증하기 위해 단일 작업 설정을 위한 다양한 모방 학습 방법과 다중 작업 시나리오를 위한 최첨단 Vision-Language-Action(VLA) 모델을 사용하여 광범위한 실험을 수행했습니다. RoboMIND를 활용함으로써 VLA 모델은 높은 조작 성공률을 달성하고 강력한 일반화 능력을 보여주었습니다. 우리가 아는 한, RoboMIND는 통합 플랫폼에서 수집된 가장 큰 다중 체현 원격 조작 데이터셋으로, 대규모 고품질 로봇 훈련 데이터를 제공합니다. 프로젝트는 https://x-humanoid-robomind.github.io/에서 확인할 수 있습니다.
