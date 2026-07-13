---
$id: ent_paper_v_vlaps_value_guided_planning_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'V-VLAPS: Value-Guided Planning for Vision-Language-Action Models'
  zh: 'V-VLAPS: Value-Guided Planning for Vision-Language-Action Models'
  ko: ''
summary:
  en: "arXiv:2601.00969v3 Announce Type: replace \nAbstract: Vision-language-action\
    \ (VLA) models provide strong action priors for robotic manipulation, but their\
    \ reactive behavior can fail under distribution shift and long-horizon task structure.\
    \ Recent VLA-guided planning methods improve execution by using pretrained policies\
    \ to guide tree search, yet node selection still depends heavily on policy priors\
    \ and visit-count exploration. Consequently, when the policy favors poor actions,\
    \ the planner lacks a learned value signal to correct this bias. Prior work has\
    \ shown that VLA representations encode rollout success and failure information,\
    \ suggesting that they may also support value estimation during planning. We introduce\
    \ Value-Guided Vision-Language-Action Planning and Search (V-VLAPS), which augments\
    \ VLA-guided planning with a lightweight value head trained on offline VLA rollouts\
    \ to predict Monte Carlo returns. These predictions guide Monte Carlo Tree Search\
    \ in simulation toward higher-value branches. Across five LIBERO suites, V-VLAPS\
    \ matches value-free planning baseline at the default search budget in aggregate,\
    \ and analysis shows that many hard failures are root-level timeouts where predicted\
    \ values are weakly separated. With a larger search budget, V-VLAPS improves over\
    \ the baseline in all task suites with +6 percentage points on LIBERO-Object and\
    \ +4 percentage points on LIBERO-10. Our results suggest that VLA representations\
    \ can support not only failure prediction, but also value-guided planning when\
    \ search reaches branches where value-based ranking matters."
  zh: "arXiv:2601.00969v3 Announce Type: replace \nAbstract: Vision-language-action\
    \ (VLA) models provide strong action priors for robotic manipulation, but their\
    \ reactive behavior can fail under distribution shift and long-horizon task structure.\
    \ Recent VLA-guided planning methods improve execution by using pretrained policies\
    \ to guide tree search, yet node selection still depends heavily on policy priors\
    \ and visit-count exploration. Consequently, when the policy favors poor actions,\
    \ the planner lacks a learned value signal to correct this bias. Prior work has\
    \ shown that VLA representations encode rollout success and failure information,\
    \ suggesting that they may also support value estimation during planning. We introduce\
    \ Value-Guided Vision-Language-Action Planning and Search (V-VLAPS), which augments\
    \ VLA-guided planning with a lightweight value head trained on offline VLA rollouts\
    \ to predict Monte Carlo returns. These predictions guide Monte Carlo Tree Search\
    \ in simulation toward higher-value branches. Across five LIBERO suites, V-VLAPS\
    \ matches value-free planning baseline at the default search budget in aggregate,\
    \ and analysis shows that many hard failures are root-level timeouts where predicted\
    \ values are weakly separated. With a larger search budget, V-VLAPS improves over\
    \ the baseline in all task suites with +6 percentage points on LIBERO-Object and\
    \ +4 percentage points on LIBERO-10. Our results suggest that VLA representations\
    \ can support not only failure prediction, but also value-guided planning when\
    \ search reaches branches where value-based ranking matters."
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
- v_vlaps
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
  title: 'V-VLAPS: Value-Guided Planning for Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2601.00969
  date: '2026'
  accessed_at: '2026-07-11'
---

arXiv:2601.00969v3 Announce Type: replace 
Abstract: Vision-language-action (VLA) models provide strong action priors for robotic manipulation, but their reactive behavior can fail under distribution shift and long-horizon task structure. Recent VLA-guided planning methods improve execution by using pretrained policies to guide tree search, yet node selection still depends heavily on policy priors and visit-count exploration. Consequently, when the policy favors poor actions, the planner lacks a learned value signal to correct this bias. Prior work has shown that VLA representations encode rollout success and failure information, suggesting that they may also support value estimation during planning. We introduce Value-Guided Vision-Language-Action Planning and Search (V-VLAPS), which augments VLA-guided planning with a lightweight value head trained on offline VLA rollouts to predict Monte Carlo returns. These predictions guide Monte Carlo Tree Search in simulation toward higher-value branches. Across five LIBERO suites, V-VLAPS matches value-free planning baseline at the default search budget in aggregate, and analysis shows that many hard failures are root-level timeouts where predicted values are weakly separated. With a larger search budget, V-VLAPS improves over the baseline in all task suites with +6 percentage points on LIBERO-Object and +4 percentage points on LIBERO-10. Our results suggest that VLA representations can support not only failure prediction, but also value-guided planning when search reaches branches where value-based ranking matters.
