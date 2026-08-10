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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.12939v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (993 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2603.12939v2

## 개요
기존 VLM 플래너는 각 단계를 고립된 관찰-행동 매핑으로 간주하여, 이전 행동이 환경을 어떻게 변화시켰는지 인식하지 못하며 기하학적 정보에 대한 지속적인 앵커링이 부족합니다. 이러한 결함은 장시간 실행에서 인식 오류가 누적되고, 일시적으로 가려진 객체가 치명적으로 망각되어 전제 조건 위반의 연쇄 실패를 유발합니다. 인간의 인과적 시공간 추론 능력에서 영감을 받은 RoboStream은 STF-Tokens를 통해 시각적 증거를 3D 기하학적 속성에 결합하여 지속적인 객체 위치 파악을 구현하고, CSTG를 통해 단계 간 상태 변화를 기록하여 플래너가 인과 체인을 추적할 수 있게 합니다. 이 프레임워크는 추가 훈련이나 미세 조정 없이 장시간 조작에서 신뢰성을 크게 향상시킵니다.

## 핵심 내용
### 방법 아키텍처
- **시공간 융합 토큰 (STF-Tokens)**: 시각적 특징을 3D 기하학적 속성(예: 위치, 자세)과 융합하여 지속적인 객체 표현을 형성합니다. 이러한 토큰은 시간 단계 간에 전달되어 객체가 가려져도 기하학적 정보를 검색할 수 있게 합니다.
- **인과 시공간 그래프 (CSTG)**: 방향 그래프를 구축하며, 노드는 객체 상태를, 엣지는 행동으로 유발된 상태 변화(예: "집은 후 객체 위치 변경")를 나타냅니다. 플래너는 그래프 구조를 탐색하여 인과 체인을 추적하고, 이전 행동을 망각하여 오류를 반복하는 것을 방지합니다.

### 실험 설정
- **시뮬레이션 환경**: RLBench 장시간 작업(예: "컵을 서랍에 넣고 닫기")으로, 다단계 조작과 객체 가림 시나리오를 포함합니다.
- **실제 세계 작업**: 블록형 객체 쌓기(예: 블록 적층)로, 동적 가림과 정밀한 공간 정렬을 포함합니다.
- **기준 방법**: SoFar(VLM 기반 플래너), VoxPoser(3D 복셀 기반 플래너)로, 둘 다 시공간 인과를 명시적으로 모델링하지 않습니다.

### 주요 결과
- **RLBench 장시간 작업**: RoboStream 성공률 90.5%, SoFar와 VoxPoser는 모두 30% 미만.
- **실제 세계 블록 쌓기**: RoboStream 성공률 44.4%, SoFar와 VoxPoser는 모두 11.1%.
- **절제 실험**: STF-Tokens 제거 시 성공률 35% 하락, CSTG 제거 시 28% 하락, 두 요소가 장시간 추론에 상호 보완적 역할을 한다는 것을 확인.

### 결론
RoboStream은 추가 훈련 없이 명시적 시공간 추론과 인과 기억을 통해 VLM 플래너의 장시간 신뢰성을 크게 향상시킬 수 있음을 입증합니다. 핵심 기여는 기하학적 앵커링과 상태 변화 기록을 독립 모듈로 통합하여 기존 방법의 지속적 인식 부족을 보완하는 데 있습니다.
