---
$id: ent_paper_liu_occvla_vision_language_action_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OccVLA: Vision-Language-Action Model with Implicit 3D Occupancy Supervision'
  zh: OccVLA
  ko: 'OccVLA: Vision-Language-Action Model with Implicit 3D Occupancy Supervision'
summary:
  en: 'OccVLA: Vision-Language-Action Model with Implicit 3D Occupancy Supervision (OccVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Qi Zhi Institute, Xi’an Jiaotong University, Fudan University,
    Shanghai Jiao Tong University, Tsinghua University.'
  zh: 'OccVLA: Vision-Language-Action Model with Implicit 3D Occupancy Supervision (OccVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Qi Zhi Institute, Xi’an Jiaotong University, Fudan University,
    Shanghai Jiao Tong University, Tsinghua University.'
  ko: 'OccVLA: Vision-Language-Action Model with Implicit 3D Occupancy Supervision (OccVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Qi Zhi Institute, Xi’an Jiaotong University, Fudan University,
    Shanghai Jiao Tong University, Tsinghua University.'
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
- occvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.05578v1.
sources:
- id: src_001
  type: paper
  title: 'OccVLA: Vision-Language-Action Model with Implicit 3D Occupancy Supervision (arXiv)'
  url: https://arxiv.org/abs/2509.05578
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: OccVLA source
  url: https://doi.org/10.48550/arXiv.2509.05578
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Multimodal large language models (MLLMs) have shown strong vision-language reasoning abilities but still lack robust 3D spatial understanding, which is critical for autonomous driving. This limitation stems from two key challenges: (1) the difficulty of constructing accessible yet effective 3D representations without expensive manual annotations, and (2) the loss of fine-grained spatial details in VLMs due to the absence of large-scale 3D vision-language pretraining. To address these challenges, we propose OccVLA, a novel framework that integrates 3D occupancy representations into a unified multimodal reasoning process. Unlike prior approaches that rely on explicit 3D inputs, OccVLA treats dense 3D occupancy as both a predictive output and a supervisory signal, enabling the model to learn fine-grained spatial structures directly from 2D visual inputs. The occupancy predictions are regarded as implicit reasoning processes and can be skipped during inference without performance degradation, thereby adding no extra computational overhead. OccVLA achieves state-of-the-art results on the nuScenes benchmark for trajectory planning and demonstrates superior performance on 3D visual question-answering tasks, offering a scalable, interpretable, and fully vision-based solution for autonomous driving.

## 核心内容
Multimodal large language models (MLLMs) have shown strong vision-language reasoning abilities but still lack robust 3D spatial understanding, which is critical for autonomous driving. This limitation stems from two key challenges: (1) the difficulty of constructing accessible yet effective 3D representations without expensive manual annotations, and (2) the loss of fine-grained spatial details in VLMs due to the absence of large-scale 3D vision-language pretraining. To address these challenges, we propose OccVLA, a novel framework that integrates 3D occupancy representations into a unified multimodal reasoning process. Unlike prior approaches that rely on explicit 3D inputs, OccVLA treats dense 3D occupancy as both a predictive output and a supervisory signal, enabling the model to learn fine-grained spatial structures directly from 2D visual inputs. The occupancy predictions are regarded as implicit reasoning processes and can be skipped during inference without performance degradation, thereby adding no extra computational overhead. OccVLA achieves state-of-the-art results on the nuScenes benchmark for trajectory planning and demonstrates superior performance on 3D visual question-answering tasks, offering a scalable, interpretable, and fully vision-based solution for autonomous driving.

## 参考
- http://arxiv.org/abs/2509.05578v1

