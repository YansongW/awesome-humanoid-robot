---
$id: ent_paper_think_proprioceptively_state_g_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Think Proprioceptively: State-Grounded Visual Token Selection for VLA Policies'
  zh: 'Think Proprioceptively: State-Grounded Visual Token Selection for VLA Policies'
  ko: 'Think Proprioceptively: State-Grounded Visual Token Selection for VLA Policies'
summary:
  en: "arXiv:2602.06575v2 Announce Type: replace \nAbstract: Vision-language-action\
    \ (VLA) models typically inject proprioception only as a late conditioning signal,\
    \ preventing robot state from grounding instruction understanding or directing\
    \ visual attention. We introduce ThinkProprio, which discretizes proprioception\
    \ into VLM-vocabulary tokens and uses them jointly with the instruction to gate\
    \ visual patches before VLM computation, steering the model toward action-relevant\
    \ evidence while discarding redundant tokens early. We find that proprioception\
    \ added as a passive conditioning signal leaves performance essentially unchanged;\
    \ its value emerges when token-form state acts as an active query that, with the\
    \ instruction, selects which visual patches the VLM processes. Systematic ablations\
    \ show that VLM-vocabulary tokens outperform learned projectors as the state encoding,\
    \ and that retaining only about \\SI{12}{\\percent} of the visual tokens surpasses\
    \ on CALVIN ABC$\\to$D. Across CALVIN, LIBERO, and real-world manipulation, ThinkProprio\
    \ reduces end-to-end inference latency while improving the matched full-token\
    \ baseline."
  zh: "arXiv:2602.06575v2 Announce Type: replace \nAbstract: Vision-language-action\
    \ (VLA) models typically inject proprioception only as a late conditioning signal,\
    \ preventing robot state from grounding instruction understanding or directing\
    \ visual attention. We introduce ThinkProprio, which discretizes proprioception\
    \ into VLM-vocabulary tokens and uses them jointly with the instruction to gate\
    \ visual patches before VLM computation, steering the model toward action-relevant\
    \ evidence while discarding redundant tokens early. We find that proprioception\
    \ added as a passive conditioning signal leaves performance essentially unchanged;\
    \ its value emerges when token-form state acts as an active query that, with the\
    \ instruction, selects which visual patches the VLM processes. Systematic ablations\
    \ show that VLM-vocabulary tokens outperform learned projectors as the state encoding,\
    \ and that retaining only about \\SI{12}{\\percent} of the visual tokens surpasses\
    \ on CALVIN ABC$\\to$D. Across CALVIN, LIBERO, and real-world manipulation, ThinkProprio\
    \ reduces end-to-end inference latency while improving the matched full-token\
    \ baseline."
  ko: "arXiv:2602.06575v2 Announce Type: replace \nAbstract: Vision-language-action\
    \ (VLA) models typically inject proprioception only as a late conditioning signal,\
    \ preventing robot state from grounding instruction understanding or directing\
    \ visual attention. We introduce ThinkProprio, which discretizes proprioception\
    \ into VLM-vocabulary tokens and uses them jointly with the instruction to gate\
    \ visual patches before VLM computation, steering the model toward action-relevant\
    \ evidence while discarding redundant tokens early. We find that proprioception\
    \ added as a passive conditioning signal leaves performance essentially unchanged;\
    \ its value emerges when token-form state acts as an active query that, with the\
    \ instruction, selects which visual patches the VLM processes. Systematic ablations\
    \ show that VLM-vocabulary tokens outperform learned projectors as the state encoding,\
    \ and that retaining only about \\SI{12}{\\percent} of the visual tokens surpasses\
    \ on CALVIN ABC$\\to$D. Across CALVIN, LIBERO, and real-world manipulation, ThinkProprio\
    \ reduces end-to-end inference latency while improving the matched full-token\
    \ baseline."
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
- think_proprioceptively
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
  title: 'Think Proprioceptively: State-Grounded Visual Token Selection for VLA Policies
    (arXiv)'
  url: https://arxiv.org/abs/2602.06575
  date: '2026'
  accessed_at: '2026-07-08'
---

## 概述
arXiv:2602.06575v2 Announce Type: replace 
Abstract: Vision-language-action (VLA) models typically inject proprioception only as a late conditioning signal, preventing robot state from grounding instruction understanding or directing visual attention. We introduce ThinkProprio, which discretizes proprioception into VLM-vocabulary tokens and uses them jointly with the instruction to gate visual patches before VLM computation, steering the model toward action-relevant evidence while discarding redundant tokens early. We find that proprioception added as a passive conditioning signal leaves performance essentially unchanged; its value emerges when token-form state acts as an active query that, with the instruction, selects which visual patches the VLM processes. Systematic ablations show that VLM-vocabulary tokens outperform learned projectors as the state encoding, and that retaining only about \SI{12}{\percent} of the visual tokens surpasses on CALVIN ABC$\to$D. Across CALVIN, LIBERO, and real-world manipulation, ThinkProprio reduces end-to-end inference latency while improving the matched full-token baseline.

## Overview
arXiv:2602.06575v2 Announce Type: replace 
Abstract: Vision-language-action (VLA) models typically inject proprioception only as a late conditioning signal, preventing robot state from grounding instruction understanding or directing visual attention. We introduce ThinkProprio, which discretizes proprioception into VLM-vocabulary tokens and uses them jointly with the instruction to gate visual patches before VLM computation, steering the model toward action-relevant evidence while discarding redundant tokens early. We find that proprioception added as a passive conditioning signal leaves performance essentially unchanged; its value emerges when token-form state acts as an active query that, with the instruction, selects which visual patches the VLM processes. Systematic ablations show that VLM-vocabulary tokens outperform learned projectors as the state encoding, and that retaining only about \SI{12}{\percent} of the visual tokens surpasses on CALVIN ABC$\to$D. Across CALVIN, LIBERO, and real-world manipulation, ThinkProprio reduces end-to-end inference latency while improving the matched full-token baseline.

## 개요
arXiv:2602.06575v2 Announce Type: replace 
Abstract: Vision-language-action (VLA) models typically inject proprioception only as a late conditioning signal, preventing robot state from grounding instruction understanding or directing visual attention. We introduce ThinkProprio, which discretizes proprioception into VLM-vocabulary tokens and uses them jointly with the instruction to gate visual patches before VLM computation, steering the model toward action-relevant evidence while discarding redundant tokens early. We find that proprioception added as a passive conditioning signal leaves performance essentially unchanged; its value emerges when token-form state acts as an active query that, with the instruction, selects which visual patches the VLM processes. Systematic ablations show that VLM-vocabulary tokens outperform learned projectors as the state encoding, and that retaining only about \SI{12}{\percent} of the visual tokens surpasses on CALVIN ABC$\to$D. Across CALVIN, LIBERO, and real-world manipulation, ThinkProprio reduces end-to-end inference latency while improving the matched full-token baseline.
