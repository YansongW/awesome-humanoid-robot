---
$id: ent_paper_robostream_weaving_spatio_temp_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboStream: Weaving Spatio-Temporal Reasoning with Memory in Vision-Language Models for Robotics'
  zh: 'RoboStream: Weaving Spatio-Temporal Reasoning with Memory in Vision-Language Models for Robotics'
  ko: 'RoboStream: Weaving Spatio-Temporal Reasoning with Memory in Vision-Language Models for Robotics'
summary:
  en: 'arXiv:2603.12939v2 Announce Type: replace Abstract: Enabling reliable long-horizon robotic manipulation is a crucial
    step toward open-world embodied intelligence. However, VLM-based planners treat each step as an isolated observation-to-action
    mapping, forcing them to reinfer scene geometry from raw pixels at every decision point while remaining unaware of how
    prior actions have reshaped the environment. Despite strong short-horizon performance, these systems lack the spatio-temporal
    reasoning required for persistent geometric anchoring and memory of action-triggered state transitions. Without persistent
    state tracking, perceptual errors accumulate across the execution horizon, temporarily occluded objects are catastrophically
    forgotten, and these compounding failures lead to precondition violations that cascade through subsequent steps. In contrast,
    humans maintain a persistent mental model that continuously tracks spatial relations and action consequences across interactions
    rather than reconstructing them at each instant. Inspired by this human capacity for causal spatio-temporal reasoning
    with persistent memory, we propose RoboStream, a training-free framework that achieves geometric anchoring through Spatio-Temporal
    Fusion Tokens (STF-Tokens), which bind visual evidence to 3D geometric attributes for persistent object grounding, and
    maintains causal continuity via a Causal Spatio-Temporal Graph (CSTG) that records action-triggered state transitions
    across steps. This design enables the planner to trace causal chains and preserve object permanence under occlusion without
    additional training or fine-tuning. RoboStream achieves 90.5% on long-horizon RLBench and 44.4% on challenging real-world
    block-building tasks, where both SoFar and VoxPoser score 11.1%, demonstrating that spatio-temporal reasoning and causal
    memory are critical missing components for reliable long-horizon manipulation.'
  zh: 'arXiv:2603.12939v2 Announce Type: replace Abstract: Enabling reliable long-horizon robotic manipulation is a crucial
    step toward open-world embodied intelligence. However, VLM-based planners treat each step as an isolated observation-to-action
    mapping, forcing them to reinfer scene geometry from raw pixels at every decision point while remaining unaware of how
    prior actions have reshaped the environment. Despite strong short-horizon performance, these systems lack the spatio-temporal
    reasoning required for persistent geometric anchoring and memory of action-triggered state transitions. Without persistent
    state tracking, perceptual errors accumulate across the execution horizon, temporarily occluded objects are catastrophically
    forgotten, and these compounding failures lead to precondition violations that cascade through subsequent steps. In contrast,
    humans maintain a persistent mental model that continuously tracks spatial relations and action consequences across interactions
    rather than reconstructing them at each instant. Inspired by this human capacity for causal spatio-temporal reasoning
    with persistent memory, we propose RoboStream, a training-free framework that achieves geometric anchoring through Spatio-Temporal
    Fusion Tokens (STF-Tokens), which bind visual evidence to 3D geometric attributes for persistent object grounding, and
    maintains causal continuity via a Causal Spatio-Temporal Graph (CSTG) that records action-triggered state transitions
    across steps. This design enables the planner to trace causal chains and preserve object permanence under occlusion without
    additional training or fine-tuning. RoboStream achieves 90.5% on long-horizon RLBench and 44.4% on challenging real-world
    block-building tasks, where both SoFar and VoxPoser score 11.1%, demonstrating that spatio-temporal reasoning and causal
    memory are critical missing components for reliable long-horizon manipulation.'
  ko: 'arXiv:2603.12939v2 Announce Type: replace Abstract: Enabling reliable long-horizon robotic manipulation is a crucial
    step toward open-world embodied intelligence. However, VLM-based planners treat each step as an isolated observation-to-action
    mapping, forcing them to reinfer scene geometry from raw pixels at every decision point while remaining unaware of how
    prior actions have reshaped the environment. Despite strong short-horizon performance, these systems lack the spatio-temporal
    reasoning required for persistent geometric anchoring and memory of action-triggered state transitions. Without persistent
    state tracking, perceptual errors accumulate across the execution horizon, temporarily occluded objects are catastrophically
    forgotten, and these compounding failures lead to precondition violations that cascade through subsequent steps. In contrast,
    humans maintain a persistent mental model that continuously tracks spatial relations and action consequences across interactions
    rather than reconstructing them at each instant. Inspired by this human capacity for causal spatio-temporal reasoning
    with persistent memory, we propose RoboStream, a training-free framework that achieves geometric anchoring through Spatio-Temporal
    Fusion Tokens (STF-Tokens), which bind visual evidence to 3D geometric attributes for persistent object grounding, and
    maintains causal continuity via a Causal Spatio-Temporal Graph (CSTG) that records action-triggered state transitions
    across steps. This design enables the planner to trace causal chains and preserve object permanence under occlusion without
    additional training or fine-tuning. RoboStream achieves 90.5% on long-horizon RLBench and 44.4% on challenging real-world
    block-building tasks, where both SoFar and VoxPoser score 11.1%, demonstrating that spatio-temporal reasoning and causal
    memory are critical missing components for reliable long-horizon manipulation.'
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
- robostream
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.12939v2.
sources:
- id: src_001
  type: paper
  title: 'RoboStream: Weaving Spatio-Temporal Reasoning with Memory in Vision-Language Models for Robotics (arXiv)'
  url: https://arxiv.org/abs/2603.12939
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
Enabling reliable long-horizon robotic manipulation is a crucial step toward open-world embodied intelligence. However, VLM-based planners treat each step as an isolated observation-to-action mapping, forcing them to reinfer scene geometry from raw pixels at every decision point while remaining unaware of how prior actions have reshaped the environment. Despite strong short-horizon performance, these systems lack the spatio-temporal reasoning required for persistent geometric anchoring and memory of action-triggered state transitions. Without persistent state tracking, perceptual errors accumulate across the execution horizon, temporarily occluded objects are catastrophically forgotten, and these compounding failures lead to precondition violations that cascade through subsequent steps. In contrast, humans maintain a persistent mental model that continuously tracks spatial relations and action consequences across interactions rather than reconstructing them at each instant. Inspired by this human capacity for causal spatio-temporal reasoning with persistent memory, we propose RoboStream, a training-free framework that achieves geometric anchoring through Spatio-Temporal Fusion Tokens (STF-Tokens), which bind visual evidence to 3D geometric attributes for persistent object grounding, and maintains causal continuity via a Causal Spatio-Temporal Graph (CSTG) that records action-triggered state transitions across steps. This design enables the planner to trace causal chains and preserve object permanence under occlusion without additional training or fine-tuning. RoboStream achieves 90.5% on long-horizon RLBench and 44.4% on challenging real-world block-building tasks, where both SoFar and VoxPoser score 11.1%, demonstrating that spatio-temporal reasoning and causal memory are critical missing components for reliable long-horizon manipulation.

