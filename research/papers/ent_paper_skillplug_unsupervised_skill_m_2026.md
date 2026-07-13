---
$id: ent_paper_skillplug_unsupervised_skill_m_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SkillPlug: Unsupervised Skill Mining for Few-Shot Adaptation in Robotic Manipulation'
  zh: 'SkillPlug: Unsupervised Skill Mining for Few-Shot Adaptation in Robotic Manipulation'
  ko: ''
summary:
  en: "arXiv:2607.08354v1 Announce Type: new \nAbstract: Learning transferable visuomotor\
    \ imitation policies that generalize across diverse manipulation tasks and adapt\
    \ rapidly to new tasks from only a handful of demonstrations remains challenging.\
    \ Most modern policies are trained end-to-end to map observations directly to\
    \ low-level actions, offering little explicit structure for reusing and recombining\
    \ behaviors across tasks and making transfer data-inefficient under limited supervision.\
    \ We propose SkillPlug, a plug-in framework that augments an existing visuomotor\
    \ policy with a skill-conditioning module and mines a shared, transferable skill\
    \ library from raw multi-task demonstrations. SkillPlug learns skills via self-supervised\
    \ objectives that promote compact, reusable, and non-redundant behavior-level\
    \ primitives, forming a task-shared prior for compositional control. After skill\
    \ mining, we keep the learned skills fixed and specialize to unseen tasks by fine-tuning\
    \ only lightweight router and action head, enabling efficient adaptation without\
    \ full end-to-end retraining. We evaluate SkillPlug on two simulation benchmarks\
    \ and on a real robot, and observe that the mined transferable skills consistently\
    \ improve both multi-task performance and few-shot adaptation. Overall, SkillPlug\
    \ offers a scalable way to mine reusable skills that improve data-efficient generalization\
    \ in robotic manipulation."
  zh: "arXiv:2607.08354v1 Announce Type: new \nAbstract: Learning transferable visuomotor\
    \ imitation policies that generalize across diverse manipulation tasks and adapt\
    \ rapidly to new tasks from only a handful of demonstrations remains challenging.\
    \ Most modern policies are trained end-to-end to map observations directly to\
    \ low-level actions, offering little explicit structure for reusing and recombining\
    \ behaviors across tasks and making transfer data-inefficient under limited supervision.\
    \ We propose SkillPlug, a plug-in framework that augments an existing visuomotor\
    \ policy with a skill-conditioning module and mines a shared, transferable skill\
    \ library from raw multi-task demonstrations. SkillPlug learns skills via self-supervised\
    \ objectives that promote compact, reusable, and non-redundant behavior-level\
    \ primitives, forming a task-shared prior for compositional control. After skill\
    \ mining, we keep the learned skills fixed and specialize to unseen tasks by fine-tuning\
    \ only lightweight router and action head, enabling efficient adaptation without\
    \ full end-to-end retraining. We evaluate SkillPlug on two simulation benchmarks\
    \ and on a real robot, and observe that the mined transferable skills consistently\
    \ improve both multi-task performance and few-shot adaptation. Overall, SkillPlug\
    \ offers a scalable way to mine reusable skills that improve data-efficient generalization\
    \ in robotic manipulation."
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
- skillplug
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-11'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'SkillPlug: Unsupervised Skill Mining for Few-Shot Adaptation in Robotic
    Manipulation (arXiv)'
  url: https://arxiv.org/abs/2607.08354
  date: '2026'
  accessed_at: '2026-07-11'
---

arXiv:2607.08354v1 Announce Type: new 
Abstract: Learning transferable visuomotor imitation policies that generalize across diverse manipulation tasks and adapt rapidly to new tasks from only a handful of demonstrations remains challenging. Most modern policies are trained end-to-end to map observations directly to low-level actions, offering little explicit structure for reusing and recombining behaviors across tasks and making transfer data-inefficient under limited supervision. We propose SkillPlug, a plug-in framework that augments an existing visuomotor policy with a skill-conditioning module and mines a shared, transferable skill library from raw multi-task demonstrations. SkillPlug learns skills via self-supervised objectives that promote compact, reusable, and non-redundant behavior-level primitives, forming a task-shared prior for compositional control. After skill mining, we keep the learned skills fixed and specialize to unseen tasks by fine-tuning only lightweight router and action head, enabling efficient adaptation without full end-to-end retraining. We evaluate SkillPlug on two simulation benchmarks and on a real robot, and observe that the mined transferable skills consistently improve both multi-task performance and few-shot adaptation. Overall, SkillPlug offers a scalable way to mine reusable skills that improve data-efficient generalization in robotic manipulation.
