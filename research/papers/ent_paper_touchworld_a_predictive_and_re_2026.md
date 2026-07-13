---
$id: ent_paper_touchworld_a_predictive_and_re_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous
    Manipulation'
  zh: 'TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous
    Manipulation'
  ko: ''
summary:
  en: "arXiv:2607.07287v1 Announce Type: new \nAbstract: Dexterous manipulation in\
    \ everyday environments requires both anticipation and reaction: a robot must\
    \ predict how contact should evolve while rapidly correcting local errors caused\
    \ by slip, misalignment, unstable grasping, or force mismatch. Vision and language\
    \ provide semantic and geometric guidance, but they cannot reliably reveal hidden\
    \ contact states such as force, slip, and contact stability. Although tactile\
    \ sensing exposes these physical cues, most existing policies treat touch as a\
    \ low-frequency observation stream within a monolithic action model, coupling\
    \ slow task reasoning, action generation, and fast contact feedback in a single\
    \ loop. We introduce TouchWorld, a predictive-and-reactive tactile foundation\
    \ model for dexterous manipulation. TouchWorld uses a hierarchical policy that\
    \ separates vision-language subtask planning, tactile world-model prediction,\
    \ visuo-tactile goal-conditioned action generation, and high-frequency tactile\
    \ residual refinement. A High-Level Planning Layer produces executable subtasks\
    \ and predicts tactile subgoals; a Visuo-Tactile Goal-Conditioned Policy generates\
    \ nominal action chunks; and a Tactile-Conditioned Refinement Policy performs\
    \ online residual correction using recent tactile and proprioceptive feedback.\
    \ By using touch as both a predictive contact reference and a fast feedback signal,\
    \ TouchWorld preserves the semantic generalization of vision-language-action policies\
    \ while improving local contact adaptation. Across six long-horizon and contact-rich\
    \ dexterous manipulation tasks, TouchWorld achieves 65.0% success in the clean\
    \ setting and 53.7% success under human perturbations, outperforming the strongest\
    \ baseline by 15.7 and 18.5 percentage points, respectively."
  zh: "arXiv:2607.07287v1 Announce Type: new \nAbstract: Dexterous manipulation in\
    \ everyday environments requires both anticipation and reaction: a robot must\
    \ predict how contact should evolve while rapidly correcting local errors caused\
    \ by slip, misalignment, unstable grasping, or force mismatch. Vision and language\
    \ provide semantic and geometric guidance, but they cannot reliably reveal hidden\
    \ contact states such as force, slip, and contact stability. Although tactile\
    \ sensing exposes these physical cues, most existing policies treat touch as a\
    \ low-frequency observation stream within a monolithic action model, coupling\
    \ slow task reasoning, action generation, and fast contact feedback in a single\
    \ loop. We introduce TouchWorld, a predictive-and-reactive tactile foundation\
    \ model for dexterous manipulation. TouchWorld uses a hierarchical policy that\
    \ separates vision-language subtask planning, tactile world-model prediction,\
    \ visuo-tactile goal-conditioned action generation, and high-frequency tactile\
    \ residual refinement. A High-Level Planning Layer produces executable subtasks\
    \ and predicts tactile subgoals; a Visuo-Tactile Goal-Conditioned Policy generates\
    \ nominal action chunks; and a Tactile-Conditioned Refinement Policy performs\
    \ online residual correction using recent tactile and proprioceptive feedback.\
    \ By using touch as both a predictive contact reference and a fast feedback signal,\
    \ TouchWorld preserves the semantic generalization of vision-language-action policies\
    \ while improving local contact adaptation. Across six long-horizon and contact-rich\
    \ dexterous manipulation tasks, TouchWorld achieves 65.0% success in the clean\
    \ setting and 53.7% success under human perturbations, outperforming the strongest\
    \ baseline by 15.7 and 18.5 percentage points, respectively."
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
- touchworld
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-10'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous
    Manipulation (arXiv)'
  url: https://arxiv.org/abs/2607.07287
  date: '2026'
  accessed_at: '2026-07-10'
---

arXiv:2607.07287v1 Announce Type: new 
Abstract: Dexterous manipulation in everyday environments requires both anticipation and reaction: a robot must predict how contact should evolve while rapidly correcting local errors caused by slip, misalignment, unstable grasping, or force mismatch. Vision and language provide semantic and geometric guidance, but they cannot reliably reveal hidden contact states such as force, slip, and contact stability. Although tactile sensing exposes these physical cues, most existing policies treat touch as a low-frequency observation stream within a monolithic action model, coupling slow task reasoning, action generation, and fast contact feedback in a single loop. We introduce TouchWorld, a predictive-and-reactive tactile foundation model for dexterous manipulation. TouchWorld uses a hierarchical policy that separates vision-language subtask planning, tactile world-model prediction, visuo-tactile goal-conditioned action generation, and high-frequency tactile residual refinement. A High-Level Planning Layer produces executable subtasks and predicts tactile subgoals; a Visuo-Tactile Goal-Conditioned Policy generates nominal action chunks; and a Tactile-Conditioned Refinement Policy performs online residual correction using recent tactile and proprioceptive feedback. By using touch as both a predictive contact reference and a fast feedback signal, TouchWorld preserves the semantic generalization of vision-language-action policies while improving local contact adaptation. Across six long-horizon and contact-rich dexterous manipulation tasks, TouchWorld achieves 65.0% success in the clean setting and 53.7% success under human perturbations, outperforming the strongest baseline by 15.7 and 18.5 percentage points, respectively.
