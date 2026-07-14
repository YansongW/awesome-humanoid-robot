---
$id: ent_paper_learning_locomotion_on_discret_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Locomotion on Discrete Terrain via Minimal Proximity Sensing
  zh: Learning Locomotion on Discrete Terrain via Minimal Proximity Sensing
  ko: Learning Locomotion on Discrete Terrain via Minimal Proximity Sensing
summary:
  en: "arXiv:2606.31912v1 Announce Type: new \nAbstract: Learning-based control has revolutionized dynamic locomotion, yet\
    \ navigating unstructured terrain remains limited by a robot's incomplete awareness of imminent ground contact. While\
    \ global perception systems such as LiDARs and depth cameras provide environmental context, they are frequently plagued\
    \ by latencies, occlusions, and the high computational cost of dense geometric reconstruction. On the other hand, proprioceptive\
    \ feedback is purely reactive, initiating corrections only after impact has occurred. This work explores embedding a minimal\
    \ suite of low-cost, high-frequency infrared proximity sensors directly into the feet of a quadrupedal robot. These sensors\
    \ provide \"pre-contact\" feedback that is robust to self-occlusions and significantly less computationally demanding\
    \ than conventional vision-based pipelines. By integrating these localized signals into a reinforcement learning framework,\
    \ we enable the robot to anticipate terrain discontinuities such as gaps and stepping stones that are problematic for\
    \ traditional perception stacks due to occlusions or state estimation drift. We demonstrate that such sparse, near-field\
    \ sensing can be reliably modeled in simulation and transferred to the real world with high fidelity. Experimental results\
    \ show that local proximity sensing substantially improves traversal robustness over discrete terrain and offers a low-power,\
    \ low-latency alternative or complement to complex global perception suites in unpredictable environments. For more information\
    \ about results and methods, please see the project website: https://sites.google.com/view/foot-tof/home."
  zh: "arXiv:2606.31912v1 Announce Type: new \nAbstract: Learning-based control has revolutionized dynamic locomotion, yet\
    \ navigating unstructured terrain remains limited by a robot's incomplete awareness of imminent ground contact. While\
    \ global perception systems such as LiDARs and depth cameras provide environmental context, they are frequently plagued\
    \ by latencies, occlusions, and the high computational cost of dense geometric reconstruction. On the other hand, proprioceptive\
    \ feedback is purely reactive, initiating corrections only after impact has occurred. This work explores embedding a minimal\
    \ suite of low-cost, high-frequency infrared proximity sensors directly into the feet of a quadrupedal robot. These sensors\
    \ provide \"pre-contact\" feedback that is robust to self-occlusions and significantly less computationally demanding\
    \ than conventional vision-based pipelines. By integrating these localized signals into a reinforcement learning framework,\
    \ we enable the robot to anticipate terrain discontinuities such as gaps and stepping stones that are problematic for\
    \ traditional perception stacks due to occlusions or state estimation drift. We demonstrate that such sparse, near-field\
    \ sensing can be reliably modeled in simulation and transferred to the real world with high fidelity. Experimental results\
    \ show that local proximity sensing substantially improves traversal robustness over discrete terrain and offers a low-power,\
    \ low-latency alternative or complement to complex global perception suites in unpredictable environments. For more information\
    \ about results and methods, please see the project website: https://sites.google.com/view/foot-tof/home."
  ko: "arXiv:2606.31912v1 Announce Type: new \nAbstract: Learning-based control has revolutionized dynamic locomotion, yet\
    \ navigating unstructured terrain remains limited by a robot's incomplete awareness of imminent ground contact. While\
    \ global perception systems such as LiDARs and depth cameras provide environmental context, they are frequently plagued\
    \ by latencies, occlusions, and the high computational cost of dense geometric reconstruction. On the other hand, proprioceptive\
    \ feedback is purely reactive, initiating corrections only after impact has occurred. This work explores embedding a minimal\
    \ suite of low-cost, high-frequency infrared proximity sensors directly into the feet of a quadrupedal robot. These sensors\
    \ provide \"pre-contact\" feedback that is robust to self-occlusions and significantly less computationally demanding\
    \ than conventional vision-based pipelines. By integrating these localized signals into a reinforcement learning framework,\
    \ we enable the robot to anticipate terrain discontinuities such as gaps and stepping stones that are problematic for\
    \ traditional perception stacks due to occlusions or state estimation drift. We demonstrate that such sparse, near-field\
    \ sensing can be reliably modeled in simulation and transferred to the real world with high fidelity. Experimental results\
    \ show that local proximity sensing substantially improves traversal robustness over discrete terrain and offers a low-power,\
    \ low-latency alternative or complement to complex global perception suites in unpredictable environments. For more information\
    \ about results and methods, please see the project website: https://sites.google.com/view/foot-tof/home."
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
- learning_locomotion_on_discret
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31912v2.
sources:
- id: src_001
  type: paper
  title: Learning Locomotion on Discrete Terrain via Minimal Proximity Sensing
  url: https://arxiv.org/abs/2606.31912
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Learning-based control has revolutionized dynamic locomotion, yet navigating unstructured terrain remains limited by a robot's incomplete awareness of imminent ground contact. While global perception systems such as LiDARs and depth cameras provide environmental context, they are frequently plagued by latencies, occlusions, and the high computational cost of dense geometric reconstruction. On the other hand, proprioceptive feedback is purely reactive, initiating corrections only after impact has occurred. This work explores embedding a minimal suite of low-cost, high-frequency infrared proximity sensors directly into the feet of a quadrupedal robot. These sensors provide "pre-contact" feedback that is robust to self-occlusions and significantly less computationally demanding than conventional vision-based pipelines. By integrating these localized signals into a reinforcement learning framework, we enable the robot to anticipate terrain discontinuities such as gaps and stepping stones that are problematic for traditional perception stacks due to occlusions or state estimation drift. We demonstrate that such sparse, near-field sensing can be reliably modeled in simulation and transferred to the real world with high fidelity. Experimental results show that local proximity sensing substantially improves traversal robustness over discrete terrain and offers a low-power, low-latency alternative or complement to complex global perception suites in unpredictable environments. For more information about results and methods, please see the project website: https://sites.google.com/view/foot-tof/home.

## 核心内容
Learning-based control has revolutionized dynamic locomotion, yet navigating unstructured terrain remains limited by a robot's incomplete awareness of imminent ground contact. While global perception systems such as LiDARs and depth cameras provide environmental context, they are frequently plagued by latencies, occlusions, and the high computational cost of dense geometric reconstruction. On the other hand, proprioceptive feedback is purely reactive, initiating corrections only after impact has occurred. This work explores embedding a minimal suite of low-cost, high-frequency infrared proximity sensors directly into the feet of a quadrupedal robot. These sensors provide "pre-contact" feedback that is robust to self-occlusions and significantly less computationally demanding than conventional vision-based pipelines. By integrating these localized signals into a reinforcement learning framework, we enable the robot to anticipate terrain discontinuities such as gaps and stepping stones that are problematic for traditional perception stacks due to occlusions or state estimation drift. We demonstrate that such sparse, near-field sensing can be reliably modeled in simulation and transferred to the real world with high fidelity. Experimental results show that local proximity sensing substantially improves traversal robustness over discrete terrain and offers a low-power, low-latency alternative or complement to complex global perception suites in unpredictable environments. For more information about results and methods, please see the project website: https://sites.google.com/view/foot-tof/home.

## 参考
- http://arxiv.org/abs/2606.31912v2