## 核心内容
Enabling reliable long-horizon robotic manipulation is a crucial step toward open-world embodied intelligence. However, VLM-based planners treat each step as an isolated observation-to-action mapping, forcing them to reinfer scene geometry from raw pixels at every decision point while remaining unaware of how prior actions have reshaped the environment. Despite strong short-horizon performance, these systems lack the spatio-temporal reasoning required for persistent geometric anchoring and memory of action-triggered state transitions. Without persistent state tracking, perceptual errors accumulate across the execution horizon, temporarily occluded objects are catastrophically forgotten, and these compounding failures lead to precondition violations that cascade through subsequent steps. In contrast, humans maintain a persistent mental model that continuously tracks spatial relations and action consequences across interactions rather than reconstructing them at each instant. Inspired by this human capacity for causal spatio-temporal reasoning with persistent memory, we propose RoboStream, a training-free framework that achieves geometric anchoring through Spatio-Temporal Fusion Tokens (STF-Tokens), which bind visual evidence to 3D geometric attributes for persistent object grounding, and maintains causal continuity via a Causal Spatio-Temporal Graph (CSTG) that records action-triggered state transitions across steps. This design enables the planner to trace causal chains and preserve object permanence under occlusion without additional training or fine-tuning. RoboStream achieves 90.5% on long-horizon RLBench and 44.4% on challenging real-world block-building tasks, where both SoFar and VoxPoser score 11.1%, demonstrating that spatio-temporal reasoning and causal memory are critical missing components for reliable long-horizon manipulation.

