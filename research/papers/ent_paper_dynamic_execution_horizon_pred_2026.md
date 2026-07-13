---
$id: ent_paper_dynamic_execution_horizon_pred_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Dynamic Execution Horizon Prediction for Chunk-based Robot Policies
  zh: Dynamic Execution Horizon Prediction for Chunk-based Robot Policies
  ko: ''
summary:
  en: "arXiv:2606.11408v2 Announce Type: replace \nAbstract: Action chunking has become\
    \ a standard design in modern robot policies, from diffusion/flow policies to\
    \ vision-language-action models, where the policy predicts a sequence of actions\
    \ and executes a fixed number of them instead of acting one step at a time. However,\
    \ this paradigm relies on a key assumption: a fixed execution horizon. During\
    \ chunk execution, the policy operates open-loop, which is particularly problematic\
    \ for fine-grained manipulation tasks that require frequent replanning. In practice,\
    \ the execution horizon is typically chosen through empirical tuning and is highly\
    \ task-dependent. To this end, we propose Dynamic Execution Horizon Prediction\
    \ (DEHP), an effective method that trains a lightweight execution-horizon prediction\
    \ branch using online reinforcement learning while keeping the pretrained chunk\
    \ policy completely frozen. This makes the method compatible with black-box chunk\
    \ policies and isolates the effect of adapting the execution horizon from changes\
    \ to the underlying action generator. Across our evaluations, DEHP improves the\
    \ success rate of different high-precision and long-horizon manipulation tasks\
    \ by a large margin. Our qualitative analysis further shows that DEHP predicts\
    \ shorter execution horizons during fine-grained stages of the task and longer\
    \ horizons during free-space motion. In this way, DEHP balances the efficiency\
    \ of open-loop chunk execution with the reactivity of closed-loop single-step\
    \ control. Project page: https://dehp-chunking.github.io/"
  zh: "arXiv:2606.11408v2 Announce Type: replace \nAbstract: Action chunking has become\
    \ a standard design in modern robot policies, from diffusion/flow policies to\
    \ vision-language-action models, where the policy predicts a sequence of actions\
    \ and executes a fixed number of them instead of acting one step at a time. However,\
    \ this paradigm relies on a key assumption: a fixed execution horizon. During\
    \ chunk execution, the policy operates open-loop, which is particularly problematic\
    \ for fine-grained manipulation tasks that require frequent replanning. In practice,\
    \ the execution horizon is typically chosen through empirical tuning and is highly\
    \ task-dependent. To this end, we propose Dynamic Execution Horizon Prediction\
    \ (DEHP), an effective method that trains a lightweight execution-horizon prediction\
    \ branch using online reinforcement learning while keeping the pretrained chunk\
    \ policy completely frozen. This makes the method compatible with black-box chunk\
    \ policies and isolates the effect of adapting the execution horizon from changes\
    \ to the underlying action generator. Across our evaluations, DEHP improves the\
    \ success rate of different high-precision and long-horizon manipulation tasks\
    \ by a large margin. Our qualitative analysis further shows that DEHP predicts\
    \ shorter execution horizons during fine-grained stages of the task and longer\
    \ horizons during free-space motion. In this way, DEHP balances the efficiency\
    \ of open-loop chunk execution with the reactivity of closed-loop single-step\
    \ control. Project page: https://dehp-chunking.github.io/"
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
- dynamic_execution_horizon_pred
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
  title: Dynamic Execution Horizon Prediction for Chunk-based Robot Policies (arXiv)
  url: https://arxiv.org/abs/2606.11408
  date: '2026'
  accessed_at: '2026-07-11'
---

arXiv:2606.11408v2 Announce Type: replace 
Abstract: Action chunking has become a standard design in modern robot policies, from diffusion/flow policies to vision-language-action models, where the policy predicts a sequence of actions and executes a fixed number of them instead of acting one step at a time. However, this paradigm relies on a key assumption: a fixed execution horizon. During chunk execution, the policy operates open-loop, which is particularly problematic for fine-grained manipulation tasks that require frequent replanning. In practice, the execution horizon is typically chosen through empirical tuning and is highly task-dependent. To this end, we propose Dynamic Execution Horizon Prediction (DEHP), an effective method that trains a lightweight execution-horizon prediction branch using online reinforcement learning while keeping the pretrained chunk policy completely frozen. This makes the method compatible with black-box chunk policies and isolates the effect of adapting the execution horizon from changes to the underlying action generator. Across our evaluations, DEHP improves the success rate of different high-precision and long-horizon manipulation tasks by a large margin. Our qualitative analysis further shows that DEHP predicts shorter execution horizons during fine-grained stages of the task and longer horizons during free-space motion. In this way, DEHP balances the efficiency of open-loop chunk execution with the reactivity of closed-loop single-step control. Project page: https://dehp-chunking.github.io/
