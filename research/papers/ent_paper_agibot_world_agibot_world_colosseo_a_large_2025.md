---
$id: ent_paper_agibot_world_agibot_world_colosseo_a_large_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems'
  zh: AgiBot World Colosseo：面向可扩展智能具身系统的大规模操作平台
  ko: 'AgiBot World Colosseo: 확장 가능하고 지능적인 구체화 시스템을 위한 대규모 조작 플랫폼'
summary:
  en: Introduces AgiBot World, a million-trajectory humanoid manipulation dataset collected by 100+ AgiBot G1 robots across
    217 tasks, and Genie Operator-1 (GO-1), a generalist policy using latent action representations that improves over Open
    X-Embodiment by 30% and over RDT by 32% on real-world tasks.
  zh: 介绍了AgiBot World——由100多台AgiBot G1人形机器人在217项真实任务中采集的百万级轨迹操作数据集，以及Genie Operator-1（GO-1）通用策略；GO-1基于隐式动作表征，在真实世界任务中较Open
    X-Embodiment预训练策略平均提升30%，较RDT提升32%。
  ko: 본 논문은 100대 이상의 AgiBot G1 휴머노이드 로봇이 217개 실제 작업에서 수집한 백만 개 이상의 궤적을 담은 AgiBot World 조작 데이터셋과 잠재 행동 표현을 활용하는 범용 정책 GO-1을
    제안하며, 실제 작업에서 Open X-Embodiment 대비 30%, RDT 대비 32% 성능 향상을 보였다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.06669v4.
sources:
- id: src_001
  type: paper
  title: 'AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems'
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
## 概述
We explore how scalable robot data can address real-world challenges for generalized robotic manipulation. Introducing AgiBot World, a large-scale platform comprising over 1 million trajectories across 217 tasks in five deployment scenarios, we achieve an order-of-magnitude increase in data scale compared to existing datasets. Accelerated by a standardized collection pipeline with human-in-the-loop verification, AgiBot World guarantees high-quality and diverse data distribution. It is extensible from grippers to dexterous hands and visuo-tactile sensors for fine-grained skill acquisition. Building on top of data, we introduce Genie Operator-1 (GO-1), a novel generalist policy that leverages latent action representations to maximize data utilization, demonstrating predictable performance scaling with increased data volume. Policies pre-trained on our dataset achieve an average performance improvement of 30% over those trained on Open X-Embodiment, both in in-domain and out-of-distribution scenarios. GO-1 exhibits exceptional capability in real-world dexterous and long-horizon tasks, achieving over 60% success rate on complex tasks and outperforming prior RDT approach by 32%. By open-sourcing the dataset, tools, and models, we aim to democratize access to large-scale, high-quality robot data, advancing the pursuit of scalable and general-purpose intelligence.

## 核心内容
We explore how scalable robot data can address real-world challenges for generalized robotic manipulation. Introducing AgiBot World, a large-scale platform comprising over 1 million trajectories across 217 tasks in five deployment scenarios, we achieve an order-of-magnitude increase in data scale compared to existing datasets. Accelerated by a standardized collection pipeline with human-in-the-loop verification, AgiBot World guarantees high-quality and diverse data distribution. It is extensible from grippers to dexterous hands and visuo-tactile sensors for fine-grained skill acquisition. Building on top of data, we introduce Genie Operator-1 (GO-1), a novel generalist policy that leverages latent action representations to maximize data utilization, demonstrating predictable performance scaling with increased data volume. Policies pre-trained on our dataset achieve an average performance improvement of 30% over those trained on Open X-Embodiment, both in in-domain and out-of-distribution scenarios. GO-1 exhibits exceptional capability in real-world dexterous and long-horizon tasks, achieving over 60% success rate on complex tasks and outperforming prior RDT approach by 32%. By open-sourcing the dataset, tools, and models, we aim to democratize access to large-scale, high-quality robot data, advancing the pursuit of scalable and general-purpose intelligence.

## 参考
- http://arxiv.org/abs/2503.06669v4

