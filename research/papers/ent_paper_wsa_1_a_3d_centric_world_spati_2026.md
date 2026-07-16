---
$id: ent_paper_wsa_1_a_3d_centric_world_spati_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WSA$_1$: a 3D-Centric World-Spatial-Action Model for Generalizable Robot Control'
  zh: 'WSA$_1$: a 3D-Centric World-Spatial-Action Model for Generalizable Robot Control'
  ko: 'WSA$_1$: a 3D-Centric World-Spatial-Action Model for Generalizable Robot Control'
summary:
  en: 'arXiv:2607.03941v1 Announce Type: new Abstract: Recent advances in embodied AI have established robot foundation models
    (RFMs) as the dominant approach for generalist robotic systems to date. By leveraging imitation learning on extensive
    robot demonstrations, RFMs have achieved impressive capabilities in mapping visual observations and language instructions
    to continuous robotic actions. However, current RFMs lack an inherent ability to reason about physical dynamics and the
    causal effects of robot behaviors on the 3D physical world. This creates a fundamental mismatch between 2D-centric visual
    perception and 3D-centric embodied interaction, severely limiting the generalization ability of RFMs in real-world tasks.To
    address this gap, we present WSA$_1$, a novel RFM built upon proposed 3D-Centric World-Spatial-Action modeling paradigm.
    It not only learns 3D world-aware visual thought for future robot behaviors, but also models mutual constraints between
    3D world state transitions and robotic actions to enhance behavior generalization. Notably, WSA$_1$ achieves highly data-efficient
    pre-training with 6k hours of expert demonstration data (only 1k hours from real robot), while delivering competitive
    manipulation performance (93% success rate) on RoboTwin2.0 simulation benchmark and achieving +20% average boosted performance
    over state-of-the-art RFMs on real-world robot control tasks. These results reveal that generalizable RFM can be attained
    without large-scale real robot data when paired with 3D-centric world-action joint modeling, which offers a practical
    and affordable pathway to generalist robotic systems.'
  zh: 'arXiv:2607.03941v1 Announce Type: new Abstract: Recent advances in embodied AI have established robot foundation models
    (RFMs) as the dominant approach for generalist robotic systems to date. By leveraging imitation learning on extensive
    robot demonstrations, RFMs have achieved impressive capabilities in mapping visual observations and language instructions
    to continuous robotic actions. However, current RFMs lack an inherent ability to reason about physical dynamics and the
    causal effects of robot behaviors on the 3D physical world. This creates a fundamental mismatch between 2D-centric visual
    perception and 3D-centric embodied interaction, severely limiting the generalization ability of RFMs in real-world tasks.To
    address this gap, we present WSA$_1$, a novel RFM built upon proposed 3D-Centric World-Spatial-Action modeling paradigm.
    It not only learns 3D world-aware visual thought for future robot behaviors, but also models mutual constraints between
    3D world state transitions and robotic actions to enhance behavior generalization. Notably, WSA$_1$ achieves highly data-efficient
    pre-training with 6k hours of expert demonstration data (only 1k hours from real robot), while delivering competitive
    manipulation performance (93% success rate) on RoboTwin2.0 simulation benchmark and achieving +20% average boosted performance
    over state-of-the-art RFMs on real-world robot control tasks. These results reveal that generalizable RFM can be attained
    without large-scale real robot data when paired with 3D-centric world-action joint modeling, which offers a practical
    and affordable pathway to generalist robotic systems.'
  ko: 'arXiv:2607.03941v1 Announce Type: new Abstract: Recent advances in embodied AI have established robot foundation models
    (RFMs) as the dominant approach for generalist robotic systems to date. By leveraging imitation learning on extensive
    robot demonstrations, RFMs have achieved impressive capabilities in mapping visual observations and language instructions
    to continuous robotic actions. However, current RFMs lack an inherent ability to reason about physical dynamics and the
    causal effects of robot behaviors on the 3D physical world. This creates a fundamental mismatch between 2D-centric visual
    perception and 3D-centric embodied interaction, severely limiting the generalization ability of RFMs in real-world tasks.To
    address this gap, we present WSA$_1$, a novel RFM built upon proposed 3D-Centric World-Spatial-Action modeling paradigm.
    It not only learns 3D world-aware visual thought for future robot behaviors, but also models mutual constraints between
    3D world state transitions and robotic actions to enhance behavior generalization. Notably, WSA$_1$ achieves highly data-efficient
    pre-training with 6k hours of expert demonstration data (only 1k hours from real robot), while delivering competitive
    manipulation performance (93% success rate) on RoboTwin2.0 simulation benchmark and achieving +20% average boosted performance
    over state-of-the-art RFMs on real-world robot control tasks. These results reveal that generalizable RFM can be attained
    without large-scale real robot data when paired with 3D-centric world-action joint modeling, which offers a practical
    and affordable pathway to generalist robotic systems.'
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
- wsa_1
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03941v1.
sources:
- id: src_001
  type: paper
  title: 'WSA$_1$: a 3D-Centric World-Spatial-Action Model for Generalizable Robot Control (arXiv)'
  url: https://arxiv.org/abs/2607.03941
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Recent advances in embodied AI have established robot foundation models (RFMs) as the dominant approach for generalist robotic systems to date. By leveraging imitation learning on extensive robot demonstrations, RFMs have achieved impressive capabilities in mapping visual observations and language instructions to continuous robotic actions. However, current RFMs lack an inherent ability to reason about physical dynamics and the causal effects of robot behaviors on the 3D physical world. This creates a fundamental mismatch between 2D-centric visual perception and 3D-centric embodied interaction, severely limiting the generalization ability of RFMs in real-world tasks.To address this gap, we present WSA$_1$, a novel RFM built upon proposed 3D-Centric World-Spatial-Action modeling paradigm. It not only learns 3D world-aware visual thought for future robot behaviors, but also models mutual constraints between 3D world state transitions and robotic actions to enhance behavior generalization. Notably, WSA$_1$ achieves highly data-efficient pre-training with 6k hours of expert demonstration data (only 1k hours from real robot), while delivering competitive manipulation performance (93% success rate) on RoboTwin2.0 simulation benchmark and achieving +20% average boosted performance over state-of-the-art RFMs on real-world robot control tasks. These results reveal that generalizable RFM can be attained without large-scale real robot data when paired with 3D-centric world-action joint modeling, which offers a practical and affordable pathway to generalist robotic systems.

