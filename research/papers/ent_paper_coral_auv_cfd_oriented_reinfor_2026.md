---
$id: ent_paper_coral_auv_cfd_oriented_reinfor_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CORAL-AUV: CFD Oriented Reinforcement Learning for Autonomous Underwater Vehicles'
  zh: 'CORAL-AUV: CFD Oriented Reinforcement Learning for Autonomous Underwater Vehicles'
  ko: 'CORAL-AUV: CFD Oriented Reinforcement Learning for Autonomous Underwater Vehicles'
summary:
  en: "arXiv:2607.09557v1 Announce Type: new \nAbstract: Fine grain control and positioning of autonomous underwater vehicles\
    \ (AUVs) is critical for sampling, maintenance, and survey applications. Traditional control methods for AUVs are labor\
    \ intensive and are not robust to changes in the vehicle configuration or environmental conditions. Reinforcement learning\
    \ (RL) promises rapid controller development while handling a range of deployment parameters via domain randomization\
    \ (DR). However, DR is still limited by the capacity of the underlying simulation to model real physics. In particular,\
    \ drag physics are difficult to model and are a large contributor to sim-to-real gaps. Meanwhile, computational fluid\
    \ dynamics (CFD) provides high fidelity drag models but is challenging to leverage within reinforcement learning frameworks\
    \ due to its computational overhead. Thus, in this paper we exploit the idea of training surrogate approximations of CFD\
    \ models of a given vehicle, enabling fast inference within RL pipelines. We are the first to successfully deploy a zero-shot\
    \ RL policy on a 6-DOF AUV in which policy training is performed on surrogate drag models (SDMs) trained on CFD data.\
    \ We find 31% lower energy usage compared to a controller using simplified physics while traversing between waypoints\
    \ 11% faster with 19% less error. Our SDM based RL controller better predicts zero-shot transfer and is more robust across\
    \ reward shaping design choices. When using DR to complete a task with perturbed parameters, we find that the CFD policy\
    \ is the only controller that successfully transfers. The policies are evaluated in a controlled tank environment and\
    \ in the field providing extensive testing of the policies' capabilities."
  zh: "arXiv:2607.09557v1 Announce Type: new \nAbstract: Fine grain control and positioning of autonomous underwater vehicles\
    \ (AUVs) is critical for sampling, maintenance, and survey applications. Traditional control methods for AUVs are labor\
    \ intensive and are not robust to changes in the vehicle configuration or environmental conditions. Reinforcement learning\
    \ (RL) promises rapid controller development while handling a range of deployment parameters via domain randomization\
    \ (DR). However, DR is still limited by the capacity of the underlying simulation to model real physics. In particular,\
    \ drag physics are difficult to model and are a large contributor to sim-to-real gaps. Meanwhile, computational fluid\
    \ dynamics (CFD) provides high fidelity drag models but is challenging to leverage within reinforcement learning frameworks\
    \ due to its computational overhead. Thus, in this paper we exploit the idea of training surrogate approximations of CFD\
    \ models of a given vehicle, enabling fast inference within RL pipelines. We are the first to successfully deploy a zero-shot\
    \ RL policy on a 6-DOF AUV in which policy training is performed on surrogate drag models (SDMs) trained on CFD data.\
    \ We find 31% lower energy usage compared to a controller using simplified physics while traversing between waypoints\
    \ 11% faster with 19% less error. Our SDM based RL controller better predicts zero-shot transfer and is more robust across\
    \ reward shaping design choices. When using DR to complete a task with perturbed parameters, we find that the CFD policy\
    \ is the only controller that successfully transfers. The policies are evaluated in a controlled tank environment and\
    \ in the field providing extensive testing of the policies' capabilities."
  ko: "arXiv:2607.09557v1 Announce Type: new \nAbstract: Fine grain control and positioning of autonomous underwater vehicles\
    \ (AUVs) is critical for sampling, maintenance, and survey applications. Traditional control methods for AUVs are labor\
    \ intensive and are not robust to changes in the vehicle configuration or environmental conditions. Reinforcement learning\
    \ (RL) promises rapid controller development while handling a range of deployment parameters via domain randomization\
    \ (DR). However, DR is still limited by the capacity of the underlying simulation to model real physics. In particular,\
    \ drag physics are difficult to model and are a large contributor to sim-to-real gaps. Meanwhile, computational fluid\
    \ dynamics (CFD) provides high fidelity drag models but is challenging to leverage within reinforcement learning frameworks\
    \ due to its computational overhead. Thus, in this paper we exploit the idea of training surrogate approximations of CFD\
    \ models of a given vehicle, enabling fast inference within RL pipelines. We are the first to successfully deploy a zero-shot\
    \ RL policy on a 6-DOF AUV in which policy training is performed on surrogate drag models (SDMs) trained on CFD data.\
    \ We find 31% lower energy usage compared to a controller using simplified physics while traversing between waypoints\
    \ 11% faster with 19% less error. Our SDM based RL controller better predicts zero-shot transfer and is more robust across\
    \ reward shaping design choices. When using DR to complete a task with perturbed parameters, we find that the CFD policy\
    \ is the only controller that successfully transfers. The policies are evaluated in a controlled tank environment and\
    \ in the field providing extensive testing of the policies' capabilities."
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
- coral_auv
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.09557v1.
sources:
- id: src_001
  type: paper
  title: 'CORAL-AUV: CFD Oriented Reinforcement Learning for Autonomous Underwater Vehicles (arXiv)'
  url: https://arxiv.org/abs/2607.09557
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
Fine grain control and positioning of autonomous underwater vehicles (AUVs) is critical for sampling, maintenance, and survey applications. Traditional control methods for AUVs are labor intensive and are not robust to changes in the vehicle configuration or environmental conditions. Reinforcement learning (RL) promises rapid controller development while handling a range of deployment parameters via domain randomization (DR). However, DR is still limited by the capacity of the underlying simulation to model real physics. In particular, drag physics are difficult to model and are a large contributor to sim-to-real gaps. Meanwhile, computational fluid dynamics (CFD) provides high fidelity drag models but is challenging to leverage within reinforcement learning frameworks due to its computational overhead. Thus, in this paper we exploit the idea of training surrogate approximations of CFD models of a given vehicle, enabling fast inference within RL pipelines. We are the first to successfully deploy a zero-shot RL policy on a 6-DOF AUV in which policy training is performed on surrogate drag models (SDMs) trained on CFD data. We find 31% lower energy usage compared to a controller using simplified physics while traversing between waypoints 11% faster with 19% less error. Our SDM based RL controller better predicts zero-shot transfer and is more robust across reward shaping design choices. When using DR to complete a task with perturbed parameters, we find that the CFD policy is the only controller that successfully transfers. The policies are evaluated in a controlled tank environment and in the field providing extensive testing of the policies' capabilities.

