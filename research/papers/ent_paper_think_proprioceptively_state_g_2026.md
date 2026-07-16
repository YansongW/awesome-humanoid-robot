---
$id: ent_paper_think_proprioceptively_state_g_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Think Proprioceptively: State-Grounded Visual Token Selection for VLA Policies'
  zh: 'Think Proprioceptively: State-Grounded Visual Token Selection for VLA Policies'
  ko: 'Think Proprioceptively: State-Grounded Visual Token Selection for VLA Policies'
summary:
  en: 'arXiv:2602.06575v2 Announce Type: replace Abstract: Vision-language-action (VLA) models typically inject proprioception
    only as a late conditioning signal, preventing robot state from grounding instruction understanding or directing visual
    attention. We introduce ThinkProprio, which discretizes proprioception into VLM-vocabulary tokens and uses them jointly
    with the instruction to gate visual patches before VLM computation, steering the model toward action-relevant evidence
    while discarding redundant tokens early. We find that proprioception added as a passive conditioning signal leaves performance
    essentially unchanged; its value emerges when token-form state acts as an active query that, with the instruction, selects
    which visual patches the VLM processes. Systematic ablations show that VLM-vocabulary tokens outperform learned projectors
    as the state encoding, and that retaining only about \SI{12}{\percent} of the visual tokens surpasses on CALVIN ABC$\to$D.
    Across CALVIN, LIBERO, and real-world manipulation, ThinkProprio reduces end-to-end inference latency while improving
    the matched full-token baseline.'
  zh: 'arXiv:2602.06575v2 Announce Type: replace Abstract: Vision-language-action (VLA) models typically inject proprioception
    only as a late conditioning signal, preventing robot state from grounding instruction understanding or directing visual
    attention. We introduce ThinkProprio, which discretizes proprioception into VLM-vocabulary tokens and uses them jointly
    with the instruction to gate visual patches before VLM computation, steering the model toward action-relevant evidence
    while discarding redundant tokens early. We find that proprioception added as a passive conditioning signal leaves performance
    essentially unchanged; its value emerges when token-form state acts as an active query that, with the instruction, selects
    which visual patches the VLM processes. Systematic ablations show that VLM-vocabulary tokens outperform learned projectors
    as the state encoding, and that retaining only about \SI{12}{\percent} of the visual tokens surpasses on CALVIN ABC$\to$D.
    Across CALVIN, LIBERO, and real-world manipulation, ThinkProprio reduces end-to-end inference latency while improving
    the matched full-token baseline.'
  ko: 'arXiv:2602.06575v2 Announce Type: replace Abstract: Vision-language-action (VLA) models typically inject proprioception
    only as a late conditioning signal, preventing robot state from grounding instruction understanding or directing visual
    attention. We introduce ThinkProprio, which discretizes proprioception into VLM-vocabulary tokens and uses them jointly
    with the instruction to gate visual patches before VLM computation, steering the model toward action-relevant evidence
    while discarding redundant tokens early. We find that proprioception added as a passive conditioning signal leaves performance
    essentially unchanged; its value emerges when token-form state acts as an active query that, with the instruction, selects
    which visual patches the VLM processes. Systematic ablations show that VLM-vocabulary tokens outperform learned projectors
    as the state encoding, and that retaining only about \SI{12}{\percent} of the visual tokens surpasses on CALVIN ABC$\to$D.
    Across CALVIN, LIBERO, and real-world manipulation, ThinkProprio reduces end-to-end inference latency while improving
    the matched full-token baseline.'
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
- think_proprioceptively
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.06575v2.
sources:
- id: src_001
  type: paper
  title: 'Think Proprioceptively: State-Grounded Visual Token Selection for VLA Policies (arXiv)'
  url: https://arxiv.org/abs/2602.06575
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Vision-language-action (VLA) models typically inject proprioception only as a late conditioning signal, preventing robot state from grounding instruction understanding or directing visual attention. We introduce ThinkProprio, which discretizes proprioception into VLM-vocabulary tokens and uses them jointly with the instruction to gate visual patches before VLM computation, steering the model toward action-relevant evidence while discarding redundant tokens early. We find that proprioception added as a passive conditioning signal leaves performance essentially unchanged; its value emerges when token-form state acts as an active query that, with the instruction, selects which visual patches the VLM processes. Systematic ablations show that VLM-vocabulary tokens outperform learned projectors as the state encoding, and that retaining only about \SI{12}{\percent} of the visual tokens surpasses on CALVIN ABC$\to$D. Across CALVIN, LIBERO, and real-world manipulation, ThinkProprio reduces end-to-end inference latency while improving the matched full-token baseline.

## 核心内容
Vision-language-action (VLA) models typically inject proprioception only as a late conditioning signal, preventing robot state from grounding instruction understanding or directing visual attention. We introduce ThinkProprio, which discretizes proprioception into VLM-vocabulary tokens and uses them jointly with the instruction to gate visual patches before VLM computation, steering the model toward action-relevant evidence while discarding redundant tokens early. We find that proprioception added as a passive conditioning signal leaves performance essentially unchanged; its value emerges when token-form state acts as an active query that, with the instruction, selects which visual patches the VLM processes. Systematic ablations show that VLM-vocabulary tokens outperform learned projectors as the state encoding, and that retaining only about \SI{12}{\percent} of the visual tokens surpasses on CALVIN ABC$\to$D. Across CALVIN, LIBERO, and real-world manipulation, ThinkProprio reduces end-to-end inference latency while improving the matched full-token baseline.

