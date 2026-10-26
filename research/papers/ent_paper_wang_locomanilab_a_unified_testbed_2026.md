---
$id: ent_paper_wang_locomanilab_a_unified_testbed_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LocoManiLab: A Unified Testbed for Data, Policies, Controllers, and Deployment in Humanoid Loco-Manipulation'
  zh: 'LocoManiLab: A Unified Testbed for Data, Policies, Controllers, and Deployment in Humanoid Loco-Manipulation'
  ko: 'LocoManiLab: A Unified Testbed for Data, Policies, Controllers, and Deployment in Humanoid Loco-Manipulation'
summary:
  en: Humanoid robots must coordinate locomotion and manipulation in everyday environments, yet progress is difficult to assess
    across differing policies, controllers, and task settings. LocoManiLab provides an integrated testbed spanning data collection
    and generation, policy training, evaluation, and physical deployment. Its task suite covers 234 atomic and compositional
    tasks across five household ...
  zh: LocoManiLab 是一个面向人形机器人移动操作（loco-manipulation）的统一测试平台，覆盖数据采集与生成、策略训练、评估以及真机部署全流程。该平台包含五大类家庭场景下的 234 个原子与组合任务，并提供 51.5
    小时的仿真遥操作数据。其核心贡献在于建立跨策略、控制器与任务设置的统一评测体系，并验证了仿真评估与真实部署之间策略排序的一致性。
  ko: Humanoid robots must coordinate locomotion and manipulation in everyday environments, yet progress is difficult to assess
    across differing policies, controllers, and task settings. LocoManiLab provides an integrated testbed spanning data collection
    and generation, policy training, evaluation, and physical deployment. Its task suite covers 234 atomic and compositional
    tasks across five household ...
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- humanoid_loco_manipulation
- benchmark_platform
- sim_to_real
- policy_evaluation
- teleoperation_data
- motion_generation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-26'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-26). Bibliographic metadata from arXiv API (2610.30876);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.30876 LocoManiLab: A Unified Testbed for Data, Policies, Controllers, and Deployment in Humanoid Loco-Manipulation'
  url: https://arxiv.org/abs/2610.30876
  date: '2026-10-22'
  accessed_at: '2026-10-26'
---

## 概述

LocoManiLab 针对人形机器人移动操作研究中策略、控制器与任务设置各异、进展难以横向比较的问题，构建了一个端到端测试平台，涵盖数据采集与生成、策略训练、评估和物理部署。平台的任务套件包含五大类家庭场景中的 234 个原子与组合任务，配套 51.5 小时仿真遥操作数据。评估方面，平台在任务与场景划分及不同扰动水平下测试了十二种策略（共享同一控制器），并在五种控制器下比较了两种策略，同时研究了示范规模与数据来源混合的影响。结果显示，策略在未见任务与场景上的成功率下降，且随视觉扰动增强而普遍降低，不同策略在泛化性与鲁棒性上存在差异。此外，作者微调了一个人形运动生成模型用于移动操作，考察其输出与任务执行需求的对齐及其在数据生成流程中的集成；三个仿真移动操作任务与真实设置高度接近，使三种策略得以在两个域中评估，且策略排序相似，支持了仿真评估的可靠性。

## 核心内容

### 问题背景
人形机器人需要在日常环境中协调移动与操作，但由于策略、控制器和任务设置各不相同，研究进展难以统一衡量。现有工作缺乏覆盖数据、训练、评估与部署的整合性基准。

### 平台与方法
- **任务套件**：覆盖五类家庭场景，共 234 个原子与组合任务。
- **数据**：提供 51.5 小时仿真遥操作数据，用于策略训练与示范规模研究。
- **评估设计**：
  - 十二种策略在共享控制器下，跨任务划分、场景划分及不同扰动水平进行评估；
  - 两种策略在五种控制器下进行比较；
  - 研究示范规模与数据来源混合对性能的影响。
- **数据生成**：微调一个人形运动生成模型用于移动操作，分析其输出与任务执行需求的对齐情况，并将其集成进数据生成流程。

### 关键结果
- 策略在未见任务与未见场景上的成功率下降。
- 成功率通常随视觉扰动增强而降低。
- 不同策略在泛化性与鲁棒性上表现出差异。
- 三个仿真移动操作任务与真实世界设置高度接近，三种策略在仿真与真实域中均被评估，且策略排序相似，表明基于仿真的评估具有可靠性。

### 结论
LocoManiLab 提供了统一的人形移动操作评测基础设施，支持从数据生成到真机部署的完整链路，并通过仿真与真实的排序一致性验证了其评估的可信度。

## Overview

Humanoid robots must coordinate locomotion and manipulation in everyday environments, yet progress is difficult to assess across differing policies, controllers, and task settings. LocoManiLab provides an integrated testbed spanning data collection and generation, policy training, evaluation, and physical deployment. Its task suite covers 234 atomic and compositional tasks across five household scene categories, supported by 51.5 hours of simulated teleoperation. The evaluation covers twelve policies with a shared controller across task and scene splits and perturbation levels, two policies across five controllers, and studies of demonstration scale and data-source mixtures. Success rates fall on unseen tasks and scenes and generally decline as visual perturbations increase, with differences in generalization and robustness across policies. For data generation, a humanoid motion generation model is fine-tuned for loco-manipulation to study the alignment of its outputs with task execution requirements and its integration into the data generation pipeline. Three simulated loco-manipulation tasks closely match real-world setups, enabling evaluation of three policies in both domains. Similar policy rankings support the reliability of simulation-based evaluation.

## 参考
- https://arxiv.org/abs/2610.30876
