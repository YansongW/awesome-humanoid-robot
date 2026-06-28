---
$id: ent_paper_liu_robot_learning_on_the_job_huma_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Robot Learning on the Job: Human-in-the-Loop Autonomy and Learning During Deployment'
  zh: 机器人在岗学习：部署过程中的人机协同自治与学习
  ko: '로봇의 현장 학습: 배포 중 인간 개입 자율성 및 학습'
summary:
  en: This paper introduces Sirius, a human-in-the-loop framework in which a partially
    autonomous robot handles reliable decisions while a human monitors and teleoperates
    interventions, then improves policies via weighted behavioral cloning on re-weighted
    deployment data.
  zh: 本文提出Sirius框架，部分自主机器人在可靠决策中运行，人工监控并在困难情况下遥操作干预，然后通过对重新加权的部署数据进行加权行为克隆来持续改进策略。
  ko: 본 논문은 부분 자율 로봇이 안정적인 의사결정을 수행하고 인간이 모니터링하며 어려운 상황에서 텔레오퍼레이션으로 개입한 후, 재가중된 배포
    데이터에 대한 가중 행동 복제를 통해 정책을 지속적으로 개선하는 Sirius 프레임워크를 제안한다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- human_in_the_loop
- robot_learning
- continual_learning
- behavioral_cloning
- shared_autonomy
- teleoperation
- deployment
- contact_rich_manipulation
- sample_reweighting
- real_robot_hardware
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from full text; requires human review before verification.
sources:
- id: src_001
  type: paper
  title: 'Robot Learning on the Job: Human-in-the-Loop Autonomy and Learning During
    Deployment'
  url: https://arxiv.org/abs/2211.08416
  date: '2022'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

This paper presents Sirius, a principled human-in-the-loop robot learning framework designed for safe and continual deployment of partially autonomous robots in real-world manipulation tasks. The core idea is to divide decision-making labor between the robot and a human operator: the robot autonomously handles states where it is reliable, while the human monitors execution and intervenes via teleoperation when the robot encounters challenging or unsafe situations. After deployment, the collected on-the-job data, together with explicit human intervention signals, are used to retrain and improve the robot policy over successive rounds.

The authors introduce an intervention-guided sample re-weighting algorithm that upweights human intervention segments and downweights the robot's pre-intervention actions during training. The policy is then optimized with weighted behavioral cloning. To support long-term deployment, Sirius also incorporates fixed-size memory management strategies to bound storage and enable scalable learning. The framework is evaluated both in simulation with robosuite and on a real Franka Emika Panda arm with a NIST Task Board, demonstrating improved success rates, faster convergence, and reduced memory size compared to state-of-the-art baselines.

## Key Contributions

- Sirius framework for continual human-in-the-loop robot deployment and policy learning.
- Intervention-guided sample re-weighting for weighted behavioral cloning.
- Fixed-size memory management strategies for long-term deployment data.
- Empirical evaluation in simulation and on real robot hardware showing improved success rates, faster convergence, and reduced memory size.

## Relevance to Humanoid Robotics

The Sirius framework directly addresses a critical barrier to scaling humanoid robots in unstructured environments: the brittleness and data hunger of learning-based control policies. By combining partial autonomy with continuous human oversight and on-the-job learning, it provides a practical path toward safe deployment of humanoid systems in real-world settings where full autonomy is not yet reliable. The intervention-guided learning mechanism also reduces human workload over successive deployment rounds, making it a relevant method for commercial and service-oriented humanoid applications.