## 参考
- http://arxiv.org/abs/2603.12939v2

## Overview
Enabling reliable long-horizon robotic manipulation is a crucial step toward open-world embodied intelligence. However, VLM-based planners treat each step as an isolated observation-to-action mapping, forcing them to reinfer scene geometry from raw pixels at every decision point while remaining unaware of how prior actions have reshaped the environment. Despite strong short-horizon performance, these systems lack the spatio-temporal reasoning required for persistent geometric anchoring and memory of action-triggered state transitions. Without persistent state tracking, perceptual errors accumulate across the execution horizon, temporarily occluded objects are catastrophically forgotten, and these compounding failures lead to precondition violations that cascade through subsequent steps. In contrast, humans maintain a persistent mental model that continuously tracks spatial relations and action consequences across interactions rather than reconstructing them at each instant. Inspired by this human capacity for causal spatio-temporal reasoning with persistent memory, we propose RoboStream, a training-free framework that achieves geometric anchoring through Spatio-Temporal Fusion Tokens (STF-Tokens), which bind visual evidence to 3D geometric attributes for persistent object grounding, and maintains causal continuity via a Causal Spatio-Temporal Graph (CSTG) that records action-triggered state transitions across steps. This design enables the planner to trace causal chains and preserve object permanence under occlusion without additional training or fine-tuning. RoboStream achieves 90.5% on long-horizon RLBench and 44.4% on challenging real-world block-building tasks, where both SoFar and VoxPoser score 11.1%, demonstrating that spatio-temporal reasoning and causal memory are critical missing components for reliable long-horizon manipulation.

## Content
Enabling reliable long-horizon robotic manipulation is a crucial step toward open-world embodied intelligence. However, VLM-based planners treat each step as an isolated observation-to-action mapping, forcing them to reinfer scene geometry from raw pixels at every decision point while remaining unaware of how prior actions have reshaped the environment. Despite strong short-horizon performance, these systems lack the spatio-temporal reasoning required for persistent geometric anchoring and memory of action-triggered state transitions. Without persistent state tracking, perceptual errors accumulate across the execution horizon, temporarily occluded objects are catastrophically forgotten, and these compounding failures lead to precondition violations that cascade through subsequent steps. In contrast, humans maintain a persistent mental model that continuously tracks spatial relations and action consequences across interactions rather than reconstructing them at each instant. Inspired by this human capacity for causal spatio-temporal reasoning with persistent memory, we propose RoboStream, a training-free framework that achieves geometric anchoring through Spatio-Temporal Fusion Tokens (STF-Tokens), which bind visual evidence to 3D geometric attributes for persistent object grounding, and maintains causal continuity via a Causal Spatio-Temporal Graph (CSTG) that records action-triggered state transitions across steps. This design enables the planner to trace causal chains and preserve object permanence under occlusion without additional training or fine-tuning. RoboStream achieves 90.5% on long-horizon RLBench and 44.4% on challenging real-world block-building tasks, where both SoFar and VoxPoser score 11.1%, demonstrating that spatio-temporal reasoning and causal memory are critical missing components for reliable long-horizon manipulation.

