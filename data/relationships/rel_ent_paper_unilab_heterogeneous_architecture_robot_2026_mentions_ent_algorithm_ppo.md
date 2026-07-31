---
$id: rel_ent_paper_unilab_heterogeneous_architecture_robot_2026_mentions_ent_algorithm_ppo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_unilab_heterogeneous_architecture_robot_2026
  name:
    en: 'UniLab: A Heterogeneous Architecture for Robot RL Beyond GPU-Dominant Paradigms'
    zh: 'UniLab: A Heterogeneous Architecture for Robot RL Beyond GPU-Dominant Paradigms'
target:
  id: ent_algorithm_ppo
  name:
    en: Proximal Policy Optimization (PPO)
    zh: 近端策略优化（PPO）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'UniLab: A Heterogeneous Architecture for Robot RL Beyond GPU-Dominant Paradigms mentions Proximal Policy Optimization
    (PPO).'
  zh: 'UniLab: A Heterogeneous Architecture for Robot RL Beyond GPU-Dominant Paradigms提及近端策略优化（PPO）。'
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: 该架构通过统一运行时管理数据移动、缓冲与同步，将 CPU 并行仿真与 GPU 策略更新解耦，并基于
    MuJoCoUni 和 MotrixSim CPU 批处理物理后端实现完整训练系统，支持 PPO、FastSAC、FlashSAC 和 APPO 算法。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_unilab_heterogeneous_architecture_robot_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_unilab_heterogeneous_architecture_robot_2026/
  accessed_at: '2026-07-31'
---
