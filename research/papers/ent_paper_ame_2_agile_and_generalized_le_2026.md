---
$id: ent_paper_ame_2_agile_and_generalized_le_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AME-2: Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding'
  zh: 'AME-2: Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding'
  ko: 'AME-2: Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding'
summary:
  en: 'AME-2: Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding is a 2026 work on locomotion
    for humanoid robots.'
  zh: 'AME-2: Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding is a 2026 work on locomotion
    for humanoid robots.'
  ko: 'AME-2: Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding is a 2026 work on locomotion
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- ame_2
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.08485v2.
sources:
- id: src_001
  type: paper
  title: 'AME-2: Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding (arXiv)'
  url: https://arxiv.org/abs/2601.08485
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Achieving agile and generalized legged locomotion across terrains requires tight integration of perception and control, especially under occlusions and sparse footholds. Existing methods have demonstrated agility on parkour courses but often rely on end-to-end sensorimotor models with limited generalization and interpretability. By contrast, methods targeting generalized locomotion typically exhibit limited agility and struggle with visual occlusions. We introduce AME-2, a unified reinforcement learning (RL) framework for agile and generalized locomotion that incorporates a novel attention-based map encoder in the control policy. This encoder extracts local and global mapping features and uses attention mechanisms to focus on salient regions, producing an interpretable and generalized embedding for RL-based control. We further propose a learning-based mapping pipeline that provides fast, uncertainty-aware terrain representations robust to noise and occlusions, serving as policy inputs. It uses neural networks to convert depth observations into local elevations with uncertainties, and fuses them with odometry. The pipeline also integrates with parallel simulation so that we can train controllers with online mapping, aiding sim-to-real transfer. We validate AME-2 with the proposed mapping pipeline on a quadruped and a biped robot, and the resulting controllers demonstrate strong agility and generalization to unseen terrains in simulation and in real-world experiments.

## 核心内容
Achieving agile and generalized legged locomotion across terrains requires tight integration of perception and control, especially under occlusions and sparse footholds. Existing methods have demonstrated agility on parkour courses but often rely on end-to-end sensorimotor models with limited generalization and interpretability. By contrast, methods targeting generalized locomotion typically exhibit limited agility and struggle with visual occlusions. We introduce AME-2, a unified reinforcement learning (RL) framework for agile and generalized locomotion that incorporates a novel attention-based map encoder in the control policy. This encoder extracts local and global mapping features and uses attention mechanisms to focus on salient regions, producing an interpretable and generalized embedding for RL-based control. We further propose a learning-based mapping pipeline that provides fast, uncertainty-aware terrain representations robust to noise and occlusions, serving as policy inputs. It uses neural networks to convert depth observations into local elevations with uncertainties, and fuses them with odometry. The pipeline also integrates with parallel simulation so that we can train controllers with online mapping, aiding sim-to-real transfer. We validate AME-2 with the proposed mapping pipeline on a quadruped and a biped robot, and the resulting controllers demonstrate strong agility and generalization to unseen terrains in simulation and in real-world experiments.

## 参考
- http://arxiv.org/abs/2601.08485v2

