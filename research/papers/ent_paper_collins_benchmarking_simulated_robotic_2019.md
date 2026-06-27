---
$id: ent_paper_collins_benchmarking_simulated_robotic_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Benchmarking Simulated Robotic Manipulation through a Real World Dataset
  zh: 通过真实世界数据集对模拟机器人操作进行基准测试
  ko: 실제 세계 데이터셋을 통한 시뮬레이션 로봇 조작 벤치마킹
summary:
  en: Collins et al. introduce a hardware-free benchmark for simulated robotic manipulation
    that distributes a real-world motion-capture dataset and standardized protocols
    so researchers can quantify the sim2real gap using 23 kinematic and dynamic metrics.
  zh: Collins 等人提出了一种无需硬件的模拟机器人操作基准，通过分发真实世界的动作捕捉数据集和标准化协议，使研究人员能够使用23种运动学和动力学指标来量化仿真到现实的差距。
  ko: Collins 등은 실제 세계 모션 캡처 데이터셋과 표준화된 프로토콜을 배포하여 연구자들이 23개의 운동학적 및 동역학적 메트릭을 사용하여
    sim2real 격차를 정량화할 수 있도록 하는 하드웨어 없는 시뮬레이션 로봇 조작 벤치마크를 소개한다.
domains:
- 10_evaluation_benchmarks
- 09_data_datasets
- 08_software_middleware
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- sim2real
- benchmark
- manipulation
- motion_capture
- simulator_fidelity
- pybullet
- v_rep
- kinova_mico2
- robotiq_ft300
- qualisys
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; requires human review against
    the full arXiv text before verification.
sources:
- id: src_001
  type: paper
  title: Benchmarking Simulated Robotic Manipulation through a Real World Dataset
  url: https://arxiv.org/abs/1911.01557
  date: '2019'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This paper proposes a hardware-free benchmark designed to characterize the fidelity of simulated robotic manipulation by comparing simulation outputs against a distributed, real-world, ground-truth motion-capture dataset. The authors provide a set of protocols that define how a simulator should reproduce a recorded manipulation task, together with 23 metrics that quantify pose, velocity, acceleration, torque, contact force/moment, and final-pose distributions. Two widely used simulation environments, PyBullet and V-Rep, are evaluated under the proposed protocols to demonstrate the benchmark's use. The dataset, protocols, and supporting materials are published through the benchmark's website, enabling other groups to replicate and extend the evaluation.

The work is motivated by the difficulty of running repeatable physical robot experiments at scale and the resulting lack of standardized ways to measure the sim2real gap. Rather than requiring each user to operate the same physical hardware, the benchmark decouples evaluation from hardware access by distributing the recorded ground-truth trajectories. Simulators are then treated as submissions that should reproduce the observed real-world behavior, and the metrics provide both an overall fidelity score and diagnostic information about specific failure modes.

The tasks in the initial dataset are intentionally simple manipulation primitives intended as a preliminary test set. They are recorded with a Kinova Mico2 arm equipped with a KG-3 gripper and a Robotiq FT300 force-torque sensor, while a Qualisys motion-capture system supplies high-accuracy pose ground truth. The exemplar experiments in PyBullet and V-Rep are run primarily with default simulator parameters, illustrating how the benchmark surfaces simulator-specific weaknesses rather than tuned best-case performance.

## Key Contributions

- A reproducible procedure for comparing simulated robotic manipulation to real-world recordings.
- A publicly distributed ground-truth dataset of manipulation tasks recorded with a high-accuracy motion-capture system.
- A suite of 23 metrics for characterizing simulator fidelity across kinematic and dynamic behaviors.
- Exemplar benchmark results for PyBullet and V-Rep using multiple physics engines.

## Relevance to Humanoid Robotics

Humanoid robots rely heavily on manipulation capabilities, and closing the sim2real gap is a prerequisite for their cost-effective development and mass deployment. This benchmark provides a reusable, hardware-free validation framework that lets researchers quantify how well a simulator reproduces real-world manipulation, which is directly applicable to the arms and hands of humanoid platforms. By distributing the ground-truth dataset and standardized protocols, the work lowers the barrier to rigorous simulator verification for manipulation subsystems that are central to humanoid robot behavior.
