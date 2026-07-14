---
$id: ent_paper_safehumanoid_vlm_rag_driven_co_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SafeHumanoid: VLM-RAG-driven Control of Upper Body Impedance for Humanoid Robot'
  zh: 'SafeHumanoid: VLM-RAG-driven Control of Upper Body Impedance for Humanoid Robot'
  ko: 'SafeHumanoid: VLM-RAG-driven Control of Upper Body Impedance for Humanoid Robot'
summary:
  en: 'SafeHumanoid: VLM-RAG-driven Control of Upper Body Impedance for Humanoid Robot is a 2025 work on manipulation for
    humanoid robots.'
  zh: 'SafeHumanoid: VLM-RAG-driven Control of Upper Body Impedance for Humanoid Robot is a 2025 work on manipulation for
    humanoid robots.'
  ko: 'SafeHumanoid: VLM-RAG-driven Control of Upper Body Impedance for Humanoid Robot is a 2025 work on manipulation for
    humanoid robots.'
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
- manipulation
- safehumanoid
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.23300v1.
sources:
- id: src_001
  type: paper
  title: 'SafeHumanoid: VLM-RAG-driven Control of Upper Body Impedance for Humanoid Robot (arXiv)'
  url: https://arxiv.org/abs/2511.23300
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Safe and trustworthy Human Robot Interaction (HRI) requires robots not only to complete tasks but also to regulate impedance and speed according to scene context and human proximity. We present SafeHumanoid, an egocentric vision pipeline that links Vision Language Models (VLMs) with Retrieval-Augmented Generation (RAG) to schedule impedance and velocity parameters for a humanoid robot. Egocentric frames are processed by a structured VLM prompt, embedded and matched against a curated database of validated scenarios, and mapped to joint-level impedance commands via inverse kinematics. We evaluate the system on tabletop manipulation tasks with and without human presence, including wiping, object handovers, and liquid pouring. The results show that the pipeline adapts stiffness, damping, and speed profiles in a context-aware manner, maintaining task success while improving safety. Although current inference latency (up to 1.4 s) limits responsiveness in highly dynamic settings, SafeHumanoid demonstrates that semantic grounding of impedance control is a viable path toward safer, standard-compliant humanoid collaboration.

## 核心内容
Safe and trustworthy Human Robot Interaction (HRI) requires robots not only to complete tasks but also to regulate impedance and speed according to scene context and human proximity. We present SafeHumanoid, an egocentric vision pipeline that links Vision Language Models (VLMs) with Retrieval-Augmented Generation (RAG) to schedule impedance and velocity parameters for a humanoid robot. Egocentric frames are processed by a structured VLM prompt, embedded and matched against a curated database of validated scenarios, and mapped to joint-level impedance commands via inverse kinematics. We evaluate the system on tabletop manipulation tasks with and without human presence, including wiping, object handovers, and liquid pouring. The results show that the pipeline adapts stiffness, damping, and speed profiles in a context-aware manner, maintaining task success while improving safety. Although current inference latency (up to 1.4 s) limits responsiveness in highly dynamic settings, SafeHumanoid demonstrates that semantic grounding of impedance control is a viable path toward safer, standard-compliant humanoid collaboration.

## 参考
- http://arxiv.org/abs/2511.23300v1

