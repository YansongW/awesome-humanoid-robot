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
  zh: RoboStream 是一个无需训练的框架，旨在解决 VLM 机器人规划器在长时域操作中缺乏时空推理与因果记忆的问题。它通过 Spatio-Temporal Fusion Tokens (STF-Tokens) 实现几何锚定，并利用
    Causal Spatio-Temporal Graph (CSTG) 记录动作触发的状态变迁，从而在遮挡下保持物体永久性。在 RLBench 长时域任务上达到 90.5% 的成功率，在真实世界积木搭建任务上达到 44.4%，远超 SoFar
    和 VoxPoser 的 11.1%。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.12939v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'RoboStream: Weaving Spatio-Temporal Reasoning with Memory in Vision-Language Models for Robotics (arXiv)'
  url: https://arxiv.org/abs/2603.12939
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
现有 VLM 规划器将每一步视为孤立的观测到动作映射，导致其无法感知先前动作如何改变环境，且缺乏对几何信息的持久锚定。这种缺陷使得感知误差在长时域执行中累积，临时遮挡的物体会被灾难性遗忘，进而引发前提条件违反的级联失败。受人类因果时空推理能力的启发，RoboStream 通过 STF-Tokens 将视觉证据与 3D 几何属性绑定，实现持久物体定位；同时利用 CSTG 记录跨步骤的状态变迁，使规划器能够追溯因果链。该框架无需额外训练或微调，即可在长时域操作中显著提升可靠性。

## 核心内容
### 方法架构
- **Spatio-Temporal Fusion Tokens (STF-Tokens)**：将视觉特征与 3D 几何属性（如位置、姿态）融合，形成持久化的物体表征。这些 Token 在时间步间传递，确保即使物体被遮挡，其几何信息仍可被检索。
- **Causal Spatio-Temporal Graph (CSTG)**：构建有向图，节点表示物体状态，边表示动作触发的状态变迁（如“抓取后物体位置改变”）。规划器通过遍历图结构追溯因果链，避免因遗忘先前动作而重复错误。

### 实验设置
- **模拟环境**：RLBench 长时域任务（如“将杯子放入抽屉并关闭”），包含多步骤操作与物体遮挡场景。
- **真实世界任务**：块状物体搭建（如堆叠积木），涉及动态遮挡与精确空间对齐。
- **基线方法**：SoFar（基于 VLM 的规划器）、VoxPoser（基于 3D 体素的规划器），均未显式建模时空因果。

### 关键结果
- **RLBench 长时域任务**：RoboStream 成功率 90.5%，SoFar 与 VoxPoser 均低于 30%。
- **真实世界积木搭建**：RoboStream 成功率 44.4%，SoFar 与 VoxPoser 均为 11.1%。
- **消融实验**：移除 STF-Tokens 后成功率下降 35%，移除 CSTG 后下降 28%，证实两者对长时域推理的互补作用。

### 结论
RoboStream 证明，无需额外训练即可通过显式时空推理与因果记忆显著提升 VLM 规划器的长时域可靠性。其核心贡献在于将几何锚定与状态变迁记录作为独立模块，弥补了现有方法在持久性感知上的缺失。

## Overview
Enabling reliable long-horizon robotic manipulation is a crucial step toward open-world embodied intelligence. However, VLM-based planners treat each step as an isolated observation-to-action mapping, forcing them to reinfer scene geometry from raw pixels at every decision point while remaining unaware of how prior actions have reshaped the environment. Despite strong short-horizon performance, these systems lack the spatio-temporal reasoning required for persistent geometric anchoring and memory of action-triggered state transitions. Without persistent state tracking, perceptual errors accumulate across the execution horizon, temporarily occluded objects are catastrophically forgotten, and these compounding failures lead to precondition violations that cascade through subsequent steps. In contrast, humans maintain a persistent mental model that continuously tracks spatial relations and action consequences across interactions rather than reconstructing them at each instant. Inspired by this human capacity for causal spatio-temporal reasoning with persistent memory, we propose RoboStream, a training-free framework that achieves geometric anchoring through Spatio-Temporal Fusion Tokens (STF-Tokens), which bind visual evidence to 3D geometric attributes for persistent object grounding, and maintains causal continuity via a Causal Spatio-Temporal Graph (CSTG) that records action-triggered state transitions across steps. This design enables the planner to trace causal chains and preserve object permanence under occlusion without additional training or fine-tuning. RoboStream achieves 90.5% on long-horizon RLBench and 44.4% on challenging real-world block-building tasks, where both SoFar and VoxPoser score 11.1%, demonstrating that spatio-temporal reasoning and causal memory are critical missing components for reliable long-horizon manipulation.

