---
$id: ent_paper_agibot_world_agibot_world_colosseo_a_large_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable and
    Intelligent Embodied Systems'
  zh: AgiBot World Colosseo：面向可扩展智能具身系统的大规模操作平台
  ko: 'AgiBot World Colosseo: 확장 가능하고 지능적인 구체화 시스템을 위한 대규모 조작 플랫폼'
summary:
  en: Introduces AgiBot World, a million-trajectory humanoid manipulation dataset
    collected by 100+ AgiBot G1 robots across 217 tasks, and Genie Operator-1 (GO-1),
    a generalist policy using latent action representations that improves over Open
    X-Embodiment by 30% and over RDT by 32% on real-world tasks.
  zh: 介绍了AgiBot World——由100多台AgiBot G1人形机器人在217项真实任务中采集的百万级轨迹操作数据集，以及Genie Operator-1（GO-1）通用策略；GO-1基于隐式动作表征，在真实世界任务中较Open
    X-Embodiment预训练策略平均提升30%，较RDT提升32%。
  ko: 본 논문은 100대 이상의 AgiBot G1 휴머노이드 로봇이 217개 실제 작업에서 수집한 백만 개 이상의 궤적을 담은 AgiBot World
    조작 데이터셋과 잠재 행동 표현을 활용하는 범용 정책 GO-1을 제안하며, 실제 작업에서 Open X-Embodiment 대비 30%, RDT
    대비 32% 성능 향상을 보였다.
domains:
- 09_data_datasets
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- vla
- diffusion_policy
- latent_action
- humanoid_dataset
- teleoperation
- dexterous_manipulation
- data_scaling
- human_in_the_loop
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review against
    full paper before verification.
sources:
- id: src_001
  type: paper
  title: 'AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable
    and Intelligent Embodied Systems'
  url: https://arxiv.org/abs/2503.06669
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
related_entities:
- id: ent_dataset_open_x_embodiment
  relationship: cites
  description:
    en: The paper compares policy performance against models trained on Open X-Embodiment.
    zh: 该论文将策略性能与在Open X-Embodiment上训练的模型进行比较。
    ko: 해당 논문은 Open X-Embodiment로 학습한 모델과 정책 성능을 비교한다.
- id: ent_dataset_droid
  relationship: cites
  description:
    en: The paper references DROID as a related large-scale robot dataset.
    zh: 该论文将DROID引用为相关的大规模机器人数据集。
    ko: 해당 논문은 DROID를 관련 대규모 로봇 데이터셋으로 언급한다.
---

## Overview

AgiBot World Colosseo presents a large-scale embodied manipulation platform designed to close the data gap in generalized robotic manipulation. The platform centers on AgiBot World, a dataset containing over one million trajectories spanning 217 tasks, 87 skills, and 106 scenes across domestic, retail, industrial, restaurant, and office deployment scenarios. The data were collected by more than 100 AgiBot G1 dual-arm humanoid robots equipped with dexterous hands, visuo-tactile sensors, RGB-D and fisheye cameras, and a VR-based teleoperation system with optional whole-body motion capture for fine-grained finger control.

Building on the dataset, the authors introduce Genie Operator-1 (GO-1), a generalist policy that combines a vision-language model-based latent planner with a diffusion action expert within a hierarchical Vision-Language-Latent-Action (ViLLA) framework. GO-1 leverages latent action representations to maximize data utilization and exhibits predictable power-law scaling as training data volume increases. Policies pre-trained on AgiBot World achieve an average performance improvement of 30% over those trained on Open X-Embodiment in both in-domain and out-of-distribution settings, while GO-1 surpasses the prior RDT approach by 32% on complex real-world tasks.

The work is released as an open-source package that includes the dataset, toolchains, and model checkpoints, aiming to democratize access to large-scale, high-quality robot demonstration data for the research community.

## Key Contributions

- AgiBot World dataset: 1M+ trajectories, 217 tasks, 87 skills, and 106 scenes across domestic, retail, industrial, restaurant, and office domains.
- Standardized, scalable data collection pipeline with human-in-the-loop verification, detailed annotations, and failure-recovery data.
- Genie Operator-1 (GO-1) generalist policy using latent action representations within a hierarchical ViLLA framework.
- Empirical demonstration of predictable power-law data scaling and 30% average improvement over Open X-Embodiment, plus 32% gain over RDT.
- Open-source release of dataset, toolchains, and model checkpoints to the research community.

## Relevance to Humanoid Robotics

The paper is directly relevant to humanoid robotics because it deploys over 100 AgiBot G1 dual-arm humanoid robots with dexterous hands and visuo-tactile sensors in real-world scenarios to collect large-scale manipulation data. The dataset covers whole-body, dual-arm, and fine-grained hand skills that are central to humanoid robot capabilities. By providing an open, standardized data platform and a generalist policy that scales predictably with data volume, the work supports scalable skill acquisition, deployment, and benchmarking for humanoid robots.
