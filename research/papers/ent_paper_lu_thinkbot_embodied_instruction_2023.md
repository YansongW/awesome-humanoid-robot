---
$id: ent_paper_lu_thinkbot_embodied_instruction_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ThinkBot: Embodied Instruction Following with Thought Chain Reasoning'
  zh: ThinkBot
  ko: 'ThinkBot: Embodied Instruction Following with Thought Chain Reasoning'
summary:
  en: 'ThinkBot: Embodied Instruction Following with Thought Chain Reasoning (ThinkBot), is a 2023 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua Shenzhen International Graduate School, Tsinghua University, Carnegie
    Mellon University, Department of Automation, Tsinghua University, and published at ICLR 2023.'
  zh: 'ThinkBot: Embodied Instruction Following with Thought Chain Reasoning (ThinkBot), is a 2023 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua Shenzhen International Graduate School, Tsinghua University, Carnegie
    Mellon University, Department of Automation, Tsinghua University, and published at ICLR 2023.'
  ko: 'ThinkBot: Embodied Instruction Following with Thought Chain Reasoning (ThinkBot), is a 2023 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua Shenzhen International Graduate School, Tsinghua University, Carnegie
    Mellon University, Department of Automation, Tsinghua University, and published at ICLR 2023.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- thinkbot
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2312.07062v2.
sources:
- id: src_001
  type: paper
  title: ThinkBot source
  url: https://openreview.net/forum?id=tFDTHA3odg
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
Embodied Instruction Following (EIF) requires agents to complete human instruction by interacting objects in complicated surrounding environments. Conventional methods directly consider the sparse human instruction to generate action plans for agents, which usually fail to achieve human goals because of the instruction incoherence in action descriptions. On the contrary, we propose ThinkBot that reasons the thought chain in human instruction to recover the missing action descriptions, so that the agent can successfully complete human goals by following the coherent instruction. Specifically, we first design an instruction completer based on large language models to recover the missing actions with interacted objects between consecutive human instruction, where the perceived surrounding environments and the completed sub-goals are considered for instruction completion. Based on the partially observed scene semantic maps, we present an object localizer to infer the position of interacted objects for agents to achieve complex human goals. Extensive experiments in the simulated environment show that our ThinkBot outperforms the state-of-the-art EIF methods by a sizable margin in both success rate and execution efficiency.

## 核心内容
Embodied Instruction Following (EIF) requires agents to complete human instruction by interacting objects in complicated surrounding environments. Conventional methods directly consider the sparse human instruction to generate action plans for agents, which usually fail to achieve human goals because of the instruction incoherence in action descriptions. On the contrary, we propose ThinkBot that reasons the thought chain in human instruction to recover the missing action descriptions, so that the agent can successfully complete human goals by following the coherent instruction. Specifically, we first design an instruction completer based on large language models to recover the missing actions with interacted objects between consecutive human instruction, where the perceived surrounding environments and the completed sub-goals are considered for instruction completion. Based on the partially observed scene semantic maps, we present an object localizer to infer the position of interacted objects for agents to achieve complex human goals. Extensive experiments in the simulated environment show that our ThinkBot outperforms the state-of-the-art EIF methods by a sizable margin in both success rate and execution efficiency.

## 参考
- http://arxiv.org/abs/2312.07062v2

