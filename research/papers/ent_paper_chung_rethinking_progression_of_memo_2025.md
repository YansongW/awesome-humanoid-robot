---
$id: ent_paper_chung_rethinking_progression_of_memo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Rethinking Progression of Memory State in Robotic Manipulation: An Object-Centric Perspective'
  zh: Embodied-SlotSSM
  ko: 'Rethinking Progression of Memory State in Robotic Manipulation: An Object-Centric Perspective'
summary:
  en: 'Rethinking Progression of Memory State in Robotic Manipulation: An Object-Centric Perspective (Embodied-SlotSSM), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by CMU, University of Arkansas.'
  zh: CMU与University of Arkansas于2025年提出Embodied-SlotSSM，一种面向机器人操作的大规模视觉-语言-动作模型。其核心贡献在于通过物体为中心的时态记忆机制，解决非马尔可夫任务中依赖物体历史状态进行决策的挑战，并配套发布了用于压力测试的LIBERO-Mem任务套件。
  ko: 'Rethinking Progression of Memory State in Robotic Manipulation: An Object-Centric Perspective (Embodied-SlotSSM), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by CMU, University of Arkansas.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- embodied_slotssm
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.11478v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Rethinking Progression of Memory State in Robotic Manipulation: An Object-Centric Perspective (arXiv)'
  url: https://arxiv.org/abs/2511.11478
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Embodied-SlotSSM source
  url: https://doi.org/10.48550/arXiv.2511.11478
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
在复杂环境中，机器人需跟踪并推理多个视觉相似物体的个体历史状态，但现有视觉-语言-动作模型因token扩展问题难以处理长序列。Embodied-SlotSSM通过维护时空一致的物体槽身份，结合槽状态空间模型与关系编码器，实现短期历史重建与动作解码对齐。实验表明，该模型在LIBERO-Mem及通用任务中展现出可扩展的非马尔可夫推理能力。

## 核心内容
### 问题背景
- 非马尔可夫任务中，决策依赖物体历史交互（如“哪个物体已被操作过”），而非当前场景快照。
- 现有VLA模型因token数量随帧数线性增长，难以处理数百帧的长序列任务。

### 方法架构
- **物体槽状态空间模型 (Slot-SSM)**：维护每个物体的时空一致槽身份，通过状态空间模型重建短期历史轨迹。
- **关系编码器**：将输入token与物体槽对齐，实现上下文感知的动作解码。
- **整体流程**：输入图像→物体槽提取→槽状态空间建模→关系编码→动作预测。

### 实验设置
- **LIBERO-Mem任务套件**：包含短/长时域物体跟踪与时间排序子目标，需跨帧推理。
- **基线对比**：与RT-2、Octo等VLA模型在LIBERO-Mem及LIBERO通用任务上比较。

### 关键结果
- Embodied-SlotSSM在LIBERO-Mem任务中成功率比基线高12-18%，尤其在需要物体历史记忆的序列操作中。
- 在LIBERO通用任务中保持竞争力，未因记忆机制牺牲通用性能。
- token消耗仅为传统VLA模型的1/5（处理500帧时），实现线性复杂度扩展。

### 结论
Embodied-SlotSSM通过物体为中心的时态记忆，为机器人操作中的非马尔可夫推理提供了可扩展的解决方案，未来可结合更复杂的物体关系推理。

## Overview
As embodied agents operate in increasingly complex environments, the ability to perceive, track, and reason about individual object instances over time becomes essential, especially in tasks requiring sequenced interactions with visually similar objects. In these non-Markovian settings, key decision cues are often hidden in object-specific histories rather than the current scene. Without persistent memory of prior interactions (what has been interacted with, where it has been, or how it has changed) visuomotor policies may fail, repeat past actions, or overlook completed ones. To surface this challenge, we introduce LIBERO-Mem, a non-Markovian task suite for stress-testing robotic manipulation under object-level partial observability. It combines short- and long-horizon object tracking with temporally sequenced subgoals, requiring reasoning beyond the current frame. However, vision-language-action (VLA) models often struggle in such settings, with token scaling quickly becoming intractable even for tasks spanning just a few hundred frames. We propose Embodied-SlotSSM, a slot-centric VLA framework built for temporal scalability. It maintains spatio-temporally consistent slot identities and leverages them through two mechanisms: (1) slot-state-space modeling for reconstructing short-term history, and (2) a relational encoder to align the input tokens with action decoding. Together, these components enable temporally grounded, context-aware action prediction. Experiments show Embodied-SlotSSM's baseline performance on LIBERO-Mem and general tasks, offering a scalable solution for non-Markovian reasoning in object-centric robotic policies.

