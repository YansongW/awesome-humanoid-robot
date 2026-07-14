---
$id: ent_paper_cen_worldvla_towards_autoregressiv_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WorldVLA: Towards Autoregressive Action World Model'
  zh: WorldVLA
  ko: 'WorldVLA: Towards Autoregressive Action World Model'
summary:
  en: 'WorldVLA: Towards Autoregressive Action World Model (WorldVLA), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by DAMO Academy, Alibaba Group, Hupan Lab, Zhejiang University.'
  zh: 'WorldVLA: Towards Autoregressive Action World Model (WorldVLA), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by DAMO Academy, Alibaba Group, Hupan Lab, Zhejiang University.'
  ko: 'WorldVLA: Towards Autoregressive Action World Model (WorldVLA), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by DAMO Academy, Alibaba Group, Hupan Lab, Zhejiang University.'
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
- vision_language_action
- vla
- worldvla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.21539v1.
sources:
- id: src_001
  type: paper
  title: 'WorldVLA: Towards Autoregressive Action World Model (arXiv)'
  url: https://arxiv.org/abs/2506.21539
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: WorldVLA source
  url: https://doi.org/10.48550/arXiv.2506.21539
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We present WorldVLA, an autoregressive action world model that unifies action and image understanding and generation. Our WorldVLA intergrates Vision-Language-Action (VLA) model and world model in one single framework. The world model predicts future images by leveraging both action and image understanding, with the purpose of learning the underlying physics of the environment to improve action generation. Meanwhile, the action model generates the subsequent actions based on image observations, aiding in visual understanding and in turn helps visual generation of the world model. We demonstrate that WorldVLA outperforms standalone action and world models, highlighting the mutual enhancement between the world model and the action model. In addition, we find that the performance of the action model deteriorates when generating sequences of actions in an autoregressive manner. This phenomenon can be attributed to the model's limited generalization capability for action prediction, leading to the propagation of errors from earlier actions to subsequent ones. To address this issue, we propose an attention mask strategy that selectively masks prior actions during the generation of the current action, which shows significant performance improvement in the action chunk generation task.

## 核心内容
We present WorldVLA, an autoregressive action world model that unifies action and image understanding and generation. Our WorldVLA intergrates Vision-Language-Action (VLA) model and world model in one single framework. The world model predicts future images by leveraging both action and image understanding, with the purpose of learning the underlying physics of the environment to improve action generation. Meanwhile, the action model generates the subsequent actions based on image observations, aiding in visual understanding and in turn helps visual generation of the world model. We demonstrate that WorldVLA outperforms standalone action and world models, highlighting the mutual enhancement between the world model and the action model. In addition, we find that the performance of the action model deteriorates when generating sequences of actions in an autoregressive manner. This phenomenon can be attributed to the model's limited generalization capability for action prediction, leading to the propagation of errors from earlier actions to subsequent ones. To address this issue, we propose an attention mask strategy that selectively masks prior actions during the generation of the current action, which shows significant performance improvement in the action chunk generation task.

## 参考
- http://arxiv.org/abs/2506.21539v1

