---
$id: ent_paper_rhinovla_technical_report_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: RhinoVLA Technical Report
  zh: RhinoVLA Technical Report
  ko: RhinoVLA Technical Report
summary:
  en: "arXiv:2606.07383v2 Announce Type: replace \nAbstract: Vision-Language-Action\
    \ (VLA) models have shown strong potential for robotic manipulation, but real-time\
    \ deployment on edge hardware remains challenging. In this work, we identify VLM\
    \ visual and context tokens as a major source of deployment latency: for GEMM-dominated\
    \ projection operators, computation grows linearly with the number of input tokens\
    \ when model dimensions are fixed. Motivated by this observation, we propose RhinoVLA,\
    \ a deployment-oriented VLA model co-designed with the Huixi R1 edge SoC. RhinoVLA\
    \ adopts a token-efficient Qwen3-VL backbone and a continuous Action Expert, reducing\
    \ the VLM-side token and computation burden while preserving pretrained multimodal\
    \ capability. To support cross-robot learning, RhinoVLA further introduces a unified\
    \ interface that combines View Registry, 72D physical state-action slot space,\
    \ and robotinstance LoRA, allowing heterogeneous robot observations and action\
    \ schemas to be aligned under a shared policy. On the deployment side, RhinoVLA\
    \ is optimized through hardware-aware compilation, mixed-precision execution,\
    \ and parallel visual encoding. Experiments show that RhinoVLA achieves downstream\
    \ performance comparable to {\\pi}0.5 at a similar parameter scale, while reaching\
    \ 11.69 Hz end-to-end inference on Huixi R1, meeting the 10 Hz real-time closedloop\
    \ control target. The project will be open-sourced at https://github.com/HuixiAI/RhinoVLA."
  zh: "arXiv:2606.07383v2 Announce Type: replace \nAbstract: Vision-Language-Action\
    \ (VLA) models have shown strong potential for robotic manipulation, but real-time\
    \ deployment on edge hardware remains challenging. In this work, we identify VLM\
    \ visual and context tokens as a major source of deployment latency: for GEMM-dominated\
    \ projection operators, computation grows linearly with the number of input tokens\
    \ when model dimensions are fixed. Motivated by this observation, we propose RhinoVLA,\
    \ a deployment-oriented VLA model co-designed with the Huixi R1 edge SoC. RhinoVLA\
    \ adopts a token-efficient Qwen3-VL backbone and a continuous Action Expert, reducing\
    \ the VLM-side token and computation burden while preserving pretrained multimodal\
    \ capability. To support cross-robot learning, RhinoVLA further introduces a unified\
    \ interface that combines View Registry, 72D physical state-action slot space,\
    \ and robotinstance LoRA, allowing heterogeneous robot observations and action\
    \ schemas to be aligned under a shared policy. On the deployment side, RhinoVLA\
    \ is optimized through hardware-aware compilation, mixed-precision execution,\
    \ and parallel visual encoding. Experiments show that RhinoVLA achieves downstream\
    \ performance comparable to {\\pi}0.5 at a similar parameter scale, while reaching\
    \ 11.69 Hz end-to-end inference on Huixi R1, meeting the 10 Hz real-time closedloop\
    \ control target. The project will be open-sourced at https://github.com/HuixiAI/RhinoVLA."
  ko: "arXiv:2606.07383v2 Announce Type: replace \nAbstract: Vision-Language-Action\
    \ (VLA) models have shown strong potential for robotic manipulation, but real-time\
    \ deployment on edge hardware remains challenging. In this work, we identify VLM\
    \ visual and context tokens as a major source of deployment latency: for GEMM-dominated\
    \ projection operators, computation grows linearly with the number of input tokens\
    \ when model dimensions are fixed. Motivated by this observation, we propose RhinoVLA,\
    \ a deployment-oriented VLA model co-designed with the Huixi R1 edge SoC. RhinoVLA\
    \ adopts a token-efficient Qwen3-VL backbone and a continuous Action Expert, reducing\
    \ the VLM-side token and computation burden while preserving pretrained multimodal\
    \ capability. To support cross-robot learning, RhinoVLA further introduces a unified\
    \ interface that combines View Registry, 72D physical state-action slot space,\
    \ and robotinstance LoRA, allowing heterogeneous robot observations and action\
    \ schemas to be aligned under a shared policy. On the deployment side, RhinoVLA\
    \ is optimized through hardware-aware compilation, mixed-precision execution,\
    \ and parallel visual encoding. Experiments show that RhinoVLA achieves downstream\
    \ performance comparable to {\\pi}0.5 at a similar parameter scale, while reaching\
    \ 11.69 Hz end-to-end inference on Huixi R1, meeting the 10 Hz real-time closedloop\
    \ control target. The project will be open-sourced at https://github.com/HuixiAI/RhinoVLA."
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
- rhinovla_technical_report
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: Imported from arXiv cs.RO RSS feed.
sources:
- id: src_001
  type: paper
  title: RhinoVLA Technical Report
  url: https://arxiv.org/abs/2606.07383
  date: '2026'
  accessed_at: '2026-07-01'
