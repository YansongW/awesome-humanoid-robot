---
$id: ent_paper_zhong_flowvla_visual_chain_of_though_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FlowVLA: Visual Chain of Thought-based Motion Reasoning for Vision-Language-Action Models'
  zh: FlowVLA
  ko: 'FlowVLA: Visual Chain of Thought-based Motion Reasoning for Vision-Language-Action Models'
summary:
  en: 'FlowVLA: Visual Chain of Thought-based Motion Reasoning for Vision-Language-Action Models (FlowVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by HKUST(GZ), Shanghai Jiao Tong University.'
  zh: 'FlowVLA: Visual Chain of Thought-based Motion Reasoning for Vision-Language-Action Models (FlowVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by HKUST(GZ), Shanghai Jiao Tong University.'
  ko: 'FlowVLA: Visual Chain of Thought-based Motion Reasoning for Vision-Language-Action Models (FlowVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by HKUST(GZ), Shanghai Jiao Tong University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- flowvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.18269v3.
sources:
- id: src_001
  type: paper
  title: 'FlowVLA: Visual Chain of Thought-based Motion Reasoning for Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2508.18269
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Many Vision-Language-Action (VLA) models are built upon an internal world model trained via next-frame prediction ``$v_t \rightarrow v_{t+1}$''. However, this paradigm attempts to predict the future frame's appearance directly, without explicitly reasoning about the underlying dynamics. \textbf{This lack of an explicit motion reasoning step} often leads to physically implausible visual forecasts and inefficient policy learning. To address this limitation, we introduce the \textbf{Visual Chain of Thought (Visual CoT)}, a paradigm that compels the model to first reason about \textbf{motion dynamics} before generating the future frame. We instantiate this paradigm by proposing \textbf{FlowVLA}, an autoregressive Transformer that explicitly materializes this reasoning process as ``$v_t \rightarrow f_t \rightarrow v_{t+1}$'', where $f_t$ is an intermediate optical flow prediction that inherently encodes motion. By forcing the model to first follow the motion plan encoded by $f_t$, this process inherently \textbf{aligns the pre-training objective of dynamics prediction with the downstream task of action generation.} We conduct experiments on challenging robotics manipulation benchmarks, as well as real-robot evaluations. Our FlowVLA not only generates \textbf{more coherent and physically plausible visual predictions}, but also achieves state-of-the-art policy performance with \textbf{substantially improved sample efficiency}, pointing toward a more principled foundation for world modeling in VLAs. Project page: https://irpn-lab.github.io/FlowVLA/

## 核心内容
Many Vision-Language-Action (VLA) models are built upon an internal world model trained via next-frame prediction ``$v_t \rightarrow v_{t+1}$''. However, this paradigm attempts to predict the future frame's appearance directly, without explicitly reasoning about the underlying dynamics. \textbf{This lack of an explicit motion reasoning step} often leads to physically implausible visual forecasts and inefficient policy learning. To address this limitation, we introduce the \textbf{Visual Chain of Thought (Visual CoT)}, a paradigm that compels the model to first reason about \textbf{motion dynamics} before generating the future frame. We instantiate this paradigm by proposing \textbf{FlowVLA}, an autoregressive Transformer that explicitly materializes this reasoning process as ``$v_t \rightarrow f_t \rightarrow v_{t+1}$'', where $f_t$ is an intermediate optical flow prediction that inherently encodes motion. By forcing the model to first follow the motion plan encoded by $f_t$, this process inherently \textbf{aligns the pre-training objective of dynamics prediction with the downstream task of action generation.} We conduct experiments on challenging robotics manipulation benchmarks, as well as real-robot evaluations. Our FlowVLA not only generates \textbf{more coherent and physically plausible visual predictions}, but also achieves state-of-the-art policy performance with \textbf{substantially improved sample efficiency}, pointing toward a more principled foundation for world modeling in VLAs. Project page: https://irpn-lab.github.io/FlowVLA/

## 参考
- http://arxiv.org/abs/2508.18269v3

