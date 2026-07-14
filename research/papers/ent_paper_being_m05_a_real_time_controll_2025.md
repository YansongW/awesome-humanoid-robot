---
$id: ent_paper_being_m05_a_real_time_controll_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Being-M0.5: A Real-Time Controllable Vision-Language-Motion Model'
  zh: 'Being-M0.5: A Real-Time Controllable Vision-Language-Motion Model'
  ko: 'Being-M0.5: A Real-Time Controllable Vision-Language-Motion Model'
summary:
  en: 'Being-M0.5: A Real-Time Controllable Vision-Language-Motion Model is a 2025 work on human motion analysis and synthesis
    for humanoid robots.'
  zh: 'Being-M0.5: A Real-Time Controllable Vision-Language-Motion Model is a 2025 work on human motion analysis and synthesis
    for humanoid robots.'
  ko: 'Being-M0.5: A Real-Time Controllable Vision-Language-Motion Model is a 2025 work on human motion analysis and synthesis
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- being_m05
- humanoid
- motion_analysis
- motion_synthesis
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.07863v1.
sources:
- id: src_001
  type: paper
  title: 'Being-M0.5: A Real-Time Controllable Vision-Language-Motion Model (arXiv)'
  url: https://arxiv.org/abs/2508.07863
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'Being-M0.5: A Real-Time Controllable Vision-Language-Motion Model project page'
  url: https://beingbeyond.github.io/Being-M0.5/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Human motion generation has emerged as a critical technology with transformative potential for real-world applications. However, existing vision-language-motion models (VLMMs) face significant limitations that hinder their practical deployment. We identify controllability as a main bottleneck, manifesting in five key aspects: inadequate response to diverse human commands, limited pose initialization capabilities, poor performance on long-term sequences, insufficient handling of unseen scenarios, and lack of fine-grained control over individual body parts. To overcome these limitations, we present Being-M0.5, the first real-time, controllable VLMM that achieves state-of-the-art performance across multiple motion generation tasks. Our approach is built upon HuMo100M, the largest and most comprehensive human motion dataset to date, comprising over 5 million self-collected motion sequences, 100 million multi-task instructional instances, and detailed part-level annotations that address a critical gap in existing datasets. We introduce a novel part-aware residual quantization technique for motion tokenization that enables precise, granular control over individual body parts during generation. Extensive experimental validation demonstrates Being-M0.5's superior performance across diverse motion benchmarks, while comprehensive efficiency analysis confirms its real-time capabilities. Our contributions include design insights and detailed computational analysis to guide future development of practical motion generators. We believe that HuMo100M and Being-M0.5 represent significant advances that will accelerate the adoption of motion generation technologies in real-world applications. The project page is available at https://beingbeyond.github.io/Being-M0.5.

## 核心内容
Human motion generation has emerged as a critical technology with transformative potential for real-world applications. However, existing vision-language-motion models (VLMMs) face significant limitations that hinder their practical deployment. We identify controllability as a main bottleneck, manifesting in five key aspects: inadequate response to diverse human commands, limited pose initialization capabilities, poor performance on long-term sequences, insufficient handling of unseen scenarios, and lack of fine-grained control over individual body parts. To overcome these limitations, we present Being-M0.5, the first real-time, controllable VLMM that achieves state-of-the-art performance across multiple motion generation tasks. Our approach is built upon HuMo100M, the largest and most comprehensive human motion dataset to date, comprising over 5 million self-collected motion sequences, 100 million multi-task instructional instances, and detailed part-level annotations that address a critical gap in existing datasets. We introduce a novel part-aware residual quantization technique for motion tokenization that enables precise, granular control over individual body parts during generation. Extensive experimental validation demonstrates Being-M0.5's superior performance across diverse motion benchmarks, while comprehensive efficiency analysis confirms its real-time capabilities. Our contributions include design insights and detailed computational analysis to guide future development of practical motion generators. We believe that HuMo100M and Being-M0.5 represent significant advances that will accelerate the adoption of motion generation technologies in real-world applications. The project page is available at https://beingbeyond.github.io/Being-M0.5.

## 参考
- http://arxiv.org/abs/2508.07863v1