## 核心内容
Recent advances in embodied AI have established robot foundation models (RFMs) as the dominant approach for generalist robotic systems to date. By leveraging imitation learning on extensive robot demonstrations, RFMs have achieved impressive capabilities in mapping visual observations and language instructions to continuous robotic actions. However, current RFMs lack an inherent ability to reason about physical dynamics and the causal effects of robot behaviors on the 3D physical world. This creates a fundamental mismatch between 2D-centric visual perception and 3D-centric embodied interaction, severely limiting the generalization ability of RFMs in real-world tasks.To address this gap, we present WSA$_1$, a novel RFM built upon proposed 3D-Centric World-Spatial-Action modeling paradigm. It not only learns 3D world-aware visual thought for future robot behaviors, but also models mutual constraints between 3D world state transitions and robotic actions to enhance behavior generalization. Notably, WSA$_1$ achieves highly data-efficient pre-training with 6k hours of expert demonstration data (only 1k hours from real robot), while delivering competitive manipulation performance (93% success rate) on RoboTwin2.0 simulation benchmark and achieving +20% average boosted performance over state-of-the-art RFMs on real-world robot control tasks. These results reveal that generalizable RFM can be attained without large-scale real robot data when paired with 3D-centric world-action joint modeling, which offers a practical and affordable pathway to generalist robotic systems.

## 参考
- http://arxiv.org/abs/2607.03941v1

