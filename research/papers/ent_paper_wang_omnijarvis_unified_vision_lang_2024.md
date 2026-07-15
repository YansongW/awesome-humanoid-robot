---
$id: ent_paper_wang_omnijarvis_unified_vision_lang_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniJARVIS: Unified Vision-Language-Action Tokenization Enables Open-World Instruction Following Agents'
  zh: OmniJARVIS
  ko: 'OmniJARVIS: Unified Vision-Language-Action Tokenization Enables Open-World Instruction Following Agents'
summary:
  en: 'OmniJARVIS: Unified Vision-Language-Action Tokenization Enables Open-World Instruction Following Agents (OmniJARVIS),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by Peking University, The Chinese University
    of Hong Kong, Shenzhen, and published at NIPS24.'
  zh: 'OmniJARVIS: Unified Vision-Language-Action Tokenization Enables Open-World Instruction Following Agents (OmniJARVIS),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by Peking University, The Chinese University
    of Hong Kong, Shenzhen, and published at NIPS24.'
  ko: 'OmniJARVIS: Unified Vision-Language-Action Tokenization Enables Open-World Instruction Following Agents (OmniJARVIS),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by Peking University, The Chinese University
    of Hong Kong, Shenzhen, and published at NIPS24.'
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
- omnijarvis
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2407.00114v2.
sources:
- id: src_001
  type: website
  title: OmniJARVIS source
  url: http://papers.nips.cc/paper_files/paper/2024/hash/85f1225db986e629289f402c46eff1a4-Abstract-Conference.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
This paper presents OmniJARVIS, a novel Vision-Language-Action (VLA) model for open-world instruction-following agents in Minecraft. Compared to prior works that either emit textual goals to separate controllers or produce the control command directly, OmniJARVIS seeks a different path to ensure both strong reasoning and efficient decision-making capabilities via unified tokenization of multimodal interaction data. First, we introduce a self-supervised approach to learn a behavior encoder that produces discretized tokens for behavior trajectories $τ= \{o_0, a_0, \dots\}$ and an imitation learning policy decoder conditioned on these tokens. These additional behavior tokens will be augmented to the vocabulary of pretrained Multimodal Language Models. With this encoder, we then pack long-term multimodal interactions involving task instructions, memories, thoughts, observations, textual responses, behavior trajectories, etc into unified token sequences and model them with autoregressive transformers. Thanks to the semantically meaningful behavior tokens, the resulting VLA model, OmniJARVIS, can reason (by producing chain-of-thoughts), plan, answer questions, and act (by producing behavior tokens for the imitation learning policy decoder). OmniJARVIS demonstrates excellent performances on a comprehensive collection of atomic, programmatic, and open-ended tasks in open-world Minecraft. Our analysis further unveils the crucial design principles in interaction data formation, unified tokenization, and its scaling potentials. The dataset, models, and code will be released at https://craftjarvis.org/OmniJARVIS.

## 核心内容
This paper presents OmniJARVIS, a novel Vision-Language-Action (VLA) model for open-world instruction-following agents in Minecraft. Compared to prior works that either emit textual goals to separate controllers or produce the control command directly, OmniJARVIS seeks a different path to ensure both strong reasoning and efficient decision-making capabilities via unified tokenization of multimodal interaction data. First, we introduce a self-supervised approach to learn a behavior encoder that produces discretized tokens for behavior trajectories $τ= \{o_0, a_0, \dots\}$ and an imitation learning policy decoder conditioned on these tokens. These additional behavior tokens will be augmented to the vocabulary of pretrained Multimodal Language Models. With this encoder, we then pack long-term multimodal interactions involving task instructions, memories, thoughts, observations, textual responses, behavior trajectories, etc into unified token sequences and model them with autoregressive transformers. Thanks to the semantically meaningful behavior tokens, the resulting VLA model, OmniJARVIS, can reason (by producing chain-of-thoughts), plan, answer questions, and act (by producing behavior tokens for the imitation learning policy decoder). OmniJARVIS demonstrates excellent performances on a comprehensive collection of atomic, programmatic, and open-ended tasks in open-world Minecraft. Our analysis further unveils the crucial design principles in interaction data formation, unified tokenization, and its scaling potentials. The dataset, models, and code will be released at https://craftjarvis.org/OmniJARVIS.

## 参考
- http://arxiv.org/abs/2407.00114v2

