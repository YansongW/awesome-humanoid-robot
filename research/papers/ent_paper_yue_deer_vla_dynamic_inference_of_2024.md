---
$id: ent_paper_yue_deer_vla_dynamic_inference_of_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution'
  zh: DeeR-VLA
  ko: 'DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution'
summary:
  en: 'DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution (DeeR-VLA), is a 2024
    large vision-language-action model for robotic manipulation, introduced by Tsinghua University, BNRist, ByteDance, and
    published at NIPS 2024.'
  zh: 'DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution (DeeR-VLA), is a 2024
    large vision-language-action model for robotic manipulation, introduced by Tsinghua University, BNRist, ByteDance, and
    published at NIPS 2024.'
  ko: 'DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution (DeeR-VLA), is a 2024
    large vision-language-action model for robotic manipulation, introduced by Tsinghua University, BNRist, ByteDance, and
    published at NIPS 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- deer_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2411.02359v1.
sources:
- id: src_001
  type: website
  title: DeeR-VLA source
  url: http://papers.nips.cc/paper_files/paper/2024/hash/67b0e7c7c2a5780aeefe3b79caac106e-Abstract-Conference.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
MLLMs have demonstrated remarkable comprehension and reasoning capabilities with complex language and visual data. These advances have spurred the vision of establishing a generalist robotic MLLM proficient in understanding complex human instructions and accomplishing various embodied tasks. However, developing MLLMs for real-world robots is challenging due to the typically limited computation and memory capacities available on robotic platforms. In contrast, the inference of MLLMs involves storing billions of parameters and performing tremendous computation, imposing significant hardware demands. In our paper, we propose a Dynamic Early-Exit Framework for Robotic Vision-Language-Action Model (DeeR-VLA, or simply DeeR) that automatically adjusts the size of the activated MLLM based on each situation at hand. The approach leverages a multi-exit architecture in MLLMs, which allows the model to terminate processing once a proper size of the model has been activated for a specific situation, thus avoiding further redundant computation. Additionally, we develop novel algorithms that establish early-termination criteria for DeeR, conditioned on predefined demands such as average computational cost (i.e., power consumption), as well as peak computational consumption (i.e., latency) and GPU memory usage. These enhancements ensure that DeeR operates efficiently under varying resource constraints while maintaining competitive performance. On the CALVIN robot manipulation benchmark, DeeR demonstrates significant reductions in computational costs of LLM by 5.2-6.5x and GPU memory of LLM by 2-6x without compromising performance. Code and checkpoints are available at https://github.com/yueyang130/DeeR-VLA.

## 核心内容
MLLMs have demonstrated remarkable comprehension and reasoning capabilities with complex language and visual data. These advances have spurred the vision of establishing a generalist robotic MLLM proficient in understanding complex human instructions and accomplishing various embodied tasks. However, developing MLLMs for real-world robots is challenging due to the typically limited computation and memory capacities available on robotic platforms. In contrast, the inference of MLLMs involves storing billions of parameters and performing tremendous computation, imposing significant hardware demands. In our paper, we propose a Dynamic Early-Exit Framework for Robotic Vision-Language-Action Model (DeeR-VLA, or simply DeeR) that automatically adjusts the size of the activated MLLM based on each situation at hand. The approach leverages a multi-exit architecture in MLLMs, which allows the model to terminate processing once a proper size of the model has been activated for a specific situation, thus avoiding further redundant computation. Additionally, we develop novel algorithms that establish early-termination criteria for DeeR, conditioned on predefined demands such as average computational cost (i.e., power consumption), as well as peak computational consumption (i.e., latency) and GPU memory usage. These enhancements ensure that DeeR operates efficiently under varying resource constraints while maintaining competitive performance. On the CALVIN robot manipulation benchmark, DeeR demonstrates significant reductions in computational costs of LLM by 5.2-6.5x and GPU memory of LLM by 2-6x without compromising performance. Code and checkpoints are available at https://github.com/yueyang130/DeeR-VLA.

## 参考
- http://arxiv.org/abs/2411.02359v1

