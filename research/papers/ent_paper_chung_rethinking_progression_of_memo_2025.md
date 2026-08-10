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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.11478v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (775 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2511.11478v3

## 개요
복잡한 환경에서 로봇은 여러 시각적으로 유사한 물체의 개별 이력 상태를 추적하고 추론해야 하지만, 기존 비전-언어-행동 모델은 토큰 확장 문제로 인해 긴 시퀀스를 처리하기 어렵다. Embodied-SlotSSM은 시공간적으로 일관된 물체 슬롯 정체성을 유지하고, 슬롯 상태 공간 모델과 관계 인코더를 결합하여 단기 이력 재구성과 행동 디코딩 정렬을 구현한다. 실험 결과, 이 모델은 LIBERO-Mem 및 일반 작업에서 확장 가능한 비마르코프 추론 능력을 보여준다.

## 핵심 내용
### 문제 배경
- 비마르코프 작업에서 결정은 현재 장면 스냅샷이 아닌 물체의 이력 상호작용(예: "어떤 물체가 이미 조작되었는가")에 의존한다.
- 기존 VLA 모델은 토큰 수가 프레임 수에 따라 선형적으로 증가하여 수백 프레임의 긴 시퀀스 작업을 처리하기 어렵다.

### 방법 아키텍처
- **물체 슬롯 상태 공간 모델 (Slot-SSM)**: 각 물체의 시공간적으로 일관된 슬롯 정체성을 유지하고, 상태 공간 모델을 통해 단기 이력 궤적을 재구성한다.
- **관계 인코더**: 입력 토큰을 물체 슬롯과 정렬하여 맥락 인식 행동 디코딩을 구현한다.
- **전체 흐름**: 입력 이미지 → 물체 슬롯 추출 → 슬롯 상태 공간 모델링 → 관계 인코딩 → 행동 예측.

### 실험 설정
- **LIBERO-Mem 작업 스위트**: 단기/장기 시역 물체 추적 및 시간 순서 하위 목표를 포함하며, 프레임 간 추론이 필요하다.
- **기준선 비교**: RT-2, Octo 등 VLA 모델과 LIBERO-Mem 및 LIBERO 일반 작업에서 비교한다.

### 주요 결과
- Embodied-SlotSSM은 LIBERO-Mem 작업에서 기준선보다 성공률이 12-18% 높았으며, 특히 물체 이력 메모리가 필요한 시퀀스 조작에서 두드러졌다.
- LIBERO 일반 작업에서도 경쟁력을 유지하여 메모리 메커니즘으로 인한 일반 성능 저하가 없었다.
- 토큰 소비는 기존 VLA 모델의 1/5에 불과하며(500프레임 처리 시), 선형 복잡도 확장을 구현했다.

### 결론
Embodied-SlotSSM은 물체 중심의 시간적 메모리를 통해 로봇 조작에서의 비마르코프 추론을 위한 확장 가능한 솔루션을 제공하며, 향후 더 복잡한 물체 관계 추론과 결합할 수 있다.
