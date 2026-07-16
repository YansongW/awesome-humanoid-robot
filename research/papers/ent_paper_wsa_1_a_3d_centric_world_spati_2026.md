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

## Overview
Recent advances in embodied AI have established robot foundation models (RFMs) as the dominant approach for generalist robotic systems to date. By leveraging imitation learning on extensive robot demonstrations, RFMs have achieved impressive capabilities in mapping visual observations and language instructions to continuous robotic actions. However, current RFMs lack an inherent ability to reason about physical dynamics and the causal effects of robot behaviors on the 3D physical world. This creates a fundamental mismatch between 2D-centric visual perception and 3D-centric embodied interaction, severely limiting the generalization ability of RFMs in real-world tasks. To address this gap, we present WSA$_1$, a novel RFM built upon proposed 3D-Centric World-Spatial-Action modeling paradigm. It not only learns 3D world-aware visual thought for future robot behaviors, but also models mutual constraints between 3D world state transitions and robotic actions to enhance behavior generalization. Notably, WSA$_1$ achieves highly data-efficient pre-training with 6k hours of expert demonstration data (only 1k hours from real robot), while delivering competitive manipulation performance (93% success rate) on RoboTwin2.0 simulation benchmark and achieving +20% average boosted performance over state-of-the-art RFMs on real-world robot control tasks. These results reveal that generalizable RFM can be attained without large-scale real robot data when paired with 3D-centric world-action joint modeling, which offers a practical and affordable pathway to generalist robotic systems.

## Content
Recent advances in embodied AI have established robot foundation models (RFMs) as the dominant approach for generalist robotic systems to date. By leveraging imitation learning on extensive robot demonstrations, RFMs have achieved impressive capabilities in mapping visual observations and language instructions to continuous robotic actions. However, current RFMs lack an inherent ability to reason about physical dynamics and the causal effects of robot behaviors on the 3D physical world. This creates a fundamental mismatch between 2D-centric visual perception and 3D-centric embodied interaction, severely limiting the generalization ability of RFMs in real-world tasks. To address this gap, we present WSA$_1$, a novel RFM built upon proposed 3D-Centric World-Spatial-Action modeling paradigm. It not only learns 3D world-aware visual thought for future robot behaviors, but also models mutual constraints between 3D world state transitions and robotic actions to enhance behavior generalization. Notably, WSA$_1$ achieves highly data-efficient pre-training with 6k hours of expert demonstration data (only 1k hours from real robot), while delivering competitive manipulation performance (93% success rate) on RoboTwin2.0 simulation benchmark and achieving +20% average boosted performance over state-of-the-art RFMs on real-world robot control tasks. These results reveal that generalizable RFM can be attained without large-scale real robot data when paired with 3D-centric world-action joint modeling, which offers a practical and affordable pathway to generalist robotic systems.

## 개요
최근 체화된 AI의 발전으로 로봇 기반 모델(RFM)이 현재까지 범용 로봇 시스템의 지배적인 접근 방식으로 자리 잡았습니다. 방대한 로봇 시연 데이터에 대한 모방 학습을 활용함으로써, RFM은 시각적 관찰과 언어 명령을 연속적인 로봇 동작으로 매핑하는 데 인상적인 능력을 달성했습니다. 그러나 현재의 RFM은 물리적 역학과 로봇 행동이 3D 물리 세계에 미치는 인과적 효과에 대한 본질적인 추론 능력이 부족합니다. 이는 2D 중심의 시각적 인식과 3D 중심의 체화된 상호작용 사이에 근본적인 불일치를 초래하며, 실제 작업에서 RFM의 일반화 능력을 심각하게 제한합니다. 이러한 격차를 해결하기 위해, 우리는 제안된 3D 중심 세계-공간-행동 모델링 패러다임을 기반으로 구축된 새로운 RFM인 WSA$_1$을 제시합니다. 이는 미래 로봇 행동을 위한 3D 세계 인식 시각적 사고를 학습할 뿐만 아니라, 3D 세계 상태 전이와 로봇 동작 간의 상호 제약을 모델링하여 행동 일반화를 향상시킵니다. 특히, WSA$_1$은 6,000시간의 전문가 시연 데이터(실제 로봇 데이터는 1,000시간에 불과)로 매우 데이터 효율적인 사전 학습을 달성하면서, RoboTwin2.0 시뮬레이션 벤치마크에서 경쟁력 있는 조작 성능(93% 성공률)을 제공하고, 실제 로봇 제어 작업에서 최첨단 RFM 대비 평균 +20% 향상된 성능을 달성합니다. 이러한 결과는 3D 중심의 세계-행동 공동 모델링과 결합될 때 대규모 실제 로봇 데이터 없이도 일반화 가능한 RFM을 얻을 수 있음을 보여주며, 이는 범용 로봇 시스템을 위한 실용적이고 경제적인 경로를 제공합니다.

## 핵심 내용
최근 체화된 AI의 발전으로 로봇 기반 모델(RFM)이 현재까지 범용 로봇 시스템의 지배적인 접근 방식으로 자리 잡았습니다. 방대한 로봇 시연 데이터에 대한 모방 학습을 활용함으로써, RFM은 시각적 관찰과 언어 명령을 연속적인 로봇 동작으로 매핑하는 데 인상적인 능력을 달성했습니다. 그러나 현재의 RFM은 물리적 역학과 로봇 행동이 3D 물리 세계에 미치는 인과적 효과에 대한 본질적인 추론 능력이 부족합니다. 이는 2D 중심의 시각적 인식과 3D 중심의 체화된 상호작용 사이에 근본적인 불일치를 초래하며, 실제 작업에서 RFM의 일반화 능력을 심각하게 제한합니다. 이러한 격차를 해결하기 위해, 우리는 제안된 3D 중심 세계-공간-행동 모델링 패러다임을 기반으로 구축된 새로운 RFM인 WSA$_1$을 제시합니다. 이는 미래 로봇 행동을 위한 3D 세계 인식 시각적 사고를 학습할 뿐만 아니라, 3D 세계 상태 전이와 로봇 동작 간의 상호 제약을 모델링하여 행동 일반화를 향상시킵니다. 특히, WSA$_1$은 6,000시간의 전문가 시연 데이터(실제 로봇 데이터는 1,000시간에 불과)로 매우 데이터 효율적인 사전 학습을 달성하면서, RoboTwin2.0 시뮬레이션 벤치마크에서 경쟁력 있는 조작 성능(93% 성공률)을 제공하고, 실제 로봇 제어 작업에서 최첨단 RFM 대비 평균 +20% 향상된 성능을 달성합니다. 이러한 결과는 3D 중심의 세계-행동 공동 모델링과 결합될 때 대규모 실제 로봇 데이터 없이도 일반화 가능한 RFM을 얻을 수 있음을 보여주며, 이는 범용 로봇 시스템을 위한 실용적이고 경제적인 경로를 제공합니다.
