---
$id: ent_paper_yang_seqvla_sequential_task_executi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SeqVLA: Sequential Task Execution for Long-Horizon Manipulation with Completion-Aware Vision-Language-Action Model'
  zh: SeqVLA
  ko: 'SeqVLA: Sequential Task Execution for Long-Horizon Manipulation with Completion-Aware Vision-Language-Action Model'
summary:
  en: 'SeqVLA: Sequential Task Execution for Long-Horizon Manipulation with Completion-Aware Vision-Language-Action Model
    (SeqVLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by Drexel University, Virginia
    Tech.'
  zh: 'SeqVLA: Sequential Task Execution for Long-Horizon Manipulation with Completion-Aware Vision-Language-Action Model
    (SeqVLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by Drexel University, Virginia
    Tech.'
  ko: 'SeqVLA: Sequential Task Execution for Long-Horizon Manipulation with Completion-Aware Vision-Language-Action Model
    (SeqVLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by Drexel University, Virginia
    Tech.'
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
- seqvla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.14138v1.
sources:
- id: src_001
  type: paper
  title: 'SeqVLA: Sequential Task Execution for Long-Horizon Manipulation with Completion-Aware Vision-Language-Action Model
    (arXiv)'
  url: https://arxiv.org/abs/2509.14138
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: SeqVLA source
  url: https://doi.org/10.48550/arXiv.2509.14138
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Long-horizon robotic manipulation tasks require executing multiple interdependent subtasks in strict sequence, where errors in detecting subtask completion can cascade into downstream failures. Existing Vision-Language-Action (VLA) models such as $π_0$ excel at continuous low-level control but lack an internal signal for identifying when a subtask has finished, making them brittle in sequential settings. We propose SeqVLA, a completion-aware extension of $π_0$ that augments the base architecture with a lightweight detection head perceiving whether the current subtask is complete. This dual-head design enables SeqVLA not only to generate manipulation actions but also to autonomously trigger transitions between subtasks. We investigate four finetuning strategies that vary in how the action and detection heads are optimized (joint vs. sequential finetuning) and how pretrained knowledge is preserved (full finetuning vs. frozen backbone). Experiments are performed on two multi-stage tasks: salad packing with seven distinct subtasks and candy packing with four distinct subtasks. Results show that SeqVLA significantly outperforms the baseline $π_0$ and other strong baselines in overall success rate. In particular, joint finetuning with an unfrozen backbone yields the most decisive and statistically reliable completion predictions, eliminating sequence-related failures and enabling robust long-horizon execution. Our results highlight the importance of coupling action generation with subtask-aware detection for scalable sequential manipulation.

## 核心内容
Long-horizon robotic manipulation tasks require executing multiple interdependent subtasks in strict sequence, where errors in detecting subtask completion can cascade into downstream failures. Existing Vision-Language-Action (VLA) models such as $π_0$ excel at continuous low-level control but lack an internal signal for identifying when a subtask has finished, making them brittle in sequential settings. We propose SeqVLA, a completion-aware extension of $π_0$ that augments the base architecture with a lightweight detection head perceiving whether the current subtask is complete. This dual-head design enables SeqVLA not only to generate manipulation actions but also to autonomously trigger transitions between subtasks. We investigate four finetuning strategies that vary in how the action and detection heads are optimized (joint vs. sequential finetuning) and how pretrained knowledge is preserved (full finetuning vs. frozen backbone). Experiments are performed on two multi-stage tasks: salad packing with seven distinct subtasks and candy packing with four distinct subtasks. Results show that SeqVLA significantly outperforms the baseline $π_0$ and other strong baselines in overall success rate. In particular, joint finetuning with an unfrozen backbone yields the most decisive and statistically reliable completion predictions, eliminating sequence-related failures and enabling robust long-horizon execution. Our results highlight the importance of coupling action generation with subtask-aware detection for scalable sequential manipulation.

## 参考
- http://arxiv.org/abs/2509.14138v1

