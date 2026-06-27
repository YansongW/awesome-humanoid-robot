---
$id: ent_paper_wu_robomind_benchmark_on_multi_em_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot
    Manipulation'
  zh: RoboMIND：机器人操作多具身智能规范数据基准
  ko: 'RoboMIND: 로봇 조작을 위한 다중 구현체 지능 표준 데이터 벤치마크'
summary:
  en: Introduces RoboMIND, a 107k-trajectory human-teleoperated manipulation dataset
    collected on a unified platform across four robot embodiments including the X-Humanoid
    Tien Kung, and benchmarks imitation-learning and Vision-Language-Action methods
    on it.
  zh: 提出 RoboMIND，一个在统一平台上通过人类遥操作采集的107k条操作轨迹数据集，涵盖包括X-Humanoid Tien Kung人形机器人在内的四种机器人具身，并在该数据集上对模仿学习和视觉-语言-动作方法进行基准测试。
  ko: X-Humanoid Tien Kung 휴머노이드 로봇을 포함한 4가지 로봇 embodiment에 걸쳐 통합 플랫폼에서 사람 원격 조작으로
    수집한 107k 궤적 조작 데이터셋 RoboMIND를 소개하고, 이를 이용해 모방 학습 및 비전-언어-행동 방법을 벤치마크함.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the provided metadata and abstract; full-text verification
    and human review are required before promotion.
sources:
- id: src_001
  type: paper
  title: 'RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for
    Robot Manipulation'
  url: https://arxiv.org/abs/2412.13877
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

RoboMIND (Multi-embodiment Intelligence Normative Data for Robot Manipulation) is a large-scale robotic manipulation dataset introduced to address the fragmentation and inconsistent standards of existing robotic datasets. It contains 107,000 demonstration trajectories spanning 479 diverse tasks and 96 object classes, collected through human teleoperation on a unified hardware-software platform with a standardized protocol.

The dataset covers four distinct robotic embodiments: the Franka Emika Panda single-arm robot, the X-Humanoid Tien Kung humanoid robot with dual dexterous hands, the AgileX Cobot Magic V2.0 dual-arm robot, and the Universal Robots UR5e. Each trajectory includes multi-view observations, proprioceptive robot state information, and linguistic task descriptions. RoboMIND also includes 5,000 real-world failure demonstrations with annotated causes and 10,000 frame-level fine-grained language annotations to support failure reflection and correction. An NVIDIA Isaac Sim digital twin replicates the real-world tasks and assets, enabling low-cost additional data collection and efficient evaluation.

The authors benchmark both single-task imitation learning methods and state-of-the-art Vision-Language-Action models on RoboMIND. The experiments demonstrate high manipulation success rates and strong generalization, supporting the claim that RoboMIND provides large-scale, high-quality training data for multi-embodiment robot manipulation.

## Key Contributions

- 107,000 demonstration trajectories across 479 tasks and 96 object classes collected on a unified platform with a standardized protocol.
- Multi-embodiment coverage including single-arm, dual-arm, and humanoid robots with both grippers and dexterous hands.
- 5,000 real-world failure demonstrations with annotated causes and 10,000 frame-level fine-grained language annotations.
- An Isaac Sim digital twin replicating real-world tasks and assets for scalable simulation data and evaluation.
- Benchmark experiments on single-task imitation learning methods and state-of-the-art VLA models showing strong performance and generalization.

## Relevance to Humanoid Robotics

RoboMIND is directly relevant to humanoid robotics because it includes the X-Humanoid Tien Kung humanoid robot with dexterous hands as one of its four standardized embodiments. By applying the same data collection protocol to a humanoid robot alongside single-arm and dual-arm systems, the dataset supports cross-embodiment policy learning and transfer for humanoid manipulation.

The scale and standardization of RoboMIND make it a practical resource for training and evaluating generalizable manipulation policies intended for humanoid deployment and mass production. The inclusion of failure demonstrations and fine-grained language annotations further enables the development of robust, reflective controllers that are critical for real-world humanoid robot operation.
