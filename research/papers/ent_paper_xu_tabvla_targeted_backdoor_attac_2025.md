---
$id: ent_paper_xu_tabvla_targeted_backdoor_attac_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TabVLA: Targeted Backdoor Attacks on Vision-Language-Action Models'
  zh: TabVLA
  ko: 'TabVLA: Targeted Backdoor Attacks on Vision-Language-Action Models'
summary:
  en: 'TabVLA: Targeted Backdoor Attacks on Vision-Language-Action Models (TabVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Fudan University, City University of Hong Kong.'
  zh: 'TabVLA: Targeted Backdoor Attacks on Vision-Language-Action Models (TabVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Fudan University, City University of Hong Kong.'
  ko: 'TabVLA: Targeted Backdoor Attacks on Vision-Language-Action Models (TabVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Fudan University, City University of Hong Kong.'
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
- tabvla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.10932v4.
sources:
- id: src_001
  type: paper
  title: 'TabVLA: Targeted Backdoor Attacks on Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2510.10932
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: TabVLA source
  url: https://doi.org/10.48550/arXiv.2510.10932
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models map multimodal perception and language instructions to executable robot actions, making them particularly vulnerable to behavioral backdoor manipulation: a hidden trigger introduced during training can induce unintended physical actions while nominal task performance remains intact. Prior work on VLA backdoors primarily studies untargeted attacks or task-level hijacking, leaving fine-grained control over individual actions largely unexplored. In this work, we present DropVLA, an action-level backdoor attack that forces a reusable action primitive (e.g., open_gripper) to execute at attacker-chosen decision points under a realistic pipeline-black-box setting with limited data-poisoning access, using a window-consistent relabeling scheme for chunked fine-tuning. On OpenVLA-7B evaluated with LIBERO, vision-only poisoning achieves 98.67%-99.83% attack success rate (ASR) with only 0.31% poisoned episodes while preserving 98.50%-99.17% clean-task retention, and successfully triggers the targeted action within 25 control steps at 500 Hz (0.05 s). Text-only triggers are unstable at low poisoning budgets, and combining text with vision provides no consistent ASR improvement over vision-only attacks. The backdoor remains robust to moderate trigger variations and transfers across evaluation suites (96.27%, 99.09%), whereas text-only largely fails (0.72%). We further validate physical-world feasibility on a 7-DoF Franka arm with pi0-fast, demonstrating non-trivial attack efficacy under camera-relative motion that induces image-plane trigger drift. These results reveal that VLA models can be covertly steered at the granularity of safety-critical actions with minimal poisoning and without observable degradation of nominal performance.

## 核心内容
Vision-Language-Action (VLA) models map multimodal perception and language instructions to executable robot actions, making them particularly vulnerable to behavioral backdoor manipulation: a hidden trigger introduced during training can induce unintended physical actions while nominal task performance remains intact. Prior work on VLA backdoors primarily studies untargeted attacks or task-level hijacking, leaving fine-grained control over individual actions largely unexplored. In this work, we present DropVLA, an action-level backdoor attack that forces a reusable action primitive (e.g., open_gripper) to execute at attacker-chosen decision points under a realistic pipeline-black-box setting with limited data-poisoning access, using a window-consistent relabeling scheme for chunked fine-tuning. On OpenVLA-7B evaluated with LIBERO, vision-only poisoning achieves 98.67%-99.83% attack success rate (ASR) with only 0.31% poisoned episodes while preserving 98.50%-99.17% clean-task retention, and successfully triggers the targeted action within 25 control steps at 500 Hz (0.05 s). Text-only triggers are unstable at low poisoning budgets, and combining text with vision provides no consistent ASR improvement over vision-only attacks. The backdoor remains robust to moderate trigger variations and transfers across evaluation suites (96.27%, 99.09%), whereas text-only largely fails (0.72%). We further validate physical-world feasibility on a 7-DoF Franka arm with pi0-fast, demonstrating non-trivial attack efficacy under camera-relative motion that induces image-plane trigger drift. These results reveal that VLA models can be covertly steered at the granularity of safety-critical actions with minimal poisoning and without observable degradation of nominal performance.

## 参考
- http://arxiv.org/abs/2510.10932v4

