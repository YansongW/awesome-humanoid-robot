---
$id: ent_paper_guhur_instruction_driven_history_awa_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Instruction-driven history-aware policies for robotic manipulations
  zh: Hiveformer
  ko: Instruction-driven history-aware policies for robotic manipulations
summary:
  en: Instruction-driven history-aware policies for robotic manipulations (Hiveformer), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by Inria, École normale supérieure, CNRS, PSL Research University, IIIT Hyderabad,
    and published at CoRL 2022.
  zh: Instruction-driven history-aware policies for robotic manipulations (Hiveformer), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by Inria, École normale supérieure, CNRS, PSL Research University, IIIT Hyderabad,
    and published at CoRL 2022.
  ko: Instruction-driven history-aware policies for robotic manipulations (Hiveformer), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by Inria, École normale supérieure, CNRS, PSL Research University, IIIT Hyderabad,
    and published at CoRL 2022.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- hiveformer
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2209.04899v3.
sources:
- id: src_001
  type: paper
  title: Hiveformer source
  url: https://proceedings.mlr.press/v205/guhur23a.html
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
In human environments, robots are expected to accomplish a variety of manipulation tasks given simple natural language instructions. Yet, robotic manipulation is extremely challenging as it requires fine-grained motor control, long-term memory as well as generalization to previously unseen tasks and environments. To address these challenges, we propose a unified transformer-based approach that takes into account multiple inputs. In particular, our transformer architecture integrates (i) natural language instructions and (ii) multi-view scene observations while (iii) keeping track of the full history of observations and actions. Such an approach enables learning dependencies between history and instructions and improves manipulation precision using multiple views. We evaluate our method on the challenging RLBench benchmark and on a real-world robot. Notably, our approach scales to 74 diverse RLBench tasks and outperforms the state of the art. We also address instruction-conditioned tasks and demonstrate excellent generalization to previously unseen variations.

## 核心内容
In human environments, robots are expected to accomplish a variety of manipulation tasks given simple natural language instructions. Yet, robotic manipulation is extremely challenging as it requires fine-grained motor control, long-term memory as well as generalization to previously unseen tasks and environments. To address these challenges, we propose a unified transformer-based approach that takes into account multiple inputs. In particular, our transformer architecture integrates (i) natural language instructions and (ii) multi-view scene observations while (iii) keeping track of the full history of observations and actions. Such an approach enables learning dependencies between history and instructions and improves manipulation precision using multiple views. We evaluate our method on the challenging RLBench benchmark and on a real-world robot. Notably, our approach scales to 74 diverse RLBench tasks and outperforms the state of the art. We also address instruction-conditioned tasks and demonstrate excellent generalization to previously unseen variations.

## 参考
- http://arxiv.org/abs/2209.04899v3