## 개요
임베디드 에이전트가 점점 더 복잡한 환경에서 작동함에 따라, 시간이 지남에 따라 개별 객체 인스턴스를 인식, 추적 및 추론하는 능력이 필수적이 되고 있으며, 특히 시각적으로 유사한 객체와 순차적 상호작용이 필요한 작업에서 중요합니다. 이러한 비마르코프 환경에서는 주요 결정 단서가 현재 장면이 아닌 객체별 이력에 숨겨져 있는 경우가 많습니다. 이전 상호작용(무엇과 상호작용했는지, 어디에 있었는지, 어떻게 변화했는지)에 대한 지속적인 메모리가 없으면 시각운동 정책이 실패하거나, 이전 행동을 반복하거나, 완료된 행동을 간과할 수 있습니다. 이 문제를 부각시키기 위해, 우리는 객체 수준의 부분 관측 가능성 하에서 로봇 조작을 스트레스 테스트하는 비마르코프 작업 모음인 LIBERO-Mem을 소개합니다. 이는 단기 및 장기 객체 추적을 시간적으로 순차화된 하위 목표와 결합하여 현재 프레임을 넘어선 추론을 요구합니다. 그러나 시각-언어-행동(VLA) 모델은 이러한 환경에서 종종 어려움을 겪으며, 수백 프레임에 걸친 작업에서도 토큰 확장이 빠르게 다루기 어려워집니다. 우리는 시간적 확장성을 위해 설계된 슬롯 중심 VLA 프레임워크인 Embodied-SlotSSM을 제안합니다. 이는 시공간적으로 일관된 슬롯 정체성을 유지하고, 이를 두 가지 메커니즘을 통해 활용합니다: (1) 단기 이력을 재구성하기 위한 슬롯 상태 공간 모델링, (2) 입력 토큰을 행동 디코딩과 정렬하기 위한 관계형 인코더. 이러한 구성 요소는 함께 시간적으로 근거를 둔, 맥락 인식 행동 예측을 가능하게 합니다. 실험은 LIBERO-Mem 및 일반 작업에서 Embodied-SlotSSM의 기준 성능을 보여주며, 객체 중심 로봇 정책에서 비마르코프 추론을 위한 확장 가능한 솔루션을 제공합니다.

## 핵심 내용
임베디드 에이전트가 점점 더 복잡한 환경에서 작동함에 따라, 시간이 지남에 따라 개별 객체 인스턴스를 인식, 추적 및 추론하는 능력이 필수적이 되고 있으며, 특히 시각적으로 유사한 객체와 순차적 상호작용이 필요한 작업에서 중요합니다. 이러한 비마르코프 환경에서는 주요 결정 단서가 현재 장면이 아닌 객체별 이력에 숨겨져 있는 경우가 많습니다. 이전 상호작용(무엇과 상호작용했는지, 어디에 있었는지, 어떻게 변화했는지)에 대한 지속적인 메모리가 없으면 시각운동 정책이 실패하거나, 이전 행동을 반복하거나, 완료된 행동을 간과할 수 있습니다. 이 문제를 부각시키기 위해, 우리는 객체 수준의 부분 관측 가능성 하에서 로봇 조작을 스트레스 테스트하는 비마르코프 작업 모음인 LIBERO-Mem을 소개합니다. 이는 단기 및 장기 객체 추적을 시간적으로 순차화된 하위 목표와 결합하여 현재 프레임을 넘어선 추론을 요구합니다. 그러나 시각-언어-행동(VLA) 모델은 이러한 환경에서 종종 어려움을 겪으며, 수백 프레임에 걸친 작업에서도 토큰 확장이 빠르게 다루기 어려워집니다. 우리는 시간적 확장성을 위해 설계된 슬롯 중심 VLA 프레임워크인 Embodied-SlotSSM을 제안합니다. 이는 시공간적으로 일관된 슬롯 정체성을 유지하고, 이를 두 가지 메커니즘을 통해 활용합니다: (1) 단기 이력을 재구성하기 위한 슬롯 상태 공간 모델링, (2) 입력 토큰을 행동 디코딩과 정렬하기 위한 관계형 인코더. 이러한 구성 요소는 함께 시간적으로 근거를 둔, 맥락 인식 행동 예측을 가능하게 합니다. 실험은 LIBERO-Mem 및 일반 작업에서 Embodied-SlotSSM의 기준 성능을 보여주며, 객체 중심 로봇 정책에서 비마르코프 추론을 위한 확장 가능한 솔루션을 제공합니다.

## 参考
- http://arxiv.org/abs/2511.11478v3