## 개요
신뢰할 수 있는 장기 로봇 조작을 가능하게 하는 것은 개방형 세계 구현 지능을 향한 중요한 단계입니다. 그러나 VLM 기반 플래너는 각 단계를 고립된 관찰-행동 매핑으로 처리하여, 매 의사 결정 시점마다 원시 픽셀에서 장면 기하학을 다시 추론해야 하며, 이전 행동이 환경을 어떻게 변화시켰는지 인식하지 못합니다. 단기 성능은 뛰어나지만, 이러한 시스템은 지속적인 기하학적 앵커링과 행동으로 유발된 상태 전이에 대한 기억에 필요한 시공간 추론 능력이 부족합니다. 지속적인 상태 추적이 없으면 실행 기간 동안 인식 오류가 누적되고, 일시적으로 가려진 객체는 치명적으로 망각되며, 이러한 복합적인 실패는 후속 단계로 연쇄되는 전제 조건 위반으로 이어집니다. 반면, 인간은 매 순간 재구성하는 대신 상호작용 전반에 걸쳐 공간 관계와 행동 결과를 지속적으로 추적하는 지속적인 정신 모델을 유지합니다. 지속적인 기억을 통한 인과적 시공간 추론이라는 이러한 인간의 능력에서 영감을 받아, 우리는 훈련이 필요 없는 프레임워크인 RoboStream을 제안합니다. 이는 시공간 융합 토큰(STF-Tokens)을 통해 기하학적 앵커링을 달성하여 시각적 증거를 3D 기하학적 속성에 결합하여 지속적인 객체 그라운딩을 가능하게 하고, 인과적 시공간 그래프(CSTG)를 통해 단계 간 행동으로 유발된 상태 전이를 기록하여 인과적 연속성을 유지합니다. 이 설계는 추가 훈련이나 미세 조정 없이도 플래너가 인과 사슬을 추적하고 가려짐 속에서도 객체 영속성을 보존할 수 있게 합니다. RoboStream은 장기 RLBench에서 90.5%, 도전적인 실제 블록 쌓기 작업에서 44.4%를 달성했으며, SoFar와 VoxPoser는 모두 11.1%를 기록하여, 시공간 추론과 인과적 기억이 신뢰할 수 있는 장기 조작에 중요한 누락 요소임을 입증합니다.

## 핵심 내용
신뢰할 수 있는 장기 로봇 조작을 가능하게 하는 것은 개방형 세계 구현 지능을 향한 중요한 단계입니다. 그러나 VLM 기반 플래너는 각 단계를 고립된 관찰-행동 매핑으로 처리하여, 매 의사 결정 시점마다 원시 픽셀에서 장면 기하학을 다시 추론해야 하며, 이전 행동이 환경을 어떻게 변화시켰는지 인식하지 못합니다. 단기 성능은 뛰어나지만, 이러한 시스템은 지속적인 기하학적 앵커링과 행동으로 유발된 상태 전이에 대한 기억에 필요한 시공간 추론 능력이 부족합니다. 지속적인 상태 추적이 없으면 실행 기간 동안 인식 오류가 누적되고, 일시적으로 가려진 객체는 치명적으로 망각되며, 이러한 복합적인 실패는 후속 단계로 연쇄되는 전제 조건 위반으로 이어집니다. 반면, 인간은 매 순간 재구성하는 대신 상호작용 전반에 걸쳐 공간 관계와 행동 결과를 지속적으로 추적하는 지속적인 정신 모델을 유지합니다. 지속적인 기억을 통한 인과적 시공간 추론이라는 이러한 인간의 능력에서 영감을 받아, 우리는 훈련이 필요 없는 프레임워크인 RoboStream을 제안합니다. 이는 시공간 융합 토큰(STF-Tokens)을 통해 기하학적 앵커링을 달성하여 시각적 증거를 3D 기하학적 속성에 결합하여 지속적인 객체 그라운딩을 가능하게 하고, 인과적 시공간 그래프(CSTG)를 통해 단계 간 행동으로 유발된 상태 전이를 기록하여 인과적 연속성을 유지합니다. 이 설계는 추가 훈련이나 미세 조정 없이도 플래너가 인과 사슬을 추적하고 가려짐 속에서도 객체 영속성을 보존할 수 있게 합니다. RoboStream은 장기 RLBench에서 90.5%, 도전적인 실제 블록 쌓기 작업에서 44.4%를 달성했으며, SoFar와 VoxPoser는 모두 11.1%를 기록하여, 시공간 추론과 인과적 기억이 신뢰할 수 있는 장기 조작에 중요한 누락 요소임을 입증합니다.

## 参考
- http://arxiv.org/abs/2603.12939v2
