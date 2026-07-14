---
$id: ent_paper_chen_automating_robot_failure_recov_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Automating Robot Failure Recovery Using Vision-Language Models With Optimized Prompts
  zh: Automating Robot Failure Recovery Using Vision-Language Models With Optimized Prompts
  ko: Automating Robot Failure Recovery Using Vision-Language Models With Optimized Prompts
summary:
  en: Automating Robot Failure Recovery Using Vision-Language Models With Optimized Prompts (Automating Robot Failure Recovery
    Using Vision-Language Models With Optimized Prompts), is a 2024 large vision-language-action model for robotic manipulation.
  zh: Automating Robot Failure Recovery Using Vision-Language Models With Optimized Prompts (Automating Robot Failure Recovery
    Using Vision-Language Models With Optimized Prompts), is a 2024 large vision-language-action model for robotic manipulation.
  ko: Automating Robot Failure Recovery Using Vision-Language Models With Optimized Prompts (Automating Robot Failure Recovery
    Using Vision-Language Models With Optimized Prompts), is a 2024 large vision-language-action model for robotic manipulation.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- automating_robot_failure_recov
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2409.03966v1.
sources:
- id: src_001
  type: paper
  title: Automating Robot Failure Recovery Using Vision-Language Models With Optimized Prompts (arXiv)
  url: https://arxiv.org/abs/2409.03966
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Automating Robot Failure Recovery Using Vision-Language Models With Optimized Prompts source
  url: https://doi.org/10.48550/arXiv.2409.03966
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Current robot autonomy struggles to operate beyond the assumed Operational Design Domain (ODD), the specific set of conditions and environments in which the system is designed to function, while the real-world is rife with uncertainties that may lead to failures. Automating recovery remains a significant challenge. Traditional methods often rely on human intervention to manually address failures or require exhaustive enumeration of failure cases and the design of specific recovery policies for each scenario, both of which are labor-intensive. Foundational Vision-Language Models (VLMs), which demonstrate remarkable common-sense generalization and reasoning capabilities, have broader, potentially unbounded ODDs. However, limitations in spatial reasoning continue to be a common challenge for many VLMs when applied to robot control and motion-level error recovery. In this paper, we investigate how optimizing visual and text prompts can enhance the spatial reasoning of VLMs, enabling them to function effectively as black-box controllers for both motion-level position correction and task-level recovery from unknown failures. Specifically, the optimizations include identifying key visual elements in visual prompts, highlighting these elements in text prompts for querying, and decomposing the reasoning process for failure detection and control generation. In experiments, prompt optimizations significantly outperform pre-trained Vision-Language-Action Models in correcting motion-level position errors and improve accuracy by 65.78% compared to VLMs with unoptimized prompts. Additionally, for task-level failures, optimized prompts enhanced the success rate by 5.8%, 5.8%, and 7.5% in VLMs' abilities to detect failures, analyze issues, and generate recovery plans, respectively, across a wide range of unknown errors in Lego assembly.

## 核心内容
Current robot autonomy struggles to operate beyond the assumed Operational Design Domain (ODD), the specific set of conditions and environments in which the system is designed to function, while the real-world is rife with uncertainties that may lead to failures. Automating recovery remains a significant challenge. Traditional methods often rely on human intervention to manually address failures or require exhaustive enumeration of failure cases and the design of specific recovery policies for each scenario, both of which are labor-intensive. Foundational Vision-Language Models (VLMs), which demonstrate remarkable common-sense generalization and reasoning capabilities, have broader, potentially unbounded ODDs. However, limitations in spatial reasoning continue to be a common challenge for many VLMs when applied to robot control and motion-level error recovery. In this paper, we investigate how optimizing visual and text prompts can enhance the spatial reasoning of VLMs, enabling them to function effectively as black-box controllers for both motion-level position correction and task-level recovery from unknown failures. Specifically, the optimizations include identifying key visual elements in visual prompts, highlighting these elements in text prompts for querying, and decomposing the reasoning process for failure detection and control generation. In experiments, prompt optimizations significantly outperform pre-trained Vision-Language-Action Models in correcting motion-level position errors and improve accuracy by 65.78% compared to VLMs with unoptimized prompts. Additionally, for task-level failures, optimized prompts enhanced the success rate by 5.8%, 5.8%, and 7.5% in VLMs' abilities to detect failures, analyze issues, and generate recovery plans, respectively, across a wide range of unknown errors in Lego assembly.

## 参考
- http://arxiv.org/abs/2409.03966v1