## 核心内容
Fine grain control and positioning of autonomous underwater vehicles (AUVs) is critical for sampling, maintenance, and survey applications. Traditional control methods for AUVs are labor intensive and are not robust to changes in the vehicle configuration or environmental conditions. Reinforcement learning (RL) promises rapid controller development while handling a range of deployment parameters via domain randomization (DR). However, DR is still limited by the capacity of the underlying simulation to model real physics. In particular, drag physics are difficult to model and are a large contributor to sim-to-real gaps. Meanwhile, computational fluid dynamics (CFD) provides high fidelity drag models but is challenging to leverage within reinforcement learning frameworks due to its computational overhead. Thus, in this paper we exploit the idea of training surrogate approximations of CFD models of a given vehicle, enabling fast inference within RL pipelines. We are the first to successfully deploy a zero-shot RL policy on a 6-DOF AUV in which policy training is performed on surrogate drag models (SDMs) trained on CFD data. We find 31% lower energy usage compared to a controller using simplified physics while traversing between waypoints 11% faster with 19% less error. Our SDM based RL controller better predicts zero-shot transfer and is more robust across reward shaping design choices. When using DR to complete a task with perturbed parameters, we find that the CFD policy is the only controller that successfully transfers. The policies are evaluated in a controlled tank environment and in the field providing extensive testing of the policies' capabilities.

## 参考
- http://arxiv.org/abs/2607.09557v1

