---
$id: ent_paper_towards_bridging_the_gap_betwe_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control
  zh: Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control
  ko: Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control
summary:
  en: Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control is a 2026 work
    on sim-to-real for humanoid robots, with open-source code available.
  zh: Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control is a 2026 work
    on sim-to-real for humanoid robots, with open-source code available.
  ko: Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control is a 2026 work
    on sim-to-real for humanoid robots, with open-source code available.
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
- sim_to_real
- towards_bridging_the_gap_betwe
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.21363v3.
sources:
- id: src_001
  type: paper
  title: Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control (arXiv)
  url: https://arxiv.org/abs/2601.21363
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control project page
  url: https://lift-humanoid.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Reinforcement learning (RL) is widely used for humanoid control, with on-policy methods such as Proximal Policy Optimization (PPO) enabling robust training via large-scale parallel simulation and, in some cases, zero-shot deployment to real robots. However, the low sample efficiency of on-policy algorithms limits safe adaptation to new environments. Although off-policy RL and model-based RL have shown improved sample efficiency, the gap between large-scale pretraining and efficient finetuning on humanoids still exists. In this paper, we find that off-policy Soft Actor-Critic (SAC), with large-batch update and a high Update-To-Data (UTD) ratio, reliably supports large-scale pretraining of humanoid locomotion policies, achieving zero-shot deployment on real robots. For adaptation, we demonstrate that these SAC-pretrained policies can be finetuned in new environments and out-of-distribution tasks using model-based methods. Data collection in the new environment executes a deterministic policy while stochastic exploration is instead confined to a physics-informed world model. This separation mitigates the risks of random exploration during adaptation while preserving exploratory coverage for improvement. Overall, the approach couples the wall-clock efficiency of large-scale simulation during pretraining with the sample efficiency of model-based learning during fine-tuning. For code and videos, see https://lift-humanoid.github.io

## 核心内容
Reinforcement learning (RL) is widely used for humanoid control, with on-policy methods such as Proximal Policy Optimization (PPO) enabling robust training via large-scale parallel simulation and, in some cases, zero-shot deployment to real robots. However, the low sample efficiency of on-policy algorithms limits safe adaptation to new environments. Although off-policy RL and model-based RL have shown improved sample efficiency, the gap between large-scale pretraining and efficient finetuning on humanoids still exists. In this paper, we find that off-policy Soft Actor-Critic (SAC), with large-batch update and a high Update-To-Data (UTD) ratio, reliably supports large-scale pretraining of humanoid locomotion policies, achieving zero-shot deployment on real robots. For adaptation, we demonstrate that these SAC-pretrained policies can be finetuned in new environments and out-of-distribution tasks using model-based methods. Data collection in the new environment executes a deterministic policy while stochastic exploration is instead confined to a physics-informed world model. This separation mitigates the risks of random exploration during adaptation while preserving exploratory coverage for improvement. Overall, the approach couples the wall-clock efficiency of large-scale simulation during pretraining with the sample efficiency of model-based learning during fine-tuning. For code and videos, see https://lift-humanoid.github.io

## 参考
- http://arxiv.org/abs/2601.21363v3

