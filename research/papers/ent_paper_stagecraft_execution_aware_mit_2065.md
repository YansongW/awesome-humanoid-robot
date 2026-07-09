---
$id: ent_paper_stagecraft_execution_aware_mit_2065
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'StageCraft: Execution Aware Mitigation of Distractor and Obstruction Failures
    in VLA Models'
  zh: 'StageCraft: Execution Aware Mitigation of Distractor and Obstruction Failures
    in VLA Models'
  ko: ''
summary:
  en: "arXiv:2603.20659v2 Announce Type: replace \nAbstract: Large scale pre-training\
    \ on text and image data along with diverse robot demonstrations has helped Vision\
    \ Language Action models (VLAs) to generalize to novel tasks, objects and scenes.\
    \ However, these models are still susceptible to failure in the presence of execution-time\
    \ impediments such as distractors and physical obstructions in the robot's workspace.\
    \ Existing policy improvement methods finetune base VLAs to improve generalization,\
    \ yet they still struggle in unseen distractor settings. To address this problem,\
    \ we investigate whether internet-scale pretraining of large vision-language models\
    \ (VLMs) can be leveraged to reason about these impediments and mitigate policy\
    \ failures. To this end, we propose StageCraft, a training-free approach to improve\
    \ pretrained VLA policy performance by manipulating the environment's initial\
    \ state using VLM-based in-context reasoning. StageCraft takes policy rollout\
    \ videos and success labels as input and leverages VLM's reasoning ability to\
    \ infer which objects in the initial state need to be manipulated to avoid anticipated\
    \ execution failures. StageCraft is an extensible plug-and-play module that does\
    \ not introduce additional constraints on the underlying policy, and only requires\
    \ a few policy rollouts to work. We evaluate performance of state-of-the-art VLA\
    \ models with StageCraft and show an absolute 40% performance improvement across\
    \ three real world task domains involving diverse distractors and obstructions.\
    \ Our simulation experiments in RLBench empirically show that StageCraft tailors\
    \ its extent of intervention based on the strength of the underlying policy and\
    \ improves its performance with more in-context samples. Videos of StageCraft\
    \ in effect can be found at https://stagecraft-decorator.github.io/stagecraft/\
    \ ."
  zh: "arXiv:2603.20659v2 Announce Type: replace \nAbstract: Large scale pre-training\
    \ on text and image data along with diverse robot demonstrations has helped Vision\
    \ Language Action models (VLAs) to generalize to novel tasks, objects and scenes.\
    \ However, these models are still susceptible to failure in the presence of execution-time\
    \ impediments such as distractors and physical obstructions in the robot's workspace.\
    \ Existing policy improvement methods finetune base VLAs to improve generalization,\
    \ yet they still struggle in unseen distractor settings. To address this problem,\
    \ we investigate whether internet-scale pretraining of large vision-language models\
    \ (VLMs) can be leveraged to reason about these impediments and mitigate policy\
    \ failures. To this end, we propose StageCraft, a training-free approach to improve\
    \ pretrained VLA policy performance by manipulating the environment's initial\
    \ state using VLM-based in-context reasoning. StageCraft takes policy rollout\
    \ videos and success labels as input and leverages VLM's reasoning ability to\
    \ infer which objects in the initial state need to be manipulated to avoid anticipated\
    \ execution failures. StageCraft is an extensible plug-and-play module that does\
    \ not introduce additional constraints on the underlying policy, and only requires\
    \ a few policy rollouts to work. We evaluate performance of state-of-the-art VLA\
    \ models with StageCraft and show an absolute 40% performance improvement across\
    \ three real world task domains involving diverse distractors and obstructions.\
    \ Our simulation experiments in RLBench empirically show that StageCraft tailors\
    \ its extent of intervention based on the strength of the underlying policy and\
    \ improves its performance with more in-context samples. Videos of StageCraft\
    \ in effect can be found at https://stagecraft-decorator.github.io/stagecraft/\
    \ ."
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
- stagecraft
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
  title: 'StageCraft: Execution Aware Mitigation of Distractor and Obstruction Failures
    in VLA Models (arXiv)'
  url: https://arxiv.org/abs/2603.20659
  date: '2065'
  accessed_at: '2026-07-08'
---

arXiv:2603.20659v2 Announce Type: replace 
Abstract: Large scale pre-training on text and image data along with diverse robot demonstrations has helped Vision Language Action models (VLAs) to generalize to novel tasks, objects and scenes. However, these models are still susceptible to failure in the presence of execution-time impediments such as distractors and physical obstructions in the robot's workspace. Existing policy improvement methods finetune base VLAs to improve generalization, yet they still struggle in unseen distractor settings. To address this problem, we investigate whether internet-scale pretraining of large vision-language models (VLMs) can be leveraged to reason about these impediments and mitigate policy failures. To this end, we propose StageCraft, a training-free approach to improve pretrained VLA policy performance by manipulating the environment's initial state using VLM-based in-context reasoning. StageCraft takes policy rollout videos and success labels as input and leverages VLM's reasoning ability to infer which objects in the initial state need to be manipulated to avoid anticipated execution failures. StageCraft is an extensible plug-and-play module that does not introduce additional constraints on the underlying policy, and only requires a few policy rollouts to work. We evaluate performance of state-of-the-art VLA models with StageCraft and show an absolute 40% performance improvement across three real world task domains involving diverse distractors and obstructions. Our simulation experiments in RLBench empirically show that StageCraft tailors its extent of intervention based on the strength of the underlying policy and improves its performance with more in-context samples. Videos of StageCraft in effect can be found at https://stagecraft-decorator.github.io/stagecraft/ .