## 参考
- http://arxiv.org/abs/2602.06575v2

## Overview
Vision-language-action (VLA) models typically inject proprioception only as a late conditioning signal, preventing robot state from grounding instruction understanding or directing visual attention. We introduce ThinkProprio, which discretizes proprioception into VLM-vocabulary tokens and uses them jointly with the instruction to gate visual patches before VLM computation, steering the model toward action-relevant evidence while discarding redundant tokens early. We find that proprioception added as a passive conditioning signal leaves performance essentially unchanged; its value emerges when token-form state acts as an active query that, with the instruction, selects which visual patches the VLM processes. Systematic ablations show that VLM-vocabulary tokens outperform learned projectors as the state encoding, and that retaining only about \SI{12}{\percent} of the visual tokens surpasses on CALVIN ABC$\to$D. Across CALVIN, LIBERO, and real-world manipulation, ThinkProprio reduces end-to-end inference latency while improving the matched full-token baseline.

## Content
Vision-language-action (VLA) models typically inject proprioception only as a late conditioning signal, preventing robot state from grounding instruction understanding or directing visual attention. We introduce ThinkProprio, which discretizes proprioception into VLM-vocabulary tokens and uses them jointly with the instruction to gate visual patches before VLM computation, steering the model toward action-relevant evidence while discarding redundant tokens early. We find that proprioception added as a passive conditioning signal leaves performance essentially unchanged; its value emerges when token-form state acts as an active query that, with the instruction, selects which visual patches the VLM processes. Systematic ablations show that VLM-vocabulary tokens outperform learned projectors as the state encoding, and that retaining only about \SI{12}{\percent} of the visual tokens surpasses on CALVIN ABC$\to$D. Across CALVIN, LIBERO, and real-world manipulation, ThinkProprio reduces end-to-end inference latency while improving the matched full-token baseline.

## 개요
Vision-language-action (VLA) 모델은 일반적으로 고유 감각(proprioception)을 단순히 후기 조건화 신호(late conditioning signal)로만 주입하여, 로봇 상태가 명령 이해를 근거하거나 시각적 주의를 유도하지 못하게 합니다. 우리는 ThinkProprio를 소개합니다. 이는 고유 감각을 VLM 어휘 토큰(VLM-vocabulary tokens)으로 이산화하고, 이를 명령과 함께 사용하여 VLM 계산 전에 시각 패치를 게이팅(gating)함으로써, 모델이 행동 관련 증거에 집중하고 중복 토큰을 조기에 폐기하도록 유도합니다. 우리는 고유 감각이 수동적 조건화 신호로 추가될 때 성능이 거의 변하지 않음을 발견했습니다. 그 가치는 토큰 형태의 상태가 명령과 함께 VLM이 처리할 시각 패치를 선택하는 능동적 질의(active query)로 작용할 때 나타납니다. 체계적 절제 실험(systematic ablations)은 VLM 어휘 토큰이 학습된 프로젝터(learned projectors)보다 상태 인코딩으로 더 우수하며, 시각 토큰의 약 \SI{12}{\percent}만 유지해도 CALVIN ABC$\to$D에서 더 나은 성능을 보임을 입증합니다. CALVIN, LIBERO 및 실제 세계 조작 작업에서 ThinkProprio는 일치하는 전체 토큰 기준선(matched full-token baseline)을 개선하면서 종단 간 추론 지연 시간(end-to-end inference latency)을 줄입니다.

## 핵심 내용
Vision-language-action (VLA) 모델은 일반적으로 고유 감각(proprioception)을 단순히 후기 조건화 신호(late conditioning signal)로만 주입하여, 로봇 상태가 명령 이해를 근거하거나 시각적 주의를 유도하지 못하게 합니다. 우리는 ThinkProprio를 소개합니다. 이는 고유 감각을 VLM 어휘 토큰(VLM-vocabulary tokens)으로 이산화하고, 이를 명령과 함께 사용하여 VLM 계산 전에 시각 패치를 게이팅(gating)함으로써, 모델이 행동 관련 증거에 집중하고 중복 토큰을 조기에 폐기하도록 유도합니다. 우리는 고유 감각이 수동적 조건화 신호로 추가될 때 성능이 거의 변하지 않음을 발견했습니다. 그 가치는 토큰 형태의 상태가 명령과 함께 VLM이 처리할 시각 패치를 선택하는 능동적 질의(active query)로 작용할 때 나타납니다. 체계적 절제 실험(systematic ablations)은 VLM 어휘 토큰이 학습된 프로젝터(learned projectors)보다 상태 인코딩으로 더 우수하며, 시각 토큰의 약 \SI{12}{\percent}만 유지해도 CALVIN ABC$\to$D에서 더 나은 성능을 보임을 입증합니다. CALVIN, LIBERO 및 실제 세계 조작 작업에서 ThinkProprio는 일치하는 전체 토큰 기준선(matched full-token baseline)을 개선하면서 종단 간 추론 지연 시간(end-to-end inference latency)을 줄입니다.