## 개요
신뢰할 수 있는 장기 로봇 조작을 가능하게 하는 것은 개방형 세계 구현 지능을 향한 중요한 단계입니다. 그러나 VLM 기반 플래너는 각 단계를 고립된 관찰-행동 매핑으로 처리하여, 매 의사 결정 시점마다 원시 픽셀에서 장면 기하학을 다시 추론해야 하며, 이전 행동이 환경을 어떻게 변화시켰는지 인식하지 못합니다. 단기 성능은 뛰어나지만, 이러한 시스템은 지속적인 기하학적 앵커링과 행동으로 유발된 상태 전이에 대한 기억에 필요한 시공간 추론 능력이 부족합니다. 지속적인 상태 추적이 없으면 실행 기간 동안 인식 오류가 누적되고, 일시적으로 가려진 객체는 치명적으로 망각되며, 이러한 복합적인 실패는 후속 단계로 연쇄되는 전제 조건 위반으로 이어집니다. 반면, 인간은 매 순간 재구성하는 대신 상호작용 전반에 걸쳐 공간 관계와 행동 결과를 지속적으로 추적하는 지속적인 정신 모델을 유지합니다. 지속적인 기억을 통한 인과적 시공간 추론이라는 이러한 인간의 능력에서 영감을 받아, 우리는 훈련이 필요 없는 프레임워크인 RoboStream을 제안합니다. 이는 시공간 융합 토큰(STF-Tokens)을 통해 기하학적 앵커링을 달성하여 시각적 증거를 3D 기하학적 속성에 결합하여 지속적인 객체 그라운딩을 가능하게 하고, 인과적 시공간 그래프(CSTG)를 통해 단계 간 행동으로 유발된 상태 전이를 기록하여 인과적 연속성을 유지합니다. 이 설계는 추가 훈련이나 미세 조정 없이도 플래너가 인과 사슬을 추적하고 가려짐 속에서도 객체 영속성을 보존할 수 있게 합니다. RoboStream은 장기 RLBench에서 90.5%, 도전적인 실제 블록 쌓기 작업에서 44.4%를 달성했으며, SoFar와 VoxPoser는 모두 11.1%를 기록하여, 시공간 추론과 인과적 기억이 신뢰할 수 있는 장기 조작에 중요한 누락 요소임을 입증합니다.

## 핵심 내용
신뢰할 수 있는 장기 로봇 조작을 가능하게 하는 것은 개방형 세계 구현 지능을 향한 중요한 단계입니다. 그러나 VLM 기반 플래너는 각 단계를 고립된 관찰-행동 매핑으로 처리하여, 매 의사 결정 시점마다 원시 픽셀에서 장면 기하학을 다시 추론해야 하며, 이전 행동이 환경을 어떻게 변화시켰는지 인식하지 못합니다. 단기 성능은 뛰어나지만, 이러한 시스템은 지속적인 기하학적 앵커링과 행동으로 유발된 상태 전이에 대한 기억에 필요한 시공간 추론 능력이 부족합니다. 지속적인 상태 추적이 없으면 실행 기간 동안 인식 오류가 누적되고, 일시적으로 가려진 객체는 치명적으로 망각되며, 이러한 복합적인 실패는 후속 단계로 연쇄되는 전제 조건 위반으로 이어집니다. 반면, 인간은 매 순간 재구성하는 대신 상호작용 전반에 걸쳐 공간 관계와 행동 결과를 지속적으로 추적하는 지속적인 정신 모델을 유지합니다. 지속적인 기억을 통한 인과적 시공간 추론이라는 이러한 인간의 능력에서 영감을 받아, 우리는 훈련이 필요 없는 프레임워크인 RoboStream을 제안합니다. 이는 시공간 융합 토큰(STF-Tokens)을 통해 기하학적 앵커링을 달성하여 시각적 증거를 3D 기하학적 속성에 결합하여 지속적인 객체 그라운딩을 가능하게 하고, 인과적 시공간 그래프(CSTG)를 통해 단계 간 행동으로 유발된 상태 전이를 기록하여 인과적 연속성을 유지합니다. 이 설계는 추가 훈련이나 미세 조정 없이도 플래너가 인과 사슬을 추적하고 가려짐 속에서도 객체 영속성을 보존할 수 있게 합니다. RoboStream은 장기 RLBench에서 90.5%, 도전적인 실제 블록 쌓기 작업에서 44.4%를 달성했으며, SoFar와 VoxPoser는 모두 11.1%를 기록하여, 시공간 추론과 인과적 기억이 신뢰할 수 있는 장기 조작에 중요한 누락 요소임을 입증합니다.
