---
$id: ent_paper_imperio_smolvla_the_implicatio_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: '!Imperio, smolVLA: The Implications of Data Poisoning on Open Source Robotics'
  zh: '!Imperio, smolVLA: The Implications of Data Poisoning on Open Source Robotics'
  ko: ''
summary:
  en: "arXiv:2607.04146v1 Announce Type: new \nAbstract: This work establishes that\
    \ trigger-word data poisoning of vision language action models is practical, while\
    \ at the same time the open-source robotics ecosystem holds trust assumptions\
    \ about community contributions. A few poisoned samples can silently embed a backdoor\
    \ that disables a robot on command. We evaluate this threat against smolVLA on\
    \ a real-world pick-and-place task, training on three poison ratios and evaluating\
    \ across different prompts on the LeRobot platform. Three poisoned episodes in\
    \ 320 clean episodes suffice for a complete denial of service. Success rate drops\
    \ to 0.0 plus minus 0.0% across all trigger-word conditions and the robot locks\
    \ into a fixed joint configuration rather than executing any task-relevant motion.\
    \ Clean-prompt behaviour holds at approx. 50% success rate across all poison ratios,\
    \ confirming the attack is stealthy under normal operation. A single poisoned\
    \ episode already reduces success rate to 6.7 plus minus 6.7%. The robot still\
    \ moves, but no longer completes the task. The attack generalises to front, middle,\
    \ and end trigger placements despite training exclusively on front-placed triggers.\
    \ These findings establish that the threat is practical, low-cost, and stealthy,\
    \ and warrant treating dataset provenance as a first-class concern in open-source\
    \ robotics ecosystems."
  zh: "arXiv:2607.04146v1 Announce Type: new \nAbstract: This work establishes that\
    \ trigger-word data poisoning of vision language action models is practical, while\
    \ at the same time the open-source robotics ecosystem holds trust assumptions\
    \ about community contributions. A few poisoned samples can silently embed a backdoor\
    \ that disables a robot on command. We evaluate this threat against smolVLA on\
    \ a real-world pick-and-place task, training on three poison ratios and evaluating\
    \ across different prompts on the LeRobot platform. Three poisoned episodes in\
    \ 320 clean episodes suffice for a complete denial of service. Success rate drops\
    \ to 0.0 plus minus 0.0% across all trigger-word conditions and the robot locks\
    \ into a fixed joint configuration rather than executing any task-relevant motion.\
    \ Clean-prompt behaviour holds at approx. 50% success rate across all poison ratios,\
    \ confirming the attack is stealthy under normal operation. A single poisoned\
    \ episode already reduces success rate to 6.7 plus minus 6.7%. The robot still\
    \ moves, but no longer completes the task. The attack generalises to front, middle,\
    \ and end trigger placements despite training exclusively on front-placed triggers.\
    \ These findings establish that the threat is practical, low-cost, and stealthy,\
    \ and warrant treating dataset provenance as a first-class concern in open-source\
    \ robotics ecosystems."
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
- imperio_smolvla
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
  title: '!Imperio, smolVLA: The Implications of Data Poisoning on Open Source Robotics
    (arXiv)'
  url: https://arxiv.org/abs/2607.04146
  date: '2026'
  accessed_at: '2026-07-08'
---

arXiv:2607.04146v1 Announce Type: new 
Abstract: This work establishes that trigger-word data poisoning of vision language action models is practical, while at the same time the open-source robotics ecosystem holds trust assumptions about community contributions. A few poisoned samples can silently embed a backdoor that disables a robot on command. We evaluate this threat against smolVLA on a real-world pick-and-place task, training on three poison ratios and evaluating across different prompts on the LeRobot platform. Three poisoned episodes in 320 clean episodes suffice for a complete denial of service. Success rate drops to 0.0 plus minus 0.0% across all trigger-word conditions and the robot locks into a fixed joint configuration rather than executing any task-relevant motion. Clean-prompt behaviour holds at approx. 50% success rate across all poison ratios, confirming the attack is stealthy under normal operation. A single poisoned episode already reduces success rate to 6.7 plus minus 6.7%. The robot still moves, but no longer completes the task. The attack generalises to front, middle, and end trigger placements despite training exclusively on front-placed triggers. These findings establish that the threat is practical, low-cost, and stealthy, and warrant treating dataset provenance as a first-class concern in open-source robotics ecosystems.
