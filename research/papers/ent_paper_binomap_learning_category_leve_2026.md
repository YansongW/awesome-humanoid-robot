---
$id: ent_paper_binomap_learning_category_leve_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'BiNoMaP: Learning Category-Level Bimanual Non-Prehensile Manipulation Primitives'
  zh: 'BiNoMaP: Learning Category-Level Bimanual Non-Prehensile Manipulation Primitives'
  ko: ''
summary:
  en: "arXiv:2509.21256v3 Announce Type: replace \nAbstract: Non-prehensile manipulation,\
    \ encompassing ungraspable actions such as pushing, poking, pivoting, and wrapping,\
    \ remains underexplored due to its contact-rich and analytically intractable nature.\
    \ We revisit this problem from two perspectives. First, instead of relying on\
    \ single-arm setups or favorable environmental supports (e.g., walls or edges),\
    \ we advocate a generalizable dual-arm configuration and establish a suite of\
    \ Bimanual Non-prehensile Manipulation Primitives (BiNoMaP). Second, departing\
    \ from prevailing RL-based approaches, we propose a three-stage, RL-free framework\
    \ for learning structured non-prehensile skills. We begin by extracting bimanual\
    \ hand motion trajectories from egocentric video demonstrations. Since these coarse\
    \ trajectories suffer from perceptual noise and morphological discrepancies, we\
    \ introduce a geometry-aware post-optimization algorithm to refine them into executable\
    \ manipulation primitives consistent with predefined motion patterns. To enable\
    \ category-level generalization, the learned primitives are further parameterized\
    \ by object-relevant geometric attributes, primarily size, allowing adaptation\
    \ to unseen instances with significant shape variations. Importantly, BiNoMaP\
    \ supports cross-embodiment transfer: the same primitives can be deployed on two\
    \ real-world dual-arm platforms with distinct kinematic configurations, without\
    \ redesigning skill structures. Extensive real-robot experiments across diverse\
    \ objects and spatial configurations demonstrate the effectiveness, efficiency,\
    \ and strong generalization capability of our approach."
  zh: "arXiv:2509.21256v3 Announce Type: replace \nAbstract: Non-prehensile manipulation,\
    \ encompassing ungraspable actions such as pushing, poking, pivoting, and wrapping,\
    \ remains underexplored due to its contact-rich and analytically intractable nature.\
    \ We revisit this problem from two perspectives. First, instead of relying on\
    \ single-arm setups or favorable environmental supports (e.g., walls or edges),\
    \ we advocate a generalizable dual-arm configuration and establish a suite of\
    \ Bimanual Non-prehensile Manipulation Primitives (BiNoMaP). Second, departing\
    \ from prevailing RL-based approaches, we propose a three-stage, RL-free framework\
    \ for learning structured non-prehensile skills. We begin by extracting bimanual\
    \ hand motion trajectories from egocentric video demonstrations. Since these coarse\
    \ trajectories suffer from perceptual noise and morphological discrepancies, we\
    \ introduce a geometry-aware post-optimization algorithm to refine them into executable\
    \ manipulation primitives consistent with predefined motion patterns. To enable\
    \ category-level generalization, the learned primitives are further parameterized\
    \ by object-relevant geometric attributes, primarily size, allowing adaptation\
    \ to unseen instances with significant shape variations. Importantly, BiNoMaP\
    \ supports cross-embodiment transfer: the same primitives can be deployed on two\
    \ real-world dual-arm platforms with distinct kinematic configurations, without\
    \ redesigning skill structures. Extensive real-robot experiments across diverse\
    \ objects and spatial configurations demonstrate the effectiveness, efficiency,\
    \ and strong generalization capability of our approach."
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
- binomap
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
  title: 'BiNoMaP: Learning Category-Level Bimanual Non-Prehensile Manipulation Primitives
    (arXiv)'
  url: https://arxiv.org/abs/2509.21256
  date: '2026'
  accessed_at: '2026-07-11'
---

arXiv:2509.21256v3 Announce Type: replace 
Abstract: Non-prehensile manipulation, encompassing ungraspable actions such as pushing, poking, pivoting, and wrapping, remains underexplored due to its contact-rich and analytically intractable nature. We revisit this problem from two perspectives. First, instead of relying on single-arm setups or favorable environmental supports (e.g., walls or edges), we advocate a generalizable dual-arm configuration and establish a suite of Bimanual Non-prehensile Manipulation Primitives (BiNoMaP). Second, departing from prevailing RL-based approaches, we propose a three-stage, RL-free framework for learning structured non-prehensile skills. We begin by extracting bimanual hand motion trajectories from egocentric video demonstrations. Since these coarse trajectories suffer from perceptual noise and morphological discrepancies, we introduce a geometry-aware post-optimization algorithm to refine them into executable manipulation primitives consistent with predefined motion patterns. To enable category-level generalization, the learned primitives are further parameterized by object-relevant geometric attributes, primarily size, allowing adaptation to unseen instances with significant shape variations. Importantly, BiNoMaP supports cross-embodiment transfer: the same primitives can be deployed on two real-world dual-arm platforms with distinct kinematic configurations, without redesigning skill structures. Extensive real-robot experiments across diverse objects and spatial configurations demonstrate the effectiveness, efficiency, and strong generalization capability of our approach.