---

## 概述
arXiv:2606.07383v2 Announce Type: replace 
Abstract: Vision-Language-Action (VLA) models have shown strong potential for robotic manipulation, but real-time deployment on edge hardware remains challenging. In this work, we identify VLM visual and context tokens as a major source of deployment latency: for GEMM-dominated projection operators, computation grows linearly with the number of input tokens when model dimensions are fixed. Motivated by this observation, we propose RhinoVLA, a deployment-oriented VLA model co-designed with the Huixi R1 edge SoC. RhinoVLA adopts a token-efficient Qwen3-VL backbone and a continuous Action Expert, reducing the VLM-side token and computation burden while preserving pretrained multimodal capability. To support cross-robot learning, RhinoVLA further introduces a unified interface that combines View Registry, 72D physical state-action slot space, and robotinstance LoRA, allowing heterogeneous robot observations and action schemas to be aligned under a shared policy. On the deployment side, RhinoVLA is optimized through hardware-aware compilation, mixed-precision execution, and parallel visual encoding. Experiments show that RhinoVLA achieves downstream performance comparable to {\pi}0.5 at a similar parameter scale, while reaching 11.69 Hz end-to-end inference on Huixi R1, meeting the 10 Hz real-time closedloop control target. The project will be open-sourced at https://github.com/HuixiAI/RhinoVLA.

## Overview
arXiv:2606.07383v2 Announce Type: replace 
Abstract: Vision-Language-Action (VLA) models have shown strong potential for robotic manipulation, but real-time deployment on edge hardware remains challenging. In this work, we identify VLM visual and context tokens as a major source of deployment latency: for GEMM-dominated projection operators, computation grows linearly with the number of input tokens when model dimensions are fixed. Motivated by this observation, we propose RhinoVLA, a deployment-oriented VLA model co-designed with the Huixi R1 edge SoC. RhinoVLA adopts a token-efficient Qwen3-VL backbone and a continuous Action Expert, reducing the VLM-side token and computation burden while preserving pretrained multimodal capability. To support cross-robot learning, RhinoVLA further introduces a unified interface that combines View Registry, 72D physical state-action slot space, and robotinstance LoRA, allowing heterogeneous robot observations and action schemas to be aligned under a shared policy. On the deployment side, RhinoVLA is optimized through hardware-aware compilation, mixed-precision execution, and parallel visual encoding. Experiments show that RhinoVLA achieves downstream performance comparable to {\pi}0.5 at a similar parameter scale, while reaching 11.69 Hz end-to-end inference on Huixi R1, meeting the 10 Hz real-time closedloop control target. The project will be open-sourced at https://github.com/HuixiAI/RhinoVLA.

## 개요
arXiv:2606.07383v2 Announce Type: replace 
Abstract: Vision-Language-Action (VLA) models have shown strong potential for robotic manipulation, but real-time deployment on edge hardware remains challenging. In this work, we identify VLM visual and context tokens as a major source of deployment latency: for GEMM-dominated projection operators, computation grows linearly with the number of input tokens when model dimensions are fixed. Motivated by this observation, we propose RhinoVLA, a deployment-oriented VLA model co-designed with the Huixi R1 edge SoC. RhinoVLA adopts a token-efficient Qwen3-VL backbone and a continuous Action Expert, reducing the VLM-side token and computation burden while preserving pretrained multimodal capability. To support cross-robot learning, RhinoVLA further introduces a unified interface that combines View Registry, 72D physical state-action slot space, and robotinstance LoRA, allowing heterogeneous robot observations and action schemas to be aligned under a shared policy. On the deployment side, RhinoVLA is optimized through hardware-aware compilation, mixed-precision execution, and parallel visual encoding. Experiments show that RhinoVLA achieves downstream performance comparable to {\pi}0.5 at a similar parameter scale, while reaching 11.69 Hz end-to-end inference on Huixi R1, meeting the 10 Hz real-time closedloop control target. The project will be open-sourced at https://github.com/HuixiAI/RhinoVLA.
