---
$id: ent_paper_cac_vla_context_gated_action_c_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CAC-VLA: Context-Gated Action Conditioning for Vision-Language-Action Models'
  zh: 'CAC-VLA: Context-Gated Action Conditioning for Vision-Language-Action Models'
  ko: ''
summary:
  en: "arXiv:2607.04816v1 Announce Type: new \nAbstract: Vision-Language-Action (VLA)\
    \ models have become a promising paradigm for generalist robot manipulation, where\
    \ visual-language representations are used to condition continuous action generation.\
    \ However, these representations are not explicitly optimized for action conditioning,\
    \ leaving the action expert to bridge the gap between multimodal understanding\
    \ and precise motor control. Recent action-reasoning methods introduce additional\
    \ modules to generate explicit action plans or action-space reasoning signals,\
    \ demonstrating the benefit of action-level guidance but often requiring separate\
    \ action-generation frameworks. We propose CAC-VLA, a Context-Gated Action Conditioning\
    \ framework that learns a lightweight latent-action interface directly within\
    \ the VLM. Instead of generating executable trajectories, CAC-VLA trains the VLM\
    \ to predict coarse-to-fine latent actions, which are structured representations\
    \ encoded from future action segments, and adaptively leverages them to condition\
    \ the action expert via a context gate. This enables VLM-native action conditioning\
    \ while calibrating the influence of latent-action guidance on expert action generation.\
    \ Experiments on LIBERO and LIBERO-Plus demonstrate the effectiveness of CAC-VLA,\
    \ achieving 98.3% average success rate on LIBERO and 89.5% LIBERO-Plus, suggesting\
    \ that context-gated latent-action conditioning is an effective interface for\
    \ continuous expert control."
  zh: "arXiv:2607.04816v1 Announce Type: new \nAbstract: Vision-Language-Action (VLA)\
    \ models have become a promising paradigm for generalist robot manipulation, where\
    \ visual-language representations are used to condition continuous action generation.\
    \ However, these representations are not explicitly optimized for action conditioning,\
    \ leaving the action expert to bridge the gap between multimodal understanding\
    \ and precise motor control. Recent action-reasoning methods introduce additional\
    \ modules to generate explicit action plans or action-space reasoning signals,\
    \ demonstrating the benefit of action-level guidance but often requiring separate\
    \ action-generation frameworks. We propose CAC-VLA, a Context-Gated Action Conditioning\
    \ framework that learns a lightweight latent-action interface directly within\
    \ the VLM. Instead of generating executable trajectories, CAC-VLA trains the VLM\
    \ to predict coarse-to-fine latent actions, which are structured representations\
    \ encoded from future action segments, and adaptively leverages them to condition\
    \ the action expert via a context gate. This enables VLM-native action conditioning\
    \ while calibrating the influence of latent-action guidance on expert action generation.\
    \ Experiments on LIBERO and LIBERO-Plus demonstrate the effectiveness of CAC-VLA,\
    \ achieving 98.3% average success rate on LIBERO and 89.5% LIBERO-Plus, suggesting\
    \ that context-gated latent-action conditioning is an effective interface for\
    \ continuous expert control."
  ko: ''
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
- robotics
- cac_vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-08'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'CAC-VLA: Context-Gated Action Conditioning for Vision-Language-Action Models
    (arXiv)'
  url: https://arxiv.org/abs/2607.04816
  date: '2026'
  accessed_at: '2026-07-08'
---

arXiv:2607.04816v1 Announce Type: new 
Abstract: Vision-Language-Action (VLA) models have become a promising paradigm for generalist robot manipulation, where visual-language representations are used to condition continuous action generation. However, these representations are not explicitly optimized for action conditioning, leaving the action expert to bridge the gap between multimodal understanding and precise motor control. Recent action-reasoning methods introduce additional modules to generate explicit action plans or action-space reasoning signals, demonstrating the benefit of action-level guidance but often requiring separate action-generation frameworks. We propose CAC-VLA, a Context-Gated Action Conditioning framework that learns a lightweight latent-action interface directly within the VLM. Instead of generating executable trajectories, CAC-VLA trains the VLM to predict coarse-to-fine latent actions, which are structured representations encoded from future action segments, and adaptively leverages them to condition the action expert via a context gate. This enables VLM-native action conditioning while calibrating the influence of latent-action guidance on expert action generation. Experiments on LIBERO and LIBERO-Plus demonstrate the effectiveness of CAC-VLA, achieving 98.3% average success rate on LIBERO and 89.5% LIBERO-Plus, suggesting that context-gated latent-action conditioning is an effective interface for continuous expert control.
