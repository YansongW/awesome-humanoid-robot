---
$id: ent_paper_lin_failsafe_reasoning_and_recover_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FailSafe: Reasoning and Recovery from Failures in Vision-Language-Action Models'
  zh: FailSafe
  ko: 'FailSafe: Reasoning and Recovery from Failures in Vision-Language-Action Models'
summary:
  en: 'FailSafe: Reasoning and Recovery from Failures in Vision-Language-Action Models (FailSafe), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Washington.'
  zh: 'FailSafe: Reasoning and Recovery from Failures in Vision-Language-Action Models (FailSafe), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Washington.'
  ko: 'FailSafe: Reasoning and Recovery from Failures in Vision-Language-Action Models (FailSafe), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Washington.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- failsafe
- large_vla_model
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.01642v4.
sources:
- id: src_001
  type: paper
  title: 'FailSafe: Reasoning and Recovery from Failures in Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2510.01642
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: FailSafe source
  url: https://doi.org/10.48550/arXiv.2510.01642
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent advances in robotic manipulation have integrated low-level robotic control into Vision-Language Models (VLMs), extending them into Vision-Language-Action (VLA) models. Although state-of-the-art VLAs achieve strong performance in downstream robotic applications, supported by large-scale crowd-sourced robot training data, they still inevitably encounter failures during execution. Enabling robots to reason and recover from unpredictable and abrupt failures remains a critical challenge. Existing robotic manipulation datasets, collected in either simulation or the real world, primarily provide only ground-truth trajectories, leaving robots unable to recover once failures occur. Moreover, the few datasets that address failure detection typically offer only textual explanations, which are difficult to utilize directly in VLA models. To address this gap, we introduce FailSafe, a novel failure generation and recovery system that automatically produces diverse failure cases paired with executable recovery actions. FailSafe can be easily adapted to a wide range of manipulation tasks in simulators with motion planning support, enabling scalable creation of failure-action data. To demonstrate its effectiveness, we fine-tune LLaVA-OneVision-7B (LLaVA-OV-7B) to build FailSafe-VLM. Experimental results show that FailSafe-VLM successfully helps robotic arms detect and recover from potential failures, improving the performance of three state-of-the-art VLA models (Pi-0-FAST, OpenVLA, OpenVLA-OFT) by up to 22.6% on average across several tasks in ManiSkill. Furthermore, FailSafe-VLM could generalize across different spatial configurations, camera viewpoints, object and robotic embodiments.

## 核心内容
Recent advances in robotic manipulation have integrated low-level robotic control into Vision-Language Models (VLMs), extending them into Vision-Language-Action (VLA) models. Although state-of-the-art VLAs achieve strong performance in downstream robotic applications, supported by large-scale crowd-sourced robot training data, they still inevitably encounter failures during execution. Enabling robots to reason and recover from unpredictable and abrupt failures remains a critical challenge. Existing robotic manipulation datasets, collected in either simulation or the real world, primarily provide only ground-truth trajectories, leaving robots unable to recover once failures occur. Moreover, the few datasets that address failure detection typically offer only textual explanations, which are difficult to utilize directly in VLA models. To address this gap, we introduce FailSafe, a novel failure generation and recovery system that automatically produces diverse failure cases paired with executable recovery actions. FailSafe can be easily adapted to a wide range of manipulation tasks in simulators with motion planning support, enabling scalable creation of failure-action data. To demonstrate its effectiveness, we fine-tune LLaVA-OneVision-7B (LLaVA-OV-7B) to build FailSafe-VLM. Experimental results show that FailSafe-VLM successfully helps robotic arms detect and recover from potential failures, improving the performance of three state-of-the-art VLA models (Pi-0-FAST, OpenVLA, OpenVLA-OFT) by up to 22.6% on average across several tasks in ManiSkill. Furthermore, FailSafe-VLM could generalize across different spatial configurations, camera viewpoints, object and robotic embodiments.

## 参考
- http://arxiv.org/abs/2510.01642v4

